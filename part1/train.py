"""Training script for REINFORCE and Actor-Critic variants on Hopper-v4.

Usage examples:
    python train.py --algorithm reinforce --episodes 2000 --seed 1
    python train.py --algorithm ac_td --episodes 2000 --seed 1 --critic-lr 1e-3
"""
import argparse
import csv
import inspect
import json
import os
import time

import gymnasium as gym
import numpy as np
import torch
import torch.nn.functional as F

from agent import Policy, Agent, VALID_ALGORITHMS


# ------------------------------------------------------------------
#  Evaluation helper
# ------------------------------------------------------------------

def evaluate_agent(agent, env_name, num_episodes, base_seed):
    """Run deterministic evaluation rollouts.

    Each episode is seeded as ``base_seed + ep_idx`` so that the
    evaluation distribution is reproducible and std is meaningful.
    """
    env = gym.make(env_name)
    returns, lengths = [], []

    for i in range(num_episodes):
        state, _ = env.reset(seed=base_seed + i)
        done = False
        ep_return = 0.0
        ep_length = 0

        while not done:
            action, _ = agent.get_action(state, evaluation=True)
            action = action.detach().cpu().numpy()
            state, reward, terminated, truncated, _ = env.step(action)
            ep_return += reward
            ep_length += 1
            done = terminated or truncated

        returns.append(ep_return)
        lengths.append(ep_length)

    env.close()
    return np.mean(returns), np.std(returns), np.mean(lengths)


# ------------------------------------------------------------------
#  Best-checkpoint helpers
# ------------------------------------------------------------------

def _smoothed_eval_max(eval_means, eval_eps, window=5):
    """Max of a centred moving-average over the eval curve.

    Returns (smoothed_best_value, episode_of_smoothed_best). Falls back to
    raw max when fewer than `window` checkpoints exist. This is the signal
    used for `model_best.pt` saves — guards against checkpointing a single
    lucky 10-rollout eval spike.
    """
    n = len(eval_means)
    if n == 0:
        return None, None
    arr = np.asarray(eval_means, dtype=float)
    eps = np.asarray(eval_eps, dtype=int)
    if n < window:
        idx = int(np.argmax(arr))
        return float(arr[idx]), int(eps[idx])
    smoothed = np.convolve(arr, np.ones(window) / window, mode='valid')
    idx = int(np.argmax(smoothed))
    # Centre the reported episode on the window
    return float(smoothed[idx]), int(eps[idx + window // 2])


def _topk_eval_mean(eval_means, k=5):
    """Mean of the top-K eval checkpoints — less biased than single max."""
    if not eval_means:
        return None
    k = min(k, len(eval_means))
    return float(np.sort(np.asarray(eval_means, dtype=float))[-k:].mean())


def write_seed_summary(out_dir, eval_means, eval_eps, total_episodes,
                       wall_time_s, smooth_window=5, topk=5, final_k=5):
    """Write per-seed summary.json with raw / smoothed / top-K / final-K stats."""
    if not eval_means:
        summary = {
            'total_episodes': total_episodes,
            'wall_time_s': round(wall_time_s, 1),
            'n_eval_checkpoints': 0,
            'best_eval_mean': None, 'best_eval_episode': None,
            'smoothed_best_eval': None, 'smoothed_best_episode': None,
            'topk_eval_mean': None, 'topk_k': topk,
            'final_eval_mean': None, 'final_k': final_k,
            'smoothing_window': smooth_window,
        }
    else:
        arr = np.asarray(eval_means, dtype=float)
        raw_idx = int(np.argmax(arr))
        smoothed_best, smoothed_ep = _smoothed_eval_max(
            eval_means, eval_eps, window=smooth_window)
        fk = min(final_k, len(arr))
        summary = {
            'total_episodes': total_episodes,
            'wall_time_s': round(wall_time_s, 1),
            'n_eval_checkpoints': len(arr),
            'best_eval_mean': round(float(arr[raw_idx]), 2),
            'best_eval_episode': int(eval_eps[raw_idx]),
            'smoothed_best_eval': (round(smoothed_best, 2)
                                   if smoothed_best is not None else None),
            'smoothed_best_episode': smoothed_ep,
            'smoothing_window': smooth_window,
            'topk_eval_mean': round(_topk_eval_mean(eval_means, topk), 2),
            'topk_k': topk,
            'final_eval_mean': round(float(arr[-fk:].mean()), 2),
            'final_k': fk,
        }
    with open(os.path.join(out_dir, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)
    return summary


# ------------------------------------------------------------------
#  LR schedule helper
# ------------------------------------------------------------------

def make_schedulers(actor_optimizer, critic_optimizer, schedule, total_updates):
    """Return (actor_sched, critic_sched) or (None, None) for 'none'.

    Both schedules decay to 10% of initial LR over `total_updates` steps,
    matched on the same floor so the two are directly comparable.

    Decay is per-update-call (= per episode when update_every=1), NOT per
    env-step. Variable-length episodes mean early (short) episodes consume
    the same decay budget as late (long) ones — flag this in the writeup.
    """
    if schedule == 'none' or total_updates <= 0:
        return None, None

    def _make(opt):
        if opt is None:
            return None
        if schedule == 'linear':
            return torch.optim.lr_scheduler.LinearLR(
                opt, start_factor=1.0, end_factor=0.1,
                total_iters=total_updates)
        if schedule == 'cosine':
            base_lr = opt.param_groups[0]['lr']
            return torch.optim.lr_scheduler.CosineAnnealingLR(
                opt, T_max=total_updates, eta_min=base_lr * 0.1)
        raise ValueError(f'Unknown lr_schedule: {schedule!r}')

    return _make(actor_optimizer), _make(critic_optimizer)


# ------------------------------------------------------------------
#  Main
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Train policy-gradient variants on Hopper-v4')
    parser.add_argument('--algorithm', type=str, default='reinforce',
                        choices=VALID_ALGORITHMS,
                        help='Policy-gradient variant to train')
    parser.add_argument('--episodes', type=int, default=3000,
                        help='Total training episodes')
    parser.add_argument('--gamma', type=float, default=0.99,
                        help='Discount factor')
    parser.add_argument('--lr', type=float, default=None,
                        help='Actor learning rate (default: 3e-4 for ac_mc/ac_td, 1e-3 for REINFORCE variants)')
    parser.add_argument('--critic-lr', type=float, default=1e-3,
                        help='Critic learning rate (AC variants only)')
    parser.add_argument('--ema-alpha', type=float, default=0.05,
                        help='EMA smoothing factor for reinforce_ema baseline')
    parser.add_argument('--fixed-baseline', type=float, default=20.0,
                        help='Constant baseline value for reinforce_fixed')
    parser.add_argument('--seed', type=int, default=1,
                        help='Random seed')
    parser.add_argument('--print-every', type=int, default=50,
                        help='Console print interval (episodes)')
    parser.add_argument('--eval-every', type=int, default=50,
                        help='Evaluation interval (episodes)')
    parser.add_argument('--eval-episodes', type=int, default=10,
                        help='Number of evaluation episodes')
    _default_results = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    parser.add_argument('--results-dir', type=str, default=_default_results,
                        help='Base output directory (default: part1/results/)')
    parser.add_argument('--update-every', type=int, default=1,
                        help='Accumulate this many episodes before each gradient update (default: 1 = per-episode)')
    parser.add_argument('--lr-schedule', type=str, default='none',
                        choices=['none', 'linear', 'cosine'],
                        help='Per-update LR schedule. "linear"/"cosine" decay to 10%% of initial '
                             'LR over the run. Stepped per update (per-episode when '
                             'update_every=1), so variable episode lengths consume the decay '
                             'budget unevenly — caveat in writeup.')
    parser.add_argument('--smooth-window', type=int, default=5,
                        help='Checkpoint window for smoothed-best eval (also gates model_best.pt saves)')
    parser.add_argument('--topk', type=int, default=5,
                        help='K for top-K eval mean in summary.json')
    parser.add_argument('--final-k', type=int, default=5,
                        help='K trailing checkpoints averaged for final_eval_mean')
    parser.add_argument('--render', action='store_true',
                        help='Render training episodes')
    parser.add_argument('--no-standardize', action='store_true',
                        help='Disable return/advantage standardization (or scaling) entirely')
    args = parser.parse_args()

    # Apply algorithm-specific LR default when not explicitly passed
    if args.lr is None:
        args.lr = 3e-4 if args.algorithm in ('ac_mc', 'ac_td') else 1e-3

    # ---- output directory ----
    # Schedule tag is empty for 'none' so existing runs keep their layout.
    schedule_tag = '' if args.lr_schedule == 'none' else f'_sched{args.lr_schedule}'
    out_dir = os.path.join(args.results_dir, args.algorithm,
                           f'lr{args.lr}_upd{args.update_every}{schedule_tag}',
                           f'seed_{args.seed}')
    os.makedirs(out_dir, exist_ok=True)

    # ---- save full CLI config for reproducibility ----
    with open(os.path.join(out_dir, 'config.json'), 'w') as f:
        json.dump(vars(args), f, indent=2)

    # ---- seeding ----
    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    # ---- environment ----
    render_mode = 'human' if args.render else None
    env = gym.make('Hopper-v4', render_mode=render_mode)

    state_space = env.observation_space.shape[0]   # 11
    action_space = env.action_space.shape[0]       # 3

    # ---- policy & agent ----
    policy = Policy(state_space, action_space)
    agent = Agent(
        policy,
        algorithm=args.algorithm,
        device=device,
        lr=args.lr,
        critic_lr=args.critic_lr,
        gamma=args.gamma,
        ema_alpha=args.ema_alpha,
        fixed_baseline=args.fixed_baseline,
        standardize=not args.no_standardize
    )
    # Prevent provenance hazards: assert the agent has the correct 6-arg store_outcome signature.
    # Older intermediate agent.py generations had a 5-arg signature and will crash here.
    assert len(inspect.signature(agent.store_outcome).parameters) >= 6, \
        "Stale agent.py detected: store_outcome must accept at least 6 arguments (including self). Please ensure you are using the final agent.py version."

    # ---- LR schedulers (per-update; see --lr-schedule help for caveat) ----
    num_updates = args.episodes // args.update_every
    actor_scheduler, critic_scheduler = make_schedulers(
        agent.actor_optimizer, agent.critic_optimizer,
        args.lr_schedule, num_updates)

    # ---- CSV loggers ----
    # actor_lr / critic_lr columns let you sanity-check the schedule from the log.
    log_fields = ['episode', 'return', 'length', 'wall_time', 'sigma_mean',
                  'actor_loss', 'critic_loss', 'baseline',
                  'mean_value', 'mean_td_error', 'actor_lr', 'critic_lr']
    log_file = open(os.path.join(out_dir, 'log.csv'), 'w', newline='')
    log_writer = csv.DictWriter(log_file, fieldnames=log_fields)
    log_writer.writeheader()

    eval_fields = ['episode_checkpoint', 'eval_mean_return',
                   'eval_std_return', 'eval_mean_length']
    eval_file = open(os.path.join(out_dir, 'eval_log.csv'), 'w', newline='')
    eval_writer = csv.DictWriter(eval_file, fieldnames=eval_fields)
    eval_writer.writeheader()

    # ---- training loop ----
    start_time = time.time()

    # Best-checkpoint tracking: fire model_best.pt on the *smoothed* eval,
    # not the raw max. A single 10-rollout eval can spike on noise alone;
    # the moving-average max is a more defensible "best stable region" signal.
    # Raw best, top-K, and final-K are still written to summary.json.
    best_smoothed_eval = -float('inf')
    eval_means_hist = []   # list of eval_mean values, in order
    eval_eps_hist = []     # corresponding episode checkpoints

    for ep in range(1, args.episodes + 1):
        # Seed the env on the first episode for reproducibility;
        # subsequent resets use the env's internal RNG.
        if ep == 1:
            state, _ = env.reset(seed=args.seed)
        else:
            state, _ = env.reset()

        done = False
        ep_return = 0.0
        ep_length = 0

        while not done:
            action, log_prob = agent.get_action(state)
            next_state, reward, terminated, truncated, _ = env.step(
                action.detach().cpu().numpy())

            # store_outcome receives both terminated (MDP-only, for TD
            # bootstrap) and episode_done (terminated|truncated, for
            # discount_rewards episode boundary reset).
            agent.store_outcome(state, next_state, log_prob, reward,
                                terminated, terminated or truncated)

            state = next_state
            ep_return += reward
            ep_length += 1
            done = terminated or truncated

        # Read LR before the scheduler step so the logged value matches what
        # was actually used in this episode's gradient update.
        actor_lr = agent.actor_optimizer.param_groups[0]['lr']
        critic_lr = (agent.critic_optimizer.param_groups[0]['lr']
                     if agent.critic_optimizer is not None else None)

        # ---- end of episode: update policy every N episodes ----
        if ep % args.update_every == 0:
            metrics = agent.update_policy()
            if actor_scheduler is not None:
                actor_scheduler.step()
            if critic_scheduler is not None:
                critic_scheduler.step()
        else:
            metrics = {'actor_loss': None, 'critic_loss': None,
                       'baseline': None, 'mean_value': None, 'mean_td_error': None}

        sigma_mean = F.softplus(policy.sigma).mean().item()
        wall_time = time.time() - start_time

        # ---- write training log row ----
        row = {
            'episode': ep,
            'return': round(ep_return, 2),
            'length': ep_length,
            'wall_time': round(wall_time, 2),
            'sigma_mean': round(sigma_mean, 6),
            'actor_loss': (round(metrics['actor_loss'], 6)
                           if metrics['actor_loss'] is not None else ''),
            'critic_loss': (round(metrics['critic_loss'], 6)
                            if metrics['critic_loss'] is not None else ''),
            'baseline': (round(metrics['baseline'], 6)
                         if metrics['baseline'] is not None else ''),
            'mean_value': (round(metrics['mean_value'], 6)
                           if metrics['mean_value'] is not None else ''),
            'mean_td_error': (round(metrics['mean_td_error'], 6)
                              if metrics['mean_td_error'] is not None else ''),
            'actor_lr': round(actor_lr, 8),
            'critic_lr': round(critic_lr, 8) if critic_lr is not None else '',
        }
        log_writer.writerow(row)
        log_file.flush()

        # ---- console output ----
        if ep % args.print_every == 0:
            print(f"Ep {ep:>5}/{args.episodes} | "
                  f"R {ep_return:>8.1f} | "
                  f"Len {ep_length:>4} | "
                  f"sig {sigma_mean:.4f} | "
                  f"Wall {wall_time:>7.1f}s")

        # ---- periodic evaluation ----
        if ep % args.eval_every == 0:
            eval_mean, eval_std, eval_len = evaluate_agent(
                agent, 'Hopper-v4', args.eval_episodes,
                base_seed=args.seed + 100_000)  # offset to avoid overlap with training seeds
            eval_writer.writerow({
                'episode_checkpoint': ep,
                'eval_mean_return': round(eval_mean, 2),
                'eval_std_return': round(eval_std, 2),
                'eval_mean_length': round(eval_len, 1),
            })
            eval_file.flush()
            eval_means_hist.append(float(eval_mean))
            eval_eps_hist.append(ep)

            # Save model_best.pt when the smoothed eval signal sets a new high.
            # For the first (smooth_window - 1) checkpoints _smoothed_eval_max
            # falls back to raw max, so the trigger still fires early.
            current_smoothed, _ = _smoothed_eval_max(
                eval_means_hist, eval_eps_hist, window=args.smooth_window)
            if current_smoothed is not None and current_smoothed > best_smoothed_eval:
                best_smoothed_eval = current_smoothed
                torch.save({
                    'policy_state_dict': policy.state_dict(),
                    'algorithm': args.algorithm,
                    'episode': ep,
                    'obs_dim': state_space,
                    'act_dim': action_space,
                    'smoothed_eval': round(current_smoothed, 2),
                    'raw_eval': round(float(eval_mean), 2),
                }, os.path.join(out_dir, 'model_best.pt'))

            print(f"       [Eval] Mean {eval_mean:>8.1f} ± {eval_std:.1f} | "
                  f"Len {eval_len:.0f} | "
                  f"SmoothedBest {best_smoothed_eval:.1f}")

    # ---- save final model ----
    torch.save({
        'policy_state_dict': policy.state_dict(),
        'algorithm': args.algorithm,
        'episode': args.episodes,
        'obs_dim': state_space,
        'act_dim': action_space,
    }, os.path.join(out_dir, 'model.pt'))

    # ---- per-seed summary (raw / smoothed / top-K / final-K) ----
    # `best_eval_mean` is the raw max of 10-rollout eval means — positively
    # biased by eval-noise; lead the writeup with `smoothed_best_eval` and
    # `topk_eval_mean` instead. All four are written so you can compare.
    seed_summary = write_seed_summary(
        out_dir,
        eval_means=eval_means_hist,
        eval_eps=eval_eps_hist,
        total_episodes=args.episodes,
        wall_time_s=time.time() - start_time,
        smooth_window=args.smooth_window,
        topk=args.topk,
        final_k=args.final_k,
    )

    log_file.close()
    eval_file.close()
    env.close()

    print(f"\nTraining complete. Results saved to {out_dir}")
    print(f"  smoothed_best_eval: {seed_summary.get('smoothed_best_eval')} "
          f"at ep {seed_summary.get('smoothed_best_episode')}")
    print(f"  best_eval (raw):    {seed_summary.get('best_eval_mean')} "
          f"at ep {seed_summary.get('best_eval_episode')}")
    print(f"  top-{args.topk} mean:         {seed_summary.get('topk_eval_mean')}")
    print(f"  final-{args.final_k} mean:       {seed_summary.get('final_eval_mean')}")


if __name__ == '__main__':
    main()
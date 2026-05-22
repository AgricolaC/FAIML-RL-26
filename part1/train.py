"""Training script for REINFORCE and Actor-Critic variants on Hopper-v4.

Usage examples:
    python train.py --algorithm reinforce --episodes 2000 --seed 1
    python train.py --algorithm ac_td --episodes 2000 --seed 1 --critic-lr 1e-3
"""
import argparse
import csv
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
#  Main
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Train policy-gradient variants on Hopper-v4')
    parser.add_argument('--algorithm', type=str, default='reinforce',
                        choices=VALID_ALGORITHMS,
                        help='Policy-gradient variant to train')
    parser.add_argument('--episodes', type=int, default=2000,
                        help='Total training episodes')
    parser.add_argument('--gamma', type=float, default=0.99,
                        help='Discount factor')
    parser.add_argument('--lr', type=float, default=None,
                        help='Actor learning rate (default: 3e-4 for ac_mc/ac_td, 1e-3 for REINFORCE variants)')
    parser.add_argument('--critic-lr', type=float, default=3e-3,
                        help='Critic learning rate (AC variants only)')
    parser.add_argument('--ema-alpha', type=float, default=0.05,
                        help='EMA smoothing factor for reinforce_ema baseline')
    parser.add_argument('--fixed-baseline', type=float, default=20.0,
                        help='Constant baseline value for reinforce_fixed')
    parser.add_argument('--seed', type=int, default=1,
                        help='Random seed')
    parser.add_argument('--print-every', type=int, default=20,
                        help='Console print interval (episodes)')
    parser.add_argument('--eval-every', type=int, default=100,
                        help='Evaluation interval (episodes)')
    parser.add_argument('--eval-episodes', type=int, default=10,
                        help='Number of evaluation episodes')
    _default_results = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results')
    parser.add_argument('--results-dir', type=str, default=_default_results,
                        help='Base output directory (default: part1/results/)')
    parser.add_argument('--update-every', type=int, default=1,
                        help='Accumulate this many episodes before each gradient update (default: 1 = per-episode)')
    parser.add_argument('--render', action='store_true',
                        help='Render training episodes')
    args = parser.parse_args()

    # Apply algorithm-specific LR default when not explicitly passed
    if args.lr is None:
        args.lr = 3e-4 if args.algorithm in ('ac_mc', 'ac_td') else 1e-3

    # ---- output directory ----
    out_dir = os.path.join(args.results_dir, args.algorithm,
                           f'lr{args.lr}_upd{args.update_every}',
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
    agent = Agent(policy,
                  algorithm=args.algorithm,
                  lr=args.lr,
                  critic_lr=args.critic_lr,
                  gamma=args.gamma,
                  ema_alpha=args.ema_alpha,
                  fixed_baseline=args.fixed_baseline)

    # ---- CSV loggers ----
    log_fields = ['episode', 'return', 'length', 'wall_time', 'sigma_mean',
                  'actor_loss', 'critic_loss', 'baseline',
                  'mean_value', 'mean_td_error']
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

        # ---- end of episode: update policy every N episodes ----
        if ep % args.update_every == 0:
            metrics = agent.update_policy()
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
            print(f"       [Eval] Mean {eval_mean:>8.1f} ± {eval_std:.1f} | "
                  f"Len {eval_len:.0f}")

    # ---- save final model ----
    torch.save({
        'policy_state_dict': policy.state_dict(),
        'algorithm': args.algorithm,
        'episode': args.episodes,
        'obs_dim': state_space,
        'act_dim': action_space,
    }, os.path.join(out_dir, 'model.pt'))

    log_file.close()
    eval_file.close()
    env.close()

    print(f"\nTraining complete. Results saved to {out_dir}")


if __name__ == '__main__':
    main()
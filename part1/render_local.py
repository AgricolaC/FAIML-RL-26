"""Render trained checkpoints from Part 1 (Hopper-v4) or Part 2 (PandaPush-v3).

Usage examples:
    python render_local.py --checkpoint results/ac_td/seed_1/model.pt
    python render_local.py --checkpoint results/reinforce_ema/seed_1/model.pt --episodes 3 --save-video videos/
    python render_local.py --checkpoint results/ac_td/seed_1/model.pt --compare results/reinforce_ema/seed_1/model.pt --no-render
    python render_local.py --checkpoint results/sac_source_none.zip --env-type source
    python render_local.py --checkpoint results/sac_source_none.zip --env-type target
    python render_local.py --checkpoint results/sac_source_udr.zip --env-type target --episodes 5 --save-video videos/udr_target/
"""
import argparse
import os
import sys
import time

import numpy as np

# Allow imports from the part1 directory regardless of cwd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Make the part2 directory importable for panda_gym
_part2_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'part2')
sys.path.insert(0, os.path.abspath(_part2_dir))


# ---------------------------------------------------------------------------
# Part 1 helpers
# ---------------------------------------------------------------------------

def _resolve_checkpoint(path, prefer_best):
    """Resolve the actual checkpoint file to load.

    If `prefer_best` is True and `model_best.pt` exists in the same directory
    as `path`, return that instead. Falls back silently to `path` if not found.
    """
    if not prefer_best:
        return path
    candidate = os.path.join(os.path.dirname(os.path.abspath(path)), 'model_best.pt')
    if os.path.exists(candidate):
        print(f"[render] Using model_best.pt (pass --no-best to use {os.path.basename(path)})")
        return candidate
    return path


def _load_part1(checkpoint_path):
    import torch
    from agent import Policy, Agent

    checkpoint = torch.load(checkpoint_path, map_location='cpu', weights_only=False)
    obs_dim = checkpoint['obs_dim']
    act_dim = checkpoint['act_dim']
    algorithm = checkpoint['algorithm']
    trained_ep = checkpoint.get('episode', '?')

    extra = ''
    if 'smoothed_eval' in checkpoint:
        extra = (f", smoothed_eval={checkpoint['smoothed_eval']:.1f}"
                 f", raw_eval={checkpoint['raw_eval']:.1f}")
    print(f"[Part1] Loaded: algorithm={algorithm}, "
          f"trained_episodes={trained_ep}, obs_dim={obs_dim}, act_dim={act_dim}{extra}")

    policy = Policy(obs_dim, act_dim)
    policy.load_state_dict(checkpoint['policy_state_dict'])
    policy.eval()

    agent = Agent(policy, algorithm=algorithm)
    return agent, {'algorithm': algorithm, 'obs_dim': obs_dim, 'act_dim': act_dim,
                   'episode': trained_ep}


def _make_hopper_env(render, save_video_dir):
    import gymnasium as gym

    if save_video_dir:
        os.makedirs(save_video_dir, exist_ok=True)
        env = gym.make('Hopper-v4', render_mode='rgb_array')
        env = gym.wrappers.RecordVideo(env, save_video_dir,
                                       episode_trigger=lambda _: True)
    elif render:
        env = gym.make('Hopper-v4', render_mode='human')
    else:
        env = gym.make('Hopper-v4')
    return env


def _run_part1_episodes(agent, env, n_episodes, seed, slow, render):
    returns, lengths = [], []

    for i in range(n_episodes):
        state, _ = env.reset(seed=seed + i)
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
            if slow and render:
                time.sleep(1 / 30)

        returns.append(ep_return)
        lengths.append(ep_length)
        print(f"Episode {i+1:>3} | return={ep_return:>8.1f} | length={ep_length}")

    return returns, lengths


def run_part1(args, checkpoint_path=None, suppress_print=False):
    raw_path = checkpoint_path or args.checkpoint
    path = _resolve_checkpoint(raw_path, getattr(args, 'use_best', True))
    agent, meta = _load_part1(path)

    render = args.render and not args.save_video
    env = _make_hopper_env(render, args.save_video)

    returns, lengths = _run_part1_episodes(
        agent, env, args.episodes, args.seed, args.slow, render)
    env.close()

    if not suppress_print:
        print(f"\n{'='*55}")
        print(f"Mean return : {np.mean(returns):>8.1f} ± {np.std(returns):.1f}")
        print(f"Mean length : {np.mean(lengths):>8.1f}")
        print(f"{'='*55}")

    if args.save_video and getattr(args, 'keep_best_only', False) and returns:
        best_idx = int(np.argmax(returns))
        import glob
        
        # 1. Rename the best episode
        for f in glob.glob(os.path.join(args.save_video, f'rl-video-episode-{best_idx}.*')):
            if f.endswith('.mp4') or f.endswith('.meta.json'):
                new_name = f.replace(f"rl-video-episode-{best_idx}", "best_episode")
                try:
                    os.replace(f, new_name)
                except OSError:
                    pass
                    
        # 2. Delete all other videos and meta files
        for ext in ('*.mp4', '*.meta.json'):
            for f in glob.glob(os.path.join(args.save_video, ext)):
                if not (f.endswith('best_episode.mp4') or f.endswith('best_episode.meta.json')):
                    try:
                        os.remove(f)
                    except OSError:
                        pass

    return returns, lengths, meta


# ---------------------------------------------------------------------------
# Part 2 helpers
# ---------------------------------------------------------------------------

def _load_part2(checkpoint_path, env):
    try:
        from stable_baselines3 import SAC
        model = SAC.load(checkpoint_path, env=env)
        algo_name = 'SAC'
    except Exception:
        from stable_baselines3 import PPO
        model = PPO.load(checkpoint_path, env=env)
        algo_name = 'PPO'

    print(f"[Part2] Loaded: algorithm={algo_name}, checkpoint={checkpoint_path}")
    return model, {'algorithm': algo_name}


def _make_panda_env(env_type, render, save_video_dir):
    import gymnasium as gym
    try:
        import panda_gym  # noqa: F401
    except ImportError:
        pass

    mode = 'rgb_array' if (save_video_dir or not render) else 'human'
    env = gym.make('PandaPush-v3', render_mode=mode,
                   type=env_type, reward_type='dense')

    if save_video_dir:
        os.makedirs(save_video_dir, exist_ok=True)
        env = __import__('gymnasium').wrappers.RecordVideo(
            env, save_video_dir, episode_trigger=lambda _: True)

    return env


def _run_part2_episodes(model, env, n_episodes, seed, slow, render):
    returns, lengths, successes = [], [], []

    for i in range(n_episodes):
        obs, _ = env.reset(seed=seed + i)
        done = False
        ep_return = 0.0
        ep_length = 0
        success = False

        while not done:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(action)
            ep_return += float(reward)
            ep_length += 1
            done = terminated or truncated
            if slow and render:
                time.sleep(1 / 30)

        if isinstance(info, dict):
            success = bool(info.get('is_success', False))

        returns.append(ep_return)
        lengths.append(ep_length)
        successes.append(float(success))
        print(f"Episode {i+1:>3} | return={ep_return:>8.3f} | "
              f"length={ep_length} | success={success}")

    return returns, lengths, successes


def run_part2(args, checkpoint_path=None, suppress_print=False):
    path = checkpoint_path or args.checkpoint
    env_type = getattr(args, 'env_type', 'source')

    render = args.render and not args.save_video
    env = _make_panda_env(env_type, render, args.save_video)
    model, meta = _load_part2(path, env)

    returns, lengths, successes = _run_part2_episodes(
        model, env, args.episodes, args.seed, args.slow, render)
    env.close()

    if not suppress_print:
        print(f"\n{'='*55}")
        print(f"Mean return  : {np.mean(returns):>8.3f} ± {np.std(returns):.3f}")
        print(f"Mean length  : {np.mean(lengths):>8.1f}")
        print(f"Success rate : {np.mean(successes):.1%}")
        print(f"{'='*55}")

    if args.save_video and getattr(args, 'keep_best_only', False) and returns:
        best_idx = int(np.argmax(returns))
        import glob
        
        # 1. Rename the best episode
        for f in glob.glob(os.path.join(args.save_video, f'rl-video-episode-{best_idx}.*')):
            if f.endswith('.mp4') or f.endswith('.meta.json'):
                new_name = f.replace(f"rl-video-episode-{best_idx}", "best_episode")
                try:
                    os.replace(f, new_name)
                except OSError:
                    pass
                    
        # 2. Delete all other videos and meta files
        for ext in ('*.mp4', '*.meta.json'):
            for f in glob.glob(os.path.join(args.save_video, ext)):
                if not (f.endswith('best_episode.mp4') or f.endswith('best_episode.meta.json')):
                    try:
                        os.remove(f)
                    except OSError:
                        pass

    return returns, lengths, meta


# ---------------------------------------------------------------------------
# Compare mode
# ---------------------------------------------------------------------------

def run_compare(args):
    ckpt_a = args.checkpoint
    ckpt_b = args.compare
    ext_a = os.path.splitext(ckpt_a)[1].lower()
    ext_b = os.path.splitext(ckpt_b)[1].lower()

    if ext_a != ext_b:
        print("ERROR: --compare checkpoints must be the same type (.pt or .zip)")
        sys.exit(1)

    args_no_render = argparse.Namespace(**vars(args))
    args_no_render.render = False
    args_no_render.save_video = None

    print(f"\n--- Running checkpoint A: {ckpt_a} ---")
    if ext_a == '.pt':
        ret_a, len_a, meta_a = run_part1(args_no_render, ckpt_a, suppress_print=True)
    else:
        ret_a, len_a, meta_a = run_part2(args_no_render, ckpt_a, suppress_print=True)

    print(f"\n--- Running checkpoint B: {ckpt_b} ---")
    if ext_b == '.pt':
        ret_b, len_b, meta_b = run_part1(args_no_render, ckpt_b, suppress_print=True)
    else:
        ret_b, len_b, meta_b = run_part2(args_no_render, ckpt_b, suppress_print=True)

    col = 22
    print(f"\n{'='*55}")
    print(f"{'=== Comparison ===':^55}")
    print(f"{'='*55}")
    print(f"{'':20s} {'Checkpoint A':<{col}} {'Checkpoint B':<{col}}")
    print(f"{'Algorithm':<20} {meta_a['algorithm']:<{col}} {meta_b['algorithm']:<{col}}")
    print(f"{'Mean return':<20} "
          f"{np.mean(ret_a):>6.1f} ± {np.std(ret_a):<5.1f}   "
          f"{np.mean(ret_b):>6.1f} ± {np.std(ret_b):<5.1f}")
    print(f"{'Mean length':<20} {np.mean(len_a):<{col}.1f} {np.mean(len_b):<{col}.1f}")
    print(f"{'='*55}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description='Render / compare trained RL checkpoints (Part 1 & 2)')
    parser.add_argument('--checkpoint', type=str, required=True,
                        help='Path to .pt (Part 1) or .zip (Part 2) checkpoint')
    parser.add_argument('--episodes', type=int, default=5,
                        help='Number of episodes to render (default: 5)')
    parser.add_argument('--seed', type=int, default=42,
                        help='Base random seed (default: 42)')
    parser.add_argument('--render', action='store_true', default=True,
                        help='Show live window (default: True)')
    parser.add_argument('--no-render', dest='render', action='store_false',
                        help='Suppress live rendering')
    parser.add_argument('--save-video', type=str, default=None,
                        help='Directory to save MP4 files via RecordVideo')
    parser.add_argument('--env-type', type=str, default='source',
                        choices=['source', 'target'],
                        help='Part 2 only: source or target env (default: source)')
    parser.add_argument('--compare', type=str, default=None,
                        help='Second checkpoint for side-by-side text comparison')
    parser.add_argument('--slow', action='store_true',
                        help='Add ~33ms delay between frames for slower playback')
    parser.add_argument('--use-best', dest='use_best', action='store_true', default=True,
                        help='Load model_best.pt from the same directory if it exists (default: on)')
    parser.add_argument('--no-best', dest='use_best', action='store_false',
                        help='Load exactly the specified checkpoint, ignoring model_best.pt')
    parser.add_argument('--keep-best-only', action='store_true',
                        help='If saving video, keep only the episode with the highest return')
    return parser.parse_args()


def main():
    args = parse_args()

    if args.compare:
        run_compare(args)
        return

    ext = os.path.splitext(args.checkpoint)[1].lower()
    if ext == '.pt':
        run_part1(args)
    elif ext == '.zip':
        run_part2(args)
    else:
        print(f"ERROR: Unknown checkpoint extension '{ext}'. Expected .pt or .zip.")
        sys.exit(1)


if __name__ == '__main__':
    main()

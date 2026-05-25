"""Evaluate a trained Hopper-v4 policy from a checkpoint.

Usage:
    python evaluate.py --model-path results/reinforce/seed_1/model.pt --episodes 10
    python evaluate.py --model-path results/ac_td/seed_1/model.pt --render
    python evaluate.py --model-path results/ac_mc/seed_1/model.pt --record-video videos/
"""
import argparse

import gymnasium as gym
import numpy as np
import torch

from agent import Policy, Agent


def main():
    parser = argparse.ArgumentParser(
        description='Evaluate a trained Hopper-v4 policy')
    parser.add_argument('--model-path', type=str, required=True,
                        help='Path to saved model.pt checkpoint')
    parser.add_argument('--episodes', type=int, default=10,
                        help='Number of evaluation episodes')
    parser.add_argument('--seed', type=int, default=42,
                        help='Base seed (each episode uses seed + ep_idx)')
    parser.add_argument('--render', action='store_true',
                        help='Render episodes in a window')
    parser.add_argument('--record-video', type=str, default=None,
                        help='Directory to save episode videos (mp4)')
    args = parser.parse_args()

    # ---- load checkpoint ----
    checkpoint = torch.load(args.model_path, map_location='cpu',
                            weights_only=False)

    obs_dim = checkpoint['obs_dim']
    act_dim = checkpoint['act_dim']
    algorithm = checkpoint['algorithm']
    trained_episodes = checkpoint.get('episode', '?')

    print(f"Loaded checkpoint: algorithm={algorithm}, "
          f"trained for {trained_episodes} episodes, "
          f"obs_dim={obs_dim}, act_dim={act_dim}")

    # ---- reconstruct policy ----
    policy = Policy(obs_dim, act_dim)
    policy.load_state_dict(checkpoint['policy_state_dict'])
    policy.eval()

    agent = Agent(policy, algorithm=algorithm)

    # ---- environment ----
    if args.record_video:
        env = gym.make('Hopper-v4', render_mode='rgb_array')
        env = gym.wrappers.RecordVideo(env, args.record_video,
                                       episode_trigger=lambda _: True)
    elif args.render:
        env = gym.make('Hopper-v4', render_mode='human')
    else:
        env = gym.make('Hopper-v4')

    returns, lengths = [], []

    for i in range(args.episodes):
        state, _ = env.reset(seed=args.seed + 100_000 + i)
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
        print(f"  Episode {i+1:>3}/{args.episodes}:  "
              f"Return = {ep_return:>8.1f}   Length = {ep_length}")

    env.close()

    print(f"\n{'='*50}")
    print(f"Results over {args.episodes} episodes:")
    print(f"  Mean Return : {np.mean(returns):>8.1f} ± {np.std(returns):.1f}")
    print(f"  Mean Length : {np.mean(lengths):>8.1f}")
    print(f"{'='*50}")


if __name__ == '__main__':
    main()

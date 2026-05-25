import argparse
import os

import gymnasium as gym
import numpy as np
import panda_gym  # noqa: F401
from gymnasium.wrappers import RecordVideo
from stable_baselines3 import PPO, SAC
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

def evaluate(model_path: str, algo: str, n_episodes: int, deterministic: bool, render: bool, record_video: bool, env_type: str) -> None:
    # Append .zip if not provided, stable-baselines3 uses zip files
    if not model_path.endswith('.zip') and os.path.exists(model_path + '.zip'):
        model_path += '.zip'
        
    if not os.path.exists(model_path):
        raise FileNotFoundError(
            f"Model file not found: {model_path}. "
            "Make sure you saved your trained model."
        )

    # Use rgb_array to allow RecordVideo to capture frames, or human for a live window.
    render_mode = "human" if render else "rgb_array"
    
    env = gym.make("PandaPush-v3", render_mode=render_mode, type=env_type, reward_type="dense")
    
    if record_video:
        video_dir = os.path.join("videos", f"{algo}_{env_type}")
        os.makedirs(video_dir, exist_ok=True)
        # Record every episode during evaluation
        env = RecordVideo(env, video_folder=video_dir, episode_trigger=lambda x: True)
    
    # We must wrap the env in a Monitor to use evaluate_policy correctly with dict observations
    env = Monitor(env)

    if algo.lower() == "ppo":
        model = PPO.load(model_path, env=env)
    elif algo.lower() == "sac":
        model = SAC.load(model_path, env=env)
    else:
        raise ValueError(f"Unknown algorithm: {algo}")

    print(f"\nEvaluating {algo.upper()} on {env_type} environment for {n_episodes} episodes...")

    # The assignment specifically asks to refer to the SB3 Evaluation Helper
    mean_reward, std_reward = evaluate_policy(
        model, 
        env, 
        n_eval_episodes=n_episodes, 
        deterministic=deterministic,
        return_episode_rewards=False
    )
    
    # Run a secondary manual loop just to compute the success rate, as evaluate_policy
    # doesn't natively expose the 'info' dict statistics like is_success.
    successes = []
    for _ in range(n_episodes):
        obs, _ = env.reset()
        done = False
        while not done:
            action, _ = model.predict(obs, deterministic=deterministic)
            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            if done and isinstance(info, dict) and "is_success" in info:
                successes.append(float(info["is_success"]))

    env.close()

    print("\n=== Evaluation summary ===")
    print(f"Episodes: {n_episodes}")
    print(f"Mean return: {mean_reward:.3f}")
    print(f"Std return:  {std_reward:.3f}")

    if successes:
        success_rate = float(np.mean(successes))
        print(f"Success rate: {success_rate:.2%}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate PPO/SAC on PandaPush-v3")
    parser.add_argument(
        "--model-path",
        type=str,
        required=True,
        help="Path to the model zip file (e.g., results/ppo_source_none_seed1/best_model.zip)",
    )
    parser.add_argument(
        "--algo",
        type=str,
        required=True,
        choices=["ppo", "sac"],
        help="RL algorithm used to train the model",
    )
    parser.add_argument(
        "--episodes", 
        type=int, 
        default=50, 
        help="Number of eval episodes (default: 50 as per rubric)"
    )
    parser.add_argument(
        "--stochastic",
        action="store_true",
        help="Use stochastic policy sampling instead of deterministic actions",
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="Render with a window (render_mode='human')",
    )
    parser.add_argument(
        "--record-video",
        action="store_true",
        help="Record and save MP4 videos of the evaluation episodes to the videos/ directory",
    )
    parser.add_argument(
        "--env-type",
        type=str, default="target",
        choices=["source", "target"],
        help="Type of environment to evaluate on (default: target)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    evaluate(
        model_path=args.model_path,
        algo=args.algo,
        n_episodes=args.episodes,
        deterministic=not args.stochastic,
        render=args.render,
        record_video=args.record_video,
        env_type=args.env_type,
    )

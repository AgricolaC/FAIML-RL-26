import argparse
import os
import gymnasium as gym
import panda_gym
from stable_baselines3 import PPO, SAC
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv, DummyVecEnv
from rand_wrapper import RandomizationWrapper # Will be implemented later

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train PPO/SAC on PandaPush-v3")
    parser.add_argument(
        "--algo",
        type=str,
        default="sac",
        choices=["ppo", "sac"],
        help="RL algorithm to use",
    )
    parser.add_argument(
        "--sampling-strategy",
        type=str,
        default="none",
        choices=["none", "udr", "adr"],
        help="Sampling strategy for the object mass",
    )
    parser.add_argument(
        "--env-type",
        type=str,
        default="source",
        choices=["source", "target"],
        help="PandaPush environment type",
    )
    parser.add_argument(
        "--timesteps",
        type=int,
        default=300_000,
        help="Number of training timesteps",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=1,
        help="Random seed",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    # Create training environment
    env_kwargs = {
        "render_mode": "rgb_array", # panda-gym requires 'rgb_array' or 'human'
        "type": args.env_type,
        "reward_type": "dense",
    }
    
    # Speed optimization for PPO: use 4 parallel environments
    if args.algo == "ppo":
        env = make_vec_env("PandaPush-v3", n_envs=4, env_kwargs=env_kwargs, vec_env_cls=SubprocVecEnv, seed=args.seed)
    else:
        env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)
    
    # Create evaluation environment (always evaluate on the same type as training for monitoring)
    eval_env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)

    # TODO: add randomization wrapper for UDR/ADR here (Phase 2)
    # Note: For VecEnvs, the wrapper should be applied inside the make_vec_env using `wrapper_class` argument
    # if args.sampling_strategy != "none":
    #     env_kwargs["strategy"] = args.sampling_strategy
    #     wrapper_class = RandomizationWrapper

    out_dir = f"results/{args.algo}_{args.env_type}_{args.sampling_strategy}_seed{args.seed}"
    os.makedirs(out_dir, exist_ok=True)

    # Setup evaluation callback
    eval_callback = EvalCallback(
        eval_env,
        best_model_save_path=out_dir,
        log_path=out_dir,
        eval_freq=10000 // (4 if args.algo == "ppo" else 1), # Adjust freq based on n_envs
        deterministic=True,
        render=False
    )

    if args.algo == "ppo":
        model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=f"runs/{args.algo}", seed=args.seed)
    else:
        model = SAC("MultiInputPolicy", env, verbose=1, tensorboard_log=f"runs/{args.algo}", seed=args.seed)

    print(f"Training {args.algo.upper()} on {args.env_type} domain (Strategy: {args.sampling_strategy})...")
    
    model.learn(
        total_timesteps=args.timesteps,
        callback=eval_callback,
        tb_log_name=f"{args.env_type}_{args.sampling_strategy}_seed{args.seed}"
    )

    # Save final model as well
    model.save(os.path.join(out_dir, "final_model"))
    print(f"Training finished. Best model saved to {out_dir}/best_model.zip")
    
    # Paranoid engineering: always close vectorized environments to prevent zombie sub-processes
    env.close()
    eval_env.close()

if __name__ == "__main__":
    main()
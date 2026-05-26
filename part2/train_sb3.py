import argparse
import os
import time
import gymnasium as gym
import panda_gym
from stable_baselines3 import PPO, SAC
from stable_baselines3.common.callbacks import EvalCallback, BaseCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv, DummyVecEnv, VecNormalize
from rand_wrapper import RandomizationWrapper # Will be implemented later

class SyncVecNormalizeCallback(BaseCallback):
    """Callback to sync VecNormalize stats from training env to eval env."""
    def __init__(self, eval_env, verbose=0):
        super().__init__(verbose)
        self.eval_env = eval_env
    def _on_step(self) -> bool:
        if self.training_env is not None and hasattr(self.training_env, "obs_rms"):
            self.eval_env.obs_rms = self.training_env.obs_rms
        return True

class TimeLimitCallback(BaseCallback):
    """Callback to stop training after a certain wall-clock time limit."""
    def __init__(self, max_time_seconds: float, verbose=1):
        super().__init__(verbose)
        self.max_time_seconds = max_time_seconds
        self.start_time = None

    def _on_training_start(self) -> None:
        self.start_time = time.time()

    def _on_step(self) -> bool:
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.max_time_seconds:
            if self.verbose > 0:
                print(f"\n[TimeLimitCallback] Stopping training: reached wall time limit of {self.max_time_seconds}s (elapsed: {elapsed_time:.2f}s)")
            return False
        return True


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
    parser.add_argument(
        "--comparison-mode",
        type=str,
        default="eqsteps",
        choices=["eqsteps", "eqtime"],
        help="Comparison framework mode: equal timesteps or equal wall-clock time budget",
    )
    parser.add_argument(
        "--time-limit",
        type=float,
        default=600.0,
        help="Wall-clock time limit in seconds for eqtime mode",
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
    
    # Speed optimization: use 4 parallel environments for both algorithms
    if args.algo == "ppo":
        env = make_vec_env("PandaPush-v3", n_envs=4, env_kwargs=env_kwargs, vec_env_cls=SubprocVecEnv, seed=args.seed)
        env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.)
        
        eval_env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)
        eval_env = VecNormalize(eval_env, norm_obs=True, norm_reward=False, clip_obs=10.)
        eval_env.training = False
    else:
        env = make_vec_env("PandaPush-v3", n_envs=4, env_kwargs=env_kwargs, vec_env_cls=SubprocVecEnv, seed=args.seed)
        eval_env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)

    # TODO: add randomization wrapper for UDR/ADR here (Phase 2)
    # Note: For VecEnvs, the wrapper should be applied inside the make_vec_env using `wrapper_class` argument
    # if args.sampling_strategy != "none":
    #     env_kwargs["strategy"] = args.sampling_strategy
    #     wrapper_class = RandomizationWrapper

    suffix = f"_{args.comparison_mode}" if args.comparison_mode != "eqsteps" else ""
    out_dir = f"results/{args.algo}_{args.env_type}_{args.sampling_strategy}_seed{args.seed}{suffix}"
    os.makedirs(out_dir, exist_ok=True)

    # Setup evaluation callback
    eval_freq = 10000 // (env.num_envs if hasattr(env, "num_envs") else 1)
    eval_callback = EvalCallback(
        eval_env,
        best_model_save_path=out_dir,
        log_path=out_dir,
        eval_freq=eval_freq,
        deterministic=True,
        render=False
    )
    
    callbacks = [eval_callback]
    if args.algo == "ppo":
        callbacks.append(SyncVecNormalizeCallback(eval_env))
    if args.comparison_mode == "eqtime":
        callbacks.append(TimeLimitCallback(args.time_limit))

    if args.algo == "ppo":
        model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=f"runs/{args.algo}", seed=args.seed)
    else:
        # train_freq=16 steps of n_envs=4 means updates happen every 64 collected transitions.
        # gradient_steps=64 performs 64 updates per training phase to keep the step:update ratio exactly 1:1.
        model = SAC(
            "MultiInputPolicy",
            env,
            verbose=1,
            tensorboard_log=f"runs/{args.algo}",
            seed=args.seed,
            train_freq=16,
            gradient_steps=64
        )

    timesteps = args.timesteps
    if args.comparison_mode == "eqtime":
        # Set a massive timestep ceiling so training is solely bounded by the TimeLimitCallback
        timesteps = 10_000_000

    print(f"Training {args.algo.upper()} on {args.env_type} domain (Strategy: {args.sampling_strategy}, Mode: {args.comparison_mode})...")
    
    model.learn(
        total_timesteps=timesteps,
        callback=callbacks,
        tb_log_name=f"{args.env_type}_{args.sampling_strategy}_seed{args.seed}{suffix}"
    )

    # Save final model as well
    model.save(os.path.join(out_dir, "final_model"))
    if args.algo == "ppo":
        env.save(os.path.join(out_dir, "vec_normalize.pkl"))
    print(f"Training finished. Best model saved to {out_dir}/best_model.zip")
    
    # Paranoid engineering: always close vectorized environments to prevent zombie sub-processes
    env.close()
    eval_env.close()

if __name__ == "__main__":
    main()
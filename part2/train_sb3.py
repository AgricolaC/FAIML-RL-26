import argparse
import os
import time
import multiprocessing
import gymnasium as gym
import panda_gym
from stable_baselines3 import PPO, SAC
from stable_baselines3.common.callbacks import EvalCallback, BaseCallback
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import SubprocVecEnv, DummyVecEnv, VecNormalize
from rand_wrapper import RandomizationWrapper

class SyncVecNormalizeCallback(BaseCallback):
    """Callback to sync VecNormalize stats from training env to eval env."""
    def __init__(self, eval_env, verbose=0):
        super().__init__(verbose)
        self.eval_env = eval_env
    def _on_step(self) -> bool:
        if self.training_env is not None and hasattr(self.training_env, "obs_rms"):
            self.eval_env.obs_rms = self.training_env.obs_rms
        return True

class SaveVecNormalizeCallback(BaseCallback):
    """Callback to save VecNormalize stats when a new best model is found."""
    def __init__(self, save_path: str):
        super().__init__()
        self.save_path = save_path

    def _on_step(self) -> bool:
        vec_norm = self.model.get_vec_normalize_env()
        if vec_norm is not None:
            vec_norm.save(os.path.join(self.save_path, "vec_normalize.pkl"))
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
        "--mass-min",
        type=float,
        default=0.1,
        help="Minimum mass limit for UDR/ADR",
    )
    parser.add_argument(
        "--mass-max",
        type=float,
        default=10.0,
        help="Maximum mass limit for UDR/ADR",
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
        default=500_000,
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
    parser.add_argument(
        "--learning-rate",
        type=float,
        default=None,
        help="Override learning rate (default: use SB3 algorithm default)",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()

    suffix = f"_{args.comparison_mode}" if args.comparison_mode != "eqsteps" else ""
    mass_suffix = ""
    if args.sampling_strategy != "none":
        mass_suffix = f"_{args.mass_min}-{args.mass_max}"
    
    run_name = f"{args.algo}_{args.env_type}_{args.sampling_strategy}{mass_suffix}_seed{args.seed}{suffix}"
    out_dir = f"results/{run_name}"
    
    os.makedirs(out_dir, exist_ok=True)
    tb_log_dir = f"runs/{args.algo}/{run_name}"

    # Create training environment
    env_kwargs = {
        "render_mode": "rgb_array", # panda-gym requires 'rgb_array' or 'human'
        "type": args.env_type,
        "reward_type": "dense",
    }
    
    vec_env_kwargs = {}
    if args.sampling_strategy != "none":
        wrapper_kwargs = {
            "mode": args.sampling_strategy,
            "mass_range": (args.mass_min, args.mass_max)
        }
        if args.sampling_strategy == "adr":
            wrapper_kwargs["shared_phi_L"] = multiprocessing.Value('f', 0.9)
            wrapper_kwargs["shared_phi_H"] = multiprocessing.Value('f', 1.1)
            wrapper_kwargs["log_path"] = os.path.join(out_dir, "adr_boundaries.csv")
            wrapper_kwargs["tb_log_dir"] = tb_log_dir
        vec_env_kwargs["wrapper_class"] = RandomizationWrapper
        vec_env_kwargs["wrapper_kwargs"] = wrapper_kwargs

    # Speed optimization: use 4 parallel environments for PPO
    if args.algo == "ppo":
        env = make_vec_env("PandaPush-v3", n_envs=4, env_kwargs=env_kwargs, vec_env_cls=SubprocVecEnv, seed=args.seed, **vec_env_kwargs)
        env = VecNormalize(env, norm_obs=True, norm_reward=True, clip_obs=10.)
        
        eval_env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)
        eval_env = VecNormalize(eval_env, norm_obs=True, norm_reward=False, clip_obs=10.)
        eval_env.training = False
    else:
        env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed, **vec_env_kwargs)
        eval_env = make_vec_env("PandaPush-v3", n_envs=1, env_kwargs=env_kwargs, vec_env_cls=DummyVecEnv, seed=args.seed)



    # Setup evaluation callback
    eval_freq = 10000 // (env.num_envs if hasattr(env, "num_envs") else 1)
    
    save_vec_normalize = SaveVecNormalizeCallback(save_path=out_dir) if args.algo == "ppo" else None
    
    eval_callback = EvalCallback(
        eval_env,
        best_model_save_path=out_dir,
        log_path=out_dir,
        eval_freq=eval_freq,
        deterministic=True,
        render=False,
        callback_on_new_best=save_vec_normalize
    )
    
    callbacks = [eval_callback]
    if args.algo == "ppo":
        callbacks.append(SyncVecNormalizeCallback(eval_env))
    if args.comparison_mode == "eqtime":
        callbacks.append(TimeLimitCallback(args.time_limit))

    if args.algo == "ppo":
        model = PPO("MultiInputPolicy", env, verbose=1, tensorboard_log=tb_log_dir, seed=args.seed)
    else:
        # SAC relies on off-policy immediate gradient updates.
        # Vectorized batching degrades performance, so we fall back to SB3 defaults.
        sac_kwargs = {
            "verbose": 1,
            "tensorboard_log": tb_log_dir,
            "seed": args.seed,
        }
        if args.learning_rate is not None:
            sac_kwargs["learning_rate"] = args.learning_rate
        model = SAC("MultiInputPolicy", env, **sac_kwargs)

    timesteps = args.timesteps
    if args.comparison_mode == "eqtime":
        # Set a massive timestep ceiling so training is solely bounded by the TimeLimitCallback
        timesteps = 10_000_000

    print(f"Training {args.algo.upper()} on {args.env_type} domain (Strategy: {args.sampling_strategy}, Mode: {args.comparison_mode})...")
    
    model.learn(
        total_timesteps=timesteps,
        callback=callbacks,
        tb_log_name="sb3"
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
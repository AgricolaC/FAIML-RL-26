"""
Unified Experiment Orchestrator for PandaPush-v3
This script consolidates PandaPush RL training and evaluation phases into a single executable.
It automatically handles training PPO/SAC models, evaluating them on Source/Target environments, 
skipping already trained configurations, and generating the final aggregated summary report.
Usage Examples:
---------------
1. Run Phase 1 Baselines (PPO vs SAC on Source & Target, eqsteps & eqtime):
    python3 run_experiments.py --mode baselines
2. Run Phase 2 Hyperparameter Sweep (SAC Learning Rate):
    python3 run_experiments.py --mode hparam
3. Run Phase 3 Domain Randomization (UDR and ADR):
    python3 run_experiments.py --mode dr
4. Run EVERYTHING sequentially:
    python3 run_experiments.py --mode all
Optional Flags:
---------------
--seeds : Specify which seeds to run. Default is 1 2 3.
          Example: python3 run_experiments.py --mode dr --seeds 42 1337
"""
import argparse
import subprocess
import os
import sys


def run_cmd(cmd):
    print(f"\nExecuting: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def train(algo, env_type, strategy, seed, comp_mode, timesteps=500000, 
          mass_min=None, mass_max=None, time_limit=None, lr=None):
    cmd = [
        sys.executable, "train_sb3.py",
        "--algo", algo,
        "--env-type", env_type,
        "--sampling-strategy", strategy,
        "--seed", str(seed),
        "--comparison-mode", comp_mode,
        "--timesteps", str(timesteps)
    ]
    if mass_min is not None:
        cmd.extend(["--mass-min", str(mass_min)])
    if mass_max is not None:
        cmd.extend(["--mass-max", str(mass_max)])
    if time_limit is not None:
        cmd.extend(["--time-limit", str(time_limit)])
    if lr is not None:
        cmd.extend(["--learning-rate", str(lr)])

    suffix = f"_{comp_mode}" if comp_mode != "eqsteps" else ""
    mass_suffix = ""
    if strategy != "none" and mass_min is not None and mass_max is not None:
        mass_suffix = f"_{mass_min}-{mass_max}"
        
    out_dir = f"results/{algo}_{env_type}_{strategy}{mass_suffix}_seed{seed}{suffix}"
    
    # Check if already trained
    if os.path.exists(os.path.join(out_dir, "best_model.zip")):
        print(f"\033[1;32m[SKIPPED]\033[0m {out_dir} already trained. Skipping.")
        return out_dir
        
    print(f"\033[1;33m[TRAINING]\033[0m {out_dir}")
    run_cmd(cmd)
    return out_dir

def evaluate(model_path, algo, env_type, episodes=50):
    if not os.path.exists(model_path):
        print(f"[WARNING] No model found at {model_path}. Skipping evaluation.")
        return
    cmd = [
        sys.executable, "eval_sb3.py",
        "--model-path", model_path,
        "--algo", algo,
        "--env-type", env_type,
        "--episodes", str(episodes)
    ]
    run_cmd(cmd)

def run_baselines(seeds):
    print("\n" + "="*74)
    print(" PHASE 1: Baselines (PPO vs SAC) on Source & Target")
    print("="*74)
    for algo in ["ppo", "sac"]:
        for env_type in ["source", "target"]:
            for comp_mode in ["eqsteps", "eqtime"]:
                for seed in seeds:
                    kwargs = {"timesteps": 500000}
                    if comp_mode == "eqtime":
                        kwargs["time_limit"] = 600.0
                    
                    out_dir = train(
                        algo=algo, 
                        env_type=env_type, 
                        strategy="none", 
                        seed=seed, 
                        comp_mode=comp_mode, 
                        **kwargs
                    )
                    
                    # Evaluate on source and target
                    model_path = os.path.join(out_dir, "best_model.zip")
                    print(f"\n--- Evaluating {algo} ({env_type}, {comp_mode}, Seed {seed}) on SOURCE ---")
                    evaluate(model_path, algo, "source")
                    print(f"\n--- Evaluating {algo} ({env_type}, {comp_mode}, Seed {seed}) on TARGET ---")
                    evaluate(model_path, algo, "target")

def run_hparam(seeds):
    print("\n" + "="*74)
    print(" PHASE 2: SAC Learning Rate Sweep")
    print("="*74)
    
    lrs = ["1e-4", "3e-4", "1e-3"]
    for lr in lrs:
        strategy = f"lr{lr}"
        # For backwards compatibility with the bash script names
        label = "lr3e-4_default" if lr == "3e-4" else strategy
            
        for seed in seeds:
            legacy_dir = f"results/sweep_sac_{label}_seed{seed}"
            if os.path.exists(os.path.join(legacy_dir, "best_model.zip")):
                print(f"\033[1;32m[SKIPPED]\033[0m {legacy_dir} already trained. Skipping.")
                out_dir = legacy_dir
            else:
                out_dir = train(
                    algo="sac", 
                    env_type="source", 
                    strategy=strategy, 
                    seed=seed, 
                    comp_mode="eqsteps", 
                    lr=float(lr)
                )
            
            model_path = os.path.join(out_dir, "best_model.zip")
            print(f"\n--- Evaluating {strategy} (Seed {seed}) on SOURCE ---")
            evaluate(model_path, "sac", "source")
            print(f"\n--- Evaluating {strategy} (Seed {seed}) on TARGET ---")
            evaluate(model_path, "sac", "target")

def run_dr(seeds):
    print("\n" + "="*74)
    print(" PHASE 3: Domain Randomization Sweep")
    print("="*74)
    
    configs = [
        ("udr", 0.5, 2.0),
        ("udr", 0.5, 5.5),
        ("udr", 0.1, 15.0),
        ("adr", 0.1, 15.0),
    ]
    
    for strategy, m_min, m_max in configs:
        for seed in seeds:
            out_dir = train(
                algo="sac",
                env_type="source",
                strategy=strategy,
                seed=seed,
                comp_mode="eqsteps",
                mass_min=m_min,
                mass_max=m_max,
                lr=1e-3
            )
            model_path = os.path.join(out_dir, "best_model.zip")
            print(f"\n--- Evaluating {strategy}_{m_min}-{m_max} (Seed {seed}) on SOURCE ---")
            evaluate(model_path, "sac", "source")
            print(f"\n--- Evaluating {strategy}_{m_min}-{m_max} (Seed {seed}) on TARGET ---")
            evaluate(model_path, "sac", "target")

def main():
    parser = argparse.ArgumentParser(description="Unified Experiment Orchestrator")
    parser.add_argument("--mode", type=str, choices=["baselines", "hparam", "dr", "all"], 
                        required=True, help="Which suite of experiments to run")
    parser.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3],
                        help="List of seeds to run")
    
    args = parser.parse_args()
    
    if args.mode in ["baselines", "all"]:
        run_baselines(args.seeds)
    if args.mode in ["hparam", "all"]:
        run_hparam(args.seeds)
    if args.mode in ["dr", "all"]:
        run_dr(args.seeds)
        
    print("\nGenerating final summary JSON...")
    run_cmd([sys.executable, "generate_summary.py"])
    print("\n\033[1;32mAll experiments complete!\033[0m")

if __name__ == "__main__":
    main()

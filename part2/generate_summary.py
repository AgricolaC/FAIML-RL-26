import json
import os
import glob
import numpy as np
from collections import defaultdict
from eval_sb3 import evaluate

def parse_run_name(dir_name):
    # Phase 2 Sweep format: sweep_{algo}_{lr}_{seed}
    if dir_name.startswith("sweep_"):
        parts = dir_name.split('_')
        if len(parts) >= 4:
            algo = parts[1]
            env_type = "source"  # Hyperparameter sweeps were done on source
            strategy = parts[2]  # e.g., lr1e-3
            seed_str = parts[-1].replace('seed', '')
            try:
                seed = int(seed_str)
            except ValueError:
                seed = -1
            comp_mode = "eqsteps"
            return algo, env_type, strategy, seed, comp_mode

    # Standard / Phase 3 formats
    parts = dir_name.split('_')
    if len(parts) >= 4:
        algo = parts[0]
        env_type = parts[1]
        
        # Check if it has mass range (e.g. ppo_source_udr_0.5-2.0_seed1)
        if "seed" in parts[3]:
            strategy = parts[2]
            seed_idx = 3
        elif len(parts) >= 5 and "seed" in parts[4]:
            strategy = f"{parts[2]}_{parts[3]}"
            seed_idx = 4
        else:
            return None, None, None, None, None
            
        seed_str = parts[seed_idx].replace('seed', '')
        try:
            seed = int(seed_str)
        except ValueError:
            seed = -1
            
        comp_mode = parts[seed_idx + 1] if len(parts) > seed_idx + 1 else "eqsteps"
        return algo, env_type, strategy, seed, comp_mode
        
    return None, None, None, None, None

def main():
    results_dir = "results"
    output_path = os.path.join(results_dir, "summary.json")
    
    # We will evaluate for 50 episodes
    eval_episodes = 50
    
    summary = []
    
    model_paths = []
    for d in glob.glob(os.path.join(results_dir, "*")):
        if not os.path.isdir(d):
            continue
        dir_name = os.path.basename(d)
        
        # We report final_model for DR conditions because EvalCallback selection 
        # on a fixed-mass eval env would bias selection toward source-mass 
        # performance, defeating the robustness objective of DR.
        if "udr" in dir_name or "adr" in dir_name:
            model_file = os.path.join(d, "final_model.zip")
        else:
            model_file = os.path.join(d, "best_model.zip")
            
        if os.path.exists(model_file):
            model_paths.append(model_file)
    
    print(f"Found {len(model_paths)} models. Evaluating each on 'source' and 'target'...")
    
    for model_path in sorted(model_paths):
        dir_name = os.path.basename(os.path.dirname(model_path))
        algo, train_env, strategy, seed, comp_mode = parse_run_name(dir_name)
        
        if not algo:
            print(f"Skipping {dir_name}: could not parse naming format.")
            continue
            
        print(f"\n===========================================================")
        print(f" Processing Model: {dir_name}")
        print(f" Algorithm: {algo.upper()}, Trained on: {train_env}, Strategy: {strategy}, Mode: {comp_mode}")
        print(f"===========================================================")
        
        # Evaluate on Source
        print(f"--> Evaluating on Source Env")
        src_metrics = evaluate(
            model_path=model_path,
            algo=algo,
            n_episodes=eval_episodes,
            deterministic=True,
            render=False,
            record_video=False,
            env_type="source"
        )
        
        # Evaluate on Target
        print(f"--> Evaluating on Target Env")
        tgt_metrics = evaluate(
            model_path=model_path,
            algo=algo,
            n_episodes=eval_episodes,
            deterministic=True,
            render=False,
            record_video=False,
            env_type="target"
        )
        
        summary.append({
            "run_name": dir_name,
            "algorithm": algo,
            "train_env": train_env,
            "strategy": strategy,
            "seed": seed,
            "comparison_mode": comp_mode,
            "evaluations": {
                "source": src_metrics,
                "target": tgt_metrics
            }
        })
    
    # Aggregate across seeds
    by_config = defaultdict(list)
    for run in summary:
        cfg_key = (run["algorithm"], run["train_env"], run["strategy"], run["comparison_mode"])
        by_config[cfg_key].append(run)
        
    per_config = []
    for cfg_key, runs in by_config.items():
        algo, train_env, strategy, comp_mode = cfg_key
        
        src_returns = [r["evaluations"]["source"]["mean_return"] for r in runs]
        src_success = [r["evaluations"]["source"]["success_rate"] for r in runs]
        tgt_returns = [r["evaluations"]["target"]["mean_return"] for r in runs]
        tgt_success = [r["evaluations"]["target"]["success_rate"] for r in runs]
        
        n_seeds = len(runs)
        
        def agg_stats(values):
            if not values: return {}
            return {
                "mean": float(np.mean(values)),
                "std": float(np.std(values, ddof=1)) if n_seeds > 1 else 0.0,
                "median": float(np.median(values)),
                "min": float(np.min(values)),
                "max": float(np.max(values))
            }
        
        per_config.append({
            "algorithm": algo,
            "train_env": train_env,
            "strategy": strategy,
            "comparison_mode": comp_mode,
            "n_seeds": n_seeds,
            "source_eval": {
                "return": agg_stats(src_returns),
                "success_rate": agg_stats(src_success),
            },
            "target_eval": {
                "return": agg_stats(tgt_returns),
                "success_rate": agg_stats(tgt_success),
            }
        })
        
    final_output = {
        "per_run": summary,
        "per_config": per_config
    }

    # Save the consolidated JSON
    with open(output_path, 'w') as f:
        json.dump(final_output, f, indent=2)
        
    print(f"\nSuccessfully wrote summary with {len(summary)} run entries and {len(per_config)} aggregated configs to {output_path}")

if __name__ == "__main__":
    main()

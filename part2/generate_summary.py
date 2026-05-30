import json
import os
import glob
import numpy as np
from collections import defaultdict
from eval_sb3 import evaluate

import re

def parse_run_name(dir_name):
    # Handle sweep_ prefix (hyperparameter sweep runs)
    if dir_name.startswith("sweep_"):
        parts = dir_name.split('_')
        if len(parts) >= 4:
            algo = parts[1]
            env_type = "source"
            strategy = parts[2]
            seed_str = parts[-1].replace('seed', '')
            try:
                seed = int(seed_str)
            except ValueError:
                seed = -1
            return algo, env_type, strategy, seed, "eqsteps", "default"

    # Standard format:
    # {algo}_{env}_{strategy}[_{mass_range}][_lr{lr}]_seed{N}[_{mode}]
    m = re.match(
        r'^(ppo|sac)_(source|target)_(none|udr|adr)'
        r'(?:_([\d.]+-[\d.]+))?'      # optional: mass range e.g. 0.5-5.5
        r'(?:_lr([\de.\-]+))?'        # optional: lr e.g. 3e-4, 1e-3
        r'_seed(\d+)'
        r'(?:_(eqtime|eqsteps))?$',   # optional: comparison mode
        dir_name
    )
    if m:
        algo, env_type, base_strategy, mass_range, lr, seed_str, mode = m.groups()
        strategy = f"{base_strategy}_{mass_range}" if mass_range else base_strategy
        comp_mode = mode if mode else "eqsteps"
        lr_val = lr if lr else "default"
        return algo, env_type, strategy, int(seed_str), comp_mode, lr_val

    return None, None, None, None, None, None

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
        algo, train_env, strategy, seed, comp_mode, lr = parse_run_name(dir_name)
        
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
            "lr": lr,
            "evaluations": {
                "source": src_metrics,
                "target": tgt_metrics
            }
        })
    
    # Aggregate across seeds
    by_config = defaultdict(list)
    for run in summary:
        cfg_key = (run["algorithm"], run["train_env"], run["strategy"], run["comparison_mode"], run["lr"])
        by_config[cfg_key].append(run)
        
    per_config = []
    for cfg_key, runs in by_config.items():
        algo, train_env, strategy, comp_mode, lr = cfg_key
        
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
            "lr": lr,
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

import json
import os
import glob
from eval_sb3 import evaluate

def parse_run_name(dir_name):
    # Example formats: sac_source_none_seed1 or sac_source_none_seed1_eqtime
    parts = dir_name.split('_')
    if len(parts) >= 4:
        algo = parts[0]
        env_type = parts[1]
        strategy = parts[2]
        seed_str = parts[3].replace('seed', '')
        try:
            seed = int(seed_str)
        except ValueError:
            seed = -1
        comp_mode = parts[4] if len(parts) >= 5 else "eqsteps"
        return algo, env_type, strategy, seed, comp_mode
    return None, None, None, None, None

def main():
    results_dir = "results"
    output_path = os.path.join(results_dir, "summary.json")
    
    # We will evaluate for 100 episodes as done in Phase 1
    eval_episodes = 100
    
    summary = []
    
    # Find all best models
    model_paths = glob.glob(os.path.join(results_dir, "*", "best_model.zip"))
    
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
    
    # Save the consolidated JSON
    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=2)
        
    print(f"\nSuccessfully wrote summary with {len(summary)} entries to {output_path}")

if __name__ == "__main__":
    main()

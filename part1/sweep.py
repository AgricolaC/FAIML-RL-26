"""Hyperparameter sweep over actor learning-rate and update_every.

Grid (constants at the top — edit to taste):
  LR_VALUES     : actor LRs to try
  UPDATE_VALUES : update_every values to try
  ALGORITHMS    : which algorithms to sweep
  SEEDS         : random seeds per config
  EPISODES      : training episodes per run

Results land in results/{algorithm}/lr{lr}_upd{N}/seed_{s}/
using train.py's --results-dir flag, so the layout is identical to a
normal run and both train.py and sweep.py share the same results tree.

Skip behaviour: if model.pt already exists for a config, that run is
skipped so the sweep can be safely resumed after interruption.
Use --no-skip to force a full re-run.

Usage:
    python sweep.py
    python sweep.py --algorithms ac_td reinforce
    python sweep.py --no-skip
    python sweep.py --summary-only          # print table from existing results
"""

import argparse
import csv
import itertools
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

# -----------------------------------------------------------------------
# Grid definition
# -----------------------------------------------------------------------
LR_VALUES     = [1e-4, 3e-4, 1e-3, 1e-2]
UPDATE_VALUES = [1,5]
SEEDS         = [1,2,3,4,5]
EPISODES      = 2000
_HERE         = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR   = os.path.join(_HERE, 'results')

ALL_ALGORITHMS = [
    'reinforce', 'reinforce_batch', 'reinforce_ema',
    'reinforce_fixed', 'ac_mc', 'ac_td',
]


# -----------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------

def _out_dir(results_dir, algorithm, lr, update_every, seed):
    return Path(results_dir) / algorithm / f'lr{lr}_upd{update_every}' / f'seed_{seed}'


def run_one(algorithm, lr, update_every, seed, episodes, results_dir, skip_existing, no_standardize):
    out_dir = _out_dir(results_dir, algorithm, lr, update_every, seed)
    if skip_existing and (out_dir / 'model.pt').exists():
        print(f"  [skip]  {out_dir}")
        return True

    cmd = [
        sys.executable, os.path.join(_HERE, 'train.py'),
        '--algorithm',   algorithm,
        '--lr',          str(lr),
        '--update-every', str(update_every),
        '--seed',        str(seed),
        '--episodes',    str(episodes),
        '--results-dir', results_dir,
        '--print-every', '500',
        '--eval-every',  '50',
        '--eval-episodes', '10',
        '--critic-lr',   '1e-3',
    ]
    if no_standardize:
        cmd.append('--no-standardize')
        
    print(f"  [run]   " + ' '.join(cmd[2:]))
    t0 = time.time()
    result = subprocess.run(cmd)
    elapsed = time.time() - t0

    if result.returncode != 0:
        print(f"  [FAIL]  returncode={result.returncode}")
        return False

    print(f"  [done]  {elapsed:.0f}s")
    return True


def load_final_eval(results_dir, algorithm, lr, update_every, seed):
    """Return the last eval_mean_return from eval_log.csv, or None."""
    path = _out_dir(results_dir, algorithm, lr, update_every, seed) / 'eval_log.csv'
    if not path.exists():
        return None
    with open(path, newline='') as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return None
    return float(rows[-1]['eval_mean_return'])


def print_summary(algorithms, lr_values, update_values, seeds, results_dir):
    seed_headers = '  '.join(f's{s:>2}' for s in seeds)
    header = f"{'Algorithm':<18} {'LR':>6}  {'upd':>4}  {seed_headers}   mean"
    sep = '-' * len(header)
    print(f"\n{'='*len(header)}")
    print("SWEEP SUMMARY  (final eval mean return, averaged over seeds)")
    print(f"{'='*len(header)}")
    print(header)

    prev_algo = None
    for algo in algorithms:
        for lr in lr_values:
            for upd in update_values:
                if algo != prev_algo:
                    print(sep)
                    prev_algo = algo

                vals = [load_final_eval(results_dir, algo, lr, upd, s) for s in seeds]
                seed_cols = '  '.join(
                    f'{v:>4.0f}' if v is not None else '  --' for v in vals)
                valid = [v for v in vals if v is not None]
                mean_str = f'{np.mean(valid):>6.0f}' if valid else '    --'
                print(f"{algo:<18} {lr:>6.0e}  {upd:>4}  {seed_cols}   {mean_str}")

    print(f"{'='*len(header)}\n")


# -----------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Hyperparameter sweep: LR × update_every across algorithms')
    parser.add_argument('--algorithms', nargs='+', default=ALL_ALGORITHMS,
                        choices=ALL_ALGORITHMS,
                        help='Algorithms to include (default: all)')
    parser.add_argument('--lr-values', nargs='+', type=float, default=LR_VALUES,
                        help='Actor LR values')
    parser.add_argument('--update-values', nargs='+', type=int, default=UPDATE_VALUES,
                        help='update_every values')
    parser.add_argument('--seeds', nargs='+', type=int, default=SEEDS,
                        help='Random seeds')
    parser.add_argument('--episodes', type=int, default=EPISODES,
                        help='Training episodes per run (default: 3000)')
    parser.add_argument('--results-dir', type=str, default=RESULTS_DIR,
                        help='Root output directory (default: part1/results/)')
    parser.add_argument('--no-skip', action='store_true',
                        help='Re-run configs that already have model.pt')
    parser.add_argument('--summary-only', action='store_true',
                        help='Print results table from existing runs and exit')
    parser.add_argument('--no-standardize', action='store_true',
                        help='Pass --no-standardize to train.py to disable standardization')
    args = parser.parse_args()

    if args.summary_only:
        print_summary(args.algorithms, args.lr_values, args.update_values,
                      args.seeds, args.results_dir)
        return

    configs = list(itertools.product(
        args.algorithms, args.lr_values, args.update_values, args.seeds))
    total = len(configs)

    print(f"Sweep: {len(args.algorithms)} algorithms × "
          f"{len(args.lr_values)} LRs × "
          f"{len(args.update_values)} update_every × "
          f"{len(args.seeds)} seeds = {total} runs")
    print(f"Episodes/run : {args.episodes}")
    print(f"Results dir  : {args.results_dir}")
    print(f"Skip existing: {not args.no_skip}\n")

    failed = []
    t_sweep = time.time()

    for i, (algo, lr, upd, seed) in enumerate(configs, 1):
        print(f"[{i:>3}/{total}]  algo={algo:<18}  lr={lr:.0e}  upd={upd}  seed={seed}")
        success = run_one(
            algo, lr, upd, seed, args.episodes,
            args.results_dir, not args.no_skip,
            args.no_standardize
        )
        if not success:
            failed.append((algo, lr, upd, seed))

    elapsed_total = time.time() - t_sweep
    print(f"\nSweep finished in {elapsed_total/60:.1f} min  "
          f"({len(configs) - len(failed)}/{total} runs succeeded)")

    print_summary(args.algorithms, args.lr_values, args.update_values,
                  args.seeds, args.results_dir)

    if failed:
        print(f"Failed runs ({len(failed)}):")
        for algo, lr, upd, seed in failed:
            print(f"  algo={algo}  lr={lr:.0e}  upd={upd}  seed={seed}")
        sys.exit(1)


if __name__ == '__main__':
    main()

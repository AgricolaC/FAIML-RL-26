"""Render model_best.pt videos for the best HP config per algorithm.

Picks the winning lr/upd per algorithm using the same final-K eval score as
plot_results.py --best-config-only, then for each seed of that config calls
render_local.py --save-video to write MP4s.

Usage:
    python part1/render_best_videos.py
    python part1/render_best_videos.py --episodes 3 --algorithms ac_td reinforce_ema
    python part1/render_best_videos.py --dry-run        # print plan, render nothing
"""
import argparse
import csv
import glob
import subprocess
import sys
from pathlib import Path

import numpy as np

ALL_ALGORITHMS = ['reinforce', 'reinforce_batch', 'reinforce_ema',
                  'reinforce_fixed', 'ac_mc', 'ac_td']

HERE = Path(__file__).resolve().parent


def best_hp_per_algo(results_dir, algorithm, final_k):
    """Return (hp_tag, [seed_dirs], score) for the highest-scoring HP config."""
    seed_dirs = sorted(
        glob.glob(str(results_dir / algorithm / 'lr*_upd*' / 'seed_*'))
    )
    if not seed_dirs:
        return None

    hp_groups = {}
    for sd in seed_dirs:
        hp_tag = Path(sd).parent.name
        hp_groups.setdefault(hp_tag, []).append(sd)

    best_tag, best_score = None, -float('inf')
    for hp_tag, sds in hp_groups.items():
        per_seed_finals = []
        for sd in sds:
            eval_path = Path(sd) / 'eval_log.csv'
            if not eval_path.exists():
                continue
            with open(eval_path, newline='') as f:
                rows = list(csv.DictReader(f))
            vals = [float(r['eval_mean_return']) for r in rows
                    if r.get('eval_mean_return')]
            if not vals:
                continue
            n = min(final_k, len(vals))
            per_seed_finals.append(float(np.mean(vals[-n:])))
        if per_seed_finals:
            score = float(np.mean(per_seed_finals))
            if score > best_score:
                best_score = score
                best_tag = hp_tag

    if best_tag is None:
        return None
    return best_tag, sorted(hp_groups[best_tag]), best_score


def main():
    p = argparse.ArgumentParser(
        description='Render model_best.pt videos for the best HP per algorithm')
    p.add_argument('--results-dir', default=str(HERE / 'results'))
    p.add_argument('--output-dir',
                   default=str(HERE.parent / 'videos' / 'model_best'))
    p.add_argument('--algorithms', nargs='+', default=ALL_ALGORITHMS,
                   choices=ALL_ALGORITHMS)
    p.add_argument('--episodes', type=int, default=3)
    p.add_argument('--seed', type=int, default=42)
    p.add_argument('--final-k', type=int, default=10,
                   help='Trailing eval checkpoints used to score HP configs')
    p.add_argument('--dry-run', action='store_true',
                   help='Print plan, skip subprocess calls')
    args = p.parse_args()

    results_dir = Path(args.results_dir)
    output_dir = Path(args.output_dir)
    render_script = HERE / 'render_local.py'

    plan = []
    for algo in args.algorithms:
        sel = best_hp_per_algo(results_dir, algo, args.final_k)
        if sel is None:
            print(f"[skip] {algo}: no eval data")
            continue
        hp_tag, seed_dirs, score = sel
        print(f"[best] {algo:<18} {hp_tag:<20} score={score:>7.1f}  "
              f"({len(seed_dirs)} seeds)")
        for sd in seed_dirs:
            ckpt = Path(sd) / 'model_best.pt'
            if not ckpt.exists():
                print(f"  [miss] {ckpt}")
                continue
            out_subdir = output_dir / algo / hp_tag / Path(sd).name
            plan.append((algo, hp_tag, Path(sd).name, ckpt, out_subdir))

    print(f"\n{len(plan)} renders queued -> {output_dir}\n")
    if args.dry_run:
        for algo, hp, seed, ckpt, out in plan:
            print(f"  {algo}/{hp}/{seed} -> {out}")
        return

    failed = []
    for i, (algo, hp, seed_name, ckpt, out_subdir) in enumerate(plan, 1):
        print(f"[{i:>2}/{len(plan)}] {algo}/{hp}/{seed_name}")
        out_subdir.mkdir(parents=True, exist_ok=True)
        cmd = [
            sys.executable, str(render_script),
            '--checkpoint', str(ckpt),
            '--save-video', str(out_subdir),
            '--no-render',
            '--no-best',
            '--episodes', str(args.episodes),
            '--seed', str(args.seed),
        ]
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"  [FAIL] returncode={result.returncode}")
            failed.append((algo, hp, seed_name))

    print(f"\nDone. {len(plan) - len(failed)}/{len(plan)} succeeded.")
    if failed:
        print("Failed:")
        for algo, hp, seed in failed:
            print(f"  {algo}/{hp}/{seed}")
        sys.exit(1)


if __name__ == '__main__':
    main()

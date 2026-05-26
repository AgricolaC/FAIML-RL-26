"""Plot learning curves and produce a summary table from training results.

Expected directory layout:
    results/
      <algorithm>/
        seed_<N>/
          log.csv
          eval_log.csv

Usage:
    python plot_results.py
    python plot_results.py --results-dir results --window 50
    python plot_results.py --algorithms reinforce ac_td
"""
import argparse
import csv
import glob
import os
import re
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # non-interactive backend
import matplotlib.pyplot as plt
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_RESULTS = os.path.join(_HERE, 'results')


# ------------------------------------------------------------------
#  Helpers
# ------------------------------------------------------------------

COLORS = {
    'reinforce':        '#e74c3c',
    'reinforce_batch':  '#3498db',
    'reinforce_ema':    '#2ecc71',
    'reinforce_fixed':  '#1abc9c',
    'ac_mc':            '#9b59b6',
    'ac_td':            '#f39c12',
}

LABELS = {
    'reinforce':        'REINFORCE',
    'reinforce_batch':  'REINFORCE (batch baseline)',
    'reinforce_ema':    'REINFORCE (EMA baseline)',
    'reinforce_fixed':  'REINFORCE (fixed baseline)',
    'ac_mc':            'Actor-Critic (MC)',
    'ac_td':            'Actor-Critic (TD)',
}


def load_csv(path):
    """Load a CSV file into a dict of column-lists."""
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        data = {k: [] for k in reader.fieldnames}
        for row in reader:
            for k, v in row.items():
                if v == '':
                    data[k].append(np.nan)
                else:
                    try:
                        data[k].append(float(v))
                    except ValueError:
                        data[k].append(v)
    return data


def smooth(values, window=50):
    """Rolling-mean smoothing with edge-padding."""
    n = len(values)
    if n == 0:
        return values
    w = min(window, n)
    kernel = np.ones(w) / w
    padded = np.pad(values, (w - 1, 0), mode='edge')
    return np.convolve(padded, kernel, mode='valid')


def select_configs(hp_groups, best_config_only, final_eval_checkpoints):
    """Return the list of (hp_tag, seed_dirs) to plot for one algorithm.

    When best_config_only is True, scores each HP config by the mean of
    each seed's final `final_eval_checkpoints` eval returns and returns
    only the winner. Falls back to all configs if no eval data exists.
    """
    if not best_config_only:
        return sorted(hp_groups.items())

    best_tag, best_score = None, -float('inf')
    for hp_tag, sds in sorted(hp_groups.items()):
        scores = []
        for sd in sds:
            eval_path = os.path.join(sd, 'eval_log.csv')
            if not os.path.exists(eval_path):
                continue
            data = load_csv(eval_path)
            vals = np.array(data.get('eval_mean_return', []), dtype=float)
            if len(vals) == 0:
                continue
            n = min(final_eval_checkpoints, len(vals))
            scores.append(float(np.nanmean(vals[-n:])))
        if scores and np.mean(scores) > best_score:
            best_score, best_tag = float(np.mean(scores)), hp_tag

    return [(best_tag, hp_groups[best_tag])] if best_tag else sorted(hp_groups.items())


# ------------------------------------------------------------------
#  Main
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description='Plot training results for Hopper-v4 experiments')
    parser.add_argument('--results-dir', type=str, default=_DEFAULT_RESULTS,
                        help='Base results directory (default: part1/results/)')
    parser.add_argument('--window', type=int, default=50,
                        help='Smoothing window for learning curves')
    parser.add_argument('--algorithms', nargs='+',
                        default=['reinforce', 'reinforce_batch',
                                 'reinforce_ema', 'reinforce_fixed',
                                 'ac_mc', 'ac_td'],
                        help='Algorithms to include in the plots')
    parser.add_argument('--conv-threshold', type=float, default=100.0,
                        help='Eval return threshold to count as converged')
    parser.add_argument('--best-config-only', dest='best_config_only',
                        action='store_true', default=True,
                        help='Plot only the best HP config per algorithm (default: on)')
    parser.add_argument('--all-configs', dest='best_config_only',
                        action='store_false',
                        help='Plot every HP config (disables --best-config-only)')
    parser.add_argument('--final-eval-checkpoints', type=int, default=10,
                        help='Trailing eval checkpoints used to score HP configs '
                             'and compute the summary table final-eval mean')
    args = parser.parse_args()

    plot_dir = os.path.join(args.results_dir, 'plots')
    os.makedirs(plot_dir, exist_ok=True)

    # ── One-time HP selection per algorithm ───────────────────────────────
    # Both plots and the summary table iterate over `algo_configs` so they
    # are guaranteed to show the same curves.
    algo_configs = {}  # algo -> [(hp_tag, [seed_dirs])]
    for algo in args.algorithms:
        seed_dirs = []
        for p in Path(args.results_dir).rglob('eval_log.csv'):
            path_str = str(p.parent)
            found_algos = [a for a in LABELS.keys() if a in path_str]
            if not found_algos:
                continue
            best_algo = max(found_algos, key=len)
            if best_algo == algo:
                seed_dirs.append(path_str)

        if not seed_dirs:
            print(f"[skip] no data for '{algo}'")
            continue
            
        hp_groups = {}
        for sd in seed_dirs:
            m_lr = re.search(r'lr([\d.eE+\-]+)', sd)
            m_upd = re.search(r'upd(\d+)', sd)
            if m_lr and m_upd:
                hp_tag = f"lr{float(m_lr.group(1)):g}_upd{m_upd.group(1)}"
            else:
                hp_tag = os.path.basename(sd)
            hp_groups.setdefault(hp_tag, []).append(sd)
            
        algo_configs[algo] = select_configs(
            hp_groups, args.best_config_only, args.final_eval_checkpoints)
        if args.best_config_only and algo_configs[algo]:
            print(f"[best-HP] {algo}: {algo_configs[algo][0][0]}")

    def _label(algo, hp_tag, n_configs):
        base = LABELS.get(algo, algo)
        return f'{base} [{hp_tag}]' if n_configs > 1 else base

    # ==================================================================
    #  1.  Learning curves  (smoothed training return vs. episode)
    # ==================================================================
    fig, ax = plt.subplots(figsize=(12, 7))

    for algo in args.algorithms:
        if algo not in algo_configs:
            continue
        color = COLORS.get(algo, '#555555')
        configs = algo_configs[algo]
        for hp_tag, hp_seed_dirs in configs:
            label = _label(algo, hp_tag, len(configs))
            all_returns = []
            for sd in hp_seed_dirs:
                log_path = os.path.join(sd, 'log.csv')
                if not os.path.exists(log_path):
                    continue
                data = load_csv(log_path)
                all_returns.append(np.array(data['return'], dtype=float))
            if not all_returns:
                continue
            min_len = min(len(r) for r in all_returns)
            all_returns = np.array([r[:min_len] for r in all_returns])
            smoothed = np.array([smooth(r, args.window) for r in all_returns])
            episodes = np.arange(1, min_len + 1)
            mean_c = smoothed.mean(axis=0)
            std_c = smoothed.std(axis=0)
            ax.plot(episodes, mean_c, color=color, label=label, linewidth=2)
            ax.fill_between(episodes, mean_c - std_c, mean_c + std_c,
                            color=color, alpha=0.15)

    title1 = 'Hopper-v4: Training Curves'
    if args.best_config_only:
        title1 += ' (best HP per algorithm)'
    ax.set_xlabel('Episode', fontsize=13)
    ax.set_ylabel('Episode Return (smoothed)', fontsize=13)
    ax.set_title(title1, fontsize=15)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    lc_path = os.path.join(plot_dir, 'learning_curves.png')
    fig.savefig(lc_path, dpi=150)
    print(f"Saved {lc_path}")
    plt.close(fig)

    # ==================================================================
    #  2.  Evaluation curves  (deterministic eval return vs. episode)
    #      Summary table data is collected here so both use the same runs.
    # ==================================================================
    fig2, ax2 = plt.subplots(figsize=(12, 7))
    has_eval = False
    summary_rows = []

    for algo in args.algorithms:
        if algo not in algo_configs:
            continue
        color = COLORS.get(algo, '#555555')
        configs = algo_configs[algo]
        for hp_tag, hp_seed_dirs in configs:
            label = _label(algo, hp_tag, len(configs))

            all_eval_returns, all_eval_eps = [], []
            for sd in hp_seed_dirs:
                eval_path = os.path.join(sd, 'eval_log.csv')
                if not os.path.exists(eval_path):
                    continue
                data = load_csv(eval_path)
                if data.get('eval_mean_return'):
                    all_eval_returns.append(
                        np.array(data['eval_mean_return'], dtype=float))
                    all_eval_eps.append(
                        np.array(data['episode_checkpoint'], dtype=float))
            if not all_eval_returns:
                continue

            has_eval = True
            min_len = min(len(r) for r in all_eval_returns)
            eval_returns = np.array([r[:min_len] for r in all_eval_returns])
            eval_eps = all_eval_eps[0][:min_len]
            mean_eval = eval_returns.mean(axis=0)
            std_eval = eval_returns.std(axis=0)

            ax2.plot(eval_eps, mean_eval, color=color, label=label,
                     linewidth=2, marker='o', markersize=3)
            ax2.fill_between(eval_eps, mean_eval - std_eval,
                             mean_eval + std_eval, color=color, alpha=0.15)

            # ── Summary table row (eval-based, not training return) ────
            n_f = min(args.final_eval_checkpoints, len(mean_eval))
            # Cross-seed final: each seed's mean over the last n_f checkpoints
            per_seed_final = [float(r[-n_f:].mean()) for r in eval_returns]
            final_mean = float(np.mean(per_seed_final))
            cross_seed_std = (float(np.std(per_seed_final, ddof=1))
                              if len(per_seed_final) > 1 else 0.0)

            # Peak: best 3-checkpoint rolling mean of the seed-averaged curve
            if len(mean_eval) >= 3:
                rolling = np.convolve(mean_eval, np.ones(3) / 3, mode='valid')
                pk_i = int(np.argmax(rolling))
                peak_val = float(rolling[pk_i])
                peak_ep = int(eval_eps[pk_i + 1])  # window centre
            else:
                pk_i = int(np.argmax(mean_eval))
                peak_val = float(mean_eval[pk_i])
                peak_ep = int(eval_eps[pk_i])

            # Convergence: first eval ep where 3-pt window >= threshold
            conv_ep = None
            for i in range(1, len(mean_eval) - 1):
                if np.all(mean_eval[i - 1: i + 2] >= args.conv_threshold):
                    conv_ep = int(eval_eps[i])
                    break
            if conv_ep is None:  # fallback for short curves (< 3 pts)
                for ep, v in zip(eval_eps, mean_eval):
                    if v >= args.conv_threshold:
                        conv_ep = int(ep)
                        break

            summary_rows.append({
                'Algorithm': label,
                'N seeds': str(len(per_seed_final)),
                'Final eval mean': f'{final_mean:.1f}',
                'Cross-seed std': f'{cross_seed_std:.1f}',
                'Peak eval mean': f'{peak_val:.1f}',
                'Peak episode': str(peak_ep),
                f'Conv ep (>{args.conv_threshold:.0f})': (
                    str(conv_ep) if conv_ep else 'N/A'),
            })

    if has_eval:
        title2 = 'Hopper-v4: Evaluation Curves'
        if args.best_config_only:
            title2 += ' (best HP per algorithm)'
        ax2.set_xlabel('Episode', fontsize=13)
        ax2.set_ylabel('Eval Mean Return', fontsize=13)
        ax2.set_title(title2, fontsize=15)
        ax2.legend(fontsize=11)
        ax2.grid(True, alpha=0.3)
        fig2.tight_layout()
        ec_path = os.path.join(plot_dir, 'eval_curves.png')
        fig2.savefig(ec_path, dpi=150)
        print(f"Saved {ec_path}")
    plt.close(fig2)

    # ==================================================================
    #  3.  Summary table — eval return (printed to console)
    # ==================================================================
    if summary_rows:
        print(f"\n{'='*80}")
        print("SUMMARY TABLE  (deterministic eval return)")
        print(f"{'='*80}")
        headers = list(summary_rows[0].keys())
        widths = {h: max(len(h), max(len(r[h]) for r in summary_rows))
                  for h in headers}
        hdr = ' | '.join(h.ljust(widths[h]) for h in headers)
        print(hdr)
        print('-' * len(hdr))
        for row in summary_rows:
            print(' | '.join(str(row[h]).ljust(widths[h]) for h in headers))
        print()


if __name__ == '__main__':
    main()

"""Generate a compact summary JSON from Part 1 sweep results.

Design goals
------------
- Every metric uses estimators that are internally consistent (no mixing of a single
  order statistic like the max with a windowed mean).
- Variance / sample-efficiency metrics are computed on RAW returns; smoothing is used
  ONLY where a denoised trajectory is genuinely wanted (curve fingerprints, the
  *display* curve, and sustained-threshold convergence detection).
- Convergence requires a SUSTAINED crossing, evaluated only once a full smoothing
  window of data exists (no min_periods=1 false positives).
- Scale-dependent thresholds (plateau epsilon) are expressed relative to each run's
  own return range, so they mean the same thing across algorithms with different scales.
- Comparative findings carry effect size in pooled-std units and an explicit overlap
  flag, so a reader can judge whether a "winner" is real or noise.
- All tunables are CLI arguments. Nothing methodological is buried as a module constant.

Tiers
-----
  per_run            one entry per (algorithm, lr, update_every, seed)
  per_config         aggregated across seeds for each (algorithm, lr, update_every)
  curves             downsampled eval trajectory per run
  cross_seed_curves  episode-aligned mean/std across seeds per config
  findings           ranked conclusions WITH effect sizes and significance flags

Usage
-----
    python generate_summary.py --results-dir results --output summary.json
    python generate_summary.py --convergence-threshold 100 --hold-fraction 0.1
    python generate_summary.py --smooth-window 100 --plateau-rel-eps 0.02 \
                               --min-mean-for-cv 30 --curve-points 25
"""

import argparse
import json
import os
import re
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd


CONFIG_RE = re.compile(r'lr([\d.eE+\-]+)_upd(\d+)')

_trapz = getattr(np, 'trapezoid', None) or getattr(np, 'trapz')


# Config object — everything tunable lives here, passed explicitly everywhere.

class SummaryConfig:
    def __init__(
        self,
        convergence_threshold=1200.0,
        hold_fraction=0.10,            # fraction of remaining episodes the crossing must hold 
        smooth_window=100,             # rolling window (used for curves + convergence ONLY)
        final_eval_checkpoints=10,     # last N eval checkpoints -> "final" window
        peak_window_checkpoints=3,     # peak measured as best rolling mean of this many checkpoints, keep it an odd number (well-defined center episode, better for reporting stability of the peak estimate)
        regress_rel_drop=0.15,         # final < peak by this fraction (both windowed means) -> regressed
        plateau_window=500,            # look-ahead window (episodes) for plateau detection
        plateau_rel_eps=0.02,          # improvement < this * return_range -> plateau
        curve_points=25,               # downsampled points per eval curve
        min_mean_for_cv=200.0,          # below this mean, report std instead of CV (avoid blow-up)
        overlap_sigma=1.0,             # how many pooled std's defines "overlapping" in findings
        meaningful_floor=200.0,         # configs below this final_eval excluded from stability findings
    ):
        self.convergence_threshold = convergence_threshold
        self.hold_fraction = hold_fraction
        self.smooth_window = smooth_window
        self.final_eval_checkpoints = final_eval_checkpoints
        self.peak_window_checkpoints = peak_window_checkpoints
        self.regress_rel_drop = regress_rel_drop
        self.plateau_window = plateau_window
        self.plateau_rel_eps = plateau_rel_eps
        self.curve_points = curve_points
        self.min_mean_for_cv = min_mean_for_cv
        self.overlap_sigma = overlap_sigma
        self.meaningful_floor = meaningful_floor

    def as_dict(self):
        return {k: v for k, v in self.__dict__.items()}


# ===========================================================================
# Small numeric helpers
# ===========================================================================

def _round(v, n=2):
    return round(float(v), n) if v is not None and np.isfinite(v) else None


def _smooth(values, window):
    """Rolling mean that ONLY produces a value once a full window exists.

    Returns an array the same length as `values`, with np.nan for the first
    (window - 1) entries. This prevents the min_periods=1 false-positive where a
    single early spike is treated as a converged smoothed value.
    """
    s = pd.Series(values).rolling(window, min_periods=window).mean()
    return s.to_numpy()


def _windowed_mean(arr, n, side='tail'):
    """Mean of the first/last n entries (clamped to len)."""
    if len(arr) == 0:
        return None
    n = min(n, len(arr))
    seg = arr[-n:] if side == 'tail' else arr[:n]
    return float(np.mean(seg))


def _rolling_best_window_mean(arr, n):
    """Best (max) rolling mean of width n over arr — the 'peak' as a windowed
    estimator rather than a single lucky checkpoint. Returns (value, center_index)."""
    if len(arr) == 0:
        return None, None
    n = min(n, len(arr))
    if n == 1:
        idx = int(np.argmax(arr))
        return float(arr[idx]), idx
    means = pd.Series(arr).rolling(n, min_periods=n).mean().to_numpy()
    # means[i] is the mean of arr[i-n+1 .. i]; argmax over valid region
    valid = np.where(~np.isnan(means))[0]
    if len(valid) == 0:
        idx = int(np.argmax(arr))
        return float(arr[idx]), idx
    best_end = int(valid[np.argmax(means[valid])])
    center = best_end - (n - 1) // 2
    return float(means[best_end]), int(center)


# ===========================================================================
# Tier 1 — per-run metrics
# ===========================================================================

def summarize_run(log_df, eval_df, cfg):
    if not log_df.empty and 'return' in log_df.columns:
        returns = log_df['return'].to_numpy(dtype=float)
        episodes = log_df['episode'].to_numpy(dtype=int)
    else:
        returns = np.array([], dtype=float)
        episodes = np.array([], dtype=int)
        
    n_ep = len(returns)

    # --- training-return final window (raw) ---
    final_return_mean = _windowed_mean(returns, 100, 'tail')
    tail = returns[-min(100, n_ep):]
    final_return_std = float(np.std(tail)) if len(tail) else None
    return_range = float(np.nanmax(returns) - np.nanmin(returns)) if n_ep else 0.0

    # --- eval windows (consistent estimators: both peak and final are windowed means) ---
    eval_returns = eval_df['eval_mean_return'].to_numpy(dtype=float)
    eval_eps = eval_df['episode_checkpoint'].to_numpy(dtype=int)

    final_eval_mean = _windowed_mean(eval_returns, cfg.final_eval_checkpoints, 'tail')
    fe_n = min(cfg.final_eval_checkpoints, len(eval_returns))
    final_eval_std = float(np.std(eval_returns[-fe_n:])) if fe_n else None

    # Calculate average return per step (Return / Length) to track jumping speed
    eval_lengths = eval_df['eval_mean_length'].to_numpy(dtype=float) if 'eval_mean_length' in eval_df.columns else np.ones_like(eval_returns)
    eval_avg_per_step = eval_returns / np.maximum(eval_lengths, 1.0)
    final_eval_avg_per_step = _windowed_mean(eval_avg_per_step, cfg.final_eval_checkpoints, 'tail')

    peak_eval_mean, peak_center_idx = _rolling_best_window_mean(
        eval_returns, cfg.peak_window_checkpoints
    )
    peak_eval_episode = (
        int(eval_eps[peak_center_idx])
        if peak_center_idx is not None and 0 <= peak_center_idx < len(eval_eps)
        else None
    )

    # --- AUC on RAW returns (integrating denoises on its own; smoothing first
    #     would discard the very signal AUC summarizes). Normalized by horizon
    #     so runs of different length are comparable. ---
    if n_ep > 1:
        auc = float(_trapz(returns, episodes) / (episodes[-1] - episodes[0]))
    else:
        auc = float(returns[0]) if n_ep else None

    # --- sustained-crossing convergence on the SMOOTHED curve, evaluated only
    #     where a full window exists. Requires the smoothed return to stay >=
    #     threshold for hold_fraction of the *remaining* episodes. ---
    smoothed = _smooth(returns, cfg.smooth_window)
    convergence_episode = _sustained_crossing(
        smoothed, episodes, cfg.convergence_threshold, cfg.hold_fraction
    )

    # --- wall time, episode length ---
    wall_time_s = float(log_df['wall_time'].iloc[-1]) if 'wall_time' in log_df else None
    lengths = log_df['length'].to_numpy(dtype=float) if 'length' in log_df else np.array([])
    mean_episode_length_final = _windowed_mean(lengths, 100, 'tail') if len(lengths) else None

    # --- optional diagnostic columns ---
    sigma_final = _last_clean(log_df, 'sigma_mean')
    critic_loss_final = _tail_mean_clean(log_df, 'critic_loss', 100)
    td_error_final = _tail_mean_clean(log_df, 'mean_td_error', 100, absolute=True)

    # --- plateau: first episode after which the best improvement over the next
    #     plateau_window episodes is < plateau_rel_eps * return_range.
    #     Range-relative so it means the same thing regardless of return scale. ---
    plateau_episode = _plateau(
        smoothed, episodes, cfg.plateau_window,
        cfg.plateau_rel_eps * return_range if return_range > 0 else None
    )

    # --- regression: peak-window-mean vs final-window-mean (consistent estimators) ---
    regressed = bool(
        peak_eval_mean is not None and final_eval_mean is not None
        and peak_eval_mean > 0
        and (peak_eval_mean - final_eval_mean) > cfg.regress_rel_drop * peak_eval_mean
    )

    return {
        'n_episodes': int(n_ep),
        'n_eval_checkpoints': int(len(eval_returns)),
        'final_return_mean': _round(final_return_mean),
        'final_return_std': _round(final_return_std),
        'final_eval_mean': _round(final_eval_mean),
        'final_eval_std': _round(final_eval_std),
        'final_eval_avg_per_step': _round(final_eval_avg_per_step, 3),
        'peak_eval_mean': _round(peak_eval_mean),
        'peak_eval_episode': peak_eval_episode,
        'convergence_episode': convergence_episode,
        'auc_return': _round(auc),
        'wall_time_s': _round(wall_time_s, 1),
        'mean_episode_length_final': _round(mean_episode_length_final, 1),
        'sigma_final': _round(sigma_final, 4),
        'critic_loss_final': _round(critic_loss_final, 3),
        'td_error_final': _round(td_error_final, 4),
        'plateau_episode': plateau_episode,
        'regressed': regressed,
    }


def _sustained_crossing(smoothed, episodes, threshold, hold_fraction):
    """First episode where smoothed >= threshold AND stays >= threshold for
    hold_fraction of the remaining episodes. Ignores NaN warm-up region."""
    n = len(smoothed)
    for i in range(n):
        v = smoothed[i]
        if np.isnan(v):
            continue
        if v >= threshold:
            remaining = n - i
            hold = max(1, int(round(hold_fraction * remaining)))
            window = smoothed[i:i + hold]
            # Treat NaN inside the hold window as failure to sustain
            if np.all(~np.isnan(window)) and np.all(window >= threshold):
                return int(episodes[i])
    return None


def _plateau(smoothed, episodes, window, abs_eps):
    """First episode where future improvement within `window` < abs_eps."""
    if abs_eps is None:
        return None
    n = len(smoothed)
    for i in range(n - window):
        seg = smoothed[i:i + window]
        if np.any(np.isnan(seg)):
            continue
        if float(np.max(seg) - seg[0]) < abs_eps:
            return int(episodes[i])
    return None


def _last_clean(df, col):
    if col not in df.columns:
        return None
    s = df[col].dropna()
    return float(s.iloc[-1]) if len(s) else None


def _tail_mean_clean(df, col, n, absolute=False):
    if col not in df.columns:
        return None
    s = df[col].dropna()
    if not len(s):
        return None
    seg = s.iloc[-min(n, len(s)):]
    if absolute:
        seg = seg.abs()
    return float(seg.mean())


# ===========================================================================
# Tier 2 — per-config aggregate across seeds
# ===========================================================================

def aggregate_config(run_summaries, cfg):
    n = len(run_summaries)

    def vals(key):
        return [r[key] for r in run_summaries if r.get(key) is not None]

    def mean_std(key):
        v = vals(key)
        if not v:
            return None, None
        # ddof=1 (sample std) when we have >1 seed; population std otherwise
        std = float(np.std(v, ddof=1)) if len(v) > 1 else 0.0
        return round(float(np.mean(v)), 2), round(std, 2)

    def median_iqr(key):
        v = vals(key)
        if not v:
            return None, None
        return (
            round(float(np.median(v)), 1),
            round(float(np.percentile(v, 75) - np.percentile(v, 25)), 1),
        )

    mu_final, std_final = mean_std('final_eval_mean')
    mu_avg_step, std_avg_step = mean_std('final_eval_avg_per_step')
    mu_peak, std_peak = mean_std('peak_eval_mean')
    mu_auc, std_auc = mean_std('auc_return')
    conv_med, conv_iqr = median_iqr('convergence_episode')
    final_vals = vals('final_eval_mean')

    # Stability: prefer absolute cross-seed std (returns are on a fixed scale here).
    # Report CV ONLY when the mean is large enough that the ratio is meaningful,
    # and only when we have >1 seed. Otherwise CV is None (not a misleading number).
    cv = None
    if (
        n > 1 and std_final is not None and mu_final is not None
        and mu_final >= cfg.min_mean_for_cv
    ):
        cv = round(std_final / mu_final, 3)

    n_converged = sum(1 for r in run_summaries if r.get('convergence_episode') is not None)

    return {
        'n_seeds': n,
        'final_eval_mean': mu_final,
        'final_eval_avg_per_step': mu_avg_step,
        'final_eval_std': std_final,                 # absolute cross-seed std (primary stability metric)
        'final_eval_min': round(float(min(final_vals)), 2) if final_vals else None,
        'final_eval_max': round(float(max(final_vals)), 2) if final_vals else None,
        'final_eval_range': round(float(max(final_vals) - min(final_vals)), 2) if len(final_vals) > 1 else None,
        'peak_eval_mean': mu_peak,
        'peak_eval_std': std_peak,
        'auc_mean': mu_auc,
        'auc_std': std_auc,
        'convergence_episode_median': conv_med,
        'convergence_episode_iqr': conv_iqr,
        'n_seeds_converged': n_converged,
        'wall_time_mean': round(float(np.mean(vals('wall_time_s'))), 1) if vals('wall_time_s') else None,
        'regressed_fraction': round(sum(r['regressed'] for r in run_summaries) / n, 2) if n else None,
        'seed_sensitivity_cv': cv,                   # None when n=1 or mean too small
        'single_seed': bool(n == 1),                 # explicit flag: stability stats unreliable
    }


# ===========================================================================
# Tier 3 — downsampled eval curves
# ===========================================================================

def fingerprint_curve(eval_df, cfg):
    eps = eval_df['episode_checkpoint'].to_numpy(dtype=int)
    vals = eval_df['eval_mean_return'].to_numpy(dtype=float)
    n = len(eps)
    if n <= cfg.curve_points:
        idx = list(range(n))
    else:
        idx = [int(i) for i in np.linspace(0, n - 1, cfg.curve_points)]
    return [{'episode': int(eps[i]), 'eval_mean_return': round(float(vals[i]), 2)} for i in idx]


def cross_seed_curves(eval_dfs):
    """Episode-ALIGNED mean/std across seeds.

    Aligns by episode_checkpoint value (not list position), so seeds that ran a
    different number of checkpoints — or were resumed — don't silently misalign.
    Only episodes present in ALL seeds are reported.
    """
    if not eval_dfs:
        return []
    per_seed = []
    for df in eval_dfs:
        m = {int(e): float(v) for e, v in
             zip(df['episode_checkpoint'], df['eval_mean_return'])}
        per_seed.append(m)
    common = set(per_seed[0])
    for m in per_seed[1:]:
        common &= set(m)
    result = []
    for ep in sorted(common):
        vs = [m[ep] for m in per_seed]
        std = float(np.std(vs, ddof=1)) if len(vs) > 1 else 0.0
        result.append({
            'episode': int(ep),
            'eval_mean': round(float(np.mean(vs)), 2),
            'eval_std': round(std, 2),
            'n_seeds': len(vs),
        })
    return result


# ===========================================================================
# Tier 4 — findings WITH effect size and significance flags
# ===========================================================================

def _pooled_std(a_std, b_std):
    a = a_std if a_std is not None else 0.0
    b = b_std if b_std is not None else 0.0
    return float(np.sqrt(0.5 * (a ** 2 + b ** 2)))


def _compare(name_a, a, name_b, b, cfg):
    """Effect-size-aware comparison of two configs' final_eval."""
    ma, mb = a['final_eval_mean'] or 0.0, b['final_eval_mean'] or 0.0
    sa, sb = a.get('final_eval_std'), b.get('final_eval_std')
    pooled = _pooled_std(sa, sb)
    margin = ma - mb
    margin_in_std = round(margin / pooled, 2) if pooled > 0 else None
    overlapping = bool(pooled > 0 and abs(margin) < cfg.overlap_sigma * pooled)
    return {
        'a': name_a, 'b': name_b,
        'a_final': round(ma, 2), 'b_final': round(mb, 2),
        'a_std': sa, 'b_std': sb,
        'margin': round(margin, 2),
        'pooled_std': round(pooled, 2),
        'margin_in_pooled_std': margin_in_std,
        'winner': name_a if margin >= 0 else name_b,
        'overlapping_within_1std': overlapping,
        'verdict': 'inconclusive (overlapping)' if overlapping else 'separated',
    }


def _label(c):
    lr = c.get('lr')
    lr_str = 'na' if lr is None else f"{lr:.0e}"
    return f"{c['algorithm']}  lr={lr_str}  upd={c['update_every']}"


def derive_findings(per_config, cfg):
    if not per_config:
        return {}

    ranked = sorted(per_config, key=lambda x: x['final_eval_mean'] or 0, reverse=True)
    best = ranked[0]
    runner_up = ranked[1] if len(ranked) > 1 else None

    # D3: gate the headline on statistical separation. If the top two configs
    # overlap within one pooled std, report a TIE rather than a noisy winner.
    best_vs_runner = (
        _compare(_label(best), best, _label(runner_up), runner_up, cfg)
        if runner_up is not None else None)
    if best_vs_runner is not None and best_vs_runner['overlapping_within_1std']:
        best_overall_label = f"TIE: {_label(best)}  ≈  {_label(runner_up)}"
    else:
        best_overall_label = _label(best)

    by_algo = defaultdict(list)
    for c in per_config:
        by_algo[c['algorithm']].append(c)

    best_per_algo = {
        algo: max(cfgs, key=lambda x: x['final_eval_mean'] or 0)
        for algo, cfgs in by_algo.items()
    }
    best_per_algo_summary = {
        algo: {
            'lr': c['lr'],
            'update_every': c['update_every'],
            'final_eval_mean': c['final_eval_mean'],
            'final_eval_std': c['final_eval_std'],
            'auc_mean': c['auc_mean'],
            'convergence_episode_median': c['convergence_episode_median'],
            'seed_sensitivity_cv': c['seed_sensitivity_cv'],
            'regressed_fraction': c['regressed_fraction'],
            'n_seeds': c['n_seeds'],
        }
        for algo, c in best_per_algo.items()
    }

    # Stability findings: only over multi-seed, meaningful configs with a defined CV.
    stable_pool = [
        c for c in per_config
        if not c['single_seed']
        and (c['final_eval_mean'] or 0) > cfg.meaningful_floor
        and c['seed_sensitivity_cv'] is not None
    ]
    most_stable = min(stable_pool, key=lambda x: x['seed_sensitivity_cv']) if stable_pool else None
    most_unstable = max(stable_pool, key=lambda x: x['seed_sensitivity_cv']) if stable_pool else None

    converged = [c for c in per_config if c['convergence_episode_median'] is not None]
    fastest = min(converged, key=lambda x: x['convergence_episode_median']) if converged else None

    most_regressed = max(per_config, key=lambda x: x['regressed_fraction'] or 0)

    # Class-level bests
    def class_best(algos):
        pool = [c for c in per_config if c['algorithm'] in algos]
        return max(pool, key=lambda x: x['final_eval_mean'] or 0) if pool else None

    reinforce_cfg = class_best({'reinforce'})
    baseline_cfg = class_best({'reinforce_batch', 'reinforce_ema', 'reinforce_fixed'})
    ac_cfg = class_best({'ac_td', 'ac_mc'})
    ac_td_cfg = best_per_algo.get('ac_td')
    ac_mc_cfg = best_per_algo.get('ac_mc')

    findings = {
        'n_configs': len(per_config),
        'n_single_seed_configs': sum(1 for c in per_config if c['single_seed']),
        'best_overall': best_overall_label,
        'best_overall_final_eval': best['final_eval_mean'],
        'best_overall_std': best['final_eval_std'],
        'best_per_algorithm': best_per_algo_summary,
        'variance_reduction_ladder': sorted(
            [
                {
                    'algorithm': algo,
                    'best_lr': d['lr'],
                    'best_upd': d['update_every'],
                    'final_eval_mean': d['final_eval_mean'],
                    'final_eval_std': d['final_eval_std'],
                    'seed_cv': d['seed_sensitivity_cv'],
                }
                for algo, d in best_per_algo_summary.items()
            ],
            key=lambda x: x['final_eval_mean'] or 0,
            reverse=True,
        ),
    }

    # Top-1 vs top-2 with significance
    if best_vs_runner is not None:
        findings['best_vs_runner_up'] = best_vs_runner

    findings['most_stable'] = (
        {'config': _label(most_stable), 'cv': most_stable['seed_sensitivity_cv']}
        if most_stable else None
    )
    findings['most_unstable'] = (
        {'config': _label(most_unstable), 'cv': most_unstable['seed_sensitivity_cv']}
        if most_unstable else None
    )
    findings['fastest_convergence'] = (
        {'config': _label(fastest), 'median_episode': fastest['convergence_episode_median']}
        if fastest else None
    )
    findings['most_regressed'] = {
        'config': _label(most_regressed),
        'regressed_fraction': most_regressed['regressed_fraction'],
    }

    # Effect-size-aware class comparisons (the assignment's core questions)
    if reinforce_cfg and baseline_cfg:
        findings['baseline_vs_reinforce'] = _compare(
            'best_baseline (' + _label(baseline_cfg) + ')', baseline_cfg,
            'reinforce (' + _label(reinforce_cfg) + ')', reinforce_cfg, cfg
        )
    if reinforce_cfg and ac_cfg:
        findings['actor_critic_vs_reinforce'] = _compare(
            'best_AC (' + _label(ac_cfg) + ')', ac_cfg,
            'reinforce (' + _label(reinforce_cfg) + ')', reinforce_cfg, cfg
        )
    if ac_td_cfg and ac_mc_cfg:
        findings['ac_td_vs_ac_mc'] = _compare(
            'ac_td (' + _label(ac_td_cfg) + ')', ac_td_cfg,
            'ac_mc (' + _label(ac_mc_cfg) + ')', ac_mc_cfg, cfg
        )

    return findings


# ===========================================================================
# Directory walker
# ===========================================================================

def walk_results(results_dir, intersect_with=None):
    """Yield (algorithm, lr, update_every, seed, seed_dir) for each complete run.

    Recursively finds all eval_log.csv files and uses regex to extract the
    configuration from the path, making it fully invariant to folder nesting depth.
    """
    root = Path(results_dir)
    intersect_root = Path(intersect_with) if intersect_with else None
    
    # Sort for deterministic yielding
    root_path = Path(results_dir).resolve()
    for p in sorted(root_path.rglob('eval_log.csv')):
        rel_parts = p.relative_to(root_path).parts
        if any(part in ('_archive', '_smoke_test', 'plots') for part in rel_parts):
            continue

        seed_dir = p.parent
        if not _complete(seed_dir, require_log=False):
            continue
            
        path_str = str(seed_dir.relative_to(root_path)) if str(root_path) != '.' else str(seed_dir)
        
        # Extract Algorithm (longest match wins to prevent 'reinforce' matching 'reinforce_batch')
        algos = ['reinforce_batch', 'reinforce_ema', 'reinforce_fixed', 'reinforce', 'ac_mc', 'ac_td']
        found = [a for a in algos if a in path_str]
        if not found:
            continue
        algorithm = max(found, key=len)
        
        # Extract LR, UPD, SEED
        m_lr = re.search(r'lr([\d.eE+\-]+)', path_str)
        lr = float(m_lr.group(1)) if m_lr else float('nan')
        
        m_upd = re.search(r'upd(\d+)', path_str)
        upd = int(m_upd.group(1)) if m_upd else 1
        
        m_seed = re.search(r'seed_?(\d+)', path_str)
        seed = int(m_seed.group(1)) if m_seed else -1

        if intersect_root:
            intersect_rel = seed_dir.relative_to(root_path)
            if not _complete(intersect_root / intersect_rel, require_log=False):
                continue
                
        yield algorithm, lr, upd, seed, seed_dir


def _parse_seed(name):
    try:
        return int(name.split('_')[1])
    except (IndexError, ValueError):
        return -1


def _complete(seed_dir, require_log=True):
    if require_log:
        return (seed_dir / 'log.csv').exists() and (seed_dir / 'eval_log.csv').exists()
    return (seed_dir / 'summary.json').exists() or (seed_dir / 'eval_log.csv').exists()


# ===========================================================================
# Main assembly
# ===========================================================================

def generate_summary(results_dir, output_path, cfg, intersect_with=None):
    per_run = []
    curves_per_run = []
    config_runs = defaultdict(list)
    config_eval_dfs = defaultdict(list)

    total = 0
    for algorithm, lr, upd, seed, seed_dir in walk_results(results_dir, intersect_with):
        try:
            log_df = pd.read_csv(seed_dir / 'log.csv')
        except FileNotFoundError:
            log_df = pd.DataFrame()
            
        eval_df = pd.read_csv(seed_dir / 'eval_log.csv')

        if len(eval_df) == 0:
            continue

        metrics = summarize_run(log_df, eval_df, cfg)
        lr_key = None if (isinstance(lr, float) and np.isnan(lr)) else lr
        per_run.append({
            'algorithm': algorithm, 'lr': lr_key, 'update_every': upd, 'seed': seed,
            **metrics,
        })
        curves_per_run.append({
            'algorithm': algorithm, 'lr': lr_key, 'update_every': upd, 'seed': seed,
            'points': fingerprint_curve(eval_df, cfg),
        })

        key = (algorithm, lr_key, upd)
        config_runs[key].append(metrics)
        config_eval_dfs[key].append(eval_df)
        total += 1

    per_config = []
    agg_curves = []
    for key in sorted(config_runs, key=lambda k: (k[0], -1 if k[1] is None else k[1], k[2])):
        algorithm, lr_key, upd = key
        agg = aggregate_config(config_runs[key], cfg)
        per_config.append({'algorithm': algorithm, 'lr': lr_key, 'update_every': upd, **agg})
        agg_curves.append({
            'algorithm': algorithm, 'lr': lr_key, 'update_every': upd,
            'cross_seed': cross_seed_curves(config_eval_dfs[key]),
        })

    findings = derive_findings(per_config, cfg)

    summary = {
        'metadata': {
            'n_runs': total,
            'n_configs': len(per_config),
            'config': cfg.as_dict(),
            'notes': {
                'auc': 'computed on RAW returns, horizon-normalized',
                'convergence': 'sustained crossing of smoothed return; warm-up window excluded',
                'peak_and_final': 'both windowed means (consistent estimators) so regression is not biased by a single lucky checkpoint',
                'plateau_eps': 'range-relative: plateau_rel_eps * (max-min return) of that run',
                'stability': 'primary metric is absolute cross-seed std; CV reported only when n_seeds>1 and mean>=min_mean_for_cv',
                'findings_significance': 'comparisons report margin_in_pooled_std and overlapping_within_1std',
            },
        },
        'per_run': per_run,
        'per_config': per_config,
        'curves': curves_per_run,
        'cross_seed_curves': agg_curves,
        'findings': findings,
    }

    with open(output_path, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"\nWrote {output_path}  ({total} runs, {len(per_config)} configs)")
    return summary


def build_config_from_args(args):
    return SummaryConfig(
        convergence_threshold=args.convergence_threshold,
        hold_fraction=args.hold_fraction,
        smooth_window=args.smooth_window,
        final_eval_checkpoints=args.final_eval_checkpoints,
        peak_window_checkpoints=args.peak_window_checkpoints,
        regress_rel_drop=args.regress_rel_drop,
        plateau_window=args.plateau_window,
        plateau_rel_eps=args.plateau_rel_eps,
        curve_points=args.curve_points,
        min_mean_for_cv=args.min_mean_for_cv,
        overlap_sigma=args.overlap_sigma,
        meaningful_floor=args.meaningful_floor,
    )


def main():
    p = argparse.ArgumentParser(
        description='Generate a statistically defensible summary.json from Part 1 sweep results',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument('--results-dir', default='results', help='Root results directory')
    p.add_argument('--intersect-with', default=None,
                   help='If provided, only process runs that ALSO exist and are complete in this parallel directory tree')
    p.add_argument('--output', default='summary.json', help='Output JSON path')
    p.add_argument('--convergence-threshold', type=float, default=1200.0,
                   help='Smoothed-return level that counts as converged')
    p.add_argument('--hold-fraction', type=float, default=0.10,
                   help='Crossing must hold for this fraction of remaining episodes')
    p.add_argument('--smooth-window', type=int, default=100,
                   help='Rolling window for smoothing (curves + convergence only)')
    p.add_argument('--final-eval-checkpoints', type=int, default=10,
                   help='Number of trailing eval checkpoints in the final window')
    p.add_argument('--peak-window-checkpoints', type=int, default=3,
                   help='Width of the rolling window used to define peak (windowed, not single max)')
    p.add_argument('--regress-rel-drop', type=float, default=0.15,
                   help='Final below peak by this fraction (both windowed means) => regressed')
    p.add_argument('--plateau-window', type=int, default=500,
                   help='Look-ahead window (episodes) for plateau detection')
    p.add_argument('--plateau-rel-eps', type=float, default=0.02,
                   help='Improvement < this * return_range over the window => plateau')
    p.add_argument('--curve-points', type=int, default=25,
                   help='Downsampled points per eval curve')
    p.add_argument('--min-mean-for-cv', type=float, default=200.0,
                   help='Below this final-eval mean, CV is suppressed (report std instead)')
    p.add_argument('--overlap-sigma', type=float, default=1.0,
                   help='Findings flagged "overlapping" if margin < this many pooled std')
    p.add_argument('--meaningful-floor', type=float, default=200.0,
                   help='Configs below this final-eval excluded from stability findings')
    args = p.parse_args()

    cfg = build_config_from_args(args)
    generate_summary(args.results_dir, args.output, cfg, args.intersect_with)


if __name__ == '__main__':
    main()
import json
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def load_summary(path):
    with open(path, 'r') as f:
        return json.load(f)

d_post = load_summary('results/summary_post.json')

variants = {
    'reinforce': 'REINFORCE (vanilla)',
    'reinforce_fixed': '\\;+ constant baseline',
    'reinforce_batch': '\\;+ batch baseline',
    'reinforce_ema': '\\;+ EMA baseline',
    'ac_mc': 'Actor--Critic (MC)',
    'ac_td': 'Actor--Critic (TD)'
}

# Group configs by algorithm and sort by iqm_return to get top 3
top_configs_by_algo = {}
for cfg in d_post['per_config']:
    algo = cfg['algorithm']
    if algo not in top_configs_by_algo:
        top_configs_by_algo[algo] = []
    top_configs_by_algo[algo].append(cfg)

for algo in top_configs_by_algo:
    top_configs_by_algo[algo] = sorted(top_configs_by_algo[algo], key=lambda x: x['iqm_return'], reverse=True)[:3]

top_config_signatures = set()
for algo, cfgs in top_configs_by_algo.items():
    for cfg in cfgs:
        top_config_signatures.add((cfg['algorithm'], cfg['lr'], cfg['update_every']))

def draw_grid_and_labels(ax):
    ax.axhline(100, color='lightgray', linestyle='--')
    ax.axhline(500, color='lightgray', linestyle='--')
    ax.axvline(1.3, color='lightgray', linestyle='--')
    ax.text(2.65, 850, 'sustained-hopper', color='gray', fontsize=10, ha='center', va='center')
    ax.text(0.15, 850, 'stander', color='gray', fontsize=10, ha='center', va='center')
    ax.text(2.65, 300, 'hopper-faller', color='gray', fontsize=10, ha='center', va='center')
    ax.text(0.15, 300, 'stutterer', color='gray', fontsize=10, ha='center', va='center')
    ax.text(2.65, -50, 'leap-crasher', color='gray', fontsize=10, ha='center', va='center')
    ax.text(0.15, -50, 'collapsed', color='gray', fontsize=10, ha='center', va='center')

algo_colors = {
    'reinforce': '#E6194B',       # Red
    'reinforce_fixed': '#3CB44B', # Green
    'reinforce_batch': '#42D4F4', # Cyan
    'reinforce_ema': '#4363D8',   # Blue
    'ac_mc': '#F58231',           # Orange
    'ac_td': '#911EB4'            # Purple
}

def plot_behavior_plane(stage='final', use_all_configs=False, filename='behavior_plane.png'):
    fig, ax = plt.subplots(figsize=(10, 7))
    draw_grid_and_labels(ax)
    
    for algo_key, color in algo_colors.items():
        if use_all_configs:
            algo_runs = [r for r in d_post['per_run'] if r['algorithm'] == algo_key]
            scatter_alpha = 0.4
            scatter_size = 20
            edge_lw = 0.3
        else:
            # filter for top 3 configs (15 seeds max)
            algo_runs = [r for r in d_post['per_run'] 
                         if r['algorithm'] == algo_key 
                         and (r['algorithm'], r['lr'], r['update_every']) in top_config_signatures]
            scatter_alpha = 0.9
            scatter_size = 40
            edge_lw = 0.8
                     
        if stage == 'final':
            x_vals = [r['final_velocity'] for r in algo_runs]
            y_vals = [r['final_survival'] for r in algo_runs]
        else:
            x_vals = [r['peak_velocity'] for r in algo_runs]
            y_vals = [r['peak_survival'] for r in algo_runs]
        
        # Advanced visualization: 2D KDE contour plot for density representation
        if np.std(x_vals) > 1e-3 and np.std(y_vals) > 1e-3:
            try:
                # Fill with soft alpha, no outer lines to avoid spaghetti overlap
                sns.kdeplot(x=x_vals, y=y_vals, ax=ax, fill=True, color=color, alpha=0.1, levels=3, warn_singular=False, zorder=1)
            except Exception:
                pass
        
        # More prominent individual points for top 3, fainter for all configs to reduce blot
        ax.scatter(x_vals, y_vals, alpha=scatter_alpha, color=color, s=scatter_size, edgecolor='white', linewidth=edge_lw, zorder=3, label=variants[algo_key])

    ax.set_xlim(-1, 4)
    ax.set_ylim(-200, 1200)
    ax.set_yticks([0, 200, 400, 600, 800, 1000])
    ax.set_xlabel("Velocity (return/step - 1)")
    ax.set_ylabel("Survival (episode length)")
    ax.legend(loc='upper right', bbox_to_anchor=(1.4, 1))
    
    os.makedirs('results', exist_ok=True)
    plt.tight_layout()
    plt.savefig(f'results/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

# Generate for both 'final' and 'best' models, with both top3 and all configs
plot_behavior_plane(stage='final', use_all_configs=False, filename='behavior_plane_top3_final.png')
plot_behavior_plane(stage='best', use_all_configs=False, filename='behavior_plane_top3_best.png')
plot_behavior_plane(stage='final', use_all_configs=True, filename='behavior_plane_all_final.png')
plot_behavior_plane(stage='best', use_all_configs=True, filename='behavior_plane_all_best.png')
print("Plots generated: behavior_plane_top3_final.png, behavior_plane_top3_best.png, behavior_plane_all_final.png, behavior_plane_all_best.png")

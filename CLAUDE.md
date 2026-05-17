# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a course project (FAIML - 01VSDWS) implementing reinforcement learning in two parts:
- **Part 1**: Custom REINFORCE and Actor-Critic on the MuJoCo **Hopper-v4** environment
- **Part 2**: SB3-based DDPG training on the **PandaPush-v3** environment with Uniform Domain Randomization (UDR) and Automatic Domain Randomization (ADR)

## Environment Setup

```bash
# Activate the local venv
source venv/bin/activate

# Install base dependencies
pip install -r requirements.txt

# Install panda-gym (required for Part 2)
cd part2/panda-gym
pip install -e .
```

## Running Scripts

```bash
# Part 1 — verify Hopper environment works
python part1/test_random_policy.py

# Part 1 — train REINFORCE / Actor-Critic (training loop is a TODO)
python part1/train.py

# Part 2 — verify PandaPush environment works
python part2/test_random_policy.py

# Part 2 — train with SB3 (uses DDPG; sampling strategy: none | udr | adr)
python part2/train_sb3.py --sampling-strategy none --env-type source --timesteps 500000

# Part 2 — evaluate a saved model
python part2/eval_sb3.py --model-path <path/to/model.zip> --episodes 500 --env-type target
```

## Architecture

### Part 1 — Custom Policy Gradient (`part1/`)

- `agent.py`: Contains `Policy` (a PyTorch `nn.Module` with an actor head and a stub critic head) and `Agent` (wraps the policy, holds episode buffers, and exposes `get_action` / `store_outcome` / `update_policy`).
  - The actor outputs a Gaussian distribution over the 3-dimensional continuous action space.
  - `sigma` is a **learned** parameter (initialized to 0.5, passed through `softplus`).
  - `update_policy` is the primary TODO site for REINFORCE (Task 2) and Actor-Critic (Task 3).
  - The critic network layers and its forward pass are also TODOs inside `Policy`.
- `train.py`: Skeleton training loop — instantiate env, agent, run episodes, call `update_policy`. Needs to be completed.

### Part 2 — SB3 + Domain Randomization (`part2/`)

- `train_sb3.py`: Creates a `PandaPush-v3` gym environment, optionally wraps it with `RandomizationWrapper`, trains a DDPG model via SB3, and saves it. The model creation and save call are TODOs.
- `eval_sb3.py`: Loads a saved SB3 model zip and evaluates it for N episodes, reporting mean/std return and success rate.
- `rand_wrapper.py`: `RandomizationWrapper(gym.Wrapper)` — resamples the PyBullet object mass at every `reset()` call. Currently only `mode="none"` is implemented; `udr` and `adr` are TODOs. The ADR variant needs to track `mass_min`, `mass_max`, and `last_sample_type` attributes that the print statement in `reset()` already references.

### Environments

| Env | State | Action | Episode ends |
|-----|-------|--------|-------------|
| Hopper-v4 | 11-dim (torso height, pitch, joint angles + velocities; x-pos excluded) | 3-dim continuous torques ∈ [−1, 1] | height < 0.7 m, \|pitch\| > 0.2 rad, or 1000 steps |
| PandaPush-v3 | dict obs (`observation`, `achieved_goal`, `desired_goal`) | 4-dim end-effector delta | success or max steps |

Hopper reward: `x_velocity + 1.0 (alive bonus) − 0.001 × ‖action‖²`

### Key implementation notes

- `discount_rewards` in `agent.py` computes Monte-Carlo returns in reverse order — used by REINFORCE.
- For Actor-Critic (Task 3), use bootstrapped returns: `R_t = r_t + γ * V(s_{t+1}) * (1 - done_t)`.
- `RandomizationWrapper.reset()` accesses the PyBullet sim via `self.env.unwrapped.task.sim`; the object body ID comes from `sim._bodies_idx["object"]` and mass is set via `sim.physics_client.changeDynamics(bodyUniqueId=..., linkIndex=-1, mass=...)`.
- Render is disabled by default in all scripts (`render = False`). Rendering requires a display; on headless machines use `pyvirtualdisplay`.

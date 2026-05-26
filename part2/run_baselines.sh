#!/bin/bash

# Exit on error
set -e

echo "================================================================"
echo " Starting Phase 1: Lower and Upper Bounds Benchmarking"
echo "================================================================"

# Activate the virtual environment if not already activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source ../venv/bin/activate
fi

# Define timesteps for convergence (e.g. 200,000 to 300,000)
TIMESTEPS=300000

echo ""
echo "----------------------------------------------------------------"
echo " STEP 1: Algorithm Selection (Train PPO & SAC on Source)"
echo "----------------------------------------------------------------"
echo "Training PPO on Source..."
python3 train_sb3.py --algo ppo --env-type source --timesteps $TIMESTEPS --seed 1

echo "Training SAC on Source..."
python3 train_sb3.py --algo sac --env-type source --timesteps $TIMESTEPS --seed 1

echo ""
echo "----------------------------------------------------------------"
echo " STEP 2: Evaluate both on Source (Reference)"
echo "----------------------------------------------------------------"
echo "Evaluating PPO on Source..."
python3 eval_sb3.py --algo ppo --model-path results/ppo_source_none_seed1/best_model.zip --env-type source --episodes 500

echo "Evaluating SAC on Source..."
python3 eval_sb3.py --algo sac --model-path results/sac_source_none_seed1/best_model.zip --env-type source --episodes 500

echo ""
echo "----------------------------------------------------------------"
echo " STEP 3: Evaluate both on Target (LOWER BOUND)"
echo "----------------------------------------------------------------"
echo "Evaluating PPO on Target..."
python3 eval_sb3.py --algo ppo --model-path results/ppo_source_none_seed1/best_model.zip --env-type target --episodes 500

echo "Evaluating SAC on Target..."
python3 eval_sb3.py --algo sac --model-path results/sac_source_none_seed1/best_model.zip --env-type target --episodes 500

echo ""
echo "----------------------------------------------------------------"
echo " STEP 4: Train on Target to find UPPER BOUND"
echo "----------------------------------------------------------------"
# (Assuming you picked the winner from step 1, but we train both here just in case)
echo "Training PPO directly on Target..."
python3 train_sb3.py --algo ppo --env-type target --timesteps $TIMESTEPS --seed 1

echo "Training SAC directly on Target..."
python3 train_sb3.py --algo sac --env-type target --timesteps $TIMESTEPS --seed 1

echo ""
echo "----------------------------------------------------------------"
echo " STEP 5: Evaluate on Target (UPPER BOUND) & Record Videos"
echo "----------------------------------------------------------------"
echo "Evaluating PPO on Target (Upper Bound)..."
python3 eval_sb3.py --algo ppo --model-path results/ppo_target_none_seed1/best_model.zip --env-type target --episodes 500 --record-video

echo "Evaluating SAC on Target (Upper Bound)..."
python3 eval_sb3.py --algo sac --model-path results/sac_target_none_seed1/best_model.zip --env-type target --episodes 500 --record-video

echo ""
echo "================================================================"
echo " Phase 1 Complete! Compare results to pick best algorithm."
echo "================================================================"

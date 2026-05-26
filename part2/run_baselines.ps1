$ErrorActionPreference = "Stop"

Write-Host "================================================================"
Write-Host " Starting Phase 1: Lower and Upper Bounds Benchmarking"
Write-Host "================================================================"

# Activate the virtual environment if not already activated
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Activating virtual environment..."
    # In Windows, venv uses \Scripts\ instead of /bin/
    if (Test-Path "..\venv\Scripts\Activate.ps1") {
        . "..\venv\Scripts\Activate.ps1"
    } else {
        Write-Warning "Could not find virtual environment at ..\venv\Scripts\Activate.ps1"
    }
}

$TIMESTEPS = 300000

Write-Host ""
Write-Host "----------------------------------------------------------------"
Write-Host " STEP 1: Algorithm Selection (Train PPO & SAC on Source)"
Write-Host "----------------------------------------------------------------"
Write-Host "Training PPO on Source..."
python train_sb3.py --algo ppo --env-type source --timesteps $TIMESTEPS --seed 1

Write-Host "Training SAC on Source..."
python train_sb3.py --algo sac --env-type source --timesteps $TIMESTEPS --seed 1

Write-Host ""
Write-Host "----------------------------------------------------------------"
Write-Host " STEP 2: Evaluate both on Source (Reference)"
Write-Host "----------------------------------------------------------------"
Write-Host "Evaluating PPO on Source..."
python eval_sb3.py --algo ppo --model-path results/ppo_source_none_seed1/best_model.zip --env-type source --episodes 500

Write-Host "Evaluating SAC on Source..."
python eval_sb3.py --algo sac --model-path results/sac_source_none_seed1/best_model.zip --env-type source --episodes 500

Write-Host ""
Write-Host "----------------------------------------------------------------"
Write-Host " STEP 3: Evaluate both on Target (LOWER BOUND)"
Write-Host "----------------------------------------------------------------"
Write-Host "Evaluating PPO on Target..."
python eval_sb3.py --algo ppo --model-path results/ppo_source_none_seed1/best_model.zip --env-type target --episodes 500

Write-Host "Evaluating SAC on Target..."
python eval_sb3.py --algo sac --model-path results/sac_source_none_seed1/best_model.zip --env-type target --episodes 500

Write-Host ""
Write-Host "----------------------------------------------------------------"
Write-Host " STEP 4: Train on Target to find UPPER BOUND"
Write-Host "----------------------------------------------------------------"
Write-Host "Training PPO directly on Target..."
python train_sb3.py --algo ppo --env-type target --timesteps $TIMESTEPS --seed 1

Write-Host "Training SAC directly on Target..."
python train_sb3.py --algo sac --env-type target --timesteps $TIMESTEPS --seed 1

Write-Host ""
Write-Host "----------------------------------------------------------------"
Write-Host " STEP 5: Evaluate on Target (UPPER BOUND) & Record Videos"
Write-Host "----------------------------------------------------------------"
Write-Host "Evaluating PPO on Target (Upper Bound)..."
python eval_sb3.py --algo ppo --model-path results/ppo_target_none_seed1/best_model.zip --env-type target --episodes 500 --record-video

Write-Host "Evaluating SAC on Target (Upper Bound)..."
python eval_sb3.py --algo sac --model-path results/sac_target_none_seed1/best_model.zip --env-type target --episodes 500 --record-video

Write-Host ""
Write-Host "================================================================"
Write-Host " Phase 1 Complete! Compare results to pick best algorithm."
Write-Host "================================================================"

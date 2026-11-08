#!/usr/bin/env bash
set -euo pipefail
# G4 pilot: GRPO on the forecast layer (docs/rl_forecast_design.md).
# Policy init + KL reference = E11 merged into base; fresh LoRA on top.
ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="$ROOT/artifacts/gemma4_e4b_merged_e11_defcon"
export FPL_GRPO_OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_g4_forecast_v2"
export FPL_G4_TRAIN_SPEC="2023-24,2024-25,2025-26-early,2025-26:29"
export FPL_GRPO_NUM_GENERATIONS=4
export FPL_GRPO_NUM_EPOCHS=2
export FPL_GRPO_TEMPERATURE=0.8
export FPL_GRPO_KL_BETA=0.04
export FPL_GRPO_LEARNING_RATE=2e-5
export FPL_GRPO_MAX_COMPLETION_LENGTH=96
export FPL_GRPO_GRAD_ACCUM=4
export FPL_GRPO_SAVE_STEPS=100
export FPL_G4_TRACE="$ROOT/logs/g4_reward_trace.jsonl"
mkdir -p logs
echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
python -u train_gemma_grpo_forecast.py 2>&1 | tee logs/train_g4_forecast_v2.log

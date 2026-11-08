#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_player_forecast_residual_2025_26_gw1_25_top128_eval_gw26"
OUTPUT_DIR="$ROOT/artifacts/gemma4_31b_lora_player_forecast_residual_gw1_25_top128"
LOG="$ROOT/logs/train_player_forecast_residual_gw1_25_top128.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=800
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS=200
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=8e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=2
export FPL_GEMMA_EVAL_BATCH_SIZE=1
export FPL_GEMMA_GRAD_ACCUM=8
export FPL_GEMMA_LOGGING_STEPS=1
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=12
export FPL_GEMMA_SAVE_TOTAL_LIMIT=10
export FPL_GEMMA_WARMUP_STEPS=8
export FPL_GEMMA_GRADIENT_CHECKPOINTING=false
export FPL_GEMMA_COMPLETION_ONLY_LOSS=true
export FPL_GEMMA_LORA_R=4
export FPL_GEMMA_LORA_ALPHA=8
export FPL_GEMMA_TARGET_SUFFIXES=self_attn.q_proj.weight,self_attn.v_proj.weight

if [[ -n "${FPL_GEMMA_RESUME_FROM_CHECKPOINT:-}" ]]; then
  echo "Resuming from $FPL_GEMMA_RESUME_FROM_CHECKPOINT"
fi

python -u "$ROOT/train_gemma_sft.py" 2>&1 | tee "$LOG"

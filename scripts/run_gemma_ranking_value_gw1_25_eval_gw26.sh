#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
DATA_DIR="$ROOT/reports/llm_ranking_value_2025_26_gw1_25_eval_gw26"
OUTPUT_DIR="$ROOT/artifacts/gemma4_31b_lora_ranking_value_gw1_25_eval_gw26"
LOG="$ROOT/logs/train_ranking_value_gw1_25_eval_gw26.log"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

if [[ -s "$OUTPUT_DIR/adapter_model.safetensors" && -z "${FPL_GEMMA_FORCE_RETRAIN:-}" ]]; then
  echo "Final adapter already exists at $OUTPUT_DIR/adapter_model.safetensors"
  exit 0
fi

if [[ -z "${FPL_GEMMA_RESUME_FROM_CHECKPOINT:-}" && -d "$OUTPUT_DIR" ]]; then
  latest_checkpoint="$(find "$OUTPUT_DIR" -maxdepth 1 -type d -name 'checkpoint-*' 2>/dev/null | sort -V | tail -1 || true)"
  if [[ -n "$latest_checkpoint" ]]; then
    export FPL_GEMMA_RESUME_FROM_CHECKPOINT="$latest_checkpoint"
  fi
fi

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=2048
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS="${FPL_GEMMA_MAX_STEPS:-1000}"
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=6e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=1
export FPL_GEMMA_EVAL_BATCH_SIZE=1
export FPL_GEMMA_GRAD_ACCUM=16
export FPL_GEMMA_LOGGING_STEPS=1
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=20
export FPL_GEMMA_SAVE_TOTAL_LIMIT=50
export FPL_GEMMA_WARMUP_STEPS=20
export FPL_GEMMA_GRADIENT_CHECKPOINTING=false
export FPL_GEMMA_COMPLETION_ONLY_LOSS=true
export FPL_GEMMA_LORA_R=8
export FPL_GEMMA_LORA_ALPHA=16
export FPL_GEMMA_TARGET_SUFFIXES=self_attn.q_proj.weight,self_attn.v_proj.weight

if [[ -n "${FPL_GEMMA_RESUME_FROM_CHECKPOINT:-}" ]]; then
  echo "Resuming from $FPL_GEMMA_RESUME_FROM_CHECKPOINT"
fi

python -u "$ROOT/train_gemma_sft.py" 2>&1 | tee "$LOG"

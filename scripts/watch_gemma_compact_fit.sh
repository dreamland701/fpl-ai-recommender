#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
DATA_DIR="$ROOT/reports/llm_player_forecast_2025_26_baseline_adjustment_fpl_sky_compact_v1_split_gw26_30"

PRIMARY_LOG="$ROOT/logs/train_player_forecast_v4_compact_2k_qv.log"

FALLBACK_SESSION="fpl_gemma_v4_compact_1536_qonly_r2"
FALLBACK_LOG="$ROOT/logs/train_player_forecast_v4_compact_1536_qonly_r2.log"
FALLBACK_OUTPUT="$ROOT/artifacts/gemma4_31b_lora_player_forecast_v4_compact_1536_qonly_r2"

is_training_running() {
  pgrep -af "$ROOT/train_gemma_sft.py" >/dev/null
}

has_failure() {
  grep -E "OutOfMemory|CUDA out of memory|Traceback|RuntimeError:" "$PRIMARY_LOG" >/dev/null 2>&1
}

has_success() {
  grep -E "train_runtime|TrainOutput" "$PRIMARY_LOG" >/dev/null 2>&1
}

start_fallback() {
  if tmux has-session -t "$FALLBACK_SESSION" 2>/dev/null; then
    return
  fi

  mkdir -p "$ROOT/logs" "$FALLBACK_OUTPUT"
  tmux new-session -d -s "$FALLBACK_SESSION" \
    "cd '$ROOT' && source '$VENV' && PYTORCH_ALLOC_CONF=expandable_segments:True FPL_GEMMA_DATA_DIR='$DATA_DIR' FPL_GEMMA_OUTPUT_DIR='$FALLBACK_OUTPUT' FPL_GEMMA_MAX_SEQ_LENGTH=1536 FPL_GEMMA_NUM_EPOCHS=1 FPL_GEMMA_LEARNING_RATE=8e-5 FPL_GEMMA_GRAD_ACCUM=16 FPL_GEMMA_LOGGING_STEPS=1 FPL_GEMMA_EVAL_STRATEGY=no FPL_GEMMA_SAVE_STEPS=100 FPL_GEMMA_SAVE_TOTAL_LIMIT=2 FPL_GEMMA_WARMUP_STEPS=20 FPL_GEMMA_LORA_R=2 FPL_GEMMA_LORA_ALPHA=4 FPL_GEMMA_TARGET_SUFFIXES=self_attn.q_proj.weight python -u '$ROOT/train_gemma_sft.py' 2>&1 | tee '$FALLBACK_LOG'"
}

while true; do
  if is_training_running; then
    sleep 120
    continue
  fi

  if has_success; then
    exit 0
  fi

  if has_failure; then
    start_fallback
    exit 0
  fi

  sleep 120
done

#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
TRAIN_RUNNER="$ROOT/scripts/run_gemma_ranking_value_gw1_25_eval_gw26.sh"
OUTPUT_DIR="$ROOT/artifacts/gemma4_31b_lora_ranking_value_gw1_25_eval_gw26"
TRAIN_SESSION="fpl_gemma_ranking_value"
LOG="$ROOT/logs/watchdog_ranking_value_training.log"
INTERVAL_SECONDS="${FPL_WATCHDOG_INTERVAL_SECONDS:-300}"

mkdir -p "$ROOT/logs"
exec > >(tee -a "$LOG") 2>&1

echo "[$(date -Is)] Watchdog started; interval=${INTERVAL_SECONDS}s"

while true; do
  if [[ -s "$OUTPUT_DIR/adapter_model.safetensors" ]]; then
    echo "[$(date -Is)] Final adapter exists; watchdog exiting"
    exit 0
  fi

  if pgrep -af "train_gemma_sft.py|eval_gemma_responses.py|pause_eval_resume_ranking_value" | grep -q "python\\|bash"; then
    sleep "$INTERVAL_SECONDS"
    continue
  fi

  echo "[$(date -Is)] No training/eval process found; restarting training"
  tmux kill-session -t "$TRAIN_SESSION" 2>/dev/null || true
  tmux new-session -d -s "$TRAIN_SESSION" "cd '$ROOT' && bash '$TRAIN_RUNNER'"
  sleep 30

  if pgrep -af "train_gemma_sft.py" | grep -q "python"; then
    echo "[$(date -Is)] Training restart confirmed"
  else
    echo "[$(date -Is)] Training restart not yet visible; will check again"
  fi

  sleep "$INTERVAL_SECONDS"
done

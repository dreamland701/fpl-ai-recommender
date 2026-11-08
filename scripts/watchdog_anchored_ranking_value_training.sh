#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
TRAIN_RUNNER="$ROOT/scripts/run_gemma_anchored_ranking_value_gw1_25_eval_gw26.sh"
OUTPUT_DIR="$ROOT/artifacts/gemma4_31b_lora_anchored_ranking_value_gw1_25_eval_gw26"
TRAIN_SESSION="fpl_gemma_anchored_ranking_value"
LOG="$ROOT/logs/watchdog_anchored_ranking_value_training.log"
INTERVAL_SECONDS="${FPL_WATCHDOG_INTERVAL_SECONDS:-300}"
STOP_MARKER="${FPL_WATCHDOG_STOP_MARKER:-$ROOT/reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint160_eval_complete.stop}"

mkdir -p "$ROOT/logs"
exec > >(tee -a "$LOG") 2>&1

echo "[$(date -Is)] Anchored watchdog started; interval=${INTERVAL_SECONDS}s"

while true; do
  if [[ -s "$STOP_MARKER" ]]; then
    echo "[$(date -Is)] Stop marker exists at $STOP_MARKER; watchdog exiting"
    exit 0
  fi

  if [[ -s "$OUTPUT_DIR/adapter_model.safetensors" ]]; then
    echo "[$(date -Is)] Final adapter exists; watchdog exiting"
    exit 0
  fi

  if pgrep -af "train_gemma_sft.py|eval_gemma_responses.py" | grep -q "python"; then
    sleep "$INTERVAL_SECONDS"
    continue
  fi

  echo "[$(date -Is)] No anchored training/eval process found; restarting training"
  tmux kill-session -t "$TRAIN_SESSION" 2>/dev/null || true
  tmux new-session -d -s "$TRAIN_SESSION" "cd '$ROOT' && bash '$TRAIN_RUNNER'"
  sleep 30

  if pgrep -af "train_gemma_sft.py" | grep -q "python"; then
    echo "[$(date -Is)] Anchored training restart confirmed"
  else
    echo "[$(date -Is)] Anchored training restart not yet visible; will check again"
  fi

  sleep "$INTERVAL_SECONDS"
done

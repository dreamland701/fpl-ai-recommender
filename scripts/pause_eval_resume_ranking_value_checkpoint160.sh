#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="/home/wescheng/models/gemma-4-31b-it"
TRAIN_SESSION="fpl_gemma_ranking_value"
TRAIN_SCRIPT="$ROOT/train_gemma_sft.py"
TRAIN_RUNNER="$ROOT/scripts/run_gemma_ranking_value_gw1_25_eval_gw26.sh"
EXAMPLES="$ROOT/reports/llm_ranking_value_2025_26_gw1_25_eval_gw26/eval.jsonl"
ADAPTER_ROOT="$ROOT/artifacts/gemma4_31b_lora_ranking_value_gw1_25_eval_gw26"
CHECKPOINT_STEP="${FPL_INTERIM_CHECKPOINT_STEP:-160}"
CHECKPOINT="$ADAPTER_ROOT/checkpoint-$CHECKPOINT_STEP"
LOG="$ROOT/logs/interim_eval_checkpoint${CHECKPOINT_STEP}_ranking_value.log"

SFT_OUTPUT="$ROOT/reports/gemma4_ranking_value_gw1_25_eval_gw26_sft_checkpoint${CHECKPOINT_STEP}_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_ranking_value_gw1_25_eval_gw26_base_checkpoint${CHECKPOINT_STEP}_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/ranking_value_gw1_25_eval_gw26_checkpoint${CHECKPOINT_STEP}_summary.json"
DETAIL_OUTPUT="$ROOT/reports/ranking_value_gw1_25_eval_gw26_checkpoint${CHECKPOINT_STEP}_rows.json"

mkdir -p "$ROOT/logs" "$ROOT/reports"
exec > >(tee -a "$LOG") 2>&1

echo "[$(date -Is)] Waiting for $CHECKPOINT"
while [[ ! -s "$CHECKPOINT/adapter_model.safetensors" || ! -s "$CHECKPOINT/trainer_state.json" ]]; do
  sleep 60
done

echo "[$(date -Is)] Found checkpoint-$CHECKPOINT_STEP; requesting clean training stop"
if tmux has-session -t "$TRAIN_SESSION" 2>/dev/null; then
  tmux send-keys -t "$TRAIN_SESSION" C-c
else
  echo "[$(date -Is)] Training tmux session $TRAIN_SESSION not found; continuing to process wait"
fi

echo "[$(date -Is)] Waiting for training process to exit and release GPU"
while pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; do
  sleep 10
done

source "$VENV"
cd "$ROOT"

example_count="$(wc -l < "$EXAMPLES" | tr -d ' ')"

echo "[$(date -Is)] Running SFT eval with adapter $CHECKPOINT"
rm -f "$SFT_OUTPUT"
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$CHECKPOINT" \
  --max-new-tokens 180

if [[ -s "$BASE_OUTPUT" && "$(wc -l < "$BASE_OUTPUT" | tr -d ' ')" == "$example_count" ]]; then
  echo "[$(date -Is)] Reusing existing base Gemma predictions at $BASE_OUTPUT"
else
  reusable_base="$(find "$ROOT/reports" -maxdepth 1 -type f -name 'gemma4_ranking_value_gw1_25_eval_gw26_base*_predictions.jsonl' | sort | while read -r candidate; do
    if [[ -s "$candidate" && "$(wc -l < "$candidate" | tr -d ' ')" == "$example_count" ]]; then
      echo "$candidate"
      break
    fi
  done)"
  if [[ -n "$reusable_base" ]]; then
    echo "[$(date -Is)] Reusing base Gemma predictions from $reusable_base"
    cp "$reusable_base" "$BASE_OUTPUT"
  else
    echo "[$(date -Is)] Running base Gemma eval"
    rm -f "$BASE_OUTPUT"
    python -u "$ROOT/eval_gemma_responses.py" \
      --model-path "$MODEL_PATH" \
      --examples "$EXAMPLES" \
      --output "$BASE_OUTPUT" \
      --max-new-tokens 180
  fi
fi

echo "[$(date -Is)] Scoring checkpoint-$CHECKPOINT_STEP eval"
python "$ROOT/score_ranking_value_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

echo "[$(date -Is)] Checkpoint-$CHECKPOINT_STEP summary:"
cat "$SUMMARY_OUTPUT"

echo "[$(date -Is)] Resuming long training run"
if pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; then
  echo "[$(date -Is)] Training process is already running"
else
  if tmux has-session -t "$TRAIN_SESSION" 2>/dev/null; then
    tmux send-keys -t "$TRAIN_SESSION" "cd '$ROOT' && bash '$TRAIN_RUNNER'" C-m
  else
    tmux new-session -d -s "$TRAIN_SESSION" "cd '$ROOT' && bash '$TRAIN_RUNNER'"
  fi

  for _ in $(seq 1 60); do
    if pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; then
      break
    fi
    sleep 2
  done

  if ! pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; then
    echo "[$(date -Is)] First resume attempt did not start training; recreating tmux session"
    tmux kill-session -t "$TRAIN_SESSION" 2>/dev/null || true
    tmux new-session -d -s "$TRAIN_SESSION" "cd '$ROOT' && bash '$TRAIN_RUNNER'"
  fi

  for _ in $(seq 1 60); do
    if pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; then
      break
    fi
    sleep 2
  done
fi

if ! pgrep -af "$TRAIN_SCRIPT" | grep -q "python"; then
  echo "[$(date -Is)] ERROR: training did not resume" >&2
  exit 1
fi

echo "[$(date -Is)] Interim eval complete; training resume command dispatched"

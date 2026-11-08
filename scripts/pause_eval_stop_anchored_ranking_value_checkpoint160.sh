#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="/home/wescheng/models/gemma-4-31b-it"
TRAIN_SESSION="fpl_gemma_anchored_ranking_value"
TRAIN_SCRIPT="$ROOT/train_gemma_sft.py"
EXAMPLES="$ROOT/reports/llm_anchored_ranking_value_2025_26_gw1_25_eval_gw26/eval.jsonl"
ADAPTER_ROOT="$ROOT/artifacts/gemma4_31b_lora_anchored_ranking_value_gw1_25_eval_gw26"
CHECKPOINT_STEP="${FPL_INTERIM_CHECKPOINT_STEP:-160}"
CHECKPOINT="$ADAPTER_ROOT/checkpoint-$CHECKPOINT_STEP"
LOG="$ROOT/logs/interim_eval_stop_anchored_ranking_value_checkpoint${CHECKPOINT_STEP}.log"

SFT_OUTPUT="$ROOT/reports/gemma4_anchored_ranking_value_gw1_25_eval_gw26_sft_checkpoint${CHECKPOINT_STEP}_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_anchored_ranking_value_gw1_25_eval_gw26_base_checkpoint${CHECKPOINT_STEP}_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint${CHECKPOINT_STEP}_summary.json"
DETAIL_OUTPUT="$ROOT/reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint${CHECKPOINT_STEP}_rows.json"
STOP_MARKER="$ROOT/reports/anchored_ranking_value_gw1_25_eval_gw26_checkpoint${CHECKPOINT_STEP}_eval_complete.stop"

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

echo "[$(date -Is)] Running anchored SFT eval with adapter $CHECKPOINT"
rm -f "$SFT_OUTPUT"
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$CHECKPOINT" \
  --max-new-tokens 260

if [[ -s "$BASE_OUTPUT" && "$(wc -l < "$BASE_OUTPUT" | tr -d ' ')" == "$example_count" ]]; then
  echo "[$(date -Is)] Reusing existing base Gemma predictions at $BASE_OUTPUT"
else
  reusable_base="$(find "$ROOT/reports" -maxdepth 1 -type f -name 'gemma4_anchored_ranking_value_gw1_25_eval_gw26_base*_predictions.jsonl' | sort | while read -r candidate; do
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
      --max-new-tokens 260
  fi
fi

echo "[$(date -Is)] Scoring checkpoint-$CHECKPOINT_STEP eval"
python "$ROOT/score_ranking_value_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

date -Is > "$STOP_MARKER"

echo "[$(date -Is)] Checkpoint-$CHECKPOINT_STEP eval complete; training intentionally left stopped"
python - <<PY
import json
from pathlib import Path
summary = json.loads(Path("$SUMMARY_OUTPUT").read_text())
print(json.dumps(summary, indent=2))
PY

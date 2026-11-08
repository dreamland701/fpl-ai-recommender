#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="/home/wescheng/models/gemma-4-31b-it"
EXAMPLES="$ROOT/reports/llm_ranking_value_2025_26_gw1_25_eval_gw26/eval.jsonl"
SFT_ADAPTER="$ROOT/artifacts/gemma4_31b_lora_ranking_value_gw1_25_eval_gw26"
SFT_OUTPUT="$ROOT/reports/gemma4_ranking_value_gw1_25_eval_gw26_sft_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_ranking_value_gw1_25_eval_gw26_base_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/ranking_value_gw1_25_eval_gw26_summary.json"
DETAIL_OUTPUT="$ROOT/reports/ranking_value_gw1_25_eval_gw26_rows.json"

source "$VENV"
cd "$ROOT"

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$SFT_ADAPTER" \
  --max-new-tokens 180

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$BASE_OUTPUT" \
  --max-new-tokens 180

python "$ROOT/score_ranking_value_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

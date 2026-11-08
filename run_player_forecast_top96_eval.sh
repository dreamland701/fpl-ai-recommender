#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="/home/wescheng/models/gemma-4-31b-it"
EXAMPLES="$ROOT/reports/llm_player_forecast_pilot_top96_2025_26_gw11_30/eval.jsonl"
SFT_ADAPTER="$ROOT/artifacts/gemma4_31b_lora_player_forecast_pilot_top96"
SFT_OUTPUT="$ROOT/reports/gemma4_player_forecast_top96_sft_eval_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_player_forecast_top96_base_eval_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/player_forecast_top96_eval_summary.json"
DETAIL_OUTPUT="$ROOT/reports/player_forecast_top96_eval_rows.json"

source "$VENV"
cd "$ROOT"

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$SFT_ADAPTER" \
  --max-new-tokens 128

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$BASE_OUTPUT" \
  --max-new-tokens 128

python "$ROOT/score_player_forecast_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

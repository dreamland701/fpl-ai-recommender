#!/usr/bin/env bash
set -euo pipefail

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="/home/wescheng/models/gemma-4-31b-it"
EXAMPLES="$ROOT/reports/llm_player_forecast_residual_2025_26_gw1_10_top128_eval_gw11/eval.jsonl"
SFT_ADAPTER="$ROOT/artifacts/gemma4_31b_lora_player_forecast_residual_gw1_10_top128_pilot"
SFT_OUTPUT="$ROOT/reports/gemma4_player_forecast_residual_gw1_10_top128_gw11_sft_pilot_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_player_forecast_residual_gw1_10_top128_gw11_base_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/player_forecast_residual_gw1_10_top128_gw11_pilot_eval_summary.json"
DETAIL_OUTPUT="$ROOT/reports/player_forecast_residual_gw1_10_top128_gw11_pilot_eval_rows.json"

source "$VENV"
cd "$ROOT"

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$SFT_ADAPTER" \
  --max-new-tokens 96

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$BASE_OUTPUT" \
  --max-new-tokens 96

python "$ROOT/score_player_forecast_residual_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

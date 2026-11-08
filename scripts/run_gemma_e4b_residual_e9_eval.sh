#!/usr/bin/env bash
set -euo pipefail

# E9-cleansplit eval: base E4B vs E9 SFT adapter on the full 2025-26 GW2-30
# eval set (7,424 rows — much larger than E7's GW12-30/4,864, since this
# split trains on zero same-season data and can test the whole season).

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="google/gemma-4-E4B-it"
EXAMPLES="$ROOT/reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30/eval.jsonl"
SFT_ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e9_cleansplit"
SFT_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_base_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/e4b_residual_e9_cleansplit_gw2_30_eval_summary.json"
DETAIL_OUTPUT="$ROOT/reports/e4b_residual_e9_cleansplit_gw2_30_eval_rows.json"

source "$VENV"
cd "$ROOT"

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$SFT_OUTPUT" \
  --adapter-path "$SFT_ADAPTER" \
  --max-new-tokens 96 \
  --no-4bit \
  --batch-size 16 \
  --resume

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" \
  --examples "$EXAMPLES" \
  --output "$BASE_OUTPUT" \
  --max-new-tokens 96 \
  --no-4bit \
  --batch-size 16 \
  --resume

python "$ROOT/score_player_forecast_residual_eval.py" \
  --examples "$EXAMPLES" \
  --base-predictions "$BASE_OUTPUT" \
  --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" \
  --examples-out "$DETAIL_OUTPUT"

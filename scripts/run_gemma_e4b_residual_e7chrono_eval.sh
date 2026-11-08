#!/usr/bin/env bash
set -euo pipefail

# E7-chrono eval: base E4B vs chrono adapter on the 2024-25 GW12-30 eval
# set (out-of-window validation of the E7 gate win).

ROOT="/home/wescheng/projects/fpl/fpl"
VENV="/home/wescheng/venvs/fpl-gemma-lite/bin/activate"
MODEL_PATH="google/gemma-4-E4B-it"
EXAMPLES="$ROOT/reports/llm_residual_v2_e7chrono2425_top256_scout_thru_2425gw11_eval_2425gw12_30/eval.jsonl"
SFT_ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e7chrono2425_top256_scout"
SFT_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e7chrono_2425gw12_30_sft_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e7chrono_2425gw12_30_base_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/e4b_residual_e7chrono_2425gw12_30_eval_summary.json"
DETAIL_OUTPUT="$ROOT/reports/e4b_residual_e7chrono_2425gw12_30_eval_rows.json"

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

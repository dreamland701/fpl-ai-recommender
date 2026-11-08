#!/usr/bin/env bash
set -uo pipefail

# Post-train chain for E10-prelaunch (the 2026-27 ship candidate). Not a
# discovery gate like E7/E8/E9 — the methodology was already validated by
# E9 (+82/+78 vs classic on a clean held-out season). This just confirms
# training converged normally on the small 4-week GW35-38 holdout before
# calling the adapter ready to ship.

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e10_prelaunch.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e10_prelaunch"
DATA_DIR="$ROOT/reports/llm_residual_v2_e10_prelaunch_top256_thru_2526_34_eval_2526_35_38"
CHAINLOG="$ROOT/logs/e10_post_train_chain.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs/decision_sweep

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "chain armed; waiting for E10 final adapter"

while ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  size1=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  sleep 1800
  size2=$(stat -c %s "$TRAINLOG" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
    log "WARNING: trainer log static for 30 min and no train_runtime — trainer dead or hung?"
  fi
done
log "E10 training complete — launching eval"

MODEL_PATH="google/gemma-4-E4B-it"
EXAMPLES="$DATA_DIR/eval.jsonl"
SFT_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e10_prelaunch_gw35_38_sft_predictions.jsonl"
BASE_OUTPUT="$ROOT/reports/gemma4_e4b_residual_e10_prelaunch_gw35_38_base_predictions.jsonl"
SUMMARY_OUTPUT="$ROOT/reports/e4b_residual_e10_prelaunch_gw35_38_eval_summary.json"
DETAIL_OUTPUT="$ROOT/reports/e4b_residual_e10_prelaunch_gw35_38_eval_rows.json"

(
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" --examples "$EXAMPLES" --output "$SFT_OUTPUT" \
  --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
&& python -u "$ROOT/eval_gemma_responses.py" \
  --model-path "$MODEL_PATH" --examples "$EXAMPLES" --output "$BASE_OUTPUT" \
  --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
&& python "$ROOT/score_player_forecast_residual_eval.py" \
  --examples "$EXAMPLES" --base-predictions "$BASE_OUTPUT" --sft-predictions "$SFT_OUTPUT" \
  --output "$SUMMARY_OUTPUT" --examples-out "$DETAIL_OUTPUT"
) > logs/e10_eval_nohup.log 2>&1 &
sleep 120
if [ ! -s "$ROOT/logs/e10_eval_nohup.log" ]; then
  log "E10 EVAL LAUNCH FAILED — no output after 120s (see logs/e10_eval_nohup.log)"
  exit 1
fi
log "eval running; waiting for summary"

until [ -s "$SUMMARY_OUTPUT" ]; do
  size1=$(stat -c %s "$ROOT/logs/e10_eval_nohup.log" 2>/dev/null || echo 0)
  sleep 900
  size2=$(stat -c %s "$ROOT/logs/e10_eval_nohup.log" 2>/dev/null || echo 0)
  if [ "$size1" = "$size2" ] && [ ! -s "$SUMMARY_OUTPUT" ]; then
    log "EVAL STALLED OR DIED — log static 15 min without summary; aborting chain"
    exit 1
  fi
done
log "eval summary present: $(python3 -c "
import json
d = json.load(open('$SUMMARY_OUTPUT'))
c, s = d['classic_ml'], d['sft_gemma_delta']
print(f\"classic 5gw MAE {c['final_points_5gw_mae']:.3f} vs SFT {s['final_points_5gw_mae']:.3f}; strict_json {s['strict_json_predictions']}/{s['total_examples']}\")
" 2>/dev/null)"

echo 900 > /proc/self/oom_score_adj 2>/dev/null || true

# Small sanity-check backtest on the GW35-38 holdout — not a ship/no-ship
# gate (that judgment already happened via E9), just confirms nothing
# broke in the composed pipeline before deployment.
PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 34 --start-week 35 --end-week 38 \
  --output-dir reports/backtest_gw35_38_llm_e10_all_baselineopt \
  --llm-examples "$EXAMPLES" --llm-predictions "$SFT_OUTPUT" --llm-fields all --decision-variant baseline \
  --skip-league-average-fetch > logs/decision_sweep/e10_sanity_gate.log 2>&1 \
  && log "sanity backtest done: $(python3 -c "import json; d=json.load(open('reports/backtest_gw35_38_llm_e10_all_baselineopt/rolling_squad_backtest.json')); print(d['total_actual_points'])" 2>/dev/null) actual pts over GW35-38 (LLM-adjusted)" \
  || log "SANITY BACKTEST FAILED (non-blocking, informational only)"

PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows.csv \
  --test-season 2025-26 --initial-train-week-max 34 --start-week 35 --end-week 38 \
  --output-dir reports/backtest_gw35_38_classic_only \
  --skip-league-average-fetch > logs/decision_sweep/e10_sanity_gate_classic.log 2>&1 \
  && log "sanity backtest done: $(python3 -c "import json; d=json.load(open('reports/backtest_gw35_38_classic_only/rolling_squad_backtest.json')); print(d['total_actual_points'])" 2>/dev/null) actual pts over GW35-38 (classic-only anchor)" \
  || log "SANITY BACKTEST FAILED (classic-only, non-blocking)"

log "CHAIN COMPLETE — E10-prelaunch ready for review. This is the ship candidate for 2026-27 GW1; the GW35-38 numbers above are a sanity check only (n=4 weeks), not a ship decision — that was already made via E9."

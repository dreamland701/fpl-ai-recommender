#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E17 post-training verdict chain. Arms now, fires when training finishes.
#
# COMPARATOR IS E11-DEFCON, NOT E11-FULL. E11-full is the deployed champion
# but it was trained THROUGH 2025-26:38, so it has already seen the GW35-38
# holdout; scoring it there would flatter it. E11-defcon used the identical
# split to E17 (train through 2025-26:34, eval 35-38), so it is the honest
# apples-to-apples comparison. If E17 wins, the deployment step is to
# consolidate it through GW38, exactly as E10 followed E9.
#
# TWO metrics, and they are NOT equally weighted:
#   * 1GW/5GW MAE on the holdout - DIAGNOSTIC ONLY. This project has a long
#     record of MAE improving while decisions get worse (E15 was the latest:
#     best MAE, worse decisions).
#   * Rolling squad decision value - THE SHIPPING METRIC. Adapters are 0-for-5
#     on it. Note the holdout is only 4 GWs, which is too short to read
#     confidently; treat a narrow decision result as inconclusive rather than
#     as a win, and lean on F6's already-measured 5-window anchor evidence
#     (+112) plus the MAE result.
# =============================================================================

ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
CHAINLOG="$ROOT/logs/e17_post_train_chain.log"
log(){ echo "$(date '+%F %T') $*" | tee -a "$CHAINLOG"; }

TRAINLOG="$ROOT/logs/train_e4b_residual_e17_context.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e17_context"
E17_DIR="$ROOT/reports/llm_residual_v2_e17_context_top256_thru_2526_34_eval_2526_35_38"
E11_DIR="$ROOT/reports/llm_residual_v2_e11_defcon_top256_thru_2526_34_eval_2526_35_38"
E11_ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e11_defcon"
E17_PRED="$ROOT/reports/gemma4_e4b_residual_e17_context_gw35_38_sft_predictions.jsonl"
E17_BASE="$ROOT/reports/gemma4_e4b_residual_e17_context_gw35_38_base_predictions.jsonl"
E11_PRED="$ROOT/reports/gemma4_e4b_residual_e11_defcon_gw35_38_sft_predictions.jsonl"
SUMMARY="$ROOT/reports/e4b_residual_e17_context_gw35_38_eval_summary.json"
TABLE_F6="$ROOT/data/fpl_training_rows_blend_f6.csv"
TABLE_OLD="$ROOT/data/fpl_training_rows_blend.csv"

log "chain armed; waiting for E17 adapter"
while ! grep -aq "train_runtime" "$TRAINLOG" 2>/dev/null || [ ! -s "$ADAPTER/adapter_model.safetensors" ]; do
  if ! ps -eo args | grep -q "[t]rain_gemma_sft.py"; then
    if [ ! -s "$ADAPTER/adapter_model.safetensors" ]; then
      log "ABORT: trainer gone and no final adapter — inspect $TRAINLOG"; exit 1
    fi
  fi
  sleep 900
done
log "training complete — decoding E17 on its own holdout"

# Single-instance decode guard (duplicate decoders cost us 336 dupe rows at GW5).
if pgrep -f "^python.*eval_gemma_responses" >/dev/null 2>&1; then
  log "ABORT: an eval_gemma_responses decode is already running"; exit 1
fi

python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$E17_DIR/eval.jsonl" --output "$E17_PRED" \
  --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
  >> logs/e17_eval_nohup.log 2>&1 || { log "E17 decode FAILED"; exit 1; }
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$E17_DIR/eval.jsonl" --output "$E17_BASE" \
  --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
  >> logs/e17_eval_nohup.log 2>&1 || { log "base decode FAILED"; exit 1; }
python "$ROOT/score_player_forecast_residual_eval.py" \
  --examples "$E17_DIR/eval.jsonl" --base-predictions "$E17_BASE" --sft-predictions "$E17_PRED" \
  --output "$SUMMARY" --examples-out "$ROOT/reports/e4b_residual_e17_context_gw35_38_eval_rows.json" \
  >> logs/e17_eval_nohup.log 2>&1 || { log "scoring FAILED"; exit 1; }

log "MAE (diagnostic): $(python3 -c "
import json
d=json.load(open('$SUMMARY')); c,s=d['classic_ml'],d['sft_gemma_delta']
print(f\"classic 1gw {c['final_points_1gw_mae']:.4f} vs E17 {s['final_points_1gw_mae']:.4f} | 5gw {c['final_points_5gw_mae']:.4f} vs {s['final_points_5gw_mae']:.4f} | strict_json {s['strict_json_predictions']}/{s['total_examples']}\")" 2>/dev/null)"

log "=== decision value (THE metric): E17 vs E11-defcon, 2025-26 GW35-38 ==="
PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
  --training-data "$TABLE_F6" --test-season 2025-26 --initial-train-week-max 34 \
  --start-week 35 --end-week 38 --output-dir "$ROOT/reports/backtest_decision_e17" \
  --llm-examples "$E17_DIR/eval.jsonl" --llm-predictions "$E17_PRED" \
  --skip-league-average-fetch >> "$CHAINLOG" 2>&1
PYTHONPATH=src FPL_PRIOR_BLEND=1 python3 -m fpl_ai.cli backtest-squad \
  --training-data "$TABLE_OLD" --test-season 2025-26 --initial-train-week-max 34 \
  --start-week 35 --end-week 38 --output-dir "$ROOT/reports/backtest_decision_e11defcon" \
  --llm-examples "$E11_DIR/eval.jsonl" --llm-predictions "$E11_PRED" \
  --skip-league-average-fetch >> "$CHAINLOG" 2>&1
# classic-only control on the same window
PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
  --training-data "$TABLE_F6" --test-season 2025-26 --initial-train-week-max 34 \
  --start-week 35 --end-week 38 --output-dir "$ROOT/reports/backtest_decision_classicF6" \
  --skip-league-average-fetch >> "$CHAINLOG" 2>&1

log "$(python3 -c "
import json
def pts(p):
    try: return json.load(open(p+'/rolling_squad_backtest.json'))['total_actual_points']
    except Exception as e: return None
a=pts('$ROOT/reports/backtest_decision_e17'); b=pts('$ROOT/reports/backtest_decision_e11defcon'); c=pts('$ROOT/reports/backtest_decision_classicF6')
print(f'DECISION VALUE GW35-38 -> E17 {a} | E11-defcon {b} | classic+F6 {c}')
if a is not None and b is not None:
    print(f'  E17 vs E11-defcon: {a-b:+.0f} over 4 GWs. NOTE 4 weeks is too short to be conclusive on its own.')
")"
log "E17 VERDICT CHAIN DONE — review before any ship decision"

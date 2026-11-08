#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E18: F6 anchor + the ORIGINAL (v1) prompts. The isolation test E17 demanded.
#
# E17's verdict was split. Its system won decision value (300 vs 260) but:
#   * its MAE was WORSE than E11-defcon's (2.0935 vs 2.0596), and
#   * the new prompt blocks were provably UNUSED — partial correlation of the
#     delta with opponent goals-conceded -0.0506 and with injured team-mates
#     -0.0328, both ~0 once the baseline-proportional shrink is controlled for.
#
# So the +40 was not the designed mechanism. Decomposed: F6 anchor +23,
# adapter +30 vs E11's +13. E18 isolates the prompt half by holding the F6
# anchor fixed and reverting to v1 prompts.
#
# Leading hypothesis it tests: F6 already absorbed the fixture signal into the
# anchor, leaving nothing in the residual for the adapter to learn, which would
# make the v17 blocks pure cost (prompts 32% longer, 0.8% truncated).
#   * E18 >= E17  -> hypothesis holds; ship F6 + v1, drop the blocks.
#   * E18 <  E17  -> the blocks do carry signal despite the null mechanism;
#                    investigate before discarding them.
# Either way E18 yields a deployable adapter in train/live parity with the F6
# anchor, which is what GW6 (2026-10-10) needs.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/e18_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }

DATA_DIR="$ROOT/reports/llm_residual_v2_e18_f6v1_top256_thru_2526_34_eval_2526_35_38"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e18_f6v1"
[ -s "$DATA_DIR/train.jsonl" ] || { log "GATE FAILED: no split"; exit 1; }

export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=1536
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS=-1
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=5e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=1
export FPL_GEMMA_EVAL_BATCH_SIZE=2
export FPL_GEMMA_GRAD_ACCUM=16
export FPL_GEMMA_LOGGING_STEPS=10
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=100
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=30
export FPL_GEMMA_GRADIENT_CHECKPOINTING=true
export FPL_GEMMA_LORA_DROPOUT=0.0
echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
log "E18 training -> $OUTPUT_DIR (v1 prompts are ~32% shorter than E17's; expect ~60h)"
python train_gemma_sft.py 2>&1 | tee "logs/train_e4b_residual_e18_f6v1.log"
log "E18 training exited rc=$?"

log "=== E18 eval: decode holdout ==="
if pgrep -f "^python.*eval_gemma_responses" >/dev/null 2>&1; then log "ABORT: a decode is already running"; exit 1; fi
PRED="$ROOT/reports/gemma4_e4b_residual_e18_f6v1_gw35_38_sft_predictions.jsonl"
BASE="$ROOT/reports/gemma4_e4b_residual_e18_f6v1_gw35_38_base_predictions.jsonl"
SUMMARY="$ROOT/reports/e4b_residual_e18_f6v1_gw35_38_eval_summary.json"
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" \
  --output "$PRED" --adapter-path "$OUTPUT_DIR" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e18_eval.log 2>&1 || { log "decode FAILED"; exit 1; }
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" \
  --output "$BASE" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e18_eval.log 2>&1 || { log "base decode FAILED"; exit 1; }
python score_player_forecast_residual_eval.py --examples "$DATA_DIR/eval.jsonl" \
  --base-predictions "$BASE" --sft-predictions "$PRED" --output "$SUMMARY" \
  --examples-out "$ROOT/reports/e4b_residual_e18_f6v1_gw35_38_eval_rows.json" >> logs/e18_eval.log 2>&1 || { log "scoring FAILED"; exit 1; }
log "MAE: $(python3 -c "
import json; d=json.load(open('$SUMMARY')); c,s=d['classic_ml'],d['sft_gemma_delta']
print(f\"classic {c['final_points_1gw_mae']:.4f} vs E18 {s['final_points_1gw_mae']:.4f} (E17 was 2.0935, E11 2.0596)\")" 2>/dev/null)"

log "=== E18 decision value ==="
PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
  --training-data data/fpl_training_rows_blend_f6.csv --test-season 2025-26 --initial-train-week-max 34 \
  --start-week 35 --end-week 38 --output-dir reports/backtest_decision_e18 \
  --llm-examples "$DATA_DIR/eval.jsonl" --llm-predictions "$PRED" --skip-league-average-fetch >> "$LOG" 2>&1
log "$(python3 -c "
import json
def p(x):
    try: return json.load(open(x+'/rolling_squad_backtest.json'))['total_actual_points']
    except Exception: return None
print(f'DECISION GW35-38 -> E18 {p(\"reports/backtest_decision_e18\")} | E17 {p(\"reports/backtest_decision_e17\")} | classic+F6 {p(\"reports/backtest_decision_classicF6\")} | E11 {p(\"reports/backtest_decision_e11defcon\")}')")"

log "=== E18 MECHANISM CHECK (standing gate since E17) ==="
python3 scripts/check_delta_mechanism.py --examples "$DATA_DIR/eval.jsonl" --predictions "$PRED" --label E18 >> "$LOG" 2>&1 || log "(mechanism check unavailable)"
log "E18 CHAIN DONE"

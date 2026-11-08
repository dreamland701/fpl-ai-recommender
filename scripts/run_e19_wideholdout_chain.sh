#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E19: the READABLE HOLDOUT. Same config as E18 (F6 anchor + v1 prompts), but
# trained through 2025-26:26 so the holdout is GW27-38 — 12 gameweeks, i.e.
# THREE independent 4-week decision windows instead of one.
#
# Why spend a whole run on measurement: every adapter verdict so far has
# rested on a single 4-week window, which is too short to separate signal
# from noise. E17 is the cautionary case — it "won" 300 vs 260 on four weeks
# with no working mechanism. The project's own rule is >=3 windows; until now
# only the ANCHOR could satisfy it, because anchor backtests are CPU-cheap
# while adapters need a decode. This run makes adapter verdicts readable.
#
# Cost: 35,840 train rows vs 37,888 (−5%). Cheap for tripling the holdout.
#
# Waits for the E18 chain to finish completely (training AND its decode) so
# the two never contend for the GPU.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/e19_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }

DATA_DIR="$ROOT/reports/llm_residual_v2_e19_wideholdout_top256_thru_2526_26_eval_2526_27_38"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e19_wideholdout"
[ -s "$DATA_DIR/train.jsonl" ] || { log "GATE FAILED: no split"; exit 1; }

log "armed; waiting for the E18 chain to finish (training + decode)"
while ! grep -aq "E18 CHAIN DONE" logs/e18_chain.log 2>/dev/null; do
  if grep -aqE "FAILED|ABORT" logs/e18_chain.log 2>/dev/null; then
    log "E18 chain reported a failure — not starting E19. Inspect logs/e18_chain.log"; exit 1
  fi
  sleep 900
done
log "E18 done — starting E19"

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
log "training -> $OUTPUT_DIR (~56h)"
python train_gemma_sft.py 2>&1 | tee "logs/train_e4b_residual_e19_wideholdout.log"
log "training exited rc=$?"

PRED="$ROOT/reports/gemma4_e4b_residual_e19_gw27_38_sft_predictions.jsonl"
BASE="$ROOT/reports/gemma4_e4b_residual_e19_gw27_38_base_predictions.jsonl"
SUMMARY="$ROOT/reports/e4b_residual_e19_gw27_38_eval_summary.json"
log "decoding the 3,072-row holdout (3x the usual, allow extra time)"
if pgrep -f "^python.*eval_gemma_responses" >/dev/null 2>&1; then log "ABORT: decode already running"; exit 1; fi
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" \
  --output "$PRED" --adapter-path "$OUTPUT_DIR" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e19_eval.log 2>&1 || { log "decode FAILED"; exit 1; }
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$DATA_DIR/eval.jsonl" \
  --output "$BASE" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e19_eval.log 2>&1 || { log "base decode FAILED"; exit 1; }
python score_player_forecast_residual_eval.py --examples "$DATA_DIR/eval.jsonl" \
  --base-predictions "$BASE" --sft-predictions "$PRED" --output "$SUMMARY" \
  --examples-out "$ROOT/reports/e4b_residual_e19_gw27_38_eval_rows.json" >> logs/e19_eval.log 2>&1 || { log "scoring FAILED"; exit 1; }
log "MAE (diagnostic): $(python3 -c "
import json; d=json.load(open('$SUMMARY')); c,s=d['classic_ml'],d['sft_gemma_delta']
print(f\"classic {c['final_points_1gw_mae']:.4f} vs E19 {s['final_points_1gw_mae']:.4f}; strict_json {s['strict_json_predictions']}/{s['total_examples']}\")" 2>/dev/null)"

log "=== THREE-WINDOW decision value (the point of this run) ==="
for W in "27 30" "31 34" "35 38"; do
  set -- $W
  PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_blend_f6.csv --test-season 2025-26 --initial-train-week-max 26 \
    --start-week $1 --end-week $2 --output-dir "reports/backtest_e19_$1_$2" \
    --llm-examples "$DATA_DIR/eval.jsonl" --llm-predictions "$PRED" --skip-league-average-fetch >> "$LOG" 2>&1
  PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_blend_f6.csv --test-season 2025-26 --initial-train-week-max 26 \
    --start-week $1 --end-week $2 --output-dir "reports/backtest_classic_$1_$2" \
    --skip-league-average-fetch >> "$LOG" 2>&1
done
log "$(python3 -c "
import json
def p(x):
    try: return json.load(open(x+'/rolling_squad_backtest.json'))['total_actual_points']
    except Exception: return None
rows=[]
for a,b in [('27','30'),('31','34'),('35','38')]:
    e=p(f'reports/backtest_e19_{a}_{b}'); c=p(f'reports/backtest_classic_{a}_{b}')
    rows.append((f'GW{a}-{b}',e,c))
print('THREE-WINDOW DECISION VALUE (E19 adapter vs classic+F6):')
we=0
for n,e,c in rows:
    if e is None or c is None: print(f'  {n}: missing'); continue
    we += 1 if e>c else 0
    print(f'  {n}: E19 {e}  classic {c}  {e-c:+.0f}')
tot_e=sum(e for _,e,c in rows if e); tot_c=sum(c for _,e,c in rows if c)
print(f'  TOTAL: E19 {tot_e}  classic {tot_c}  {tot_e-tot_c:+.0f}   windows won {we}/3')")"

log "=== mechanism check ==="
python3 scripts/check_delta_mechanism.py --examples "$DATA_DIR/eval.jsonl" --predictions "$PRED" --label E19 >> "$LOG" 2>&1 || log "(mechanism check unavailable)"
log "E19 CHAIN DONE"

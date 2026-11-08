#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E20 GPU chain (approved by Wes 2026-10-04): train the E19 recipe on the
# data-contract-fixed corpus, read it on the same 12-week holdout, then build
# the GW6 final packet after Friday's press conferences.
#
#   1. wait for scripts/run_e20_contract_pipeline.sh to pass its gate and for
#      any live decode to finish (one GPU job at a time)
#   2. train E20 (E19 hyperparameters, ~55h)
#   3. decode the 3,072-row holdout with and without the adapter, score it,
#      availability AUC among likely starters (the promotion-rule metric)
#   4. decision value on the FIXED pipeline: E20 vs classic+F6 (N_F), GW27-38
#   5. at 2026-10-09 17:00 UTC: fresh entry/snapshot/evidence, fixed-pipeline
#      decision sheet, E11-full shadow decode (+ E20 if it trained), summary
#
# A failure in E20 skips the E20 steps; the GW6 refresh still runs.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/e20_chain.log"; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1

SPLIT="$ROOT/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e20_contract"
PRED="$ROOT/reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl"
BASEPRED="$ROOT/reports/gemma4_e4b_residual_e20_gw27_38_base_predictions.jsonl"
SUMMARY="$ROOT/reports/e4b_residual_e20_gw27_38_eval_summary.json"
BT="$ROOT/reports/review_fixes_2026_10/bt_e20"
PACKET="$ROOT/reports/gw6_packet_2026_10"
FINAL="$PACKET/final"
E20_OK=0

wait_for_gpu(){ while pgrep -f "^python.*(eval_gemma_responses|train_gemma)" >/dev/null 2>&1; do sleep 120; done; }

log "armed; waiting for the E20 corpus gate"
until grep -aq "GATE PASSED" logs/e20_pipeline.log 2>/dev/null; do
  if grep -aq "GATE FAILED" logs/e20_pipeline.log 2>/dev/null; then log "corpus gate FAILED — skipping E20"; break; fi
  sleep 120
done

if grep -aq "GATE PASSED" logs/e20_pipeline.log 2>/dev/null; then
  wait_for_gpu
  log "=== E20 training -> $ADAPTER (~55h) ==="
  export PYTORCH_ALLOC_CONF=expandable_segments:True
  export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
  export FPL_GEMMA_LOAD_IN_4BIT=false
  export FPL_GEMMA_DATA_DIR="$SPLIT"
  export FPL_GEMMA_OUTPUT_DIR="$ADAPTER"
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
  python train_gemma_sft.py 2>&1 | tee "logs/train_e4b_residual_e20_contract.log"
  rc=${PIPESTATUS[0]}
  log "E20 training exited rc=$rc"
  if [ "$rc" -eq 0 ] && [ -s "$ADAPTER/adapter_model.safetensors" ]; then E20_OK=1; else log "E20 TRAINING FAILED"; fi
fi

if [ "$E20_OK" -eq 1 ]; then
  log "=== E20 holdout decode (adapter, then base) ==="
  wait_for_gpu
  python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$SPLIT/eval.jsonl" \
    --output "$PRED" --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e20_eval.log 2>&1 \
    || { log "E20 decode FAILED"; E20_OK=0; }
fi
if [ "$E20_OK" -eq 1 ]; then
  python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it --examples "$SPLIT/eval.jsonl" \
    --output "$BASEPRED" --max-new-tokens 96 --no-4bit --batch-size 16 --resume >> logs/e20_eval.log 2>&1 \
    || log "base decode FAILED (scoring skipped)"
  if [ -s "$BASEPRED" ]; then
    python score_player_forecast_residual_eval.py --examples "$SPLIT/eval.jsonl" \
      --base-predictions "$BASEPRED" --sft-predictions "$PRED" --output "$SUMMARY" \
      --examples-out "$ROOT/reports/e4b_residual_e20_gw27_38_eval_rows.json" >> logs/e20_eval.log 2>&1 || log "scoring FAILED"
    log "MAE: $(python3 -c "
import json; d=json.load(open('$SUMMARY')); c,s=d['classic_ml'],d['sft_gemma_delta']
print(f\"classic {c['final_points_1gw_mae']:.4f} vs E20 {s['final_points_1gw_mae']:.4f}; strict_json {s['strict_json_predictions']}/{s['total_examples']}\")" 2>/dev/null)"
  fi
  log "availability AUC among likely starters (promotion-rule metric): $(PYTHONPATH=src python3 - <<PYEOF 2>/dev/null
import json
from fpl_ai.llm_adjust import load_llm_delta_lookup
rows = [json.loads(l) for l in open("$SPLIT/eval.jsonl") if l.strip()]
lookup = load_llm_delta_lookup("$SPLIT/eval.jsonl", "$PRED")
def auc(scores, labels):
    pairs = sorted(zip(scores, labels)); pos = sum(labels); neg = len(labels) - pos
    rank_sum, i = 0.0, 0
    while i < len(pairs):
        j = i
        while j < len(pairs) and pairs[j][0] == pairs[i][0]: j += 1
        rank_sum += sum(1 for k in range(i, j) if pairs[k][1]) * (i + j + 1) / 2.0
        i = j
    return (rank_sum - pos * (pos + 1) / 2.0) / (pos * neg) if pos and neg else float("nan")
cs, ads, ys = [], [], []
for r in rows:
    m = r["metadata"]; b = m["baseline_forecast"]; p = float(b["baseline_appearance_probability"])
    if p < 0.5: continue
    d = lookup.get((str(r.get("season") or m["season"]), int(r["week"]), int(m["player_id"])), {})
    label = float((m.get("labels") or {}).get("minutes_1gw", 0.0)) > 0
    cs.append(p); ads.append(min(1.0, max(0.0, p + d.get("delta_appearance_probability", 0.0)))); ys.append(label)
print(f"classic {auc(cs, ys):.3f} vs E20 {auc(ads, ys):.3f} (n={len(ys)})")
PYEOF
)"
  log "=== decision value on the fixed pipeline: E20 vs classic+F6 (N_F) ==="
  mkdir -p "$BT"
  for W in "27 30" "31 34" "35 38"; do
    set -- $W
    PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
      --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season 2025-26 --initial-train-week-max $(( $1 - 1 )) \
      --start-week $1 --end-week $2 --output-dir "$BT/E20_2025-26_$1_$2" \
      --llm-examples "$SPLIT/eval.jsonl" --llm-predictions "$PRED" --skip-league-average-fetch > "$BT/E20_2025-26_$1_$2.log" 2>&1
  done
  log "$(python3 -c "
import json
def p(x):
    try: return json.load(open(x + '/rolling_squad_backtest.json'))['total_actual_points']
    except Exception: return None
tot_e = tot_c = won = 0
print('THREE-WINDOW DECISION VALUE on the fixed pipeline (E20 vs classic+F6):')
for a, b in (('27', '30'), ('31', '34'), ('35', '38')):
    e = p(f'$BT/E20_2025-26_{a}_{b}'); c = p(f'$ROOT/reports/review_fixes_2026_10/bt/N_F_2025-26_{a}_{b}')
    if e is None or c is None: print(f'  GW{a}-{b}: missing'); continue
    tot_e += e; tot_c += c; won += e > c
    print(f'  GW{a}-{b}: E20 {e:.0f}  classic+F6 {c:.0f}  {e - c:+.0f}')
print(f'  TOTAL: E20 {tot_e:.0f}  classic+F6 {tot_c:.0f}  {tot_e - tot_c:+.0f}  windows won {won}/3 (adapter noise sd ~24/window)')
")"
  python3 scripts/check_delta_mechanism.py --examples "$SPLIT/eval.jsonl" --predictions "$PRED" --label E20 >> "$LOG" 2>&1 \
    || log "(mechanism check unavailable)"
  log "E20 EVAL DONE"
fi

# ----------------------------------------------------------------------------- GW6 final packet
TARGET=$(date -d '2026-10-09T17:00:00Z' +%s)
NOW=$(date +%s)
if [ "$NOW" -lt "$TARGET" ]; then
  log "waiting until 2026-10-09 17:00 UTC for the GW6 final refresh (after Friday press conferences)"
  sleep $(( TARGET - NOW ))
fi
DEADLINE=$(date -d '2026-10-10T10:00:00Z' +%s)
if [ "$(date +%s)" -ge "$DEADLINE" ]; then log "past the GW6 deadline — skipping the final refresh"; log "E20 CHAIN DONE"; exit 0; fi

log "=== GW6 final refresh -> $FINAL ==="
mkdir -p "$FINAL"
export PACKET_DIR="$FINAL"
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
PYTHONPATH=src python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$FINAL/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 \
  || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$FINAL/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/route_lineups.py" > "$FINAL/route_lineups.log" 2>&1 || log "route lineups FAILED"

log "collecting GW6 evidence through today"
TODAY=$(date -u +%F)
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-09-19 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_gw6final.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-09-19 --output reports/evidence_pl_scout_2627_gw6final.jsonl >> "$LOG" 2>&1 \
  || log "scout collection FAILED"

live_examples(){ # tag table
  local tag=$1 table=$2
  FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python3 scripts/build_live_gw_examples.py --stage corpus \
    --deadline-ts 2026-10-10T10:00:00Z --training-data "$table" --output "reports/live_gw6final_2627_${tag}_corpus_bare.jsonl" >> "$LOG" 2>&1 || return 1
  PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py --corpus "reports/live_gw6final_2627_${tag}_corpus_bare.jsonl" \
    --evidence reports/evidence_guardian_football_2627_gw6final.jsonl --evidence reports/evidence_guardian_football_2627_gw5.jsonl \
    --evidence reports/evidence_pl_scout_2627_gw6final.jsonl --evidence reports/evidence_pl_scout_2627_gw5.jsonl \
    --include-non-curated --lookback-days 14 --output "reports/live_gw6final_2627_${tag}_corpus_evidence.jsonl" >> "$LOG" 2>&1 || return 1
  PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py --corpus "reports/live_gw6final_2627_${tag}_corpus_evidence.jsonl" \
    --history-dir data/fpl_history --output "reports/live_gw6final_2627_${tag}_corpus_full.jsonl" >> "$LOG" 2>&1 || return 1
  FPL_LIVE_INCLUDE_MARKET=0 PYTHONPATH=src python3 scripts/build_live_gw_examples.py --stage prompts \
    --corpus "reports/live_gw6final_2627_${tag}_corpus_full.jsonl" --output "reports/live_gw6final_2627_${tag}_examples.jsonl" >> "$LOG" 2>&1
}

wait_for_gpu
if live_examples classic data/fpl_training_rows_v3_contract.csv; then
  bash scripts/decode_live.sh reports/live_gw6final_2627_classic_examples.jsonl reports/live_gw6final_2627_e11full_predictions.jsonl \
    artifacts/gemma4_e4b_lora_residual_v2_e11_full >> logs/live_gw6final_decode.log 2>&1 || log "E11-full decode FAILED"
  python3 "$PACKET/shadow_sheet.py" reports/live_gw6final_2627_classic_examples.jsonl reports/live_gw6final_2627_e11full_predictions.jsonl e11full \
    > "$FINAL/shadow_e11full.log" 2>&1 || log "E11-full shadow sheet FAILED"
else
  log "E11-full live examples FAILED"
fi
if [ "$E20_OK" -eq 1 ]; then
  if live_examples f6 data/fpl_training_rows_v3_contract_f6.csv; then
    bash scripts/decode_live.sh reports/live_gw6final_2627_f6_examples.jsonl reports/live_gw6final_2627_e20_predictions.jsonl \
      "$ADAPTER" >> logs/live_gw6final_decode.log 2>&1 || log "E20 decode FAILED"
    python3 "$PACKET/shadow_sheet.py" reports/live_gw6final_2627_f6_examples.jsonl reports/live_gw6final_2627_e20_predictions.jsonl e20 \
      > "$FINAL/shadow_e20.log" 2>&1 || log "E20 shadow sheet FAILED"
  fi
fi
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary FAILED"
log "GW6 final packet ready: $FINAL/README.md"
log "E20 CHAIN DONE"

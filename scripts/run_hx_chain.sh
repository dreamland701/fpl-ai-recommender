#!/usr/bin/env bash
# Generic regression-head chain (2026-10-15). Env: TAG (e.g. h2), SPLIT, LSPLIT, LIVE_END (last live week), BATCH, CKPT,
# optional FIELDS (all|availability), MAX_ROWS, DATA_LABEL. Classic reference backtests are reused when present.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
: "${TAG:?}" "${SPLIT:?}" "${LSPLIT:?}" "${LIVE_END:?}"; BATCH=${BATCH:-1}; CKPT=${CKPT:-1}; FIELDS=${FIELDS:-all}; MAX_ROWS=${MAX_ROWS:-0}
LOG=logs/${TAG}_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "${TAG^^} FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv; ADAPTER=artifacts/gemma4_e4b_${TAG}_reghead; OUT=reports/h_series
ACCUM=$((16 / BATCH))
bt(){ local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }
log "=== ${TAG^^}: head on $SPLIT (fields $FIELDS, batch $BATCH ckpt $CKPT, max rows $MAX_ROWS) ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38" "2026-27 2 $LIVE_END"; do set -- $W; bt "$OUT/bt_classic/$1_$2_$3" $1 $2 $3 & done
FPL_RH_DATA_DIR=$SPLIT FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=$BATCH FPL_RH_ACCUM=$ACCUM FPL_RH_CKPT=$CKPT \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=200 FPL_RH_COMPACT=1 FPL_RH_FIELDS=$FIELDS FPL_RH_MAX_ROWS=$MAX_ROWS \
  python3 -u train_gemma_reghead.py >> logs/train_${TAG}.log 2>&1
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training"
python3 -u scripts/reghead_predict.py "$SPLIT/eval.jsonl" "$ADAPTER" "$OUT/${TAG}_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "holdout predict"
python3 -u scripts/reghead_predict.py "$LSPLIT/eval.jsonl" "$ADAPTER" "$OUT/${TAG}_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "live predict"
python3 scripts/track_sft_accuracy.py --set "${TAG^^} holdout 2025-26 GW27-38 (${DATA_LABEL:-$SPLIT})" "$SPLIT/eval.jsonl" "$OUT/${TAG}_holdout_pred.jsonl" "$OUT/${TAG}_holdout_pred.jsonl" \
  --set "${TAG^^} live 2026-27 GW2-$LIVE_END" "$LSPLIT/eval.jsonl" "$OUT/${TAG}_live_pred.jsonl" "$OUT/${TAG}_live_pred.jsonl" --out-md "$OUT/${TAG}_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 scripts/avail_auc_from_preds.py "$OUT/${TAG}_holdout_pred.jsonl" "$OUT/${TAG}_live_pred.jsonl" | tee -a "$LOG"
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_${TAG}/$1_$2_$3" $1 $2 $3 "$SPLIT/eval.jsonl" "$OUT/${TAG}_holdout_pred.jsonl" & done
bt "$OUT/bt_${TAG}/2026-27_2_$LIVE_END" 2026-27 2 $LIVE_END "$LSPLIT/eval.jsonl" "$OUT/${TAG}_live_pred.jsonl" &
wait
log "RESULT: $(TAG=$TAG LIVE_END=$LIVE_END python3 - <<'PY'
import json, os
tag, le = os.environ["TAG"], os.environ["LIVE_END"]
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(t):
    w = [tot(f"reports/h_series/{t}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{t}/2026-27_2_{le}/rolling_squad_backtest.json")
c, h = s("bt_classic"), s(f"bt_{tag}")
print(f"{tag.upper()} squad points: holdout {h[0]} = {h[1]} vs classic {c[0]} = {c[1]} ({h[1] - c[1]:+.0f}); live GW2-{le} {h[2]} vs classic {c[2]}")
PY
)"
log "${TAG^^} CHAIN DONE"

#!/usr/bin/env bash
# H3 (2026-10-15): availability-only regression head on ALL players (classic P(appear) in [0.15, 0.95]), trained on
# 2022-23..2024-25, evaluated on all of 2025-26 (GW2-38, 9 decision windows) and live 2026-27 GW2-6. Decision arms:
# classic, head P(appear) through the production threshold optimizer, head P coupled into points via the Platt ratio
# (scripts/avail_couple_preds.py), and the soft-availability optimizer. One GPU job; peak ~25-30 GB (batch 1, no ckpt).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h3_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H3 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
SPLIT=reports/llm_residual_v2_e22_all_thru_2425_38_eval_2526_2_38; LSPLIT=reports/llm_residual_v2_e22_all_eval_2627_2_6
DATA=reports/h3_data; ADAPTER=artifacts/gemma4_e4b_h3_avail_reghead; OUT=reports/h_series; CAP=${CAP:-16000}
WINDOWS=("2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25" "2025-26 27 30" "2025-26 31 34" "2025-26 35 38")
log "=== H3: availability head on all players (cap $CAP train rows) ==="
until grep -q "SPLITS DONE\|SPLITS FAILED" logs/h3_splits.log 2>/dev/null; do sleep 60; done
grep -q "SPLITS DONE" logs/h3_splits.log || die "splits"
mkdir -p "$DATA"
python3 scripts/filter_split_rows.py "$SPLIT/train.jsonl" "$DATA/train.jsonl" --mode train --cap "$CAP" --seed 7 | tee -a "$LOG"
python3 scripts/filter_split_rows.py "$SPLIT/eval.jsonl" "$DATA/eval.jsonl" --mode eval | tee -a "$LOG"
python3 scripts/filter_split_rows.py "$LSPLIT/eval.jsonl" "$DATA/live_eval.jsonl" --mode eval | tee -a "$LOG"
[ -s "$DATA/train.jsonl" ] && [ -s "$DATA/eval.jsonl" ] && [ -s "$DATA/live_eval.jsonl" ] || die "filtered rows"
bt(){ local dir=$1 season=$2 a=$3 b=$4 variant=$5 ex=$6 pr=$7 fields=$8; mkdir -p "$(dirname "$dir")"; local extra=()
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  [ -n "$ex" ] && extra=(--llm-examples "$ex" --llm-predictions "$pr" --llm-fields "$fields")
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch --decision-variant "$variant" "${extra[@]}" > "$dir.log" 2>&1; }
arm(){ local tag=$1 variant=$2 hp=$3 lp=$4 fields=$5; local n=0
  for W in "${WINDOWS[@]}"; do set -- $W; bt "$OUT/$tag/$1_$2_$3" $1 $2 $3 $variant "${hp:+$DATA/eval.jsonl}" "$hp" $fields & n=$((n+1)); [ $((n % 5)) = 0 ] && wait; done
  bt "$OUT/$tag/2026-27_2_6" 2026-27 2 6 $variant "${lp:+$DATA/live_eval.jsonl}" "$lp" $fields & wait; }
log "classic references (CPU, background)"
( arm bt_h3_classic baseline "" "" all; arm bt_h3_classic_soft avail_soft "" "" all; log "classic references done" ) &
log "=== H3 training ==="
FPL_RH_DATA_DIR=$DATA FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=1 FPL_RH_ACCUM=16 FPL_RH_CKPT=0 \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=200 FPL_RH_COMPACT=1 FPL_RH_FIELDS=availability \
  python3 -u train_gemma_reghead.py >> logs/train_h3.log 2>&1
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training"
log "=== H3 predictions ==="
python3 -u scripts/reghead_predict.py "$DATA/eval.jsonl" "$ADAPTER" "$OUT/h3_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "holdout predict"
python3 -u scripts/reghead_predict.py "$DATA/live_eval.jsonl" "$ADAPTER" "$OUT/h3_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "live predict"
wait
log "=== H3 ledger ==="
python3 scripts/avail_couple_preds.py "$DATA/eval.jsonl" "$OUT/h3_holdout_pred.jsonl" "$OUT/h3_holdout_coupled.jsonl" "$OUT/h3_holdout_platt.jsonl" \
  --platt "$OUT/platt_all.json" --fit-from "$DATA/train.jsonl" | tee -a "$LOG"
python3 scripts/avail_couple_preds.py "$DATA/live_eval.jsonl" "$OUT/h3_live_pred.jsonl" "$OUT/h3_live_coupled.jsonl" "$OUT/h3_live_platt.jsonl" --platt "$OUT/platt_all.json" | tee -a "$LOG"
{ echo "## H3 holdout 2025-26 GW2-38 (all players, uncertain rows)"; python3 scripts/avail_ledger.py "$DATA/eval.jsonl" "$OUT/h3_holdout_pred.jsonl" --platt "$OUT/platt_all.json" --label H3
  echo; echo "## H3 live 2026-27 GW2-6"; python3 scripts/avail_ledger.py "$DATA/live_eval.jsonl" "$OUT/h3_live_pred.jsonl" --platt "$OUT/platt_all.json" --label H3 --windows 5; } > "$OUT/h3_availability.md" 2>&1
cat "$OUT/h3_availability.md" >> "$LOG"
log "=== H3 decision backtests ==="
arm bt_h3_availability baseline "$OUT/h3_holdout_pred.jsonl" "$OUT/h3_live_pred.jsonl" availability
arm bt_h3_coupled baseline "$OUT/h3_holdout_coupled.jsonl" "$OUT/h3_live_coupled.jsonl" points
arm bt_h3_coupled_soft avail_soft "$OUT/h3_holdout_coupled.jsonl" "$OUT/h3_live_coupled.jsonl" all
arm bt_h3_platt_soft avail_soft "$OUT/h3_holdout_platt.jsonl" "$OUT/h3_live_platt.jsonl" availability
log "RESULT: $(python3 - <<'PY'
import json
def tot(p):
    try: return json.load(open(p))["total_actual_points"]
    except Exception: return None
W=[(2,5),(6,9),(10,13),(14,17),(18,21),(22,25),(27,30),(31,34),(35,38)]; out=[]
for tag in ["bt_h3_classic","bt_h3_availability","bt_h3_coupled","bt_h3_classic_soft","bt_h3_coupled_soft","bt_h3_platt_soft"]:
    w=[tot(f"reports/h_series/{tag}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a,b in W]; l=tot(f"reports/h_series/{tag}/2026-27_2_6/rolling_squad_backtest.json")
    out.append(f"{tag}: holdout {[int(x) if x is not None else None for x in w]} = {sum(x for x in w if x is not None):.0f}, live {l}")
print(" | ".join(out))
PY
)"
log "H3 CHAIN DONE"

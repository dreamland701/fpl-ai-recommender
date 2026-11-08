#!/usr/bin/env bash
# E20 variant backtests (2025-26 GW27-38, fixed classic+F6) and the live
# E11-full shadow replay (2026-27 GW2-5) on the old and fixed pipelines.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OLD=/home/wescheng/fpl_backups/2026-10-03_pre_review_fixes/src
R=$ROOT/reports/review_fixes_2026_10; OUT=$R/bt_sft_variants; mkdir -p "$OUT"
SPLIT=$ROOT/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl
E20=$ROOT/reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl
V=$R/e20_variants; LIVE=$R/e11full_live_gw2_5_predictions.jsonl
run() { # tag src table season a b examples preds fields
  local tag=$1 src=$2 table=$3 season=$4 a=$5 b=$6 ex=$7 pr=$8 fields=$9
  local dir="$OUT/${tag}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ "$ex" != none ] && extra=(--llm-examples "$ex" --llm-predictions "$pr" --llm-fields "$fields")
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 10 \
    $PY -m fpl_ai.cli backtest-squad --training-data $table --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week $a --end-week $b --output-dir "$dir" "${extra[@]}" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run; export ROOT PY OLD R OUT SPLIT E20 V LIVE
{
for W in "27 30" "31 34" "35 38"; do
  echo "points src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $E20 points"
  echo "availability src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $E20 availability"
  echo "availscaled src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $E20 availability_scaled"
  echo "deshrunk src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $V/e20_pred_deshrunk.jsonl all"
  echo "shrinkonly src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $V/e20_pred_shrinkonly.jsonl all"
  echo "demean src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $V/e20_pred_demean.jsonl all"
  echo "availnorm src/ data/fpl_training_rows_v3_contract_f6.csv 2025-26 $W $SPLIT $V/e20_pred_availnorm.jsonl points"
done
for spec in "NC src/ data/fpl_training_rows_v3_contract.csv" "NF src/ data/fpl_training_rows_v3_contract_f6.csv" "OC $OLD data/fpl_training_rows_blend.csv"; do
  set -- $spec
  echo "live_classic_$1 $2 $3 2026-27 2 5 none none all"
  echo "live_e11full_$1 $2 $3 2026-27 2 5 $LIVE $LIVE all"
done
} | sed "s#src/#$ROOT/src#" | xargs -P 10 -L 1 bash -c 'run "$@"' _
echo VARIANTS DONE

#!/usr/bin/env bash
# Replicate "route the adapter's availability into points" on the fixed pipeline
# with the out-of-sample predictions of three earlier adapters (18 windows).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
R=$ROOT/reports/review_fixes_2026_10; OUT=$R/avail_replication/bt; mkdir -p "$OUT"
run() { # tag season a b examples preds fields
  local dir="$OUT/$1_$2_$3_$4"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 15 \
    $PY -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season "$2" \
    --initial-train-week-max $(( $3 - 1 )) --start-week $3 --end-week $4 --output-dir "$dir" \
    --llm-examples "$5" --llm-predictions "$6" --llm-fields "$7" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run; export ROOT PY R OUT
E9X=reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30/eval.jsonl
E9P=reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl
C24X=reports/llm_residual_v2_e7chrono2324_top256_scout_thru_2324gw11_eval_2324gw12_38/eval.jsonl
C24P=reports/gemma4_e4b_residual_e7chrono2324_2324gw12_38_sft_predictions.jsonl
C25X=reports/llm_residual_v2_e7chrono2425_evalext_2425gw12_38/eval.jsonl
C25P=reports/gemma4_e4b_residual_e7chrono2425_evalext_2425gw12_38_sft_predictions.jsonl
{
for W in "2 5" "6 9" "10 13" "14 17" "18 21" "22 25"; do set -- $W
  echo "all 2025-26 $1 $2 $E9X $E9P all"; echo "availscaled 2025-26 $1 $2 $E9X $E9P availability_scaled"
  echo "availnorm 2025-26 $1 $2 $E9X $R/avail_replication/e9_pred_availnorm.jsonl points"; done
for W in "12 15" "16 19" "20 23" "24 27" "28 31" "32 35"; do set -- $W
  echo "all 2023-24 $1 $2 $C24X $C24P all"; echo "availscaled 2023-24 $1 $2 $C24X $C24P availability_scaled"
  echo "availnorm 2023-24 $1 $2 $C24X $R/avail_replication/e7c2324_pred_availnorm.jsonl points"
  echo "all 2024-25 $1 $2 $C25X $C25P all"; echo "availscaled 2024-25 $1 $2 $C25X $C25P availability_scaled"
  echo "availnorm 2024-25 $1 $2 $C25X $R/avail_replication/e7c2425_pred_availnorm.jsonl points"; done
} | xargs -P 8 -L 1 bash -c 'run "$@"' _
echo REPLICATION DONE

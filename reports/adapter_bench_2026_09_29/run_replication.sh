#!/usr/bin/env bash
# Replicate V3 (availability-normalized points) on 18 windows independent of E19.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
T=/home/wescheng/projects/fpl/fpl/reports/adapter_bench_2026_09_29
mkdir -p $T/rep
run(){ # tag season a b [examples preds fields]
  local tag=$1 season=$2 a=$3 b=$4; shift 4
  local extra=()
  if [ $# -gt 0 ]; then extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields "$3"); fi
  PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_blend_f6.csv --test-season "$season" --initial-train-week-max $((a-1)) \
    --start-week $a --end-week $b --output-dir "$T/rep/${tag}_${season}_${a}_${b}" \
    "${extra[@]}" --skip-league-average-fetch > "$T/rep/${tag}_${season}_${a}_${b}.log" 2>&1
}
E9X=reports/llm_residual_v2_e9_cleansplit_top256_thru_2425_eval_2526_gw2_30/eval.jsonl
E9P=reports/gemma4_e4b_residual_e9_cleansplit_gw2_30_sft_predictions.jsonl
C24X=reports/llm_residual_v2_e7chrono2324_top256_scout_thru_2324gw11_eval_2324gw12_38/eval.jsonl
C24P=reports/gemma4_e4b_residual_e7chrono2324_2324gw12_38_sft_predictions.jsonl
C25X=reports/llm_residual_v2_e7chrono2425_evalext_2425gw12_38/eval.jsonl
C25P=reports/gemma4_e4b_residual_e7chrono2425_evalext_2425gw12_38_sft_predictions.jsonl
batch(){ # season examples preds v3preds windows...
  local season=$1 X=$2 P=$3 V3=$4; shift 4
  for W in "$@"; do set -- $W
    run classic "$season" $1 $2 &
    run v0 "$season" $1 $2 "$X" "$P" all &
    run v3 "$season" $1 $2 "$X" "$V3" points &
  done
}
batch 2025-26 $E9X $E9P $T/e9_pred_availnorm.jsonl "2 5" "6 9" "10 13" "14 17" "18 21" "22 25"
wait
batch 2023-24 $C24X $C24P $T/e7c2324_pred_availnorm.jsonl "12 15" "16 19" "20 23" "24 27" "28 31" "32 35"
wait
batch 2024-25 $C25X $C25P $T/e7c2425_pred_availnorm.jsonl "12 15" "16 19" "20 23" "24 27" "28 31" "32 35"
wait
echo ALL DONE

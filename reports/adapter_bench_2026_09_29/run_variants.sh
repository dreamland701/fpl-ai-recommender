#!/usr/bin/env bash
# E19 adapter variants on the three GW27-38 windows. Outputs to job tmp only.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
T=/home/wescheng/projects/fpl/fpl/reports/adapter_bench_2026_09_29
EX=$ROOT/reports/llm_residual_v2_e19_wideholdout_top256_thru_2526_26_eval_2526_27_38/eval.jsonl
ORIG=$ROOT/reports/gemma4_e4b_residual_e19_gw27_38_sft_predictions.jsonl
run(){ # name preds fields a b
  PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_blend_f6.csv --test-season 2025-26 --initial-train-week-max 26 \
    --start-week $4 --end-week $5 --output-dir "$T/bt/$1_$4_$5" \
    --llm-examples "$EX" --llm-predictions "$2" --llm-fields "$3" --skip-league-average-fetch > "$T/bt/$1_$4_$5.log" 2>&1
}
mkdir -p $T/bt
for W in "27 30" "31 34" "35 38"; do
  set -- $W
  run v0_all "$ORIG" all $1 $2 &
  run v1_deshrunk "$T/e19_pred_deshrunk.jsonl" all $1 $2 &
  run v2_availscaled "$ORIG" availability_scaled $1 $2 &
  run v3_availnorm "$T/e19_pred_availnorm.jsonl" points $1 $2 &
  run v4_shrinkonly "$T/e19_pred_shrinkonly.jsonl" all $1 $2 &
  run v5_evidgated "$T/e19_pred_evidgated.jsonl" all $1 $2 &
done
wait
echo ALL DONE

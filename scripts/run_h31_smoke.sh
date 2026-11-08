#!/usr/bin/env bash
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_RH_4BIT=1 FPL_RH_MODEL=/home/wescheng/models/gemma-4-31b-it FPL_RH_DATA_DIR=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38
export FPL_RH_OUTPUT_DIR=artifacts/_h31_smoke FPL_RH_MAX_ROWS=64 FPL_RH_MAX_STEPS=4 FPL_RH_BATCH=1 FPL_RH_ACCUM=4 FPL_RH_CKPT=1 FPL_RH_SAVE_STEPS=1000 FPL_RH_COMPACT=1
echo "$(date '+%F %T') smoke start"; timeout 2400 python3 -u train_gemma_reghead.py; echo "$(date '+%F %T') smoke train exit $?"
echo "$(date '+%F %T') predict smoke (8 rows)"; head -n 8 reports/llm_residual_v2_e22_top96_eval_2627_2_6/eval.jsonl > artifacts/_h31_smoke/ex8.jsonl
timeout 1200 python3 -u scripts/reghead_predict.py artifacts/_h31_smoke/ex8.jsonl artifacts/_h31_smoke artifacts/_h31_smoke/pred8.jsonl 4; echo "$(date '+%F %T') predict exit $?"
echo "$(date '+%F %T') H31 SMOKE DONE"

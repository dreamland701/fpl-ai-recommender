#!/usr/bin/env bash
# P0 (2026-10-15): LoRA training throughput probe on the E21 rows; results as RESULT lines in logs/probe_lora.log.
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
echo "$(date '+%F %T') probe start" >> logs/probe_lora.log
python3 -u scripts/probe_lora_throughput.py reports/llm_residual_v2_e21_clean_top96_thru_2526_26_eval_2526_27_38/train.jsonl >> logs/probe_lora.log 2>&1
echo "$(date '+%F %T') probe done" >> logs/probe_lora.log

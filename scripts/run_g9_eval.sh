#!/usr/bin/env bash
# G9 eval only (the chain's training finished 2026-10-13 04:10; its eval crashed on the infeasible 2025-26
# week-22 free-hit rebuild, now a kept chip in PlanEnvV2.rollout).
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1
LOG=logs/g9_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
H=2025-26:2,2023-24:2,2024-25:2
OUT=artifacts/gemma4_e4b_g9
log "=== G9 eval rerun (closed loop, g9 state) ==="
FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --detail g9 --adapter-path $OUT --halves $H \
  --output reports/grpo_states_v2/eval_g9.json >> "$LOG" 2>&1 || log "G9 eval FAILED"
G9=$(python3 -c "
import json; d=json.load(open('reports/grpo_states_v2/eval_g9.json')); print(json.dumps(d)[:600])" 2>/dev/null)
log "G9 eval json: $G9"
log "G9 EVAL DONE"

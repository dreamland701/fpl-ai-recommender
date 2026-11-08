#!/usr/bin/env bash
# Re-run the closed-loop holdout evals on the bank-fixed states (2026-10-10). The earlier numbers
# (planner 766, untrained 749, G5 749, G5b 731) started GW27 with a spurious £100m in the bank.
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONDONTWRITEBYTECODE=1 FPL_GEN_DEVICE_MAP=gpu
while pgrep -f "[r]un_chip_advisor_eval" >/dev/null; do sleep 60; done
S=reports/grpo_states_v2/2025-26-holdout.jsonl
for pair in "untrained:none" "g5:artifacts/gemma4_e4b_grpo_plan_g5" "g5b:artifacts/gemma4_e4b_grpo_plan_g5b"; do
  tag=${pair%%:*}; ad=${pair#*:}
  python3 scripts/run_grpo_plan_eval_v2.py --states $S --adapter-path "$ad" --output reports/grpo_states_v2/eval_holdout_${tag}_fixedbank.json >> logs/rerun_g5_fixedbank.log 2>&1
done
python3 - <<'PY' | tee -a logs/rerun_g5_fixedbank.log
import json
for tag in ("untrained", "g5", "g5b"):
    d = json.load(open(f"reports/grpo_states_v2/eval_holdout_{tag}_fixedbank.json")); s = d["summary"]
    print(f"{tag}: policy {s.get('policy')} | planner {s['planner']} | classic no chips {s['classic_no_chips']} | invalid {len(d['invalid_weeks'])}")
PY
echo FIXEDBANK EVALS DONE | tee -a logs/rerun_g5_fixedbank.log

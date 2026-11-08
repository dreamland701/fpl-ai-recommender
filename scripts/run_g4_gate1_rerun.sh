#!/usr/bin/env bash
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/g4_gate1_rerun.log
echo "$(date '+%F %T') gate-1 rerun start (alongside E14, batch 8)" >> $LOG
PYTHONPATH=src python3 scripts/run_g4_decision_eval.py --model-path artifacts/gemma4_e4b_merged_e11_defcon --tag e11ref >> $LOG 2>&1
PYTHONPATH=src python3 scripts/run_g4_decision_eval.py --model-path artifacts/gemma4_e4b_merged_e11_defcon --adapter-path artifacts/gemma4_e4b_g4_forecast_v2 --tag g4 >> $LOG 2>&1
python3 - <<PYEOF >> $LOG 2>&1
import json
e = json.load(open("reports/g4_decision_eval_e11ref.json")); g = json.load(open("reports/g4_decision_eval_g4.json"))
tot = lambda rows, k: sum(r[k] for r in rows)
print(f"DECISION GW30-38: classic {tot(e,'classic'):.0f} | E11 {tot(e,'e11ref'):.0f} | G4 {tot(g,'g4'):.0f}")
clean = [(a, b) for a, b in zip(e, g) if a['week'] >= 35]
print(f"DECISION GW35-38 (clean): classic {sum(a['classic'] for a,_ in clean):.0f} | E11 {sum(a['e11ref'] for a,_ in clean):.0f} | G4 {sum(b['g4'] for _,b in clean):.0f}")
wins = sum(1 for a, b in zip(e, g) if b['g4'] > a['e11ref']); ties = sum(1 for a, b in zip(e, g) if b['g4'] == a['e11ref'])
print(f"G4 vs E11 per week: wins {wins} ties {ties} losses {len(g)-wins-ties}")
PYEOF
echo "$(date '+%F %T') GATE-1 RERUN COMPLETE" >> $LOG

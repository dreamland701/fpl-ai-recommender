#!/usr/bin/env bash
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/f2c_backtests.log
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
log "rebuilding blend table with F2b+F2c"
FPL_PRIOR_BLEND=1 PYTHONPATH=src python3 -m fpl_ai.cli build-training-table --history-root data/fpl_history --output data/fpl_training_rows_blend_v2.csv >> "$LOG" 2>&1
for season in 2023-24 2024-25 2025-26; do
  PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_blend_v2.csv --test-season $season \
    --initial-train-week-max 1 --start-week 2 --end-week 8 \
    --decision-variant baseline \
    --output-dir reports/backtest_f2c_${season} >> "$LOG" 2>&1
  python3 -c "
import json
d = json.load(open('reports/backtest_f2c_${season}/rolling_squad_backtest.json'))
print(f'$season blend_v2: actual {d[\"total_actual_points\"]}')" >> "$LOG" 2>&1
done
log "F2C MATRIX COMPLETE (compare: base 389/408/409, f2b-blend 411/440/406)"

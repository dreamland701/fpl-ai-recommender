#!/usr/bin/env bash
set -uo pipefail
ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG="logs/premiumfix_backtests.log"
log() { echo "$(date '+%F %T') $*" >> "$LOG"; }
run() {
  local name="$1"; shift
  log "START $name"
  PYTHONPATH=src python3 -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows.csv \
    --test-season 2025-26 \
    --output-dir "reports/backtest_premiumfix_$name" \
    "$@" >> "$LOG" 2>&1
  local pts
  pts=$(python3 -c "import json;d=json.load(open('reports/backtest_premiumfix_$name/summary.json'));print(d.get('total_points') or d.get('classic_total') or d)" 2>/dev/null)
  log "DONE $name total=$pts"
}
run base --decision-variant baseline
FPL_BAND_CALIBRATION=1 run cal --decision-variant baseline
FPL_DRAFT_CAPTAIN_LEVERAGE=0.5 run lev --decision-variant captlev3
FPL_BAND_CALIBRATION=1 FPL_DRAFT_CAPTAIN_LEVERAGE=0.5 run both --decision-variant captlev3
log "MATRIX COMPLETE"

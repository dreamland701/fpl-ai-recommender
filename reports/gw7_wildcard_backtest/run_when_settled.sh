#!/usr/bin/env bash
# Score the pre-registered GW7 wildcard proposal once GW7 is settled.
# Checks every 6 hours from 2026-10-19 until 2026-10-31; writes README.md here.
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl
HERE=reports/gw7_wildcard_backtest
LOG=$HERE/run_when_settled.log
log(){ echo "$(date '+%F %T') $*" >> "$LOG"; }
START=$(date -d '2026-10-19T07:00:00Z' +%s); END=$(date -d '2026-10-31T07:00:00Z' +%s)
[ "$(date +%s)" -lt "$START" ] && { log "sleeping until 2026-10-19 07:00 UTC"; sleep $(( START - $(date +%s) )); }
while [ "$(date +%s)" -lt "$END" ]; do
  if PYTHONDONTWRITEBYTECODE=1 /home/wescheng/venvs/fpl-gemma-lite/bin/python $HERE/score_gw7.py >> "$LOG" 2>&1; then
    log "GW7 scored -> $HERE/README.md"; exit 0
  fi
  log "not settled yet; next check in 6h"; sleep 21600
done
log "gave up: GW7 still not settled by 2026-10-31"

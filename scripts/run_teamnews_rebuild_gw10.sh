#!/usr/bin/env bash
# Rebuild the F16 team-news table variant on the GW9-ingested production table (CPU; "re-run after every weekly table rebuild"),
# so Friday's GW10 final refresh can write the F16 shadow. Atomic: writes .new then mv. Log logs/teamnews_rebuild_gw10.log.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1
LOG=logs/teamnews_rebuild_gw10.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
TN=data/fpl_training_rows_v3_contract_f6_teamnews.csv
log "=== team-news table rebuild on data/fpl_training_rows_v3_contract_f6.csv ==="
if python3 scripts/build_team_news_table.py --table data/fpl_training_rows_v3_contract_f6.csv --out "$TN.new" >> "$LOG" 2>&1; then
  mv "$TN.new" "$TN"; log "TEAMNEWS REBUILD DONE: $(wc -l < "$TN") lines"
else
  log "TEAMNEWS REBUILD FAILED"; rm -f "$TN.new"
fi

#!/usr/bin/env bash
# GW9 interim packet (Tue 2026-10-27; deadline Sat 2026-10-31 11:00 UTC = 04:00 PDT): entry, frozen snapshot,
# classic+F6 forecasts on the GW8-rebuilt tables, decision sheet, exact optimizer, lineups, role-override sheet
# (Konsa -> Calafiori candidate), README. CPU only. Writes into reports/gw9_packet_2026_10/ (the packet root is the
# interim; Saturday's final refresh writes final/).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1
PACKET=$ROOT/reports/gw9_packet_2026_10; export PACKET_DIR=$PACKET
LOG=$PACKET/build.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "=== GW9 interim packet -> $PACKET ==="
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$PACKET/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$PACKET/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$PACKET/milp.log" 2>&1 || log "milp FAILED"
python3 "$PACKET/route_lineups.py" > "$PACKET/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$PACKET" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$PACKET/entry_state.json" --asof-week 9 --transfer Konsa:Calafiori --auto --out-md "$PACKET/role_override_sheet.md" \
  --out-jsonl "$PACKET/forecasts_role_override.jsonl" > "$PACKET/role_override.log" 2>&1 || log "role override sheet FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "summary FAILED"
log "GW9 INTERIM DONE: $PACKET/README.md"

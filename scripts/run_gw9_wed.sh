#!/usr/bin/env bash
# GW9 Wednesday packet (Wes sets his squad Wed 2026-10-28 16:00 PDT; deadline Sat 2026-10-31 11:00 UTC = 04:00 PDT):
# fresh entry + snapshot, classic+F6 forecasts, decision sheet, exact optimizer, the Isak-forced routes
# (João Pedro -> Isak with 1/2/3 moves), lineups, role-override sheet (João Pedro:Isak and Konsa:Calafiori as
# transfer counterfactuals), README comparing against Tuesday's interim. CPU only. Writes reports/gw9_packet_2026_10/wed/.
# SLEEP_UNTIL=<ISO UTC> sleeps first (the armed copy); empty = run now. Kill by pid in logs/pids/gw9_wed.pid to veto.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1
PACKET=$ROOT/reports/gw9_packet_2026_10; WED=$PACKET/wed; export PACKET_DIR=$WED; mkdir -p "$WED"
LOG=$WED/build.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
if [ -n "${SLEEP_UNTIL:-}" ]; then
  TARGET=$(date -d "$SLEEP_UNTIL" +%s); NOW=$(date +%s)
  if [ "$NOW" -lt "$TARGET" ]; then log "armed; sleeping until $SLEEP_UNTIL"; sleep $(( TARGET - NOW )); fi
fi
log "=== GW9 Wednesday packet -> $WED ==="
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$WED/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$WED/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$WED/milp.log" 2>&1 || log "milp FAILED"
FORCE_IN=Isak FORCE_OUT="João Pedro" python3 "$PACKET/forced_routes.py" > "$WED/forced_routes.log" 2>&1 || log "forced routes FAILED"
python3 "$PACKET/route_lineups.py" > "$WED/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$WED" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$WED/entry_state.json" \
  --asof-week 9 --transfer "João Pedro:Isak" --auto --out-md "$WED/role_override_sheet_isak.md" \
  --out-jsonl "$WED/forecasts_role_override_isak.jsonl" > "$WED/role_override_isak.log" 2>&1 || log "role override (Isak) FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$WED" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$WED/entry_state.json" \
  --asof-week 9 --transfer Konsa:Calafiori --auto --out-md "$WED/role_override_sheet.md" \
  --out-jsonl "$WED/forecasts_role_override.jsonl" > "$WED/role_override.log" 2>&1 || log "role override sheet FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "summary FAILED"
log "GW9 WED DONE: $WED/README.md"

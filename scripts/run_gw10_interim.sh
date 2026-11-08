#!/usr/bin/env bash
# GW10 interim packet (Wed 2026-11-04 22:30 PST; deadline Fri 2026-11-06 18:30 UTC = 10:30 PST; first kickoff EVE v COV Fri 20:00Z).
# Entry, frozen snapshot, classic+F6 forecasts on the GW9-rebuilt table (cutoff 9), decision sheet, exact optimizer, lineups,
# role-override sheet (--auto), README. CPU only (the GPU is running the H12 trainer). Writes into reports/gw10_packet_2026_11/
# by default (the packet root is the interim); PACKET_DIR=<packet>/thu re-runs it as Thursday's re-pick.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1
PACKET=$ROOT/reports/gw10_packet_2026_11; OUT=${PACKET_DIR:-$PACKET}; export PACKET_DIR=$OUT; mkdir -p "$OUT"
LOG=$OUT/build.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "=== GW10 interim packet -> $OUT ==="
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$OUT/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$OUT/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$OUT/milp.log" 2>&1 || log "milp FAILED"
python3 "$PACKET/route_lineups.py" > "$OUT/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$OUT" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$OUT/entry_state.json" \
  --asof-week 10 --auto --out-md "$OUT/role_override_sheet.md" --out-jsonl "$OUT/forecasts_role_override.jsonl" > "$OUT/role_override.log" 2>&1 || log "role override sheet FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "summary FAILED"
log "GW10 INTERIM DONE: $OUT/README.md"

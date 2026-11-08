#!/usr/bin/env bash
# Post-ingest rebuild (written 2026-11-03): the manual steps run_weekly_ingest.sh prints, done in order.
#   1. bump TRAINING_CUTOFF_WEEK to <gw> in src/fpl_ai/config.py
#   2. rebuild both fixed-pipeline tables (classic+F6 decisions table; classic table for the E11-full shadow baselines),
#      each into a .new file then an atomic mv, so a backtest that already opened the old file keeps its inode
#   3. parity audit of the next GW's live frame vs history
# Usage: scripts/run_post_ingest_rebuild.sh <completed_gw> <next_deadline_iso> <next_packet_dir>
# Log: stdout (launch with nohup); sentinel "POST-INGEST DONE" / "POST-INGEST FAILED".
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
GW=$1; DEADLINE=$2; PACKET=$3
log(){ echo "$(date '+%F %T') $*"; }; die(){ log "POST-INGEST FAILED: $*"; exit 1; }
export PYTHONPATH=src PYTHONDONTWRITEBYTECODE=1
log "=== step 1: TRAINING_CUTOFF_WEEK -> $GW ==="
sed -i -E "s/^TRAINING_CUTOFF_WEEK = [0-9]+$/TRAINING_CUTOFF_WEEK = $GW/" src/fpl_ai/config.py
grep -q "^TRAINING_CUTOFF_WEEK = $GW$" src/fpl_ai/config.py || die "cutoff bump did not apply"
log "=== step 2a: classic+F6 table ==="
FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 -m fpl_ai.cli build-training-table --history-root data/fpl_history \
  --output data/fpl_training_rows_v3_contract_f6.csv.new || die "F6 table build"
[ -s data/fpl_training_rows_v3_contract_f6.csv.new ] || die "F6 table empty"
mv data/fpl_training_rows_v3_contract_f6.csv.new data/fpl_training_rows_v3_contract_f6.csv
log "F6 table: $(wc -l < data/fpl_training_rows_v3_contract_f6.csv) lines"
log "=== step 2b: classic table (E11-full shadow baselines) ==="
FPL_PRIOR_BLEND=1 python3 -m fpl_ai.cli build-training-table --history-root data/fpl_history \
  --output data/fpl_training_rows_v3_contract.csv.new || die "classic table build"
[ -s data/fpl_training_rows_v3_contract.csv.new ] || die "classic table empty"
mv data/fpl_training_rows_v3_contract.csv.new data/fpl_training_rows_v3_contract.csv
log "classic table: $(wc -l < data/fpl_training_rows_v3_contract.csv) lines"
log "=== step 3: parity audit for the next GW (deadline $DEADLINE) ==="
mkdir -p "$PACKET"
FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 scripts/train_live_parity_audit.py --deadline-ts "$DEADLINE" --out "$PACKET/parity_audit.md" || log "parity audit FAILED (non-fatal)"
log "POST-INGEST DONE"

#!/usr/bin/env bash
# GW8 weekly ingest + rebuild chain (2026-10-26, cron part 2). CPU only. Sentinel: "WEEKLY GW8 REBUILD DONE" / "WEEKLY GW8 FAILED".
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/weekly_rebuild_gw8.log
log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
die(){ log "STOP: $*"; log "WEEKLY GW8 FAILED"; exit 1; }
grep -q "H5 CHAIN DONE\|H5 FAILED" logs/h5_chain.log || die "H5 chain still running"
pgrep -f "^python3 .*(backtest[-]squad|train_gemma[_]reghead|reghead[_]predict)" > /dev/null && die "a process is still using the tables"
log "=== 0/7 backup production tables + feature jsons -> data/backup_2026_10_26 ==="
if [ -d data/backup_2026_10_26 ]; then log "backup already exists (pre-ingest tables of 10-26), keeping it"; else
mkdir -p data/backup_2026_10_26
cp -p data/fpl_training_rows_v3_contract_f6.csv data/fpl_training_rows_v3_contract.csv data/backup_2026_10_26/ || die "backup"
cp -p reports/team_news_f16/gn_feat.json reports/extract_facts/facts_by_player_week_combined.json data/backup_2026_10_26/ || die "backup jsons"
fi
log "=== 1/7 weekly ingest (settled gate -> sync -> status backfill -> verify) ==="
bash scripts/run_weekly_ingest.sh 8 > logs/weekly_ingest_gw8.log 2>&1
grep -q "ingestion OK" logs/weekly_ingest_gw8.log || die "ingest did not report OK (see logs/weekly_ingest_gw8.log)"
grep -E "flagged rate|status distribution|rows:" logs/weekly_ingest_gw8.log | tail -3 | tee -a "$LOG"
log "=== 2/7 cutoff 7 -> 8 ==="
sed -i 's/^TRAINING_CUTOFF_WEEK = 7$/TRAINING_CUTOFF_WEEK = 8/' src/fpl_ai/config.py
grep -q "^TRAINING_CUTOFF_WEEK = 8$" src/fpl_ai/config.py || die "cutoff bump"
log "=== 3/7 rebuild F6 table ==="
FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python3 -m fpl_ai.cli build-training-table --history-root data/fpl_history --output data/fpl_training_rows_v3_contract_f6.csv >> "$LOG" 2>&1 || die "F6 table"
log "=== 4/7 rebuild classic table ==="
FPL_PRIOR_BLEND=1 PYTHONPATH=src python3 -m fpl_ai.cli build-training-table --history-root data/fpl_history --output data/fpl_training_rows_v3_contract.csv >> "$LOG" 2>&1 || die "classic table"
log "rows: f6 $(wc -l < data/fpl_training_rows_v3_contract_f6.csv) classic $(wc -l < data/fpl_training_rows_v3_contract.csv) (were 195576)"
log "=== 5/7 team news table (F16, Guardian predicted lineups) ==="
PYTHONPATH=src python3 scripts/build_team_news_table.py --table data/fpl_training_rows_v3_contract_f6.csv --out data/fpl_training_rows_v3_contract_f6_teamnews.csv --feat-json reports/team_news_f16/gn_feat.json >> "$LOG" 2>&1 || die "team news table"
log "=== 6/7 extract features (combined 31B availability + Haiku role facts) ==="
PYTHONPATH=src python3 scripts/build_extract_features.py --docs reports/extract_facts/docs_all.jsonl --facts reports/extract_facts/backfill_combined.jsonl --table data/fpl_training_rows_v3_contract_f6_teamnews.csv --out data/fpl_training_rows_v3_contract_f6_extract_combined.csv --feat-json reports/extract_facts/facts_by_player_week_combined.json >> "$LOG" 2>&1 || die "extract features"
log "=== 7/7 parity audit GW9 (deadline 2026-10-31T11:00:00Z) ==="
mkdir -p reports/gw9_packet_2026_10
FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python3 scripts/train_live_parity_audit.py --deadline-ts 2026-10-31T11:00:00Z --training-data data/fpl_training_rows_v3_contract_f6.csv --seasons 2023-24 2024-25 2025-26 --out reports/gw9_packet_2026_10/parity_audit.md >> "$LOG" 2>&1 || die "parity audit"
grep -E "^Flags:" reports/gw9_packet_2026_10/parity_audit.md | tee -a "$LOG"
log "WEEKLY GW8 REBUILD DONE"

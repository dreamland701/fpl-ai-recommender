#!/usr/bin/env bash
# GW8 final refresh (deadline 2026-10-23 17:30 UTC = 10:30 PDT): sleeps until Friday 14:00 UTC (07:00 PDT, after the
# Thursday press conferences and the Saka scan news), then rebuilds the packet (entry, snapshot, classic+F6 forecasts,
# decision sheet, exact optimizer, lineups, README), the evidence and the F6 live corpus on CPU. The H1 (E4B) shadow
# read + side-by-side sheet need the GPU: they run only if the flag file logs/gw8_gpu_ok exists (Wes's go-ahead),
# else the runbook prints the command. Kill by pid in logs/pids/gw8_final_refresh.pid to veto.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1
LOG=logs/gw8_final_refresh.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw8_packet_2026_10; FINAL=$PACKET/final; export PACKET_DIR=$FINAL
TAG=gw8final; DEADLINE=2026-10-23T17:30:00Z
TARGET=$(date -d '2026-10-23T14:00:00Z' +%s); NOW=$(date +%s)
if [ "$NOW" -lt "$TARGET" ]; then log "armed; sleeping until 2026-10-23 14:00 UTC (07:00 PDT)"; sleep $(( TARGET - NOW )); fi
if [ "$(date +%s)" -ge "$(date -d "$DEADLINE" +%s)" ]; then log "past the GW8 deadline; nothing to do"; exit 0; fi
log "=== GW8 final refresh -> $FINAL ==="; mkdir -p "$FINAL"
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$FINAL/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$FINAL/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$FINAL/milp.log" 2>&1 || log "milp FAILED"
python3 "$PACKET/route_lineups.py" > "$FINAL/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary FAILED"
TODAY=$(date -u +%F)
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-10-03 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_${TAG}.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-10-03 --output reports/evidence_pl_scout_2627_${TAG}.jsonl >> "$LOG" 2>&1 || log "scout collection FAILED"
pre=reports/live_${TAG}_2627_f6
python3 scripts/build_live_gw_examples.py --stage corpus --deadline-ts $DEADLINE --training-data data/fpl_training_rows_v3_contract_f6.csv \
  --output "${pre}_corpus_bare.jsonl" >> "$LOG" 2>&1 || log "corpus FAILED"
python3 scripts/attach_player_evidence_to_corpus.py --corpus "${pre}_corpus_bare.jsonl" \
  --evidence reports/evidence_guardian_football_2627_${TAG}.jsonl --evidence reports/evidence_guardian_football_2627_gw8interim.jsonl \
  --evidence reports/evidence_pl_scout_2627_${TAG}.jsonl --evidence reports/evidence_pl_scout_2627_gw8interim.jsonl \
  --include-non-curated --lookback-days 14 --output "${pre}_corpus_evidence.jsonl" >> "$LOG" 2>&1 || log "evidence attach FAILED"
python3 scripts/attach_fixture_outlook_to_corpus.py --corpus "${pre}_corpus_evidence.jsonl" --history-dir data/fpl_history \
  --output "${pre}_corpus_full.jsonl" >> "$LOG" 2>&1 || log "fixture outlook FAILED"
FPL_LIVE_INCLUDE_MARKET=0 python3 scripts/build_live_gw_examples.py --stage prompts --corpus "${pre}_corpus_full.jsonl" \
  --output "${pre}_examples.jsonl" >> "$LOG" 2>&1 || log "prompts FAILED"
EX=${pre}_examples.jsonl
python3 - "$EX" 2>&1 <<'PY' | tee -a "$LOG"
import json, sys
rows=[json.loads(l) for l in open(sys.argv[1])]
pa=sorted(r["metadata"]["baseline_forecast"]["baseline_appearance_probability"] for r in rows)
print("EYEBALL baseline P(app) p50/p90:", round(pa[len(pa)//2],2), round(pa[int(len(pa)*.9)],2), "rows", len(rows), "(p90 near 0.13 = cold-start bug)")
PY
PR=reports/h_series/h1_${TAG}_pred.jsonl
if [ -e logs/gw8_gpu_ok ]; then
  [ -s "$PR" ] || python3 -u scripts/reghead_predict.py "$EX" artifacts/gemma4_e4b_h1_reghead_e22 "$PR" 8 >> "$LOG" 2>&1 || log "H1 read FAILED"
  python3 scripts/sft_side_by_side.py --examples "$EX" --predictions "$PR" --entry-state "$FINAL/entry_state.json" --label h1 \
    --output-md "$FINAL/side_by_side_h1.md" >> "$LOG" 2>&1 || log "side-by-side FAILED"
else
  log "GPU step skipped (no logs/gw8_gpu_ok): H1 read -> python3 scripts/reghead_predict.py $EX artifacts/gemma4_e4b_h1_reghead_e22 $PR 8; then scripts/sft_side_by_side.py"
fi
python3 scripts/live_chip_line.py --event 8 --tag ${TAG}_2627 --no-llm --output reports/chip_line_gw8.md >> "$LOG" 2>&1 || log "chip line FAILED"
log "GW8 FINAL REFRESH DONE: $FINAL/README.md"

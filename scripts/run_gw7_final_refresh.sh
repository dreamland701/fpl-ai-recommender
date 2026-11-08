#!/usr/bin/env bash
# GW7 final refresh (deadline 2026-10-17 10:00 UTC): waits until Friday 17:00 UTC (after the press conferences),
# then rebuilds the packet, the evidence, both live corpora and the chip line on CPU. The adapter decodes and the
# G8 chip opinion need the GPU: they run only with FPL_GW7_GPU=1 (Wes's go-ahead), else the runbook prints them.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
# FPL_PER_FIXTURE=1 + HORIZON=0 (2026-10-14 ship): per-fixture minutes/1GW heads and P(appear) = minutes per fixture / 90;
# +79..+139 over 21 windows, +47 closed loop (memory fpl-dgw-pricing-defect); horizon heads stay rate-based.
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0
LOG=logs/gw7_final_refresh.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw7_packet_2026_10; FINAL=$PACKET/final; export PACKET_DIR=$FINAL
TARGET=$(date -d '2026-10-16T17:00:00Z' +%s); NOW=$(date +%s)
if [ "$NOW" -lt "$TARGET" ]; then log "armed; sleeping until 2026-10-16 17:00 UTC"; sleep $(( TARGET - NOW )); fi
if [ "$(date +%s)" -ge "$(date -d '2026-10-17T10:00:00Z' +%s)" ]; then log "past the GW7 deadline; nothing to do"; exit 0; fi
log "=== GW7 final refresh -> $FINAL ==="; mkdir -p "$FINAL"
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$FINAL/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$FINAL/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/route_lineups.py" > "$FINAL/route_lineups.log" 2>&1 || log "route lineups FAILED"
TODAY=$(date -u +%F)
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-09-26 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_gw7final.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-09-26 --output reports/evidence_pl_scout_2627_gw7final.jsonl >> "$LOG" 2>&1 || log "scout collection FAILED"
live_examples(){ local tag=$1 table=$2 pre=reports/live_gw7final_2627_$1
  FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 scripts/build_live_gw_examples.py --stage corpus --deadline-ts 2026-10-17T10:00:00Z \
    --training-data "$table" --output "${pre}_corpus_bare.jsonl" >> "$LOG" 2>&1 || return 1
  python3 scripts/attach_player_evidence_to_corpus.py --corpus "${pre}_corpus_bare.jsonl" \
    --evidence reports/evidence_guardian_football_2627_gw7final.jsonl --evidence reports/evidence_guardian_football_2627_gw6final.jsonl \
    --evidence reports/evidence_pl_scout_2627_gw7final.jsonl --evidence reports/evidence_pl_scout_2627_gw6final.jsonl \
    --include-non-curated --lookback-days 14 --output "${pre}_corpus_evidence.jsonl" >> "$LOG" 2>&1 || return 1
  python3 scripts/attach_fixture_outlook_to_corpus.py --corpus "${pre}_corpus_evidence.jsonl" --history-dir data/fpl_history \
    --output "${pre}_corpus_full.jsonl" >> "$LOG" 2>&1 || return 1
  FPL_LIVE_INCLUDE_MARKET=0 python3 scripts/build_live_gw_examples.py --stage prompts --corpus "${pre}_corpus_full.jsonl" \
    --output "${pre}_examples.jsonl" >> "$LOG" 2>&1; }
live_examples classic data/fpl_training_rows_v3_contract.csv || log "classic examples FAILED"
live_examples f6 data/fpl_training_rows_v3_contract_f6.csv || log "f6 examples FAILED"
python3 - >> "$LOG" 2>&1 <<'PY'
import json
rows=[json.loads(l) for l in open("reports/live_gw7final_2627_f6_examples.jsonl")]
pa=sorted(r["metadata"]["baseline_forecast"]["baseline_appearance_probability"] for r in rows)
print("EYEBALL baseline P(app) p50/p90:", round(pa[len(pa)//2],2), round(pa[int(len(pa)*.9)],2), "rows", len(rows), "(p90 near 0.13 = cold-start bug)")
PY
if [ "${FPL_GW7_GPU:-0}" = "1" ]; then
  bash scripts/decode_live.sh reports/live_gw7final_2627_f6_examples.jsonl reports/live_gw7final_2627_e20_predictions.jsonl \
    artifacts/gemma4_e4b_lora_residual_v2_e20_contract >> logs/live_gw7final_decode.log 2>&1 || log "E20 decode FAILED"
  python3 "$PACKET/shadow_sheet.py" reports/live_gw7final_2627_f6_examples.jsonl reports/live_gw7final_2627_e20_predictions.jsonl e20 > "$FINAL/shadow_e20.log" 2>&1 || log "E20 shadow sheet FAILED"
  FPL_GEN_DEVICE_MAP=gpu python3 scripts/live_chip_line.py --event 7 --tag gw7final_2627 --output reports/chip_line_gw7.md >> "$LOG" 2>&1 || log "chip line (G8) FAILED"
else
  python3 scripts/live_chip_line.py --event 7 --tag gw7final_2627 --no-llm --output reports/chip_line_gw7.md >> "$LOG" 2>&1 || log "chip line FAILED"
  log "GPU steps skipped (FPL_GW7_GPU unset): E20 decode + shadow sheet, G8 chip opinion"
fi
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary FAILED"
log "GW7 FINAL REFRESH DONE: $FINAL/README.md, reports/chip_line_gw7.md"

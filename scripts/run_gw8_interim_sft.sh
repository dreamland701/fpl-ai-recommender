#!/usr/bin/env bash
# GW8 interim SFT side-by-side (2026-10-21 evening PDT, after the Saka injury): evidence pull, the F6 live corpus,
# the H1 (Gemma-4-E4B regression head, merged) shadow read on the GPU (~10 min, well under the 55 GB rule), the
# sheet with the planned move and without it, and the CPU chip line. Classic decides; the adapter is in shadow.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1
LOG=logs/gw8_interim_sft.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw8_packet_2026_10; D=$PACKET/interim_1021; export PACKET_DIR=$D
TAG=gw8interim; DEADLINE=2026-10-23T17:30:00Z; TODAY=$(date -u +%F)
log "=== GW8 interim SFT chain (tag $TAG) ==="
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-10-03 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_${TAG}.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-10-03 --output reports/evidence_pl_scout_2627_${TAG}.jsonl >> "$LOG" 2>&1 || log "scout collection FAILED"
pre=reports/live_${TAG}_2627_f6
FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 scripts/build_live_gw_examples.py --stage corpus --deadline-ts $DEADLINE \
  --training-data data/fpl_training_rows_v3_contract_f6.csv --output "${pre}_corpus_bare.jsonl" >> "$LOG" 2>&1 || log "corpus FAILED"
python3 scripts/attach_player_evidence_to_corpus.py --corpus "${pre}_corpus_bare.jsonl" \
  --evidence reports/evidence_guardian_football_2627_${TAG}.jsonl --evidence reports/evidence_guardian_football_2627_gw7final.jsonl \
  --evidence reports/evidence_pl_scout_2627_${TAG}.jsonl --evidence reports/evidence_pl_scout_2627_gw7final.jsonl \
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
[ -s "$PR" ] || python3 -u scripts/reghead_predict.py "$EX" artifacts/gemma4_e4b_h1_reghead_e22 "$PR" 8 >> "$LOG" 2>&1 || log "H1 read FAILED"
python3 scripts/sft_side_by_side.py --examples "$EX" --predictions "$PR" --entry-state "$D/entry_state.json" --label h1 \
  --transfer Saka:Rogers --output-md "$D/side_by_side_h1_saka_rogers.md" >> "$LOG" 2>&1 || log "sheet (Saka->Rogers) FAILED"
python3 scripts/sft_side_by_side.py --examples "$EX" --predictions "$PR" --entry-state "$D/entry_state.json" --label h1 \
  --output-md "$D/side_by_side_h1_hold.md" >> "$LOG" 2>&1 || log "sheet (hold) FAILED"
python3 scripts/live_chip_line.py --event 8 --tag ${TAG}_2627 --no-llm --output reports/chip_line_gw8_interim.md >> "$LOG" 2>&1 || log "chip line FAILED"
log "GW8 INTERIM SFT DONE"

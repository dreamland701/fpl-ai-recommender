#!/usr/bin/env bash
# GW10 interim SFT side-by-side (Wes, Wed 2026-11-04 22:20 PST: "what should i change my squad for the next GW ... run the pipeline
# (classic and SFT etc)"). One GPU job at a time: waits for the H12 chain (Gemma-4-12B trainer ends ~Thu 11:15 PST, its predictions
# + scoring ~2 h later), then on CPU: Guardian + Scout pulls, the F6 live corpus/examples for the GW10 deadline, the live team-news
# categories (the Guardian GW10 lineup article lands Fri ~16:00Z, so normally absent here), the H5 team-sheet examples; then the H5
# (E4B, ~10 min, ~17 GB) read on the GPU, the side-by-side sheet (hold, plus the planned moves listed OUT:IN per line in
# logs/gw10_planned_moves if that file exists), README, the CPU chip line. Classic decides; the adapter is in shadow.
# Sentinels "GW10 INTERIM SFT DONE" / "... FAILED" in logs/gw10_interim_sft.log. Veto: kill the pid in logs/pids/gw10_interim_sft.pid.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1
LOG=logs/gw10_interim_sft.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw10_packet_2026_11; D=${PACKET_DIR:-$PACKET}; export PACKET_DIR=$D
TAG=gw10interim; DEADLINE=2026-11-06T18:30:00Z; EVENT=10
MARK='re-armed 2026-11-03 22:44'; CHAIN_PID=$(cat logs/pids/h12_chain.pid 2>/dev/null || echo 0)
chain_over(){ sed -n "/$MARK/,\$p" logs/h12_chain.log | grep -q -E "H12 CHAIN DONE|H12 FAILED" || ! kill -0 "$CHAIN_PID" 2>/dev/null; }
gpu_wait(){ while pgrep -f "^python3 .*(reghead_predict|train_gemma_reghead|extract_availability_facts)" > /dev/null; do sleep 30; done; }
log "=== GW10 interim SFT (tag $TAG): waiting for the H12 chain (pid $CHAIN_PID) to finish ==="
until chain_over; do sleep 60; done
log "H12 chain over: $(sed -n "/$MARK/,\$p" logs/h12_chain.log | grep -E 'H12 CHAIN DONE|H12 FAILED' | tail -1 || echo 'chain pid gone')"
gpu_wait
if [ "$(date +%s)" -ge "$(date -d "$DEADLINE" +%s)" ]; then log "past the GW10 deadline; nothing to do"; exit 0; fi
[ -s "$D/entry_state.json" ] || { log "GW10 INTERIM SFT FAILED: no $D/entry_state.json (run scripts/run_gw10_interim.sh first)"; exit 1; }
TODAY=$(date -u +%F)
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-10-17 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_${TAG}.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-10-17 --output reports/evidence_pl_scout_2627_${TAG}.jsonl >> "$LOG" 2>&1 || log "scout collection FAILED"
pre=reports/live_${TAG}_2627_f6
python3 scripts/build_live_gw_examples.py --stage corpus --deadline-ts $DEADLINE --training-data data/fpl_training_rows_v3_contract_f6.csv \
  --output "${pre}_corpus_bare.jsonl" >> "$LOG" 2>&1 || log "corpus FAILED"
python3 scripts/attach_player_evidence_to_corpus.py --corpus "${pre}_corpus_bare.jsonl" \
  --evidence reports/evidence_guardian_football_2627_${TAG}.jsonl --evidence reports/evidence_guardian_football_2627_gw9final.jsonl \
  --evidence reports/evidence_pl_scout_2627_${TAG}.jsonl --evidence reports/evidence_pl_scout_2627_gw9final.jsonl \
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
GN=reports/team_news_f16/gn_feat_live_gw${EVENT}_${TAG}.json
python3 scripts/live_team_news.py --event $EVENT --bootstrap "$D/snapshot/bootstrap_static.json" \
  --store reports/evidence_guardian_football_2627_${TAG}.jsonl --out "$GN" --entry-state "$D/entry_state.json" 2>&1 | tee -a "$LOG"
SPLIT=reports/live_${TAG}_2627_h5_split; mkdir -p "$SPLIT"; cp "$EX" "$SPLIT/eval.jsonl"
FACTS=reports/extract_facts/facts_by_player_week_combined.json
[ -s reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json ] && FACTS=reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json
python3 scripts/attach_team_sheet_to_split.py --split "$SPLIT" --out "${SPLIT}_sheet" --facts-json "$FACTS" --teamnews-json "$GN" \
  --table data/fpl_training_rows_v3_contract_f6.csv >> "$LOG" 2>&1 || log "team sheet attach FAILED"
HEX=${SPLIT}_sheet/eval.jsonl; ADAPTER=artifacts/gemma4_e4b_h5_teamsheet_mse; PR=reports/h_series/h5_${TAG}_pred.jsonl
gpu_wait
[ -s "$PR" ] || python3 -u scripts/reghead_predict.py "$HEX" "$ADAPTER" "$PR" 8 >> "$LOG" 2>&1 || log "h5 read FAILED"
python3 scripts/sft_side_by_side.py --examples "$HEX" --predictions "$PR" --entry-state "$D/entry_state.json" --label h5 \
  --output-md "$D/side_by_side_h5.md" >> "$LOG" 2>&1 || log "side-by-side FAILED"
if [ -s logs/gw10_planned_moves ]; then
  args=(); while read -r m; do [ -n "$m" ] && args+=(--transfer "$m"); done < logs/gw10_planned_moves
  python3 scripts/sft_side_by_side.py --examples "$HEX" --predictions "$PR" --entry-state "$D/entry_state.json" --label h5 "${args[@]}" \
    --output-md "$D/side_by_side_h5_planned.md" >> "$LOG" 2>&1 || log "side-by-side (planned moves) FAILED"
fi
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "summary FAILED"
python3 scripts/live_chip_line.py --event $EVENT --tag ${TAG}_2627 --no-llm --output reports/chip_line_gw10_interim.md >> "$LOG" 2>&1 || log "chip line FAILED"
log "GW10 INTERIM SFT DONE: $D/side_by_side_h5.md"

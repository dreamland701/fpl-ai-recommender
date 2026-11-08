#!/usr/bin/env bash
# GW9 final refresh (deadline Sat 2026-10-31 11:00 UTC = 04:00 PDT): sleeps until Saturday 09:15 UTC (02:15 PDT), i.e.
# after Friday's press conferences and the Guardian predicted-lineups article (lands Fri ~15:40 UTC), then rebuilds the
# packet into reports/gw9_packet_2026_10/final (entry, snapshot, classic+F6 forecasts, decision sheet, exact optimizer,
# lineups, role-override sheet, README), re-pulls the Guardian and Scout stores, builds the F6 live corpus + examples,
# the live team-news categories and the H5 team-sheet examples, all on CPU. The H5 (E4B) shadow read + side-by-side
# sheet need the GPU: they run only if logs/gw9_gpu_ok exists (Wes's go-ahead), else the runbook prints the command.
# Kill by pid in logs/pids/gw9_final_refresh.pid to veto.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1
LOG=logs/gw9_final_refresh.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw9_packet_2026_10; FINAL=$PACKET/final; export PACKET_DIR=$FINAL
TAG=gw9final; DEADLINE=2026-10-31T11:00:00Z; EVENT=9
TARGET=$(date -d '2026-10-31T09:15:00Z' +%s); NOW=$(date +%s)
if [ "$NOW" -lt "$TARGET" ]; then log "armed; sleeping until 2026-10-31 09:15 UTC (02:15 PDT)"; sleep $(( TARGET - NOW )); fi
if [ "$(date +%s)" -ge "$(date -d "$DEADLINE" +%s)" ]; then log "past the GW9 deadline; nothing to do"; exit 0; fi
log "=== GW9 final refresh -> $FINAL ==="; mkdir -p "$FINAL"
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$FINAL/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$FINAL/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$FINAL/milp.log" 2>&1 || log "milp FAILED"
python3 "$PACKET/route_lineups.py" > "$FINAL/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$FINAL" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$FINAL/entry_state.json" \
  --asof-week $EVENT --auto --out-md "$FINAL/role_override_sheet.md" --out-jsonl "$FINAL/forecasts_role_override.jsonl" \
  > "$FINAL/role_override.log" 2>&1 || log "role override sheet FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary FAILED"
TODAY=$(date -u +%F)
( set +u; . ~/.fpl_secrets.env; python3 scripts/collect_guardian_football_evidence.py --from-date 2026-10-10 --to-date "$TODAY" \
    --sleep 1 --output reports/evidence_guardian_football_2627_${TAG}.jsonl ) >> "$LOG" 2>&1 || log "guardian collection FAILED"
python3 scripts/backfill_pl_scout_articles.py --since 2026-10-10 --output reports/evidence_pl_scout_2627_${TAG}.jsonl >> "$LOG" 2>&1 || log "scout collection FAILED"
pre=reports/live_${TAG}_2627_f6
python3 scripts/build_live_gw_examples.py --stage corpus --deadline-ts $DEADLINE --training-data data/fpl_training_rows_v3_contract_f6.csv \
  --output "${pre}_corpus_bare.jsonl" >> "$LOG" 2>&1 || log "corpus FAILED"
python3 scripts/attach_player_evidence_to_corpus.py --corpus "${pre}_corpus_bare.jsonl" \
  --evidence reports/evidence_guardian_football_2627_${TAG}.jsonl --evidence reports/evidence_guardian_football_2627_gw8final.jsonl \
  --evidence reports/evidence_pl_scout_2627_${TAG}.jsonl --evidence reports/evidence_pl_scout_2627_gw8final.jsonl \
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
# live team-news categories (the Guardian predicted lineups for GW9) + the H5 team-sheet examples
GN=reports/team_news_f16/gn_feat_live_gw${EVENT}.json
python3 scripts/live_team_news.py --event $EVENT --bootstrap "$FINAL/snapshot/bootstrap_static.json" \
  --store reports/evidence_guardian_football_2627_${TAG}.jsonl --out "$GN" --entry-state "$FINAL/entry_state.json" 2>&1 | tee -a "$LOG"
# F16 live shadow (2026-10-28): classic+F6+F16 on the team-news table with this week's Guardian categories (parity-checked on GW7);
# the production forecast still decides, final/f16_shadow.md shows what the lineup article would change
FPL_TEAM_NEWS_FEATS=1 FPL_TEAM_NEWS_LIVE_JSON=$GN python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6_teamnews.csv "$FINAL/forecasts_f16_shadow.jsonl" >> "$LOG" 2>&1 || log "F16 shadow forecast FAILED"
python3 scripts/f16_shadow_diff.py --packet-dir "$FINAL" --categories "$GN" --event $EVENT --out "$FINAL/f16_shadow.md" >> "$LOG" 2>&1 || log "F16 shadow diff FAILED"
SPLIT=reports/live_${TAG}_2627_h5_split; mkdir -p "$SPLIT"; cp "$EX" "$SPLIT/eval.jsonl"
FACTS=reports/extract_facts/facts_by_player_week_combined.json
[ -s reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json ] && FACTS=reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json
python3 scripts/attach_team_sheet_to_split.py --split "$SPLIT" --out "${SPLIT}_sheet" --facts-json "$FACTS" --teamnews-json "$GN" \
  --table data/fpl_training_rows_v3_contract_f6.csv >> "$LOG" 2>&1 || log "team sheet attach FAILED"
# shadow adapter: logs/gw9_shadow_adapter names it (H6 numeric-block arm once its chain verdict is in), else H5; an h6 adapter
# needs the numeric-history block in the prompt (2026-10-28, scripts/attach_numeric_history_to_split.py)
ADAPTER=$(cat logs/gw9_shadow_adapter 2>/dev/null || echo artifacts/gemma4_e4b_h5_teamsheet_mse); ALABEL=$(basename "$ADAPTER" | sed 's/gemma4_e4b_//; s/_.*//')
HEX=${SPLIT}_sheet/eval.jsonl
case "$ADAPTER" in *h6*)
  python3 scripts/attach_numeric_history_to_split.py --split "${SPLIT}_sheet" --out "${SPLIT}_sheet_num" --table data/fpl_training_rows_v3_contract_f6.csv \
    --prior-table data/fpl_training_rows_v3_contract_f6_prior.csv >> "$LOG" 2>&1 && HEX=${SPLIT}_sheet_num/eval.jsonl || log "numeric block FAILED (reading the team-sheet prompt instead)" ;;
esac
PR=reports/h_series/${ALABEL}_${TAG}_pred.jsonl
if [ -e logs/gw9_gpu_ok ]; then
  while pgrep -f "^python3 .*(reghead_predict|train_gemma_reghead|extract_availability_facts)" > /dev/null; do sleep 30; done
  [ -s "$PR" ] || python3 -u scripts/reghead_predict.py "$HEX" "$ADAPTER" "$PR" 8 >> "$LOG" 2>&1 || log "$ALABEL read FAILED"
  python3 scripts/sft_side_by_side.py --examples "$HEX" --predictions "$PR" --entry-state "$FINAL/entry_state.json" --label "$ALABEL" \
    --output-md "$FINAL/side_by_side_${ALABEL}.md" >> "$LOG" 2>&1 || log "side-by-side FAILED"
  python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary (2) FAILED"
else
  log "GPU step skipped (no logs/gw9_gpu_ok): $ALABEL read -> python3 scripts/reghead_predict.py $HEX $ADAPTER $PR 8; then scripts/sft_side_by_side.py --examples $HEX --predictions $PR --entry-state $FINAL/entry_state.json --label $ALABEL --output-md $FINAL/side_by_side_${ALABEL}.md"
fi
python3 scripts/live_chip_line.py --event $EVENT --tag ${TAG}_2627 --no-llm --output reports/chip_line_gw9.md >> "$LOG" 2>&1 || log "chip line FAILED"
log "GW9 FINAL REFRESH DONE: $FINAL/README.md"

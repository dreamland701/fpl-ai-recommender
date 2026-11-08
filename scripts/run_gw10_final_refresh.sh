#!/usr/bin/env bash
# GW10 final refresh (deadline Fri 2026-11-06 18:30 UTC = 10:30 PST; first kickoff EVE v COV 20:00Z): sleeps until Friday 16:35 UTC
# (08:35 PST), i.e. after Friday's press conferences and the Guardian predicted-lineups article (GW8 15:42Z, GW9 16:19Z), then
# rebuilds the packet into reports/gw10_packet_2026_11/final (entry, snapshot, the hand-edit replay of confirmed moves the API hides
# until the deadline from logs/gw10_hand_edit, classic+F6 forecasts, decision sheet, exact optimizer, lineups, role-override sheet,
# README), re-pulls the Guardian and Scout stores, builds the F6 live corpus + examples, the live team-news categories, the F16 shadow
# (needs data/fpl_training_rows_v3_contract_f6_teamnews.csv rebuilt on the GW9-ingested table, done Wed/Thu), the H5 team-sheet
# examples; the shadow adapter read (E4B H5 by default; logs/gw10_shadow_adapter may name an h6/h12 adapter, which gets the
# numeric-history block and, for 12b, the fpl-gemma-12b venv) + side-by-side sheets run only if logs/gw10_gpu_ok exists and after
# any trainer/predict process has exited (one GPU job at a time). Chip line last. Kill by pid in logs/pids/gw10_final_refresh.pid.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH=src FPL_PLANNER_DISCIPLINE=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1
export PYTHONDONTWRITEBYTECODE=1 HF_HUB_OFFLINE=1 HF_HUB_DISABLE_XET=1
LOG=logs/gw10_final_refresh.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
PACKET=$ROOT/reports/gw10_packet_2026_11; FINAL=$PACKET/final; export PACKET_DIR=$FINAL
TAG=gw10final; DEADLINE=2026-11-06T18:30:00Z; EVENT=10; VENV12=/home/wescheng/venvs/fpl-gemma-12b
gpu_wait(){ while pgrep -f "^python3 .*(reghead_predict|train_gemma_reghead|extract_availability_facts)" > /dev/null; do sleep 30; done; }
TARGET=$(date -d '2026-11-06T16:35:00Z' +%s); NOW=$(date +%s)
if [ "$NOW" -lt "$TARGET" ]; then log "armed; sleeping until 2026-11-06 16:35 UTC (08:35 PST)"; sleep $(( TARGET - NOW )); fi
if [ "$(date +%s)" -ge "$(date -d "$DEADLINE" +%s)" ]; then log "past the GW10 deadline; nothing to do"; exit 0; fi
log "=== GW10 final refresh -> $FINAL ==="; mkdir -p "$FINAL"
python3 "$PACKET/fetch_entry.py" >> "$LOG" 2>&1 || log "entry fetch FAILED"
python3 "$PACKET/snapshot.py" >> "$LOG" 2>&1 || log "snapshot FAILED"
python3 "$PACKET/entry_state.py" >> "$LOG" 2>&1 || log "entry state FAILED"
python3 scripts/apply_hand_edit.py --entry-state "$FINAL/entry_state.json" --bootstrap "$FINAL/snapshot/bootstrap_static.json" \
  --moves logs/gw10_hand_edit --note "confirmed by Wes; the public API hides current-GW transfers until the deadline" 2>&1 | tee -a "$LOG"
python3 "$PACKET/forecast.py" new data/fpl_training_rows_v3_contract_f6.csv "$FINAL/forecasts_new_pipeline.jsonl" >> "$LOG" 2>&1 || log "forecast FAILED"
python3 "$PACKET/decide.py" > "$FINAL/decide.log" 2>&1 || log "decision sheet FAILED"
python3 "$PACKET/milp_routes.py" > "$FINAL/milp.log" 2>&1 || log "milp FAILED"
python3 "$PACKET/route_lineups.py" > "$FINAL/route_lineups.log" 2>&1 || log "route lineups FAILED"
python3 scripts/role_override_sheet.py --packet-dir "$FINAL" --table data/fpl_training_rows_v3_contract_f6.csv --entry-state "$FINAL/entry_state.json" \
  --asof-week $EVENT --auto --out-md "$FINAL/role_override_sheet.md" --out-jsonl "$FINAL/forecasts_role_override.jsonl" \
  > "$FINAL/role_override.log" 2>&1 || log "role override sheet FAILED"
python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary FAILED"
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
# live team-news categories (the Guardian predicted lineups for GW10, from both GW10 pulls) + the F16 shadow
GN=reports/team_news_f16/gn_feat_live_gw${EVENT}.json
python3 scripts/live_team_news.py --event $EVENT --bootstrap "$FINAL/snapshot/bootstrap_static.json" \
  --store reports/evidence_guardian_football_2627_${TAG}.jsonl --store reports/evidence_guardian_football_2627_gw10interim.jsonl \
  --out "$GN" --entry-state "$FINAL/entry_state.json" 2>&1 | tee -a "$LOG"
TN=data/fpl_training_rows_v3_contract_f6_teamnews.csv
if [ "$TN" -nt data/fpl_training_rows_v3_contract_f6.csv ]; then
  FPL_TEAM_NEWS_FEATS=1 FPL_TEAM_NEWS_LIVE_JSON=$GN python3 "$PACKET/forecast.py" new "$TN" "$FINAL/forecasts_f16_shadow.jsonl" >> "$LOG" 2>&1 || log "F16 shadow forecast FAILED"
  python3 scripts/f16_shadow_diff.py --packet-dir "$FINAL" --categories "$GN" --event $EVENT --out "$FINAL/f16_shadow.md" >> "$LOG" 2>&1 || log "F16 shadow diff FAILED"
else
  log "F16 shadow skipped: $TN is older than the production table (rebuild with scripts/build_team_news_table.py)"
fi
SPLIT=reports/live_${TAG}_2627_h5_split; mkdir -p "$SPLIT"; cp "$EX" "$SPLIT/eval.jsonl"
FACTS=reports/extract_facts/facts_by_player_week_combined.json
[ -s reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json ] && FACTS=reports/extract_facts/facts_by_player_week_live_gw${EVENT}.json
python3 scripts/attach_team_sheet_to_split.py --split "$SPLIT" --out "${SPLIT}_sheet" --facts-json "$FACTS" --teamnews-json "$GN" \
  --table data/fpl_training_rows_v3_contract_f6.csv >> "$LOG" 2>&1 || log "team sheet attach FAILED"
ADAPTER=$(cat logs/gw10_shadow_adapter 2>/dev/null || echo artifacts/gemma4_e4b_h5_teamsheet_mse)
ALABEL=$(basename "$ADAPTER" | sed 's/gemma4_e4b_//; s/gemma4_12b_//; s/_.*//')
HEX=${SPLIT}_sheet/eval.jsonl
case "$ADAPTER" in *h6*|*h12*|*12b*)
  python3 scripts/attach_numeric_history_to_split.py --split "${SPLIT}_sheet" --out "${SPLIT}_sheet_num" --table data/fpl_training_rows_v3_contract_f6.csv \
    --prior-table data/fpl_training_rows_v3_contract_f6_prior.csv >> "$LOG" 2>&1 && HEX=${SPLIT}_sheet_num/eval.jsonl || log "numeric block FAILED (reading the team-sheet prompt instead)" ;;
esac
predict(){ case "$ADAPTER" in *12b*) ( source "$VENV12/bin/activate"; exec python3 -u scripts/reghead_predict.py "$@" );; *) python3 -u scripts/reghead_predict.py "$@";; esac; }
PR=reports/h_series/${ALABEL}_${TAG}_pred.jsonl
if [ -e logs/gw10_gpu_ok ]; then
  gpu_wait
  [ -s "$PR" ] || predict "$HEX" "$ADAPTER" "$PR" 8 >> "$LOG" 2>&1 || log "$ALABEL read FAILED"
  python3 scripts/sft_side_by_side.py --examples "$HEX" --predictions "$PR" --entry-state "$FINAL/entry_state.json" --label "$ALABEL" \
    --output-md "$FINAL/side_by_side_${ALABEL}.md" >> "$LOG" 2>&1 || log "side-by-side FAILED"
  if [ -s logs/gw10_planned_moves ]; then
    args=(); while read -r m; do [ -n "$m" ] && args+=(--transfer "$m"); done < logs/gw10_planned_moves
    python3 scripts/sft_side_by_side.py --examples "$HEX" --predictions "$PR" --entry-state "$FINAL/entry_state.json" --label "$ALABEL" "${args[@]}" \
      --output-md "$FINAL/side_by_side_${ALABEL}_planned.md" >> "$LOG" 2>&1 || log "side-by-side (planned moves) FAILED"
  fi
  python3 "$PACKET/final_summary.py" >> "$LOG" 2>&1 || log "final summary (2) FAILED"
else
  log "GPU step skipped (no logs/gw10_gpu_ok): $ALABEL read -> scripts/reghead_predict.py $HEX $ADAPTER $PR 8; then scripts/sft_side_by_side.py --examples $HEX --predictions $PR --entry-state $FINAL/entry_state.json --label $ALABEL --output-md $FINAL/side_by_side_${ALABEL}.md"
fi
python3 scripts/live_chip_line.py --event $EVENT --tag ${TAG}_2627 --no-llm --output reports/chip_line_gw10.md >> "$LOG" 2>&1 || log "chip line FAILED"
log "GW10 FINAL REFRESH DONE: $FINAL/README.md"

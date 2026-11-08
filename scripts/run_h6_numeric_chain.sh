#!/usr/bin/env bash
# H6 (2026-10-28, Wes: "start the next round of SFT or RL"): the H5 recipe (E4B regression head, MSE, team sheet + role
# facts, top-96 E22 prompts) with ONE change: a numeric-history block in every prompt (week-by-week minutes/points with the
# status flag, season totals, last-5 xG/xA, prior-season start share; scripts/attach_numeric_history_to_split.py).
# Diagnosis behind it (reports/gw9_packet_2026_10/returner_pattern_calibration.md + band check): the classic under-
# forecasts returners by 18 min / +0.37 pts and every player it puts at 45-72 min by ~9 min / +0.36 pts; the H prompts
# carried none of the numbers needed to see that, and H1/H5 deltas are flat across minutes bands. Same train/eval rows as
# H5 (train through 2025-26 GW26; eval 2025-26 GW27-38 + live 2026-27 GW2-6) so H6 - H5 isolates the block; plus a new
# live window 2026-27 GW7-8 (corpus rebuilt here) scored for classic, H5 and H6. Then H6b = same block, 2 epochs,
# head LR 2e-3, LoRA LR 1e-4 ("fit harder"), skipped if it could not finish before the Saturday GW9 refresh.
# GPU: one job at a time (waits on reghead_predict/train_gemma_reghead/extract_availability_facts), peak ~17 GB (H5).
# Log logs/h6_chain.log; sentinels "H6 CHAIN DONE" / "H6 FAILED". Env: FPL_H6_SKIP_B=1 skips H6b.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h6_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H6 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1 FPL_DEPTH_CHART=0
export FPL_EVIDENCE_DROP='price (rise|fall|change)s?|risers|fallers|most.?bought|most.?sold|transfers in|transfer (window|news|rumou?rs?|gossip|deadline|verdict|latest)|deadline day'
export FPL_EVIDENCE_PRIORITY='team news|predicted line'
TABLE=data/fpl_training_rows_v3_contract_f6.csv; PRIOR=data/fpl_training_rows_v3_contract_f6_prior.csv
TSPLIT=reports/llm_residual_v2_e22_top96_ts2_thru_2526_26_eval_2526_27_38; TLSPLIT=reports/llm_residual_v2_e22_top96_ts2_eval_2627_2_6
NSPLIT=reports/llm_residual_v2_e22_top96_ts2n_thru_2526_26_eval_2526_27_38; NLSPLIT=reports/llm_residual_v2_e22_top96_ts2n_eval_2627_2_6
EX=reports/extract_facts; FACTS=$EX/facts_by_player_week_combined.json; GN=reports/team_news_f16/gn_feat.json
H5=artifacts/gemma4_e4b_h5_teamsheet_mse; OUT=reports/h_series; mkdir -p "$OUT"
SPLIT_FLAGS=(--include-fixtures --include-congestion --include-provenance --include-defcon --compact-context
             --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 --top-n 96)
gpu_wait(){ while pgrep -f "reghead_predict.py|train_gemma_reghead.py|extract_availability_facts.py" > /dev/null; do sleep 30; done; }
watchdog(){ local pid=$1 used
  while kill -0 "$pid" 2>/dev/null; do
    used=$(free -g | awk '/Mem:/{print $3}')
    if [ "${used:-0}" -gt 100 ]; then log "WATCHDOG: used ${used} GB > 100, killing $pid"; kill "$pid"; fi
    sleep 10
  done; }
bt(){ local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }

log "=== H6: numeric-history block on the H5 splits ==="
[ -s "$TSPLIT/train.jsonl" ] && [ -s "$TSPLIT/eval.jsonl" ] && [ -s "$TLSPLIT/eval.jsonl" ] || die "H5 splits missing"
[ -s "$NSPLIT/train.jsonl" ] || python3 scripts/attach_numeric_history_to_split.py --split "$TSPLIT" --out "$NSPLIT" --table "$TABLE" --prior-table "$PRIOR" >> "$LOG" 2>&1 || die "numeric block (holdout split)"
[ -s "$NLSPLIT/eval.jsonl" ] || python3 scripts/attach_numeric_history_to_split.py --split "$TLSPLIT" --out "$NLSPLIT" --table "$TABLE" --prior-table "$PRIOR" >> "$LOG" 2>&1 || die "numeric block (live split)"
log "splits: $(wc -l < $NSPLIT/train.jsonl) train / $(wc -l < $NSPLIT/eval.jsonl) holdout / $(wc -l < $NLSPLIT/eval.jsonl) live rows; blocks in train: $(grep -c 'Numeric history' $NSPLIT/train.jsonl)"

log "=== live window 2026-27 GW7-8: corpus rebuild (E22 recipe, stores through gw8final) ==="
LBASE=reports/llm_player_forecast_2627_e22b_base.jsonl; LFULL=reports/llm_player_forecast_2627_e22b_full.jsonl
L78=reports/llm_residual_v2_e22b_top96_eval_2627_7_8; TS78=${L78}_ts2; N78=${L78}_ts2n
if [ ! -s "$N78/eval.jsonl" ]; then
  ( python3 -m fpl_ai.cli export-llm-player-forecast-corpus --training-data "$TABLE" --output "$LBASE" --seasons 2026-27 --prompt-style baseline_adjustment \
    && EV=(); for f in reports/evidence_guardian_football_2627_gw{2,3,4,5,6,6final,7,7final,8interim,8final}.jsonl reports/evidence_pl_scout_2627_gw{2,3,4,5,6,6final,7,7final,8interim,8final}.jsonl; do [ -s "$f" ] && EV+=(--evidence "$f"); done \
    && python3 scripts/attach_player_evidence_to_corpus.py --corpus "$LBASE" "${EV[@]}" --include-non-curated --cutoff-hours 12 --output reports/_e22b_live_ev.jsonl \
    && python3 scripts/attach_fixture_outlook_to_corpus.py --corpus reports/_e22b_live_ev.jsonl --history-dir data/fpl_history --output reports/_e22b_live_fx.jsonl \
    && python3 scripts/attach_congestion_to_corpus.py --corpus reports/_e22b_live_fx.jsonl --euro-fixtures data/competition_fixtures/european_fixtures.jsonl --history-dir data/fpl_history --output reports/_e22b_live_cg.jsonl \
    && python3 scripts/attach_defcon_to_corpus.py --corpus reports/_e22b_live_cg.jsonl --training-data "$TABLE" --output "$LFULL" \
    && python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$LFULL" --output-dir "$L78" "${SPLIT_FLAGS[@]}" --train-through 2026-27:6 --eval-weeks 2026-27:7-8 \
    && python3 scripts/attach_team_sheet_to_split.py --split "$L78" --out "$TS78" --facts-json "$FACTS" --teamnews-json "$GN" --table "$TABLE" \
    && python3 scripts/attach_numeric_history_to_split.py --split "$TS78" --out "$N78" --table "$TABLE" --prior-table "$PRIOR" ) >> "$LOG" 2>&1 \
    || log "GW7-8 live window build FAILED (non-fatal; the window is skipped)"
fi
[ -s "$N78/eval.jsonl" ] && log "GW7-8 live window: $(wc -l < $N78/eval.jsonl) eval rows ($(python3 -c "import json;print(sorted({json.loads(l)['week'] for l in open('$N78/eval.jsonl')}))"))"

train_and_score(){ local tag=$1 adapter=$2 epochs=$3 lr=$4 hlr=$5
  gpu_wait
  log "=== $tag training (E4B, H5 recipe + numeric block, mse, epochs $epochs, lr $lr, head lr $hlr, batch 1 x 16, ckpt on) ==="
  if [ ! -s "$adapter/head.pt" ]; then
    FPL_RH_DATA_DIR=$NSPLIT FPL_RH_OUTPUT_DIR=$adapter FPL_RH_LORA_MODE=modules FPL_RH_BATCH=1 FPL_RH_ACCUM=16 FPL_RH_CKPT=1 FPL_RH_LOSS=mse \
    FPL_RH_LR=$lr FPL_RH_HEAD_LR=$hlr FPL_RH_EPOCHS=$epochs FPL_RH_SAVE_STEPS=100 FPL_RH_COMPACT=1 FPL_RH_MAX_ROWS=0 \
      python3 -u train_gemma_reghead.py >> logs/train_${tag}.log 2>&1 &
    P=$!; watchdog "$P"; wait "$P" || log "trainer exited non-zero"
  fi
  [ -s "$adapter/head.pt" ] && [ -s "$adapter/adapter_model.safetensors" ] || die "$tag training (no adapter/head)"
  log "=== $tag predictions ==="
  gpu_wait; [ -s "$OUT/${tag}_holdout_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$NSPLIT/eval.jsonl" "$adapter" "$OUT/${tag}_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "$tag holdout predict"
  gpu_wait; [ -s "$OUT/${tag}_live_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$NLSPLIT/eval.jsonl" "$adapter" "$OUT/${tag}_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "$tag live predict"
  if [ -s "$N78/eval.jsonl" ]; then
    gpu_wait; [ -s "$OUT/${tag}_live78_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$N78/eval.jsonl" "$adapter" "$OUT/${tag}_live78_pred.jsonl" 8 >> "$LOG" 2>&1 || log "$tag live78 predict FAILED"
  fi
  log "=== $tag ledgers + mechanism checks (vs H5) ==="
  python3 scripts/track_sft_accuracy.py --set "$tag holdout 2025-26 GW27-38 (numeric block)" "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" "$OUT/${tag}_holdout_pred.jsonl" \
    --set "$tag live 2026-27 GW2-6" "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" "$OUT/${tag}_live_pred.jsonl" --out-md "$OUT/${tag}_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
  python3 scripts/team_sheet_mechanism_check.py --examples "$NSPLIT/eval.jsonl" --base h5=$OUT/h5_holdout_pred.jsonl --test $tag=$OUT/${tag}_holdout_pred.jsonl --out "$OUT/${tag}_mechanism_holdout.md" >> "$LOG" 2>&1 || log "mechanism check (holdout) FAILED"
  python3 scripts/team_sheet_mechanism_check.py --examples "$NLSPLIT/eval.jsonl" --base h5=$OUT/h5_live_pred.jsonl --test $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_mechanism_live.md" >> "$LOG" 2>&1 || log "mechanism check (live) FAILED"
  python3 scripts/band_delta_check.py --examples "$NSPLIT/eval.jsonl" --examples "$NLSPLIT/eval.jsonl" --pred h5=$OUT/h5_holdout_pred.jsonl --pred h5=$OUT/h5_live_pred.jsonl \
    --pred $tag=$OUT/${tag}_holdout_pred.jsonl --pred $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_band_check.md" >> "$LOG" 2>&1 || log "band check FAILED"
  log "=== $tag decision backtests ==="
  for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_$tag/$1_$2_$3" $1 $2 $3 "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" & done
  bt "$OUT/bt_$tag/2026-27_2_6" 2026-27 2 6 "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" &
  wait
  if [ -s "$OUT/${tag}_live78_pred.jsonl" ]; then
    bt "$OUT/bt_classic/2026-27_7_8" 2026-27 7 8 &
    [ -s "$OUT/h5_live78_pred.jsonl" ] && bt "$OUT/bt_h5/2026-27_7_8" 2026-27 7 8 "$TS78/eval.jsonl" "$OUT/h5_live78_pred.jsonl" &
    bt "$OUT/bt_$tag/2026-27_7_8" 2026-27 7 8 "$N78/eval.jsonl" "$OUT/${tag}_live78_pred.jsonl" &
    wait
  fi
  python3 scripts/xpts_rescore.py --label ${tag}_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h5 --test "reports/h_series/bt_$tag" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
  log "RESULT $tag: $(TAG=$tag python3 - <<'PY'
import json, os
tag = os.environ["TAG"]
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(t):
    w = [tot(f"reports/h_series/{t}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{t}/2026-27_2_6/rolling_squad_backtest.json"), tot(f"reports/h_series/{t}/2026-27_7_8/rolling_squad_backtest.json")
c, h5, h = s("bt_classic"), s("bt_h5"), s(f"bt_{tag}")
print(f"squad points holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H5 {h5[1]} ({h[1] - h5[1]:+.0f}); live GW2-6 {h[2]} vs classic {c[2]} vs H5 {h5[2]}; live GW7-8 {h[3]} vs classic {c[3]} vs H5 {h5[3]}")
PY
)"
}

# H5 read on the new GW7-8 window (team-sheet prompt, no numeric block) for the three-way comparison
if [ -s "$TS78/eval.jsonl" ] && [ ! -s "$OUT/h5_live78_pred.jsonl" ]; then
  gpu_wait; python3 -u scripts/reghead_predict.py "$TS78/eval.jsonl" "$H5" "$OUT/h5_live78_pred.jsonl" 8 >> "$LOG" 2>&1 || log "H5 live78 predict FAILED"
fi
train_and_score h6 artifacts/gemma4_e4b_h6_numeric_mse 1 5e-5 5e-4
# H6b only if it can land before the Saturday GW9 refresh GPU step (Sat 2026-10-31 09:15 UTC), ~26 h at H5's pace
if [ "${FPL_H6_SKIP_B:-0}" != "1" ] && [ $(( $(date -d '2026-10-31T08:00:00Z' +%s) - $(date +%s) )) -gt $(( 27 * 3600 )) ]; then
  train_and_score h6b artifacts/gemma4_e4b_h6b_numeric_mse_e2 2 1e-4 2e-3
else
  log "H6b skipped (not enough time before the Saturday refresh, or FPL_H6_SKIP_B=1); run later: train_and_score h6b ..."
fi
log "H6 CHAIN DONE"

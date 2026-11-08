#!/usr/bin/env bash
# H6b scoring (written 2026-11-03 21:50 PST). scripts/run_h6b_after_gw9.sh died on `N78: unbound variable` (set -u)
# at 2026-11-01 07:16 PST, after the GPU work had finished (training 29.2 h, holdout 1,152 + live 480 predictions).
# This re-runs the scoring half of its train_and_score with N78/TS78 defined as in run_h6_numeric_chain.sh:
# live GW7-8 read (GPU, 192 rows, ~3 min), accuracy ledger, mechanism checks vs H5, band check, five decision
# backtests (three at a time), xPts rescore (label h6b_arms, arms H5/H6/H6b vs classic), RESULT line.
# Log logs/h6b_score.log; sentinels "H6B SCORE DONE" / "H6B SCORE FAILED".
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h6b_score.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H6B SCORE FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1 FPL_DEPTH_CHART=0
TABLE=data/fpl_training_rows_v3_contract_f6.csv
NSPLIT=reports/llm_residual_v2_e22_top96_ts2n_thru_2526_26_eval_2526_27_38; NLSPLIT=reports/llm_residual_v2_e22_top96_ts2n_eval_2627_2_6
L78=reports/llm_residual_v2_e22b_top96_eval_2627_7_8; TS78=${L78}_ts2; N78=${L78}_ts2n
ADAPTER=artifacts/gemma4_e4b_h6b_numeric_mse_e2; OUT=reports/h_series; tag=h6b
gpu_wait(){ while pgrep -f "^python3 .*(reghead_predict|train_gemma_reghead|extract_availability_facts)" > /dev/null; do sleep 30; done; }
bt(){ local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  [ -s "$dir/rolling_squad_backtest.json" ] && return 0
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }

log "=== H6b scoring (re-run of the scoring half of run_h6b_after_gw9.sh) ==="
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "adapter missing"
[ "$(wc -l < "$OUT/${tag}_holdout_pred.jsonl")" = 1152 ] || die "holdout predictions incomplete"
[ "$(wc -l < "$OUT/${tag}_live_pred.jsonl")" = 480 ] || die "live predictions incomplete"
[ -s "$N78/eval.jsonl" ] || die "N78 split missing"
log "=== $tag live GW7-8 predictions (192 rows) ==="
gpu_wait; [ -s "$OUT/${tag}_live78_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$N78/eval.jsonl" "$ADAPTER" "$OUT/${tag}_live78_pred.jsonl" 8 >> "$LOG" 2>&1 || log "$tag live78 predict FAILED"
log "=== $tag ledgers + mechanism checks (vs H5) ==="
python3 scripts/track_sft_accuracy.py --set "$tag holdout 2025-26 GW27-38 (numeric block)" "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" "$OUT/${tag}_holdout_pred.jsonl" \
  --set "$tag live 2026-27 GW2-6" "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" "$OUT/${tag}_live_pred.jsonl" --out-md "$OUT/${tag}_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$NSPLIT/eval.jsonl" --base h5=$OUT/h5_holdout_pred.jsonl --test $tag=$OUT/${tag}_holdout_pred.jsonl --out "$OUT/${tag}_mechanism_holdout.md" >> "$LOG" 2>&1 || log "mechanism check (holdout) FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$NLSPLIT/eval.jsonl" --base h5=$OUT/h5_live_pred.jsonl --test $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_mechanism_live.md" >> "$LOG" 2>&1 || log "mechanism check (live) FAILED"
python3 scripts/band_delta_check.py --examples "$NSPLIT/eval.jsonl" --examples "$NLSPLIT/eval.jsonl" --pred h5=$OUT/h5_holdout_pred.jsonl --pred h5=$OUT/h5_live_pred.jsonl \
  --pred $tag=$OUT/${tag}_holdout_pred.jsonl --pred $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_band_check.md" >> "$LOG" 2>&1 || log "band check FAILED"
log "=== $tag decision backtests (3 at a time) ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_$tag/$1_$2_$3" $1 $2 $3 "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" & done
wait
bt "$OUT/bt_$tag/2026-27_2_6" 2026-27 2 6 "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" &
[ -s "$OUT/${tag}_live78_pred.jsonl" ] && bt "$OUT/bt_$tag/2026-27_7_8" 2026-27 7 8 "$N78/eval.jsonl" "$OUT/${tag}_live78_pred.jsonl" &
wait
python3 scripts/xpts_rescore.py --label ${tag}_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h5 --test reports/h_series/bt_h6 --test "reports/h_series/bt_$tag" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
log "RESULT $tag: $(TAG=$tag python3 - <<'PY'
import json, os
tag = os.environ["TAG"]
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(t):
    w = [tot(f"reports/h_series/{t}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{t}/2026-27_2_6/rolling_squad_backtest.json"), tot(f"reports/h_series/{t}/2026-27_7_8/rolling_squad_backtest.json")
c, h5, h6, h = s("bt_classic"), s("bt_h5"), s("bt_h6"), s(f"bt_{tag}")
print(f"squad points holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H5 {h5[1]} ({h[1] - h5[1]:+.0f}) vs H6 {h6[1]}; live GW2-6 {h[2]} vs classic {c[2]} vs H5 {h5[2]} vs H6 {h6[2]}; live GW7-8 {h[3]} vs classic {c[3]} vs H5 {h5[3]} vs H6 {h6[3]}")
PY
)"
log "H6B SCORE DONE"

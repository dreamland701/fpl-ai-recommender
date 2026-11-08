#!/usr/bin/env bash
# H6b follow-on (2026-10-29 08:40 PDT, Wes: "keep going on the AI training front"): the H6 chain idled 10 h on an
# unanchored GPU guard, so its own clock gate will skip H6b. This script waits for the H6 chain process to exit, then runs
# H6b (same numeric block, 2 epochs, head LR 2e-3, LoRA LR 1e-4) with the chain's own train_and_score, unless the chain
# already trained it, or it is past 2026-10-30T06:30Z (23:30 PDT Thu): H6b takes ~25.7 h and must clear the Saturday GW9
# refresh GPU read (Sat 09:15 UTC); otherwise it is deferred to after that read. Guards anchored on ^python3.
# Log logs/h6b_followon.log; sentinels "H6B CHAIN DONE" / "H6B FAILED" / "H6B DEFERRED". Kill by logs/pids/h6b_followon.pid.
H6_CHAIN_PID=283125
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h6b_followon.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H6B FAILED: $*"; exit 1; }
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
gpu_wait(){ while pgrep -f "^python3 .*(reghead_predict|train_gemma_reghead|extract_availability_facts)" > /dev/null; do sleep 30; done; }
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

log "=== H6b follow-on armed; waiting for the H6 chain (pid $H6_CHAIN_PID) to exit ==="
while kill -0 "$H6_CHAIN_PID" 2>/dev/null; do sleep 60; done
log "H6 chain exited; last chain line: $(tail -n 1 logs/h6_chain.log | cut -c1-160)"
if grep -q "h6b training" logs/h6_chain.log || [ -s artifacts/gemma4_e4b_h6b_numeric_mse_e2/head.pt ]; then
  log "H6b already trained by the chain; H6B CHAIN DONE (nothing to do)"; exit 0
fi
grep -q "RESULT h6:" logs/h6_chain.log || log "WARNING: no 'RESULT h6' line in the chain log (H6 may have failed); H6b still runs on the same splits"
[ -s "$NSPLIT/train.jsonl" ] && [ -s "$NSPLIT/eval.jsonl" ] && [ -s "$NLSPLIT/eval.jsonl" ] || die "numeric splits missing"
if [ "$(date +%s)" -gt "$(date -d '2026-10-30T06:30:00Z' +%s)" ]; then
  log "H6B DEFERRED: past 2026-10-30T06:30Z, H6b (~26 h) could not clear the Saturday GW9 read; queue it after Sat 09:15 UTC"; exit 0
fi
train_and_score h6b artifacts/gemma4_e4b_h6b_numeric_mse_e2 2 1e-4 2e-3
log "H6B CHAIN DONE"

#!/usr/bin/env bash
# H12 = Gemma-4-12B-it (bf16 LoRA) on the H6 recipe. Written 2026-11-03 22:15 PST on Wes's "scale things further with
# latest AI/LLM approach" + "run something leveraging my free GPU" under the standing training go-ahead
# (memory fpl-training-go-ahead-2026-10-31). Why this run: the only capacity test so far (H31, 31B nf4, 10-21) used the H1
# Huber recipe whose constant-shrink defect H5's MSE loss later removed, so capacity has never been tested on the fixed
# loss; 12B is the largest dense Gemma 4 that trains in bf16 under the 55 GB one-job rule and shares the January-2025
# cutoff (holdout clean). Everything else = H6 (team sheet + role facts + numeric block, mse, 1 epoch, LoRA LR 5e-5,
# head LR 5e-4, batch 1 x 16, ckpt; ts2n splits; same ledgers, mechanism/band checks, five decision windows, xPts).
# Order: wait for the 12B weights (background download) -> smoke test (48 rows = 3 steps; abort if peak > 50 GB)
# -> training -> predictions (holdout 1,152 / live 480 / live78 192) -> scoring -> RESULT line.
# Guards anchored ^python3. Log logs/h12_chain.log, trainer logs/train_h12.log, sentinels "H12 CHAIN DONE" / "H12 FAILED".
# Veto: kill the pid in logs/pids/h12_chain.pid (and the trainer pid from `pgrep -f "^python3 -u train_gemma_reghead"`).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h12_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H12 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1 FPL_DEPTH_CHART=0
MODEL=google/gemma-4-12B-it; HFDIR=$HOME/.cache/huggingface/hub/models--google--gemma-4-12B-it
# 22:50 PST: the 12B is the Gemma 4 *Unified* checkpoint (model_type gemma4_unified, saved with transformers 5.10); the production
# venv's transformers 5.6.0.dev0 cannot load it, so the two GPU steps run in /home/wescheng/venvs/fpl-gemma-12b (transformers 5.22.1,
# peft 0.21.2, same ~/.local torch 2.9.1+cu128). Activated inside a subshell that execs python3, so the process name stays `python3`
# for every anchored gpu_wait guard and the watchdog pid is the trainer itself.
VENV12=/home/wescheng/venvs/fpl-gemma-12b
TABLE=data/fpl_training_rows_v3_contract_f6_asof_gw8.csv   # frozen pre-GW9-ingest copy: bt_classic/bt_h5/bt_h6/bt_h6b were built on it
NSPLIT=reports/llm_residual_v2_e22_top96_ts2n_thru_2526_26_eval_2526_27_38; NLSPLIT=reports/llm_residual_v2_e22_top96_ts2n_eval_2627_2_6
L78=reports/llm_residual_v2_e22b_top96_eval_2627_7_8; N78=${L78}_ts2n
OUT=reports/h_series; tag=h12; ADAPTER=artifacts/gemma4_12b_h12_numeric_mse; SMOKE=artifacts/gemma4_12b_h12_smoke
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
train(){ local outdir=$1 maxrows=$2 logfile=$3
  ( source "$VENV12/bin/activate"
    export FPL_RH_MODEL=$MODEL FPL_RH_DATA_DIR=$NSPLIT FPL_RH_OUTPUT_DIR=$outdir FPL_RH_LORA_MODE=modules FPL_RH_BATCH=1 FPL_RH_ACCUM=16 FPL_RH_CKPT=1
    export FPL_RH_LOSS=mse FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=100 FPL_RH_COMPACT=1 FPL_RH_MAX_ROWS=$maxrows HF_HUB_OFFLINE=1
    exec python3 -u train_gemma_reghead.py ) >> "$logfile" 2>&1 &
  local P=$!; watchdog "$P"; wait "$P" || log "trainer ($outdir) exited non-zero"; }
predict(){ ( source "$VENV12/bin/activate"; export HF_HUB_OFFLINE=1; exec python3 -u scripts/reghead_predict.py "$@" ) >> "$LOG" 2>&1; }

log "=== H12 chain armed: waiting for the Gemma-4-12B-it weights (background download, logs/download_gemma4_12b.log) ==="
for _ in $(seq 1 1440); do
  if ls "$HFDIR"/snapshots/*/model.safetensors > /dev/null 2>&1 && ! ls "$HFDIR"/blobs/*.incomplete > /dev/null 2>&1; then break; fi
  sleep 30
done
ls "$HFDIR"/snapshots/*/model.safetensors > /dev/null 2>&1 || die "12B weights not present after 12 h"
log "12B weights present ($(du -sh "$HFDIR" | cut -f1))"
[ -s "$NSPLIT/train.jsonl" ] && [ -s "$NSPLIT/eval.jsonl" ] && [ -s "$NLSPLIT/eval.jsonl" ] && [ -s "$N78/eval.jsonl" ] || die "numeric splits missing"
if [ ! -s "$ADAPTER/head.pt" ]; then
  if [ ! -s "$SMOKE/head.pt" ]; then
    gpu_wait; log "=== h12 smoke test: 48 rows = 3 optimizer steps (logs/train_h12_smoke.log) ==="
    train "$SMOKE" 48 logs/train_h12_smoke.log
  fi
  grep -q "DONE:" logs/train_h12_smoke.log || die "smoke test did not finish (see logs/train_h12_smoke.log)"
  PEAK=$(grep -oE "peak [0-9.]+G" logs/train_h12_smoke.log | tail -1 | grep -oE "[0-9.]+"); SPS=$(grep -oE "[0-9.]+s/step" logs/train_h12_smoke.log | tail -1)
  log "smoke: peak ${PEAK:-?} GB torch-allocated, ${SPS:-?}; $(grep -oE "LoRA modules: [^;]+; head [^;]+; hidden [0-9]+" logs/train_h12_smoke.log | tail -1)"
  if [ -n "${PEAK:-}" ] && awk -v p="$PEAK" 'BEGIN{exit !(p > 50)}'; then die "smoke peak ${PEAK} GB > 50 GB cap"; fi
  gpu_wait; log "=== h12 training (Gemma-4-12B-it bf16 LoRA, H6 recipe: numeric block + team sheet + role facts, mse, 1 epoch, lr 5e-5, head lr 5e-4, batch 1 x 16, ckpt) ==="
  train "$ADAPTER" 0 logs/train_h12.log
fi
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "$tag training (no adapter/head)"
log "=== $tag predictions ==="
gpu_wait; [ -s "$OUT/${tag}_holdout_pred.jsonl" ] || predict "$NSPLIT/eval.jsonl" "$ADAPTER" "$OUT/${tag}_holdout_pred.jsonl" 8 || die "$tag holdout predict"
gpu_wait; [ -s "$OUT/${tag}_live_pred.jsonl" ] || predict "$NLSPLIT/eval.jsonl" "$ADAPTER" "$OUT/${tag}_live_pred.jsonl" 8 || die "$tag live predict"
gpu_wait; [ -s "$OUT/${tag}_live78_pred.jsonl" ] || predict "$N78/eval.jsonl" "$ADAPTER" "$OUT/${tag}_live78_pred.jsonl" 8 || log "$tag live78 predict FAILED"
log "=== $tag ledgers + mechanism checks (vs H5) ==="
python3 scripts/track_sft_accuracy.py --set "$tag holdout 2025-26 GW27-38 (12B, numeric block)" "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" "$OUT/${tag}_holdout_pred.jsonl" \
  --set "$tag live 2026-27 GW2-6" "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" "$OUT/${tag}_live_pred.jsonl" --out-md "$OUT/${tag}_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$NSPLIT/eval.jsonl" --base h5=$OUT/h5_holdout_pred.jsonl --test $tag=$OUT/${tag}_holdout_pred.jsonl --out "$OUT/${tag}_mechanism_holdout.md" >> "$LOG" 2>&1 || log "mechanism check (holdout) FAILED"
python3 scripts/team_sheet_mechanism_check.py --examples "$NLSPLIT/eval.jsonl" --base h5=$OUT/h5_live_pred.jsonl --test $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_mechanism_live.md" >> "$LOG" 2>&1 || log "mechanism check (live) FAILED"
python3 scripts/band_delta_check.py --examples "$NSPLIT/eval.jsonl" --examples "$NLSPLIT/eval.jsonl" --pred h5=$OUT/h5_holdout_pred.jsonl --pred h5=$OUT/h5_live_pred.jsonl \
  --pred h6=$OUT/h6_holdout_pred.jsonl --pred h6=$OUT/h6_live_pred.jsonl --pred $tag=$OUT/${tag}_holdout_pred.jsonl --pred $tag=$OUT/${tag}_live_pred.jsonl --out "$OUT/${tag}_band_check.md" >> "$LOG" 2>&1 || log "band check FAILED"
log "=== $tag decision backtests (3 at a time) ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_$tag/$1_$2_$3" $1 $2 $3 "$NSPLIT/eval.jsonl" "$OUT/${tag}_holdout_pred.jsonl" & done
wait
bt "$OUT/bt_$tag/2026-27_2_6" 2026-27 2 6 "$NLSPLIT/eval.jsonl" "$OUT/${tag}_live_pred.jsonl" &
[ -s "$OUT/${tag}_live78_pred.jsonl" ] && bt "$OUT/bt_$tag/2026-27_7_8" 2026-27 7 8 "$N78/eval.jsonl" "$OUT/${tag}_live78_pred.jsonl" &
wait
python3 scripts/xpts_rescore.py --label ${tag}_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h5 --test reports/h_series/bt_h6 --test reports/h_series/bt_h6b --test "reports/h_series/bt_$tag" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
log "RESULT $tag: $(TAG=$tag python3 - <<'PY'
import json, os
tag = os.environ["TAG"]
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(t):
    w = [tot(f"reports/h_series/{t}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{t}/2026-27_2_6/rolling_squad_backtest.json"), tot(f"reports/h_series/{t}/2026-27_7_8/rolling_squad_backtest.json")
c, h5, h6, h6b, h = s("bt_classic"), s("bt_h5"), s("bt_h6"), s("bt_h6b"), s(f"bt_{tag}")
print(f"squad points holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H5 {h5[1]} ({h[1] - h5[1]:+.0f}) vs H6 {h6[1]} vs H6b {h6b[1]}; live GW2-6 {h[2]} vs classic {c[2]} vs H5 {h5[2]} vs H6b {h6b[2]}; live GW7-8 {h[3]} vs classic {c[3]} vs H5 {h5[3]} vs H6b {h6b[3]}")
PY
)"
log "H12 CHAIN DONE"

#!/usr/bin/env bash
# H31 (2026-10-18, Wes: "one run with 31B gemma and see what happens"): the H1 regression-head recipe on the same E22
# corpus with Gemma-4-31B-it as the backbone, loaded in bitsandbytes nf4 so the planned peak stays under the 55 GB
# one-job rule (memory: fpl-oom-incident-2026-10-15). Same split, same eval rows, same classic reference backtests
# (reports/h_series/bt_classic) and the same ledgers as H1, so H1 (E4B) vs H31 (31B) is a pure capacity comparison.
# Env: FPL_H31_MAX_ROWS (0 = all 13,440), FPL_H31_ACCUM (16), FPL_H31_PRED_BATCH (4).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h31_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H31 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
MODEL=/home/wescheng/models/gemma-4-31b-it
ADAPTER=artifacts/gemma4_31b_h31_reghead_e22; OUT=reports/h_series
MAX_ROWS=${FPL_H31_MAX_ROWS:-0}; ACCUM=${FPL_H31_ACCUM:-16}; PB=${FPL_H31_PRED_BATCH:-4}
export FPL_RH_4BIT=1 FPL_RH_MODEL=$MODEL
bt(){ # dir season a b [examples preds]
  local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }
log "=== H31 training (31B nf4, batch 1 x accum $ACCUM, ckpt on, max rows $MAX_ROWS) ==="
if [ ! -s "$ADAPTER/head.pt" ]; then
FPL_RH_DATA_DIR=$SPLIT FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=1 FPL_RH_ACCUM=$ACCUM FPL_RH_CKPT=1 \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=100 FPL_RH_COMPACT=1 FPL_RH_MAX_ROWS=$MAX_ROWS \
  python3 -u train_gemma_reghead.py >> logs/train_h31.log 2>&1
fi
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training (no adapter/head)"
log "=== H31 predictions (31B nf4, batch $PB) ==="
[ -s "$OUT/h31_holdout_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$SPLIT/eval.jsonl" "$ADAPTER" "$OUT/h31_holdout_pred.jsonl" $PB >> "$LOG" 2>&1 || die "holdout predict"
[ -s "$OUT/h31_live_pred.jsonl" ] || python3 -u scripts/reghead_predict.py "$LSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h31_live_pred.jsonl" $PB >> "$LOG" 2>&1 || die "live predict"
python3 scripts/track_sft_accuracy.py --set "H31 holdout 2025-26 GW27-38 (E22 corpus, 31B)" "$SPLIT/eval.jsonl" "$OUT/h31_holdout_pred.jsonl" "$OUT/h31_holdout_pred.jsonl" \
  --set "H31 live 2026-27 GW2-6" "$LSPLIT/eval.jsonl" "$OUT/h31_live_pred.jsonl" "$OUT/h31_live_pred.jsonl" --out-md "$OUT/h31_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 - "$SPLIT/eval.jsonl" "$OUT/h31_holdout_pred.jsonl" "$LSPLIT/eval.jsonl" "$OUT/h31_live_pred.jsonl" <<'PY' | tee -a "$LOG"
import json, sys
import numpy as np
from sklearn.metrics import roc_auc_score, brier_score_loss
for lab, ex, pr in (("holdout", sys.argv[1], sys.argv[2]), ("live", sys.argv[3], sys.argv[4])):
    y, b, p = [], [], []
    for l in open(pr):
        q = json.loads(l); m = q["metadata"]; d = json.loads(q["response"])
        y.append(float(m["labels"]["appearance_probability"] > 0.5)); b0 = float(m["baseline_forecast"]["baseline_appearance_probability"])
        b.append(b0); p.append(min(1, max(0, b0 + d["delta_appearance_probability"])))
    y, b, p = map(np.array, (y, b, p)); unc = (b > 0.15) & (b < 0.95)
    auc = lambda yy, pp: roc_auc_score(yy, pp) if len(yy) > 10 and 0 < yy.mean() < 1 else float("nan")
    print(f"AVAIL {lab}: n {len(y)} played {y.mean():.3f} | AUC classic {auc(y, b):.4f} H31 {auc(y, p):.4f} | Brier classic {brier_score_loss(y, b):.4f} H31 {brier_score_loss(y, p):.4f} | uncertain {unc.sum()}: AUC {auc(y[unc], b[unc]):.4f} -> {auc(y[unc], p[unc]):.4f}, Brier {brier_score_loss(y[unc], b[unc]):.4f} -> {brier_score_loss(y[unc], p[unc]):.4f}")
PY
log "=== H31 decision backtests ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_h31/$1_$2_$3" $1 $2 $3 "$SPLIT/eval.jsonl" "$OUT/h31_holdout_pred.jsonl" & done
bt "$OUT/bt_h31/2026-27_2_6" 2026-27 2 6 "$LSPLIT/eval.jsonl" "$OUT/h31_live_pred.jsonl" &
wait
log "RESULT: $(python3 - <<'PY'
import json, os
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(tag):
    w = [tot(f"reports/h_series/{tag}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{tag}/2026-27_2_6/rolling_squad_backtest.json")
c, h1, h = s("bt_classic"), s("bt_h1"), s("bt_h31")
print(f"H31 squad points: holdout {h[0]} = {h[1]} vs classic {c[1]} ({h[1] - c[1]:+.0f}) vs H1 {h1[1]}; live GW2-6 {h[2]} vs classic {c[2]} vs H1 {h1[2]}")
PY
)"
python3 scripts/xpts_rescore.py --label h31_arms --out reports/h_series/xpts --baseline reports/h_series/bt_classic --test reports/h_series/bt_h1 --test reports/h_series/bt_h31 >> "$LOG" 2>&1 || log "xpts rescore FAILED"
log "H31 CHAIN DONE"

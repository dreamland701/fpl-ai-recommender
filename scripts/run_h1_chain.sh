#!/usr/bin/env bash
# H1 (2026-10-15): regression-head LoRA on the E22 corpus (status-backfilled table, per-fixture classic baseline,
# official news line in the prompt). Waits for the LoRA throughput probe (picks the fastest module-LoRA config)
# and the E22 corpus gate; runs the classic reference backtests on CPU meanwhile; then trains, predicts the
# holdout (2025-26 GW27-38) and live (2026-27 GW2-6) rows in one forward pass each, and scores accuracy,
# availability AUC and the decision backtests against the classic reference.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h1_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "H1 FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src HF_HUB_DISABLE_XET=1 HF_HUB_OFFLINE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 FPL_DRAFT_MILP=1
TABLE=data/fpl_training_rows_v3_contract_f6.csv
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
ADAPTER=artifacts/gemma4_e4b_h1_reghead_e22; OUT=reports/h_series
log "=== H1 chain: waiting for the probe and the E22 corpus ==="
until grep -q "probe done" logs/probe_lora.log 2>/dev/null; do sleep 60; done
until grep -q "E22 CORPUS DONE\|E22 CORPUS FAILED" logs/e22_corpus.log 2>/dev/null; do sleep 60; done
grep -q "E22 CORPUS DONE" logs/e22_corpus.log || die "corpus"
BATCH=1; CKPT=0; ACCUM=16; log "config: batch 1, no checkpointing (bisect 2026-10-15 13:02: 2.6 s/row vs 3.9 with ckpt at ~600 tokens), accum 16"
bt(){ # dir season a b [examples preds]
  local dir=$1 season=$2 a=$3 b=$4; shift 4; mkdir -p "$(dirname "$dir")"
  local extra=(); [ $# -ge 2 ] && extra=(--llm-examples "$1" --llm-predictions "$2" --llm-fields all)
  nice -n 10 python3 -m fpl_ai.cli backtest-squad --training-data "$TABLE" --test-season "$season" --initial-train-week-max $((a - 1)) \
    --start-week "$a" --end-week "$b" --output-dir "$dir" --skip-league-average-fetch "${extra[@]}" > "$dir.log" 2>&1; }
log "classic reference backtests (CPU, background)"
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38" "2026-27 2 6"; do set -- $W; bt "$OUT/bt_classic/$1_$2_$3" $1 $2 $3 & done
log "=== H1 training ==="
FPL_RH_DATA_DIR=$SPLIT FPL_RH_OUTPUT_DIR=$ADAPTER FPL_RH_LORA_MODE=modules FPL_RH_BATCH=$BATCH FPL_RH_ACCUM=$ACCUM FPL_RH_CKPT=$CKPT \
FPL_RH_LR=5e-5 FPL_RH_HEAD_LR=5e-4 FPL_RH_EPOCHS=1 FPL_RH_SAVE_STEPS=200 FPL_RH_COMPACT=1 \
  python3 -u train_gemma_reghead.py >> logs/train_h1.log 2>&1
[ -s "$ADAPTER/head.pt" ] && [ -s "$ADAPTER/adapter_model.safetensors" ] || die "training (no adapter/head)"
log "=== H1 predictions ==="
python3 -u scripts/reghead_predict.py "$SPLIT/eval.jsonl" "$ADAPTER" "$OUT/h1_holdout_pred.jsonl" 8 >> "$LOG" 2>&1 || die "holdout predict"
python3 -u scripts/reghead_predict.py "$LSPLIT/eval.jsonl" "$ADAPTER" "$OUT/h1_live_pred.jsonl" 8 >> "$LOG" 2>&1 || die "live predict"
python3 scripts/track_sft_accuracy.py --set "H1 holdout 2025-26 GW27-38 (E22 corpus)" "$SPLIT/eval.jsonl" "$OUT/h1_holdout_pred.jsonl" "$OUT/h1_holdout_pred.jsonl" \
  --set "H1 live 2026-27 GW2-6" "$LSPLIT/eval.jsonl" "$OUT/h1_live_pred.jsonl" "$OUT/h1_live_pred.jsonl" --out-md "$OUT/h1_accuracy.md" >> "$LOG" 2>&1 || log "accuracy ledger FAILED"
python3 - "$SPLIT/eval.jsonl" "$OUT/h1_holdout_pred.jsonl" "$LSPLIT/eval.jsonl" "$OUT/h1_live_pred.jsonl" <<'PY' | tee -a "$LOG"
import json, sys
import numpy as np
from sklearn.metrics import roc_auc_score, brier_score_loss
for lab, ex, pr in (("holdout", sys.argv[1], sys.argv[2]), ("live", sys.argv[3], sys.argv[4])):
    rows = {(r["season"], r["week"], r["metadata"]["player_id"]): r for r in map(json.loads, open(ex))}
    y, b, p = [], [], []
    for l in open(pr):
        q = json.loads(l); m = q["metadata"]; d = json.loads(q["response"])
        y.append(float(m["labels"]["appearance_probability"] > 0.5)); b0 = float(m["baseline_forecast"]["baseline_appearance_probability"])
        b.append(b0); p.append(min(1, max(0, b0 + d["delta_appearance_probability"])))
    y, b, p = map(np.array, (y, b, p))
    unc = (b > 0.15) & (b < 0.95)
    print(f"AVAIL {lab}: n {len(y)} played {y.mean():.3f} | AUC classic {roc_auc_score(y, b):.4f} H1 {roc_auc_score(y, p):.4f} | "
          f"Brier classic {brier_score_loss(y, b):.4f} H1 {brier_score_loss(y, p):.4f} | uncertain rows {unc.sum()}: AUC {roc_auc_score(y[unc], b[unc]) if unc.sum() > 10 and 0 < y[unc].mean() < 1 else float('nan'):.4f} -> {roc_auc_score(y[unc], p[unc]) if unc.sum() > 10 and 0 < y[unc].mean() < 1 else float('nan'):.4f}")
PY
log "=== H1 decision backtests ==="
for W in "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"; do set -- $W; bt "$OUT/bt_h1/$1_$2_$3" $1 $2 $3 "$SPLIT/eval.jsonl" "$OUT/h1_holdout_pred.jsonl" & done
bt "$OUT/bt_h1/2026-27_2_6" 2026-27 2 6 "$LSPLIT/eval.jsonl" "$OUT/h1_live_pred.jsonl" &
wait
log "RESULT: $(python3 - <<'PY'
import json, os
tot = lambda p: json.load(open(p))["total_actual_points"] if os.path.exists(p) else None
def s(tag):
    w = [tot(f"reports/h_series/{tag}/2025-26_{a}_{b}/rolling_squad_backtest.json") for a, b in ((27, 30), (31, 34), (35, 38))]
    return w, sum(x for x in w if x is not None), tot(f"reports/h_series/{tag}/2026-27_2_6/rolling_squad_backtest.json")
c, h = s("bt_classic"), s("bt_h1")
print(f"H1 squad points: holdout {h[0]} = {h[1]} vs classic {c[0]} = {c[1]} ({h[1] - c[1]:+.0f}); live GW2-6 {h[2]} vs classic {c[2]}")
PY
)"
log "H1 CHAIN DONE"

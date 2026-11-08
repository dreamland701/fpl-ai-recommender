#!/usr/bin/env bash
# F16 (Guardian team-news categories) + F17 (prior-season shares) together, 2026-10-28 (CPU): 21-window decision
# backtests for PB_F (production F6 table, base) / TN1_F (team-news table, FPL_TEAM_NEWS_FEATS=1) / PP_F (prior table) /
# TP_F (combined table, both on), walk-forward accuracy per config, xPts re-score against PB_F, summary.
# Logs: logs/f16_f17_chain.log. Never log the sentinel you grep for elsewhere.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/f16_f17_combo; mkdir -p "$OUT/bt" "$OUT/accuracy"
LOG=logs/f16_f17_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "=== F16+F17 chain start ==="
for t in data/fpl_training_rows_v3_contract_f6_teamnews_prior.csv; do [ -s "$t" ] || { log "missing $t"; exit 1; }; done
CONFIGS="PB_F TN1_F PP_F TP_F" JOBS=4 OUT=$OUT/bt TABLE=data/fpl_training_rows_v3_contract_f6_teamnews.csv /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1
log "backtests done: $(ls $OUT/bt/*/rolling_squad_backtest.json 2>/dev/null | wc -l) window files (expect 84)"
for triple in "PB_F:data/fpl_training_rows_v3_contract_f6.csv:0" "TN1_F:data/fpl_training_rows_v3_contract_f6_teamnews.csv:1" \
              "PP_F:data/fpl_training_rows_v3_contract_f6_prior.csv:0" "TP_F:data/fpl_training_rows_v3_contract_f6_teamnews_prior.csv:1"; do
  IFS=: read -r cfg table tn <<< "$triple"
  [ -s "$OUT/accuracy/$cfg.json" ] || PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 \
    FPL_TEAM_NEWS_FEATS=$tn PYTHONDONTWRITEBYTECODE=1 nice -n 10 $PY reports/review_fixes_2026_10/walkforward_accuracy.py "$table" "$OUT/accuracy/$cfg.json" > "$OUT/accuracy/$cfg.log" 2>&1 || log "accuracy $cfg FAILED"
done
log "accuracy done"
PYTHONPATH=$ROOT/src $PY scripts/xpts_rescore.py --baseline "$OUT/bt/PB_F" --test "$OUT/bt/TN1_F" --test "$OUT/bt/PP_F" --test "$OUT/bt/TP_F" \
  --label f16_f17 --out "$OUT/xpts" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
$PY - "$OUT" <<'PY' 2>&1 | tee -a "$LOG"
import json, glob, os, sys, statistics as st
import numpy as np
out = sys.argv[1]
def totals(cfg):
    return {os.path.basename(os.path.dirname(f))[len(cfg) + 1:]: json.load(open(f))["total_actual_points"]
            for f in glob.glob(f"{out}/bt/{cfg}_*/rolling_squad_backtest.json")}
base = totals("PB_F")
for cfg in ("TN1_F", "PP_F", "TP_F"):
    runs = totals(cfg); keys = sorted(set(base) & set(runs)); d = [runs[k] - base[k] for k in keys]
    if len(d) > 1:
        print(f"{cfg}: {len(keys)} windows | {sum(runs[k] for k in keys):.0f} vs {sum(base[k] for k in keys):.0f} ({sum(d):+.0f}) | "
              f"wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} (ties {sum(x == 0 for x in d)}) | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5):+.2f}")
acc = {}
for cfg in ("PB_F", "TN1_F", "PP_F", "TP_F"):
    try:
        acc[cfg] = json.load(open(f"{out}/accuracy/{cfg}.json"))
    except Exception as e:
        print(cfg, "accuracy missing", e)
for cfg, rows in acc.items():
    keys = sorted({k for r in rows for k in r if k.startswith(("mae_", "rmse_", "auc", "brier"))})
    print(cfg, {k: round(float(np.mean([r[k] for r in rows if k in r])), 4) for k in keys})
PY
log "F16F17 CHAIN DONE"

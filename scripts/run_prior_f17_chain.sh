#!/usr/bin/env bash
# F17 prior-season availability features + corrected F13, 2026-10-27 (CPU): 21-window decision backtests for
# PB_F (base) / PI_F (F13 re-keyed) / PP_F (F17) / PN_F (F17 without the shares), walk-forward accuracy per table,
# xPts re-score against PB_F, summary. Logs: logs/prior_f17_chain.log. Never log the sentinel you grep for elsewhere.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/prior_f17; mkdir -p "$OUT/bt" "$OUT/accuracy"
LOG=logs/prior_f17_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "=== F17 chain start ==="
CONFIGS="PB_F PI_F PP_F PN_F" JOBS=4 OUT=$OUT/bt TABLE=data/fpl_training_rows_v3_contract_f6.csv /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1
log "backtests done: $(ls $OUT/bt/*/rolling_squad_backtest.json 2>/dev/null | wc -l) window files (expect 84)"
for pair in "PB_F:data/fpl_training_rows_v3_contract_f6.csv" "PI_F:data/fpl_training_rows_v3_contract_f6_injc.csv" \
            "PP_F:data/fpl_training_rows_v3_contract_f6_prior.csv" "PN_F:data/fpl_training_rows_v3_contract_f6_priorn.csv"; do
  cfg=${pair%%:*}; table=${pair#*:}
  [ -s "$OUT/accuracy/$cfg.json" ] || PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 \
    PYTHONDONTWRITEBYTECODE=1 nice -n 10 $PY reports/review_fixes_2026_10/walkforward_accuracy.py "$table" "$OUT/accuracy/$cfg.json" > "$OUT/accuracy/$cfg.log" 2>&1 || log "accuracy $cfg FAILED"
done
log "accuracy done"
PYTHONPATH=$ROOT/src $PY scripts/xpts_rescore.py --baseline "$OUT/bt/PB_F" --test "$OUT/bt/PI_F" --test "$OUT/bt/PP_F" --test "$OUT/bt/PN_F" \
  --label prior_f17 --out "$OUT/xpts" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
$PY - "$OUT" <<'PY' 2>&1 | tee -a "$LOG"
import json, glob, os, sys, statistics as st
import numpy as np
out = sys.argv[1]
def totals(cfg):
    return {os.path.basename(os.path.dirname(f))[len(cfg) + 1:]: json.load(open(f))["total_actual_points"]
            for f in glob.glob(f"{out}/bt/{cfg}_*/rolling_squad_backtest.json")}
base = totals("PB_F")
for cfg in ("PI_F", "PP_F", "PN_F"):
    runs = totals(cfg); keys = sorted(set(base) & set(runs)); d = [runs[k] - base[k] for k in keys]
    if len(d) > 1:
        print(f"{cfg}: {len(keys)} windows | {sum(runs[k] for k in keys):.0f} vs {sum(base[k] for k in keys):.0f} ({sum(d):+.0f}) | "
              f"wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} (ties {sum(x == 0 for x in d)}) | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5):+.2f}")
acc = {}
for cfg in ("PB_F", "PI_F", "PP_F", "PN_F"):
    try:
        acc[cfg] = json.load(open(f"{out}/accuracy/{cfg}.json"))
    except Exception as e:
        print(cfg, "accuracy missing", e)
for cfg, rows in acc.items():
    keys = sorted({k for r in rows for k in r if k.startswith(("mae_", "rmse_", "auc", "brier"))})
    print(cfg, {k: round(float(np.mean([r[k] for r in rows if k in r])), 4) for k in keys})
PY
log "F17 CHAIN DONE"

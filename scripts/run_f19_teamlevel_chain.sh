#!/usr/bin/env bash
# F19 team-level baselines bench (2026-10-31, Wes: "should the classic model capture up-and-coming teams?"). CPU only,
# 3 workers beside the H6b trainer (one GPU job at a time; <=3 CPU backtest workers alongside training).
# 21-window decision backtests TL1_F (FPL_TEAM_LEVEL_FEATS=1 on data/fpl_training_rows_v3_contract_f6_teamlevel.csv, built by
# scripts/add_team_level_features.py) against the PB_F baseline already in reports/f16_f17_combo/bt (production table, same
# flags), walk-forward accuracy, xPts re-score, summary. Study behind it: reports/team_trajectory_study/README.md.
# Log: logs/f19_teamlevel_chain.log. Sentinel "F19 CHAIN DONE" (never log it elsewhere). Veto: kill the pid in logs/pids/f19_teamlevel_chain.pid.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/team_level_f19; mkdir -p "$OUT/bt" "$OUT/accuracy"
BASE=$ROOT/reports/f16_f17_combo
LOG=logs/f19_teamlevel_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
TABLE=data/fpl_training_rows_v3_contract_f6_teamlevel.csv
log "=== F19 team-level chain start (TL1_F on $TABLE vs PB_F baseline in $BASE/bt) ==="
[ -s "$TABLE" ] || { log "missing $TABLE"; exit 1; }
[ "$(ls $BASE/bt/PB_F_*/rolling_squad_backtest.json 2>/dev/null | wc -l)" -eq 21 ] || { log "PB_F baseline incomplete"; exit 1; }
CONFIGS="TL1_F" JOBS=3 OUT=$OUT/bt TABLE=$TABLE nice -n 10 /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1
log "backtests done: $(ls $OUT/bt/TL1_F_*/rolling_squad_backtest.json 2>/dev/null | wc -l) window files (expect 21)"
[ -s "$OUT/accuracy/TL1_F.json" ] || PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 \
  FPL_TEAM_LEVEL_FEATS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 $PY reports/review_fixes_2026_10/walkforward_accuracy.py "$TABLE" "$OUT/accuracy/TL1_F.json" \
  > "$OUT/accuracy/TL1_F.log" 2>&1 || log "accuracy FAILED"
[ -s "$OUT/accuracy/PB_F.json" ] || cp "$BASE/accuracy/PB_F.json" "$OUT/accuracy/PB_F.json"
log "accuracy done"
PYTHONPATH=$ROOT/src $PY scripts/xpts_rescore.py --baseline "$BASE/bt/PB_F" --test "$OUT/bt/TL1_F" --label f19_teamlevel --out "$OUT/xpts" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
$PY - "$OUT" "$BASE" <<'PY' 2>&1 | tee -a "$LOG"
import json, glob, os, sys, statistics as st
import numpy as np
out, base = sys.argv[1], sys.argv[2]
def totals(root, cfg):
    return {os.path.basename(os.path.dirname(f))[len(cfg) + 1:]: json.load(open(f))["total_actual_points"]
            for f in glob.glob(f"{root}/bt/{cfg}_*/rolling_squad_backtest.json")}
b = totals(base, "PB_F"); r = totals(out, "TL1_F"); keys = sorted(set(b) & set(r)); d = [r[k] - b[k] for k in keys]
if len(d) > 1:
    print(f"RESULT TL1_F vs PB_F: {len(keys)} windows | {sum(r[k] for k in keys):.0f} vs {sum(b[k] for k in keys):.0f} ({sum(d):+.0f}) | "
          f"wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} (ties {sum(x == 0 for x in d)}) | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5):+.2f} | "
          f"per window: " + ", ".join(f"{k} {r[k]-b[k]:+.0f}" for k in keys))
for cfg in ("PB_F", "TL1_F"):
    try:
        rows = json.load(open(f"{out}/accuracy/{cfg}.json"))
        ks = sorted({k for rr in rows for k in rr if k.startswith(("mae_", "rmse_", "auc", "brier"))})
        print(cfg, {k: round(float(np.mean([rr[k] for rr in rows if k in rr])), 4) for k in ks})
    except Exception as e:
        print(cfg, "accuracy missing", e)
PY
log "F19 CHAIN DONE"

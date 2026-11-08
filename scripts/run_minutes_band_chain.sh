#!/usr/bin/env bash
# Minutes-band calibration bench (2026-10-28, the Isak case; CPU): MB1_F (all rows) / MB2_F (unflagged only) / MB3_F (bands
# < 80 min only) on the 21 standard windows vs the rebuilt PB_F baseline in reports/f16_f17_combo/bt, then the xPts re-score.
# Log logs/minutes_band_chain.log, sentinel "MBCAL CHAIN DONE". Never log the sentinel you grep for elsewhere.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/minutes_band_cal; mkdir -p "$OUT/bt"
LOG=logs/minutes_band_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
log "=== minutes-band calibration chain start ==="
CONFIGS="MB1_F MB2_F MB3_F" JOBS=3 OUT=$OUT/bt TABLE=data/fpl_training_rows_v3_contract_f6.csv /usr/bin/bash scripts/run_market_backtests.sh >> "$LOG" 2>&1
log "backtests done: $(ls $OUT/bt/*/rolling_squad_backtest.json 2>/dev/null | wc -l) window files (expect 63)"
PYTHONPATH=$ROOT/src $PY scripts/xpts_rescore.py --baseline reports/f16_f17_combo/bt/PB_F --test "$OUT/bt/MB1_F" --test "$OUT/bt/MB2_F" --test "$OUT/bt/MB3_F" \
  --label minutes_band --out "$OUT/xpts" >> "$LOG" 2>&1 || log "xpts rescore FAILED"
$PY - "$OUT" <<'PY' 2>&1 | tee -a "$LOG"
import json, glob, os, sys, statistics as st
out = sys.argv[1]
def totals(d, cfg):
    return {os.path.basename(os.path.dirname(f))[len(cfg) + 1:]: json.load(open(f))["total_actual_points"] for f in glob.glob(f"{d}/{cfg}_*/rolling_squad_backtest.json")}
base = totals("reports/f16_f17_combo/bt", "PB_F")
for cfg in ("MB1_F", "MB2_F", "MB3_F"):
    runs = totals(f"{out}/bt", cfg); keys = sorted(set(base) & set(runs)); d = [runs[k] - base[k] for k in keys]
    if len(d) > 1:
        print(f"{cfg}: {len(keys)} windows | {sum(runs[k] for k in keys):.0f} vs {sum(base[k] for k in keys):.0f} ({sum(d):+.0f}) | wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} (ties {sum(x == 0 for x in d)}) | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5):+.2f}")
PY
log "MBCAL CHAIN DONE"

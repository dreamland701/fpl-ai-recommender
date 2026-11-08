#!/usr/bin/env bash
# 21-window squad backtest of classic + F6 with gradient-boosted trees (FPL_MODEL_CLASS=hgb).
# Compare with reports/review_fixes_2026_10/bt/N_F_* (ridge, total 5,162).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/review_fixes_2026_10/nonlinear/bt; mkdir -p "$OUT"
run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4
  local dir="$OUT/${cfg}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  local heads=minutes,1gw,3gw,5gw; [ "$cfg" = HM_F ] && heads=minutes; [ "$cfg" = H1_F ] && heads=minutes,1gw
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 OMP_NUM_THREADS=3 \
    FPL_MODEL_CLASS=hgb FPL_HGB_HEADS=$heads nice -n 10 \
    $PY -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run_one; export ROOT PY OUT
WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for cfg in ${CONFIGS:-H_F}; do for w in "${WINDOWS[@]}"; do echo "$cfg $w"; done; done | xargs -P "${JOBS:-5}" -L 1 bash -c 'run_one "$@"' _
python3 - <<'PY'
import json, glob, os
base = {os.path.basename(os.path.dirname(f))[4:]: json.load(open(f))["total_actual_points"] for f in glob.glob("reports/review_fixes_2026_10/bt/N_F_*/rolling_squad_backtest.json")}
for cfg in ("H_F", "HM_F", "H1_F"):
    runs = {os.path.basename(os.path.dirname(f))[len(cfg) + 1:]: json.load(open(f))["total_actual_points"] for f in glob.glob(f"reports/review_fixes_2026_10/nonlinear/bt/{cfg}_*/rolling_squad_backtest.json")}
    if not runs: continue
    keys = sorted(set(runs) & set(base))
    d = [runs[k] - base[k] for k in keys]
    import statistics as st
    print(f"{cfg}: {len(keys)} windows | trees {sum(runs[k] for k in keys):.0f} vs ridge {sum(base[k] for k in keys):.0f} | diff {sum(d):+.0f} | wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5) if len(d) > 1 and st.stdev(d) > 0 else float('nan'):+.2f}")
PY
echo NONLINEAR BACKTEST DONE

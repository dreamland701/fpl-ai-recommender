#!/usr/bin/env bash
# F13 injury-history features: 21-window squad backtest + walk-forward accuracy vs classic + F6 (bt/N_F, 5,162).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/review_fixes_2026_10/injury_f13; mkdir -p "$OUT"
run_one() { # season a b
  local season=$1 a=$2 b=$3 dir="$OUT/I_F_${1}_${2}_${3}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 10 \
    $PY -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6_inj.csv --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run_one; export ROOT PY OUT
printf '%s\n' "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25" \
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38" "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" \
  "2023-24 28 31" "2023-24 32 35" "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" \
  "2024-25 32 35" | xargs -P 3 -L 1 bash -c 'run_one "$@"' _
PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 \
  $PY reports/review_fixes_2026_10/walkforward_accuracy.py data/fpl_training_rows_v3_contract_f6_inj.csv "$OUT/accuracy.json" > "$OUT/accuracy.log" 2>&1
$PY - <<'PY'
import json, glob, os, statistics as st
import numpy as np
base = {os.path.basename(os.path.dirname(f))[4:]: json.load(open(f))["total_actual_points"] for f in glob.glob("reports/review_fixes_2026_10/bt/N_F_*/rolling_squad_backtest.json")}
runs = {os.path.basename(os.path.dirname(f))[4:]: json.load(open(f))["total_actual_points"] for f in glob.glob("reports/review_fixes_2026_10/injury_f13/I_F_*/rolling_squad_backtest.json")}
keys = sorted(set(base) & set(runs)); d = [runs[k] - base[k] for k in keys]
print(f"F13 injury history: {len(keys)} windows | {sum(runs[k] for k in keys):.0f} vs {sum(base[k] for k in keys):.0f} ({sum(d):+.0f}) | wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)} | t {st.mean(d) / (st.stdev(d) / len(d) ** 0.5):+.2f}")
a = json.load(open("reports/review_fixes_2026_10/accuracy/N_F.json")); b = json.load(open("reports/review_fixes_2026_10/injury_f13/accuracy.json"))
for h in (1, 3, 5):
    ka = [e[f"mae_{h}"] for e in a if f"mae_{h}" in e]; kb = [e[f"mae_{h}"] for e in b if f"mae_{h}" in e]
    print(f"  {h}GW MAE: base {np.mean(ka):.4f} | with injury history {np.mean(kb):.4f} ({np.mean(kb) - np.mean(ka):+.4f})")
PY
echo INJURY BACKTEST DONE

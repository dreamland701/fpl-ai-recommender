#!/usr/bin/env bash
# Decision-objective sweep (Wes 2026-10-11, the "ROI / stacking" question): do the optimizer's scoring knobs
# (transfer horizon, availability handling, captain leverage) change squad points? 21 windows each,
# vs baseline bt/N_F (5,162). CPU only, 3 workers.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/review_fixes_2026_10/objective_sweep; mkdir -p "$OUT"
run_one() { local v=$1 s=$2 a=$3 b=$4 dir="$OUT/${1}_${2}_${3}_${4}"; [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 10 $PY -m fpl_ai.cli backtest-squad \
    --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season "$s" --initial-train-week-max $((a - 1)) --start-week $a \
    --end-week $b --decision-variant "$v" --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1; }
export -f run_one; export ROOT PY OUT
W=("2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25" "2025-26 27 30" "2025-26 31 34"
   "2025-26 35 38" "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35" "2024-25 12 15"
   "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35")
for v in horizon5 avail_soft horizon5_avail captlev2 captlev3 avail_soft_captlev3; do for w in "${W[@]}"; do echo "$v $w"; done; done | xargs -P 3 -L 1 bash -c 'run_one "$@"' _
$PY - <<'PY'
import json, glob, os, statistics as st
base = {os.path.basename(os.path.dirname(f))[4:]: json.load(open(f))["total_actual_points"] for f in glob.glob("reports/review_fixes_2026_10/bt/N_F_*/rolling_squad_backtest.json")}
print(f"baseline: {sum(base.values()):.0f}")
for v in ("horizon5", "avail_soft", "horizon5_avail", "captlev2", "captlev3", "avail_soft_captlev3"):
    r = {os.path.basename(os.path.dirname(f))[len(v) + 1:]: json.load(open(f))["total_actual_points"] for f in glob.glob(f"reports/review_fixes_2026_10/objective_sweep/{v}_*/rolling_squad_backtest.json")}
    k = sorted(set(r) & set(base)); d = [r[x] - base[x] for x in k]
    print(f"{v}: {len(k)} windows, {sum(r[x] for x in k):.0f} ({sum(d):+.0f}), wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)}, t {st.mean(d) / (st.stdev(d) / len(d) ** .5) if len(d) > 1 and st.stdev(d) else 0:+.2f}")
PY
echo SWEEP DONE

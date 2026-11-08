#!/usr/bin/env bash
# Transfer discipline in the REAL decision engine (2026-10-10): the RL env's LLM policies beat its
# best-transfer-every-week planner mostly by holding. Does demanding a minimum projected gain before
# transferring help the actual classic + F6 engine? 21 windows per threshold; baseline (0.0) = bt/N_F (5,162).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/review_fixes_2026_10/transfer_discipline; mkdir -p "$OUT"
run_one() { # gain season a b
  local g=$1 season=$2 a=$3 b=$4 dir="$OUT/G${1}_${2}_${3}_${4}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 10 \
    $PY -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b --min-projected-gain "$g" \
    --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run_one; export ROOT PY OUT
WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for g in 1.0 2.0 3.0 5.0; do for w in "${WINDOWS[@]}"; do echo "$g $w"; done; done | xargs -P 8 -L 1 bash -c 'run_one "$@"' _
python3 - <<'PY'
import json, glob, os, statistics as st
base = {os.path.basename(os.path.dirname(f))[4:]: (json.load(open(f))["total_actual_points"], json.load(open(f))["total_transfer_hits"],
        sum(len(w.get("transfers_applied", [])) for w in json.load(open(f))["weeks"])) for f in glob.glob("reports/review_fixes_2026_10/bt/N_F_*/rolling_squad_backtest.json")}
print(f"gain >= 0.0 (current): total {sum(v[0] for v in base.values()):.0f}, transfers {sum(v[2] for v in base.values())}")
for g in ("1.0", "2.0", "3.0", "5.0"):
    runs = {}
    for f in glob.glob(f"reports/review_fixes_2026_10/transfer_discipline/G{g}_*/rolling_squad_backtest.json"):
        j = json.load(open(f)); runs[os.path.basename(os.path.dirname(f))[len(g) + 2:]] = (j["total_actual_points"], sum(len(w.get("transfers_applied", [])) for w in j["weeks"]))
    keys = sorted(set(runs) & set(base)); d = [runs[k][0] - base[k][0] for k in keys]
    t = st.mean(d) / (st.stdev(d) / len(d) ** 0.5) if len(d) > 1 and st.stdev(d) > 0 else float("nan")
    print(f"gain >= {g}: {len(keys)} windows, total {sum(runs[k][0] for k in keys):.0f} ({sum(d):+.0f}), wins {sum(x > 0 for x in d)}-{sum(x < 0 for x in d)}, t {t:+.2f}, transfers {sum(runs[k][1] for k in keys)}")
PY
echo TRANSFER DISCIPLINE DONE

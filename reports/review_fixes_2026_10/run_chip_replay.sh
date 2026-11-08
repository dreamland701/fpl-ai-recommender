#!/usr/bin/env bash
# Do model-chosen Wildcards / Free Hits pay off? N_F (fixed classic+F6) on the
# 21 re-baseline windows, with --simulate-wildcard or --simulate-free-hit,
# compared against the plain N_F runs in bt/.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/review_fixes_2026_10/bt_chips; mkdir -p "$OUT"
run_one() { # chip season a b
  local chip=$1 season=$2 a=$3 b=$4 flag
  [ "$chip" = WC ] && flag=--simulate-wildcard || flag=--simulate-free-hit
  local dir="$OUT/${chip}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 nice -n 10 \
    $PY -m fpl_ai.cli backtest-squad --training-data data/fpl_training_rows_v3_contract_f6.csv --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b $flag \
    --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run_one; export ROOT PY OUT
W=("2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25" "2025-26 27 30"
   "2025-26 31 34" "2025-26 35 38" "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31"
   "2023-24 32 35" "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35")
for chip in WC FH; do for w in "${W[@]}"; do echo "$chip $w"; done; done | xargs -P 10 -L 1 bash -c 'run_one "$@"' _
echo CHIP REPLAY DONE

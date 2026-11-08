#!/usr/bin/env bash
# Double-gameweek pricing fix (2026-10-13, memory fpl-dgw-pricing-defect): the 21-window decision
# backtest for two forecast variants, against the fixed classic+F6 baseline already in
# reports/review_fixes_2026_10/bt (config N_F = same code, same table, flags off).
#   P_F = FPL_PER_FIXTURE=1   (minutes + 1GW heads per fixture, x fixture count; P(appear) fixed)
#   A_F = FPL_DGW_PAPP=1      (only the P(appear) formula fixed)
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=$ROOT/reports/dgw_fix/bt
mkdir -p "$OUT"
TABLE=data/fpl_training_rows_v3_contract_f6.csv

run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4 flag extra=""
  case $cfg in
    P_F) flag="FPL_PER_FIXTURE=1" ;;
    A_F) flag="FPL_DGW_PAPP=1" ;;
    # MILP draft (FPL_DRAFT_MILP=1, backtest.py): exact initial squads instead of the position-ordered
    # beam, which the per-fixture forecasts exposed (three Liverpool defenders, no Salah, GW24 2024-25)
    MN_F) flag="FPL_DRAFT_MILP=1" ;;
    MP_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1" ;;
    MP1_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0" ;;
    # blend5 transfer horizon (5GW + 0.6*3GW + 0.35*1GW): with blanks and doubles priced into the
    # horizon heads, a 3-week objective sells a premium before a single blank (Salah, GW15 2024-25)
    MN5_F) flag="FPL_DRAFT_MILP=1"; extra="--decision-variant horizon5" ;;
    MP5_F) flag="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1"; extra="--decision-variant horizon5" ;;
  esac
  local dir="$OUT/${cfg}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  env $flag PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 \
    $PY -m fpl_ai.cli backtest-squad --training-data $TABLE --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b \
    --output-dir "$dir" --skip-league-average-fetch $extra > "$dir.log" 2>&1
}
export -f run_one
export ROOT PY OUT TABLE

WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for cfg in ${CONFIGS:-P_F A_F}; do
  for w in "${WINDOWS[@]}"; do echo "$cfg $w"; done
done | xargs -P "${JOBS:-10}" -L 1 bash -c 'run_one "$@"' _
echo ALL DONE

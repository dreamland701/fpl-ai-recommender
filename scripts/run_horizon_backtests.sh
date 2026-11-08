#!/usr/bin/env bash
# Programme item 2 (2026-10-17): terminal-value transfer horizons on the production (status) table.
# Baselines on disk: MP1_F (per-fixture 1GW only, ship candidate) and MP_F (full per-fixture horizons) in reports/dgw_fix/bt.
#   MPT3_F   = MP_F  + --decision-variant 3gw_t3    (3GW per-fixture sum + 3 fixtures x 5GW per-fixture rate)
#   MPT6_F   = MP_F  + 3gw_t6
#   MPB5T3_F = MP_F  + blend5_t3
#   MP1T3_F  = MP1_F + 3gw_t3   (terminal value on the ship candidate's rate-per-week heads)
#   MP1T6_F  = MP1_F + 3gw_t6
# usage: CONFIGS="MPT3_F MPT6_F" JOBS=6 scripts/run_horizon_backtests.sh
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=${OUT:-$ROOT/reports/horizon/bt}
mkdir -p "$OUT"
TABLE=${TABLE:-data/fpl_training_rows_v3_contract_f6_status.csv}
FULL="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1"
ONE="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"

run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4 flag extra=""
  case $cfg in
    MP_F)     flag="$FULL" ;;
    MP1_F)    flag="$ONE" ;;
    MPT3_F)   flag="$FULL"; extra="--decision-variant 3gw_t3" ;;
    MPT6_F)   flag="$FULL"; extra="--decision-variant 3gw_t6" ;;
    MPB5T3_F) flag="$FULL"; extra="--decision-variant blend5_t3" ;;
    MP1T3_F)  flag="$ONE";  extra="--decision-variant 3gw_t3" ;;
    MP1T6_F)  flag="$ONE";  extra="--decision-variant 3gw_t6" ;;
    *) echo "unknown config $cfg"; return 1 ;;
  esac
  local dir="$OUT/${cfg}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  local t0=$(date +%s)
  env $flag PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$ROOT/src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 \
    $PY -m fpl_ai.cli backtest-squad --training-data $TABLE --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b \
    --output-dir "$dir" --skip-league-average-fetch $extra > "$dir.log" 2>&1
  echo "$(date '+%F %T') $cfg $season $a-$b done in $(( $(date +%s) - t0 )) s (exit $?)" >> "$OUT/progress.log"
}
export -f run_one
export ROOT PY OUT TABLE FULL ONE

WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for cfg in ${CONFIGS:-MPT3_F MPT6_F MPB5T3_F MP1T3_F MP1T6_F}; do
  for w in "${WINDOWS[@]}"; do echo "$cfg $w"; done
done | xargs -P "${JOBS:-6}" -L 1 bash -c 'run_one "$@"' _
echo "$(date '+%F %T') HORIZON BENCH COMPLETE configs=${CONFIGS:-default}" >> "$OUT/progress.log"

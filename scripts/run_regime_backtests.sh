#!/usr/bin/env bash
# Programme item 1 (2026-10-17): scoring-regime alignment on the production (status) table, baseline ST1_F in
# reports/status_backfill/bt (FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0).
#   RP_F   = + position dummies only            (FPL_REGIME_TERM=pos)
#   RG1_F  = + dummies + DefCon-regime crosses   (FPL_REGIME_TERM=1)
#   RW1_F  = + recency weights, half-life 1 season (FPL_RECENCY_HALFLIFE=1)
#   RW2_F  = + recency weights, half-life 2 seasons
#   RGW_F  = regime term + half-life 2
# usage: CONFIGS="RG1_F RW2_F" JOBS=6 scripts/run_regime_backtests.sh   (WINDOWS=live adds 2026-27 GW2-6 only)
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OUT=${OUT:-$ROOT/reports/regime/bt}
mkdir -p "$OUT"
TABLE=${TABLE:-data/fpl_training_rows_v3_contract_f6_status.csv}
BASE="FPL_DRAFT_MILP=1 FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0"

run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4 flag extra=""
  case $cfg in
    ST1_F) flag="$BASE" ;;
    # item 3 (free-transfer banking): the real cap is 5 since 2024-25 (backtest default 2); run on 2024-25+ windows
    HB5_F) flag="$BASE"; extra="--max-free-transfers 5" ;;
    HB5G_F) flag="$BASE FPL_REGIME_TERM=1"; extra="--max-free-transfers 5" ;;
    # item 5 (bench credit in the weekly evaluation): measured sub usage vs the legacy 0.05/0.12/0.06/0.04
    SB1_F) flag="$BASE FPL_BENCH_WEIGHTS=0.05,0.33,0.06,0.0" ;;
    SB2_F) flag="$BASE FPL_BENCH_WEIGHTS=0.05,0.25,0.08,0.02" ;;
    # item 4 (set-piece duties): TABLE=data/fpl_training_rows_v3_contract_f6_setpiece.csv
    SP1_F) flag="$BASE" ;;
    RP_F)  flag="$BASE FPL_REGIME_TERM=pos" ;;
    RG1_F) flag="$BASE FPL_REGIME_TERM=1" ;;
    RW1_F) flag="$BASE FPL_RECENCY_HALFLIFE=1" ;;
    RW2_F) flag="$BASE FPL_RECENCY_HALFLIFE=2" ;;
    RGW_F) flag="$BASE FPL_REGIME_TERM=1 FPL_RECENCY_HALFLIFE=2" ;;
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
export ROOT PY OUT TABLE BASE

ALL_WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
case ${WINDOWS:-all} in
  live) WINDOWS_RUN=("2026-27 2 6") ;;
  s26)  WINDOWS_RUN=("${ALL_WINDOWS[@]:0:9}") ;;
  s24plus) WINDOWS_RUN=("${ALL_WINDOWS[@]:0:9}" "${ALL_WINDOWS[@]:15:6}") ;;
  *)    WINDOWS_RUN=("${ALL_WINDOWS[@]}") ;;
esac
for cfg in ${CONFIGS:-RP_F RG1_F RW1_F RW2_F RGW_F}; do
  for w in "${WINDOWS_RUN[@]}"; do echo "$cfg $w"; done
done | xargs -P "${JOBS:-6}" -L 1 bash -c 'run_one "$@"' _
echo "$(date '+%F %T') ALL DONE configs=${CONFIGS:-RP_F RG1_F RW1_F RW2_F RGW_F} windows=${WINDOWS:-all}" >> "$OUT/progress.log"

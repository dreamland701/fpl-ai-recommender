#!/usr/bin/env bash
# Re-baseline after the 2026-10 review fixes: 6 configs x 21 windows (CPU only).
#   O = pre-fix code (backup) + pre-fix tables   (what every earlier verdict used)
#   M = fixed code + pre-fix tables              (rules + label purge only)
#   N = fixed code + rebuilt contract tables     (everything)
#   _C = classic (F2b blend), _F = classic + F6
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
OLD_SRC=/home/wescheng/fpl_backups/2026-10-03_pre_review_fixes/src
OUT=$ROOT/reports/review_fixes_2026_10/bt
mkdir -p "$OUT"

run_one() { # cfg season a b
  local cfg=$1 season=$2 a=$3 b=$4 src table
  case $cfg in
    O_C) src=$OLD_SRC; table=data/fpl_training_rows_blend.csv ;;
    O_F) src=$OLD_SRC; table=data/fpl_training_rows_blend_f6.csv ;;
    M_C) src=$ROOT/src; table=data/fpl_training_rows_blend.csv ;;
    M_F) src=$ROOT/src; table=data/fpl_training_rows_blend_f6.csv ;;
    N_C) src=$ROOT/src; table=data/fpl_training_rows_v3_contract.csv ;;
    N_F) src=$ROOT/src; table=data/fpl_training_rows_v3_contract_f6.csv ;;
  esac
  local dir="$OUT/${cfg}_${season}_${a}_${b}"
  [ -f "$dir/rolling_squad_backtest.json" ] && return 0
  PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 \
    $PY -m fpl_ai.cli backtest-squad --training-data $table --test-season "$season" \
    --initial-train-week-max $((a - 1)) --start-week $a --end-week $b \
    --output-dir "$dir" --skip-league-average-fetch > "$dir.log" 2>&1
}
export -f run_one
export ROOT PY OLD_SRC OUT

WINDOWS=(
  "2025-26 2 5" "2025-26 6 9" "2025-26 10 13" "2025-26 14 17" "2025-26 18 21" "2025-26 22 25"
  "2025-26 27 30" "2025-26 31 34" "2025-26 35 38"
  "2023-24 12 15" "2023-24 16 19" "2023-24 20 23" "2023-24 24 27" "2023-24 28 31" "2023-24 32 35"
  "2024-25 12 15" "2024-25 16 19" "2024-25 20 23" "2024-25 24 27" "2024-25 28 31" "2024-25 32 35"
)
for cfg in ${CONFIGS:-O_C O_F M_C M_F N_C N_F}; do
  for w in "${WINDOWS[@]}"; do echo "$cfg $w"; done
done | xargs -P "${JOBS:-12}" -L 1 bash -c 'run_one "$@"' _
echo ALL DONE

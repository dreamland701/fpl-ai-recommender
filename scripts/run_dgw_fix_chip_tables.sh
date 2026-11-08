#!/usr/bin/env bash
# Chip-timing tables on the per-fixture forecast states (double-gameweek pricing fix, 2026-10-13).
# Waits for scripts/build_grpo_state_cache_v2.py --out reports/dgw_fix/states_pf to finish every key,
# then builds one half per invocation into reports/dgw_fix/chip_timing_pf (same layout as reports/chip_timing).
# STATES=dgw_fix/states_pf1 TABLES=dgw_fix/chip_timing_pf1 runs the 1GW-only variant (horizon heads rate-based).
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
PY=/home/wescheng/venvs/fpl-gemma-lite/bin/python
KEYS="2020-21 2021-22 2022-23 2023-24 2024-25 2025-26-train 2025-26-holdout"
for k in $KEYS; do
  until grep -q "weekly states" "logs/dgw_states_pf_$k.log" 2>/dev/null; do sleep 20; done
done
echo "$(date '+%F %T') states ready"
for half in ${HALVES:-2020-21:1 2020-21:2 2021-22:1 2021-22:2 2022-23:1 2022-23:2 2023-24:1 2023-24:2 2024-25:1 2024-25:2 2025-26:1 2025-26:2}; do
  FPL_STATES_DIR="${STATES:-dgw_fix/states_pf}" FPL_CHIP_TABLES_DIR="${TABLES:-dgw_fix/chip_timing_pf}" FPL_PLANNER_DISCIPLINE=1 PYTHONPATH=src \
    $PY scripts/chip_timing_tables.py --halves "$half" --workers 16 2>&1 | grep -v "^  FAILED" 
done
echo "$(date '+%F %T') ALL DONE"

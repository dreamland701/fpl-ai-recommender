#!/usr/bin/env bash
cd /home/wescheng/projects/fpl/fpl
PYTHONDONTWRITEBYTECODE=1 /home/wescheng/venvs/fpl-gemma-lite/bin/python scripts/backfill_history_status_from_vaastav.py --repo /tmp/claude-1000/-home-wescheng-projects-fpl-fpl/199414a0-8e7b-40c8-8cf5-1ea16aed51b2/scratchpad/vaastav/Fantasy-Premier-League --seasons 2020-21 2021-22 2022-23 2023-24 2024-25 2025-26 --setpiece --out-name weekly_setpiece.csv
echo "$(date '+%F %T') SETPIECE BACKFILL DONE"

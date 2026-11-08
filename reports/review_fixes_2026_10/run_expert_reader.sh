#!/usr/bin/env bash
# Expert-reader test (31B reads articles, rates start risk and outlook), queued after the 31B chip-advisor run
# so only one 31B copy is ever in memory alongside E21.
set -uo pipefail
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
while pgrep -f "[r]un_chip_advisor_eval.py --model-path /home" >/dev/null; do sleep 60; done
OUT=reports/review_fixes_2026_10/expert_reader
mkdir -p $OUT
PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True python3 reports/review_fixes_2026_10/expert_reader.py rate $OUT/ratings_31b.jsonl > logs/expert_reader.log 2>&1 \
  && python3 reports/review_fixes_2026_10/expert_reader.py score $OUT/ratings_31b.jsonl $OUT/result_31b.md >> logs/expert_reader.log 2>&1
echo "EXPERT READER DONE" >> logs/expert_reader.log

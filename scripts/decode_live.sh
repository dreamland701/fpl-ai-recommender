#!/usr/bin/env bash
set -uo pipefail
# Single-instance guard for live decodes. Twice now (E14 training, GW5
# decode) a second process was launched while the first was alive; with
# --resume both appended to the same file and produced duplicates (GW5:
# 672 rows / 336 dupes for 659 examples, silently corrupting the sheet).
EXAMPLES="$1"; OUTPUT="$2"; ADAPTER="$3"
cd /home/wescheng/projects/fpl/fpl
# Match the PYTHON process only. A bare pattern also matches the wrapper
# shell whose argv contains this script's own command line (self-match).
if pgrep -f "^python.*eval_gemma_responses" > /dev/null 2>&1; then
  echo "REFUSING: a decoder is already running:"
  pgrep -af "^python.*eval_gemma_responses" | cut -c1-90
  exit 1
fi
n_ex=$(wc -l < "$EXAMPLES")
if [ -f "$OUTPUT" ]; then
  n_out=$(wc -l < "$OUTPUT")
  if [ "$n_out" -gt "$n_ex" ]; then
    echo "REFUSING: $OUTPUT has $n_out rows > $n_ex examples (corrupt) — delete it first"; exit 1
  fi
fi
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
python -u eval_gemma_responses.py --model-path google/gemma-4-E4B-it \
  --examples "$EXAMPLES" --output "$OUTPUT" --adapter-path "$ADAPTER" \
  --max-new-tokens 96 --no-4bit --batch-size 16 --resume
n_out=$(wc -l < "$OUTPUT")
echo "decode finished: $n_out/$n_ex rows"
[ "$n_out" -eq "$n_ex" ] || { echo "WARNING: row-count mismatch"; exit 1; }

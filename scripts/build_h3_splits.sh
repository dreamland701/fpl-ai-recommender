#!/usr/bin/env bash
# H3 splits (2026-10-15): the E22 all-player corpus in the E22 prompt recipe, no top-N, train through 2024-25, eval all
# of 2025-26 (GW2-38) and live 2026-27 GW2-6. CPU only.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/h3_splits.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src
FULL=reports/llm_player_forecast_2022_26_e22_full.jsonl; LFULL=reports/llm_player_forecast_2627_e22_full.jsonl
SPLIT=reports/llm_residual_v2_e22_all_thru_2425_38_eval_2526_2_38; LSPLIT=reports/llm_residual_v2_e22_all_eval_2627_2_6
FLAGS=(--include-fixtures --include-congestion --include-provenance --include-defcon --compact-context
       --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 --top-n 0)
log "=== H3 splits ==="
[ -s "$SPLIT/eval.jsonl" ] || nice -n 10 python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$FULL" --output-dir "$SPLIT" "${FLAGS[@]}" \
  --train-through 2024-25:38 --eval-weeks 2025-26:2-38 >> "$LOG" 2>&1 || { log "SPLITS FAILED: holdout split"; exit 1; }
log "holdout split: $(wc -l < $SPLIT/train.jsonl) train / $(wc -l < $SPLIT/eval.jsonl) eval rows"
[ -s "$LSPLIT/eval.jsonl" ] || nice -n 10 python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$LFULL" --output-dir "$LSPLIT" "${FLAGS[@]}" \
  --train-through 2026-27:1 --eval-weeks 2026-27:2-6 >> "$LOG" 2>&1 || { log "SPLITS FAILED: live split"; exit 1; }
log "live split: $(wc -l < $LSPLIT/eval.jsonl) eval rows"
log "SPLITS DONE"

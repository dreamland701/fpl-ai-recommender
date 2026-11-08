#!/usr/bin/env bash
set -uo pipefail
# G7: GRPO on the chip and captain advisor, then closed-loop evaluation on the held-out
# 2025-26 GW20-38 and the in-sample 2024-25 GW20-38 (zero-shot pilot: advisor 2,225,
# planner 2,274, no chips 2,237 over those two). Runs alongside G6; if memory runs out the
# trainer is killed first (oom_score_adj 800).
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/g7_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True
OUT=artifacts/gemma4_e4b_grpo_chip_advisor_g7
rm -rf "$OUT"
log "G7 training starts (129 decisions x 2 epochs, lr 5e-5, temperature 1.0, receding reward)"
FPL_GRPO_OUTPUT_DIR="$OUT" python train_gemma_grpo_chip_advisor.py >> logs/train_g7.log 2>&1 &
PID=$!; echo 800 > "/proc/$PID/oom_score_adj" 2>/dev/null || true
wait "$PID"
[ -s "$OUT/adapter_model.safetensors" ] || { log "G7 TRAINING FAILED (no adapter)"; exit 1; }
log "=== G7 closed-loop eval ==="
FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --adapter-path "$OUT" --halves 2025-26:2,2024-25:2 \
  --output reports/grpo_states_v2/eval_g7_trained.json >> "$LOG" 2>&1 || log "G7 eval FAILED"
log "RESULT: $(python3 -c "
import json
t = json.load(open('reports/grpo_states_v2/eval_g7_trained.json')); z = json.load(open('reports/grpo_states_v2/eval_g7_zeroshot_pilot.json'))
for h in t:
    print(f\"{h}: trained {t[h]['advisor']} (chips {t[h]['advisor_chips']}) | zero-shot {z[h]['advisor']} | planner {t[h]['planner']} | no chips {t[h]['no_chips']} || \", end='')
" 2>&1)"
log "G7 CHAIN DONE"

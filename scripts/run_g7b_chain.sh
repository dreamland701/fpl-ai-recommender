#!/usr/bin/env bash
set -uo pipefail
# G7b: G7 with an anonymised prompt (no season/gameweek labels), two more seasons of decisions
# (2020-21, 2021-22), a KL pull toward the base model, a disciplined planner, chips-and-captain-only
# decisions, and two held-out half-seasons
# (2025-26 and 2023-24 GW20-38). G7 overfit: +135 vs the planner in-sample, -68 held out.
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/g7b_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True FPL_G7_SPLIT=g7b
# Disciplined planner (transfer only when it beats holding by 1 projected point) and a chips-and-captain-only
# advisor: the LLM's earlier edge came from holding against a best-transfer-every-week strawman.
export FPL_PLANNER_DISCIPLINE=1 FPL_PLANNER_MIN_GAIN=1.0
until [ -s reports/grpo_states_v2/2020-21.jsonl ] && [ -s reports/grpo_states_v2/2021-22.jsonl ] && ! pgrep -f "[b]uild_grpo_state_cache_v2" >/dev/null; do sleep 60; done
HALVES=2025-26:2,2023-24:2,2024-25:2
log "zero-shot baseline with the anonymised prompt on $HALVES (runs alongside training)"
FPL_GEN_DEVICE_MAP=gpu nohup python3 scripts/run_chip_advisor_eval.py --halves $HALVES \
  --output reports/grpo_states_v2/eval_g7b_zeroshot.json >> logs/g7b_zeroshot.log 2>&1 &
python3 train_gemma_grpo_chip_advisor.py --dry-run >> "$LOG" 2>&1 || { log "G7b dry run FAILED"; exit 1; }
OUT=artifacts/gemma4_e4b_grpo_chip_advisor_g7b; rm -rf "$OUT"
log "G7b training starts (lr 3e-5, KL 0.04, 2 epochs)"
FPL_GRPO_OUTPUT_DIR="$OUT" FPL_GRPO_LEARNING_RATE=3e-5 FPL_GRPO_KL_BETA=0.04 python train_gemma_grpo_chip_advisor.py >> logs/train_g7b.log 2>&1 &
PID=$!; echo 800 > "/proc/$PID/oom_score_adj" 2>/dev/null || true
wait "$PID"
[ -s "$OUT/adapter_model.safetensors" ] || { log "G7b TRAINING FAILED (no adapter)"; exit 1; }
while pgrep -f "[r]un_chip_advisor_eval.py --halves" >/dev/null; do sleep 60; done
FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --adapter-path "$OUT" --halves $HALVES \
  --output reports/grpo_states_v2/eval_g7b_trained.json >> "$LOG" 2>&1 || log "G7b eval FAILED"
log "RESULT: $(python3 -c "
import json
t = json.load(open('reports/grpo_states_v2/eval_g7b_trained.json')); z = json.load(open('reports/grpo_states_v2/eval_g7b_zeroshot.json'))
for h in t:
    tag = 'held out' if h != '2024-25:2' else 'in-sample'
    print(f\"{h} ({tag}): trained {t[h]['advisor']} | zero-shot {z.get(h, {}).get('advisor')} | planner {t[h]['planner']} | no chips {t[h]['no_chips']} || \", end='')
" 2>&1)"
log "G7B CHAIN DONE"

#!/usr/bin/env bash
set -uo pipefail
# G9: GRPO over the policy's own full-half rollouts (train_g9_rollout.py), initialised from G8 compact, then the
# closed-loop eval on the G8 halves. Waits for the GPU queue unit (E21 chain) to finish before loading a model.
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/g9_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export FPL_G9_RESUME=1 PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True FPL_PLANNER_DISCIPLINE=1 FPL_PLANNER_MIN_GAIN=1.0
H=2025-26:2,2023-24:2,2024-25:2
OUT=artifacts/gemma4_e4b_g9
while systemctl --user is-active --quiet fpl-gpu-queue; do sleep 300; done
log "=== G9: training (full-half rollouts, group 4, init G8 compact) ==="
python3 train_g9_rollout.py >> logs/train_g9.log 2>&1 || log "G9 training FAILED"
[ -s "$OUT/adapter_model.safetensors" ] || { log "no adapter; stop"; exit 1; }
log "=== G9 eval (closed loop, g9 state) ==="
FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --detail g9 --adapter-path $OUT --halves $H \
  --output reports/grpo_states_v2/eval_g9.json >> "$LOG" 2>&1 || log "G9 eval FAILED"
log "G9: $(grep -a TOTAL "$LOG" | tail -1)"
log "RESULT: $(python3 - <<'PY'
import json, os
out = []
for tag, f in (("G9", "eval_g9.json"), ("G8 compact", "eval_g8_compact.json"), ("G7b", "eval_g7b_trained.json"), ("31B zero-shot", "eval_g7b_zeroshot_31b.json")):
    p = f"reports/grpo_states_v2/{f}"
    if os.path.exists(p):
        d = json.load(open(p)); held = sum(d[h]["advisor"] for h in ("2025-26:2", "2023-24:2") if h in d)
        planner = sum(d[h]["planner"] for h in ("2025-26:2", "2023-24:2") if h in d)
        out.append(f"{tag}: held-out {held:.0f} vs planner {planner:.0f} ({held - planner:+.0f}); 2024-25 H2 {d.get('2024-25:2', {}).get('advisor')}")
print(" || ".join(out))
PY
)"
log "G9 CHAIN DONE"

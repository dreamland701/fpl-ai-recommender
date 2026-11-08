#!/usr/bin/env bash
set -uo pipefail
# G8: GRPO over the policy's own 5-week rollouts, compact state first, then rich, each evaluated week by week
# on held-out 2025-26 and 2023-24 GW20-38 (+ in-sample 2024-25 GW20-38). Runs as its own memory-capped unit
# alongside the 4-bit 31B queue.
cd /home/wescheng/projects/fpl/fpl; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/g8_chain.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export FPL_G8_RESUME=1 PYTHONDONTWRITEBYTECODE=1 PYTORCH_ALLOC_CONF=expandable_segments:True FPL_PLANNER_DISCIPLINE=1 FPL_PLANNER_MIN_GAIN=1.0
H=2025-26:2,2023-24:2,2024-25:2
for d in compact rich; do
  OUT=artifacts/gemma4_e4b_g8_$d
  log "=== G8 $d: training (50 starts x 6 rollouts x 5 weeks) ==="
  FPL_G8_DETAIL=$d FPL_G8_OUTPUT=$OUT python3 train_g8_rollout.py >> logs/train_g8_$d.log 2>&1 || log "G8 $d training FAILED"
  [ -s "$OUT/adapter_model.safetensors" ] || continue
  FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --detail $d --adapter-path $OUT --halves $H \
    --output reports/grpo_states_v2/eval_g8_$d.json >> "$LOG" 2>&1 || log "G8 $d eval FAILED"
  log "G8 $d: $(grep -a TOTAL "$LOG" | tail -1)"
done
log "=== untrained policy with the rich state (baseline for rich) ==="
FPL_GEN_DEVICE_MAP=gpu python3 scripts/run_chip_advisor_eval.py --detail rich --halves $H \
  --output reports/grpo_states_v2/eval_g8_rich_zeroshot.json >> "$LOG" 2>&1 || log "rich zero-shot FAILED"
log "RESULT: $(python3 - <<'PY'
import json, os
out = []
for tag, f in (("G8 compact", "eval_g8_compact.json"), ("G8 rich", "eval_g8_rich.json"), ("untrained rich", "eval_g8_rich_zeroshot.json"),
               ("untrained compact (G7b zero-shot)", "eval_g7b_zeroshot.json"), ("G7b", "eval_g7b_trained.json")):
    p = f"reports/grpo_states_v2/{f}"
    if os.path.exists(p):
        d = json.load(open(p)); held = sum(d[h]["advisor"] for h in ("2025-26:2", "2023-24:2") if h in d)
        planner = sum(d[h]["planner"] for h in ("2025-26:2", "2023-24:2") if h in d)
        out.append(f"{tag}: held-out {held:.0f} vs planner {planner:.0f} ({held - planner:+.0f}); 2024-25 {d.get('2024-25:2', {}).get('advisor')}")
print(" || ".join(out))
PY
)"
log "G8 CHAIN DONE"

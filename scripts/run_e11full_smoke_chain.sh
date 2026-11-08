#!/usr/bin/env bash
set -uo pipefail

# Auto-chain after E11-full consolidation: SMOKE CHECK only (no holdout
# exists — GW35-38 are now training data; quality was certified by E11's
# measured eval). Decodes 48 train rows (24 from the newly-consolidated
# 2025-26 GW35-38 + 24 random earlier) through BOTH the final E11-full
# adapter and the E11 (thru-34) fallback, then compares strict-JSON rate
# and delta magnitudes. Pass = 100% strict JSON + magnitudes in E11's
# family. Never loads a model while the trainer is alive (oom rule).

ROOT="/home/wescheng/projects/fpl/fpl"
TRAINLOG="$ROOT/logs/train_e4b_residual_e11_full.log"
ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e11_full"
E11_ADAPTER="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e11_defcon"
TRAIN_JSONL="$ROOT/reports/llm_residual_v2_e11full_top256_thru_2526_38/train.jsonl"
SAMPLE="$ROOT/reports/e11full_smoke_sample.jsonl"
FULL_OUT="$ROOT/reports/e11full_smoke_predictions_full.jsonl"
E11_OUT="$ROOT/reports/e11full_smoke_predictions_e11.jsonl"
CHAINLOG="$ROOT/logs/e11full_smoke_chain.log"
TRAINER_PID=1095800
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "smoke chain armed; waiting for E11-full trainer (pid $TRAINER_PID) to finish"

while true; do
  if grep -q "train_runtime" "$TRAINLOG" 2>/dev/null && [ -s "$ADAPTER/adapter_model.safetensors" ] && ! kill -0 "$TRAINER_PID" 2>/dev/null; then
    break
  fi
  if ! kill -0 "$TRAINER_PID" 2>/dev/null; then
    sleep 300  # grace for final save/flush
    if ! grep -q "train_runtime" "$TRAINLOG" 2>/dev/null; then
      log "SMOKE FAILED — trainer exited WITHOUT train_runtime (crash? check $TRAINLOG); fallback adapter = E11"
      exit 1
    fi
  fi
  sleep 900
done
log "E11-full training complete — building 48-row smoke sample"

python3 - <<'EOF' >> "$CHAINLOG" 2>&1
import json, random
rows = [json.loads(l) for l in open('reports/llm_residual_v2_e11full_top256_thru_2526_38/train.jsonl') if l.strip()]
def wk(r):
    return int(r['metadata'].get('week') or r.get('week') or 0)
def is_new(r):
    return r['metadata']['season'] == '2025-26' and 35 <= wk(r) <= 38
new = [r for r in rows if is_new(r)]
old = [r for r in rows if not is_new(r)]
random.seed(11)
sample = random.sample(new, min(24, len(new))) + random.sample(old, 24)
with open('reports/e11full_smoke_sample.jsonl', 'w') as f:
    for r in sample:
        f.write(json.dumps(r) + '\n')
print(f'smoke sample: {len(sample)} rows ({min(24, len(new))} from 2025-26 GW35-38, {len(sample)-min(24,len(new))} earlier)')
EOF

(
python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$SAMPLE" --output "$FULL_OUT" \
  --adapter-path "$ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume \
&& python -u "$ROOT/eval_gemma_responses.py" \
  --model-path google/gemma-4-E4B-it --examples "$SAMPLE" --output "$E11_OUT" \
  --adapter-path "$E11_ADAPTER" --max-new-tokens 96 --no-4bit --batch-size 16 --resume
) > logs/e11full_smoke_nohup.log 2>&1
if [ ! -s "$FULL_OUT" ] || [ ! -s "$E11_OUT" ]; then
  log "SMOKE FAILED — decode outputs missing (see logs/e11full_smoke_nohup.log); fallback adapter = E11"
  exit 1
fi

python3 - <<'EOF' >> "$CHAINLOG" 2>&1
import json
sample = [json.loads(l) for l in open('reports/e11full_smoke_sample.jsonl')]
def load(path):
    return [json.loads(l) for l in open(path)]
def stats(preds, label):
    strict, d1 = 0, []
    for p in preds:
        resp = (p.get('response') or p.get('completion') or '').strip()
        try:
            d = json.loads(resp)
            strict += 1
            d1.append(abs(float(d.get('delta_points_1gw') or 0.0)))
        except Exception:
            d1.append(None)
    ok = [x for x in d1 if x is not None]
    nz = sum(1 for x in ok if x > 1e-9)
    print(f"{label}: strict_json {strict}/{len(preds)} | mean|d1gw| {sum(ok)/max(len(ok),1):.3f} | max {max(ok) if ok else 0:.2f} | nonzero {nz}/{len(ok)}")
    return d1
full = stats(load('reports/e11full_smoke_predictions_full.jsonl'), 'E11-FULL')
e11  = stats(load('reports/e11full_smoke_predictions_e11.jsonl'),  'E11     ')
pairs = [(a, b) for a, b in zip(full, e11) if a is not None and b is not None]
if pairs:
    print(f"mean |d1gw(full) - d1gw(e11)| over {len(pairs)} shared-parse rows: {sum(abs(a-b) for a,b in pairs)/len(pairs):.3f}")
def wk(r):
    return int(r['metadata'].get('week') or r.get('week') or 0)
new_idx = [i for i, r in enumerate(sample) if r['metadata']['season'] == '2025-26' and 35 <= wk(r) <= 38]
newvals = [full[i] for i in new_idx if full[i] is not None]
if newvals:
    print(f"E11-FULL on the NEW GW35-38 rows: n={len(newvals)} mean|d1gw| {sum(newvals)/len(newvals):.3f} (nonzero {sum(1 for x in newvals if x>1e-9)}/{len(newvals)})")
EOF
log "SMOKE COMPLETE — E11-full adapter ready for GW2 if strict_json is 48/48 and magnitudes match E11's family"

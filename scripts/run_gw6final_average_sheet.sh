#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# After the E20 chain's GW6 final refresh: the SFT's expected (average) deltas
# for the squad and the side-by-side targets, then the side-by-side sheet with
# a third XI built from them. A short GPU job (~25 rows, ~3 minutes); G5 may be
# resuming at the same time, which is fine.
# =============================================================================
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/gw6final_average_sheet.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
export PYTHONDONTWRITEBYTECODE=1
FINAL=reports/gw6_packet_2026_10/final
EX=reports/live_gw6final_2627_f6_examples.jsonl
PR=reports/live_gw6final_2627_e20_predictions.jsonl
SUB=reports/live_gw6final_2627_f6_examples_squad_targets.jsonl
OUT=reports/live_gw6final_2627_e20_expectation_predictions_squad_targets.jsonl
GIVE_UP=$(date -d '2026-10-10T09:00:00Z' +%s)  # an hour before the GW6 deadline

until grep -aq "E20 CHAIN DONE" logs/e20_chain.log; do
  [ "$(date +%s)" -ge "$GIVE_UP" ] && { log "E20 chain never finished; skipped"; exit 1; }
  sleep 120
done
for f in "$EX" "$PR" "$FINAL/entry_state.json"; do
  [ -s "$f" ] || { log "missing $f; skipped"; exit 1; }
done
python3 - "$EX" "$FINAL/entry_state.json" "$SUB" >> "$LOG" 2>&1 <<'PY'
import json, re, sys
ex, state, out = sys.argv[1:4]
squad = {int(s["player_id"]) for s in json.load(open(state))["squad"]}
targets = set(eval(re.search(r"TARGETS = (\(.*?\))", open("scripts/sft_side_by_side.py").read()).group(1))) | {"Bijol", "De Cuyper"}
n = 0
with open(out, "w") as f:
    for line in open(ex):
        m = json.loads(line)["metadata"]
        if int(m["player_id"]) in squad or m["player_name"] in targets:
            f.write(line)
            n += 1
print(f"{n} rows (squad + targets)")
PY
rm -f "$OUT"
python -u scripts/expectation_decode.py "$SUB" "$PR" artifacts/gemma4_e4b_lora_residual_v2_e20_contract "$OUT" 0 >> "$LOG" 2>&1 \
  || { log "expectation decode FAILED"; exit 1; }
python3 scripts/sft_side_by_side.py --examples "$EX" --predictions "$PR" --entry-state "$FINAL/entry_state.json" --label e20 \
  --output-md "$FINAL/sft_side_by_side_e20_with_average.md" --expected-predictions "$OUT" >> "$LOG" 2>&1 \
  || { log "side-by-side FAILED"; exit 1; }
log "GW6 FINAL AVERAGE SHEET DONE: $FINAL/sft_side_by_side_e20_with_average.md"

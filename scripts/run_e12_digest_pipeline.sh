#!/usr/bin/env bash
set -uo pipefail

# E12-digest pipeline: single-variable evidence swap vs E11.
# Re-attach evidence over the FINAL E11 corpus (fixtures/congestion/defcon
# already attached; the attach script REBUILDS metadata.evidence_documents
# wholesale) using the digest evidence layer: filtered originals (Type-B
# list-articles removed) + 32,350 per-player mini-docs + the sky file
# unchanged (E11 parity). Then split with E11's exact flags/protocol,
# sanity gates, and — only if every gate passes — launch training.

ROOT="/home/wescheng/projects/fpl/fpl"
CORPUS_IN="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_full.jsonl"
CORPUS_OUT="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e12_digest.jsonl"
SPLIT="reports/llm_residual_v2_e12_digest_top256_thru_2526_34_eval_2526_35_38"
CHAINLOG="$ROOT/logs/e12_pipeline.log"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

log() { echo "$(date '+%F %T') $*" | tee -a "$CHAINLOG"; }
log "E12 pipeline start — re-attach evidence with digest layer"

PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$CORPUS_IN" \
  --evidence reports/e12_evidence/evidence_guardian_football_2022_23.jsonl \
  --evidence reports/e12_evidence/evidence_guardian_football_2023_24.jsonl \
  --evidence reports/e12_evidence/evidence_guardian_football_2024_25.jsonl \
  --evidence reports/e12_evidence/evidence_guardian_football_2025_26.jsonl \
  --evidence reports/e12_evidence/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
  --evidence reports/e12_evidence/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/e12_evidence/evidence_e12_typeB_minidocs.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --include-non-curated \
  --output "$CORPUS_OUT" >> "$CHAINLOG" 2>&1
if [ ! -s "$CORPUS_OUT" ]; then log "GATE FAILED — attach produced no corpus"; exit 1; fi
log "attach done ($(wc -l < "$CORPUS_OUT") rows) — building split"

python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$CORPUS_OUT" \
  --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:34 \
  --eval-weeks 2025-26:35-38 \
  --top-n 256 >> "$CHAINLOG" 2>&1
if [ ! -s "$SPLIT/summary.json" ]; then log "GATE FAILED — split build produced no summary"; exit 1; fi

log "split built — sanity gates"
python3 - <<PYEOF >> "$CHAINLOG" 2>&1
import json
s = json.load(open("$SPLIT/summary.json"))
train_n, eval_n = s["train_count"], s["eval_count"]
cov = s["train_evidence_present"] / max(train_n, 1)
defcon_lines = digest_rows = 0
for l in open("$SPLIT/train.jsonl"):
    p = json.loads(l)["prompt"]
    if "Defensive contribution (rule since 2025-26" in p: defcon_lines += 1
    if "digest:" in p: digest_rows += 1
print(f"train {train_n} eval {eval_n} coverage {cov:.1%} defcon_lines {defcon_lines} digest_rows {digest_rows}")
assert train_n > 35000, train_n
assert eval_n == 1024, eval_n
assert cov > 0.80, cov
assert defcon_lines > 7000, f"DefCon lines missing: {defcon_lines}"
assert digest_rows > 2000, f"digest mini-docs barely present in prompts: {digest_rows} — investigate before spending GPU"
PYEOF
if [ $? -ne 0 ]; then log "GATE FAILED — sanity asserts (see above)"; exit 1; fi

python3 scripts/audit_evidence_quality.py --examples "$SPLIT/train.jsonl" >> "$CHAINLOG" 2>&1 || true
log "gates PASSED — launching E12 training"

setsid nohup bash scripts/run_gemma_e4b_residual_e12_digest.sh > logs/e12_train_launcher.log 2>&1 < /dev/null &
sleep 240
if grep -qiE "traceback|error" logs/train_e4b_residual_e12_digest.log 2>/dev/null; then
  log "TRAINING LAUNCH FAILED — traceback in first 4 min (see logs/train_e4b_residual_e12_digest.log)"
  exit 1
fi
if ! pgrep -f "train_gemma_sft.py" > /dev/null; then
  log "TRAINING LAUNCH FAILED — no trainer process after 4 min"
  exit 1
fi
log "E12 TRAINING LAUNCHED — pid $(pgrep -f train_gemma_sft.py | head -1); ~55-58h to completion"

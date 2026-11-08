#!/usr/bin/env bash
set -euo pipefail

# E10-prelaunch: the actual 2026-27 GW1 ship candidate. Same evidence
# recipe as v7_scout/E9 (8 files, --include-non-curated) applied to the
# freshly rebuilt base corpus (v9_prelaunch, all seasons through 2025-26
# GW38 inclusive — the config.py cutoff fix landed 2026-08-06). Unlike
# E9 (which deliberately withheld all of 2025-26 to validate the
# train-prior/test-next methodology), this run folds 2025-26 INTO
# training so the adapter gets real DefCon-era labeled examples (see
# fpl-defcon-gap memory for why that matters) plus the season's final
# GW31-38 stretch, which no prior adapter has ever trained on.
#
# Split: train through 2025-26:34 (near-complete season), small honest
# holdout on 2025-26:35-38 (4 weeks, all DefCon-era) — not a discovery
# gate, just a sanity check that training converged normally. This is a
# deployment build, not another ablation; the real validation already
# happened via E9.

ROOT="/home/wescheng/projects/fpl/fpl"
cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

BASE_CORPUS="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v9_prelaunch.jsonl"
EVIDENCE_CORPUS="reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v9_prelaunch_evidence.jsonl"
SPLIT_DIR="reports/llm_residual_v2_e10_prelaunch_top256_thru_2526_34_eval_2526_35_38"

log() { echo "$(date '+%F %T') $*"; }

log "waiting for base corpus export to finish"
until [ -s "$BASE_CORPUS" ]; do
  sleep 60
done
log "base corpus present ($(wc -l < "$BASE_CORPUS") rows) — attaching evidence"

PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$BASE_CORPUS" \
  --evidence reports/evidence_guardian_football_2022_23.jsonl \
  --evidence reports/evidence_guardian_football_2023_24.jsonl \
  --evidence reports/evidence_guardian_football_2024_25.jsonl \
  --evidence reports/evidence_guardian_football_2025_26.jsonl \
  --evidence reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
  --evidence reports/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --include-non-curated \
  --output "$EVIDENCE_CORPUS"
log "evidence attached -> $EVIDENCE_CORPUS ($(wc -l < "$EVIDENCE_CORPUS") rows)"

python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$EVIDENCE_CORPUS" \
  --output-dir "$SPLIT_DIR" \
  --include-fixtures --include-congestion --include-provenance --include-decomposition --include-role --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:34 \
  --eval-weeks 2025-26:35-38 \
  --top-n 256

log "split built at $SPLIT_DIR"
python3 -c "
import json
s = json.load(open('$SPLIT_DIR/summary.json'))
print(json.dumps(s, indent=2))
"

# Sanity gate before spending GPU time: coverage should be in the same
# ballpark as v7/E9 (84%+), and row counts should be sane (not zero/tiny).
python3 - <<PYEOF
import json, sys
s = json.load(open("$SPLIT_DIR/summary.json"))
train_n, eval_n = s["train_count"], s["eval_count"]
train_cov = s["train_evidence_present"] / max(train_n, 1)
eval_cov = s["eval_evidence_present"] / max(eval_n, 1)
print(f"train {train_n} rows ({train_cov:.1%} evidence), eval {eval_n} rows ({eval_cov:.1%} evidence)")
assert train_n > 30000, f"train_count too low: {train_n}"
assert eval_n > 500, f"eval_count too low: {eval_n}"
assert train_cov > 0.5, f"train evidence coverage too low: {train_cov:.1%}"
print("SANITY GATE PASSED")
PYEOF

log "E10-prelaunch pipeline ready; launching training"
chmod +x "$ROOT/scripts/run_gemma_e4b_residual_e10_prelaunch.sh"
# Redirect to a separate _nohup.log catch-file, NOT the training script's
# own internal tee target (logs/train_e4b_residual_e10_prelaunch.log) —
# pointing both at the same path would corrupt interleaved writes.
setsid nohup "$ROOT/scripts/run_gemma_e4b_residual_e10_prelaunch.sh" > "$ROOT/logs/e10_train_nohup.log" 2>&1 < /dev/null &
disown
sleep 5
TRAINER_PID=$(pgrep -f "python train_gemma_sft.py" | head -1)
if [ -n "$TRAINER_PID" ]; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "E10 trainer python pid $TRAINER_PID (oom_score_adj 800)"
else
  log "E10 LAUNCH FAILED — no trainer process found"
  exit 1
fi

chmod +x "$ROOT/scripts/run_e10_post_train_chain.sh"
setsid nohup "$ROOT/scripts/run_e10_post_train_chain.sh" > "$ROOT/logs/e10_post_train_chain_nohup.log" 2>&1 < /dev/null &
disown
log "PIPELINE COMPLETE — training + post-train chain both launched and detached"

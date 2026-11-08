#!/usr/bin/env bash
set -uo pipefail

# E8 pipeline: Whisper-transcribe the full Sky Sports Fantasy Podcast
# backlog (2024-08 to present, feed exists since the Aug-2024 migration;
# covers all of 2024-25 + 2025-26) -> attach transcripts as a THIRD
# evidence source alongside the existing PL-Scout + Sky-written-tips corpus
# (v7's recipe) -> rebuild the v8 residual split with byte-identical
# builder flags to E7 -> sanity-check the new corpus actually gained
# evidence coverage over v7 (26,987/32,000 rows, 84.3%) -> launch E8
# training -> arm the post-train eval+gate chain (run_e8_post_train_chain.sh)
# and stop there for review, per standing convention (judgment points are
# not auto-cascaded).
#
# This whole script is meant to be launched once via nohup and left
# unattended; each step logs to CHAINLOG and is artifact-verified before
# the next step starts.

ROOT="/home/wescheng/projects/fpl/fpl"
CHAINLOG="$ROOT/logs/e8_podcast_evidence_pipeline.log"
PODCAST_EVIDENCE="$ROOT/reports/evidence_sky_podcast_transcripts_fantasy_2024_26.jsonl"
V6_CORPUS="$ROOT/reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v6_role.jsonl"
V8_CORPUS="$ROOT/reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v8_podcast.jsonl"
SPLIT_DIR="$ROOT/reports/llm_residual_v2_e8_top256_podcast_evidence_thru_gw11_eval_gw12_30"

cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
export PYTHONPATH="$ROOT/src"
mkdir -p "$ROOT/logs"

log() { echo "$(date '+%F %T') $*" >> "$CHAINLOG"; }
log "E8 pipeline starting: Sky Fantasy Podcast transcription"

python3 scripts/transcribe_sky_podcasts.py \
  --feed fantasy --since 2024-08-01 --until 2026-06-01 \
  --output "$PODCAST_EVIDENCE" --skip-existing \
  >> "$CHAINLOG" 2>&1

if [ ! -s "$PODCAST_EVIDENCE" ]; then
  log "TRANSCRIPTION PRODUCED NO ROWS — aborting pipeline"
  exit 1
fi
ROWS=$(wc -l < "$PODCAST_EVIDENCE")
log "transcription done: $ROWS episodes -> $PODCAST_EVIDENCE"

log "attaching evidence (PL Scout + Sky tips + podcast transcripts) onto v6 corpus"
python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$V6_CORPUS" \
  --evidence reports/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --evidence "$PODCAST_EVIDENCE" \
  --include-non-curated \
  --output "$V8_CORPUS" \
  >> "$CHAINLOG" 2>&1 \
  && log "v8 corpus built -> $V8_CORPUS" \
  || { log "CORPUS ATTACH FAILED — aborting pipeline"; exit 1; }

log "building v8 residual split (E7-identical builder flags)"
python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$V8_CORPUS" \
  --output-dir "$SPLIT_DIR" \
  --train-through 2025-26:11 --eval-weeks 2025-26:12-30 --top-n 256 \
  --include-fixtures --include-congestion --include-provenance --include-decomposition --include-role \
  --compact-context --prefer-scout --preferred-chars 800 \
  --max-evidence-docs 2 --max-evidence-chars 260 \
  >> "$CHAINLOG" 2>&1 \
  && log "v8 split built -> $SPLIT_DIR" \
  || { log "SPLIT BUILD FAILED — aborting pipeline"; exit 1; }

# Sanity gate: v7 had 32,000 train / 4,864 eval rows, 26,987 (84.3%) with
# evidence. v8 must match row counts exactly (labels/rows are untouched —
# only evidence changed) and must not have LOST evidence coverage; if
# coverage didn't move at all the podcast transcripts contributed nothing
# and an E8 run would just re-measure E7 noise, not worth 48h of GPU.
python3 - "$SPLIT_DIR/summary.json" <<'EOF' >> "$CHAINLOG" 2>&1
import json, sys
s = json.load(open(sys.argv[1]))
print("v8 summary:", {k: s[k] for k in ("train_count", "eval_count", "train_evidence_present", "eval_evidence_present")})
assert s["train_count"] == 32000, f"train_count changed: {s['train_count']}"
assert s["eval_count"] == 4864, f"eval_count changed: {s['eval_count']}"
if s["train_evidence_present"] <= 26987:
    print("SANITY WARNING: train_evidence_present did not increase over v7 (26987) — podcast evidence may not be reaching any player-week.")
    sys.exit(2)
print("sanity check passed: evidence coverage increased over v7")
EOF
SANITY=$?
if [ $SANITY -ne 0 ]; then
  log "SANITY CHECK FAILED (exit $SANITY) — NOT launching E8 training; data needs review before spending GPU time"
  exit 1
fi
log "sanity check passed — launching E8 training"

chmod +x "$ROOT/scripts/run_gemma_e4b_residual_e8_top256_podcast_evidence.sh"
nohup "$ROOT/scripts/run_gemma_e4b_residual_e8_top256_podcast_evidence.sh" > "$ROOT/logs/e8_train_nohup.log" 2>&1 &
sleep 120
TRAINER_PID=$(ps -ef | grep "python train_gemma_sft.py" | grep -v grep | awk '{print $2}' | head -1)
if [ -n "$TRAINER_PID" ] && readlink /proc/$TRAINER_PID/exe 2>/dev/null | grep -q python; then
  echo 800 > /proc/$TRAINER_PID/oom_score_adj 2>/dev/null || true
  log "E8 trainer verified, pid $TRAINER_PID (oom guard 800)"
else
  log "E8 TRAIN LAUNCH FAILED — no verified python trainer process"
  exit 1
fi

log "arming post-train eval+gate chain"
chmod +x "$ROOT/scripts/run_e8_post_train_chain.sh"
nohup "$ROOT/scripts/run_e8_post_train_chain.sh" > "$ROOT/logs/e8_post_train_chain_nohup.log" 2>&1 &
sleep 5
CHAIN_PID=$(ps -ef | grep "run_e8_post_train_chain.sh" | grep -v grep | awk '{print $2}' | head -1)
if [ -n "$CHAIN_PID" ]; then
  log "post-train chain armed, pid $CHAIN_PID — PIPELINE LAUNCH COMPLETE, stopping for review at the gate (judgment point)"
else
  log "WARNING: could not verify post-train chain process; check manually once training finishes"
fi

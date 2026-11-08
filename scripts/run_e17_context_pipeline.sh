#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E17: CONTEXT the player's own history cannot contain.
#
# Wes, 2026-09-18, on the Konsa and Evanilson-v-Liverpool cases:
#   "those are the things that you cannot tell from the previous goals of the
#    player, but need to go deep into understanding what's going on."
#
# Exactly right, and both were traced to concrete defects:
#
#  1. FIXTURE BLINDNESS. Anchor coef on opponent_goals_against_avg_3 was
#     +0.0041 (top feature 0.4843), -0.0163 on the 5-week version (wrong
#     sign); it leaned on the coarse FDR integer instead. Real 1GW points
#     swing 25-34% across opponent-quality quartiles; the forecast swung ~2%.
#     Worse, the PROMPT asserted opponent form was "already priced" and said
#     to "adjust only for" news/congestion/future fixtures — so the adapter
#     obeyed: corr(delta, opponent GA) = -0.048 while corr(delta, baseline)
#     = -0.708, i.e. the channel had collapsed to unconditional shrink.
#
#  2. NO TEAM-MATE CONTEXT. Konsa carried a cold-start P(app) of 0.74 while
#     Saliba was injured, White doubtful (75%) and Mosquera doubtful (50%).
#     His prompt mentioned NONE of his six positional rivals, because
#     evidence windows are mention-centered: an article about Saliba attaches
#     to Saliba, never to Konsa. (This is why the four earlier regex
#     team-context attempts failed — they mined prose for a structured field.)
#
# THREE CHANGES vs the E11-defcon champion. Everything else is byte-identical
# (same evidence sources, max-docs 2 x 260 chars, top-n 256, train-through
# 2025-26:34, eval 2025-26:35-38, same hyperparameters) so the comparison is
# clean:
#   A. FPL_OPPONENT_INTERACTION=1 — F6 anchor features. Already validated on
#      the classic anchor: 1GW MAE -0.0339 winning 4/4 windows, decision
#      value +112 over 5 windows (3/5). Regenerates corpus baselines.
#   B. attach_depth_chart_to_corpus.py — positional depth chart + opponent's
#      measured recent defensive record, both from structured official data.
#   C. FPL_PROMPT_V17=1 — provenance text that states the two blind spots
#      honestly and names the opponent adjustment as in-scope.
#
# NOTE F7 (depth chart as ANCHOR features) was measured NEGATIVE and is
# deliberately NOT enabled: +0.0107 MAE, lost 4/4 windows, every component
# neutral-to-harmful. The signal is real but collinear with minutes_avg_3.
# It belongs in the prompt, as a judgment call, which is what C does.
# =============================================================================

ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs reports
LOG="logs/e17_pipeline.log"
log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
die(){ log "GATE FAILED: $*"; exit 1; }

TABLE="data/fpl_training_rows_blend_f6.csv"
BASE="reports/llm_player_forecast_2022_26_e17_base.jsonl"
EV="reports/_e17_ev.jsonl"; FX="reports/_e17_fx.jsonl"; CG="reports/_e17_cg.jsonl"
DC="reports/_e17_dc.jsonl"
FULL="reports/llm_player_forecast_2022_26_e17_full.jsonl"
SPLIT="reports/llm_residual_v2_e17_context_top256_thru_2526_34_eval_2526_35_38"

export FPL_PRIOR_BLEND=1
export FPL_OPPONENT_INTERACTION=1
# F7 anchor features stay OFF (measured negative) - prompt-side only.
export FPL_DEPTH_CHART=0

log "=== E17 step 1/6: training table with F6 opponent interaction ==="
if [ -s "$TABLE" ]; then log "table exists, reusing $TABLE"; else
  PYTHONPATH=src python3 -m fpl_ai.cli build-training-table \
    --history-root data/fpl_history --output "$TABLE" >>"$LOG" 2>&1 || die "build-training-table"
fi
python3 -c "
import pandas as pd,sys,warnings;warnings.filterwarnings('ignore')
d=pd.read_csv('$TABLE',low_memory=False)
need=['opp_def_weakness_3','form_x_opp_weakness_3','xgi_x_opp_weakness_3']
missing=[c for c in need if c not in d.columns]
sys.exit('missing F6 cols: '+str(missing) if missing else 0)
" >>"$LOG" 2>&1 || die "F6 columns absent from table"
log "table OK ($(wc -l < "$TABLE") rows)"

log "=== E17 step 2/6: export base corpus with F6 baselines (slow) ==="
if [ -s "$BASE" ]; then log "base corpus exists, reusing"; else
  PYTHONPATH=src python3 -m fpl_ai.cli export-llm-player-forecast-corpus \
    --training-data "$TABLE" --output "$BASE" \
    --seasons 2022-23,2023-24,2024-25,2025-26 \
    --prompt-style baseline_adjustment >>"$LOG" 2>&1 || die "corpus export"
fi
[ -s "$BASE" ] || die "base corpus empty"
log "base corpus ready ($(wc -l < "$BASE") rows)"

log "=== E17 step 3/6: evidence attach (E11 recipe, unchanged) ==="
# Reuse guards: stages 1-3 are deterministic and slow (~18 min). The E17
# prompt gate failed once on a bug isolated to stage 4, so a relaunch should
# not redo the evidence chain. Delete reports/_e17_*.jsonl to force a rebuild.
if [ -s "$CG" ]; then
  log "evidence/fixture/congestion outputs exist, reusing ($(wc -l < "$CG") rows)"
else
PYTHONPATH=src python3 scripts/attach_player_evidence_to_corpus.py \
  --corpus "$BASE" \
  --evidence reports/evidence_guardian_football_2022_23.jsonl \
  --evidence reports/evidence_guardian_football_2023_24.jsonl \
  --evidence reports/evidence_guardian_football_2024_25.jsonl \
  --evidence reports/evidence_guardian_football_2025_26.jsonl \
  --evidence reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl \
  --evidence reports/evidence_pl_scout_2022_26.jsonl \
  --evidence reports/evidence_sky_fpl_expert_tips_2022_26.jsonl \
  --include-non-curated --output "$EV" >>"$LOG" 2>&1 || die "evidence attach"
PYTHONPATH=src python3 scripts/attach_fixture_outlook_to_corpus.py \
  --corpus "$EV" --history-dir data/fpl_history --output "$FX" >>"$LOG" 2>&1 || die "fixture attach"
PYTHONPATH=src python3 scripts/attach_congestion_to_corpus.py \
  --corpus "$FX" --euro-fixtures data/competition_fixtures/european_fixtures.jsonl \
  --history-dir data/fpl_history --output "$CG" >>"$LOG" 2>&1 || die "congestion attach"
fi

log "=== E17 step 4/6: NEW depth-chart + opponent-record attach ==="
PYTHONPATH=src python3 scripts/attach_depth_chart_to_corpus.py \
  --corpus "$CG" --history-root data/fpl_history --output "$DC" >>"$LOG" 2>&1 || die "depth-chart attach"
PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py \
  --corpus "$DC" --training-data "$TABLE" --output "$FULL" >>"$LOG" 2>&1 || die "defcon attach"
[ -s "$FULL" ] || die "attach chain produced nothing"
log "attach chain done ($(wc -l < "$FULL") rows)"

log "=== E17 step 5/6: split with v17 prompts ==="
export FPL_PROMPT_V17=1
python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$FULL" --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:34 --eval-weeks 2025-26:35-38 --top-n 256 >>"$LOG" 2>&1 || die "split build"

log "=== E17 step 6/6: PROMPT GATE (never burn 50h on a broken split) ==="
python3 - <<'PYEOF' >>"$LOG" 2>&1 || die "prompt gate"
import json, sys, glob
paths = glob.glob("reports/llm_residual_v2_e17_context_top256_thru_2526_34_eval_2526_35_38/train.jsonl")
if not paths: sys.exit("no train.jsonl")
n = depth = opp = prov = 0
for line in open(paths[0]):
    rec = json.loads(line)
    text = json.dumps(rec)
    n += 1
    if "Positional depth chart" in text: depth += 1
    if "Opponent recent record" in text: opp += 1
    if "Two known weaknesses you SHOULD correct" in text: prov += 1
print(f"gate: rows={n} depth_chart={depth} opponent={opp} v17_provenance={prov}")
if n == 0: sys.exit("empty train split")
if prov < n * 0.95: sys.exit(f"v17 provenance missing on {n-prov}/{n} rows")
if opp  < n * 0.80: sys.exit(f"opponent block missing on {n-opp}/{n} rows")
if depth < n * 0.70: sys.exit(f"depth chart missing on {n-depth}/{n} rows")
print("GATE PASSED")
PYEOF
log "gate passed — launching training"

DATA_DIR="$ROOT/$SPLIT"
OUTPUT_DIR="$ROOT/artifacts/gemma4_e4b_lora_residual_v2_e17_context"
export PYTORCH_ALLOC_CONF=expandable_segments:True
export FPL_GEMMA_MODEL_PATH="google/gemma-4-E4B-it"
export FPL_GEMMA_LOAD_IN_4BIT=false
export FPL_GEMMA_DATA_DIR="$DATA_DIR"
export FPL_GEMMA_OUTPUT_DIR="$OUTPUT_DIR"
export FPL_GEMMA_MAX_SEQ_LENGTH=1536
export FPL_GEMMA_TRUNCATION_MODE=keep_start
export FPL_GEMMA_MAX_STEPS=-1
export FPL_GEMMA_NUM_EPOCHS=1
export FPL_GEMMA_LEARNING_RATE=5e-5
export FPL_GEMMA_TRAIN_BATCH_SIZE=1
export FPL_GEMMA_EVAL_BATCH_SIZE=2
export FPL_GEMMA_GRAD_ACCUM=16
export FPL_GEMMA_LOGGING_STEPS=10
export FPL_GEMMA_EVAL_STRATEGY=no
export FPL_GEMMA_SAVE_STEPS=100
export FPL_GEMMA_SAVE_TOTAL_LIMIT=3
export FPL_GEMMA_WARMUP_STEPS=30
export FPL_GEMMA_GRADIENT_CHECKPOINTING=true
export FPL_GEMMA_LORA_DROPOUT=0.0
echo 800 > /proc/self/oom_score_adj 2>/dev/null || true
log "training -> $OUTPUT_DIR"
python train_gemma_sft.py 2>&1 | tee "logs/train_e4b_residual_e17_context.log"
log "E17 training exited rc=$?"

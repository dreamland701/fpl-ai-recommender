#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# E20 corpus: the E19 recipe rebuilt on the data-contract-fixed pipeline.
#
# E19 (F6 anchor, v1 prompts, train through 2025-26:26, holdout GW27-38) is
# the readable-holdout reference. E20 changes ONLY the data, per
# docs/review_fixes_2026_10.md: ownership in true percent, no end-of-season
# status/news copied onto history, club at fixture time, as-of F6 centering,
# and corpus baselines fit with immature multi-week labels purged.
#
# Same evidence sources, same attach chain (minus the depth chart, which v1
# prompts never render), same split flags. Wes approved the GPU work on
# 2026-10-04; scripts/run_e20_contract_chain.sh trains on this split.
# =============================================================================
ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
mkdir -p logs reports
LOG="logs/e20_pipeline.log"
log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
die(){ log "GATE FAILED: $*"; exit 1; }

TABLE="data/fpl_training_rows_v3_contract_f6.csv"
BASE="reports/llm_player_forecast_2022_26_e20_base.jsonl"
EV="reports/_e20_ev.jsonl"; FX="reports/_e20_fx.jsonl"; CG="reports/_e20_cg.jsonl"
FULL="reports/llm_player_forecast_2022_26_e20_full.jsonl"
SPLIT="reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38"
REF="reports/llm_residual_v2_e19_wideholdout_top256_thru_2526_26_eval_2526_27_38"

export FPL_PRIOR_BLEND=1
export FPL_OPPONENT_INTERACTION=1
export FPL_DEPTH_CHART=0
export PYTHONDONTWRITEBYTECODE=1

log "=== E20 step 1/5: fixed table sanity ==="
python3 - <<PYEOF >>"$LOG" 2>&1 || die "table sanity"
import sys, warnings
import pandas as pd
warnings.filterwarnings("ignore")
d = pd.read_csv("$TABLE", low_memory=False, usecols=lambda c: c in {
    "season", "opp_def_weakness_3", "selected_by_percent_pre_deadline", "status_pre_deadline"})
problems = []
if "opp_def_weakness_3" not in d.columns: problems.append("no F6 columns")
if d["selected_by_percent_pre_deadline"].max() > 100: problems.append("ownership not in percent")
hist = d.loc[d["season"] != "2026-27", "status_pre_deadline"].fillna("").astype(str).str.strip()
if (hist != "").mean() > 0.001: problems.append("historical status is not unknown")
print("table:", len(d), "rows; problems:", problems or "none")
sys.exit("; ".join(problems) if problems else 0)
PYEOF
log "table OK"

log "=== E20 step 2/5: export base corpus with fixed baselines ==="
if [ -s "$BASE" ]; then log "base corpus exists, reusing"; else
  PYTHONPATH=src python3 -m fpl_ai.cli export-llm-player-forecast-corpus \
    --training-data "$TABLE" --output "$BASE" \
    --seasons 2022-23,2023-24,2024-25,2025-26 \
    --prompt-style baseline_adjustment >>"$LOG" 2>&1 || die "corpus export"
fi
[ -s "$BASE" ] || die "base corpus empty"
log "base corpus ready ($(wc -l < "$BASE") rows)"

log "=== E20 step 3/5: evidence, fixture outlook, congestion, defcon (E17/E19 recipe) ==="
if [ -s "$FULL" ]; then log "full corpus exists, reusing"; else
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
  PYTHONPATH=src python3 scripts/attach_defcon_to_corpus.py \
    --corpus "$CG" --training-data "$TABLE" --output "$FULL" >>"$LOG" 2>&1 || die "defcon attach"
fi
[ -s "$FULL" ] || die "attach chain produced nothing"
log "attach chain done ($(wc -l < "$FULL") rows)"

log "=== E20 step 4/5: split (E19 flags, v1 prompts) ==="
unset FPL_PROMPT_V17
python3 scripts/build_residual_player_forecast_split_v2.py \
  --corpus "$FULL" --output-dir "$SPLIT" \
  --include-fixtures --include-congestion --include-provenance --include-defcon --compact-context \
  --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 \
  --train-through 2025-26:26 --eval-weeks 2025-26:27-38 --top-n 256 >>"$LOG" 2>&1 || die "split build"

log "=== E20 step 5/5: PROMPT GATE (never burn 55h on a broken split) ==="
python3 - <<PYEOF >>"$LOG" 2>&1 || die "prompt gate"
import json, sys
def scan(path):
    n = v1 = v17 = depth = opp = market = status_none = 0
    for line in open(path):
        text = json.loads(line)["prompt"] if line.strip() else ""
        n += 1
        v1 += "already prices in recent form" in text
        v17 += "Two known weaknesses you SHOULD correct" in text
        depth += "Positional depth chart" in text
        opp += "Opponent recent record" in text
        market += "- Market:" in text
        status_none += "Status pre-deadline: none" in text
    return dict(n=n, v1=v1, v17=v17, depth=depth, opp=opp, market=market, status_none=status_none)
new_train, new_eval = scan("$SPLIT/train.jsonl"), scan("$SPLIT/eval.jsonl")
ref_train, ref_eval = scan("$REF/train.jsonl"), scan("$REF/eval.jsonl")
print("E20 train", new_train); print("E20 eval ", new_eval)
print("E19 train", ref_train); print("E19 eval ", ref_eval)
problems = []
for label, new, ref in (("train", new_train, ref_train), ("eval", new_eval, ref_eval)):
    if new["n"] == 0: problems.append(f"{label} empty")
    if abs(new["n"] - ref["n"]) > 0.05 * ref["n"]: problems.append(f"{label} rows {new['n']} vs E19 {ref['n']}")
    if new["v1"] != new["n"]: problems.append(f"{label} v1 provenance on {new['v1']}/{new['n']}")
    if new["v17"] or new["depth"] or new["opp"] or new["market"]: problems.append(f"{label} has non-E19 blocks")
    if new["status_none"] < 0.95 * new["n"]: problems.append(f"{label} status lines not neutral ({new['status_none']}/{new['n']})")
print("problems:", problems or "none")
sys.exit("; ".join(problems) if problems else 0)
PYEOF
log "GATE PASSED — split ready at $SPLIT"

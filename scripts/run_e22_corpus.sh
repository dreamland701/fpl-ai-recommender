#!/usr/bin/env bash
# E22 corpus (2026-10-15): E21 recipe (12 h cutoff, focused articles, top 96) rebuilt on the status-backfilled
# table with the per-fixture classic baseline, so prompts carry the official pre-deadline status/news line
# (none before: every earlier adapter trained with that line empty) and the production classic as baseline.
set -uo pipefail
ROOT=/home/wescheng/projects/fpl/fpl; cd "$ROOT"; source /home/wescheng/venvs/fpl-gemma-lite/bin/activate
LOG=logs/e22_corpus.log; log(){ echo "$(date '+%F %T') $*" | tee -a "$LOG"; }; die(){ log "E22 CORPUS FAILED: $*"; exit 1; }
export PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_DEPTH_CHART=0 \
       FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0
export FPL_EVIDENCE_DROP='price (rise|fall|change)s?|risers|fallers|most.?bought|most.?sold|transfers in|transfer (window|news|rumou?rs?|gossip|deadline|verdict|latest)|deadline day'
export FPL_EVIDENCE_PRIORITY='team news|predicted line'
TABLE=data/fpl_training_rows_v3_contract_f6.csv; CUTOFF=12
BASE=reports/llm_player_forecast_2022_26_e22_base.jsonl; LBASE=reports/llm_player_forecast_2627_e22_base.jsonl
FULL=reports/llm_player_forecast_2022_26_e22_full.jsonl; LFULL=reports/llm_player_forecast_2627_e22_full.jsonl
SPLIT=reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38; LSPLIT=reports/llm_residual_v2_e22_top96_eval_2627_2_6
SPLIT_FLAGS=(--include-fixtures --include-congestion --include-provenance --include-defcon --compact-context
             --prefer-scout --preferred-chars 800 --max-evidence-docs 2 --max-evidence-chars 260 --top-n 96)
attach(){ local base=$1 out=$2 tag=$3; shift 3; local ev=(); for f in "$@"; do ev+=(--evidence "$f"); done
  python3 scripts/attach_player_evidence_to_corpus.py --corpus "$base" "${ev[@]}" --include-non-curated --cutoff-hours "$CUTOFF" \
    --output "reports/_e22${tag}_ev.jsonl" >> "$LOG" 2>&1 || return 1
  python3 scripts/attach_fixture_outlook_to_corpus.py --corpus "reports/_e22${tag}_ev.jsonl" --history-dir data/fpl_history \
    --output "reports/_e22${tag}_fx.jsonl" >> "$LOG" 2>&1 || return 1
  python3 scripts/attach_congestion_to_corpus.py --corpus "reports/_e22${tag}_fx.jsonl" --euro-fixtures data/competition_fixtures/european_fixtures.jsonl \
    --history-dir data/fpl_history --output "reports/_e22${tag}_cg.jsonl" >> "$LOG" 2>&1 || return 1
  python3 scripts/attach_defcon_to_corpus.py --corpus "reports/_e22${tag}_cg.jsonl" --training-data "$TABLE" --output "$out" >> "$LOG" 2>&1; }
log "=== E22 corpora ==="
[ -s "$BASE" ] || die "base corpus missing"
[ -s "$LBASE" ] || python3 -m fpl_ai.cli export-llm-player-forecast-corpus --training-data "$TABLE" --output "$LBASE" --seasons 2026-27 \
    --prompt-style baseline_adjustment >> "$LOG" 2>&1 || die "live base export"
log "live base $(wc -l < "$LBASE") rows"
[ -s "$FULL" ] || attach "$BASE" "$FULL" train reports/evidence_guardian_football_2022_23.jsonl reports/evidence_guardian_football_2023_24.jsonl \
  reports/evidence_guardian_football_2024_25.jsonl reports/evidence_guardian_football_2025_26.jsonl \
  reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl reports/evidence_pl_scout_2022_26.jsonl \
  reports/evidence_sky_fpl_expert_tips_2022_26.jsonl || die "training corpus"
[ -s "$LFULL" ] || attach "$LBASE" "$LFULL" live reports/evidence_guardian_football_2627_gw2.jsonl reports/evidence_guardian_football_2627_gw3.jsonl \
  reports/evidence_guardian_football_2627_gw4.jsonl reports/evidence_guardian_football_2627_gw5.jsonl reports/evidence_guardian_football_2627_gw6.jsonl \
  reports/evidence_guardian_football_2627_gw6final.jsonl reports/evidence_guardian_football_2627_gw7.jsonl \
  reports/evidence_pl_scout_2627_gw2.jsonl reports/evidence_pl_scout_2627_gw3.jsonl reports/evidence_pl_scout_2627_gw4.jsonl \
  reports/evidence_pl_scout_2627_gw5.jsonl reports/evidence_pl_scout_2627_gw6.jsonl reports/evidence_pl_scout_2627_gw6final.jsonl \
  reports/evidence_pl_scout_2627_gw7.jsonl || die "live corpus"
python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$FULL" --output-dir "$SPLIT" "${SPLIT_FLAGS[@]}" \
  --train-through 2025-26:26 --eval-weeks 2025-26:27-38 >> "$LOG" 2>&1 || die "split"
python3 scripts/build_residual_player_forecast_split_v2.py --corpus "$LFULL" --output-dir "$LSPLIT" "${SPLIT_FLAGS[@]}" \
  --train-through 2026-27:1 --eval-weeks 2026-27:2-6 >> "$LOG" 2>&1 || die "live split"
log "=== prompt gate ==="
python3 - "$SPLIT" "$LSPLIT" <<'PYEOF' >> "$LOG" 2>&1 || die "prompt gate"
import json, os, re, sys
from datetime import datetime
DOC = re.compile(r"\n\[(\d+)\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)")
drop = re.compile(os.environ["FPL_EVIDENCE_DROP"], re.I); prio = re.compile(os.environ["FPL_EVIDENCE_PRIORITY"], re.I)
problems = []
for path in (f"{sys.argv[1]}/train.jsonl", f"{sys.argv[1]}/eval.jsonl", f"{sys.argv[2]}/eval.jsonl"):
    n = ev = late = dropped = misordered = team = news = 0
    for line in open(path):
        r = json.loads(line); n += 1
        news += "Official player news pre-deadline: none" not in r["prompt"]
        dl = datetime.fromisoformat(str(r["deadline_ts"]).replace("Z", "+00:00")) if r.get("deadline_ts") not in (None, "", "nan") else None
        docs = DOC.findall("\n" + r["prompt"].split("Timestamp-safe text evidence:", 1)[-1])
        ev += bool(docs)
        for i, (idx, src, ts, title) in enumerate(docs):
            if dl and (dl - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() < 12 * 3600 - 1:
                late += 1
            dropped += bool(drop.search(title)); team += bool(prio.search(title))
            if i > 0 and prio.search(title) and not prio.search(docs[0][3]):
                misordered += 1
    print(f"{path}: {n} rows, {ev} with evidence, {news} with official news, team-news docs {team}, docs <12h {late}, dropped types {dropped}, misordered {misordered}")
    if n == 0 or late or dropped or misordered:
        problems.append(path)
print("problems:", problems or "none")
sys.exit(1 if problems else 0)
PYEOF
log "GATE PASSED: $(wc -l < $SPLIT/train.jsonl) train / $(wc -l < $SPLIT/eval.jsonl) holdout / $(wc -l < $LSPLIT/eval.jsonl) live rows"
log "E22 CORPUS DONE"

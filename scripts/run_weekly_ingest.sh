#!/usr/bin/env bash
set -uo pipefail
# =============================================================================
# Weekly post-gameweek data ingestion, with the gates that past mistakes earned.
#
# Usage:  scripts/run_weekly_ingest.sh <completed_gw>
#   e.g.  scripts/run_weekly_ingest.sh 5     # after GW5 has FULLY settled
#
# This exists because the weekly process was purely manual and its steps are
# individually easy to forget. Each gate below is here because of a specific
# incident:
#
#  1. SETTLED GATE. Twice (GW2, GW4 2026-27) a mid-gameweek scoreline was
#     narrated as final; GW4's "three defenders blanked" post-mortem was
#     simply wrong because Leeds had not kicked off. Provisional league
#     averages also drift a lot late (GW2 read 66 mid-week, settled at 79).
#     Nothing downstream runs until gw_status.py says settled.
#
#  2. STATUS BACKFILL. Found 2026-09-18: sync-history writes status='a' and
#     empty news on EVERY live-season row. Saliba read "available" with 0
#     minutes for four straight gameweeks, so the injury flag was dead for
#     the whole live season while history ran 19-38% flagged. Left manual,
#     this bug returns every single week. See backfill_live_status_from_corpus.py.
#
#  3. STATUS VERIFY. Belt and braces on (2): if the flagged rate is still
#     0.000 after the backfill, something upstream changed - stop loudly
#     rather than train on data where nobody is ever injured.
#
# Does NOT touch the cutoff in src/fpl_ai/config.py or build any corpus;
# it prints the remaining manual steps at the end.
# =============================================================================

ROOT="/home/wescheng/projects/fpl/fpl"; cd "$ROOT"
source /home/wescheng/venvs/fpl-gemma-lite/bin/activate

GW="${1:-}"; NEXT=$(( ${GW:-0} + 1 ))
SEASON="${FPL_SEASON:-2026-27}"
if [ -z "$GW" ]; then echo "usage: $0 <completed_gw>   (the gameweek that just FINISHED)"; exit 2; fi

log(){ echo "$(date '+%F %T') $*"; }
die(){ echo "STOP: $*" >&2; exit 1; }

log "=== gate 1/4: is GW$GW actually settled? ==="
PYTHONPATH=src python3 scripts/gw_status.py --event "$GW" --require-settled \
  || die "GW$GW is NOT settled. Do not score, do not ledger, do not ingest. Re-run when every fixture is finished."

log "=== step 2/4: sync history through GW$GW ==="
PYTHONPATH=src python3 -m fpl_ai.cli sync-history \
  --history-root data/fpl_history --current-season "$SEASON" --current-max-gw "$GW" \
  || die "sync-history failed"

log "=== step 3/4: backfill pre-deadline status/news (else the injury flag is dead) ==="
PYTHONPATH=src python3 scripts/backfill_live_status_from_corpus.py \
  --season "$SEASON" --history-root data/fpl_history --reports-dir reports \
  || die "status backfill failed"

log "=== gate 4/4: verify the injury flag is actually populated ==="
PYTHONPATH=src python3 - "$SEASON" "$GW" <<'PYEOF' || die "status verification failed"
import csv, collections, sys
season, gw = sys.argv[1], int(sys.argv[2])
counts = collections.Counter()
by_week = collections.defaultdict(lambda: [0, 0])  # week -> [rows, flagged]
for row in csv.DictReader(open(f"data/fpl_history/{season}/merged_gw.csv")):
    counts[str(row.get("status") or "?")] += 1
    try:
        w = int(row.get("round") or 0)
    except ValueError:
        w = 0
    by_week[w][0] += 1
    by_week[w][1] += str(row.get("status") or "a") != "a"
total = sum(counts.values())
# 2026-10-26: GW7 and GW8 rows were all 'a' while the season aggregate still read 0.18-0.21, because the corpus
# naming changed and the backfill matched nothing for those weeks. Check the week that just finished on its own.
print("  flagged by week: " + ", ".join(f"GW{w} {f/n:.2f}" for w, (n, f) in sorted(by_week.items()) if n))
n_gw, f_gw = by_week.get(gw, [0, 0])
if n_gw == 0:
    raise SystemExit(f"no GW{gw} rows in merged_gw.csv after the sync")
if f_gw == 0:
    raise SystemExit(f"GW{gw} flagged rate is 0.000 - the status backfill did not reach this week's rows "
                     f"(is reports/live_gw{gw}*_corpus_bare*.jsonl present?). Do NOT rebuild the training table on this.")
flagged = total - counts.get("a", 0)
rate = flagged / total if total else 0.0
print(f"  status distribution: {dict(counts)}")
print(f"  flagged rate: {rate:.3f}  (historical seasons run 0.19-0.38)")
if total == 0:
    raise SystemExit("no rows in merged_gw.csv")
if rate == 0.0:
    raise SystemExit(
        "flagged rate is 0.000 - the backfill did not take. Every player reads "
        "'available'. Do NOT rebuild the training table on this."
    )
if rate < 0.05:
    print("  WARNING: flagged rate unusually low; check the archived corpora are present")
PYEOF

log "=== ingestion OK. Remaining MANUAL steps ==="
cat <<EOF

  1. Bump TRAINING_CUTOFF_WEEK to $GW in src/fpl_ai/config.py
  2. Rebuild BOTH fixed-pipeline tables (docs/review_fixes_2026_10.md):
       FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python3 -m fpl_ai.cli \\
         build-training-table --history-root data/fpl_history \\
         --output data/fpl_training_rows_v3_contract_f6.csv    # decisions: classic+F6
       FPL_PRIOR_BLEND=1 PYTHONPATH=src python3 -m fpl_ai.cli \\
         build-training-table --history-root data/fpl_history \\
         --output data/fpl_training_rows_v3_contract.csv       # E11-full shadow baselines
     (Decisions come from classic+F6 since 2026-09-29; adapters run in shadow.
      E11-full was trained on non-F6 baselines, so its live corpus uses the
      classic table. The old blend*.csv tables are pre-fix: do not rebuild them.)
     (weekly_status.csv in each history season dir is picked up automatically: the pre-deadline
      status reconstructed from vaastav commits, scripts/backfill_history_status_from_vaastav.py)
  2b. Parity audit of the next GW's live frame vs history (a degenerate feature is a bug):
       FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 PYTHONPATH=src python3 scripts/train_live_parity_audit.py \
         --deadline-ts <next deadline> --out reports/gw<next>_packet_*/parity_audit.md
  3. Append the GW$GW result to reports/season_2627_ledger.jsonl
  4. Fresh article pull -> next GW corpus -> live decode -> sheet
     (EYEBALL the corpus baseline distribution before decoding: P(app) p90
      collapsing toward ~0.13 is the walk-forward cold-start bug.)
  5. Bench order is a REQUIRED output of the sheet, not an afterthought.
  6. Classic vs classic + SFT side by side, with the evidence behind each
     SFT move (scripts/sft_side_by_side.py). Wes asked for this every week.
     Include the SFT's average (scripts/expectation_decode.py on the squad and
     targets, then --expected-predictions): the written greedy deltas
     exaggerate cuts.
  7. Score last week's shadow forecasts once it settles (Wes, 2026-10-10:
     "track whether the SFT output is more accurate"):
       python3 scripts/track_sft_accuracy.py --labels-csv data/fpl_training_rows_v3_contract_f6.csv \
         --set "2026-27 GW$GW" <that week's examples> <E20 predictions> <E20 expectation predictions> \
         --out-md reports/sft_accuracy_gw$GW.md
     The expectation file must cover every row being scored (decode the full
     week, ~40 min merged, not just the squad subset).
  8. Chip line (Wes, 2026-10-12: "when would be the best time for chip usage"):
     after the live classic decode for GW$NEXT exists,
       FPL_GEN_DEVICE_MAP=gpu python3 scripts/live_chip_line.py --event $NEXT --tag gw${NEXT}final_2627 \
         --output reports/chip_line_gw$NEXT.md
     Shows the priced options, the planner rule and the G8 compact shadow. Both
     fire a chip as soon as this week looks as good as the next four, so treat
     "use now" as "nothing better in sight", not as a timing call.

EOF

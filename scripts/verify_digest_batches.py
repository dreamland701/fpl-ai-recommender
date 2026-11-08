#!/usr/bin/env python3
"""Verify Haiku digest batches: structure, order, and EFFORT.

Structure/order: every output row parses, counts match, keys align.
Effort guard (batch 021 lesson): an agent that fatigues mid-file emits
empty digests for fact-bearing articles. Flag a batch when (a) >30% of
rows are empty, or (b) ANY empty row's title matches an obviously
fact-bearing class (Ones to watch:, Differentials:, team news, bonus
points, Scout Selection, best captains, predicted lineups). Flagged
batches must be re-run — their outputs are renamed *.rejected.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

FACT_BEARING = re.compile(
    r"(ones to watch:|differentials?:|team news|bonus points|scout selection|"
    r"best captains|predicted lineups|price (rise|fall)|injur(y|ies) (list|update))",
    re.I,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-dir", default="reports/e12_digest_batches")
    parser.add_argument("--reject", action="store_true", help="Rename flagged outputs to *.rejected")
    args = parser.parse_args()

    batch_dir = Path(args.batch_dir)
    ok, flagged = [], []
    for path in sorted(batch_dir.glob("batch_*_output.jsonl")):
        batch_id = path.name.split("_")[1]
        input_path = batch_dir / f"batch_{batch_id}_input.jsonl"
        try:
            inp = [json.loads(l) for l in open(input_path)]
            out = [json.loads(l) for l in open(path)]
            assert len(out) == len(inp), f"count {len(out)}/{len(inp)}"
            assert [r["article_key"] for r in out] == [r["article_key"] for r in inp], "key order"
            empties, suspicious, facts = 0, [], 0
            for a, b in zip(inp, out):
                digest = b["digest"]
                if isinstance(digest, str):
                    digest = json.loads(digest)
                pf = digest.get("player_facts")
                assert isinstance(pf, list), "player_facts not a list"
                facts += len(pf)
                if not pf:
                    # Stub articles (aggregator link-outs with title-only
                    # bodies, ~70-130 chars) are legitimately blank — they
                    # carry no facts in ANY evidence regime. Only substantial
                    # articles count toward the effort guard.
                    body = a["article"].split("\n", 1)
                    substantial = len(body[1]) >= 300 if len(body) > 1 else False
                    if not substantial:
                        continue
                    empties += 1
                    # Instructional guides ("How to check FPL bonus points...")
                    # match the fact-bearing patterns but are legitimately
                    # fact-free — judged so twice independently in the pilot.
                    how_to = re.match(r"\s*how\b", a["title"], re.I)
                    if FACT_BEARING.search(a["title"]) and not how_to:
                        suspicious.append(a["title"][:70])
            if empties > 0.3 * len(inp) or suspicious:
                flagged.append((path, empties, len(inp), suspicious))
            else:
                ok.append((batch_id, facts, empties))
        except Exception as exc:
            flagged.append((path, -1, -1, [f"STRUCTURE: {exc}"]))

    total_facts = sum(f for _, f, _ in ok)
    print(f"OK batches: {len(ok)} | total player_facts: {total_facts} | flagged: {len(flagged)}")
    for path, empties, n, suspicious in flagged:
        print(f"FLAGGED {path.name}: {empties}/{n} empty; suspicious blanks:")
        for title in suspicious[:5]:
            print(f"   - {title}")
        if args.reject:
            path.rename(path.with_suffix(".jsonl.rejected"))
            print(f"   -> renamed to {path.name}.rejected (re-run this batch)")


if __name__ == "__main__":
    main()

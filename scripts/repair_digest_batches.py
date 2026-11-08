#!/usr/bin/env python3
"""Row-level repair for defective digest batches.

salvage: for every batch with an output (including *.rejected), parse each
line INDIVIDUALLY (a malformed line no longer poisons the file), rebuild the
output in input-key order, and write it back as the primary output when
complete. Rows that are missing, malformed, duplicated-away, or lazy-empty
(empty player_facts on a fact-bearing title) go to a repair manifest plus a
repair input file containing the full articles to re-digest.

splice: merge a repair output (JSONL {"article_key","digest"}) into the
reconstructed outputs, then finalize.

This converts a ~45% batch-defect rate (dropped rows, order scrambles, bad
JSON lines, fatigue empties) into a small row-repair stream instead of
re-running whole 25-article batches.
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


def load_rows(path: Path) -> list[dict]:
    rows = []
    for line in open(path):
        if line.strip():
            rows.append(json.loads(line))
    return rows


def salvage(batch_dir: Path) -> None:
    manifest, repair_articles = [], []
    for input_path in sorted(batch_dir.glob("batch_*_input.jsonl")):
        batch_id = input_path.name.split("_")[1]
        candidates = [
            batch_dir / f"batch_{batch_id}_output.jsonl",
            batch_dir / f"batch_{batch_id}_output.jsonl.rejected",
        ]
        existing = [p for p in candidates if p.exists()]
        if not existing:
            continue  # not attempted yet
        inp = load_rows(input_path)
        salvaged: dict[str, dict] = {}
        for path in existing:
            for line in open(path):
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                    digest = row["digest"]
                    if isinstance(digest, str):
                        digest = json.loads(digest)
                    assert isinstance(digest.get("player_facts"), list)
                except Exception:
                    continue
                key = row.get("article_key")
                if not key:
                    continue
                keep_new = key not in salvaged or (
                    not salvaged[key].get("player_facts") and digest.get("player_facts")
                )
                if keep_new:
                    salvaged[key] = digest
        needs_repair = []
        for row in inp:
            key = row["article_key"]
            digest = salvaged.get(key)
            # Lazy-empty logic must match verify_digest_batches.py exactly:
            # stub articles (title-only bodies <300 chars) and instructional
            # "How ..." titles are legitimately blank.
            body = row["article"].split("\n", 1)
            substantial = len(body[1]) >= 300 if len(body) > 1 else False
            how_to = re.match(r"\s*how\b", row["title"], re.I)
            lazy = (
                digest is not None
                and not digest.get("player_facts")
                and substantial
                and FACT_BEARING.search(row["title"])
                and not how_to
            )
            if digest is None or lazy:
                needs_repair.append(row)
        if needs_repair:
            partial = batch_dir / f"batch_{batch_id}_output.partial.jsonl"
            with open(partial, "w") as handle:
                for row in inp:
                    if row["article_key"] in salvaged:
                        handle.write(json.dumps({"article_key": row["article_key"], "digest": salvaged[row["article_key"]]}) + "\n")
            for row in needs_repair:
                manifest.append({"batch": batch_id, "article_key": row["article_key"], "title": row["title"]})
                repair_articles.append(row)
            primary = batch_dir / f"batch_{batch_id}_output.jsonl"
            if primary.exists():
                primary.rename(primary.with_suffix(".jsonl.rejected"))
        else:
            final = batch_dir / f"batch_{batch_id}_output.jsonl"
            with open(final, "w") as handle:
                for row in inp:
                    handle.write(json.dumps({"article_key": row["article_key"], "digest": salvaged[row["article_key"]]}) + "\n")
            for path in existing:
                if path.suffix == ".rejected":
                    path.unlink()
    with open(batch_dir / "repair_manifest.jsonl", "w") as handle:
        for entry in manifest:
            handle.write(json.dumps(entry) + "\n")
    with open(batch_dir / "repair_input.jsonl", "w") as handle:
        for row in repair_articles:
            handle.write(json.dumps(row) + "\n")
    print(f"repair rows needed: {len(manifest)} across {len({m['batch'] for m in manifest})} batches -> repair_input.jsonl")


def splice(batch_dir: Path, repairs_path: Path) -> None:
    repairs: dict[str, dict] = {}
    for line in open(repairs_path):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            digest = row["digest"]
            if isinstance(digest, str):
                digest = json.loads(digest)
            assert isinstance(digest.get("player_facts"), list)
            repairs[row["article_key"]] = digest
        except Exception:
            continue
    finalized = still_missing = 0
    for partial in sorted(batch_dir.glob("batch_*_output.partial.jsonl")):
        batch_id = partial.name.split("_")[1]
        inp = load_rows(batch_dir / f"batch_{batch_id}_input.jsonl")
        have = {r["article_key"]: r["digest"] for r in load_rows(partial)}
        have.update({k: v for k, v in repairs.items()})
        missing = [r for r in inp if r["article_key"] not in have]
        if missing:
            still_missing += len(missing)
            continue
        final = batch_dir / f"batch_{batch_id}_output.jsonl"
        with open(final, "w") as handle:
            for row in inp:
                handle.write(json.dumps({"article_key": row["article_key"], "digest": have[row["article_key"]]}) + "\n")
        partial.unlink()
        rejected = batch_dir / f"batch_{batch_id}_output.jsonl.rejected"
        if rejected.exists():
            rejected.unlink()
        finalized += 1
    print(f"finalized batches: {finalized}; rows still missing: {still_missing}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--stage", choices=["salvage", "splice"], required=True)
    parser.add_argument("--batch-dir", default="reports/e12_digest_batches")
    parser.add_argument("--repairs", help="splice: repair output JSONL")
    args = parser.parse_args()
    batch_dir = Path(args.batch_dir)
    if args.stage == "salvage":
        salvage(batch_dir)
    else:
        splice(batch_dir, Path(args.repairs))


if __name__ == "__main__":
    main()

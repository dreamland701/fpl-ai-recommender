#!/usr/bin/env python3
"""E12 stage 1: route Type-B (list/table) articles and build digest prompts.

One digest prompt per unique list-type article across every evidence file
used in training + live. The prompt template is the pilot-validated one
(reports/article_digest_pilot_prompts.jsonl — Krafth case: 40 facts +
team notes). Type-A narrative articles are untouched (keep windows).
Router misses degrade to the status quo (windows), so the heuristic only
needs precision on what it flags, not perfect recall.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

EVIDENCE_FILES = [
    "reports/evidence_guardian_football_2022_23.jsonl",
    "reports/evidence_guardian_football_2023_24.jsonl",
    "reports/evidence_guardian_football_2024_25.jsonl",
    "reports/evidence_guardian_football_2025_26.jsonl",
    "reports/evidence_2025_26_gw1_30_v4_pl_fulltext_decoded.jsonl",
    "reports/evidence_pl_scout_2022_26.jsonl",
    "reports/evidence_guardian_football_2026_prelaunch.jsonl",
    "reports/evidence_pl_scout_2026_prelaunch.jsonl",
    "reports/evidence_guardian_football_2627_gw2.jsonl",
    "reports/evidence_pl_scout_2627_gw2.jsonl",
]

LIST_TITLE = re.compile(
    r"(team news|predicted lineups?|talking points|price (rise|fall|change)|"
    r"injur(y|ies) (list|round|update)|lessons from|transfer radar|squad for|"
    r"best.*picks|captain.*for|scout selection|deadline day|tips|"
    r"who could|ones to watch|differentials|bonus points?|defensive contribution)",
    re.I,
)

ARTICLE_CHARS_CAP = 12000

INSTRUCTION = (
    "\n\nRead the whole article once and produce a structured digest as STRICT JSON only (no prose):\n"
    '{"article_type": "team_news"|"prices"|"stats_roundup"|"analysis", '
    '"summary": "<one sentence, max 200 chars>", '
    '"player_facts": [{"player": "<name exactly as written>", "team": "<team if stated>", '
    '"fact": "<max 120 chars, from the text only>"}], '
    '"team_notes": [{"team": "<team>", "note": "<max 120 chars>"}]}\n'
    "Include EVERY player for whom the article states a status, injury, doubt, predicted "
    "start/omission, price, or points fact — including facts inside lists and tables like "
    "'Krafth (knee, Jun)' meaning injured until June. Do not invent players or facts. "
    "Cap player_facts at 40 entries."
)


def is_type_b(title: str, content: str) -> bool:
    if LIST_TITLE.search(title or ""):
        return True
    table_like = content.count("|") > 20 or len(re.findall(r"£\d", content)) > 15
    return table_like


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/e12_digest_prompts.jsonl")
    parser.add_argument("--batch-dir", default="reports/e12_digest_batches")
    parser.add_argument("--batch-size", type=int, default=25)
    args = parser.parse_args()

    best: dict[str, dict] = {}
    for path in EVIDENCE_FILES:
        if not Path(path).exists():
            print(f"MISSING {path}")
            continue
        for line in open(path):
            doc = json.loads(line)
            title = str(doc.get("title") or "")
            published = str(doc.get("published_at") or doc.get("published_ts") or "")
            content = str(doc.get("content") or "")
            if not title or not content:
                continue
            if not is_type_b(title, content):
                continue
            key = hashlib.sha1(f"{title}|{published[:10]}".encode()).hexdigest()[:16]
            if key in best and len(best[key]["content"]) >= len(content):
                continue
            best[key] = {
                "article_key": key,
                "title": title,
                "published_at": published,
                "source_name": str(doc.get("source_name") or doc.get("source") or "unknown"),
                "source_file": path,
                "content": content,
            }

    rows = sorted(best.values(), key=lambda r: (r["published_at"], r["article_key"]))
    with open(args.output, "w") as handle:
        for row in rows:
            prompt = (
                f"Article ({row['source_name']}, {row['published_at']}): {row['title']}\n"
                f"{row['content'][:ARTICLE_CHARS_CAP]}"
                f"{INSTRUCTION}"
            )
            handle.write(json.dumps({
                "article_key": row["article_key"],
                "title": row["title"],
                "published_at": row["published_at"],
                "source_file": row["source_file"],
                "prompt": prompt,
            }) + "\n")

    batch_dir = Path(args.batch_dir)
    batch_dir.mkdir(exist_ok=True)
    for index in range(0, len(rows), args.batch_size):
        batch_id = index // args.batch_size
        with open(batch_dir / f"batch_{batch_id:03d}_input.jsonl", "w") as handle:
            for row in rows[index:index + args.batch_size]:
                handle.write(json.dumps({
                    "article_key": row["article_key"],
                    "title": row["title"],
                    "published_at": row["published_at"],
                    "article": f"({row['source_name']}, {row['published_at']}): {row['title']}\n{row['content'][:ARTICLE_CHARS_CAP]}",
                }) + "\n")
    n_batches = (len(rows) + args.batch_size - 1) // args.batch_size
    print(f"{len(rows)} unique Type-B articles -> {args.output}; {n_batches} batch inputs in {batch_dir}/")


if __name__ == "__main__":
    main()

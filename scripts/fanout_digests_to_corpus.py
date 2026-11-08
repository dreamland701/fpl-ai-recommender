#!/usr/bin/env python3
"""E12 stage 2: fan digest outputs into per-player mini-docs + filtered originals.

Consumes the Haiku digest batches (reports/e12_digest_batches/batch_*_output.jsonl)
and produces the E12 evidence layer:
  - reports/e12_evidence/<original-name>          (originals minus Type-B articles)
  - reports/e12_evidence/evidence_e12_typeB_minidocs.jsonl

Each player_fact becomes one mini-doc: same title/published_at (chrono-legality
inherited), unique url fragment (the attach script dedupes on url+ts+title),
content = digest summary + the player's fact + their team's note when present.
The existing attach script then matches mini-docs to players exactly as it
matches raw articles (name-in-content), so the ONLY variable that changes in
E12 is the text a player sees from list-type articles: their distilled fact
instead of a mention-centered window (or, more often, instead of nothing).
Team notes reach only players NAMED in the article in this version — roster
resolution across historical weeks is deliberately out of scope for E12.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from build_article_digest_prompts import EVIDENCE_FILES  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-dir", default="reports/e12_digest_batches")
    parser.add_argument("--prompts", default="reports/e12_digest_prompts.jsonl")
    parser.add_argument("--output-dir", default="reports/e12_evidence")
    args = parser.parse_args()

    meta = {json.loads(l)["article_key"]: json.loads(l) for l in open(args.prompts)}

    digests: dict[str, dict] = {}
    parse_failures = 0
    for path in sorted(Path(args.batch_dir).glob("batch_*_output.jsonl")):
        for line in open(path):
            try:
                row = json.loads(line)
                digest = row["digest"]
                if isinstance(digest, str):
                    digest = json.loads(digest)
                assert isinstance(digest.get("player_facts"), list)
                digests[row["article_key"]] = digest
            except Exception:
                parse_failures += 1

    out_dir = Path(args.output_dir)
    out_dir.mkdir(exist_ok=True)

    # Type-B article identity (title, date) -> key, to strip them from originals
    typeb_by_title_date = {
        (m["title"], str(m["published_at"])[:10]): key for key, m in meta.items()
    }

    minidocs = []
    covered_articles = 0
    for key, digest in digests.items():
        m = meta.get(key)
        if m is None:
            continue
        covered_articles += 1
        summary = str(digest.get("summary") or "")
        notes_by_team = {}
        for note in digest.get("team_notes") or []:
            team = str(note.get("team") or "").strip()
            if team:
                notes_by_team.setdefault(team, []).append(str(note.get("note") or ""))
        for index, fact in enumerate(digest.get("player_facts") or []):
            player = str(fact.get("player") or "").strip()
            fact_text = str(fact.get("fact") or "").strip()
            if not player or not fact_text:
                continue
            team = str(fact.get("team") or "").strip()
            note_txt = ""
            if team and team in notes_by_team:
                note_txt = " Team note (" + team + "): " + "; ".join(notes_by_team[team])
            minidocs.append({
                "title": m["title"],
                "url": f"digest://{key}#pf{index}",
                "published_at": m["published_at"],
                "source_name": "digest:" + str(m.get("source_file", "")).split("/")[-1],
                "category": "digest",
                "content": f"{summary} {player}: {fact_text}.{note_txt}",
            })

    with open(out_dir / "evidence_e12_typeB_minidocs.jsonl", "w") as handle:
        for doc in minidocs:
            handle.write(json.dumps(doc) + "\n")

    stripped_total = 0
    for path in EVIDENCE_FILES:
        source = Path(path)
        if not source.exists():
            continue
        kept, stripped = [], 0
        for line in open(source):
            doc = json.loads(line)
            title = str(doc.get("title") or "")
            date = str(doc.get("published_at") or doc.get("published_ts") or "")[:10]
            key = typeb_by_title_date.get((title, date))
            if key is not None and key in digests:
                stripped += 1  # replaced by its mini-docs
                continue
            kept.append(line)
        stripped_total += stripped
        with open(out_dir / source.name, "w") as handle:
            handle.writelines(kept)
        print(f"{source.name}: kept {len(kept)}, replaced-by-digest {stripped}")

    print(
        f"digested articles: {covered_articles}/{len(meta)} | mini-docs: {len(minidocs)} | "
        f"digest parse failures: {parse_failures} | Type-B stripped from originals: {stripped_total}"
    )
    if covered_articles < len(meta):
        missing = len(meta) - covered_articles
        print(f"WARNING: {missing} Type-B articles have no digest yet — they stay in originals only if their batch is missing; rerun after all batches land")


if __name__ == "__main__":
    main()

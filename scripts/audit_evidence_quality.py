#!/usr/bin/env python3
"""Audit the evidence text actually fed to the forecast adapter.

Wes's standing concern (2026-08-21): are we using enough articles, are
they long enough, and do the windows carry real information — not just
titles? This measures, for any examples/eval/train JSONL whose prompts
contain the standard "Timestamp-safe text evidence:" block:

- coverage: rows with >=1 evidence document
- docs per row
- evidence characters per document actually IN the prompt (the windowed
  text, not the source), flagging "title-only" docs (no body text beyond
  the header line)
- where resolvable against the source evidence JSONLs: the full source
  article length and the fraction the prompt window shows

Usage:
  PYTHONPATH=src python3 scripts/audit_evidence_quality.py \
    --examples <split_dir>/train.jsonl [--sample 3] \
    [--source-evidence reports/evidence_*.jsonl ...]
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
from pathlib import Path

DOC_HEADER = re.compile(r"^\[(\d+)\] (.+?) \| (\d{4})", re.MULTILINE)
EVIDENCE_BLOCK = re.compile(r"Timestamp-safe text evidence:\n(.*?)(?:\n<\|turn>|\Z)", re.DOTALL)
TITLE_LINE = re.compile(r"^Title: (.*)$", re.MULTILINE)


def parse_docs(prompt: str) -> list[dict]:
    match = EVIDENCE_BLOCK.search(prompt)
    if not match:
        return []
    block = match.group(1)
    if "no relevant evidence" in block.lower() or not block.strip():
        return []
    headers = list(DOC_HEADER.finditer(block))
    docs = []
    for i, h in enumerate(headers):
        end = headers[i + 1].start() if i + 1 < len(headers) else len(block)
        chunk = block[h.start():end]
        title_match = TITLE_LINE.search(chunk)
        title = title_match.group(1).strip() if title_match else ""
        body = chunk[title_match.end():].strip() if title_match else chunk
        body = re.sub(r"^Text:\s*", "", body).strip()
        docs.append({"source": h.group(2), "year": h.group(3), "title": title, "body_chars": len(body), "body": body})
    return docs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examples", required=True)
    parser.add_argument("--source-evidence", nargs="*", default=[])
    parser.add_argument("--sample", type=int, default=0, help="Print N sample evidence windows for eyeballing.")
    args = parser.parse_args()

    source_len_by_title: dict[str, int] = {}
    for path in args.source_evidence:
        for line in Path(path).open():
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            title = str(row.get("title") or "").strip()
            content = str(row.get("full_text") or row.get("content") or "")
            year = str(row.get("published_at") or "")[:4]
            if title:
                # Key by (title, publication year): annual series (e.g. the
                # Scout's "Quick Fantasy tips: ... Gameweek 1") reuse titles
                # verbatim every season — title-only keying silently matched
                # a different year's edition (caught 2026-08-22: reported a
                # window as 39% of a 2,046-char 2024-25 edition when it was
                # really 93.5% of the 858-char 2025-26 one).
                key = (title, year)
                source_len_by_title[key] = max(source_len_by_title.get(key, 0), len(content))

    n_rows = 0
    rows_with_ev = 0
    docs_per_row: list[int] = []
    body_chars: list[int] = []
    title_only = 0
    shown_fractions: list[float] = []
    samples: list[str] = []
    per_source: dict[str, int] = {}

    for line in Path(args.examples).open():
        row = json.loads(line)
        prompt = row.get("prompt") or ""
        docs = parse_docs(prompt)
        n_rows += 1
        if docs:
            rows_with_ev += 1
            docs_per_row.append(len(docs))
        for doc in docs:
            body_chars.append(doc["body_chars"])
            per_source[doc["source"]] = per_source.get(doc["source"], 0) + 1
            if doc["body_chars"] < 40:
                title_only += 1
            src_len = source_len_by_title.get((doc["title"], doc.get("year", "")))
            if src_len:
                shown_fractions.append(min(1.0, doc["body_chars"] / max(src_len, 1)))
            if args.sample and len(samples) < args.sample and doc["body_chars"] > 0:
                samples.append(f"--- [{doc['source']}] {doc['title'][:80]}\n{doc['body'][:400]}")

    def dist(vals, label, unit=""):
        if not vals:
            print(f"{label}: none")
            return
        qs = statistics.quantiles(vals, n=4)
        print(f"{label}: n={len(vals)} min={min(vals):.0f} p25={qs[0]:.0f} median={qs[1]:.0f} p75={qs[2]:.0f} max={max(vals):.0f}{unit}")

    print(f"rows: {n_rows} | with evidence: {rows_with_ev} ({rows_with_ev / max(n_rows,1):.1%})")
    dist(docs_per_row, "docs per evidence row")
    dist(body_chars, "prompt-window body chars per doc")
    print(f"title-only docs (<40 body chars): {title_only} / {len(body_chars)} ({title_only / max(len(body_chars),1):.1%})")
    if shown_fractions:
        dist([f * 100 for f in shown_fractions], "percent of source article shown", unit="%")
        print(f"(source lengths resolved for {len(shown_fractions)} / {len(body_chars)} docs)")
    print("docs by source:", dict(sorted(per_source.items(), key=lambda kv: -kv[1])))
    for s in samples:
        print()
        print(s)


if __name__ == "__main__":
    main()

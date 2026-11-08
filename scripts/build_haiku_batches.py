#!/usr/bin/env python3
"""Write per-document prompt files for Haiku subagent extraction workers (2026-10-23, the zero-API-cost arm of the
availability-fact backfill): the same prompt the 31B extractor sees (scripts/extract_availability_facts.py, v2, article
capped at --max-chars), one file per document, lines wrapped to <= --wrap chars (the subagent's Read tool truncates
longer lines), grouped --per-batch files per worker directory. A worker reads <stem>.prompt.txt and writes
<stem>.out.json; scripts/score_extract_pilot.py merge_haiku() turns a finished tree into one jsonl of facts.

usage: build_haiku_batches.py --docs reports/extract_facts/docs_avail.jsonl --out reports/extract_facts/haiku_backfill
         [--per-batch 12] [--max-chars 5000] [--prompt-version v2] [--wrap 1000]
"""
from __future__ import annotations
import argparse
import json
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_availability_facts import build_prompt  # noqa: E402


def wrap(text: str, width: int) -> str:
    out = []
    for line in text.split("\n"):
        if len(line) <= width:
            out.append(line)
        else:
            out.extend(textwrap.wrap(line, width, break_long_words=False, break_on_hyphens=False) or [""])
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--per-batch", type=int, default=12); ap.add_argument("--max-chars", type=int, default=5000)
    ap.add_argument("--prompt-version", default="v2"); ap.add_argument("--wrap", type=int, default=1000)
    args = ap.parse_args()
    docs = [json.loads(l) for l in open(args.docs)]
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for b in range(0, len(docs), args.per_batch):
        bi = b // args.per_batch; bdir = out / f"batch_{bi:03d}"; bdir.mkdir(exist_ok=True)
        names = []
        for k, d in enumerate(docs[b:b + args.per_batch]):
            stem = f"{bi:03d}_{k:02d}_{d['doc_id']}"
            p = bdir / f"{stem}.prompt.txt"
            if not p.exists():
                p.write_text(wrap(build_prompt(d, max_chars=args.max_chars, version=args.prompt_version), args.wrap))
            names.append(f"{stem}.prompt.txt")
        manifest[bdir.name] = names
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1))
    longest = max(len(l) for bdir in out.glob("batch_*") for p in bdir.glob("*.prompt.txt") for l in p.read_text().split("\n"))
    print(f"{len(docs)} docs -> {len(manifest)} batches of <= {args.per_batch} in {out} (longest line {longest} chars)")


if __name__ == "__main__":
    main()

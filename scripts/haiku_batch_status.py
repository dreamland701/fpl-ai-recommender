#!/usr/bin/env python3
"""Status of a Haiku worker tree (scripts/build_haiku_batches.py layout): per batch, prompt files, outputs written,
outputs that parse (scripts/extract_availability_facts.py parse_facts) and the names still missing or unparsable.
usage: haiku_batch_status.py <dir> [--batches 000-007] [--names]   (exit code 1 while anything is missing in the range)"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_availability_facts import parse_facts  # noqa: E402

ap = argparse.ArgumentParser(); ap.add_argument("dir"); ap.add_argument("--batches", default=None); ap.add_argument("--names", action="store_true")
a = ap.parse_args()
root = Path(a.dir); manifest = json.load(open(root / "manifest.json"))
lo, hi = (a.batches.split("-") + [None])[:2] if a.batches else (None, None)
tot = {"prompts": 0, "written": 0, "ok": 0, "facts": 0}; bad_all = []
for bname, names in sorted(manifest.items()):
    bi = bname.split("_")[1]
    if lo is not None and not (lo <= bi <= (hi or lo)):
        continue
    written = ok = facts = 0; bad = []
    for n in names:
        o = root / bname / n.replace(".prompt.txt", ".out.json")
        if not o.exists():
            bad.append(n); continue
        written += 1
        fl, good = parse_facts(o.read_text())
        if good:
            ok += 1; facts += len(fl)
        else:
            bad.append(n + " (unparsable)")
    tot["prompts"] += len(names); tot["written"] += written; tot["ok"] += ok; tot["facts"] += facts; bad_all += [f"{bname}/{b}" for b in bad]
    flag = "" if not bad else f"  MISSING {len(bad)}" + (": " + ", ".join(bad) if a.names else "")
    print(f"{bname}: {len(names)} prompts, {written} written, {ok} parse ok, {facts} facts{flag}")
print(f"TOTAL: {tot['prompts']} prompts, {tot['written']} written, {tot['ok']} parse ok, {tot['facts']} facts, {len(bad_all)} to redo")
sys.exit(1 if bad_all else 0)

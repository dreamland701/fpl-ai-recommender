#!/usr/bin/env python3
"""Keep the rows where availability is uncertain (classic P(appear) in [0.15, 0.95]) from a residual split file,
optionally capped by a seeded random sample (train). Rows below 0.15 are non-squad players, rows above 0.95 are
certain starters: neither moves a decision through the availability channel. (H3, 2026-10-15)
usage: filter_split_rows.py <in.jsonl> <out.jsonl> --mode train|eval [--cap N] [--seed S] [--lo 0.15] [--hi 0.95]"""
import argparse, json, random
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("src"); ap.add_argument("dst"); ap.add_argument("--mode", choices=["train", "eval"], required=True)
ap.add_argument("--cap", type=int, default=0); ap.add_argument("--seed", type=int, default=7)
ap.add_argument("--lo", type=float, default=0.15); ap.add_argument("--hi", type=float, default=0.95)
a = ap.parse_args()
keep, n, played, flagged, news, ev = [], 0, 0, 0, 0, 0
for line in open(a.src):
    if not line.strip():
        continue
    n += 1; r = json.loads(line); m = r["metadata"]; p = m["baseline_forecast"].get("baseline_appearance_probability")
    if p is None or not (a.lo <= float(p) <= a.hi):
        continue
    keep.append(line)
if a.mode == "train" and a.cap > 0 and len(keep) > a.cap:
    random.Random(a.seed).shuffle(keep); keep = keep[:a.cap]
for line in keep:
    r = json.loads(line); m = r["metadata"]; pr = r["prompt"]
    played += m["labels"]["minutes_1gw"] > 0
    st = pr.split("Status pre-deadline: ", 1)[1].split("\n", 1)[0].strip() if "Status pre-deadline: " in pr else "?"
    flagged += st not in ("a", "none", "?"); news += "Official player news pre-deadline: none" not in pr; ev += bool(m.get("evidence_present"))
Path(a.dst).parent.mkdir(parents=True, exist_ok=True)
with open(a.dst, "w") as f:
    f.writelines(keep)
k = max(len(keep), 1)
print(f"{a.src}: {n} rows -> {len(keep)} kept ({a.mode}, P in [{a.lo},{a.hi}], cap {a.cap}); played {played / k:.3f}, flagged status {flagged / k:.3f}, news {news / k:.3f}, evidence {ev / k:.3f}")

#!/usr/bin/env python3
"""Backfill pre-deadline status/news into the live season's merged_gw.csv.

WHY THIS EXISTS (2026-09-18)
----------------------------
The weekly sync-history ingestion writes ``status='a'`` and an empty ``news``
for every 2026-27 row. Verified: all 2,549 rows carry status 'a', including
Saliba, who has been injured with 0 minutes for four straight gameweeks. The
consequence is that ``status_flag_pre_deadline`` is identically 0.0 for the
live season, while the seven historical seasons run 19-38% flagged. So:

  * the anchor's injury flag is dead exactly when it matters (in-season),
  * the F7 depth-chart features cannot see who is unavailable,
  * the approved in-season incremental training would learn from rows in
    which nobody is ever injured.

We cannot re-query past snapshots from the FPL API, but we archived the real
pre-deadline snapshot ourselves every week in
``reports/live_gw{N}_{season}_corpus_bare.jsonl``. Each record's metadata
carries ``status_pre_deadline``/``news_pre_deadline`` as read at that week's
deadline, so restoring from it is chrono-legal by construction: the value was
observed BEFORE the gameweek it is written onto.

Idempotent. Only fills the target season's rows; other seasons untouched.
"""

from __future__ import annotations

import argparse
import csv
import glob
import json
import os
import shutil
from pathlib import Path


def load_corpus_status(season: str, reports_dir: Path) -> dict:
    """(week, player_id) -> (status, news) from archived pre-deadline corpora."""
    out: dict[tuple[int, int], tuple[str, str]] = {}
    # 2026-10-26: since GW6 the weekly refresh names its snapshots live_gw{N}{interim|final}_{season}_{classic|f6}_corpus_bare.jsonl,
    # which the old exact pattern (live_gw{N}_{season}_corpus_bare.jsonl) missed, so GW7 and GW8 rows stayed status 'a'
    # (the aggregate verify gate passed on the earlier weeks). Match every bare snapshot of the season and apply them in
    # modification-time order, so the latest pre-deadline snapshot of a week (the Friday final) wins over an interim one.
    short = season[2:4] + season[5:7]  # 2026-27 -> 2627 (the files use the short form)
    patterns = [str(reports_dir / f"live_gw*_{season.replace('-', '')}*corpus_bare*.jsonl"),
                str(reports_dir / f"live_gw*_{short}*corpus_bare*.jsonl")]
    files = sorted({f for pat in patterns for f in glob.glob(pat)}, key=os.path.getmtime)
    for path in files:
        for line in open(path):
            try:
                meta = json.loads(line)["metadata"]
            except Exception:
                continue
            week = meta.get("week")
            pid = meta.get("player_id")
            if week is None or pid is None:
                continue
            out[(int(week), int(pid))] = (
                str(meta.get("status_pre_deadline") or "a"),
                str(meta.get("news_pre_deadline") or ""),
            )
    return out, files


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--history-root", default="data/fpl_history")
    ap.add_argument("--reports-dir", default="reports")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    merged = Path(args.history_root) / args.season / "merged_gw.csv"
    if not merged.exists():
        print(f"no merged_gw.csv at {merged}")
        return 1

    status_map, files = load_corpus_status(args.season, Path(args.reports_dir))
    if not status_map:
        print("no archived corpora found; nothing to backfill")
        return 1
    print(f"loaded {len(status_map):,} pre-deadline status records from {len(files)} corpora")
    for f in files:
        print(f"  corpus (applied in this order, later wins): {os.path.basename(f)}")
    weeks = sorted({w for w, _ in status_map})
    print(f"  weeks covered: {weeks}")

    rows = list(csv.DictReader(open(merged)))
    if not rows:
        print("merged_gw.csv is empty")
        return 1
    fieldnames = list(rows[0].keys())
    for col in ("status", "news"):
        if col not in fieldnames:
            fieldnames.append(col)

    filled = 0
    changed = 0
    missing = 0
    for row in rows:
        try:
            key = (int(row["round"]), int(row["element"]))
        except (KeyError, ValueError, TypeError):
            missing += 1
            continue
        hit = status_map.get(key)
        if hit is None:
            missing += 1
            continue
        status, news = hit
        if row.get("status") != status or (row.get("news") or "") != news:
            changed += 1
        row["status"] = status
        row["news"] = news
        filled += 1

    from collections import Counter

    dist = Counter(r.get("status", "?") for r in rows)
    print(f"rows: {len(rows):,}  filled: {filled:,}  changed: {changed:,}  unmatched: {missing:,}")
    print(f"resulting status distribution: {dict(dist)}")

    if args.dry_run:
        print("--dry-run: not writing")
        return 0

    backup = merged.with_suffix(".csv.prestatus")
    if not backup.exists():
        shutil.copy2(merged, backup)
        print(f"backup written to {backup}")

    tmp = merged.with_suffix(".csv.tmp")
    with open(tmp, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    os.replace(tmp, merged)
    print(f"wrote {merged}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Reconstruct weekly PRE-DEADLINE player status/news for past seasons from the vaastav data repository's
commit history (2026-10-14).

Why: the October review fix stopped copying players_raw.csv's end-of-season status onto every week (a
leak), but nothing replaced it, so status_flag_pre_deadline is 0.0 on every row of 2019-20..2025-26 and
the model learns the official injury flag from the live season alone (66 flagged regular rows, while
flagged regulars play 39% vs 93%). vaastav committed players_raw.csv roughly weekly, so the last commit
BEFORE each gameweek's deadline is a pre-deadline snapshot of status, news and chance_of_playing.

usage: backfill_history_status_from_vaastav.py --repo <blob-less clone> --history-root data/fpl_history \
         --seasons 2019-20 2020-21 2021-22 2022-23 2023-24 2024-25 2025-26 [--deadline-margin-min 90]
Writes data/fpl_history/<season>/weekly_status.csv: week, player_id, status, news, chance_next,
snapshot_ts, age_hours (hours between the snapshot commit and the deadline).
"""
from __future__ import annotations

import argparse
import io
import subprocess
from datetime import timedelta
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def commits_for(repo: Path, path: str) -> list[tuple[str, pd.Timestamp]]:
    out = subprocess.run(["git", "-C", str(repo), "log", "--format=%H %cI", "--", path], capture_output=True, text=True, check=True).stdout
    rows = []
    for line in out.splitlines():
        sha, ts = line.split()
        rows.append((sha, pd.Timestamp(ts).tz_convert("UTC")))
    return sorted(rows, key=lambda r: r[1])


def show(repo: Path, sha: str, path: str) -> pd.DataFrame:
    raw = subprocess.run(["git", "-C", str(repo), "show", f"{sha}:{path}"], capture_output=True, check=True).stdout
    frame = pd.read_csv(io.BytesIO(raw), low_memory=False)
    keep = {"id": "player_id", "status": "status", "news": "news", "chance_of_playing_next_round": "chance_next"}
    keep.update(EXTRA_COLUMNS)
    frame = frame[[c for c in keep if c in frame.columns]].rename(columns=keep)
    return frame


# Programme item 4 (2026-10-17): set-piece duties are in the same snapshots (columns exist from 2020-21).
SETPIECE_COLUMNS = {"penalties_order": "pen_order", "corners_and_indirect_freekicks_order": "corner_order",
                    "direct_freekicks_order": "fk_order"}
EXTRA_COLUMNS: dict = {}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--history-root", default=str(ROOT / "data/fpl_history"))
    ap.add_argument("--seasons", nargs="+", default=["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26"])
    ap.add_argument("--deadline-margin-min", type=int, default=90, help="deadline = first kickoff minus this")
    ap.add_argument("--max-age-days", type=float, default=10.0, help="older snapshots are treated as unknown")
    ap.add_argument("--setpiece", action="store_true", help="also capture penalty / corner / free-kick order (item 4)")
    ap.add_argument("--out-name", default="weekly_status.csv", help="output file name inside each season directory")
    args = ap.parse_args()
    repo = Path(args.repo)
    if args.setpiece:
        EXTRA_COLUMNS.update(SETPIECE_COLUMNS)
    for season in args.seasons:
        path = f"data/{season}/players_raw.csv"
        commits = commits_for(repo, path)
        if not commits:
            print(f"{season}: no commits for {path}"); continue
        fixtures = pd.read_csv(Path(args.history_root) / season / "fixtures.csv").dropna(subset=["kickoff_time", "event"])
        fixtures["kickoff"] = pd.to_datetime(fixtures["kickoff_time"], utc=True)
        deadlines = fixtures.groupby("event")["kickoff"].min() - timedelta(minutes=args.deadline_margin_min)
        cache: dict[str, pd.DataFrame] = {}
        rows, ages, missing = [], [], []
        for week, deadline in deadlines.items():
            before = [c for c in commits if c[1] < deadline]
            if not before:
                missing.append(int(week)); continue
            sha, ts = before[-1]
            age_h = (deadline - ts).total_seconds() / 3600.0
            if age_h > args.max_age_days * 24:
                missing.append(int(week)); continue
            if sha not in cache:
                cache[sha] = show(repo, sha, path)
            snap = cache[sha].copy()
            snap["week"] = int(week); snap["snapshot_ts"] = ts.isoformat(); snap["age_hours"] = round(age_h, 1)
            rows.append(snap); ages.append(age_h)
        out = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
        out_path = Path(args.history_root) / season / args.out_name
        out.to_csv(out_path, index=False)
        flagged = (out["status"].astype(str).str.lower() != "a").mean() if len(out) else float("nan")
        print(f"{season}: {len(deadlines)} gameweeks, {len(deadlines) - len(missing)} with a pre-deadline snapshot "
              f"(median age {pd.Series(ages).median():.0f} h, max {max(ages):.0f} h), {len(cache)} distinct commits, "
              f"flagged share {flagged:.3f}, missing weeks {missing} -> {out_path}")


if __name__ == "__main__":
    main()

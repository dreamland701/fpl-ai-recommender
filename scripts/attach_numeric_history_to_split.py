#!/usr/bin/env python3
"""H6 (2026-10-28): add a compact NUMERIC HISTORY block to each prompt of a residual split. Diagnosis behind it: the E22/H
prompts carry only the classic's five baseline numbers, status/news, fixtures, congestion, team sheet and two articles; no
week-by-week minutes/points, no xG, no prior-season record, so an injury blank three games ago (Isak GW6) or a rotation
profile (Calafiori) is invisible to the adapter, and H1/H5 deltas are flat across minutes bands where the classic is
18 min / +0.37 pts wrong on returners. The block (from the production table, keyed on `code` for prior seasons) is
inserted before "Timestamp-safe text evidence:" so compact_prompt keeps it. Idempotent per row (skips rows that already
carry the block). usage: attach_numeric_history_to_split.py --split <dir> --out <dir> [--table ...] [--prior-table ...]"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

MARKER = "Timestamp-safe text evidence:"
HEADER = "Numeric history (this season, oldest to newest; min/pts per gameweek; flag = official status at that deadline):"
COLS = ["season", "week", "player_id", "code", "fixture_count", "observed_minutes", "observed_starts", "observed_points",
        "status_pre_deadline", "expected_goals_avg_5", "expected_assists_avg_5", "minutes_avg_5", "price_pre_deadline"]


def fmt(x, nd=2):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{x:.{nd}f}"


def build_blocks(table: str, prior_table: str | None, keys: set[tuple[str, int, int]]) -> dict[tuple[str, int, int], str]:
    t = pd.read_csv(table, low_memory=False, usecols=COLS)
    t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    prior = None
    if prior_table and Path(prior_table).exists():
        prior = pd.read_csv(prior_table, low_memory=False, usecols=["season", "week", "player_id", "prior_pl_games", "no_prior_pl_season", "prior_start_share", "prior_minutes_share"])
        prior = prior.set_index(["season", "week", "player_id"])
    seasons = sorted(t["season"].unique())
    t = t.sort_values(["season", "player_id", "week"])
    grouped = {k: g for k, g in t.groupby(["season", "player_id"], sort=False)}
    # prior-season record keyed on code (fallback when the prior table is absent)
    played = t[t["fixture_count"] > 0]
    agg = played.groupby(["code", "season"]).agg(games=("week", "size"), starts=("observed_starts", "sum"), minutes=("observed_minutes", "sum"), points=("observed_points", "sum"))
    blocks = {}
    for season, week, pid in keys:
        g = grouped.get((season, pid))
        if g is None:
            continue
        hist = g[(g["week"] < week)]
        row = g[g["week"] == week]
        parts = []
        for r in hist.tail(8).itertuples():
            if r.fixture_count == 0:
                parts.append(f"GW{int(r.week)} blank")
                continue
            flag = "" if (pd.isna(r.status_pre_deadline) or r.status_pre_deadline == "a") else f" ({r.status_pre_deadline})"
            parts.append(f"GW{int(r.week)} {int(r.observed_minutes)}/{int(r.observed_points)}{flag}")
        lines = [HEADER, "- " + ("; ".join(parts) if parts else "no gameweeks played yet this season")]
        hp = hist[hist["fixture_count"] > 0]
        if len(hp):
            lines.append(f"- Season so far: {int(hp.observed_starts.sum())} starts in {len(hp)} team games, {int(hp.observed_minutes.sum())} min, {int(hp.observed_points.sum())} pts, "
                         f"{int((hp.observed_minutes == 0).sum())} no-shows; last-5 per game xG {fmt(float(row.expected_goals_avg_5.iloc[0]) if len(row) else float('nan'))}, "
                         f"xA {fmt(float(row.expected_assists_avg_5.iloc[0]) if len(row) else float('nan'))}")
        code = row["code"].iloc[0] if len(row) and not pd.isna(row["code"].iloc[0]) else None
        prev = seasons[seasons.index(season) - 1] if season in seasons and seasons.index(season) > 0 else None
        ptxt = None
        if prior is not None and (season, week, pid) in prior.index:
            p = prior.loc[(season, week, pid)]
            if isinstance(p, pd.DataFrame):
                p = p.iloc[0]
            if float(p.get("no_prior_pl_season", 0) or 0) >= 1:
                ptxt = "no Premier League season last year (promoted/new signing)"
            elif not pd.isna(p.get("prior_start_share")):
                ptxt = f"started {100 * float(p.prior_start_share):.0f}% of last season's team games ({100 * float(p.prior_minutes_share):.0f}% of minutes, {int(p.prior_pl_games)} games)"
        if ptxt is None and code is not None and prev is not None and (code, prev) in agg.index:
            a = agg.loc[(code, prev)]
            ptxt = f"{int(a.starts)} starts in {int(a.games)} team games, {int(a.minutes)} min, {int(a.points)} pts"
        lines.append(f"- Prior season ({prev or 'n/a'}): {ptxt or 'no Premier League record'}")
        blocks[(season, week, pid)] = "\n".join(lines)
    return blocks


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--table", default="data/fpl_training_rows_v3_contract_f6.csv")
    ap.add_argument("--prior-table", default="data/fpl_training_rows_v3_contract_f6_prior.csv")
    args = ap.parse_args()
    src, out = Path(args.split), Path(args.out); out.mkdir(parents=True, exist_ok=True)
    files = [p for p in ("train.jsonl", "eval.jsonl") if (src / p).exists()]
    rows = {p: [json.loads(l) for l in open(src / p) if l.strip()] for p in files}
    keys = {(r["metadata"]["season"], int(r["week"]), int(r["metadata"]["player_id"])) for rs in rows.values() for r in rs}
    blocks = build_blocks(args.table, args.prior_table, keys)
    for p, rs in rows.items():
        done = miss = 0
        with open(out / p, "w") as f:
            for r in rs:
                k = (r["metadata"]["season"], int(r["week"]), int(r["metadata"]["player_id"]))
                b = blocks.get(k)
                if b and HEADER not in r["prompt"] and MARKER in r["prompt"]:
                    r["prompt"] = r["prompt"].replace(MARKER, b + "\n\n" + MARKER, 1); done += 1
                elif b and HEADER not in r["prompt"]:
                    r["prompt"] = r["prompt"].replace("<|turn>\n<|turn>model", b + "\n<|turn>\n<|turn>model", 1); done += 1
                else:
                    miss += b is None
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{p}: {len(rs)} rows, block added {done}, no history row {miss}")
    for extra in src.iterdir():
        if extra.name not in files and extra.is_file() and not (out / extra.name).exists():
            (out / extra.name).write_bytes(extra.read_bytes())


if __name__ == "__main__":
    main()

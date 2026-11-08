#!/usr/bin/env python3
"""Build data/market_odds/pl_match_odds.csv from football-data.co.uk season files (F14 market features).

Steps per season file data/market_odds/raw/E0_<yyzz>.csv:
  1. map football-data team names to FPL team ids by matching each club's set of match dates against
     data/fpl_history/<season>/fixtures.csv (no name table needed; works for every season, and the
     mapping is written to data/market_odds/team_names.json for the live upcoming-odds file);
  2. de-vig the closing 1X2 and over/under 2.5 lines (Pinnacle closing, else average closing, else
     the pre-closing lines, else Bet365) and fit an independent-Poisson expected goals per side.

usage: build_market_odds.py [--raw data/market_odds/raw] [--history data/fpl_history]
                            [--out data/market_odds/pl_match_odds.csv] [--upcoming data/market_odds/raw/fixtures.csv]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.market import devig, fit_poisson, london_date  # noqa: E402

SEASON_OF = {"1920": "2019-20", "2021": "2020-21", "2122": "2021-22", "2223": "2022-23", "2324": "2023-24",
             "2425": "2024-25", "2526": "2025-26", "2627": "2026-27", "2728": "2027-28"}
SOURCES = [  # (home, draw, away, over, under) column names, best first
    ("PSCH", "PSCD", "PSCA", "PC>2.5", "PC<2.5"),
    ("AvgCH", "AvgCD", "AvgCA", "AvgC>2.5", "AvgC<2.5"),
    ("PSH", "PSD", "PSA", "P>2.5", "P<2.5"),
    ("AvgH", "AvgD", "AvgA", "Avg>2.5", "Avg<2.5"),
    ("B365H", "B365D", "B365A", "B365>2.5", "B365<2.5"),
]


def read_fd(path: Path) -> pd.DataFrame:
    frame = pd.read_csv(path, encoding="utf-8-sig")
    frame = frame[frame["Div"].astype(str) == "E0"].copy()
    frame["date"] = pd.to_datetime(frame["Date"], dayfirst=True, errors="coerce").dt.strftime("%Y-%m-%d")
    return frame.dropna(subset=["date", "HomeTeam", "AwayTeam"])


def map_names(fd: pd.DataFrame, fixtures: pd.DataFrame) -> dict:
    """football-data name -> FPL team id, by overlap of match dates."""
    fixtures = fixtures.dropna(subset=["kickoff_time"]).copy()
    fixtures["date"] = london_date(fixtures["kickoff_time"])
    # (date, side) pairs: two clubs can share every match DATE early in a season (Hull and Forest,
    # six rounds into 2026-27), but not every date AND venue.
    fpl_dates = {}
    for team_col, side in (("team_h", "H"), ("team_a", "A")):
        for team, group in fixtures.groupby(team_col):
            fpl_dates.setdefault(int(team), set()).update((d, side) for d in group["date"])
    mapping = {}
    for name in sorted(set(fd["HomeTeam"]) | set(fd["AwayTeam"])):
        dates = {(d, "H") for d in fd.loc[fd["HomeTeam"] == name, "date"]} | {(d, "A") for d in fd.loc[fd["AwayTeam"] == name, "date"]}
        scored = sorted(((len(dates & d), team) for team, d in fpl_dates.items()), reverse=True)
        best, second = scored[0], scored[1] if len(scored) > 1 else (0, None)
        if best[0] == 0 or best[0] == second[0]:
            raise SystemExit(f"ambiguous team mapping for {name}: {scored[:3]}")
        mapping[name] = best[1]
    if len(set(mapping.values())) != len(mapping):
        raise SystemExit(f"two names mapped to one id: {mapping}")
    return mapping


def pick_source(row: pd.Series):
    for h, d, a, o, u in SOURCES:
        if all(c in row.index for c in (h, d, a)):
            probs = devig([row[h], row[d], row[a]])
            if probs is None:
                continue
            over = None
            if o in row.index and u in row.index:
                ou = devig([row[o], row[u]])
                over = ou[0] if ou else None
            return probs, over, h
    return None, None, None


def build_rows(fd: pd.DataFrame, season: str, mapping: dict) -> list:
    rows = []
    for _, r in fd.iterrows():
        probs, over, source = pick_source(r)
        if probs is None:
            continue
        lam_h, lam_a = fit_poisson(probs[0], probs[1], probs[2], over)
        rows.append({"season": season, "date": r["date"], "home_team_id": mapping[r["HomeTeam"]],
                     "away_team_id": mapping[r["AwayTeam"]], "home_name": r["HomeTeam"], "away_name": r["AwayTeam"],
                     "p_home": round(probs[0], 4), "p_draw": round(probs[1], 4), "p_away": round(probs[2], 4),
                     "p_over25": round(over, 4) if over is not None else float("nan"),
                     "lambda_home": round(lam_h, 4), "lambda_away": round(lam_a, 4), "source": source})
    return rows


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--raw", default=str(ROOT / "data/market_odds/raw"))
    ap.add_argument("--history", default=str(ROOT / "data/fpl_history"))
    ap.add_argument("--out", default=str(ROOT / "data/market_odds/pl_match_odds.csv"))
    ap.add_argument("--upcoming", default=str(ROOT / "data/market_odds/raw/fixtures.csv"),
                    help="football-data fixtures.csv (odds for unplayed matches) -> data/market_odds/upcoming_odds.csv")
    ap.add_argument("--names-out", default=str(ROOT / "data/market_odds/team_names.json"))
    args = ap.parse_args()
    all_rows, names = [], {}
    for path in sorted(Path(args.raw).glob("E0_*.csv")):
        code = path.stem.split("_")[1]
        season = SEASON_OF.get(code)
        fixtures_path = Path(args.history) / season / "fixtures.csv" if season else None
        if season is None or not fixtures_path.exists():
            print(f"skip {path.name}: no FPL fixtures for season {season}")
            continue
        fd = read_fd(path)
        mapping = map_names(fd, pd.read_csv(fixtures_path))
        names[season] = mapping
        rows = build_rows(fd, season, mapping)
        all_rows += rows
        print(f"{season}: {len(rows)} matches, {len(mapping)} teams, sources {pd.Series([r['source'] for r in rows]).value_counts().to_dict()}")
    out = pd.DataFrame(all_rows).sort_values(["season", "date", "home_team_id"])
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.out, index=False)
    Path(args.names_out).write_text(json.dumps(names, indent=1, sort_keys=True))
    print(f"wrote {len(out)} rows -> {args.out}")
    # upcoming odds for the live season: names come from the latest mapped season
    up_path = Path(args.upcoming)
    if up_path.exists() and names:
        season = max(names)
        mapping = names[season]
        up = read_fd(up_path)
        up = up[up["HomeTeam"].isin(mapping) & up["AwayTeam"].isin(mapping)]
        rows = build_rows(up, season, mapping)
        up_out = Path(args.out).parent / "upcoming_odds.csv"
        pd.DataFrame(rows, columns=out.columns).to_csv(up_out, index=False)
        print(f"upcoming ({season}): {len(rows)} matches -> {up_out}")


if __name__ == "__main__":
    main()

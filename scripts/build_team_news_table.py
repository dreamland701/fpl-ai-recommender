#!/usr/bin/env python3
"""F16: parse the Guardian's weekly "Premier League team news: predicted lineups" articles into per-player-week
categories and write them as columns onto a copy of the production table (2026-10-21, the Konsa case).

Each article (one per gameweek, published a median 17 h before the deadline, 88-94% within 24 h) lists for every
team: "Subs from <names> Doubtful <names> Injured <names> Suspended <names>". A squad player not named in any list
is the Guardian's implied XI. Categories per (season, week, player): XI / sub / doubtful / injured / suspended,
using only articles published before that week's deadline (deadline = 90 min before the first kickoff, from
fixtures.csv) and within 72 h of it. Columns: gn_article (team-week had an article), gn_xi, gn_sub, gn_doubtful,
gn_out (injured or suspended). Features are used only with FPL_TEAM_NEWS_FEATS=1 (dataset.get_feature_columns).

Measured 2026-10-21 (2025-26 uncertain rows, classic P < 0.5): implied-XI rows started 35% vs named subs 20%;
P 0.5-0.8: 75% vs 50%; P >= 0.8: 91% vs 72%; Guardian "injured" rows at classic P 0.5-0.8 played 0% (n 59).
21-window bench (TN1_F vs TN0_F, same table): +31 actual / +33 xPts, t 1.35 / 1.61, 4 wins / 14 ties / 3 losses.

usage: build_team_news_table.py --table data/fpl_training_rows_v3_contract_f6.csv \
         --out data/fpl_training_rows_v3_contract_f6_teamnews.csv [--store <jsonl>]... [--feat-json <path>]
Default stores: the Guardian season files 2022-23..2025-26 plus every 2026-27 live file.
Re-run after every weekly table rebuild (the weekly ingest does not rebuild table variants).
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import glob
import json
import re
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
ALIAS = {"manchester utd": "man utd", "manchester united": "man utd", "nottingham forest": "nottm forest", "tottenham": "spurs", "manchester city": "man city", "manchester united": "man utd", "tottenham": "spurs", "tottenham hotspur": "spurs",
         "nottingham forest": "nottm forest", "wolverhampton": "wolves", "wolverhampton wanderers": "wolves",
         "newcastle united": "newcastle", "west ham united": "west ham", "brighton  hove albion": "brighton",
         "brighton and hove albion": "brighton", "sheffield united": "sheffield utd", "leeds united": "leeds",
         "luton town": "luton", "ipswich town": "ipswich", "leicester city": "leicester", "coventry city": "coventry",
         "hull city": "hull", "afc bournemouth": "bournemouth"}
HDR = re.compile(r"(?P<home>[A-Z][A-Za-z'&\. ]+?) v (?P<away>[A-Z][A-Za-z'&\. ]+?) (?:Saturday|Sunday|Monday|Tuesday|Wednesday|Thursday|Friday)")
BLOCK = re.compile(r"Subs from (?P<subs>.*?) Doubtful (?P<doubt>.*?) Injured (?P<inj>.*?) Suspended (?P<susp>.*?)(?= Discipline| Form| Leading scorer|$)", re.S)
TITLE = re.compile(r"predicted lineups", re.I)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z\- ]", "", s.lower()).strip()


def team_resolver(season: str):
    teams = list(csv.DictReader(open(ROOT / "data/fpl_history" / season / "teams.csv")))
    by = {}
    for t in teams:
        by[norm(t["name"])] = int(t["id"])
        by[norm(t["short_name"])] = int(t["id"])

    def resolve(name: str):
        n = norm(name)
        n = ALIAS.get(n, n)
        if n in by:
            return by[n]
        for k, v in by.items():
            if k.split()[0] == n.split()[0] and len(n.split()[0]) > 3:
                return v
        return None
    return resolve


def deadlines(season: str) -> dict[int, dt.datetime]:
    rows = list(csv.DictReader(open(ROOT / "data/fpl_history" / season / "fixtures.csv")))
    gwcol = [c for c in rows[0].keys() if c in ("event", "GW", "round")][0]
    byg = collections.defaultdict(list)
    for r in rows:
        if r.get("kickoff_time") and r.get(gwcol):
            try:
                byg[int(float(r[gwcol]))].append(dt.datetime.fromisoformat(r["kickoff_time"].replace("Z", "+00:00")))
            except ValueError:
                pass
    return {g: min(v) - dt.timedelta(minutes=90) for g, v in byg.items()}


def names(field: str) -> list[str]:
    field = re.sub(r"\([^)]*\)", "", field)
    return [n.strip() for n in field.split(",") if n.strip() and n.strip().lower() != "none"]


def parse_article(text: str, resolve) -> dict[int, dict[str, list[str]]]:
    out = {}
    hdrs = list(HDR.finditer(text))
    for i, m in enumerate(hdrs):
        seg = text[m.end(): hdrs[i + 1].start() if i + 1 < len(hdrs) else len(text)]
        blocks = list(BLOCK.finditer(seg))
        for team_name, b in zip((m.group("home"), m.group("away")), blocks[:2]):
            tid = resolve(team_name)
            if tid is None:
                continue
            out[tid] = {"sub": names(b.group("subs")), "doubtful": names(b.group("doubt")),
                        "injured": names(b.group("inj")), "suspended": names(b.group("susp"))}
    return out


def player_keys(web_name: str) -> set[str]:
    n = norm(web_name.replace(".", " "))
    toks = n.split()
    return {n, toks[-1]} if toks else {n}


def default_stores() -> dict[str, list[str]]:
    r = ROOT / "reports"
    return {"2022-23": [str(r / "evidence_guardian_football_2022_23.jsonl")],
            "2023-24": [str(r / "evidence_guardian_football_2023_24.jsonl")],
            "2024-25": [str(r / "evidence_guardian_football_2024_25.jsonl")],
            "2025-26": [str(r / "evidence_guardian_football_2025_26.jsonl")],
            "2026-27": sorted(glob.glob(str(r / "evidence_guardian_football_2627_gw*.jsonl")))
            + [str(r / "evidence_guardian_football_2026_prelaunch.jsonl"), str(r / "evidence_guardian_football_2026_wed.jsonl")]}


def build_categories(table: pd.DataFrame, stores: dict[str, list[str]], max_hours: float = 72.0):
    feat: dict[tuple[str, int, int], str] = {}
    coverage = collections.Counter(); hours = collections.defaultdict(list)
    matched = collections.Counter(); unmatched = collections.Counter(); seen = set()
    for season, paths in stores.items():
        if season not in set(table.season):
            continue
        resolve = team_resolver(season); dl = deadlines(season)
        tbl = table[table.season == season]
        squads = {(w, t): g[["player_id", "player_name"]] for (w, t), g in tbl.groupby(["week", "team_id"])}
        for path in paths:
            if not Path(path).exists():
                continue
            for line in open(path):
                d = json.loads(line)
                if not TITLE.search(d.get("title", "")) or d.get("url") in seen:
                    continue
                seen.add(d.get("url"))
                ts = dt.datetime.fromisoformat(d["published_at"].replace("Z", "+00:00"))
                nxt = [(g, x) for g, x in dl.items() if x >= ts]
                if not nxt:
                    continue
                g, x = min(nxt, key=lambda y: y[1])
                if (x - ts).total_seconds() > max_hours * 3600:
                    continue
                for tid, cats in parse_article(d.get("full_text") or d.get("content") or "", resolve).items():
                    sq = squads.get((g, tid))
                    if sq is None:
                        continue
                    coverage[season] += 1; hours[season].append((x - ts).total_seconds() / 3600)
                    listed = {}
                    for cat, nms in cats.items():
                        for nm in nms:
                            k = norm(nm).split()[-1] if norm(nm) else ""
                            cands = [r for _, r in sq.iterrows() if k and k in player_keys(r.player_name)]
                            if len(cands) == 1:
                                listed[int(cands[0].player_id)] = cat; matched[season] += 1
                            else:
                                unmatched[season] += 1
                    for _, r in sq.iterrows():
                        feat[(season, g, int(r.player_id))] = listed.get(int(r.player_id), "XI")
    print("team-weeks covered:", dict(coverage), "| hours before deadline p50:",
          {s: round(float(np.median(v)), 1) for s, v in hours.items()})
    print("listed names matched / unmatched:", dict(matched), dict(unmatched))
    return feat


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--table", default="data/fpl_training_rows_v3_contract_f6.csv")
    ap.add_argument("--out", default="data/fpl_training_rows_v3_contract_f6_teamnews.csv")
    ap.add_argument("--store", action="append", help="season=path (repeatable); default: the Guardian season files")
    ap.add_argument("--feat-json", help="also write the (season|week|player_id) -> category map")
    args = ap.parse_args()
    stores = default_stores()
    for item in args.store or []:
        season, path = item.split("=", 1)
        stores.setdefault(season, []).append(path)
    table = pd.read_csv(args.table, low_memory=False)
    feat = build_categories(table, stores)
    cat = pd.Series([feat.get((s, w, p)) for s, w, p in zip(table.season, table.week, table.player_id)], index=table.index)
    cols = pd.DataFrame({"gn_article": cat.notna().astype(float),
                         "gn_xi": (cat == "XI").astype(float), "gn_sub": (cat == "sub").astype(float),
                         "gn_doubtful": (cat == "doubtful").astype(float),
                         "gn_out": ((cat == "injured") | (cat == "suspended")).astype(float)}, index=table.index)
    table = pd.concat([table.drop(columns=[c for c in cols.columns if c in table.columns]), cols], axis=1)
    print(cols.mean().round(3).to_dict())
    print("article coverage by season:", table.groupby("season")["gn_article"].mean().round(2).to_dict())
    table.to_csv(args.out, index=False)
    print("wrote", args.out, table.shape)
    if args.feat_json:
        json.dump({f"{s}|{w}|{p}": c for (s, w, p), c in feat.items()}, open(args.feat_json, "w"))


if __name__ == "__main__":
    main()

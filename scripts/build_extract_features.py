#!/usr/bin/env python3
"""Turn extracted availability facts into per-player-week features on a copy of the production table (2026-10-22).

Inputs: the routed documents (scripts/build_extract_docs.py: doc_id -> season, gw, hours_before, source) and one or
more extractor outputs (scripts/extract_availability_facts.py rows: doc_id -> facts[{player, team, status, ...}]).
Each fact is resolved to a player_id of that season (data/fpl_history/<season>/players_raw.csv: surname of
second_name or web_name, or the full name; a stated club disambiguates through the table's team_id for that week;
only unique matches count) and keyed to (season, week = the document's next deadline gameweek).

Columns written (zeros where no fact), only for documents published within --max-hours of the deadline:
  ex_n                      number of facts about the player that week
  ex_<s>                    1 if any fact of status s           (s in xi, bench, doubt, out, return, role)
  ex_<s>_w                  max recency weight of status s facts, weight = 1 - hours_before / max_hours
  ex_last_<s>               1 for the status of the most recent fact
Features are used only with FPL_EXTRACT_FEATS=1 (dataset.get_feature_columns). --feat-json also dumps the resolved
facts per (season, week, player_id) for the SFT team sheet. Re-run after every weekly table rebuild.

usage: build_extract_features.py --docs reports/extract_facts/docs_all.jsonl --facts <pred.jsonl> [--facts ...] \
         --table data/fpl_training_rows_v3_contract_f6.csv --out data/fpl_training_rows_v3_contract_f6_extract.csv \
         [--max-hours 168] [--feat-json reports/extract_facts/facts_by_player_week.json]
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_team_news_table import team_resolver  # noqa: E402
from extract_availability_facts import STATUSES  # noqa: E402


LETTER_MAP = str.maketrans({"’": "'", "‘": "'", "ß": "ss", "ø": "o", "Ø": "O", "æ": "ae", "Æ": "AE", "đ": "d", "Đ": "D", "ł": "l", "Ł": "L", "ı": "i"})
# nicknames the FPL feed never spells out (first_name/second_name/web_name all lack the token): alias key -> web_name
ALIASES = {  # alias key -> (web_name, required second_name fragment or None)
    "jota": ("Diogo J.", "teixeira"), "diogo jota": ("Diogo J.", "teixeira"), "rodri": ("Rodrigo", "hernandez"),
    "gabriel jesus": ("G.Jesus", None), "jesus": ("G.Jesus", None), "bruno guimaraes": ("Bruno G.", None), "guimaraes": ("Bruno G.", None)}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", (s or "").translate(LETTER_MAP))
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z\- ]", "", s.lower().replace("_", " ").replace(".", " ").replace("'", " ")).strip()


def tokens(s: str) -> list[str]:
    return [t for t in norm(s).replace("-", " ").split() if not t.isdigit()]


class Resolver:
    """season -> (surname|full name) -> player ids, restricted to players with a table row that week."""

    def __init__(self, season: str, table: pd.DataFrame):
        self.by_key: dict[str, set[int]] = collections.defaultdict(set)
        self.first_tokens: dict[int, set[str]] = collections.defaultdict(set)
        p = ROOT / "data/fpl_history" / season / "players_raw.csv"
        if p.exists():
            for r in csv.DictReader(open(p, newline="")):
                pid = int(r["id"])
                first, second, web = tokens(r.get("first_name", "")), tokens(r.get("second_name", "")), tokens(r.get("web_name", ""))
                keys = {second[-1] if second else "", web[-1] if web else "", " ".join(first + second), " ".join(web)}
                keys |= {t for t in second if len(t) >= 4}                      # every surname token ("Núñez Ribeiro" -> nunez)
                keys |= {t for t in first if len(t) >= 4 and t != "igor"}        # first names used alone (Alisson, Ederson, Rodri from "Rodrigo 'Rodri'")
                if len(web) == 2 and len(web[1]) == 1:                           # "Ederson M." / "Diogo J." -> ederson, diogo
                    keys.add(web[0])
                if len(web) == 2 and len(web[0]) == 1:                           # "A.Becker" -> becker (already) + first name
                    keys |= set(first[:1])
                for alias, (target, frag) in ALIASES.items():
                    if norm(r.get("web_name", "")) == norm(target) and (frag is None or frag in norm(r.get("second_name", ""))):
                        keys.add(alias)
                for key in keys:
                    if key:
                        self.by_key[key].add(pid)
                self.first_tokens[pid] |= set(first) | set(web[:1])
        for pid, name in table[["player_id", "player_name"]].drop_duplicates().itertuples(index=False):
            toks = tokens(str(name))
            if toks:
                self.by_key[toks[-1]].add(int(pid)); self.by_key[" ".join(toks)].add(int(pid))
        self.week_team = {(int(w), int(pid)): int(t) for w, pid, t in
                          table[["week", "player_id", "team_id"]].dropna().itertuples(index=False)}
        self.week_players = collections.defaultdict(set)
        for (w, pid) in self.week_team:
            self.week_players[w].add(pid)
        self.resolve_team = team_resolver(season)

    def __call__(self, name: str, team: str | None, week: int) -> int | None:
        toks = tokens(name)
        if not toks:
            return None
        cands = set(self.by_key.get(" ".join(toks), set()))
        if not cands:
            cands = set(self.by_key.get(toks[-1], set()))
            if len(toks) > 1:  # surname fallback: the stated first name (or initial) must agree with the candidate's ("Diogo Jota" is not Jota Silva)
                cands = {c for c in cands if not self.first_tokens.get(c)
                         or any(f.startswith(toks[0]) if len(toks[0]) == 1 else f[:2] == toks[0][:2] for f in self.first_tokens[c])}  # Andy/Andrew, Kostas/Konstantinos
        cands &= self.week_players.get(week, set())
        if len(cands) > 1 and team:
            tid = self.resolve_team(team)
            if tid is not None:
                narrowed = {c for c in cands if self.week_team.get((week, c)) == tid}
                cands = narrowed or cands
        if len(cands) > 1 and len(toks) > 1:  # initial + surname ("C.Jones") against first names
            narrowed = {c for c in cands if any(k.startswith(toks[0][0]) and k.endswith(toks[-1]) for k, v in self.by_key.items() if c in v and " " in k)}
            cands = narrowed or cands
        return next(iter(cands)) if len(cands) == 1 else None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", required=True); ap.add_argument("--facts", action="append", required=True)
    ap.add_argument("--table", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--max-hours", type=float, default=168.0); ap.add_argument("--feat-json", default=None)
    args = ap.parse_args()
    docs = {d["doc_id"]: d for d in (json.loads(l) for l in open(args.docs))}
    table = pd.read_csv(args.table, low_memory=False)
    resolvers: dict[str, Resolver] = {}
    per: dict[tuple[str, int, int], list[dict]] = collections.defaultdict(list)
    n_facts = n_scope = n_res = 0; unresolved = collections.Counter(); seen_docs = set()
    for path in args.facts:
        for line in open(path):
            r = json.loads(line)
            d = docs.get(r["doc_id"])
            if d is None or r["doc_id"] in seen_docs:
                continue
            seen_docs.add(r["doc_id"])
            for f in r.get("facts", []):
                n_facts += 1
                if f.get("status") not in STATUSES or d["hours_before"] > args.max_hours or d["hours_before"] < 0:
                    continue
                n_scope += 1
                if d["season"] not in resolvers:
                    if d["season"] not in set(table.season):
                        continue
                    resolvers[d["season"]] = Resolver(d["season"], table[table.season == d["season"]])
                pid = resolvers[d["season"]](f.get("player", ""), f.get("team"), int(d["gw"]))
                if pid is None:
                    unresolved[f.get("player", "")] += 1; continue
                n_res += 1
                per[(d["season"], int(d["gw"]), pid)].append({"status": f["status"], "hours_before": d["hours_before"],
                                                              "detail": f.get("detail", ""), "team": f.get("team"), "source": d["source"],
                                                              "doc_id": r["doc_id"], "title": d["title"], "player": f.get("player", "")})
    print(f"facts {n_facts} | within {args.max_hours:.0f}h with a valid status {n_scope} | resolved {n_res} "
          f"({n_res / max(1, n_scope):.0%}) | player-weeks with facts {len(per)} | docs {len(seen_docs)}")
    print("unresolved (top):", unresolved.most_common(15))
    cols = ["ex_n"] + [f"ex_{s}" for s in STATUSES] + [f"ex_{s}_w" for s in STATUSES] + [f"ex_last_{s}" for s in STATUSES]
    feat = pd.DataFrame(0.0, index=range(len(per)), columns=cols)
    keys = []
    for i, (key, facts) in enumerate(per.items()):
        keys.append(key); feat.at[i, "ex_n"] = len(facts)
        for f in facts:
            w = max(0.0, 1.0 - f["hours_before"] / args.max_hours)
            feat.at[i, f"ex_{f['status']}"] = 1.0
            feat.at[i, f"ex_{f['status']}_w"] = max(feat.at[i, f"ex_{f['status']}_w"], w)
        latest = min(facts, key=lambda f: f["hours_before"])
        feat.at[i, f"ex_last_{latest['status']}"] = 1.0
    feat.insert(0, "season", [k[0] for k in keys]); feat.insert(1, "week", [k[1] for k in keys]); feat.insert(2, "player_id", [k[2] for k in keys])
    out = table.drop(columns=[c for c in cols if c in table.columns]).merge(feat, on=["season", "week", "player_id"], how="left")
    out[cols] = out[cols].fillna(0.0)
    assert len(out) == len(table), (len(out), len(table))
    out.to_csv(args.out, index=False)
    by_season = out[out.ex_n > 0].groupby("season").size().to_dict()
    print(f"wrote {args.out}: rows with facts by season {by_season}")
    print("status counts (rows):", {s: int(out[f"ex_{s}"].sum()) for s in STATUSES})
    if args.feat_json:
        Path(args.feat_json).parent.mkdir(parents=True, exist_ok=True)
        with open(args.feat_json, "w") as f:
            json.dump({f"{k[0]}|{k[1]}|{k[2]}": v for k, v in per.items()}, f, ensure_ascii=False)
        print("facts json ->", args.feat_json)


if __name__ == "__main__":
    main()

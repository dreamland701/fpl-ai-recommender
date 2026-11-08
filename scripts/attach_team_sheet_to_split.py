#!/usr/bin/env python3
"""Insert a dense pre-deadline team sheet into every prompt of an SFT split (2026-10-23, step 3 of the
"read facts, not snippets" path): the facts the extractor read (scripts/build_extract_features.py --feat-json) and the
Guardian predicted-lineup categories (scripts/build_team_news_table.py --feat-json) for the player's team that week,
rendered as one short section placed before "Timestamp-safe text evidence:" so the compact H-recipe prompt keeps it.

Block (≤ --max-chars, default 1100 ≈ 300 tokens):
  Pre-deadline team sheet (facts read from news before the deadline; Nh = hours before it):
  - This player: out (hamstring, 20h, Guardian) | doubt (late test, 60h)      or "no pre-deadline fact"
  - Team ARS: OUT A (hamstring 20h), B (suspended 40h); DOUBT C (10h); RETURN D (30h); BENCH E; XI F; ROLE G (penalties)
  - Guardian predicted lineup: subs F, G; doubtful C; injured A, B                 (when the article exists)
Rows whose team has nothing get the section with "no pre-deadline facts for this team" so the format is uniform and
the mechanism check can compare rows with and without facts (metadata.team_sheet_facts counts them).

usage: attach_team_sheet_to_split.py --split <dir with train.jsonl/eval.jsonl> --out <dir> \
         --facts-json reports/extract_facts/facts_by_player_week_31b_v2.json [--teamnews-json reports/team_news_f16/gn_feat.json] \
         --table data/fpl_training_rows_v3_contract_f6.csv [--max-chars 1100]
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import shutil
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MARKER = "Timestamp-safe text evidence:"
ORDER = ("out", "doubt", "return", "bench", "xi", "role")
GN_LABEL = {"sub": "subs", "doubtful": "doubtful", "injured": "injured", "suspended": "suspended"}


def short_names(season: str) -> dict[int, str]:
    p = ROOT / "data/fpl_history" / season / "teams.csv"
    return {int(r["id"]): r["short_name"] for r in csv.DictReader(open(p, newline=""))} if p.exists() else {}


def fact_line(f: dict, with_source: bool = False) -> str:
    bits = [f.get("detail", "").strip().rstrip("."), f"{int(round(f['hours_before']))}h"]
    if with_source:
        bits.append(f.get("source", ""))
    return f"{f['status']} (" + ", ".join(b for b in bits if b) + ")"


def build_block(player_name: str, own: list[dict], team_facts: dict[int, list[dict]], names: dict[int, str],
                gn: dict[int, str], team_short: str, max_chars: int) -> str:
    lines = ["Pre-deadline team sheet (facts read from news before the deadline; Nh = hours before it):"]
    own_sorted = sorted(own, key=lambda f: f["hours_before"])
    lines.append("- This player (" + player_name + "): " + (" | ".join(fact_line(f, True) for f in own_sorted[:3]) if own else "no pre-deadline fact"))
    groups = collections.defaultdict(list)
    for pid, facts in team_facts.items():
        latest = min(facts, key=lambda f: f["hours_before"])
        groups[latest["status"]].append((names.get(pid, latest.get("player", "?")), latest))
    if groups:
        parts = []
        for st in ORDER:
            if groups.get(st):
                items = sorted(groups[st], key=lambda x: x[1]["hours_before"])
                parts.append(st.upper() + " " + ", ".join(f"{n} ({f.get('detail', '').strip().rstrip('.')[:40]} {int(round(f['hours_before']))}h)" if f.get("detail") else f"{n} ({int(round(f['hours_before']))}h)" for n, f in items[:8]))
        lines.append(f"- Team {team_short}: " + "; ".join(parts))
    else:
        lines.append(f"- Team {team_short}: no pre-deadline facts for this team")
    if gn:
        cats = collections.defaultdict(list)
        for pid, cat in gn.items():
            if cat in GN_LABEL:
                cats[GN_LABEL[cat]].append(names.get(pid, str(pid)))
        lines.append("- Guardian predicted lineup: " + "; ".join(f"{k} {', '.join(sorted(v))}" for k, v in cats.items()) if cats else "- Guardian predicted lineup: full-strength (no one listed)")
    block = "\n".join(lines)
    if len(block) > max_chars:
        block = block[: max_chars - 1].rsplit(";", 1)[0] + " …"
    return block


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--split", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--facts-json", required=True); ap.add_argument("--teamnews-json", default=None)
    ap.add_argument("--table", default="data/fpl_training_rows_v3_contract_f6.csv"); ap.add_argument("--max-chars", type=int, default=1100)
    args = ap.parse_args()
    facts = json.load(open(args.facts_json))
    by_team_week: dict[tuple[str, int, int], dict[int, list[dict]]] = collections.defaultdict(dict)
    table = pd.read_csv(args.table, usecols=["season", "week", "player_id", "player_name", "team_id"], low_memory=False)
    team_of = {(s, int(w), int(p)): int(t) for s, w, p, t in table[["season", "week", "player_id", "team_id"]].dropna().itertuples(index=False)}
    # 2026-10-27 (live use): a week the table does not hold yet (the coming gameweek) falls back to the player's latest team.
    latest = table[["season", "week", "player_id", "team_id"]].dropna().sort_values("week").drop_duplicates(["season", "player_id"], keep="last")
    team_latest = {(s, int(p)): int(t) for s, p, t in latest[["season", "player_id", "team_id"]].itertuples(index=False)}
    _team_of_get = team_of.get
    team_of = type("TeamOf", (), {"get": staticmethod(lambda key, default=None: _team_of_get(key) if _team_of_get(key) is not None else team_latest.get((key[0], key[2]), default))})()
    name_of = {(s, int(p)): str(n) for s, p, n in table[["season", "player_id", "player_name"]].drop_duplicates(["season", "player_id"]).itertuples(index=False)}
    for key, fl in facts.items():
        s, w, p = key.split("|"); w, p = int(w), int(p)
        t = team_of.get((s, w, p))
        if t is not None:
            by_team_week[(s, w, t)][p] = fl
    gn_by_team_week: dict[tuple[str, int, int], dict[int, str]] = collections.defaultdict(dict)
    if args.teamnews_json:
        for key, cat in json.load(open(args.teamnews_json)).items():
            s, w, p = key.split("|"); w, p = int(w), int(p)
            t = team_of.get((s, w, p))
            if t is not None and cat != "XI":
                gn_by_team_week[(s, w, t)][p] = cat
    shorts: dict[str, dict[int, str]] = {}
    Path(args.out).mkdir(parents=True, exist_ok=True)
    stats = collections.Counter()
    for name in ("train.jsonl", "eval.jsonl"):
        src = Path(args.split) / name
        if not src.exists():
            continue
        with open(src) as fin, open(Path(args.out) / name, "w") as fout:
            for line in fin:
                r = json.loads(line); m = r["metadata"]
                s = str(m["season"]); w = int(m["week"]); p = int(m["player_id"]); t = int(float(m.get("team_id") or team_of.get((s, w, p), 0)))
                if s not in shorts:
                    shorts[s] = short_names(s)
                tf = by_team_week.get((s, w, t), {}); own = tf.get(p, [])
                names = {pid: name_of.get((s, pid), fl[0].get("player", "?")) for pid, fl in tf.items()}
                names.update({pid: name_of.get((s, pid), str(pid)) for pid in gn_by_team_week.get((s, w, t), {})})
                block = build_block(str(m.get("player_name", "")), own, tf, names, gn_by_team_week.get((s, w, t), {}), shorts[s].get(t, str(t)), args.max_chars)
                prompt = r["prompt"]
                if MARKER in prompt:
                    prompt = prompt.replace(MARKER, block + "\n\n" + MARKER, 1)
                else:
                    cut = prompt.rfind("<turn|>")
                    prompt = (prompt[:cut] + "\n" + block + "\n" + prompt[cut:]) if cut > 0 else prompt + "\n" + block
                r["prompt"] = prompt
                m["team_sheet_facts"] = sum(len(v) for v in tf.values()); m["team_sheet_own_facts"] = len(own)
                m["team_sheet_guardian"] = bool(gn_by_team_week.get((s, w, t)))
                fout.write(json.dumps(r, ensure_ascii=False) + "\n")
                stats[name + " rows"] += 1; stats[name + " with team facts"] += bool(tf); stats[name + " with own facts"] += bool(own)
                stats[name + " with guardian"] += bool(gn_by_team_week.get((s, w, t)))
    for extra in ("summary.json",):
        if (Path(args.split) / extra).exists():
            shutil.copy(Path(args.split) / extra, Path(args.out) / extra)
    print(json.dumps(stats, indent=1))


if __name__ == "__main__":
    main()

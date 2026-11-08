#!/usr/bin/env python3
"""Live F16: parse the newest Guardian "Premier League team news: predicted lineups" article published before a
gameweek's deadline (and within --max-hours of it) into per-player categories for the CURRENT squads, keyed like
scripts/build_team_news_table.py --feat-json ("2026-27|9|<player_id>": XI | sub | doubtful | injured | suspended), so
the H5 team-sheet block (scripts/attach_team_sheet_to_split.py --teamnews-json) and the packet can use it for a week
the training table does not hold yet. Also prints each team's listed names and the entry squad's categories.

The table builder only covers weeks present in the table (2026-10-26 finding: the GW8 article landed Fri 15:42 UTC,
after the 14:00 UTC refresh pull, so GW8 had no categories at all); pull the Guardian store again shortly before the
deadline and run this on it.

usage: live_team_news.py --event 9 --bootstrap <snapshot/bootstrap_static.json> --store <guardian jsonl>... \
         --out reports/team_news_f16/gn_feat_live_gw9.json [--entry-state <entry_state.json>] [--max-hours 72]
"""
import argparse
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_team_news_table import TITLE, norm, parse_article, player_keys, team_resolver  # noqa: E402


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--event", type=int, required=True)
    ap.add_argument("--bootstrap", required=True)
    ap.add_argument("--store", action="append", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--entry-state")
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--max-hours", type=float, default=72.0)
    args = ap.parse_args()
    boot = json.load(open(args.bootstrap))
    event = next(e for e in boot["events"] if e["id"] == args.event)
    deadline = dt.datetime.fromisoformat(event["deadline_time"].replace("Z", "+00:00"))
    teams = {t["id"]: t for t in boot["teams"]}
    resolve = team_resolver(args.season)  # the table builder's resolver (teams.csv + ALIAS), same behaviour as F16
    squads = {}
    for e in boot["elements"]:
        squads.setdefault(e["team"], []).append(e)
    best = None
    for path in args.store:
        if not Path(path).exists():
            continue
        for line in open(path):
            d = json.loads(line)
            if not TITLE.search(d.get("title", "")):
                continue
            ts = dt.datetime.fromisoformat(d["published_at"].replace("Z", "+00:00"))
            if ts >= deadline or (deadline - ts).total_seconds() > args.max_hours * 3600:
                continue
            if best is None or ts > best[0]:
                best = (ts, d)
    feat = {}
    if best is None:
        print(f"no predicted-lineups article within {args.max_hours:.0f} h before the GW{args.event} deadline {deadline.isoformat()} in {args.store}")
        Path(args.out).write_text("{}\n")
        return
    ts, d = best
    print(f"article: {d.get('title')} | published {ts.isoformat()} ({(deadline - ts).total_seconds() / 3600:.1f} h before the deadline) | {d.get('url')}")
    parsed = parse_article(d.get("full_text") or d.get("content") or "", resolve)
    matched = unmatched = 0
    for tid, cats in parsed.items():
        sq = squads.get(tid, [])
        listed = {}
        for cat, nms in cats.items():
            for nm in nms:
                k = norm(nm).split()[-1] if norm(nm) else ""
                cands = [e for e in sq if k and k in player_keys(e["web_name"])]
                if len(cands) == 1:
                    listed[cands[0]["id"]] = cat; matched += 1
                else:
                    unmatched += 1
        for e in sq:
            feat[f"{args.season}|{args.event}|{e['id']}"] = listed.get(e["id"], "XI")
        print(f"  {teams[tid]['short_name']}: " + "; ".join(f"{cat} {', '.join(nms)}" for cat, nms in cats.items() if nms))
    print(f"teams covered {len(parsed)}/20; listed names matched {matched}, unmatched {unmatched}")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(feat) + "\n")
    if args.entry_state and Path(args.entry_state).exists():
        state = json.load(open(args.entry_state))
        rows = []
        for s in state["squad"]:
            cat = feat.get(f"{args.season}|{args.event}|{s['player_id']}")
            rows.append(f"{s['name']} {cat if cat else 'team not covered'}")
        print("entry squad:", "; ".join(rows))
    print(f"wrote {args.out}: {len(feat)} player categories")


if __name__ == "__main__":
    main()

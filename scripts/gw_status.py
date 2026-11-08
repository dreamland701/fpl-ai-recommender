#!/usr/bin/env python3
"""Gate any gameweek analysis on settled data. HARD STOP if unfinished.

Twice now (GW2 and GW4 2026-27) a mid-gameweek scoreline was narrated as if
final — GW4's "three defenders blanked" post-mortem was wrong because Leeds
had not kicked off. A note-to-self did not hold, so this is a script: run it
BEFORE any results/ledger/post-mortem work and refuse to proceed on red.
"""
from __future__ import annotations
import argparse, json, sys, urllib.request

def req(u):
    return json.loads(urllib.request.urlopen(
        urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read())

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--event", type=int, required=True)
    ap.add_argument("--require-settled", action="store_true",
                    help="exit 1 unless every fixture is finished AND data_checked")
    a = ap.parse_args()
    b = req("https://fantasy.premierleague.com/api/bootstrap-static/")
    teams = {t["id"]: t["name"] for t in b["teams"]}
    ev = next(x for x in b["events"] if x["id"] == a.event)
    fx = req(f"https://fantasy.premierleague.com/api/fixtures/?event={a.event}")
    pending = [x for x in fx if not x["finished"]]
    settled = ev["finished"] and ev.get("data_checked")
    print(f"GW{a.event}: finished={ev['finished']} data_checked={ev.get('data_checked')} "
          f"avg={ev['average_entry_score']} | fixtures {len(fx) - len(pending)}/{len(fx)} finished")
    for x in pending:
        state = "IN PLAY" if x.get("started") else "NOT STARTED"
        print(f"   PENDING [{state}] {teams[x['team_h']]} v {teams[x['team_a']]}  ko {x['kickoff_time']}")
    if settled:
        print("STATUS: SETTLED — safe to score, ledger, and post-mortem.")
        return 0
    print("STATUS: NOT SETTLED — scores are provisional. Do NOT report totals, "
          "compare to the average, run a post-mortem, or write the ledger.")
    if a.require_settled:
        sys.exit(1)
    return 0

if __name__ == "__main__":
    sys.exit(main())

"""Score the pre-registered GW7 wildcard proposal against Wes's actual GW7.

Refuses to run until GW7 is settled (finished and data_checked). Verifies the
frozen proposal's sha256, then scores each frozen squad on official GW7 points
with automatic substitutions in its frozen bench order (fpl_ai.rules) and the
vice-captain rule, minus planned hits. Wes's actual score comes from his entry
history (gross points and transfer cost). Writes result_gw7.json and README.md.
"""
import hashlib
import json
import os
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.rules import automatic_substitutions  # noqa: E402

HERE = Path(__file__).resolve().parent
PROPOSAL = HERE / "proposal_frozen_2026-10-07.json"
ENTRY = 6535607
# SCORE_GW / SCORE_OUT exist only to test the scorer on a settled gameweek.
GW = int(os.environ.get("SCORE_GW", 7))
OUT = Path(os.environ.get("SCORE_OUT", HERE))
API = "https://fantasy.premierleague.com/api"


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(request, timeout=30).read())


def main() -> None:
    expected = (HERE / "proposal_frozen_2026-10-07.sha256").read_text().split()[0]
    if hashlib.sha256(PROPOSAL.read_bytes()).hexdigest() != expected:
        raise SystemExit("frozen proposal was modified after pre-registration; refusing to score it")
    bootstrap = get(f"{API}/bootstrap-static/")
    event = next(e for e in bootstrap["events"] if e["id"] == GW)
    if not (event["finished"] and event.get("data_checked")):
        raise SystemExit(f"GW{GW} is not settled yet (finished={event['finished']}, data_checked={event.get('data_checked')})")
    live = {e["id"]: e["stats"] for e in get(f"{API}/event/{GW}/live/")["elements"]}
    points = {pid: float(s["total_points"]) for pid, s in live.items()}
    minutes = {pid: float(s["minutes"]) for pid, s in live.items()}
    proposal = json.loads(PROPOSAL.read_text())
    result = {"gw": GW, "average_entry_score": event.get("average_entry_score"), "scenarios": {}}
    for key in ("wildcard_playable", "wildcard_fodder", "plan"):
        p = proposal[key]
        positions = {s["player_id"]: s["pos"] for s in p["squad"]}
        counted, subs = automatic_substitutions(positions, p["gw7_xi_ids"], p["gw7_bench_ids"], minutes)
        captain = p["gw7_captain_id"] if minutes.get(p["gw7_captain_id"], 0) > 0 else (
            p["gw7_vice_id"] if minutes.get(p["gw7_vice_id"], 0) > 0 else None)
        gross = sum(points.get(i, 0.0) for i in counted) + (points.get(captain, 0.0) if captain else 0.0)
        hit = p.get("gw7_hit", 0)
        names = {s["player_id"]: s["name"] for s in p["squad"]}
        result["scenarios"][key] = {
            "gross": gross, "hit": hit, "net": gross - hit,
            "captain_scored": names.get(captain), "autosubs": [f"{names[o]} -> {names[i]}" for o, i in subs],
            "players": [{"name": names[i], "minutes": minutes.get(i, 0), "points": points.get(i, 0),
                         "counted": i in counted} for i in p["gw7_xi_ids"] + p["gw7_bench_ids"]],
            "projected_gw7_10_gain_vs_keeping": p["projected_gw7_10_gain_vs_keeping"],
        }
    history = get(f"{API}/entry/{ENTRY}/history/")
    row = next(r for r in history["current"] if r["event"] == GW)
    picks = get(f"{API}/entry/{ENTRY}/event/{GW}/picks/")
    names = {e["id"]: e["web_name"] for e in bootstrap["elements"]}
    result["actual"] = {
        "gross": row["points"], "hit": row["event_transfers_cost"], "net": row["points"] - row["event_transfers_cost"],
        "active_chip": picks.get("active_chip"),
        "squad": [names[p["element"]] for p in sorted(picks["picks"], key=lambda p: p["position"])],
        "captain": next(names[p["element"]] for p in picks["picks"] if p["is_captain"]),
    }
    (OUT / f"result_gw{GW}.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
    a = result["actual"]
    lines = [f"# GW7 wildcard backtest (pre-registered 2026-10-07, scored after GW{GW} settled)", "",
             f"GW{GW} average entry score: {result['average_entry_score']}.", "",
             "| Team | GW7 points (net of hits) | Gross | Hits | Captain who scored |", "|---|---|---|---|---|",
             f"| **Your actual team** | **{a['net']}** | {a['gross']} | {a['hit']} | {a['captain']} |"]
    labels = {"wildcard_playable": "Wildcard (primary, playable bench)", "wildcard_fodder": "Wildcard (fodder bench)",
              "plan": "Planned squad, frozen lineup"}
    for key, label in labels.items():
        s = result["scenarios"][key]
        lines.append(f"| {label} | {s['net']:.0f} | {s['gross']:.0f} | {s['hit']} | {s['captain_scored']} |")
    w = result["scenarios"]["wildcard_playable"]
    lines += ["", f"**Wildcard minus your actual team: {w['net'] - a['net']:+.0f} points in GW{GW}.** "
              f"The Wildcard projected +27 over the plan across GW7–10 (about +7 a week). One week is far too noisy "
              f"to judge it on: a single gameweek's spread is roughly ±15–20 points.", "",
              f"Your GW7 squad: {', '.join(a['squad'])} (chip: {a['active_chip'] or 'none'})."]
    for key, label in labels.items():
        s = result["scenarios"][key]
        lines += ["", f"## {label}", f"Autosubs: {', '.join(s['autosubs']) or 'none'}", ""]
        lines += [f"- {r['name']}: {r['minutes']:.0f} min, {r['points']:.0f} pts{' (counted)' if r['counted'] else ''}"
                  for r in s["players"]]
    (OUT / "README.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[:12]))


if __name__ == "__main__":
    main()

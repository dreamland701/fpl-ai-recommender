#!/usr/bin/env python3
"""The weekly chip line for Wes's entry: what the planner rule and the G8 compact policy would do this week.

Wes (2026-10-12): "tell me when it predicts would be the best time for chip usage for this half".
Builds the live decision state from the public FPL API (the squad entered for the last gameweek, bank,
chips already used this half) and the live classic forecasts, then shows the priced chip options the
policies see, the planner rule's move and the G8 compact adapter's reply. G8 compact is the best policy
on held-out seasons so far (+66 over the planner on two halves, ~1.3 sigma), so this is a shadow
opinion next to the rule, not a new decision engine (memory: fpl-chip-timing-room).

usage: live_chip_line.py --event 7 --tag gw7final_2627 [--adapter artifacts/gemma4_e4b_g8_compact] [--no-llm]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
import urllib.request
from dataclasses import replace
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")
from fpl_ai.chip_advisor import options_prompt, parse_week_choice  # noqa: E402
from fpl_ai.grpo_env import WeeklyState  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, MAX_HORIZON, PlanEnvV2, chip_half  # noqa: E402
from fpl_ai.rules import selling_price  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer  # noqa: E402

ENTRY = 6535607
API = "https://fantasy.premierleague.com/api"
CHIP_NAMES = {"wildcard": "wildcard", "freehit": "free_hit", "bboost": "bench_boost", "3xc": "triple_captain"}


def get(path):
    with urllib.request.urlopen(f"{API}/{path}", timeout=30) as r:
        return json.load(r)


def live_state(event: int, tag: str, season: str) -> tuple[WeeklyState, dict]:
    boot = get("bootstrap-static/")
    elements = {e["id"]: e for e in boot["elements"]}
    fixtures = get(f"fixtures/?event={event}")
    per_team = {}
    for f in fixtures:
        for t in (f["team_h"], f["team_a"]):
            per_team[t] = per_team.get(t, 0) + 1
    forecasts = []
    # 2026-10-26: since GW6 the weekly refresh writes live_<tag>_f6_examples.jsonl (the GW5 one wrote _classic_);
    # take whichever exists so the chip line no longer dies on the tag mismatch.
    candidates = [ROOT / "reports" / f"live_{tag}_{kind}_examples.jsonl" for kind in ("classic", "f6")]
    examples_path = next((c for c in candidates if c.exists()), None)
    if examples_path is None:
        raise SystemExit(f"no live examples for tag {tag}: tried {[str(c) for c in candidates]}")
    for line in open(examples_path):
        r = json.loads(line); m = r["metadata"]; b = m["baseline_forecast"]
        e = elements.get(int(m["player_id"]))
        if e is None:
            continue
        forecasts.append(PlayerForecast(season=season, week=event, player_id=int(m["player_id"]), player_name=m["player_name"],
                                        team_id=int(m["team_id"]), position=m["position"], price=e["now_cost"] / 10,
                                        predicted_minutes=float(b["baseline_minutes_1gw"]), predicted_points_1gw=float(b["baseline_points_1gw"]),
                                        predicted_points_3gw=float(b["baseline_points_3gw"]), predicted_points_5gw=float(b["baseline_points_5gw"]),
                                        appearance_probability=float(b["baseline_appearance_probability"]),
                                        fixture_count=per_team.get(e["team"], 0), uncertainty=float(b["baseline_uncertainty"])))
    # schedule ahead within the half: doubles and blanks per gameweek (teams), from the published fixture list
    half_end = 19 if chip_half(event) == 1 else 38
    schedule, calendar = [], []
    prev_last = None
    for ev in range(event, half_end + 1):
        per = {}
        kicks = []
        for f in get(f"fixtures/?event={ev}"):
            for t in (f["team_h"], f["team_a"]):
                per[t] = per.get(t, 0) + 1
            if f.get("kickoff_time"):
                kicks.append(datetime.fromisoformat(f["kickoff_time"].replace("Z", "+00:00")))
        schedule.append((ev, sum(1 for v in per.values() if v >= 2), 20 - len(per)))
        if kicks:
            first, last = min(kicks), max(kicks)
            gap = (first - prev_last).days if prev_last else None
            calendar.append({"event": ev, "first": first, "last": last, "gap": gap, "span_days": (last - first).days + 1})
            prev_last = last
    # European midweeks (UCL/UEL/UECL, data/competition_fixtures/european_fixtures.jsonl) per club, this season
    euro = {}
    aliases = {"Tottenham": "Spurs", "Man United": "Man Utd", "Coventry": "Coventry City", "Hull": "Hull City", "Ipswich": "Ipswich Town"}
    name_to_id = {t["name"]: t["id"] for t in boot["teams"]}
    euro_path = ROOT / "data" / "competition_fixtures" / "european_fixtures.jsonl"
    if euro_path.exists():
        for line in euro_path.read_text().splitlines():
            try:
                r = json.loads(line)
            except json.JSONDecodeError:
                continue
            if int(r.get("season_start_year", 0)) != int(season[:4]):
                continue
            when = datetime.fromisoformat(str(r["date_utc"]).replace("Z", "+00:00").replace(" ", "T"))
            for side in ("home", "away"):
                tid = name_to_id.get(aliases.get(r.get(side), r.get(side)))
                if tid:
                    euro.setdefault(tid, []).append(when)
    history = get(f"entry/{ENTRY}/history/")
    last = history["current"][-1]
    picks = get(f"entry/{ENTRY}/event/{last['event']}/picks/")
    purchase = {}
    for p in ROOT.glob("reports/gw*_packet_*/entered_squad_gw*.json"):
        for s in json.load(open(p))["squad"]:
            purchase.setdefault(s["player_id"], s["price"])  # earliest known purchase price
    by_id = {f.player_id: f for f in forecasts}
    squad = []
    for p in picks["picks"]:
        pid = p["element"]; e = elements[pid]; now = e["now_cost"] / 10
        bought = purchase.get(pid, now)
        f = by_id.get(pid)
        squad.append(SquadPlayer(pid, e["web_name"], e["team"], f.position if f else {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}[e["element_type"]],
                                 selling_price(bought, now), bought))
    used = {CHIP_NAMES.get(c["name"], c["name"]) for c in history["chips"] if chip_half(int(c["event"])) == chip_half(event)}
    chips = {chip_half(event): frozenset(c for c in CHIPS if c not in used)}
    state = WeeklyState(season=season, week=event, squad=squad, bank=last["bank"] / 10, free_transfers=1,
                        forecasts=forecasts, actual_points={}, actual_minutes={})
    info = {"deadline": next(ev["deadline_time"] for ev in boot["events"] if ev["id"] == event), "last_event": last["event"],
            "points_last": last["points"], "total": last["total_points"], "bank": last["bank"] / 10, "chips_used_this_half": sorted(used),
            "missing_forecast": [s.player_name for s in squad if s.player_id not in by_id], "schedule": schedule,
            "calendar": calendar, "euro": euro, "squad_clubs": sorted({s.team_id for s in squad}),
            "team_names": {t["id"]: t["short_name"] for t in boot["teams"]}}
    return state, chips, info


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--event", type=int, required=True)
    ap.add_argument("--tag", required=True, help="live file tag, e.g. gw7final_2627")
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--adapter", default=str(ROOT / "artifacts" / "gemma4_e4b_g8_compact"))
    ap.add_argument("--no-llm", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()
    state, chips, info = live_state(args.event, args.tag, args.season)
    # the policy reads "best of the next 4 weeks" from the origin forecasts only, so later weeks are placeholders
    states = [state] + [replace(state, week=state.week + k) for k in range(1, MAX_HORIZON) if state.week + k <= 38]
    # with the bench boost still held, a wildcard is rebuilt to value the bench for the week after (chip
    # sequencing test 10-12, reports/chip_timing/wildcard_bench_boost.md: bench boost after it 8.3 vs 4.3,
    # half total +4.7 over 208 wildcard weeks)
    env = PlanEnvV2(states, optimize, chips=chips, wildcard_bench="bench_boost" in chips[chip_half(args.event)])
    prompt, facts = options_prompt(env)
    planner = env.baseline_plan()[0]
    options = "\n".join(l for l in prompt.splitlines() if l.startswith("- ") and any(c in l for c in ("Captain", "Bench Boost", "Free Hit", "Wildcard")))
    lines = [f"# Chip line: GW{args.event} (deadline {info['deadline']})", "",
             f"Entry {ENTRY}: GW{info['last_event']} {info['points_last']} pts, total {info['total']}, bank £{info['bank']:.1f}; "
             f"chips used this half: {info['chips_used_this_half'] or 'none'}; chips left: {sorted(chips[chip_half(args.event)])}", ""]
    if info["missing_forecast"]:
        lines.append(f"(no live forecast for: {', '.join(info['missing_forecast'])})\n")
    # schedule rule (reports/chip_timing tables, 12 halves): holding TC/BB for the biggest known double gameweek and
    # playing FH in the biggest blank beat the planner's 5-week rule by ~+5 and ~+14 per half when such weeks exist
    doubles = [(ev, d) for ev, d, b in info["schedule"] if d >= 6]
    blanks = [(ev, b) for ev, d, b in info["schedule"] if b >= 6]
    sched = ", ".join(f"GW{ev}: {d} teams double" for ev, d in doubles) + ("; " if doubles and blanks else "") \
        + ", ".join(f"GW{ev}: {b} teams blank" for ev, b in blanks) or "no double or blank gameweek published for the rest of this half"
    rule = []
    if doubles:
        rule.append(f"hold triple captain and bench boost for GW{max(doubles, key=lambda x: x[1])[0]}")
    if blanks:
        rule.append(f"free hit in GW{max(blanks, key=lambda x: x[1])[0]}")
    # calendar: when each remaining round is played, rest before it, and which of the squad's clubs play in Europe
    # in the four days before it (measured effects are small: post-break Man City start 75% vs 80%, a European
    # midweek costs about 1.5 points of start rate; tie-breakers between otherwise equal chip weeks, not drivers)
    cal = ["", "| GW | first kickoff | days since last round | round spans | squad clubs with Europe in the 4 days before | note |",
           "|---|---|---|---|---|---|"]
    for c in info["calendar"]:
        clubs = [info["team_names"][t] for t in info["squad_clubs"]
                 if any(0 <= (c["first"] - e).days <= 4 and e < c["first"] for e in info["euro"].get(t, []))]
        note = []
        if c["gap"] is not None and c["gap"] >= 10:
            note.append("post-break")
        if c["gap"] is not None and c["gap"] <= 3:
            note.append("congested")
        if c["first"].month == 12 and c["first"].day >= 20 or (c["first"].month == 1 and c["first"].day <= 3):
            note.append("festive rotation")
        cal.append(f"| {c['event']} | {c['first']:%a %d %b} | {c['gap'] if c['gap'] is not None else '-'} | {c['span_days']} d | "
                   f"{', '.join(clubs) or '-'} | {', '.join(note)} |")
    lines += ["## Schedule ahead", "", sched + ".", ("Schedule rule: " + "; ".join(rule) + ".") if rule else
              "Schedule rule: nothing to wait for; the chips expire at the end of the half, so take the best week the forecasts show.",
              *cal, "",
              "## Priced options this week (what both policies see)", "", options, "",
              f"## Planner rule: chip **{planner.chip}**, transfer {planner.transfer}, captain = forecast-best"]
    if not args.no_llm:
        spec = importlib.util.spec_from_file_location("plan_eval", ROOT / "scripts" / "run_grpo_plan_eval.py")
        plan_eval = importlib.util.module_from_spec(spec); spec.loader.exec_module(plan_eval)
        generate = plan_eval.load_generator("google/gemma-4-E4B-it", args.adapter, chat_template=True)
        text = generate(prompt, 8)
        choice = parse_week_choice(text, facts)
        names = {f.player_id: f.player_name for f in state.forecasts}
        verdict = (f"chip **{choice.chip}**, captain {names.get(choice.captain, choice.captain) if choice.captain else 'forecast-best'}"
                   if choice else "unparseable reply (would fall back to the planner)")
        lines += ["", f"## G8 compact (shadow): {verdict}", "", "```", text.strip()[-600:], "```"]
    out = "\n".join(lines) + "\n"
    print(out)
    if args.output:
        Path(args.output).write_text(out)


if __name__ == "__main__":
    main()

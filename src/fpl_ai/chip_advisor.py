"""G7 chip and captain advisor: the LLM decides this week's chip, captain and transfer count from
explicitly priced options, after a short piece of reasoning.

Wes (2026-10-10): "if we prompt it in the right way and give it options to think through, at what
week and whether to use this, [it] should be able to come up with some policy better than nothing".
G5 asked for a whole five-week plan from a dense state dump; here the decision is the one a manager
actually makes each week, and each option comes with the numbers that matter for it:
  - this week: projected points with no chip (after the best single transfer), and what Triple
    Captain, Bench Boost, Free Hit and Wildcard would each add by the forecasts;
  - the next weeks: the best captain and the bench total per week, so "now or later" can be judged;
  - how many weeks are left before this half's chips expire.
Scored with grpo_plan_env_v2.receding_value (this week's action, then the planner, plus held-chip
values), exactly like the closed-loop evaluation.
"""
from __future__ import annotations

import json
import re
from typing import Dict, List, Optional, Tuple

from .grpo_plan_env_v2 import CHIPS, FIRST_HALF_LAST_WEEK, PLANNER_DISCIPLINE, PlanEnvV2, WeekAction, chip_half, outlook_points

SEASON_LAST_WEEK = 38
# Median realised week-1 gain of playing the chip vs not, over the 120 G5 training windows
# (scripts/compute_g6_chip_values.py); shown to the model as the "typical week" reference.
FH_TYPICAL = 8.0
WC_TYPICAL = 5.0
CHIP_LABEL = {"triple_captain": "Triple Captain", "bench_boost": "Bench Boost", "free_hit": "Free Hit", "wildcard": "Wildcard"}


def _projected(squad_ids, table, value_key="p1") -> Tuple[float, float, List[int]]:
    """Projected XI points (best formation, no captain bonus), bench points, and squad ids by value."""
    vals = sorted(((table[pid][value_key], pid) for pid in squad_ids if pid in table), reverse=True)
    return sum(v for v, _ in vals[:11]), sum(v for v, _ in vals[11:15]), [pid for _, pid in vals]


def options_prompt(env: PlanEnvV2, labels: bool = False) -> Tuple[str, Dict]:
    """The decision prompt for the env's first week, and the facts behind it (for parsing and logs).

    labels=False (default since G7b) leaves out the season and gameweek numbers and describes timing
    relative to now ("in 2 weeks", "N weeks left"): G7, trained with labels, scored +135 over the planner
    on a season it trained on and -68 on a held-out one, i.e. it memorised which weeks paid off.
    """
    def when(week):
        if labels:
            return f"GW{week}"
        ahead = week - env.states[0].week
        return "this week" if ahead == 0 else f"in {ahead} week{'s' if ahead > 1 else ''}"
    start = env.states[0]
    table = env._forecast_table(start)
    squad = env._start_squad()
    env._refresh_sell(squad, table)
    half = chip_half(start.week)
    half_end = FIRST_HALF_LAST_WEEK if half == 1 else SEASON_LAST_WEEK
    chips_left = sorted(env.chips[half])

    best1 = env._move(0, squad, "best1")
    after, _ = env._apply(squad, best1, table, wildcard=False)
    xi_pts, bench_pts, ranked = _projected(after.players, table)
    xi, bench, captain, vice = env._lineup(after, table)
    cap_pts = table[captain]["p1"]
    no_chip = sum(table[p]["p1"] for p in xi) + cap_pts
    captains = sorted(xi, key=lambda p: -table[p]["p1"])[:3]

    # captain and bench totals for the coming weeks (current squad after the transfer, origin forecasts)
    ids = list(after.players)
    ahead = []
    for k in range(env.horizon):
        vals = sorted(((outlook_points(f, k), f.player_id, f.player_name) for f in start.forecasts if f.player_id in ids), reverse=True)
        if vals:
            ahead.append((start.week + k, vals[0][0], vals[0][2], sum(v for v, _, _ in vals[11:15])))

    def best_later(index):
        later = ahead[1:]
        if not later:
            return ""
        week, value = max(((w, row[index]) for w, *row in [(a[0], a[1], a[2], a[3]) for a in later]), key=lambda x: x[1])
        return f"; best of the next {len(later)} weeks: +{value:.1f} {when(week)}"

    lines = []
    if "triple_captain" in chips_left:
        lines.append(f"- Triple Captain ({table[captain]['name']}): +{cap_pts:.1f} this week" + best_later(0))
    if "bench_boost" in chips_left:
        lines.append(f"- Bench Boost: +{sum(table[p]['p1'] for p in bench[:4]):.1f} this week (bench: "
                     + ", ".join(f"{table[p]['name']} {table[p]['p1']:.1f}" for p in bench[:4]) + ")" + best_later(2))
    if "free_hit" in chips_left:
        fh = env._move(0, squad, "free_hit")
        fh_ids = [p for p in after.players if p not in fh["out"]] + list(fh["in"])
        fh_xi, _, fh_rank = _projected(fh_ids, table)
        fh_total = fh_xi + table[fh_rank[0]]["p1"]
        lines.append(f"- Free Hit: one-week rebuild, {fh_total:.1f} projected ({fh_total - no_chip:+.1f} vs no chip); squad reverts next week")
    if "wildcard" in chips_left:
        wc = env._move(0, squad, "wildcard")
        wc_ids = [p for p in after.players if p not in wc["out"]] + list(wc["in"])
        wc5, _, _ = _projected(wc_ids, table, "p5")
        cur5, _, _ = _projected(after.players, table, "p5")
        lines.append(f"- Wildcard: permanent rebuild of {len(wc['in'])} players, {wc5 - cur5:+.1f} projected over the next five weeks")

    outlook = [f"{when(w).capitalize()}: best captain {name} {cap:.1f}, bench {bench_total:.1f}" for w, cap, name, bench_total in ahead]

    hold_move = "; ".join(f"{table[o]['name'] if o in table else o} -> {table[i]['name'] if i in table else i}"
                          for o, i in zip(best1["out"], best1["in"])) or "no transfer worth making"
    best2 = env._move(0, squad, "best2")
    best2_txt = "; ".join(f"{table[o]['name'] if o in table else o} -> {table[i]['name'] if i in table else i}"
                          for o, i in zip(best2["out"], best2["in"])) or "same as best1"
    weeks_left = half_end - start.week + 1
    prompt = (
        (f"You manage an FPL team. Decide this week's move: {start.season} GW{start.week}.\n" if labels
           else "You manage an FPL team. Decide this week's move.\n")
        + f"Bank £{squad.bank:.1f}, free transfers {squad.free_transfers}.\n"
        f"Chips left this half: {', '.join(CHIP_LABEL[c] for c in chips_left) or 'none'}. "
        f"Each chip can be used once and is lost if not used within the next {weeks_left} weeks (this one included).\n\n"
        f"This week with no chip: {no_chip:.1f} projected points after the best single transfer ({hold_move}), "
        f"captain {table[captain]['name']} {cap_pts:.1f}.\n"
        + ("Chip options this week, by the forecasts:\n" + "\n".join(lines) + "\n" if lines else "")
        + "Coming weeks with your current squad (forecasts get vaguer further out):\n" + "\n".join(outlook) + "\n\n"
        + ("Transfers are handled for you: the best single move is made only when it clearly beats banking the free "
           "transfer. You decide the chip and the captain.\n" if PLANNER_DISCIPLINE else
           f"Transfer options: \"hold\" (bank the free transfer), \"best1\" ({hold_move}), \"best2\" ({best2_txt}; "
           f"extra transfers beyond your free ones cost 4 points each).\n")
        + 
        f"Captain options: " + ", ".join(f"{table[p]['name']} (id {p}, {table[p]['p1']:.1f})" for p in captains) + ".\n\n"
        "How to decide: a chip played now cannot be played in a better week later this half. Play Triple Captain or "
        "Bench Boost only if this week is at least as good as the coming weeks shown; with only a few weeks left, use "
        "them before they expire. Later weeks' forecasts are two-week averages, so they look flatter than this week's: "
        "a coming week within a point or two of this one is usually just as good. Free Hit and Wildcard forecasts are "
        "optimistic: in past seasons they gained about "
        f"{FH_TYPICAL:+.0f} and {WC_TYPICAL:+.0f} real points in a typical week, so save them for a week whose forecast "
        "gain is exceptional. Think it through in at most three short sentences, comparing this week with the coming "
        "weeks for each chip you hold. Then give your decision as one JSON object on the last line: "
        + ("{\"chip\": \"none\"|\"triple_captain\"|\"bench_boost\"|\"free_hit\"|\"wildcard\", \"captain\": <id>}" if PLANNER_DISCIPLINE else
           "{\"chip\": \"none\"|\"triple_captain\"|\"bench_boost\"|\"free_hit\"|\"wildcard\", \"captain\": <id>, \"transfer\": \"hold\"|\"best1\"|\"best2\"}")
    )
    return prompt, {"chips": chips_left, "captains": captains, "no_chip": no_chip}


def parse_week_choice(text: str, facts: Dict) -> Optional[WeekAction]:
    """The last JSON object in the reply; chip must be available and the captain one of the options."""
    for match in reversed(list(re.finditer(r"\{[^{}]*\}", text))):
        try:
            obj = json.loads(match.group(0))
        except json.JSONDecodeError:
            continue
        chip = obj.get("chip", "none")
        transfer = "auto" if PLANNER_DISCIPLINE else obj.get("transfer", "best1")
        captain = obj.get("captain")
        if chip != "none" and chip not in facts["chips"]:
            return None
        if transfer not in ("hold", "best1", "best2", "auto"):
            return None
        if captain is not None and (isinstance(captain, bool) or not isinstance(captain, int) or captain not in facts["captains"]):
            captain = None
        return WeekAction(transfer=transfer, captain=captain, chip=chip)
    return None

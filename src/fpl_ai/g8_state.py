"""G8 policy state: the weekly prompt for the chip and captain policy, in two sizes.

Wes (2026-10-11): give the RL policy "rich info", all as text. "compact" is the G7b advisor prompt
(forecasts, priced chip options, captain candidates). "rich" adds, for every squad player and the
best alternatives, the classic model's inputs a manager reads: recent points, minutes, xG/xA,
price, ownership, transfer trend, P(appear), the next five fixtures (home/away, difficulty) and,
when the player had any, a pre-deadline article excerpt (published 12 h+ before the deadline,
as a live decision sees). Comparing the two on held-out half-seasons tells whether more input helps.

No season or gameweek labels anywhere (G7 memorised weeks from them).
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, Tuple

import pandas as pd

from .chip_advisor import options_prompt
from .grpo_plan_env_v2 import FIRST_HALF_LAST_WEEK, PlanEnvV2

ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT / "data" / "fpl_training_rows_v3_contract_f6.csv"
CORPORA = [ROOT / "reports" / "llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38" / "train.jsonl",
           ROOT / "reports" / "llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38" / "eval.jsonl",
           ROOT / "reports" / "llm_residual_v2_e20_contract_top256_eval_2627_2_5" / "eval.jsonl"]
COLUMNS = ["season", "week", "player_id", "player_name", "position", "price_pre_deadline", "selected_by_percent_pre_deadline",
           "transfer_balance_prev_event", "points_avg_3", "points_avg_5", "minutes_avg_3", "minutes_avg_5",
           "expected_goals_avg_3", "expected_assists_avg_3", "fixture_difficulty_mean", "home_fixture_count", "fixture_count"]
DOC = re.compile(r"\n\[\d+\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)\nText: ([^\n]*)")
ARTICLE_CUTOFF_HOURS = 12


class FeatureLookup:
    """Pre-deadline player features and article excerpts by (season, week, player_id)."""

    def __init__(self, with_articles: bool = True):
        t = pd.read_csv(TABLE, usecols=COLUMNS, low_memory=False)
        self.rows = {(r.season, int(r.week), int(r.player_id)): r for r in t.itertuples(index=False)}
        # schedule only (difficulty, home/away) is read from later weeks: no outcomes, no later form
        self.fixtures = {(r.season, int(r.week), int(r.player_id)): (int(r.fixture_count or 0), float(r.fixture_difficulty_mean or 0),
                                                                     int(r.home_fixture_count or 0)) for r in t.itertuples(index=False)}
        self.articles: Dict[Tuple[str, int, int], str] = {}
        if with_articles:
            for path in CORPORA:
                for line in open(path):
                    r = json.loads(line)
                    d = r.get("deadline_ts")
                    if not isinstance(d, str) or d in ("", "nan"):
                        continue
                    deadline = datetime.fromisoformat(d.replace("Z", "+00:00"))
                    docs = [x for x in DOC.findall("\n" + r["prompt"].split("Timestamp-safe text evidence:", 1)[-1])
                            if (deadline - datetime.fromisoformat(x[1].replace("Z", "+00:00"))).total_seconds() >= ARTICLE_CUTOFF_HOURS * 3600]
                    # keep only excerpts that name him as FPL does: surname matching at attach time picks up
                    # namesakes (Raya Martin got a lower-league "Martin"; Antonee Robinson got Karl Robinson)
                    web = re.search(r"- Player: (.*)", r["prompt"])
                    web = web.group(1).strip() if web else ""
                    docs = [x for x in docs if web and (web in x[3] or web in x[2])]
                    if docs:
                        src, _, title, text = docs[0]
                        self.articles[(r["season"], int(r["week"]), int(r["metadata"]["player_id"]))] = \
                            f"{src.strip()}: \"{title.strip()[:80]}\" {text.strip()[:160]}"

    def fixture_text(self, season: str, week: int, pid: int) -> str:
        out = []
        for k in range(5):
            f = self.fixtures.get((season, week + k, pid))
            if f is None:
                out.append("?")
            elif f[0] == 0:
                out.append("blank")
            else:
                ha = "H" if f[2] >= f[0] else ("A" if f[2] == 0 else "H+A")
                out.append(f"{ha}{f[1]:.0f}" + ("x2" if f[0] > 1 else ""))
        return " ".join(out)


def _player_line(lookup: FeatureLookup, forecast, season: str, week: int, with_articles: bool, sell=None) -> str:
    r = lookup.rows.get((season, week, forecast.player_id))
    price = f"£{sell:.1f}" if sell is not None else f"£{forecast.price:.1f}"
    line = (f"{forecast.player_name} ({forecast.position}, {price}, id {forecast.player_id}): forecast {forecast.predicted_points_1gw:.1f} "
            f"/ {forecast.predicted_points_3gw:.1f} / {forecast.predicted_points_5gw:.1f} (1/3/5 wk), P(plays) {forecast.appearance_probability:.2f}")
    if r is not None:
        line += (f"; last 3/5: {r.points_avg_3:.1f}/{r.points_avg_5:.1f} pts, {r.minutes_avg_3:.0f}/{r.minutes_avg_5:.0f} min, "
                 f"xG {r.expected_goals_avg_3:.2f} xA {r.expected_assists_avg_3:.2f}; owned {r.selected_by_percent_pre_deadline:.1f}%, "
                 f"net transfers {r.transfer_balance_prev_event:+,.0f}")
    line += f"; next 5 (H/A + difficulty): {lookup.fixture_text(season, week, forecast.player_id)}"
    if with_articles and (season, week, forecast.player_id) in lookup.articles:
        line += f"\n    news: {lookup.articles[(season, week, forecast.player_id)]}"
    return line


def schedule_ahead(states, i: int, n: int = 6):
    """(week, teams with two fixtures, teams with none) for the next n weeks after states[i], from the
    fixture counts in those weeks' forecasts: the schedule as published a few weeks out, no outcomes."""
    out = []
    for k in range(1, n + 1):
        if i + k >= len(states):
            break
        per_team: Dict[int, int] = {}
        for f in states[i + k].forecasts:
            per_team[f.team_id] = max(per_team.get(f.team_id, 0), f.fixture_count)
        teams = max(20, len(per_team))
        out.append((states[i + k].week, sum(1 for v in per_team.values() if v >= 2), teams - sum(1 for v in per_team.values() if v >= 1)))
    return out


def g9_lines(env: PlanEnvV2, schedule, recent) -> str:
    """G9 (10-12): the two signals the chip-timing tables pointed at — the schedule ahead (doubles and
    blanks are where chip timing pays) and squad health (a wildcard pays when the squad is broken, not
    when the projection is big)."""
    start = env.states[0]
    squad_ids = {p.player_id for p in start.squad}
    fc = [f for f in start.forecasts if f.player_id in squad_ids]
    papp = [f.appearance_probability for f in fc]
    flagged = [f.player_name for f in fc if f.appearance_probability < 0.5]
    weeks_left = (FIRST_HALF_LAST_WEEK if start.week <= FIRST_HALF_LAST_WEEK else 38) - start.week + 1
    sched = [f"in {w - start.week} week{'s' if w - start.week > 1 else ''}: " + ", ".join(
        ([f"{d} teams double"] if d >= 4 else []) + ([f"{b} teams blank"] if b >= 4 else []))
        for w, d, b in (schedule or []) if d >= 4 or b >= 4]
    lines = [f"Weeks left in this half (unused chips expire after it): {weeks_left}.",
             "Schedule ahead: " + ("; ".join(sched) if sched else "no double or blank gameweek published within six weeks") + "."]
    if papp:
        health = f"Squad health: {len(flagged)} of {len(fc)} doubtful or out" + (f" ({', '.join(flagged[:5])})" if flagged else "") \
            + f", average chance of playing {sum(papp) / len(papp):.0%}"
        if recent:
            health += f"; last {len(recent)} week{'s' if len(recent) > 1 else ''} scored {sum(recent) / len(recent):.0f} per week"
        lines.append(health + ".")
    return "\n".join(lines) + "\n\n"


def g8_prompt(env: PlanEnvV2, detail: str = "rich", lookup: Optional[FeatureLookup] = None,
              with_articles: bool = True, n_alternatives: int = 10, schedule=None, recent=None) -> Tuple[str, Dict]:
    """compact = the G7b advisor prompt; rich = that plus a full per-player brief; g9 = compact plus the
    schedule-ahead and squad-health lines (`schedule` from schedule_ahead(), `recent` = this rollout's
    realised points so far)."""
    base, facts = options_prompt(env)
    if detail == "compact":
        return base, facts
    if detail == "g9":
        cut = base.index("How to decide:")
        return base[:cut] + g9_lines(env, schedule, recent) + base[cut:], facts
    assert lookup is not None
    start = env.states[0]
    table = {f.player_id: f for f in start.forecasts}
    sell = {p.player_id: p.sell_price for p in start.squad}
    squad = sorted((table[pid] for pid in sell if pid in table), key=lambda f: ("GKDEFMIDFWD".index(f.position), -f.predicted_points_1gw))
    alts = sorted((f for f in start.forecasts if f.player_id not in sell), key=lambda f: -f.predicted_points_5gw)[:n_alternatives]
    brief = ("Your squad, player by player:\n"
             + "\n".join("- " + _player_line(lookup, f, start.season, start.week, with_articles, sell[f.player_id]) for f in squad)
             + "\n\nBest players outside your squad (5-week forecast):\n"
             + "\n".join("- " + _player_line(lookup, f, start.season, start.week, False) for f in alts)
             + "\n\nFixture difficulty: 1 = easiest, 5 = hardest; x2 = double gameweek.\n\n")
    cut = base.index("How to decide:")
    return base[:cut] + brief + base[cut:], facts

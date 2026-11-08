#!/usr/bin/env python3
"""How much is there to win in the captain choice among the forecast's top candidates?

The advisor / G8 prompt offers the three highest-forecast XI players. Per half-season, on the no-chip
closed loop: the points the forecast-best captain actually added (the planner's choice), the hindsight
best of the top 3 (an upper bound on choosing among the offered candidates), and the hindsight best of
the whole XI (for scale). Also: how often the forecast-best was the best of the three.
"""
import sys
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src")); sys.path.insert(0, str(ROOT / "scripts"))
import os; os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")
from chip_timing_tables import ALL_HALVES, half_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, PlanEnvV2, WeekAction  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

rows = []
for item in ALL_HALVES:
    season, half = item.split(":"); states = half_states(season, int(half))
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, chosen, top3, xi_best, hits3 = None, 0.0, 0.0, 0.0, 0
    for state in states:
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state], optimize, chips=chips)
        table = env._forecast_table(state); squad = env._start_squad(); env._refresh_sell(squad, table)
        xi, bench, captain, vice = env._lineup(squad, table)
        pts = lambda pid: state.actual_points.get(pid, 0.0) if state.actual_minutes.get(pid, 0.0) > 0 else 0.0  # noqa: E731
        cands = sorted(xi, key=lambda p: -table[p]["p1"])[:3]
        chosen += pts(captain); best3 = max(pts(p) for p in cands); top3 += best3; xi_best += max(pts(p) for p in xi)
        hits3 += pts(captain) == best3
        _, _, carried = env.rollout([WeekAction(transfer="auto")], return_state=True); chips = carried["chips"]
    rows.append((item, chosen, top3, xi_best, hits3, len(states)))
lines = ["# Captain choice: room among the offered candidates (no-chip loop, extra points from the armband)", "",
         "| Half | Forecast-best captain | Hindsight best of top 3 | Room (top 3) | Hindsight best of XI | Forecast-best was best of 3 |", "|---|---|---|---|---|---|"]
for item, c, t3, xb, h, n in rows:
    lines.append(f"| {item} | {c:.0f} | {t3:.0f} | +{t3 - c:.0f} | {xb:.0f} | {h}/{n} |")
T = [sum(r[i] for r in rows) for i in range(1, 6)]
lines.append(f"| **total** | {T[0]:.0f} | {T[1]:.0f} | +{T[1] - T[0]:.0f} | {T[2]:.0f} | {T[3]}/{T[4]} |")
(ROOT / "reports" / "chip_timing" / "captain_room.md").write_text("\n".join(lines) + "\n"); print("\n".join(lines))

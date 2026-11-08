#!/usr/bin/env python3
"""Value of holding free hit and wildcard, for the receding-horizon GRPO reward.

For every G5 training window, the realised gain of playing the chip in week 1 (then the planner)
over best single transfer with no chip (then the planner). A chip can be played once per half, so
holding it is worth roughly what it gains in a good week, not an average one: the value stored is
the 75th percentile of the week-1 gains (only spend it in the top quarter of weeks), floored at 0.
Triple captain and bench boost need no value: the planner continuation spends them in-window.

usage: compute_g6_chip_values.py <out.json>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import PlanEnvV2, WeekAction, receding_value  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

KEYS = ["2022-23", "2023-24", "2024-25", "2025-26-train"]


def main() -> None:
    gains = {"free_hit": [], "wildcard": []}
    for key in KEYS:
        states = sorted(load_states(ROOT / "reports" / "grpo_states_v2" / f"{key}.jsonl"), key=lambda s: s.week)
        for start in range(0, len(states) - 4):
            window = states[start:start + 5]
            if [s.week for s in window] != list(range(window[0].week, window[0].week + 5)):
                continue
            env = PlanEnvV2(window, optimize)
            base = receding_value(env, WeekAction(transfer="best1"))
            for chip in gains:
                gains[chip].append(receding_value(env, WeekAction(transfer="best1", chip=chip)) - base)
        print(f"{key}: {len(gains['free_hit'])} windows so far", flush=True)
    out = {"method": "75th percentile of realised week-1 gain over best1, floored at 0", "windows": len(gains["free_hit"])}
    for chip, g in gains.items():
        g = np.array(g)
        out[chip] = round(max(0.0, float(np.percentile(g, 75))), 1)
        out[f"{chip}_gain_quantiles"] = {q: round(float(np.percentile(g, q)), 1) for q in (10, 25, 50, 75, 90)}
        out[f"{chip}_gain_mean"] = round(float(g.mean()), 2)
    Path(sys.argv[1]).write_text(json.dumps(out, indent=1))
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""G7 chip advisor, closed loop over whole half-seasons: does the LLM, given priced options and a
moment to reason, time chips and captains better than the deterministic planner?

Every week the advisor sees the state it actually reached and chooses this week's chip, captain and
transfer count (scripts/../src/fpl_ai/chip_advisor.py). Run over every half-season in the state caches
(2022-23 to 2025-26, GW2-19 and GW20-38, fresh chips each half), next to the same-chips planner and
best-single-transfer with no chips. Zero-shot uses the base model; --adapter-path scores a trained one.
Unparseable replies fall back to the planner's move and are counted.

usage: run_chip_advisor_eval.py --output OUT.json [--adapter-path DIR] [--halves 2022-23:2,...]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.chip_advisor import options_prompt, parse_week_choice  # noqa: E402
from fpl_ai.g8_state import FeatureLookup, g8_prompt, schedule_ahead  # noqa: E402
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, FIRST_HALF_LAST_WEEK, MAX_HORIZON, PLANNER_DISCIPLINE, PlanEnvV2, WeekAction  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

FILES = {"2022-23": ["2022-23"], "2023-24": ["2023-24"], "2024-25": ["2024-25"], "2025-26": ["2025-26-train", "2025-26-holdout"]}


def season_states(season):
    states = []
    for key in FILES[season]:
        states += load_states(ROOT / "reports" / "grpo_states_v2" / f"{key}.jsonl")
    return sorted(states, key=lambda s: s.week)


def half_loop(states, choose):
    """Closed loop over one half-season; the squad, bank and free transfers carry week to week."""
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, total, log = None, 0.0, []
    for i, state in enumerate(states):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state] + list(states[i + 1:i + MAX_HORIZON]), optimize, chips=chips)
        action, note = choose(env, {"schedule": schedule_ahead(states, i), "recent": [d["realized"] for d in log[-3:]]})
        try:
            realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([action], return_state=True)
        except RuntimeError as exc:
            # the optimizer could not solve this squad's week (G9 eval 10-13: an infeasible hold); hold instead
            sq = {pid: (p.position, p.team_id, p.sell_price) for pid, p in ((p.player_id, p) for p in state.squad)}
            print(f"OPTIMIZER FAILED week {state.week} action {action} bank {state.bank} ft {state.free_transfers}: {exc}\n  squad {sq}", flush=True)
            action = replace(action, transfer="hold")
            realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([action], return_state=True)
            note = f"{note}; optimizer failed, held"
        chips = carried["chips"]
        print(f"  week {state.week}: {note} -> chip {detail[0]['chip']} transfer {detail[0]['transfer']} realized {realized:.0f}", flush=True)
        total += realized
        log.append({**detail[0], "note": note})
    return total, log


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", required=True)
    ap.add_argument("--adapter-path")
    ap.add_argument("--model-path", default="google/gemma-4-E4B-it", help="e.g. /home/wescheng/models/gemma-4-31b-it")
    ap.add_argument("--halves", default="2022-23:1,2022-23:2,2023-24:1,2023-24:2,2024-25:1,2024-25:2,2025-26:1,2025-26:2")
    ap.add_argument("--max-new-tokens", type=int, default=220)
    ap.add_argument("--detail", choices=["advisor", "compact", "rich", "g9"], default="advisor",
                    help="advisor = the G7/G7b prompt; compact/rich = the G8 state; g9 = compact + schedule + squad health (src/fpl_ai/g8_state.py)")
    args = ap.parse_args()
    spec = importlib.util.spec_from_file_location("plan_eval", ROOT / "scripts" / "run_grpo_plan_eval.py")
    plan_eval = importlib.util.module_from_spec(spec); spec.loader.exec_module(plan_eval)
    generate = plan_eval.load_generator(args.model_path, args.adapter_path, chat_template=True)

    lookup = FeatureLookup() if args.detail == "rich" else None
    results = {}
    for item in args.halves.split(","):
        season, half = item.split(":"); half = int(half)
        states = [s for s in season_states(season) if (s.week <= FIRST_HALF_LAST_WEEK) == (half == 1)]
        invalid, replies = [], []

        def advisor(env, ctx):
            prompt, facts = options_prompt(env) if args.detail == "advisor" else g8_prompt(env, args.detail, lookup, **(ctx if args.detail == "g9" else {}))
            text = generate(prompt, 8)
            choice = parse_week_choice(text, facts)
            replies.append({"week": env.states[0].week, "reply": text[-400:]})
            if choice is None:
                invalid.append(env.states[0].week)
                return env.baseline_plan()[0], "invalid -> planner"
            return choice, "advisor"

        planner = half_loop(states, lambda env, ctx: (env.baseline_plan()[0], "planner"))
        no_chips = half_loop(states, lambda env, ctx: (WeekAction(transfer="auto" if PLANNER_DISCIPLINE else "best1"), "no chips"))
        adv = half_loop(states, advisor)
        chips_used = [(d["week"], d.get("chip")) for d in adv[1] if d.get("chip", "none") != "none"]
        results[item] = {"advisor": round(adv[0], 1), "planner": round(planner[0], 1), "no_chips": round(no_chips[0], 1),
                         "invalid_weeks": invalid, "advisor_chips": chips_used,
                         "planner_chips": [(d["week"], d.get("chip")) for d in planner[1] if d.get("chip", "none") != "none"],
                         "replies": replies}
        print(f"{item}: advisor {adv[0]:.0f} | planner {planner[0]:.0f} | no chips {no_chips[0]:.0f} | invalid {len(invalid)} | "
              f"advisor chips {chips_used}", flush=True)
        Path(args.output).write_text(json.dumps(results, indent=1))
    tot = {k: sum(v[k] for v in results.values()) for k in ("advisor", "planner", "no_chips")}
    print(f"TOTAL over {len(results)} half-seasons: advisor {tot['advisor']:.0f} | planner {tot['planner']:.0f} | no chips {tot['no_chips']:.0f}")


if __name__ == "__main__":
    main()

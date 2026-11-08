#!/usr/bin/env python3
"""Closed-loop season evaluation for G5 (review P1-08, P1-09).

Every week the policy sees the state it actually reached (squad, bank, free
transfers, chips), emits a K-week plan from origin-only information, and only
the first week is executed; the state then carries to the next week. The same
loop is run for the deterministic planner (same chips; it never plays a
wildcard or free hit) and for "classic, no chips" (best single move, no chips).
Unparseable policy output falls back to the planner's action and is counted.

usage: run_grpo_plan_eval_v2.py --states reports/grpo_states_v2/2025-26-holdout.jsonl
          [--adapter-path artifacts/gemma4_e4b_grpo_plan_g5] --output OUT.json
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

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, MAX_HORIZON, PlanEnvV2, WeekAction, parse_plan  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402


def season_loop(states, choose, chips):
    """choose(env) -> WeekAction for the env's first week; returns per-week log and total."""
    carried = None
    total, log = 0.0, []
    for i, state in enumerate(states):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        window = [state] + list(states[i + 1:i + MAX_HORIZON])
        env = PlanEnvV2(window, optimize, chips=chips)
        action, note = choose(env)
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([action], return_state=True)
        chips = carried["chips"]
        total += realized
        log.append({**detail[0], "note": note})
    return total, log


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--states", required=True)
    ap.add_argument("--adapter-path", help='a G5 adapter, or "none" for the untrained policy (base model)')
    ap.add_argument("--model-path", default="google/gemma-4-E4B-it")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    states = sorted(load_states(args.states), key=lambda s: s.week)
    fresh = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    results = {}
    results["planner"] = season_loop(states, lambda env: (env.baseline_plan()[0], "planner"), dict(fresh))
    results["classic_no_chips"] = season_loop(states, lambda env: (WeekAction(transfer="best1"), "best1"),
                                              {1: frozenset(), 2: frozenset()})
    if args.adapter_path:
        spec = importlib.util.spec_from_file_location("plan_eval", ROOT / "scripts" / "run_grpo_plan_eval.py")
        plan_eval = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plan_eval)
        generate = plan_eval.load_generator(args.model_path, None if args.adapter_path == "none" else args.adapter_path,
                                            chat_template=True)
        invalid = []

        def policy(env):
            plan = parse_plan(generate(env.state_prompt(), 8), env.horizon)
            if plan is None:
                invalid.append(env.states[0].week)
                return env.baseline_plan()[0], "invalid -> planner"
            return plan[0], "policy"

        results["policy"] = season_loop(states, policy, dict(fresh))
        results["policy_invalid_weeks"] = invalid
    summary = {k: round(v[0], 1) for k, v in results.items() if isinstance(v, tuple)}
    Path(args.output).write_text(json.dumps({"summary": summary, "detail": {k: v[1] for k, v in results.items()
                                                                             if isinstance(v, tuple)},
                                             "invalid_weeks": results.get("policy_invalid_weeks", [])}, indent=1))
    print(json.dumps(summary))


if __name__ == "__main__":
    main()

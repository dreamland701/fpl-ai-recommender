#!/usr/bin/env python3
"""Live G2-v3 plan read for the current GW from the ACTUAL squad.

Builds a 3-week PlanEpisodeEnv from live adjusted forecasts (GW+1/GW+2
pseudo-weeks interpolated from the 3gw/5gw heads: wk2 = (3gw-1gw)/2,
wk3 = (5gw-3gw)/2), with llm_deltas + window evidence snippets matching
the adjusted-state-cache schema, renders state_prompt, decodes with the
G2-v3 policy (min_new_tokens=8, the deployment setting for the GRPO
empty-EOS attractor), and prints the parsed weekly actions.
"""
from __future__ import annotations

import argparse
import dataclasses
import importlib.util
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.grpo_env import WeeklyState  # noqa: E402
from fpl_ai.grpo_plan_env import PlanEpisodeEnv, parse_plan  # noqa: E402
from fpl_ai.rules import selling_price  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer  # noqa: E402


def _load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


apply_stage = _load_module("apply_stage", "apply_llm_deltas_and_draft.py")
adjusted_states = _load_module("adjusted_states", "build_adjusted_grpo_states.py")
plan_eval_spec = importlib.util.spec_from_file_location("plan_eval", ROOT / "scripts" / "run_grpo_plan_eval.py")
plan_eval = importlib.util.module_from_spec(plan_eval_spec)
plan_eval_spec.loader.exec_module(plan_eval)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examples", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--corpus", required=True, help="Evidence-attached corpus (for snippets).")
    parser.add_argument("--bootstrap-json", required=True)
    parser.add_argument("--entered-squad", required=True)
    parser.add_argument("--bank", type=float, required=True)
    parser.add_argument("--free-transfers", type=int, default=1)
    parser.add_argument("--week", type=int, required=True)
    parser.add_argument("--adapter-path", default="artifacts/gemma4_e4b_grpo_plan_v3")
    parser.add_argument("--model-path", default="google/gemma-4-E4B-it")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    examples = [json.loads(line) for line in Path(args.examples).open() if line.strip()]
    predictions = [json.loads(line) for line in Path(args.predictions).open() if line.strip()]
    assert len(examples) == len(predictions), (len(examples), len(predictions))
    bootstrap = json.load(open(args.bootstrap_json))
    price_by_id = {int(e["id"]): float(e["now_cost"]) / 10.0 for e in bootstrap["elements"]}

    base_forecasts: list[PlayerForecast] = []
    llm_deltas: dict[int, dict] = {}
    for example, prediction in zip(examples, predictions):
        metadata = example["metadata"]
        baseline = metadata["baseline_forecast"]
        response = prediction.get("response") or prediction.get("completion") or ""
        deltas = apply_stage.parse_deltas(response) or {}
        pid = int(metadata["player_id"])
        d1 = float(deltas.get("delta_points_1gw") or 0.0)
        dP = float(deltas.get("delta_appearance_probability") or 0.0)
        if abs(d1) > 1e-9 or abs(dP) > 1e-9:
            llm_deltas[pid] = {"d1": d1, "dP": dP}
        appearance = float(baseline["baseline_appearance_probability"]) + dP
        base_forecasts.append(
            PlayerForecast(
                season=str(metadata["season"]),
                week=args.week,
                player_id=pid,
                player_name=str(metadata["player_name"]),
                team_id=int(metadata["team_id"]),
                position=str(metadata["position"]),
                price=price_by_id.get(pid, 0.0),
                predicted_minutes=max(0.0, float(baseline["baseline_minutes_1gw"]) + float(deltas.get("delta_minutes_1gw") or 0.0)),
                predicted_points_1gw=max(0.0, float(baseline["baseline_points_1gw"]) + d1),
                predicted_points_3gw=max(0.0, float(baseline["baseline_points_3gw"]) + float(deltas.get("delta_points_3gw") or 0.0)),
                predicted_points_5gw=max(0.0, float(baseline["baseline_points_5gw"]) + float(deltas.get("delta_points_5gw") or 0.0)),
                appearance_probability=min(1.0, max(0.0, appearance)),
                fixture_count=1,
                uncertainty=float(baseline.get("baseline_uncertainty") or 0.2),
            )
        )

    def pseudo_week(offset: int) -> list[PlayerForecast]:
        rows = []
        for f in base_forecasts:
            if offset == 1:
                one = max(0.0, (f.predicted_points_3gw - f.predicted_points_1gw) / 2.0)
            else:
                one = max(0.0, (f.predicted_points_5gw - f.predicted_points_3gw) / 2.0)
            rows.append(PlayerForecast(
                season=f.season, week=args.week + offset, player_id=f.player_id,
                player_name=f.player_name, team_id=f.team_id, position=f.position,
                price=f.price, predicted_minutes=f.predicted_minutes,
                predicted_points_1gw=one,
                predicted_points_3gw=f.predicted_points_3gw,
                predicted_points_5gw=f.predicted_points_5gw,
                appearance_probability=f.appearance_probability,
                fixture_count=1, uncertainty=f.uncertainty,
            ))
        return rows

    snippets: dict[int, str] = {}
    for line in open(args.corpus):
        row = json.loads(line)
        md = row["metadata"]
        docs = md.get("evidence_documents") or []
        if docs:
            snippet = adjusted_states.window_snippet(docs, str(md.get("player_name")))
            if snippet:
                snippets[int(md["player_id"])] = snippet

    entered = json.load(open(args.entered_squad))
    squad = []
    for p in entered["squad"]:
        pid = int(p["player_id"])
        buy = float(p["price"])
        now = price_by_id.get(pid, buy)
        sell = selling_price(buy, now)
        squad.append(SquadPlayer(player_id=pid, player_name=p["player_name"], team_id=int(p["team_id"]),
                                 position=p["position"], sell_price=sell, purchase_price=buy))

    def state(week: int, forecasts: list[PlayerForecast]) -> WeeklyState:
        return WeeklyState(
            season="2026-27", week=week, squad=squad, bank=args.bank,
            free_transfers=args.free_transfers, forecasts=forecasts,
            actual_points={}, actual_minutes={},
            llm_deltas=llm_deltas if week == args.week else {},
            evidence_snippets=snippets if week == args.week else {},
        )

    env = PlanEpisodeEnv([
        state(args.week, base_forecasts),
        state(args.week + 1, pseudo_week(1)),
        state(args.week + 2, pseudo_week(2)),
    ])
    prompt = env.state_prompt()
    print(f"state prompt: {len(prompt)} chars")

    generate_one = plan_eval.load_generator(args.model_path, args.adapter_path)
    response = generate_one(prompt, 8)
    plan = parse_plan(response, env.horizon)
    print("--- raw response ---")
    print(response.strip()[:600])
    print("--- parsed plan ---")
    if plan is None:
        print("UNPARSEABLE -> deterministic advisor stands")
    else:
        for i, action in enumerate(plan):
            print(f"GW{args.week + i}: horizon={action.horizon} availability={action.availability} "
                  f"knee={action.soft_knee} aggressiveness={action.transfer_aggressiveness} "
                  f"bank_transfer={action.bank_transfer} transfer_pick={action.transfer_pick} "
                  f"captain_pick={action.captain_pick} chip={action.chip_play}")
    Path(args.output).write_text(json.dumps({
        "week": args.week, "prompt": prompt, "response": response,
        "plan": None if plan is None else [dataclasses.asdict(a) for a in plan],
    }, indent=2))
    print("written ->", args.output)


if __name__ == "__main__":
    main()

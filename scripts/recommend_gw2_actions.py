#!/usr/bin/env python3
"""GW2+ weekly direction: transfers/lineup/captain/bench from the ACTUAL squad.

Unlike apply_llm_deltas_and_draft.py (initial-squad draft), this stage starts
from the squad Wes actually entered, applies the adapter deltas to the live
classic forecasts, and runs recommend_actions() for transfer options with
hit costs, then prints the full enter-this-in-the-app sheet including the
explicit bench order (GW1 lesson).
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.decision import DEFAULT_DECISION_WEIGHTS, recommend_actions  # noqa: E402
from fpl_ai.llm_adjust import apply_deltas_to_forecast  # noqa: E402
from fpl_ai.rules import selling_price  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer, SquadState  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "apply_stage", ROOT / "scripts" / "apply_llm_deltas_and_draft.py"
)
apply_stage = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(apply_stage)
parse_deltas, DELTA_KEYS = apply_stage.parse_deltas, apply_stage.DELTA_KEYS


def sell_price(buy: float, now: float) -> float:
    return selling_price(buy, now)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examples", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--bootstrap-json", required=True)
    parser.add_argument("--entered-squad", required=True, help="Previous GW's final_squad JSON (buy prices).")
    parser.add_argument("--bank", type=float, required=True)
    parser.add_argument("--free-transfers", type=int, default=1)
    parser.add_argument("--week", type=int, required=True)
    parser.add_argument("--output", help="JSON dump of the recommendation bundle.")
    args = parser.parse_args()

    examples = [json.loads(line) for line in Path(args.examples).open() if line.strip()]
    predictions = [json.loads(line) for line in Path(args.predictions).open() if line.strip()]
    assert len(examples) == len(predictions), (len(examples), len(predictions))

    bootstrap = json.load(open(args.bootstrap_json))
    price_by_id = {int(e["id"]): float(e["now_cost"]) / 10.0 for e in bootstrap["elements"]}
    team_names = {t["id"]: t["name"] for t in bootstrap["teams"]}

    forecasts = []
    deltas_by_id: dict[int, dict] = {}
    unparseable = 0
    for example, prediction in zip(examples, predictions):
        metadata = example["metadata"]
        baseline = metadata["baseline_forecast"]
        response = prediction.get("response") or prediction.get("completion") or ""
        deltas = parse_deltas(response)
        if deltas is None:
            unparseable += 1
            deltas = {}
        deltas_by_id[int(metadata["player_id"])] = deltas
        classic = PlayerForecast(
            season=str(metadata["season"]),
            week=int(metadata["week"]),
            player_id=int(metadata["player_id"]),
            player_name=str(metadata["player_name"]),
            team_id=int(metadata["team_id"]),
            position=str(metadata["position"]),
            price=price_by_id.get(int(metadata["player_id"]), 0.0),
            predicted_minutes=float(baseline["baseline_minutes_1gw"]),
            predicted_points_1gw=float(baseline["baseline_points_1gw"]),
            predicted_points_3gw=float(baseline["baseline_points_3gw"]),
            predicted_points_5gw=float(baseline["baseline_points_5gw"]),
            appearance_probability=float(baseline["baseline_appearance_probability"]),
            fixture_count=int(metadata.get("fixture_count", 1)),
            uncertainty=float(baseline.get("baseline_uncertainty") or 0.2),
        )
        forecasts.append(apply_deltas_to_forecast(classic, deltas, "all"))
    forecast_by_id = {f.player_id: f for f in forecasts}
    print(f"forecast rows: {len(forecasts)} | unparseable: {unparseable}")

    entered = json.load(open(args.entered_squad))
    squad_players = []
    for p in entered["squad"]:
        pid = int(p["player_id"])
        squad_players.append(
            SquadPlayer(
                player_id=pid,
                player_name=p["player_name"],
                team_id=int(p["team_id"]),
                position=p["position"],
                sell_price=sell_price(float(p["price"]), price_by_id.get(pid, float(p["price"]))),
                purchase_price=float(p["price"]),
            )
        )

    squad_state = SquadState(
        season="2026-27",
        week=args.week,
        squad_players=squad_players,
        bank=args.bank,
        free_transfers=args.free_transfers,
        chips_available={"wildcard": True, "free_hit": True, "bench_boost": True, "triple_captain": True},
    )
    bundle = recommend_actions(squad_state, forecasts, top_n_transfers=5, max_transfers_considered=2)

    weights = DEFAULT_DECISION_WEIGHTS

    def bench_ordered(option):
        bench_names = list(option.bench_order)
        by_name = {f.player_name: f for f in forecasts}
        gk = [n for n in bench_names if by_name[n].position == "GK"]
        out = sorted(
            (n for n in bench_names if by_name[n].position != "GK"),
            key=lambda n: -(by_name[n].predicted_points_1gw * weights.availability_weight(by_name[n])),
        )
        return gk + out

    print()
    print("=== NOTABLE LLM DELTAS ON YOUR 15 ===")
    for p in squad_players:
        d = deltas_by_id.get(p.player_id) or {}
        if any(abs(float(d.get(k) or 0.0)) > 1e-9 for k in DELTA_KEYS):
            f = forecast_by_id.get(p.player_id)
            print(
                f"  {p.player_name:16s} d1gw {float(d.get('delta_points_1gw') or 0):+.2f} "
                f"dP(app) {float(d.get('delta_appearance_probability') or 0):+.2f} "
                f"-> 1gw {f.predicted_points_1gw:.2f} P(app) {f.appearance_probability:.2f}"
            )

    for option in bundle.candidate_options:
        print()
        print(f"=== OPTION {option.option_id}: {option.label} ===")
        print(f"projected gain {option.projected_gain:+.2f} | hit {option.hit_cost} | predicted XI score {option.predicted_score:.1f}")
        print(f"captain: {option.captain_name} | vice: {option.vice_captain_name} | chip: {option.chip} ({option.chip_confidence:.2f})")
        print("XI:", ", ".join(option.starters))
        print("BENCH (enter EXACTLY this order):", " -> ".join(bench_ordered(option)))
        if option.rationale:
            print("why:", option.rationale)

    print()
    print("=== FWD MARKET UNDER YOUR BUDGET (context for the Watkins call) ===")
    watkins_sell = next((sp.sell_price for sp in squad_players if "Watkins" in sp.player_name), 0.0)
    budget = args.bank + watkins_sell
    fwds = [f for f in forecasts if f.position == "FWD" and f.price <= budget and f.player_id not in {p.player_id for p in squad_players}]
    for f in sorted(fwds, key=weights.horizon_points, reverse=True)[:12]:
        d = deltas_by_id.get(f.player_id) or {}
        print(
            f"  {f.player_name:18s} {team_names.get(f.team_id,'?'):14s} {f.price:5.1f} "
            f"1gw {f.predicted_points_1gw:.2f} 3gw {f.predicted_points_3gw:.2f} 5gw {f.predicted_points_5gw:.2f} "
            f"P(app) {f.appearance_probability:.2f} d1gw {float(d.get('delta_points_1gw') or 0):+.2f}"
        )

    if args.output:
        Path(args.output).write_text(json.dumps({
            "week": args.week,
            "bank": args.bank,
            "free_transfers": args.free_transfers,
            "options": [
                {
                    "option_id": o.option_id, "label": o.label,
                    "projected_gain": o.projected_gain, "hit_cost": o.hit_cost,
                    "predicted_score": o.predicted_score,
                    "captain": o.captain_name, "vice_captain": o.vice_captain_name,
                    "starters": list(o.starters), "bench_order": bench_ordered(o),
                    "chip": o.chip,
                }
                for o in bundle.candidate_options
            ],
        }, indent=2))
        print("written ->", args.output)


if __name__ == "__main__":
    main()

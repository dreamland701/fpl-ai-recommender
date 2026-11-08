#!/usr/bin/env python3
"""Apply frozen-adapter deltas to live classic forecasts and draft the squad.

Final stage of the weekly live runbook: read the examples + E10 responses,
parse each JSON delta completion, add the deltas onto the classic baseline
(the E9-validated "all fields" configuration), rebuild PlayerForecast
objects, and run the initial-squad beam search + lineup optimizer.
Unparseable responses fall back to zero deltas (classic-only), matching
the residual scoring convention.
"""
from __future__ import annotations

import argparse
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.backtest import build_initial_squad  # noqa: E402
from fpl_ai.decision import DEFAULT_DECISION_WEIGHTS, _optimize_lineup  # noqa: E402
from fpl_ai.llm_adjust import DELTA_CLIP_BOUNDS, apply_deltas_to_forecast, parse_delta_response  # noqa: E402
from fpl_ai.types import PlayerForecast  # noqa: E402

DELTA_KEYS = tuple(DELTA_CLIP_BOUNDS)
# Same parser (finite values only, clipped to the training bounds) as the
# backtests, so a live sheet never acts on a delta the evaluation never saw.
parse_deltas = parse_delta_response


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--examples", required=True)
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--bootstrap-json", required=True, help="Cached bootstrap-static JSON for team names.")
    parser.add_argument("--fixtures-csv", default="data/fpl_history/2026-27/fixtures.csv")
    parser.add_argument("--bench-gk-weight", type=float, default=0.15)
    parser.add_argument("--budget", type=float, default=100.0)
    parser.add_argument("--output", help="Optional JSON dump of the adjusted forecasts + squad.")
    args = parser.parse_args()

    examples = [json.loads(line) for line in Path(args.examples).open() if line.strip()]
    predictions = [json.loads(line) for line in Path(args.predictions).open() if line.strip()]
    assert len(examples) == len(predictions), (len(examples), len(predictions))

    bootstrap_early = json.load(open(args.bootstrap_json))
    price_by_id = {int(e["id"]): float(e["now_cost"]) / 10.0 for e in bootstrap_early["elements"]}

    price_missing = 0
    forecasts = []
    unparseable = 0
    adjusted_count = 0
    deltas_by_id: dict[int, dict] = {}
    for example, prediction in zip(examples, predictions):
        metadata = example["metadata"]
        baseline = metadata["baseline_forecast"]
        response = prediction.get("response") or prediction.get("completion") or ""
        deltas = parse_deltas(response)
        if deltas is None:
            unparseable += 1
            deltas = {}
        else:
            adjusted_count += any(abs(float(deltas.get(k) or 0.0)) > 1e-9 for k in DELTA_KEYS)
        deltas_by_id[int(metadata["player_id"])] = deltas

        price = price_by_id.get(int(metadata["player_id"]), 0.0)
        if price <= 0:
            price_missing += 1

        classic = PlayerForecast(
            season=str(metadata["season"]),
            week=int(metadata["week"]),
            player_id=int(metadata["player_id"]),
            player_name=str(metadata["player_name"]),
            team_id=int(metadata["team_id"]),
            position=str(metadata["position"]),
            price=price,
            predicted_minutes=float(baseline["baseline_minutes_1gw"]),
            predicted_points_1gw=float(baseline["baseline_points_1gw"]),
            predicted_points_3gw=float(baseline["baseline_points_3gw"]),
            predicted_points_5gw=float(baseline["baseline_points_5gw"]),
            appearance_probability=float(baseline["baseline_appearance_probability"]),
            fixture_count=int(metadata.get("fixture_count", 1)),
            uncertainty=float(baseline.get("baseline_uncertainty") or 0.2),
        )
        forecasts.append(apply_deltas_to_forecast(classic, deltas, "all"))

    print(f"rows: {len(forecasts)} | unparseable: {unparseable} | nonzero-delta rows: {adjusted_count} | missing price: {price_missing}")

    forecast_by_id = {f.player_id: f for f in forecasts}
    squad, bank = build_initial_squad(forecasts, budget=args.budget, bench_gk_weight=args.bench_gk_weight)
    starters, bench, captain_id, vice_id, _score = _optimize_lineup(squad, forecast_by_id, DEFAULT_DECISION_WEIGHTS)

    bootstrap = json.load(open(args.bootstrap_json))
    team_names = {t["id"]: t["name"] for t in bootstrap["teams"]}
    opponent: dict[int, tuple] = {}
    import csv as _csv

    with open(args.fixtures_csv) as handle:
        for row in _csv.DictReader(handle):
            if str(row.get("event")) == str(forecasts[0].week):
                opponent[int(row["team_h"])] = (team_names.get(int(row["team_a"]), "?"), "H")
                opponent[int(row["team_a"])] = (team_names.get(int(row["team_h"]), "?"), "A")

    def show(pid_list, label):
        print(f"--- {label} ---")
        for pid in pid_list:
            player = next(x for x in squad if x.player_id == pid)
            forecast = forecast_by_id[pid]
            cap = " (C)" if pid == captain_id else (" (VC)" if pid == vice_id else "")
            opp, venue = opponent.get(player.team_id, ("?", "?"))
            deltas = deltas_by_id.get(pid) or {}
            delta_txt = ""
            if any(abs(float(deltas.get(k) or 0.0)) > 1e-9 for k in DELTA_KEYS):
                delta_txt = f" [LLM d1gw {float(deltas.get('delta_points_1gw') or 0):+.1f}, dP(app) {float(deltas.get('delta_appearance_probability') or 0):+.2f}]"
            print(
                f"{forecast.position:4s} {player.player_name:16s} {team_names.get(player.team_id, '?'):14s} "
                f"vs {opp:14s}({venue}) price={player.sell_price:.1f} 1gw={forecast.predicted_points_1gw:.2f} "
                f"P(app)={forecast.appearance_probability:.2f}{cap}{delta_txt}"
            )

    pos_order = {"GK": 0, "DEF": 1, "MID": 2, "FWD": 3}
    show(sorted(starters, key=lambda pid: pos_order[forecast_by_id[pid].position]), "STARTING XI (classic + E10)")
    # BENCH ORDER MATTERS: autosubs take the first legally-substitutable
    # bench player in listed order (GW1 2026-27 lesson: Mitchell at bench-2
    # absorbed the sub ahead of Bijol's 10-pointer because the sheet never
    # specified an order). GK has its own slot; outfield bench is ranked by
    # expected fielded points (1gw x availability weight) so the best
    # candidate always sits first.
    weights = DEFAULT_DECISION_WEIGHTS
    bench_gk = [pid for pid in bench if forecast_by_id[pid].position == "GK"]
    bench_out = sorted(
        (pid for pid in bench if forecast_by_id[pid].position != "GK"),
        key=lambda pid: -(forecast_by_id[pid].predicted_points_1gw * weights.availability_weight(forecast_by_id[pid])),
    )
    ordered_bench = bench_gk + bench_out
    print("--- BENCH (enter EXACTLY this order in the app) ---")
    for slot, pid in enumerate(ordered_bench):
        player = next(x for x in squad if x.player_id == pid)
        forecast = forecast_by_id[pid]
        label = "GK " if forecast.position == "GK" else f"{slot}. "
        print(f"{label} {forecast.position:4s} {player.player_name:16s} 1gw={forecast.predicted_points_1gw:.2f} P(app)={forecast.appearance_probability:.2f}")
    xi_total = sum(forecast_by_id[pid].predicted_points_1gw for pid in starters)
    print()
    print("total cost:", round(sum(p.sell_price for p in squad), 1), "| bank:", round(bank, 1))
    print("XI predicted 1gw total (incl captain x2):", round(xi_total + forecast_by_id[captain_id].predicted_points_1gw, 1))

    if args.output:
        Path(args.output).write_text(json.dumps({
            "squad": [
                {"player_id": p.player_id, "player_name": p.player_name, "team_id": p.team_id,
                 "position": p.position, "price": p.sell_price,
                 "role": "XI" if p.player_id in starters else "bench",
                 "bench_order": (ordered_bench.index(p.player_id) if p.player_id in ordered_bench else None),
                 "captain": p.player_id == captain_id,
                 "vice_captain": p.player_id == vice_id}
                for p in squad
            ],
            "bank": bank,
            "unparseable": unparseable,
        }, indent=2))
        print("written ->", args.output)


if __name__ == "__main__":
    main()

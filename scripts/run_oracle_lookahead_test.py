#!/usr/bin/env python3
"""Oracle lookahead test: upper-bound the option value of banking transfers.

DIAGNOSTIC ONLY — the oracle projection deliberately leaks realized outcomes
into the lookahead's *next-week* estimate (this week's decisions still use
classic forecasts). Interpretation:

- If oracle lookahead >> greedy, the banking/lookahead mechanism is sound and
  the earlier 3-window rejection was a forecast-quality problem → investing
  in better next-week forecasts (or LLM judgment) can unlock real points.
- If oracle lookahead ~= greedy even with perfect next-week knowledge,
  FT banking has ~zero option value at 1 transfer/week and the lookahead
  direction is closed for good.

Runs greedy (lookahead=1) and oracle lookahead (lookahead=2) on the three
standard windows and prints the paired table.

Usage:
  python3 scripts/run_oracle_lookahead_test.py \
    [--training-data data/fpl_training_rows.csv] \
    [--output reports/oracle_lookahead_test.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.backtest import run_rolling_squad_backtest  # noqa: E402
from fpl_ai.service import FPLRecommender  # noqa: E402

WINDOWS = ["2025-26", "2024-25", "2023-24"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output", default="reports/oracle_lookahead_test.json")
    parser.add_argument("--start-week", type=int, default=12)
    parser.add_argument("--end-week", type=int, default=30)
    args = parser.parse_args()

    recommender = FPLRecommender.from_training_csv(args.training_data)
    results: dict[str, dict[str, float]] = {}
    for season in WINDOWS:
        results[season] = {}
        for label, lookahead, projection, oracle_now in (
            # Hybrid (v1): classic current forecasts, oracle next-week value.
            # Measures banking on info the future executor won't have.
            ("greedy", 1, "schedule", False),
            ("oracle_lookahead", 2, "oracle", False),
            # Full oracle (v2, the "actual space" test): both runs act on
            # realized outcomes; the ONLY difference is banking structure.
            ("oracle_greedy", 1, "schedule", True),
            ("oracle_greedy_lookahead", 2, "oracle", True),
        ):
            report = run_rolling_squad_backtest(
                recommender.dataset,
                test_season=season,
                initial_train_week_max=args.start_week - 1,
                start_week=args.start_week,
                end_week=args.end_week,
                transfer_lookahead=lookahead,
                lookahead_projection=projection,
                oracle_forecasts=oracle_now,
            )
            results[season][label] = float(report.total_actual_points)
            banked = sum(
                1
                for week in report.weeks
                if any("bank the free transfer" in note for note in week.notes)
            )
            results[season][f"{label}_banked_weeks"] = banked
            print(f"{season} {label}: {report.total_actual_points} (banked {banked} wks)", flush=True)

    for title, a_key, b_key in (
        ("Hybrid: classic now, oracle next-week value", "greedy", "oracle_lookahead"),
        ("Full oracle (actual space): pure banking option value", "oracle_greedy", "oracle_greedy_lookahead"),
    ):
        print(f"\n=== {title} (GW12-30) ===")
        print(f"{'window':<10} {'run A':>8} {'run B':>8} {'delta':>7}")
        deltas = []
        for season in WINDOWS:
            run_a = results[season][a_key]
            run_b = results[season][b_key]
            deltas.append(run_b - run_a)
            print(f"{season:<10} {run_a:>8.0f} {run_b:>8.0f} {run_b - run_a:>+7.0f}")
        print(f"{'mean':<10} {'':>8} {'':>8} {sum(deltas) / len(deltas):>+7.1f}")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(results, indent=2))
    print(f"\nwritten -> {output_path}")


if __name__ == "__main__":
    main()

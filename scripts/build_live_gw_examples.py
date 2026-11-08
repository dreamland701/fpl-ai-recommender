#!/usr/bin/env python3
"""Build live-inference examples for the frozen E10 adapter for one GW.

The weekly runbook's core glue (first built for GW1 2026-27): produce the
same prompt schema the adapter was trained on, but from LIVE data —
classic forecasts from the walk-forward ridge on all history, player
context (status/news/price/team) from the official API, and fresh
pre-deadline evidence attached per player by the existing attach script.

Two modes, run in sequence with the attach scripts between them:

  --stage corpus   -> bare corpus JSONL (metadata + baseline forecast per
                      player) + data/fpl_history/<season>/fixtures.csv +
                      teams.csv so attach_fixture_outlook_to_corpus.py can
                      resolve the live season's schedule.
  --stage prompts  -> read the evidence+fixture-attached corpus and emit
                      eval-ready rows ({"prompt", "metadata"}) using the
                      split builder's own prompt functions (imported, not
                      copied) so the schema matches training exactly.

Known, accepted schema gaps vs training prompts (documented, not silent):
role-context and baseline-decomposition blocks are omitted (their attach
scripts need in-training-table rows, which a live future GW doesn't have);
congestion is omitted but genuinely empty for GW1 anyway (no European
fixtures in August).
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import os
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import pandas as pd  # noqa: E402

from fpl_ai.dataset import CanonicalDataset, training_rows_asof  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402
from fpl_ai.api import OfficialSnapshotService  # noqa: E402

_spec = importlib.util.spec_from_file_location(
    "split_v2", ROOT / "scripts" / "build_residual_player_forecast_split_v2.py"
)
split_v2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(split_v2)


def stage_corpus(args) -> None:
    dataset = CanonicalDataset.from_csv(args.training_data)
    snap = OfficialSnapshotService()
    official_frame = snap.build_current_week_frame(args.deadline_ts)
    live_frame = dataset.build_live_week_frame(official_frame, history_root=args.history_root)
    # Fit exactly as a backtest would at this deadline: multi-week labels that
    # had not settled before the live week are masked, not read as partial sums.
    live_season = str(live_frame["season"].mode().iloc[0])
    live_week = int(pd.to_numeric(live_frame["week"], errors="coerce").mode().iloc[0])
    train_frame = training_rows_asof(dataset.training_frame, live_season, live_week)
    model_suite = fit_model_suite_from_frame(train_frame=train_frame, feature_names=dataset.feature_columns)
    forecasts = model_suite.predict_frame(live_frame)

    status_by_id = dict(zip(official_frame["player_id"], official_frame["status"].fillna("a")))
    market_by_id = {
        int(pid): {"price": round(float(price or 0.0), 1), "selected_by_percent": round(float(sel or 0.0), 1)}
        for pid, price, sel in zip(
            official_frame["player_id"],
            official_frame.get("price", official_frame.get("now_cost", 0.0)),
            official_frame.get("selected_by_percent", 0.0),
        )
    }
    news_by_id = dict(zip(official_frame["player_id"], official_frame["news"].fillna("")))
    defcon_by_id = {
        int(r["player_id"]): {
            "avg_3": round(float(r.get("defensive_contribution_avg_3") or 0.0), 1),
            "avg_5": round(float(r.get("defensive_contribution_avg_5") or 0.0), 1),
            "tracked": bool(r.get("defensive_data_source_available")),
        }
        for r in live_frame.to_dict("records")
    }

    season = str(forecasts[0].season)

    # Fixtures + teams for the live season so the fixture-outlook attach
    # script can build the next-5-GW schedule block (full-season fixtures
    # are published at launch, so this is timestamp-safe).
    client = snap.client
    season_dir = Path(args.history_root) / season
    season_dir.mkdir(parents=True, exist_ok=True)
    bootstrap = client.bootstrap_static()
    with (season_dir / "teams.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "name", "short_name"])
        writer.writeheader()
        for team in bootstrap.get("teams", []):
            writer.writerow({"id": team["id"], "name": team["name"], "short_name": team["short_name"]})
    # Same full-field write as `sync-history` (ingest._backfill_current_fixtures):
    # the table builder reads scores from this file, so a schedule-only rewrite
    # would silently break the next rebuild.
    pd.DataFrame(list(client.fixtures())).to_csv(season_dir / "fixtures.csv", index=False)

    count = 0
    with Path(args.output).open("w") as handle:
        for forecast in forecasts:
            metadata = {
                "season": forecast.season,
                "week": forecast.week,
                "deadline_ts": args.deadline_ts,
                "player_id": forecast.player_id,
                "player_name": forecast.player_name,
                "team_id": forecast.team_id,
                "position": forecast.position,
                "fixture_count": int(forecast.fixture_count),
                "status_pre_deadline": str(status_by_id.get(forecast.player_id, "a")),
                "news_pre_deadline": str(news_by_id.get(forecast.player_id, "")),
                "baseline_forecast": {
                    "baseline_points_1gw": round(forecast.predicted_points_1gw, 4),
                    "baseline_points_3gw": round(forecast.predicted_points_3gw, 4),
                    "baseline_points_5gw": round(forecast.predicted_points_5gw, 4),
                    "baseline_minutes_1gw": round(forecast.predicted_minutes, 4),
                    "baseline_appearance_probability": round(forecast.appearance_probability, 4),
                    "baseline_uncertainty": round(forecast.uncertainty, 4),
                },
                "labels": {},  # live: outcomes unknown
                "defcon": defcon_by_id.get(forecast.player_id, {"avg_3": 0.0, "avg_5": 0.0, "tracked": False}),
                "market": market_by_id.get(forecast.player_id),
            }
            handle.write(json.dumps({
                "season": forecast.season,
                "week": forecast.week,
                "deadline_ts": args.deadline_ts,
                "metadata": metadata,
            }, ensure_ascii=False) + "\n")
            count += 1
    print(f"stage corpus: {count} players -> {args.output}; fixtures/teams -> {season_dir}")


def stage_prompts(args) -> None:
    clip_text = ", ".join(
        f"{key} in [-{spec[2]:g}, {spec[2]:g}]" for key, spec in split_v2.DELTA_SPECS.items()
    )
    system = (
        "You are an FPL player forecaster. You combine a classic ML statistical signal with pre-deadline text "
        "evidence and output bounded forecast deltas as strict JSON. No hidden reasoning, no extra text."
    )
    count = evidence_present = 0
    with Path(args.corpus).open() as source, Path(args.output).open("w") as sink:
        for line in source:
            row = json.loads(line)
            metadata = dict(row["metadata"])
            documents = split_v2._clean_evidence_documents(metadata)
            user = split_v2._build_user_prompt(
                metadata,
                documents,
                max_docs=2,
                max_chars=260,
                clip_text=clip_text,
                no_evidence=False,
                include_fixtures=True,
                include_congestion=True,
                include_provenance=True,
                include_decomposition=True,
                include_role=True,
                compact_context=True,
                include_defcon=True,
                # E13a parity switch: the Market line exists only in E13a+
                # training prompts. Decode with E13a -> leave on (default);
                # fall back to E11-full -> set FPL_LIVE_INCLUDE_MARKET=0 or
                # the adapter sees a line it never trained on.
                include_market=os.environ.get("FPL_LIVE_INCLUDE_MARKET", "1") == "1",
                prefer_scout=True,
                preferred_chars=800,
            )
            prompt = f"<|turn>system\n{system}<|turn>\n<|turn>user\n{user}<|turn>\n<|turn>model\n"
            out_metadata = {
                "season": metadata.get("season"),
                "week": metadata.get("week"),
                "player_id": metadata.get("player_id"),
                "player_name": metadata.get("player_name"),
                "team_id": metadata.get("team_id"),
                "position": metadata.get("position"),
                "baseline_forecast": metadata["baseline_forecast"],
                "evidence_present": bool(documents),
            }
            evidence_present += bool(documents)
            sink.write(json.dumps({
                "season": row["season"],
                "week": row["week"],
                "deadline_ts": row["deadline_ts"],
                "prompt": prompt,
                "metadata": out_metadata,
            }, ensure_ascii=False) + "\n")
            count += 1
    print(f"stage prompts: {count} rows ({evidence_present} with evidence) -> {args.output}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stage", choices=["corpus", "prompts"], required=True)
    parser.add_argument("--deadline-ts", default="2026-08-21T17:30:00Z")
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--history-root", default="data/fpl_history")
    parser.add_argument("--corpus", help="prompts stage: the evidence-attached corpus JSONL")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.stage == "corpus":
        stage_corpus(args)
    else:
        stage_prompts(args)


if __name__ == "__main__":
    main()

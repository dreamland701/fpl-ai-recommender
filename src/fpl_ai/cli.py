"""Command-line entrypoint for the FPL recommender."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import List

import pandas as pd

from .api import OfficialFPLClient
from .backtest import run_rolling_squad_backtest, write_backtest_outputs
from .decision import DECISION_VARIANTS
from .evidence_collect import available_fetchable_source_keys, collect_and_write_evidence
from .evidence import evidence_snapshot_to_dict
from .evaluation import evaluate_time_split, write_evaluation_outputs
from .ingest import DEFAULT_COMPLETED_SEASONS
from .llm_data import (
    build_multiseason_decision_sft_examples,
    build_multiseason_player_forecast_examples,
    build_multiseason_transfer_choice_examples,
    build_decision_sft_examples,
    normalize_evidence_corpus,
    split_llm_examples_by_time,
    write_llm_training_examples,
    write_llm_training_split,
    write_normalized_evidence,
)
from .llm_adjust import load_llm_delta_lookup
from .llm_eval import evaluate_llm_predictions, write_llm_evaluation_outputs
from .llm_transfer_eval import (
    evaluate_llm_transfer_choices,
    write_llm_transfer_evaluation_outputs,
)
from .service import FPLRecommender
from .types import SourceDocument, SquadPlayer, SquadState
from .weekly_evidence import backfill_weekly_google_news_evidence, enrich_evidence_fulltext, enrich_premierleague_fulltext


def _load_squad_state(path: str) -> SquadState:
    payload = json.loads(Path(path).read_text())
    squad_players = [SquadPlayer(**player) for player in payload["squad_players"]]
    return SquadState(
        season=payload["season"],
        week=int(payload["week"]),
        squad_players=squad_players,
        bank=float(payload["bank"]),
        free_transfers=int(payload["free_transfers"]),
        chips_available=payload.get("chips_available", {}),
    )


def _load_sources(path: str) -> List[SourceDocument]:
    payload = json.loads(Path(path).read_text())
    return [SourceDocument(**document) for document in payload]


def _print_json(payload) -> None:
    print(json.dumps(payload, indent=2))


def _parse_seasons(value: str) -> List[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def _write_table(records, output: str | None) -> None:
    if output:
        path = Path(output)
        path.parent.mkdir(parents=True, exist_ok=True)
        pd.DataFrame(records).to_csv(path, index=False)
        print(f"Wrote forecasts to {path}")
        return
    _print_json(records)


def main() -> None:
    parser = argparse.ArgumentParser(description="FPL AI Recommender CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    build_parser = subparsers.add_parser("build-training-table", help="Normalize historical data into training rows.")
    build_parser.add_argument("--history-root", required=True)
    build_parser.add_argument("--output", required=True)

    sync_parser = subparsers.add_parser("sync-history", help="Download completed seasons and backfill the current season.")
    sync_parser.add_argument("--history-root", required=True)
    sync_parser.add_argument("--completed-seasons", default=",".join(DEFAULT_COMPLETED_SEASONS))
    sync_parser.add_argument("--current-season", default="2025-26")
    sync_parser.add_argument("--current-max-gw", type=int, default=30)

    bootstrap_parser = subparsers.add_parser(
        "bootstrap-training-data",
        help="Fetch raw history and immediately build the training table.",
    )
    bootstrap_parser.add_argument("--history-root", required=True)
    bootstrap_parser.add_argument("--output", required=True)
    bootstrap_parser.add_argument("--completed-seasons", default=",".join(DEFAULT_COMPLETED_SEASONS))
    bootstrap_parser.add_argument("--current-season", default="2025-26")
    bootstrap_parser.add_argument("--current-max-gw", type=int, default=30)

    train_parser = subparsers.add_parser("train-models", help="Train the baseline ridge-regression models.")
    train_parser.add_argument("--training-data", required=True)
    train_parser.add_argument("--model-dir", required=True)
    train_parser.add_argument("--alpha", type=float, default=1.0)

    evaluate_parser = subparsers.add_parser("evaluate-models", help="Run a time-based honest backtest.")
    evaluate_parser.add_argument("--training-data", required=True)
    evaluate_parser.add_argument("--test-season", default="2025-26")
    evaluate_parser.add_argument("--test-week-min", type=int, default=1)
    evaluate_parser.add_argument("--test-week-max", type=int, default=30)
    evaluate_parser.add_argument("--output-dir", required=True)
    evaluate_parser.add_argument("--alpha", type=float, default=1.0)

    backtest_parser = subparsers.add_parser(
        "backtest-squad",
        help="Run a rolling squad-level backtest with a synthetic starting squad.",
    )
    backtest_parser.add_argument("--training-data", required=True)
    backtest_parser.add_argument("--test-season", default="2025-26")
    backtest_parser.add_argument("--initial-train-week-max", type=int, default=10)
    backtest_parser.add_argument("--start-week", type=int, default=11)
    backtest_parser.add_argument("--end-week", type=int, default=30)
    backtest_parser.add_argument("--output-dir", required=True)
    backtest_parser.add_argument("--alpha", type=float, default=1.0)
    backtest_parser.add_argument("--initial-budget", type=float, default=100.0)
    backtest_parser.add_argument("--max-free-transfers", type=int, default=2)
    backtest_parser.add_argument("--max-transfers-per-week", type=int, default=1)
    backtest_parser.add_argument("--min-projected-gain", type=float, default=0.0)
    backtest_parser.add_argument("--skip-league-average-fetch", action="store_true")
    backtest_parser.add_argument("--llm-examples", help="Residual eval examples JSONL; enables LLM-adjusted forecasts.")
    backtest_parser.add_argument("--llm-predictions", help="Model predictions JSONL aligned row-wise with --llm-examples.")
    backtest_parser.add_argument("--llm-fields", choices=["all", "points", "availability", "availability_scaled"], default="all", help="Which forecast fields the LLM deltas adjust.")
    backtest_parser.add_argument(
        "--decision-variant",
        choices=sorted(DECISION_VARIANTS),
        default="baseline",
        help="Decision-layer scoring preset (transfer horizon / availability handling).",
    )
    backtest_parser.add_argument(
        "--transfer-lookahead",
        type=int,
        choices=[1, 2],
        default=1,
        help="1 = greedy weekly transfers; 2 = plan this week's move against next week's best follow-up (FT banking visible).",
    )
    backtest_parser.add_argument("--lookahead-discount", type=float, default=0.9)
    backtest_parser.add_argument(
        "--lookahead-projection",
        choices=["schedule", "horizon_diff", "oracle"],
        default="schedule",
        help="Next-week estimate: rescale 1GW by future schedule, use the model's own (3GW-1GW)/2, or 'oracle' (realized outcomes — DIAGNOSTIC ONLY, leaks labels).",
    )
    backtest_parser.add_argument("--simulate-wildcard", action="store_true", help="Allow one mid-window Wildcard (full squad rebuild) when the projected gain clears --wildcard-min-gain.")
    backtest_parser.add_argument("--simulate-free-hit", action="store_true", help="Allow one Free Hit (one-week rebuild, squad reverts) when the one-week gain clears --free-hit-min-gain.")
    backtest_parser.add_argument("--wildcard-min-gain", type=float, default=12.0)
    backtest_parser.add_argument("--free-hit-min-gain", type=float, default=10.0)

    normalize_evidence_parser = subparsers.add_parser(
        "normalize-evidence",
        help="Normalize a local evidence export into timestamp-safe JSONL.",
    )
    normalize_evidence_parser.add_argument("--input", required=True)
    normalize_evidence_parser.add_argument("--output", required=True)
    normalize_evidence_parser.add_argument("--include-non-curated", action="store_true")

    evidence_snapshot_parser = subparsers.add_parser(
        "build-evidence-snapshot",
        help="Build a deadline-scoped typed evidence snapshot from normalized evidence inputs.",
    )
    evidence_snapshot_parser.add_argument("--deadline-ts", required=True)
    evidence_snapshot_parser.add_argument("--input", required=True)
    evidence_snapshot_parser.add_argument("--output")
    evidence_snapshot_parser.add_argument("--include-non-curated", action="store_true")
    evidence_snapshot_parser.add_argument("--max-docs", type=int, default=6)
    evidence_snapshot_parser.add_argument("--lookback-days", type=int, default=14)

    collect_evidence_parser = subparsers.add_parser(
        "collect-evidence",
        help="Fetch a normalized curated evidence corpus from supported feeds plus optional local imports.",
    )
    collect_evidence_parser.add_argument("--output", required=True)
    collect_evidence_parser.add_argument("--input", action="append", default=[])
    collect_evidence_parser.add_argument("--source", action="append", choices=available_fetchable_source_keys())
    collect_evidence_parser.add_argument("--include-non-curated", action="store_true")
    collect_evidence_parser.add_argument("--lookback-days", type=int, default=7)
    collect_evidence_parser.add_argument("--max-items-per-source", type=int, default=50)

    weekly_evidence_parser = subparsers.add_parser(
        "backfill-weekly-evidence",
        help="Backfill timestamp-safe weekly evidence packets from historical Google News RSS results.",
    )
    weekly_evidence_parser.add_argument("--training-data", required=True)
    weekly_evidence_parser.add_argument("--season", default="2025-26")
    weekly_evidence_parser.add_argument("--start-week", type=int, default=1)
    weekly_evidence_parser.add_argument("--end-week", type=int, default=30)
    weekly_evidence_parser.add_argument("--documents-output", required=True)
    weekly_evidence_parser.add_argument("--packets-output", required=True)
    weekly_evidence_parser.add_argument("--report-output", required=True)
    weekly_evidence_parser.add_argument("--lookback-days", type=int, default=14)
    weekly_evidence_parser.add_argument("--max-items-per-query", type=int, default=40)
    weekly_evidence_parser.add_argument("--max-documents-per-week", type=int, default=80)
    weekly_evidence_parser.add_argument("--sleep-seconds", type=float, default=0.25)

    enrich_pl_parser = subparsers.add_parser(
        "enrich-premierleague-fulltext",
        help="Resolve official Premier League/FPL Scout evidence rows and extract article body text.",
    )
    enrich_pl_parser.add_argument("--input", required=True)
    enrich_pl_parser.add_argument("--output", required=True)
    enrich_pl_parser.add_argument("--report-output", required=True)
    enrich_pl_parser.add_argument("--max-rows", type=int)
    enrich_pl_parser.add_argument("--sleep-seconds", type=float, default=0.25)

    enrich_fulltext_parser = subparsers.add_parser(
        "enrich-evidence-fulltext",
        help="Resolve evidence rows to publisher URLs and extract article body text where possible.",
    )
    enrich_fulltext_parser.add_argument("--input", required=True)
    enrich_fulltext_parser.add_argument("--output", required=True)
    enrich_fulltext_parser.add_argument("--report-output", required=True)
    enrich_fulltext_parser.add_argument("--max-rows", type=int)
    enrich_fulltext_parser.add_argument("--sleep-seconds", type=float, default=0.25)
    enrich_fulltext_parser.add_argument("--source-name-regex")
    enrich_fulltext_parser.add_argument("--category-regex")
    enrich_fulltext_parser.add_argument("--request-timeout", type=float, default=10.0)
    enrich_fulltext_parser.add_argument("--output-every", type=int, default=25)

    llm_export_parser = subparsers.add_parser(
        "export-llm-sft",
        help="Export week-by-week LLM decision fine-tuning examples from a backtest report.",
    )
    llm_export_parser.add_argument("--training-data", required=True)
    llm_export_parser.add_argument("--backtest-report", required=True)
    llm_export_parser.add_argument("--output", required=True)
    llm_export_parser.add_argument("--evidence")
    llm_export_parser.add_argument("--include-non-curated-evidence", action="store_true")
    llm_export_parser.add_argument("--max-docs-per-week", type=int, default=6)
    llm_export_parser.add_argument("--lookback-days", type=int, default=14)

    llm_corpus_parser = subparsers.add_parser(
        "export-llm-sft-corpus",
        help="Build a multi-season week-by-week LLM decision corpus from rolling backtests.",
    )
    llm_corpus_parser.add_argument("--training-data", required=True)
    llm_corpus_parser.add_argument("--output", required=True)
    llm_corpus_parser.add_argument("--seasons")
    llm_corpus_parser.add_argument("--initial-train-week-max", type=int, default=10)
    llm_corpus_parser.add_argument("--start-week", type=int)
    llm_corpus_parser.add_argument("--end-week", type=int)
    llm_corpus_parser.add_argument("--alpha", type=float, default=1.0)
    llm_corpus_parser.add_argument("--initial-budget", type=float, default=100.0)
    llm_corpus_parser.add_argument("--max-free-transfers", type=int, default=2)
    llm_corpus_parser.add_argument("--max-transfers-per-week", type=int, default=1)
    llm_corpus_parser.add_argument("--min-projected-gain", type=float, default=0.0)
    llm_corpus_parser.add_argument("--evidence")
    llm_corpus_parser.add_argument("--include-non-curated-evidence", action="store_true")
    llm_corpus_parser.add_argument("--max-docs-per-week", type=int, default=6)
    llm_corpus_parser.add_argument("--lookback-days", type=int, default=14)

    llm_split_parser = subparsers.add_parser(
        "split-llm-sft",
        help="Split an LLM JSONL corpus into time-based train/eval sets.",
    )
    llm_split_parser.add_argument("--input", required=True)
    llm_split_parser.add_argument("--output-dir", required=True)
    llm_split_parser.add_argument("--eval-season", required=True)
    llm_split_parser.add_argument("--eval-week-min", type=int, required=True)
    llm_split_parser.add_argument("--eval-week-max", type=int)

    llm_transfer_choice_parser = subparsers.add_parser(
        "export-llm-transfer-choice-corpus",
        help="Export a multiseason outcome-labeled transfer-choice corpus for LLM training.",
    )
    llm_transfer_choice_parser.add_argument("--training-data", required=True)
    llm_transfer_choice_parser.add_argument("--output", required=True)
    llm_transfer_choice_parser.add_argument("--seasons")
    llm_transfer_choice_parser.add_argument("--initial-train-week-max", type=int, default=10)
    llm_transfer_choice_parser.add_argument("--start-week", type=int)
    llm_transfer_choice_parser.add_argument("--end-week", type=int)
    llm_transfer_choice_parser.add_argument("--alpha", type=float, default=1.0)
    llm_transfer_choice_parser.add_argument("--initial-budget", type=float, default=100.0)
    llm_transfer_choice_parser.add_argument("--max-free-transfers", type=int, default=2)
    llm_transfer_choice_parser.add_argument("--max-transfers-per-week", type=int, default=1)
    llm_transfer_choice_parser.add_argument("--min-projected-gain", type=float, default=0.0)
    llm_transfer_choice_parser.add_argument("--evidence")
    llm_transfer_choice_parser.add_argument("--include-non-curated-evidence", action="store_true")
    llm_transfer_choice_parser.add_argument("--max-docs-per-week", type=int, default=6)
    llm_transfer_choice_parser.add_argument("--lookback-days", type=int, default=14)

    llm_player_forecast_parser = subparsers.add_parser(
        "export-llm-player-forecast-corpus",
        help="Export a multiseason player-level forecasting corpus for LLM training.",
    )
    llm_player_forecast_parser.add_argument("--training-data", required=True)
    llm_player_forecast_parser.add_argument("--output", required=True)
    llm_player_forecast_parser.add_argument("--seasons")
    llm_player_forecast_parser.add_argument("--start-week", type=int)
    llm_player_forecast_parser.add_argument("--end-week", type=int)
    llm_player_forecast_parser.add_argument("--evidence")
    llm_player_forecast_parser.add_argument("--include-non-curated-evidence", action="store_true")
    llm_player_forecast_parser.add_argument("--max-docs-per-week", type=int, default=3)
    llm_player_forecast_parser.add_argument("--lookback-days", type=int, default=7)
    llm_player_forecast_parser.add_argument(
        "--prompt-style",
        choices=["features", "baseline_adjustment"],
        default="features",
        help="features keeps the original engineered-feature prompt; baseline_adjustment uses ML forecast plus evidence text.",
    )
    llm_player_forecast_parser.add_argument("--max-evidence-chars-per-document", type=int, default=6000)

    llm_eval_parser = subparsers.add_parser(
        "evaluate-llm-predictions",
        help="Evaluate week-by-week LLM JSON predictions against the exported eval examples.",
    )
    llm_eval_parser.add_argument("--examples", required=True)
    llm_eval_parser.add_argument("--predictions", required=True)
    llm_eval_parser.add_argument("--output-dir", required=True)

    llm_transfer_eval_parser = subparsers.add_parser(
        "evaluate-llm-transfer-choices",
        help="Evaluate selected-option predictions against outcome-labeled transfer-choice examples.",
    )
    llm_transfer_eval_parser.add_argument("--examples", required=True)
    llm_transfer_eval_parser.add_argument("--predictions", required=True)
    llm_transfer_eval_parser.add_argument("--output-dir", required=True)

    forecast_parser = subparsers.add_parser("predict-week", help="Predict per-player outcomes for a historical week.")
    forecast_parser.add_argument("--training-data", required=True)
    forecast_parser.add_argument("--model-dir", required=True)
    forecast_parser.add_argument("--season", required=True)
    forecast_parser.add_argument("--week", required=True, type=int)
    forecast_parser.add_argument("--top-n", type=int, default=25)
    forecast_parser.add_argument("--output")

    recommend_parser = subparsers.add_parser("recommend", help="Recommend transfers and lineup decisions.")
    recommend_parser.add_argument("--training-data", required=True)
    recommend_parser.add_argument("--model-dir", required=True)
    recommend_parser.add_argument("--season", required=True)
    recommend_parser.add_argument("--week", required=True, type=int)
    recommend_parser.add_argument("--squad", required=True)
    recommend_parser.add_argument("--sources")

    hybrid_parser = subparsers.add_parser(
        "build-hybrid-decision-context",
        help="Build the ML + evidence + legal-candidate prompt/context for Gemma ranking.",
    )
    hybrid_parser.add_argument("--training-data", required=True)
    hybrid_parser.add_argument("--model-dir", required=True)
    hybrid_parser.add_argument("--deadline-ts", required=True)
    hybrid_parser.add_argument("--squad", required=True)
    hybrid_parser.add_argument("--evidence")
    hybrid_parser.add_argument("--include-non-curated", action="store_true")
    hybrid_parser.add_argument("--max-docs", type=int, default=6)
    hybrid_parser.add_argument("--lookback-days", type=int, default=14)
    hybrid_parser.add_argument("--top-n-transfers", type=int, default=5)
    hybrid_parser.add_argument("--max-transfers-considered", type=int, default=2)
    hybrid_parser.add_argument("--output")

    args = parser.parse_args()

    if args.command == "build-training-table":
        recommender = FPLRecommender.from_history_root(args.history_root)
        recommender.save_training_rows(args.output)
        print(f"Wrote training rows to {args.output}")
        return

    if args.command == "sync-history":
        recommender = FPLRecommender()
        summary = recommender.sync_history(
            history_root=args.history_root,
            completed_seasons=_parse_seasons(args.completed_seasons),
            current_season=args.current_season,
            current_max_gw=args.current_max_gw,
        )
        _print_json(asdict(summary))
        return

    if args.command == "bootstrap-training-data":
        recommender = FPLRecommender()
        summary = recommender.bootstrap_training_data(
            history_root=args.history_root,
            training_output=args.output,
            completed_seasons=_parse_seasons(args.completed_seasons),
            current_season=args.current_season,
            current_max_gw=args.current_max_gw,
        )
        _print_json(
            {
                "sync_summary": asdict(summary),
                "training_output": args.output,
            }
        )
        return

    if args.command == "train-models":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        manifest = recommender.train_models(args.model_dir, alpha=args.alpha)
        _print_json(asdict(manifest))
        return

    if args.command == "evaluate-models":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        report = evaluate_time_split(
            recommender.dataset,
            test_season=args.test_season,
            test_week_min=args.test_week_min,
            test_week_max=args.test_week_max,
            alpha=args.alpha,
        )
        paths = write_evaluation_outputs(report, args.output_dir)
        _print_json({"report": asdict(report), "paths": paths})
        return

    if args.command == "backtest-squad":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        llm_delta_lookup = None
        if bool(args.llm_examples) != bool(args.llm_predictions):
            raise SystemExit("--llm-examples and --llm-predictions must be provided together.")
        if args.llm_examples:
            llm_delta_lookup = load_llm_delta_lookup(args.llm_examples, args.llm_predictions)
        league_average_by_week = None
        if not args.skip_league_average_fetch:
            try:
                league_average_by_week = OfficialFPLClient().average_entry_scores()
            except Exception:
                league_average_by_week = None
        report = run_rolling_squad_backtest(
            recommender.dataset,
            test_season=args.test_season,
            initial_train_week_max=args.initial_train_week_max,
            start_week=args.start_week,
            end_week=args.end_week,
            alpha=args.alpha,
            initial_budget=args.initial_budget,
            max_free_transfers=args.max_free_transfers,
            max_transfers_per_week=args.max_transfers_per_week,
            min_projected_gain=args.min_projected_gain,
            league_average_by_week=league_average_by_week,
            llm_delta_lookup=llm_delta_lookup,
            llm_fields=args.llm_fields,
            decision_weights=DECISION_VARIANTS[args.decision_variant],
            transfer_lookahead=args.transfer_lookahead,
            lookahead_discount=args.lookahead_discount,
            lookahead_projection=args.lookahead_projection,
            simulate_wildcard=args.simulate_wildcard,
            simulate_free_hit=args.simulate_free_hit,
            wildcard_min_gain=args.wildcard_min_gain,
            free_hit_min_gain=args.free_hit_min_gain,
        )
        paths = write_backtest_outputs(report, args.output_dir)
        _print_json({"report": asdict(report), "paths": paths})
        return

    if args.command == "normalize-evidence":
        evidence_frame = normalize_evidence_corpus(
            args.input,
            curated_only=not args.include_non_curated,
        )
        write_normalized_evidence(evidence_frame, args.output)
        _print_json({"rows": int(len(evidence_frame)), "output": args.output})
        return

    if args.command == "build-evidence-snapshot":
        recommender = FPLRecommender()
        snapshot = recommender.build_evidence_snapshot(
            deadline_ts=args.deadline_ts,
            evidence_path=args.input,
            curated_only=not args.include_non_curated,
            max_documents=args.max_docs,
            lookback_days=args.lookback_days,
        )
        payload = evidence_snapshot_to_dict(snapshot)
        if args.output:
            path = Path(args.output)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=2))
            _print_json({"output": args.output, "document_count": snapshot.document_count})
            return
        _print_json(payload)
        return

    if args.command == "collect-evidence":
        frame = collect_and_write_evidence(
            output_path=args.output,
            local_inputs=args.input,
            source_keys=args.source or None,
            curated_only=not args.include_non_curated,
            lookback_days=args.lookback_days,
            max_items_per_source=args.max_items_per_source,
        )
        _print_json({"rows": int(len(frame)), "output": args.output})
        return

    if args.command == "backfill-weekly-evidence":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        report = backfill_weekly_google_news_evidence(
            dataset=recommender.dataset,
            season=args.season,
            start_week=args.start_week,
            end_week=args.end_week,
            documents_output=args.documents_output,
            packets_output=args.packets_output,
            report_output=args.report_output,
            lookback_days=args.lookback_days,
            max_items_per_query=args.max_items_per_query,
            max_documents_per_week=args.max_documents_per_week,
            sleep_seconds=args.sleep_seconds,
        )
        _print_json(asdict(report))
        return

    if args.command == "enrich-premierleague-fulltext":
        report = enrich_premierleague_fulltext(
            input_path=args.input,
            output_path=args.output,
            report_output=args.report_output,
            max_rows=args.max_rows,
            sleep_seconds=args.sleep_seconds,
        )
        _print_json(report)
        return

    if args.command == "enrich-evidence-fulltext":
        report = enrich_evidence_fulltext(
            input_path=args.input,
            output_path=args.output,
            report_output=args.report_output,
            max_rows=args.max_rows,
            sleep_seconds=args.sleep_seconds,
            source_name_regex=args.source_name_regex,
            category_regex=args.category_regex,
            request_timeout=args.request_timeout,
            output_every=args.output_every,
        )
        _print_json(report)
        return

    if args.command == "export-llm-sft":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        evidence_frame = (
            normalize_evidence_corpus(args.evidence, curated_only=not args.include_non_curated_evidence)
            if args.evidence
            else pd.DataFrame()
        )
        examples = build_decision_sft_examples(
            recommender.dataset,
            backtest_report_path=args.backtest_report,
            evidence_frame=evidence_frame,
            max_documents_per_week=args.max_docs_per_week,
            lookback_days=args.lookback_days,
        )
        write_llm_training_examples(examples, args.output)
        _print_json({"examples": len(examples), "output": args.output})
        return

    if args.command == "export-llm-sft-corpus":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        evidence_frame = (
            normalize_evidence_corpus(args.evidence, curated_only=not args.include_non_curated_evidence)
            if args.evidence
            else pd.DataFrame()
        )
        examples = build_multiseason_decision_sft_examples(
            dataset=recommender.dataset,
            seasons=_parse_seasons(args.seasons) if args.seasons else None,
            initial_train_week_max=args.initial_train_week_max,
            start_week=args.start_week,
            end_week=args.end_week,
            alpha=args.alpha,
            initial_budget=args.initial_budget,
            max_free_transfers=args.max_free_transfers,
            max_transfers_per_week=args.max_transfers_per_week,
            min_projected_gain=args.min_projected_gain,
            evidence_frame=evidence_frame,
            max_documents_per_week=args.max_docs_per_week,
            lookback_days=args.lookback_days,
        )
        write_llm_training_examples(examples, args.output)
        _print_json({"examples": len(examples), "output": args.output})
        return

    if args.command == "split-llm-sft":
        payload = [json.loads(line) for line in Path(args.input).read_text().splitlines() if line.strip()]
        split_payload = split_llm_examples_by_time(
            examples=payload,
            eval_season=args.eval_season,
            eval_week_min=args.eval_week_min,
            eval_week_max=args.eval_week_max,
        )
        paths = write_llm_training_split(split_payload, args.output_dir)
        _print_json(
            {
                "train_examples": len(split_payload["train"]),
                "eval_examples": len(split_payload["eval"]),
                "paths": paths,
            }
        )
        return

    if args.command == "export-llm-transfer-choice-corpus":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        evidence_frame = (
            normalize_evidence_corpus(args.evidence, curated_only=not args.include_non_curated_evidence)
            if args.evidence
            else pd.DataFrame()
        )
        examples = build_multiseason_transfer_choice_examples(
            dataset=recommender.dataset,
            seasons=_parse_seasons(args.seasons) if args.seasons else None,
            initial_train_week_max=args.initial_train_week_max,
            start_week=args.start_week,
            end_week=args.end_week,
            alpha=args.alpha,
            initial_budget=args.initial_budget,
            max_free_transfers=args.max_free_transfers,
            max_transfers_per_week=args.max_transfers_per_week,
            min_projected_gain=args.min_projected_gain,
            evidence_frame=evidence_frame,
            max_documents_per_week=args.max_docs_per_week,
            lookback_days=args.lookback_days,
        )
        write_llm_training_examples(examples, args.output)
        _print_json({"examples": len(examples), "output": args.output})
        return

    if args.command == "export-llm-player-forecast-corpus":
        recommender = FPLRecommender.from_training_csv(args.training_data)
        evidence_frame = (
            normalize_evidence_corpus(args.evidence, curated_only=not args.include_non_curated_evidence)
            if args.evidence
            else pd.DataFrame()
        )
        examples = build_multiseason_player_forecast_examples(
            dataset=recommender.dataset,
            seasons=_parse_seasons(args.seasons) if args.seasons else None,
            start_week=args.start_week,
            end_week=args.end_week,
            evidence_frame=evidence_frame,
            max_documents_per_week=args.max_docs_per_week,
            lookback_days=args.lookback_days,
            prompt_style=args.prompt_style,
            max_evidence_chars_per_document=args.max_evidence_chars_per_document,
        )
        write_llm_training_examples(examples, args.output)
        _print_json({"examples": len(examples), "output": args.output})
        return

    if args.command == "evaluate-llm-predictions":
        report = evaluate_llm_predictions(args.examples, args.predictions)
        paths = write_llm_evaluation_outputs(report, args.output_dir)
        _print_json({"report": asdict(report), "paths": paths})
        return

    if args.command == "evaluate-llm-transfer-choices":
        report = evaluate_llm_transfer_choices(args.examples, args.predictions)
        paths = write_llm_transfer_evaluation_outputs(report, args.output_dir)
        _print_json({"report": asdict(report), "paths": paths})
        return

    if args.command == "predict-week":
        recommender = FPLRecommender.from_training_csv(args.training_data, model_dir=args.model_dir)
        forecasts = recommender.predict_player_outcomes((args.season, args.week))
        records = sorted(
            [asdict(forecast) for forecast in forecasts],
            key=lambda record: record["predicted_points_3gw"],
            reverse=True,
        )[: args.top_n]
        _write_table(records, args.output)
        return

    if args.command == "recommend":
        recommender = FPLRecommender.from_training_csv(args.training_data, model_dir=args.model_dir)
        squad_state = _load_squad_state(args.squad)
        source_documents = _load_sources(args.sources) if args.sources else []
        bundle = recommender.recommend_actions(
            week_id=(args.season, args.week),
            squad_state=squad_state,
            supporting_sources=source_documents,
        )
        report = recommender.generate_cited_report(bundle)
        _print_json(
            {
                "recommendation_bundle": asdict(bundle),
                "cited_report": asdict(report),
            }
        )
        return

    if args.command == "build-hybrid-decision-context":
        recommender = FPLRecommender.from_training_csv(args.training_data, model_dir=args.model_dir)
        squad_state = _load_squad_state(args.squad)
        context = recommender.build_hybrid_decision_context(
            deadline_ts=args.deadline_ts,
            squad_state=squad_state,
            evidence_path=args.evidence,
            curated_only=not args.include_non_curated,
            max_documents=args.max_docs,
            lookback_days=args.lookback_days,
            top_n_transfers=args.top_n_transfers,
            max_transfers_considered=args.max_transfers_considered,
        )
        payload = asdict(context)
        if args.output:
            path = Path(args.output)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(payload, indent=2))
            _print_json({"output": args.output, "candidate_options": len(context.candidate_options)})
            return
        _print_json(payload)
        return


if __name__ == "__main__":
    main()

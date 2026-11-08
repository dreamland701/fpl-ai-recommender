"""Time-based evaluation and backtest reporting."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from .config import parse_season_start_year
from .dataset import CanonicalDataset
from .models import RidgeRegressor


@dataclass(frozen=True)
class MetricSummary:
    metric: str
    model_value: float
    baseline_name: str
    baseline_value: float


@dataclass(frozen=True)
class PositionMetric:
    position: str
    sample_size: int
    points_1gw_rmse: float
    minutes_rmse: float


@dataclass(frozen=True)
class EvaluationReport:
    train_seasons: Sequence[str]
    test_season: str
    test_weeks: Sequence[int]
    train_rows: int
    test_rows: int
    feature_names: Sequence[str]
    summaries: Sequence[MetricSummary]
    by_position: Sequence[PositionMetric]
    notes: Sequence[str]


def _season_week_key(frame: pd.DataFrame) -> pd.Series:
    return frame["season"].astype(str).map(parse_season_start_year) * 100 + frame["week"].astype(int)


def _rmse(actual: np.ndarray, predicted: np.ndarray) -> float:
    return float(np.sqrt(np.mean((actual - predicted) ** 2)))


def _train_test_split(
    dataset: CanonicalDataset,
    test_season: str,
    test_week_min: int = 1,
    test_week_max: Optional[int] = None,
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    frame = dataset.training_frame.copy()
    eligible = frame.loc[frame["eligible_for_backtest"]].copy()
    test_mask = (eligible["season"].astype(str) == test_season) & (eligible["week"].astype(int) >= test_week_min)
    if test_week_max is not None:
        test_mask &= eligible["week"].astype(int) <= test_week_max

    train_mask = _season_week_key(eligible) < parse_season_start_year(test_season) * 100 + test_week_min
    train_frame = eligible.loc[train_mask].copy()
    test_frame = eligible.loc[test_mask].copy()
    return train_frame, test_frame


def _baseline_points_1gw(frame: pd.DataFrame) -> np.ndarray:
    return frame["points_avg_3"].fillna(0.0).to_numpy(dtype=float)


def _baseline_minutes(frame: pd.DataFrame) -> np.ndarray:
    return frame["minutes_avg_3"].fillna(0.0).to_numpy(dtype=float)


def _fit_and_predict(
    train_frame: pd.DataFrame,
    test_frame: pd.DataFrame,
    feature_names: Sequence[str],
    target_column: str,
    alpha: float = 1.0,
) -> np.ndarray:
    model = RidgeRegressor(feature_names=feature_names, alpha=alpha).fit(train_frame, target_column)
    predictions = model.predict(test_frame)
    if target_column == "label_minutes_1gw":
        return np.clip(predictions, 0.0, 180.0)
    return np.clip(predictions, 0.0, None)


def evaluate_time_split(
    dataset: CanonicalDataset,
    test_season: str = "2025-26",
    test_week_min: int = 1,
    test_week_max: Optional[int] = 30,
    alpha: float = 1.0,
) -> EvaluationReport:
    train_frame, test_frame = _train_test_split(
        dataset,
        test_season=test_season,
        test_week_min=test_week_min,
        test_week_max=test_week_max,
    )
    if train_frame.empty or test_frame.empty:
        raise ValueError("Train/test split is empty; cannot evaluate.")

    feature_names = dataset.feature_columns
    points_predictions = _fit_and_predict(
        train_frame,
        test_frame,
        feature_names=feature_names,
        target_column="label_points_1gw",
        alpha=alpha,
    )
    minutes_predictions = _fit_and_predict(
        train_frame,
        test_frame,
        feature_names=feature_names,
        target_column="label_minutes_1gw",
        alpha=alpha,
    )
    points_actual = test_frame["label_points_1gw"].to_numpy(dtype=float)
    minutes_actual = test_frame["label_minutes_1gw"].to_numpy(dtype=float)
    baseline_points = _baseline_points_1gw(test_frame)
    baseline_minutes = _baseline_minutes(test_frame)

    summaries = [
        MetricSummary(
            metric="points_1gw_rmse",
            model_value=_rmse(points_actual, points_predictions),
            baseline_name="points_avg_3",
            baseline_value=_rmse(points_actual, baseline_points),
        ),
        MetricSummary(
            metric="minutes_rmse",
            model_value=_rmse(minutes_actual, minutes_predictions),
            baseline_name="minutes_avg_3",
            baseline_value=_rmse(minutes_actual, baseline_minutes),
        ),
    ]

    by_position: List[PositionMetric] = []
    for position in ["GK", "DEF", "MID", "FWD"]:
        mask = test_frame["position"].astype(str) == position
        if not mask.any():
            continue
        by_position.append(
            PositionMetric(
                position=position,
                sample_size=int(mask.sum()),
                points_1gw_rmse=_rmse(points_actual[mask.to_numpy()], points_predictions[mask.to_numpy()]),
                minutes_rmse=_rmse(minutes_actual[mask.to_numpy()], minutes_predictions[mask.to_numpy()]),
            )
        )

    train_seasons = sorted(train_frame["season"].astype(str).unique().tolist(), key=parse_season_start_year)
    test_weeks = sorted(test_frame["week"].astype(int).unique().tolist())
    notes = [
        "This report uses a time-based split: train on seasons strictly before the test window.",
        "GW31 of 2025-26 remains excluded from both training and backtests.",
        "Metrics below are holdout-set RMSE values, not training-set fit statistics.",
        "The current feature set includes ICT/bonus/BPS across all seasons plus xG/xA/xGI/xGC/starts/defensive contribution when the raw source provides them.",
    ]
    return EvaluationReport(
        train_seasons=train_seasons,
        test_season=test_season,
        test_weeks=test_weeks,
        train_rows=int(len(train_frame)),
        test_rows=int(len(test_frame)),
        feature_names=list(feature_names),
        summaries=summaries,
        by_position=by_position,
        notes=notes,
    )


def report_to_markdown(report: EvaluationReport) -> str:
    summary_lookup = {summary.metric: summary for summary in report.summaries}
    lines = [
        "# Honest Backtest Report",
        "",
        f"- Train seasons: {', '.join(report.train_seasons)}",
        f"- Test window: {report.test_season} GW{min(report.test_weeks)}-GW{max(report.test_weeks)}",
        f"- Train rows: {report.train_rows}",
        f"- Test rows: {report.test_rows}",
        "",
        "## Summary Metrics",
        "",
        "| Metric | Model | Baseline | Baseline Name |",
        "| --- | ---: | ---: | --- |",
    ]
    for summary in report.summaries:
        lines.append(
            f"| {summary.metric} | {summary.model_value:.4f} | {summary.baseline_value:.4f} | {summary.baseline_name} |"
        )

    lines.extend(
        [
            "",
            "## By Position",
            "",
            "| Position | Samples | Points 1GW RMSE | Minutes RMSE |",
            "| --- | ---: | ---: | ---: |",
        ]
    )
    for row in report.by_position:
        lines.append(
            f"| {row.position} | {row.sample_size} | {row.points_1gw_rmse:.4f} | {row.minutes_rmse:.4f} |"
        )

    lines.extend(["", "## Notes", ""])
    lines.extend([f"- {note}" for note in report.notes])
    return "\n".join(lines)


def write_evaluation_outputs(report: EvaluationReport, output_dir: str) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    json_path = output_path / "evaluation_report.json"
    md_path = output_path / "evaluation_report.md"
    json_path.write_text(json.dumps(asdict(report), indent=2))
    md_path.write_text(report_to_markdown(report))
    return {"json": str(json_path), "markdown": str(md_path)}

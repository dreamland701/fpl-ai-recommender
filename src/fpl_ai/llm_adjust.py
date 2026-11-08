"""Apply SFT-model residual deltas to classic-ML player forecasts.

The residual eval pipeline produces, per (season, week, player), a strict-JSON
delta object relative to the classic ML baseline. This module loads those
predictions next to their example files and applies them — clipped to the
training bounds — to `PlayerForecast` objects inside the decision/backtest
paths. Players without a prediction (outside the top-N pool the model was run
on) keep the classic forecast untouched.

Corpus baselines and backtest forecasts follow the same rolling protocol
(fit on strictly-prior weeks, alpha 1.0), so deltas computed against the
former apply cleanly to the latter.
"""

from __future__ import annotations

import json
import math
import warnings
from dataclasses import replace
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple, Union

from .types import PlayerForecast

DeltaKey = Union[Tuple[str, int, int], Tuple[int, int]]

# Inference-time clip bounds; must match the dataset builder's DELTA_SPECS.
DELTA_CLIP_BOUNDS: Mapping[str, float] = {
    "delta_points_1gw": 2.0,
    "delta_points_3gw": 4.0,
    "delta_points_5gw": 6.0,
    "delta_minutes_1gw": 20.0,
    "delta_appearance_probability": 0.25,
}


def _extract_first_json_object(text: str) -> Optional[str]:
    start = text.find("{")
    if start < 0:
        return None
    depth = 0
    in_string = False
    escape = False
    for index, char in enumerate(text[start:], start=start):
        if in_string:
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[start : index + 1]
    return None


def _finite_number(value: object) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float, str)):
        return None
    try:
        number = float(value)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def parse_delta_response(text: str) -> Optional[Dict[str, float]]:
    """Parse a model response into clipped delta values; None if unusable.

    Non-finite values (JSON NaN/Infinity, "nan" strings) and booleans are
    dropped rather than clipped: clipping NaN yields the upper bound.
    """
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        extracted = _extract_first_json_object(text)
        if extracted is None:
            return None
        try:
            parsed = json.loads(extracted)
        except json.JSONDecodeError:
            return None
    if not isinstance(parsed, dict):
        return None
    deltas: Dict[str, float] = {}
    for key, bound in DELTA_CLIP_BOUNDS.items():
        value = _finite_number(parsed.get(key))
        if value is None:
            continue
        deltas[key] = max(-bound, min(bound, value))
    return deltas or None


def _row_key(row: Mapping[str, object]) -> Optional[DeltaKey]:
    metadata = row.get("metadata") or {}
    player_id = metadata.get("player_id")
    week = row.get("week", metadata.get("week"))
    if player_id is None or week is None or int(player_id) <= 0:
        return None
    season = str(row.get("season") or metadata.get("season") or "")
    return (season, int(week), int(player_id)) if season else (int(week), int(player_id))


def load_llm_delta_lookup(
    examples_path: str | Path,
    predictions_path: str | Path,
) -> Dict[DeltaKey, Dict[str, float]]:
    """Pair eval examples with predictions and parse their deltas.

    Keys are (season, week, player_id): FPL player ids are reassigned between
    seasons, so (week, player_id) alone can attach one player's delta to
    another. Examples without a season fall back to (week, player_id).

    Prediction rows that carry their own identifiers are joined on them, so
    reordered predictions give the same lookup and any example without its
    own prediction is an error. Only legacy prediction files without
    identifiers are paired by row order.
    """
    examples: List[dict] = []
    with Path(examples_path).open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                examples.append(json.loads(line))
    predictions: List[dict] = []
    with Path(predictions_path).open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                predictions.append(json.loads(line))
    if len(examples) != len(predictions):
        raise ValueError(
            f"examples ({len(examples)}) and predictions ({len(predictions)}) row counts differ"
        )

    example_keys = [_row_key(example) for example in examples]
    prediction_keys = [_row_key(prediction) for prediction in predictions]
    if predictions and all(key is not None for key in prediction_keys):
        by_key: Dict[DeltaKey, dict] = {}
        for key, prediction in zip(prediction_keys, predictions):
            if key in by_key:
                raise ValueError(f"duplicate prediction rows for {key}")
            by_key[key] = prediction
        unmatched = [key for key in example_keys if key not in by_key]
        if unmatched:
            raise ValueError(f"{len(unmatched)} examples have no matching prediction, e.g. {unmatched[0]}")
        pairs = [(key, by_key[key]) for key in example_keys]
    else:
        pairs = list(zip(example_keys, predictions))

    lookup: Dict[DeltaKey, Dict[str, float]] = {}
    duplicates = 0
    for key, prediction in pairs:
        if key is None:
            continue
        deltas = parse_delta_response(str(prediction.get("response") or ""))
        if deltas is None:
            continue
        if key in lookup:
            duplicates += 1
            continue
        lookup[key] = deltas
    if duplicates:
        warnings.warn(f"{duplicates} duplicate (season, week, player) delta rows ignored; first kept")
    return lookup


def _lookup_deltas(
    lookup: Mapping[DeltaKey, Mapping[str, float]], forecast: PlayerForecast, week: int
) -> Optional[Mapping[str, float]]:
    deltas = lookup.get((str(forecast.season), int(week), int(forecast.player_id)))
    if deltas is None:
        deltas = lookup.get((int(week), int(forecast.player_id)))
    return deltas


def apply_deltas_to_forecast(
    forecast: PlayerForecast,
    deltas: Optional[Mapping[str, float]],
    fields: str = "all",
) -> PlayerForecast:
    """The one place deltas meet forecasts, for backtests and live alike.

    fields modes:

    - 'all': apply every delta.
    - 'points': points horizons only.
    - 'availability': minutes + appearance probability only — keeps classic
      points ordering (decision-inert with the current threshold-style
      optimizer penalty; kept for comparison).
    - 'availability_scaled': replace classic P(appear) with the LLM's and
      rescale points by the ratio. Unconditional points = conditional x
      P(appear), so a better-calibrated P legitimately rescales expected
      points; ratio clamped to [0.6, 1.4] to bound single-signal influence.
    """
    if fields not in {"all", "points", "availability", "availability_scaled"}:
        raise ValueError(f"unknown fields mode: {fields}")
    if not deltas:
        return forecast
    clipped: Dict[str, float] = {}
    for key, bound in DELTA_CLIP_BOUNDS.items():
        value = _finite_number(deltas.get(key))
        if value is not None:
            clipped[key] = max(-bound, min(bound, value))
    if fields == "availability_scaled":
        new_probability = min(
            1.0, max(0.0, forecast.appearance_probability + clipped.get("delta_appearance_probability", 0.0))
        )
        old_probability = max(forecast.appearance_probability, 1e-6)
        ratio = min(1.4, max(0.6, new_probability / old_probability))
        return replace(
            forecast,
            predicted_points_1gw=forecast.predicted_points_1gw * ratio,
            predicted_points_3gw=forecast.predicted_points_3gw * ratio,
            predicted_points_5gw=forecast.predicted_points_5gw * ratio,
            predicted_minutes=max(0.0, forecast.predicted_minutes + clipped.get("delta_minutes_1gw", 0.0)),
            appearance_probability=new_probability,
        )
    changes: Dict[str, float] = {}
    if fields in {"all", "points"}:
        changes["predicted_points_1gw"] = forecast.predicted_points_1gw + clipped.get("delta_points_1gw", 0.0)
        changes["predicted_points_3gw"] = forecast.predicted_points_3gw + clipped.get("delta_points_3gw", 0.0)
        changes["predicted_points_5gw"] = forecast.predicted_points_5gw + clipped.get("delta_points_5gw", 0.0)
    if fields in {"all", "availability"}:
        changes["predicted_minutes"] = max(0.0, forecast.predicted_minutes + clipped.get("delta_minutes_1gw", 0.0))
        changes["appearance_probability"] = min(
            1.0, max(0.0, forecast.appearance_probability + clipped.get("delta_appearance_probability", 0.0))
        )
    return replace(forecast, **changes)


def apply_llm_deltas(
    forecasts: Sequence[PlayerForecast],
    lookup: Mapping[DeltaKey, Mapping[str, float]],
    week: int,
    fields: str = "all",
) -> List[PlayerForecast]:
    """Apply looked-up deltas (see apply_deltas_to_forecast for fields)."""
    if fields not in {"all", "points", "availability", "availability_scaled"}:
        raise ValueError(f"unknown fields mode: {fields}")
    return [apply_deltas_to_forecast(forecast, _lookup_deltas(lookup, forecast, week), fields) for forecast in forecasts]

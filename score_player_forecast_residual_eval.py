from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable


DELTA_TO_TARGET = {
    "delta_points_1gw": ("baseline_points_1gw", "points_1gw", "final_points_1gw"),
    "delta_points_3gw": ("baseline_points_3gw", "points_3gw", "final_points_3gw"),
    "delta_points_5gw": ("baseline_points_5gw", "points_5gw", "final_points_5gw"),
    "delta_minutes_1gw": ("baseline_minutes_1gw", "minutes_1gw", "final_minutes_1gw"),
    "delta_appearance_probability": (
        "baseline_appearance_probability",
        "appearance_probability",
        "final_appearance_probability",
    ),
}


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def is_strict_json(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith("{") and stripped.endswith("}")


def extract_first_json_object(text: str) -> str | None:
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


def parse_prediction(text: str) -> dict[str, Any] | None:
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        extracted = extract_first_json_object(text)
        if extracted is None:
            return None
        try:
            parsed = json.loads(extracted)
        except json.JSONDecodeError:
            return None
    return parsed if isinstance(parsed, dict) else None


def as_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def rmse(pairs: list[tuple[float, float]]) -> float | None:
    if not pairs:
        return None
    return math.sqrt(sum((pred - target) ** 2 for pred, target in pairs) / len(pairs))


def mae(pairs: list[tuple[float, float]]) -> float | None:
    if not pairs:
        return None
    return sum(abs(pred - target) for pred, target in pairs) / len(pairs)


def _average_ranks(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda index: values[index])
    ranks = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start
        while end + 1 < len(order) and values[order[end + 1]] == values[order[start]]:
            end += 1
        average = (start + end) / 2 + 1
        for position in range(start, end + 1):
            ranks[order[position]] = average
        start = end + 1
    return ranks


def _pearson(a: list[float], b: list[float]) -> float | None:
    n = len(a)
    if n < 2:
        return None
    mean_a = sum(a) / n
    mean_b = sum(b) / n
    cov = sum((x - mean_a) * (y - mean_b) for x, y in zip(a, b))
    var_a = sum((x - mean_a) ** 2 for x in a)
    var_b = sum((y - mean_b) ** 2 for y in b)
    if var_a == 0 or var_b == 0:
        return None
    return cov / math.sqrt(var_a * var_b)


def spearman(a: list[float], b: list[float]) -> float | None:
    return _pearson(_average_ranks(a), _average_ranks(b))


def ranking_metrics(
    rows: list[dict[str, Any]],
    predictor: Callable[[dict[str, Any], str], float],
    top_k: int = 11,
) -> dict[str, float]:
    """Week-wise rank quality: mean Spearman vs realized points, and the
    realized points of the predicted top-k (a proxy XI) per week."""
    by_week: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_week[(str(row["season"]), int(row["week"]))].append(row)

    metrics: dict[str, float] = {}
    for horizon in ("points_1gw", "points_5gw"):
        correlations: list[float] = []
        top_k_realized: list[float] = []
        for group in by_week.values():
            predictions = [predictor(row, horizon) for row in group]
            targets = [float(row[f"target_{horizon}"]) for row in group]
            correlation = spearman(predictions, targets)
            if correlation is not None:
                correlations.append(correlation)
            order = sorted(range(len(group)), key=lambda index: predictions[index], reverse=True)
            top_k_realized.append(sum(targets[index] for index in order[:top_k]))
        if correlations:
            metrics[f"spearman_{horizon}"] = round(sum(correlations) / len(correlations), 4)
        if top_k_realized:
            metrics[f"top{top_k}_realized_{horizon}_per_week"] = round(
                sum(top_k_realized) / len(top_k_realized), 3
            )
    return metrics


def model_predictor(row: dict[str, Any], horizon: str) -> float:
    # Unparseable responses fall back to the classic ML anchor, matching what
    # the downstream optimizer would consume.
    final_value = row.get(f"final_{horizon}")
    if final_value is None:
        return float(row[f"baseline_{horizon}"])
    return float(final_value)


def classic_predictor(row: dict[str, Any], horizon: str) -> float:
    return float(row[f"baseline_{horizon}"])


def clamp_prediction(final_key: str, value: float) -> float:
    if final_key == "final_appearance_probability":
        return min(1.0, max(0.0, value))
    if final_key == "final_minutes_1gw":
        return max(0.0, value)
    return value


def summarize_predictions(examples: list[dict[str, Any]], predictions: list[dict[str, Any]]):
    strict_json_predictions = 0
    parseable_json_predictions = 0
    pairs_by_final = {final_key: [] for _, _, final_key in DELTA_TO_TARGET.values()}
    delta_pairs = {delta_key: [] for delta_key in DELTA_TO_TARGET}
    rows = []

    for example, prediction in zip(examples, predictions):
        response = prediction["response"]
        strict = is_strict_json(response)
        parsed = parse_prediction(response)
        if strict:
            strict_json_predictions += 1
        if parsed is not None:
            parseable_json_predictions += 1

        metadata = example["metadata"]
        baseline = metadata["baseline_forecast"]
        labels = metadata["labels"]
        row = {
            "season": example["season"],
            "week": example["week"],
            "player_id": metadata["player_id"],
            "player_name": metadata["player_name"],
            "strict_json": strict,
            "parseable_json": parsed is not None,
        }

        for delta_key, (baseline_key, label_key, final_key) in DELTA_TO_TARGET.items():
            base_value = float(baseline.get(baseline_key) or 0.0)
            target_value = float(labels.get(label_key) or 0.0)
            target_delta = target_value - base_value
            pred_delta = as_float(parsed.get(delta_key)) if parsed is not None else None
            final_value = clamp_prediction(final_key, base_value + pred_delta) if pred_delta is not None else None

            row[f"baseline_{label_key}"] = base_value
            row[f"target_{label_key}"] = target_value
            row[delta_key] = pred_delta
            row[f"target_{delta_key}"] = target_delta
            row[final_key] = final_value

            if final_value is not None:
                pairs_by_final[final_key].append((final_value, target_value))
            if pred_delta is not None:
                delta_pairs[delta_key].append((pred_delta, target_delta))

        rows.append(row)

    summary: dict[str, Any] = {
        "total_examples": len(examples),
        "strict_json_predictions": strict_json_predictions,
        "parseable_json_predictions": parseable_json_predictions,
    }
    for final_key, pairs in pairs_by_final.items():
        if pairs:
            summary[f"{final_key}_rmse"] = round(rmse(pairs), 4)
            summary[f"{final_key}_mae"] = round(mae(pairs), 4)
    for delta_key, pairs in delta_pairs.items():
        if pairs:
            summary[f"{delta_key}_rmse"] = round(rmse(pairs), 4)
            summary[f"{delta_key}_mae"] = round(mae(pairs), 4)
    return summary, rows


def summarize_classic(examples: list[dict[str, Any]]):
    pairs_by_final = {final_key: [] for _, _, final_key in DELTA_TO_TARGET.values()}
    for example in examples:
        baseline = example["metadata"]["baseline_forecast"]
        labels = example["metadata"]["labels"]
        for _, (baseline_key, label_key, final_key) in DELTA_TO_TARGET.items():
            pairs_by_final[final_key].append((float(baseline.get(baseline_key) or 0.0), float(labels.get(label_key) or 0.0)))
    summary: dict[str, Any] = {"total_examples": len(examples)}
    for final_key, pairs in pairs_by_final.items():
        summary[f"{final_key}_rmse"] = round(rmse(pairs), 4)
        summary[f"{final_key}_mae"] = round(mae(pairs), 4)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--examples", required=True)
    parser.add_argument("--base-predictions", required=True)
    parser.add_argument("--sft-predictions", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--examples-out")
    args = parser.parse_args()

    examples = load_jsonl(Path(args.examples))
    base_predictions = load_jsonl(Path(args.base_predictions))
    sft_predictions = load_jsonl(Path(args.sft_predictions))
    if len(base_predictions) != len(examples):
        raise ValueError(f"Base predictions count {len(base_predictions)} != examples count {len(examples)}")
    if len(sft_predictions) != len(examples):
        raise ValueError(f"SFT predictions count {len(sft_predictions)} != examples count {len(examples)}")

    base_summary, base_rows = summarize_predictions(examples, base_predictions)
    sft_summary, sft_rows = summarize_predictions(examples, sft_predictions)
    classic_summary = summarize_classic(examples)

    base_summary.update(ranking_metrics(base_rows, model_predictor))
    sft_summary.update(ranking_metrics(sft_rows, model_predictor))
    classic_summary.update(ranking_metrics(base_rows, classic_predictor))
    ranking_lift = {}
    for key, classic_value in classic_summary.items():
        if key.startswith(("spearman_", "top11_realized_")) and key in sft_summary:
            ranking_lift[f"sft_{key}_vs_classic"] = round(sft_summary[key] - classic_value, 4)

    examples_out = []
    for base_row, sft_row in zip(base_rows[:12], sft_rows[:12]):
        examples_out.append(
            {
                "season": base_row["season"],
                "week": base_row["week"],
                "player_id": base_row["player_id"],
                "player_name": base_row["player_name"],
                "target_points_1gw": base_row["target_points_1gw"],
                "classic_points_1gw": base_row["baseline_points_1gw"],
                "base_final_points_1gw": base_row["final_points_1gw"],
                "sft_final_points_1gw": sft_row["final_points_1gw"],
                "base_delta_points_1gw": base_row["delta_points_1gw"],
                "sft_delta_points_1gw": sft_row["delta_points_1gw"],
                "target_points_5gw": base_row["target_points_5gw"],
                "classic_points_5gw": base_row["baseline_points_5gw"],
                "base_final_points_5gw": base_row["final_points_5gw"],
                "sft_final_points_5gw": sft_row["final_points_5gw"],
                "target_minutes_1gw": base_row["target_minutes_1gw"],
                "classic_minutes_1gw": base_row["baseline_minutes_1gw"],
                "base_final_minutes_1gw": base_row["final_minutes_1gw"],
                "sft_final_minutes_1gw": sft_row["final_minutes_1gw"],
                "base_strict_json": base_row["strict_json"],
                "sft_strict_json": sft_row["strict_json"],
            }
        )

    summary = {
        "classic_ml": classic_summary,
        "base_gemma_delta": base_summary,
        "sft_gemma_delta": sft_summary,
        "ranking_lift": ranking_lift,
        "examples": examples_out,
    }
    Path(args.output).write_text(json.dumps(summary, indent=2) + "\n")
    if args.examples_out:
        Path(args.examples_out).write_text(json.dumps({"base_rows": base_rows, "sft_rows": sft_rows}, indent=2) + "\n")


if __name__ == "__main__":
    main()

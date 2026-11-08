from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


TARGET_FIELDS = [
    "predicted_points_1gw",
    "predicted_points_3gw",
    "predicted_points_5gw",
    "predicted_minutes_1gw",
    "predicted_appearance_probability",
]


def load_jsonl(path: Path):
    rows = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def is_strict_json(text: str) -> bool:
    stripped = text.strip()
    return stripped.startswith("{") and stripped.endswith("}")


def extract_first_json_object(text: str):
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


def parse_prediction(text: str):
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
    if not isinstance(parsed, dict):
        return None
    return parsed


def as_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def rmse(pairs):
    if not pairs:
        return None
    mse = sum((pred - target) ** 2 for pred, target in pairs) / len(pairs)
    return math.sqrt(mse)


def mae(pairs):
    if not pairs:
        return None
    return sum(abs(pred - target) for pred, target in pairs) / len(pairs)


def summarize_split(examples, predictions):
    total_examples = len(examples)
    strict_json_predictions = 0
    parseable_json_predictions = 0
    pairs_by_field = {field: [] for field in TARGET_FIELDS}
    scored_rows = []

    for example, prediction in zip(examples, predictions):
        response = prediction["response"]
        strict = is_strict_json(response)
        if strict:
            strict_json_predictions += 1
        parsed = parse_prediction(response)
        if parsed is not None:
            parseable_json_predictions += 1

        row = {
            "season": example["season"],
            "week": example["week"],
            "player_id": example["metadata"]["player_id"],
            "player_name": example["metadata"]["player_name"],
            "strict_json": strict,
            "parseable_json": parsed is not None,
        }

        for field in TARGET_FIELDS:
            pred_value = as_float(parsed.get(field)) if parsed is not None else None
            target_key = {
                "predicted_points_1gw": "points_1gw",
                "predicted_points_3gw": "points_3gw",
                "predicted_points_5gw": "points_5gw",
                "predicted_minutes_1gw": "minutes_1gw",
                "predicted_appearance_probability": "appearance_probability",
            }[field]
            target_value = as_float(example["metadata"]["labels"][target_key])
            row[field] = pred_value
            row[f"target_{target_key}"] = target_value
            if pred_value is not None and target_value is not None:
                pairs_by_field[field].append((pred_value, target_value))

        scored_rows.append(row)

    summary = {
        "total_examples": total_examples,
        "strict_json_predictions": strict_json_predictions,
        "parseable_json_predictions": parseable_json_predictions,
    }

    for field in TARGET_FIELDS:
        rmse_value = rmse(pairs_by_field[field])
        mae_value = mae(pairs_by_field[field])
        if rmse_value is not None:
            summary[f"{field}_rmse"] = round(rmse_value, 4)
        if mae_value is not None:
            summary[f"{field}_mae"] = round(mae_value, 4)

    return summary, scored_rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--examples", required=True)
    parser.add_argument("--base-predictions", required=True)
    parser.add_argument("--sft-predictions", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--examples-out", required=False)
    args = parser.parse_args()

    examples = load_jsonl(Path(args.examples))
    base_predictions = load_jsonl(Path(args.base_predictions))
    sft_predictions = load_jsonl(Path(args.sft_predictions))

    if len(base_predictions) != len(examples):
        raise ValueError(f"Base predictions count {len(base_predictions)} != examples count {len(examples)}")
    if len(sft_predictions) != len(examples):
        raise ValueError(f"SFT predictions count {len(sft_predictions)} != examples count {len(examples)}")

    base_summary, base_rows = summarize_split(examples, base_predictions)
    sft_summary, sft_rows = summarize_split(examples, sft_predictions)

    examples_out = []
    for base_row, sft_row in zip(base_rows[:12], sft_rows[:12]):
        examples_out.append(
            {
                "season": base_row["season"],
                "week": base_row["week"],
                "player_id": base_row["player_id"],
                "player_name": base_row["player_name"],
                "target_points_1gw": base_row["target_points_1gw"],
                "base_points_1gw": base_row["predicted_points_1gw"],
                "sft_points_1gw": sft_row["predicted_points_1gw"],
                "target_points_3gw": base_row["target_points_3gw"],
                "base_points_3gw": base_row["predicted_points_3gw"],
                "sft_points_3gw": sft_row["predicted_points_3gw"],
                "target_points_5gw": base_row["target_points_5gw"],
                "base_points_5gw": base_row["predicted_points_5gw"],
                "sft_points_5gw": sft_row["predicted_points_5gw"],
                "target_minutes_1gw": base_row["target_minutes_1gw"],
                "base_minutes_1gw": base_row["predicted_minutes_1gw"],
                "sft_minutes_1gw": sft_row["predicted_minutes_1gw"],
                "base_strict_json": base_row["strict_json"],
                "sft_strict_json": sft_row["strict_json"],
            }
        )

    summary = {
        "base": base_summary,
        "sft": sft_summary,
        "examples": examples_out,
    }

    output_path = Path(args.output)
    output_path.write_text(json.dumps(summary, indent=2))

    if args.examples_out:
        Path(args.examples_out).write_text(json.dumps({"base_rows": base_rows, "sft_rows": sft_rows}, indent=2))


if __name__ == "__main__":
    main()

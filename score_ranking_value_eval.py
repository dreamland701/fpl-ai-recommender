from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


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


def coerce_player_ids(value: Any) -> list[int]:
    if not isinstance(value, list):
        return []
    ids: list[int] = []
    for item in value:
        try:
            ids.append(int(item))
        except (TypeError, ValueError):
            continue
    return ids


def dcg(values: list[float]) -> float:
    return sum(value / math.log2(index + 2) for index, value in enumerate(values))


def summarize(examples: list[dict[str, Any]], predictions: list[dict[str, Any]], source: str) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    strict = 0
    parseable = 0
    top1_hits = 0
    top3_hits = 0
    top5_overlap = 0
    predicted_value_sum = 0.0
    oracle_value_sum = 0.0
    baseline_value_sum = 0.0
    ndcg_sum = 0.0
    valid_rankings = 0
    detail_rows: list[dict[str, Any]] = []

    for example, prediction in zip(examples, predictions):
        response = prediction.get("response", "")
        parsed = parse_prediction(response)
        if is_strict_json(response):
            strict += 1
        if parsed is not None:
            parseable += 1
        predicted_ids = []
        if parsed is not None:
            predicted_ids = coerce_player_ids(parsed.get("final_ranked_player_ids"))
            if not predicted_ids:
                predicted_ids = coerce_player_ids(parsed.get("ranked_player_ids"))

        metadata = example["metadata"]
        candidates = {int(row["player_id"]): row for row in metadata["candidates"]}
        oracle_ids = [int(value) for value in metadata["target_ranked_player_ids"]]
        baseline_ids = [int(value) for value in metadata["baseline_ranked_player_ids"]]
        anchored_target_ids = [
            int(value) for value in metadata.get("anchored_target_ranked_player_ids", oracle_ids)
        ]
        rank_size = len(oracle_ids)
        oracle_set = set(oracle_ids)

        clean_predicted_ids: list[int] = []
        seen: set[int] = set()
        for player_id in predicted_ids:
            if player_id in candidates and player_id not in seen:
                clean_predicted_ids.append(player_id)
                seen.add(player_id)
            if len(clean_predicted_ids) >= rank_size:
                break

        if clean_predicted_ids:
            valid_rankings += 1
            if clean_predicted_ids[0] == oracle_ids[0]:
                top1_hits += 1
            if oracle_ids[0] in clean_predicted_ids[:3]:
                top3_hits += 1
            top5_overlap += len(set(clean_predicted_ids[:rank_size]) & oracle_set)
            predicted_values = [float(candidates[player_id]["actual_value"]) for player_id in clean_predicted_ids[:rank_size]]
            predicted_value_sum += sum(predicted_values)
            ideal_values = [float(candidates[player_id]["actual_value"]) for player_id in oracle_ids[:rank_size]]
            ideal_dcg = dcg(ideal_values)
            ndcg_sum += dcg(predicted_values) / ideal_dcg if ideal_dcg else 0.0

        oracle_value_sum += sum(float(candidates[player_id]["actual_value"]) for player_id in oracle_ids[:rank_size])
        baseline_value_sum += sum(float(candidates[player_id]["actual_value"]) for player_id in baseline_ids[:rank_size])
        anchored_target_value = sum(
            float(candidates[player_id]["actual_value"]) for player_id in anchored_target_ids[:rank_size]
        )
        if len(detail_rows) < 12:
            detail_rows.append(
                {
                    "source": source,
                    "season": example["season"],
                    "week": example["week"],
                    "strict_json": is_strict_json(response),
                    "parseable_json": parsed is not None,
                    "predicted_ids": clean_predicted_ids,
                    "oracle_ids": oracle_ids,
                    "baseline_ids": baseline_ids,
                    "anchored_target_ids": anchored_target_ids,
                    "predicted_value": round(sum(float(candidates[player_id]["actual_value"]) for player_id in clean_predicted_ids[:rank_size]), 4),
                    "oracle_value": round(sum(float(candidates[player_id]["actual_value"]) for player_id in oracle_ids[:rank_size]), 4),
                    "baseline_value": round(sum(float(candidates[player_id]["actual_value"]) for player_id in baseline_ids[:rank_size]), 4),
                    "anchored_target_value": round(anchored_target_value, 4),
                    "candidates": [
                        {
                            "player_id": int(row["player_id"]),
                            "player_name": row["player_name"],
                            "baseline_value": row["baseline_value"],
                            "actual_value": row["actual_value"],
                        }
                        for row in metadata["candidates"]
                    ],
                }
            )

    total = len(examples)
    summary = {
        "total_examples": total,
        "strict_json_predictions": strict,
        "parseable_json_predictions": parseable,
        "valid_rankings": valid_rankings,
        "top1_accuracy": round(top1_hits / valid_rankings, 4) if valid_rankings else 0.0,
        "top3_contains_oracle_top1": round(top3_hits / valid_rankings, 4) if valid_rankings else 0.0,
        "top5_overlap_rate": round(top5_overlap / (valid_rankings * 5), 4) if valid_rankings else 0.0,
        "predicted_top5_value_per_example": round(predicted_value_sum / valid_rankings, 4) if valid_rankings else 0.0,
        "baseline_top5_value_per_example": round(baseline_value_sum / total, 4) if total else 0.0,
        "oracle_top5_value_per_example": round(oracle_value_sum / total, 4) if total else 0.0,
        "ndcg_at_5": round(ndcg_sum / valid_rankings, 4) if valid_rankings else 0.0,
    }
    if examples and "anchored_target_ranked_player_ids" in examples[0].get("metadata", {}):
        anchored_sum = 0.0
        for example in examples:
            metadata = example["metadata"]
            candidates = {int(row["player_id"]): row for row in metadata["candidates"]}
            anchored_ids = [int(value) for value in metadata["anchored_target_ranked_player_ids"]]
            rank_size = len(metadata["target_ranked_player_ids"])
            anchored_sum += sum(float(candidates[player_id]["actual_value"]) for player_id in anchored_ids[:rank_size])
        summary["anchored_target_top5_value_per_example"] = round(anchored_sum / total, 4) if total else 0.0
        summary["predicted_vs_baseline_value_delta_per_example"] = round(
            summary["predicted_top5_value_per_example"] - summary["baseline_top5_value_per_example"],
            4,
        )
        summary["predicted_vs_anchored_target_value_gap_per_example"] = round(
            summary["anchored_target_top5_value_per_example"] - summary["predicted_top5_value_per_example"],
            4,
        )
    return summary, detail_rows


def baseline_summary(examples: list[dict[str, Any]]) -> dict[str, Any]:
    predictions = []
    for example in examples:
        predictions.append({"response": json.dumps({"ranked_player_ids": example["metadata"]["baseline_ranked_player_ids"]})})
    summary, _ = summarize(examples, predictions, "classic_ml")
    summary["strict_json_predictions"] = len(examples)
    summary["parseable_json_predictions"] = len(examples)
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

    classic = baseline_summary(examples)
    base, base_rows = summarize(examples, base_predictions, "base_gemma")
    sft, sft_rows = summarize(examples, sft_predictions, "sft_gemma")
    summary = {
        "classic_ml": classic,
        "base_gemma": base,
        "sft_gemma": sft,
        "examples": sft_rows[:8],
    }
    Path(args.output).write_text(json.dumps(summary, indent=2) + "\n")
    if args.examples_out:
        Path(args.examples_out).write_text(json.dumps({"base_rows": base_rows, "sft_rows": sft_rows}, indent=2) + "\n")


if __name__ == "__main__":
    main()

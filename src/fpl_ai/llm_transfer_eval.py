"""Evaluation utilities for transfer-choice LLM outputs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple


@dataclass(frozen=True)
class LLMTransferChoiceWeekResult:
    season: str
    week: int
    prediction_found: bool
    valid_json: bool
    selected_option_match: bool
    predicted_option_id: Optional[int]
    target_option_id: int
    predicted_option_actual_score: float
    target_option_actual_score: float
    score_gap_vs_target: float


@dataclass(frozen=True)
class LLMTransferChoiceEvaluationReport:
    total_examples: int
    matched_predictions: int
    valid_json_predictions: int
    option_accuracy: float
    average_predicted_option_actual_score: float
    average_target_option_actual_score: float
    average_score_gap_vs_target: float
    weeks: Sequence[LLMTransferChoiceWeekResult]
    notes: Sequence[str]


def _load_jsonl(path: str) -> List[Dict[str, object]]:
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]


def _parse_response_json(value: object) -> Optional[Dict[str, object]]:
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                return None
    return None


def _prediction_lookup(records: Sequence[Mapping[str, object]]) -> Dict[Tuple[str, int], Mapping[str, object]]:
    lookup: Dict[Tuple[str, int], Mapping[str, object]] = {}
    for record in records:
        season = str(record.get("season", ""))
        week_value = record.get("week")
        if not season or week_value is None:
            continue
        lookup[(season, int(week_value))] = record
    return lookup


def _assistant_target(example: Mapping[str, object]) -> Dict[str, object]:
    messages = list(example.get("messages", []))
    assistant_messages = [message for message in messages if message.get("role") == "assistant"]
    if not assistant_messages:
        raise ValueError("Example is missing assistant target content.")
    parsed = _parse_response_json(assistant_messages[-1].get("content"))
    if parsed is None:
        raise ValueError("Assistant target is not valid JSON.")
    return parsed


def evaluate_llm_transfer_choices(example_path: str, prediction_path: str) -> LLMTransferChoiceEvaluationReport:
    examples = _load_jsonl(example_path)
    prediction_lookup = _prediction_lookup(_load_jsonl(prediction_path))
    week_results: List[LLMTransferChoiceWeekResult] = []
    for example in examples:
        season = str(example["season"])
        week = int(example["week"])
        target = _assistant_target(example)
        metadata = dict(example.get("metadata", {}))
        candidate_options = {
            int(option["option_id"]): option for option in metadata.get("candidate_options", [])
        }
        record = prediction_lookup.get((season, week))
        parsed_prediction = None if record is None else _parse_response_json(
            record.get("response", record.get("assistant", record.get("prediction")))
        )
        target_option_id = int(target.get("selected_option", 0))
        predicted_option_id: Optional[int] = None
        if parsed_prediction is not None and parsed_prediction.get("selected_option") is not None:
            try:
                predicted_option_id = int(parsed_prediction.get("selected_option"))
            except (TypeError, ValueError):
                predicted_option_id = None
        predicted_score = (
            float(candidate_options.get(predicted_option_id, {}).get("actual_score", 0.0))
            if predicted_option_id is not None
            else 0.0
        )
        target_score = float(candidate_options.get(target_option_id, {}).get("actual_score", 0.0))
        week_results.append(
            LLMTransferChoiceWeekResult(
                season=season,
                week=week,
                prediction_found=record is not None,
                valid_json=parsed_prediction is not None,
                selected_option_match=predicted_option_id == target_option_id,
                predicted_option_id=predicted_option_id,
                target_option_id=target_option_id,
                predicted_option_actual_score=round(predicted_score, 2),
                target_option_actual_score=round(target_score, 2),
                score_gap_vs_target=round(predicted_score - target_score, 2),
            )
        )

    def mean(values: Sequence[float]) -> float:
        return round(sum(values) / max(len(values), 1), 4)

    return LLMTransferChoiceEvaluationReport(
        total_examples=len(week_results),
        matched_predictions=sum(result.prediction_found for result in week_results),
        valid_json_predictions=sum(result.valid_json for result in week_results),
        option_accuracy=mean([1.0 if result.selected_option_match else 0.0 for result in week_results]),
        average_predicted_option_actual_score=mean([result.predicted_option_actual_score for result in week_results]),
        average_target_option_actual_score=mean([result.target_option_actual_score for result in week_results]),
        average_score_gap_vs_target=mean([result.score_gap_vs_target for result in week_results]),
        weeks=week_results,
        notes=[
            "This evaluator scores selected transfer options against outcome-labeled candidate choices.",
            "Target options are the best realized weekly choices among the legal candidate set exported for each pre-deadline week.",
        ],
    )


def report_to_markdown(report: LLMTransferChoiceEvaluationReport) -> str:
    lines = [
        "# LLM Transfer-Choice Evaluation",
        "",
        f"- Total eval examples: {report.total_examples}",
        f"- Matched predictions: {report.matched_predictions}",
        f"- Valid JSON predictions: {report.valid_json_predictions}",
        f"- Option accuracy: {report.option_accuracy:.4f}",
        f"- Avg predicted-option actual score: {report.average_predicted_option_actual_score:.4f}",
        f"- Avg target-option actual score: {report.average_target_option_actual_score:.4f}",
        f"- Avg score gap vs target: {report.average_score_gap_vs_target:.4f}",
        "",
        "## Notes",
        "",
    ]
    lines.extend([f"- {note}" for note in report.notes])
    lines.extend(
        [
            "",
            "## Weekly Results",
            "",
            "| Week | Found | JSON | Match | Pred Opt | Target Opt | Pred Score | Target Score | Gap |",
            "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for result in report.weeks:
        pred_option = "" if result.predicted_option_id is None else str(result.predicted_option_id)
        lines.append(
            f"| {result.season} GW{result.week} | {result.prediction_found} | {result.valid_json} | "
            f"{result.selected_option_match} | {pred_option} | {result.target_option_id} | "
            f"{result.predicted_option_actual_score:.2f} | {result.target_option_actual_score:.2f} | "
            f"{result.score_gap_vs_target:.2f} |"
        )
    return "\n".join(lines)


def write_llm_transfer_evaluation_outputs(
    report: LLMTransferChoiceEvaluationReport,
    output_dir: str,
) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    json_path = output_path / "llm_transfer_choice_evaluation_report.json"
    markdown_path = output_path / "llm_transfer_choice_evaluation_report.md"
    json_path.write_text(json.dumps(asdict(report), indent=2))
    markdown_path.write_text(report_to_markdown(report))
    return {"json": str(json_path), "markdown": str(markdown_path)}

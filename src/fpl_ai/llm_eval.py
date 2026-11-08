"""Evaluation utilities for week-by-week LLM decision outputs."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence, Tuple

from .rules import POSITION_ORDER, automatic_substitutions


@dataclass(frozen=True)
class LLMWeekPredictionResult:
    season: str
    week: int
    prediction_found: bool
    valid_json: bool
    captain_match: bool
    vice_captain_match: bool
    chip_match: bool
    transfer_exact_match: bool
    starters_jaccard: float
    bench_slot_accuracy: float
    predicted_policy_actual_score: float
    target_policy_actual_score: float
    score_gap_vs_target: float


@dataclass(frozen=True)
class LLMEvaluationReport:
    total_examples: int
    matched_predictions: int
    valid_json_predictions: int
    captain_accuracy: float
    vice_captain_accuracy: float
    chip_accuracy: float
    transfer_exact_match_rate: float
    starters_jaccard_mean: float
    bench_slot_accuracy_mean: float
    average_predicted_policy_actual_score: float
    average_target_policy_actual_score: float
    average_score_gap_vs_target: float
    weeks: Sequence[LLMWeekPredictionResult]
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


def _normalized_names(value: object) -> List[str]:
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def _normalized_transfer_signature(transfers: object) -> List[Tuple[Tuple[str, ...], Tuple[str, ...]]]:
    if not isinstance(transfers, list):
        return []
    signature = []
    for transfer in transfers:
        if not isinstance(transfer, Mapping):
            continue
        signature.append(
            (
                tuple(sorted(_normalized_names(transfer.get("players_out")))),
                tuple(sorted(_normalized_names(transfer.get("players_in")))),
            )
        )
    return sorted(signature)


def _apply_autosubs(
    starters: Sequence[str],
    bench_order: Sequence[str],
    positions: Mapping[str, str],
    actual_minutes: Mapping[str, float],
) -> List[str]:
    known = {name: str(positions[name]) for name in positions if str(positions[name]) in POSITION_ORDER}
    starters = [name for name in dict.fromkeys(starters) if name in known]
    bench_order = [name for name in dict.fromkeys(bench_order) if name in known and name not in starters]
    minutes = {name: float(actual_minutes.get(name, 0.0)) for name in starters + bench_order}
    counted, _ = automatic_substitutions(known, starters, bench_order, minutes)
    return sorted(dict.fromkeys(counted))


def _score_prediction_bundle(
    metadata: Mapping[str, object],
    prediction: Mapping[str, object],
) -> float:
    positions = {str(key): str(value) for key, value in dict(metadata.get("player_positions", {})).items()}
    actual_points = {str(key): float(value) for key, value in dict(metadata.get("player_actual_points", {})).items()}
    actual_minutes = {str(key): float(value) for key, value in dict(metadata.get("player_actual_minutes", {})).items()}
    current_squad = _normalized_names(metadata.get("current_squad_names"))
    squad_names = set(current_squad)

    transfers = prediction.get("transfers", [])
    transfer_count = 0
    if isinstance(transfers, list):
        for transfer in transfers:
            if not isinstance(transfer, Mapping):
                continue
            players_out = _normalized_names(transfer.get("players_out"))
            players_in = _normalized_names(transfer.get("players_in"))
            transfer_count += len(players_in)
            for player_name in players_out:
                squad_names.discard(player_name)
            for player_name in players_in:
                squad_names.add(player_name)

    starters = [name for name in _normalized_names(prediction.get("starters")) if name in squad_names]
    bench_order = [name for name in _normalized_names(prediction.get("bench_order")) if name in squad_names and name not in starters]
    remaining_players = [name for name in sorted(squad_names) if name not in starters and name not in bench_order]
    bench_order = bench_order + remaining_players

    chip = str(prediction.get("chip", "none") or "none")
    captain = str(prediction.get("captain", "")).strip()
    vice_captain = str(prediction.get("vice_captain", "")).strip()
    free_transfers_before = int(metadata.get("free_transfers_before", 1))
    hit_cost = max(0, transfer_count - free_transfers_before) * 4

    if chip == "bench_boost":
        lineup_names = list(sorted(squad_names))
    else:
        lineup_names = _apply_autosubs(starters, bench_order, positions, actual_minutes)
    effective_captain = captain
    if float(actual_minutes.get(captain, 0.0)) <= 0.0 and vice_captain:
        effective_captain = vice_captain if float(actual_minutes.get(vice_captain, 0.0)) > 0.0 else captain
    total = sum(actual_points.get(player_name, 0.0) for player_name in lineup_names)
    total += actual_points.get(effective_captain, 0.0)
    if chip == "triple_captain":
        total += actual_points.get(effective_captain, 0.0)
    return round(total - hit_cost, 2)


def evaluate_llm_predictions(example_path: str, prediction_path: str) -> LLMEvaluationReport:
    examples = _load_jsonl(example_path)
    prediction_lookup = _prediction_lookup(_load_jsonl(prediction_path))
    week_results: List[LLMWeekPredictionResult] = []
    for example in examples:
        season = str(example["season"])
        week = int(example["week"])
        target = _assistant_target(example)
        metadata = dict(example.get("metadata", {}))
        record = prediction_lookup.get((season, week))
        parsed_prediction = None if record is None else _parse_response_json(
            record.get("response", record.get("assistant", record.get("prediction")))
        )
        target_starters = set(_normalized_names(target.get("starters")))
        predicted_starters = set(_normalized_names((parsed_prediction or {}).get("starters")))
        starter_union = target_starters | predicted_starters
        starters_jaccard = (
            len(target_starters & predicted_starters) / len(starter_union) if starter_union else 1.0
        )
        target_bench = _normalized_names(target.get("bench_order"))
        predicted_bench = _normalized_names((parsed_prediction or {}).get("bench_order"))
        bench_slot_matches = sum(
            1 for left, right in zip(target_bench, predicted_bench) if left == right
        )
        bench_slot_accuracy = bench_slot_matches / max(len(target_bench), 1)
        predicted_score = 0.0 if parsed_prediction is None else _score_prediction_bundle(metadata, parsed_prediction)
        target_score = float(metadata.get("team_actual_score", 0.0))
        week_results.append(
            LLMWeekPredictionResult(
                season=season,
                week=week,
                prediction_found=record is not None,
                valid_json=parsed_prediction is not None,
                captain_match=str((parsed_prediction or {}).get("captain", "")).strip() == str(target.get("captain", "")).strip(),
                vice_captain_match=str((parsed_prediction or {}).get("vice_captain", "")).strip()
                == str(target.get("vice_captain", "")).strip(),
                chip_match=str((parsed_prediction or {}).get("chip", "none") or "none")
                == str(target.get("chip", "none") or "none"),
                transfer_exact_match=_normalized_transfer_signature((parsed_prediction or {}).get("transfers"))
                == _normalized_transfer_signature(target.get("transfers")),
                starters_jaccard=round(starters_jaccard, 4),
                bench_slot_accuracy=round(bench_slot_accuracy, 4),
                predicted_policy_actual_score=predicted_score,
                target_policy_actual_score=target_score,
                score_gap_vs_target=round(predicted_score - target_score, 2),
            )
        )

    matched_predictions = sum(result.prediction_found for result in week_results)
    valid_json_predictions = sum(result.valid_json for result in week_results)
    total_examples = max(len(week_results), 1)

    def mean(values: Sequence[float]) -> float:
        return round(sum(values) / max(len(values), 1), 4)

    return LLMEvaluationReport(
        total_examples=len(week_results),
        matched_predictions=matched_predictions,
        valid_json_predictions=valid_json_predictions,
        captain_accuracy=mean([1.0 if result.captain_match else 0.0 for result in week_results]),
        vice_captain_accuracy=mean([1.0 if result.vice_captain_match else 0.0 for result in week_results]),
        chip_accuracy=mean([1.0 if result.chip_match else 0.0 for result in week_results]),
        transfer_exact_match_rate=mean([1.0 if result.transfer_exact_match else 0.0 for result in week_results]),
        starters_jaccard_mean=mean([result.starters_jaccard for result in week_results]),
        bench_slot_accuracy_mean=mean([result.bench_slot_accuracy for result in week_results]),
        average_predicted_policy_actual_score=mean([result.predicted_policy_actual_score for result in week_results]),
        average_target_policy_actual_score=mean([result.target_policy_actual_score for result in week_results]),
        average_score_gap_vs_target=mean([result.score_gap_vs_target for result in week_results]),
        weeks=week_results,
        notes=[
            "This evaluator scores strict JSON action bundles week by week.",
            "Actual-score reconstruction uses the prompt/example metadata, including actual points and minutes for current-squad and shortlist players.",
            "The score comparison is against the structured backtest policy stored in the training example metadata.",
        ],
    )


def report_to_markdown(report: LLMEvaluationReport) -> str:
    lines = [
        "# LLM Decision Evaluation",
        "",
        f"- Total eval examples: {report.total_examples}",
        f"- Matched predictions: {report.matched_predictions}",
        f"- Valid JSON predictions: {report.valid_json_predictions}",
        f"- Captain accuracy: {report.captain_accuracy:.4f}",
        f"- Vice-captain accuracy: {report.vice_captain_accuracy:.4f}",
        f"- Chip accuracy: {report.chip_accuracy:.4f}",
        f"- Transfer exact-match rate: {report.transfer_exact_match_rate:.4f}",
        f"- Starters Jaccard mean: {report.starters_jaccard_mean:.4f}",
        f"- Bench-slot accuracy mean: {report.bench_slot_accuracy_mean:.4f}",
        f"- Avg predicted-policy actual score: {report.average_predicted_policy_actual_score:.4f}",
        f"- Avg target-policy actual score: {report.average_target_policy_actual_score:.4f}",
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
            "| Week | Found | JSON | Captain | Vice | Chip | Transfers | Starters Jaccard | Bench Acc | Pred Score | Target Score | Gap |",
            "| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )
    for result in report.weeks:
        lines.append(
            f"| {result.season} GW{result.week} | {result.prediction_found} | {result.valid_json} | "
            f"{result.captain_match} | {result.vice_captain_match} | {result.chip_match} | "
            f"{result.transfer_exact_match} | {result.starters_jaccard:.4f} | {result.bench_slot_accuracy:.4f} | "
            f"{result.predicted_policy_actual_score:.2f} | {result.target_policy_actual_score:.2f} | "
            f"{result.score_gap_vs_target:.2f} |"
        )
    return "\n".join(lines)


def write_llm_evaluation_outputs(report: LLMEvaluationReport, output_dir: str) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    json_path = output_path / "llm_evaluation_report.json"
    markdown_path = output_path / "llm_evaluation_report.md"
    json_path.write_text(json.dumps(asdict(report), indent=2))
    markdown_path.write_text(report_to_markdown(report))
    return {"json": str(json_path), "markdown": str(markdown_path)}

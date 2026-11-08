#!/usr/bin/env python3
"""Build anchored listwise FPL value-ranking SFT examples.

The target is still realized future utility, but Gemma is trained to make a
bounded number of swaps from the classic ML top-five instead of freely reranking
the whole slate. This keeps the model focused on corrections.
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

from build_ranking_value_sft_split import (
    _actual_value,
    _baseline_value,
    _candidate_line,
    _counts,
    _load_jsonl,
    _parse_weeks,
    _sample_slate,
    _week_evidence_lines,
    _write_jsonl,
)


def _player_id(row: dict[str, Any]) -> int:
    return int(row["metadata"]["player_id"])


def _rank_by_baseline(slate: list[dict[str, Any]], rank_size: int) -> list[dict[str, Any]]:
    return sorted(slate, key=_baseline_value, reverse=True)[:rank_size]


def _rank_by_actual(slate: list[dict[str, Any]], rank_size: int) -> list[dict[str, Any]]:
    return sorted(
        slate,
        key=lambda row: (_actual_value(row), row["metadata"]["labels"].get("points_5gw", 0), _baseline_value(row)),
        reverse=True,
    )[:rank_size]


def _anchored_target(
    slate: list[dict[str, Any]],
    rank_size: int,
    max_swaps: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    selected = {_player_id(row): row for row in _rank_by_baseline(slate, rank_size)}
    outside = sorted(
        [row for row in slate if _player_id(row) not in selected],
        key=lambda row: (_actual_value(row), _baseline_value(row)),
        reverse=True,
    )
    swaps: list[dict[str, Any]] = []

    for incoming in outside:
        if len(swaps) >= max_swaps:
            break
        worst_selected = min(selected.values(), key=lambda row: (_actual_value(row), _baseline_value(row)))
        if _actual_value(incoming) <= _actual_value(worst_selected):
            continue

        outgoing_id = _player_id(worst_selected)
        incoming_id = _player_id(incoming)
        del selected[outgoing_id]
        selected[incoming_id] = incoming
        swaps.append(
            {
                "out_player_id": outgoing_id,
                "in_player_id": incoming_id,
                "actual_value_gain": round(_actual_value(incoming) - _actual_value(worst_selected), 4),
            }
        )

    ranked = sorted(selected.values(), key=lambda row: (_actual_value(row), _baseline_value(row)), reverse=True)
    return ranked[:rank_size], swaps


def _ids(rows: Iterable[dict[str, Any]]) -> list[int]:
    return [_player_id(row) for row in rows]


def _build_prompt(
    season: str,
    week: int,
    deadline_ts: str,
    slate: list[dict[str, Any]],
    evidence: str,
    rank_size: int,
    max_swaps: int,
) -> str:
    baseline_rows = _rank_by_baseline(slate, rank_size)
    baseline_ids = _ids(baseline_rows)
    candidate_lines = "\n".join(_candidate_line(row) for row in slate)
    user = f"""Choose a final FPL value top {rank_size} from this candidate slate using only the pre-deadline snapshot.

Training utility target:
utility = 0.20 * actual_1gw_points + 0.30 * actual_3gw_points + 0.50 * actual_5gw_points.

Anchoring rule:
- The classic ML top {rank_size} is the default answer: {baseline_ids}
- Make at most {max_swaps} swaps away from that baseline.
- Only swap when the pre-deadline snapshot suggests a materially better future utility.
- If uncertain, keep the ML baseline player.

Return exactly one JSON object, no prose/markdown/extra text, with:
- "baseline_ranked_player_ids": the provided baseline ids
- "final_ranked_player_ids": final top {rank_size} player ids from best to worst
- "swaps": objects with "out_player_id", "in_player_id", and short "reason"
- "value_scores": objects with "player_id" and numeric "score" for the final players

Example:
{{"baseline_ranked_player_ids":[101,202,303,404,505],"final_ranked_player_ids":[101,606,202,303,404],"swaps":[{{"out_player_id":505,"in_player_id":606,"reason":"stronger medium-horizon value and safer minutes"}}],"value_scores":[{{"player_id":101,"score":18.4}},{{"player_id":606,"score":16.2}},{{"player_id":202,"score":15.1}},{{"player_id":303,"score":14.0}},{{"player_id":404,"score":13.2}}]}}

Snapshot:
- Season: {season}
- Gameweek: {week}
- Deadline: {deadline_ts}

Timestamp-safe evidence:
{evidence}

Candidates:
{candidate_lines}
"""
    system = (
        "You are an FPL anchored value-ranking assistant. Return strict JSON only. "
        "Start from the classic ML baseline and make only high-confidence bounded swaps."
    )
    return f"<|turn>system\n{system}<|turn>\n<|turn>user\n{user}<|turn>\n<|turn>model\n"


def _build_completion(
    slate: list[dict[str, Any]],
    rank_size: int,
    max_swaps: int,
) -> str:
    baseline_rows = _rank_by_baseline(slate, rank_size)
    anchored_rows, swaps = _anchored_target(slate, rank_size, max_swaps)
    return json.dumps(
        {
            "baseline_ranked_player_ids": _ids(baseline_rows),
            "final_ranked_player_ids": _ids(anchored_rows),
            "swaps": [
                {
                    "out_player_id": swap["out_player_id"],
                    "in_player_id": swap["in_player_id"],
                    "reason": "stronger medium-horizon value with acceptable availability risk",
                }
                for swap in swaps
            ],
            "value_scores": [
                {
                    "player_id": _player_id(row),
                    "score": round(_actual_value(row), 2),
                }
                for row in anchored_rows
            ],
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def _slate_metadata(
    season: str,
    week: int,
    deadline_ts: str,
    slate: list[dict[str, Any]],
    rank_size: int,
    max_swaps: int,
) -> dict[str, Any]:
    candidates = []
    for row in slate:
        metadata = row["metadata"]
        candidates.append(
            {
                "player_id": int(metadata["player_id"]),
                "player_name": metadata["player_name"],
                "position": metadata["position"],
                "team_id": int(metadata["team_id"]),
                "baseline_value": round(_baseline_value(row), 4),
                "actual_value": round(_actual_value(row), 4),
                "baseline_forecast": metadata["baseline_forecast"],
                "labels": metadata["labels"],
            }
        )

    target_rows = _rank_by_actual(slate, rank_size)
    baseline_rows = _rank_by_baseline(slate, rank_size)
    anchored_rows, swaps = _anchored_target(slate, rank_size, max_swaps)
    return {
        "task": "fpl_anchored_value_ranking",
        "season": season,
        "week": week,
        "deadline_ts": deadline_ts,
        "utility_formula": "0.20*points_1gw + 0.30*points_3gw + 0.50*points_5gw",
        "max_swaps": max_swaps,
        "candidates": candidates,
        "target_ranked_player_ids": _ids(target_rows),
        "baseline_ranked_player_ids": _ids(baseline_rows),
        "anchored_target_ranked_player_ids": _ids(anchored_rows),
        "anchored_target_swaps": swaps,
    }


def _build_examples(
    rows: list[dict[str, Any]],
    weeks: set[int],
    slates_per_week: int,
    slate_size: int,
    rank_size: int,
    candidate_pool_size: int,
    evidence_docs: int,
    evidence_chars: int,
    max_swaps: int,
    seed: int,
) -> list[dict[str, Any]]:
    by_week: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        week = int(row["week"])
        if week in weeks:
            by_week[(str(row["season"]), week)].append(row)

    examples: list[dict[str, Any]] = []
    rng = random.Random(seed)
    for season, week in sorted(by_week, key=lambda item: (item[0], item[1])):
        week_rows = sorted(by_week[(season, week)], key=_baseline_value, reverse=True)
        if len(week_rows) < rank_size:
            continue
        pool = week_rows[:candidate_pool_size] if candidate_pool_size > 0 else week_rows
        deadline_ts = str(week_rows[0]["deadline_ts"])
        evidence = _week_evidence_lines(week_rows, max_docs=evidence_docs, max_chars=evidence_chars)

        deterministic_slates: list[list[dict[str, Any]]] = []
        for start in range(0, min(len(pool), slate_size * 4), slate_size):
            chunk = pool[start : start + slate_size]
            if len(chunk) >= rank_size:
                deterministic_slates.append(chunk)

        week_slates = deterministic_slates[:slates_per_week]
        while len(week_slates) < slates_per_week:
            week_slates.append(_sample_slate(pool, slate_size, rng))

        for slate_index, slate in enumerate(week_slates):
            prompt = _build_prompt(season, week, deadline_ts, slate, evidence, rank_size, max_swaps)
            completion = _build_completion(slate, rank_size, max_swaps)
            examples.append(
                {
                    "season": season,
                    "week": week,
                    "deadline_ts": deadline_ts,
                    "prompt": prompt,
                    "completion": completion,
                    "metadata": {
                        **_slate_metadata(season, week, deadline_ts, slate, rank_size, max_swaps),
                        "slate_index": slate_index,
                        "slate_size": len(slate),
                    },
                }
            )

    return examples


def _swap_counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    return {
        str(k): v
        for k, v in sorted(
            Counter(len(row["metadata"].get("anchored_target_swaps") or []) for row in rows).items()
        )
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--train-weeks", default="1-25")
    parser.add_argument("--eval-weeks", default="26")
    parser.add_argument("--train-slates-per-week", type=int, default=640)
    parser.add_argument("--eval-slates-per-week", type=int, default=128)
    parser.add_argument("--slate-size", type=int, default=12)
    parser.add_argument("--rank-size", type=int, default=5)
    parser.add_argument("--candidate-pool-size", type=int, default=128)
    parser.add_argument("--evidence-docs", type=int, default=3)
    parser.add_argument("--evidence-chars", type=int, default=320)
    parser.add_argument("--max-swaps", type=int, default=2)
    parser.add_argument("--seed", type=int, default=20260612)
    args = parser.parse_args()

    if args.max_swaps < 0 or args.max_swaps > args.rank_size:
        raise ValueError("--max-swaps must be between 0 and --rank-size")

    all_rows = _load_jsonl(args.source_dir / "train.jsonl") + _load_jsonl(args.source_dir / "eval.jsonl")
    train_weeks = _parse_weeks(args.train_weeks)
    eval_weeks = _parse_weeks(args.eval_weeks)
    if train_weeks & eval_weeks:
        raise ValueError(f"Train/eval weeks overlap: {sorted(train_weeks & eval_weeks)}")

    train_rows = _build_examples(
        all_rows,
        weeks=train_weeks,
        slates_per_week=args.train_slates_per_week,
        slate_size=args.slate_size,
        rank_size=args.rank_size,
        candidate_pool_size=args.candidate_pool_size,
        evidence_docs=args.evidence_docs,
        evidence_chars=args.evidence_chars,
        max_swaps=args.max_swaps,
        seed=args.seed,
    )
    eval_rows = _build_examples(
        all_rows,
        weeks=eval_weeks,
        slates_per_week=args.eval_slates_per_week,
        slate_size=args.slate_size,
        rank_size=args.rank_size,
        candidate_pool_size=args.candidate_pool_size,
        evidence_docs=args.evidence_docs,
        evidence_chars=args.evidence_chars,
        max_swaps=args.max_swaps,
        seed=args.seed + 1,
    )
    if not train_rows or not eval_rows:
        raise ValueError("No rows selected")

    train_count = _write_jsonl(args.output_dir / "train.jsonl", train_rows)
    eval_count = _write_jsonl(args.output_dir / "eval.jsonl", eval_rows)
    summary = {
        "source_dir": str(args.source_dir),
        "output_dir": str(args.output_dir),
        "task": "fpl_anchored_value_ranking_listwise",
        "utility_formula": "0.20*points_1gw + 0.30*points_3gw + 0.50*points_5gw",
        "candidate_pool_size": args.candidate_pool_size,
        "slate_size": args.slate_size,
        "rank_size": args.rank_size,
        "max_swaps": args.max_swaps,
        "train_weeks": sorted(train_weeks),
        "eval_weeks": sorted(eval_weeks),
        "train_slates_per_week": args.train_slates_per_week,
        "eval_slates_per_week": args.eval_slates_per_week,
        "train_count": train_count,
        "eval_count": eval_count,
        "train_counts_by_week": _counts(train_rows),
        "eval_counts_by_week": _counts(eval_rows),
        "train_swap_counts": _swap_counts(train_rows),
        "eval_swap_counts": _swap_counts(eval_rows),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

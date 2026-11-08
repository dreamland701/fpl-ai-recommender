#!/usr/bin/env python3
"""Build snapshot-safe listwise FPL value-ranking SFT examples."""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def _write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")
            count += 1
    return count


def _parse_weeks(raw: str) -> set[int]:
    weeks: set[int] = set()
    for part in raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            weeks.update(range(int(start), int(end) + 1))
        else:
            weeks.add(int(part))
    return weeks


def _float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def _baseline_value(row: dict[str, Any]) -> float:
    baseline = row.get("metadata", {}).get("baseline_forecast", {})
    return (
        0.20 * _float(baseline.get("baseline_points_1gw"))
        + 0.30 * _float(baseline.get("baseline_points_3gw"))
        + 0.50 * _float(baseline.get("baseline_points_5gw"))
    )


def _actual_value(row: dict[str, Any]) -> float:
    labels = row.get("metadata", {}).get("labels", {})
    return (
        0.20 * _float(labels.get("points_1gw"))
        + 0.30 * _float(labels.get("points_3gw"))
        + 0.50 * _float(labels.get("points_5gw"))
    )


def _looks_like_outcome_leakage_evidence(doc: dict[str, Any]) -> bool:
    title = " ".join(str(doc.get("title") or "").lower().split())
    snippet = " ".join(str(doc.get("snippet") or "").lower().split())
    content = " ".join(str(doc.get("content") or "").lower().split())
    combined = " ".join(part for part in [title, snippet, content[:500]] if part)

    defensive_recap_titles = (
        "who's got fpl defensive contribution points in gameweek",
        "who has got fpl defensive contribution points in gameweek",
        "who got fpl defensive contribution points in gameweek",
    )
    if any(pattern in title for pattern in defensive_recap_titles):
        return True

    outcome_fragments = (
        "players who have received extra points",
        "picked up two extra fpl points so far in this gameweek",
        "defensive contributions are subject to change up until one hour after the final whistle",
    )
    return any(fragment in combined for fragment in outcome_fragments)


def _week_evidence_lines(rows: list[dict[str, Any]], max_docs: int, max_chars: int) -> str:
    seen: set[tuple[str, str]] = set()
    docs: list[dict[str, Any]] = []
    for row in rows:
        for doc in row.get("metadata", {}).get("evidence_documents") or []:
            if not isinstance(doc, dict) or _looks_like_outcome_leakage_evidence(doc):
                continue
            key = (str(doc.get("url") or ""), str(doc.get("title") or ""))
            if key in seen:
                continue
            seen.add(key)
            docs.append(doc)
            if len(docs) >= max_docs:
                break
        if len(docs) >= max_docs:
            break

    if not docs:
        return "No timestamp-safe text evidence available."

    lines: list[str] = []
    for index, doc in enumerate(docs, start=1):
        content = " ".join(str(doc.get("content") or doc.get("snippet") or "").split())
        if len(content) > max_chars:
            content = content[:max_chars].rsplit(" ", 1)[0] + " ..."
        lines.append(
            "\n".join(
                [
                    f"[{index}] {doc.get('source_name') or 'unknown'} | {doc.get('published_at') or 'unknown time'}",
                    f"Title: {doc.get('title') or ''}",
                    f"Text: {content}",
                ]
            )
        )
    return "\n\n".join(lines)


def _candidate_line(row: dict[str, Any]) -> str:
    metadata = row["metadata"]
    baseline = metadata["baseline_forecast"]
    status = metadata.get("status_pre_deadline") or "none"
    news = " ".join(str(metadata.get("news_pre_deadline") or "none").split())
    if len(news) > 90:
        news = news[:90].rsplit(" ", 1)[0] + " ..."
    return (
        f"- id={metadata['player_id']} | {metadata['player_name']} | pos={metadata['position']} | "
        f"team={metadata['team_id']} | status={status} | news={news} | "
        f"ml_1gw={_float(baseline.get('baseline_points_1gw')):.2f} | "
        f"ml_3gw={_float(baseline.get('baseline_points_3gw')):.2f} | "
        f"ml_5gw={_float(baseline.get('baseline_points_5gw')):.2f} | "
        f"ml_min={_float(baseline.get('baseline_minutes_1gw')):.1f} | "
        f"ml_app={_float(baseline.get('baseline_appearance_probability')):.2f} | "
        f"ml_unc={_float(baseline.get('baseline_uncertainty')):.2f}"
    )


def _build_prompt(season: str, week: int, deadline_ts: str, slate: list[dict[str, Any]], evidence: str) -> str:
    candidate_lines = "\n".join(_candidate_line(row) for row in slate)
    user = f"""Rank this FPL candidate slate by realized future FPL utility using only the pre-deadline snapshot.

Training utility target:
utility = 0.20 * actual_1gw_points + 0.30 * actual_3gw_points + 0.50 * actual_5gw_points.
This is a value function for transfer/lineup planning, so prefer players with strong medium-horizon upside while keeping near-term points relevant.

Return exactly one JSON object, no prose/markdown/extra text, with:
- "ranked_player_ids": top 5 player ids from best to worst
- "value_scores": objects with "player_id" and numeric "score" for the same players

Example:
{{"ranked_player_ids":[101,202,303,404,505],"value_scores":[{{"player_id":101,"score":18.4}},{{"player_id":202,"score":15.1}},{{"player_id":303,"score":14.0}},{{"player_id":404,"score":13.2}},{{"player_id":505,"score":12.8}}]}}

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
        "You are an FPL value-ranking assistant. Return strict JSON only. "
        "Use the ML baseline, availability fields, player context, and timestamp-safe evidence to rank candidates."
    )
    return f"<|turn>system\n{system}<|turn>\n<|turn>user\n{user}<|turn>\n<|turn>model\n"


def _build_completion(slate: list[dict[str, Any]], rank_size: int) -> str:
    ranked = sorted(
        slate,
        key=lambda row: (_actual_value(row), _float(row["metadata"]["labels"].get("points_5gw")), _baseline_value(row)),
        reverse=True,
    )[:rank_size]
    return json.dumps(
        {
            "ranked_player_ids": [int(row["metadata"]["player_id"]) for row in ranked],
            "value_scores": [
                {
                    "player_id": int(row["metadata"]["player_id"]),
                    "score": round(_actual_value(row), 2),
                }
                for row in ranked
            ],
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )


def _slate_metadata(season: str, week: int, deadline_ts: str, slate: list[dict[str, Any]], rank_size: int) -> dict[str, Any]:
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
    target_rows = sorted(candidates, key=lambda row: row["actual_value"], reverse=True)[:rank_size]
    return {
        "task": "fpl_value_ranking",
        "season": season,
        "week": week,
        "deadline_ts": deadline_ts,
        "utility_formula": "0.20*points_1gw + 0.30*points_3gw + 0.50*points_5gw",
        "candidates": candidates,
        "target_ranked_player_ids": [row["player_id"] for row in target_rows],
        "baseline_ranked_player_ids": [
            row["player_id"] for row in sorted(candidates, key=lambda row: row["baseline_value"], reverse=True)[:rank_size]
        ],
    }


def _sample_slate(pool: list[dict[str, Any]], slate_size: int, rng: random.Random) -> list[dict[str, Any]]:
    if len(pool) <= slate_size:
        return sorted(pool, key=_baseline_value, reverse=True)

    top = pool[: min(24, len(pool))]
    mid = pool[min(24, len(pool)) : min(72, len(pool))]
    rest = pool[min(72, len(pool)) :]
    chosen: dict[int, dict[str, Any]] = {}

    for bucket, count in [(top, 4), (mid, 4), (rest or mid or top, slate_size)]:
        if not bucket:
            continue
        for row in rng.sample(bucket, min(count, len(bucket))):
            chosen[int(row["metadata"]["player_id"])] = row
            if len(chosen) >= slate_size:
                break
        if len(chosen) >= slate_size:
            break

    while len(chosen) < slate_size:
        row = rng.choice(pool)
        chosen[int(row["metadata"]["player_id"])] = row

    return sorted(chosen.values(), key=_baseline_value, reverse=True)[:slate_size]


def _build_examples(
    rows: list[dict[str, Any]],
    weeks: set[int],
    slates_per_week: int,
    slate_size: int,
    rank_size: int,
    candidate_pool_size: int,
    evidence_docs: int,
    evidence_chars: int,
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
            prompt = _build_prompt(season, week, deadline_ts, slate, evidence)
            completion = _build_completion(slate, rank_size)
            examples.append(
                {
                    "season": season,
                    "week": week,
                    "deadline_ts": deadline_ts,
                    "prompt": prompt,
                    "completion": completion,
                    "metadata": {
                        **_slate_metadata(season, week, deadline_ts, slate, rank_size),
                        "slate_index": slate_index,
                        "slate_size": len(slate),
                    },
                }
            )

    return examples


def _counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    return {str(k): v for k, v in sorted(Counter(int(row["week"]) for row in rows).items())}


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
    parser.add_argument("--seed", type=int, default=20260604)
    args = parser.parse_args()

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
        seed=args.seed + 1,
    )
    if not train_rows or not eval_rows:
        raise ValueError("No rows selected")

    train_count = _write_jsonl(args.output_dir / "train.jsonl", train_rows)
    eval_count = _write_jsonl(args.output_dir / "eval.jsonl", eval_rows)
    summary = {
        "source_dir": str(args.source_dir),
        "output_dir": str(args.output_dir),
        "task": "fpl_value_ranking_listwise",
        "utility_formula": "0.20*points_1gw + 0.30*points_3gw + 0.50*points_5gw",
        "candidate_pool_size": args.candidate_pool_size,
        "slate_size": args.slate_size,
        "rank_size": args.rank_size,
        "train_weeks": sorted(train_weeks),
        "eval_weeks": sorted(eval_weeks),
        "train_slates_per_week": args.train_slates_per_week,
        "eval_slates_per_week": args.eval_slates_per_week,
        "train_count": train_count,
        "eval_count": eval_count,
        "train_counts_by_week": _counts(train_rows),
        "eval_counts_by_week": _counts(eval_rows),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

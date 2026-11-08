#!/usr/bin/env python3
"""Build residual/delta player forecast SFT examples from absolute forecast rows."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


BASELINE_TO_LABEL = {
    "delta_points_1gw": ("baseline_points_1gw", "points_1gw"),
    "delta_points_3gw": ("baseline_points_3gw", "points_3gw"),
    "delta_points_5gw": ("baseline_points_5gw", "points_5gw"),
    "delta_minutes_1gw": ("baseline_minutes_1gw", "minutes_1gw"),
    "delta_appearance_probability": ("baseline_appearance_probability", "appearance_probability"),
}


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
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
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


def _baseline_score(row: dict[str, Any]) -> float:
    baseline = row.get("metadata", {}).get("baseline_forecast", {})
    points_5 = float(baseline.get("baseline_points_5gw") or 0.0)
    points_3 = float(baseline.get("baseline_points_3gw") or 0.0)
    points_1 = float(baseline.get("baseline_points_1gw") or 0.0)
    minutes_1 = float(baseline.get("baseline_minutes_1gw") or 0.0)
    appearance = float(baseline.get("baseline_appearance_probability") or 0.0)
    return points_5 + 0.75 * points_3 + 1.5 * points_1 + 0.02 * minutes_1 + 2.0 * appearance


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


def _clean_evidence_documents(metadata: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        doc
        for doc in metadata.get("evidence_documents") or []
        if isinstance(doc, dict) and not _looks_like_outcome_leakage_evidence(doc)
    ]


def _select_top_by_week(rows: list[dict[str, Any]], weeks: set[int], top_n: int) -> list[dict[str, Any]]:
    by_week: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        week = int(row["week"])
        if week in weeks:
            by_week[week].append(row)

    selected: list[dict[str, Any]] = []
    for week in sorted(by_week):
        ranked = sorted(by_week[week], key=_baseline_score, reverse=True)
        selected.extend(ranked[:top_n] if top_n > 0 else ranked)
    return selected


def _evidence_lines(metadata: dict[str, Any], max_docs: int = 2, max_chars: int = 260) -> str:
    docs = _clean_evidence_documents(metadata)
    lines: list[str] = []
    for index, doc in enumerate(docs[:max_docs], start=1):
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
    return "\n\n".join(lines) if lines else "No timestamp-safe text evidence available."


def _build_user_prompt(metadata: dict[str, Any]) -> str:
    baseline = metadata["baseline_forecast"]
    body = f"""Player context:
- Season: {metadata.get('season')}
- Gameweek: {metadata.get('week')}
- Deadline: {metadata.get('deadline_ts')}
- Player: {metadata.get('player_name')}
- Player ID: {metadata.get('player_id')}
- Team ID: {metadata.get('team_id')}
- Position: {metadata.get('position')}
- Status pre-deadline: {metadata.get('status_pre_deadline') or 'none'}
- Official player news pre-deadline: {metadata.get('news_pre_deadline') or 'none'}

Classic ML baseline forecast:
{json.dumps(baseline, indent=2)}

Timestamp-safe text evidence:
{_evidence_lines(metadata)}
"""
    return (
        "Adjust the classic ML FPL forecast using only pre-deadline evidence. Output residual deltas to add to the "
        "baseline. Use near-zero deltas unless evidence gives a clear reason.\n\n"
        "Return exactly one JSON object, no prose/markdown/extra text, with numeric fields:\n"
        "- \"delta_points_1gw\"\n"
        "- \"delta_points_3gw\"\n"
        "- \"delta_points_5gw\"\n"
        "- \"delta_minutes_1gw\"\n"
        "- \"delta_appearance_probability\"\n\n"
        "Example:\n"
        "{\"delta_points_1gw\": -0.5, \"delta_points_3gw\": 1.2, \"delta_points_5gw\": 2.0, "
        "\"delta_minutes_1gw\": -8.0, \"delta_appearance_probability\": -0.1}\n\n"
        + body
    )


def _to_residual_row(row: dict[str, Any]) -> dict[str, Any]:
    metadata = row["metadata"]
    metadata = dict(metadata)
    metadata["evidence_documents"] = _clean_evidence_documents(metadata)
    baseline = metadata["baseline_forecast"]
    labels = metadata["labels"]
    deltas: dict[str, float] = {}
    final_forecast: dict[str, float] = {}
    for delta_key, (baseline_key, label_key) in BASELINE_TO_LABEL.items():
        base_value = float(baseline.get(baseline_key) or 0.0)
        label_value = float(labels.get(label_key) or 0.0)
        delta = round(label_value - base_value, 4)
        deltas[delta_key] = delta
        final_forecast[label_key] = label_value

    messages = row["messages"]
    system = {
        "role": "system",
        "content": (
            "You are an FPL forecast adjustment assistant. Return strict JSON residual deltas only. "
            "Do not include hidden reasoning or extra text."
        ),
    }
    prompt_messages = [system, {"role": "user", "content": _build_user_prompt(metadata)}]
    prompt = "".join(
        f"<|turn>{message['role']}\n{message['content']}<|turn>\n" for message in prompt_messages
    ) + "<|turn>model\n"
    completion = json.dumps(deltas, ensure_ascii=False, separators=(",", ":"))

    residual_metadata = dict(metadata)
    residual_metadata["residual_labels"] = deltas
    residual_metadata["residual_target_final_forecast"] = final_forecast
    return {
        "season": row["season"],
        "week": row["week"],
        "deadline_ts": row["deadline_ts"],
        "prompt": prompt,
        "completion": completion,
        "metadata": residual_metadata,
    }


def _counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    return {str(k): v for k, v in sorted(Counter(int(row["week"]) for row in rows).items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--train-weeks", default="1-10")
    parser.add_argument("--eval-weeks", default="11")
    parser.add_argument("--top-n", type=int, default=128, help="Use <=0 for all players in selected weeks.")
    args = parser.parse_args()

    all_rows = _load_jsonl(args.source_dir / "train.jsonl") + _load_jsonl(args.source_dir / "eval.jsonl")
    train_weeks = _parse_weeks(args.train_weeks)
    eval_weeks = _parse_weeks(args.eval_weeks)
    if train_weeks & eval_weeks:
        raise ValueError(f"Train/eval weeks overlap: {sorted(train_weeks & eval_weeks)}")

    train_rows = [_to_residual_row(row) for row in _select_top_by_week(all_rows, train_weeks, args.top_n)]
    eval_rows = [_to_residual_row(row) for row in _select_top_by_week(all_rows, eval_weeks, args.top_n)]
    if not train_rows or not eval_rows:
        raise ValueError("No rows selected")

    train_count = _write_jsonl(args.output_dir / "train.jsonl", train_rows)
    eval_count = _write_jsonl(args.output_dir / "eval.jsonl", eval_rows)

    summary = {
        "source_dir": str(args.source_dir),
        "output_dir": str(args.output_dir),
        "task": "player_forecast_residual_delta",
        "selection": "top_n_by_pre_deadline_baseline_forecast",
        "top_n": args.top_n,
        "train_weeks": sorted(train_weeks),
        "eval_weeks": sorted(eval_weeks),
        "train_count": train_count,
        "eval_count": eval_count,
        "train_counts_by_week": _counts(train_rows),
        "eval_counts_by_week": _counts(eval_rows),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

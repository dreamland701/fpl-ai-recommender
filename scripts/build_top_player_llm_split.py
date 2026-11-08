#!/usr/bin/env python3
"""Build a compact, time-forward LLM SFT split from player forecast examples."""

from __future__ import annotations

import argparse
import json
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

    # Use only pre-deadline model outputs. Labels/actuals are intentionally not used.
    return points_5 + 0.75 * points_3 + 1.5 * points_1 + 0.02 * minutes_1 + 2.0 * appearance


def _select_top_by_week(rows: list[dict[str, Any]], weeks: set[int], top_n: int) -> list[dict[str, Any]]:
    by_week: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        week = int(row["week"])
        if week in weeks:
            by_week[week].append(row)

    selected: list[dict[str, Any]] = []
    for week in sorted(by_week):
        ranked = sorted(by_week[week], key=_baseline_score, reverse=True)
        selected.extend(ranked[:top_n])
    return selected


def _counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    return {str(k): v for k, v in sorted(Counter(int(row["week"]) for row in rows).items())}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--train-weeks", default="1-10")
    parser.add_argument("--eval-weeks", default="11")
    parser.add_argument("--top-n", type=int, default=128)
    args = parser.parse_args()

    all_rows = _load_jsonl(args.source_dir / "train.jsonl") + _load_jsonl(args.source_dir / "eval.jsonl")
    train_weeks = _parse_weeks(args.train_weeks)
    eval_weeks = _parse_weeks(args.eval_weeks)

    overlap = train_weeks & eval_weeks
    if overlap:
        raise ValueError(f"Train/eval weeks overlap: {sorted(overlap)}")

    train_rows = _select_top_by_week(all_rows, train_weeks, args.top_n)
    eval_rows = _select_top_by_week(all_rows, eval_weeks, args.top_n)

    if not train_rows:
        raise ValueError("No train rows selected")
    if not eval_rows:
        raise ValueError("No eval rows selected")

    train_count = _write_jsonl(args.output_dir / "train.jsonl", train_rows)
    eval_count = _write_jsonl(args.output_dir / "eval.jsonl", eval_rows)

    summary = {
        "source_dir": str(args.source_dir),
        "output_dir": str(args.output_dir),
        "selection": "top_n_by_pre_deadline_baseline_forecast",
        "top_n": args.top_n,
        "train_weeks": sorted(train_weeks),
        "eval_weeks": sorted(eval_weeks),
        "train_count": train_count,
        "eval_count": eval_count,
        "train_counts_by_week": _counts(train_rows),
        "eval_counts_by_week": _counts(eval_rows),
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

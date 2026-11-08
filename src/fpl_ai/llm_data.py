"""Timestamp-safe evidence handling and LLM training-data exports."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence
from urllib.parse import urljoin, urlparse

import pandas as pd

from .backtest import run_rolling_squad_backtest
from .config import DEFAULT_CURATED_SOURCES, parse_season_start_year
from .dataset import CanonicalDataset, training_rows_asof
from .decision import _optimize_lineup
from .hybrid import build_hybrid_decision_prompt
from .llm_eval import _score_prediction_bundle
from .models import fit_model_suite_from_frame
from .types import PlayerForecast, SquadPlayer


PLAYER_FORECAST_PROMPT_FIELDS = (
    "price_pre_deadline",
    "selected_by_percent_pre_deadline",
    "fixture_count",
    "home_fixture_count",
    "away_fixture_count",
    "fixture_difficulty_mean",
    "fixture_difficulty_min",
    "primary_opponent_team_id",
    "blank_gw",
    "double_gw",
    "price_change_1",
    "selected_change_1",
    "transfer_balance_prev_event",
    "points_avg_1",
    "minutes_avg_1",
    "appearance_rate_1",
    "played_60_rate_1",
    "points_avg_3",
    "minutes_avg_3",
    "appearance_rate_3",
    "played_60_rate_3",
    "points_avg_5",
    "minutes_avg_5",
    "appearance_rate_5",
    "played_60_rate_5",
    "bonus_avg_3",
    "bps_avg_3",
    "influence_avg_3",
    "creativity_avg_3",
    "threat_avg_3",
    "ict_index_avg_3",
    "starts_avg_3",
    "expected_goals_avg_3",
    "expected_assists_avg_3",
    "expected_goal_involvements_avg_3",
    "expected_goals_conceded_avg_3",
    "defensive_contribution_avg_3",
    "bonus_avg_5",
    "bps_avg_5",
    "influence_avg_5",
    "creativity_avg_5",
    "threat_avg_5",
    "ict_index_avg_5",
    "starts_avg_5",
    "expected_goals_avg_5",
    "expected_assists_avg_5",
    "expected_goal_involvements_avg_5",
    "expected_goals_conceded_avg_5",
    "defensive_contribution_avg_5",
    "team_goals_for_avg_3",
    "team_goals_against_avg_3",
    "team_goals_for_avg_5",
    "team_goals_against_avg_5",
    "opponent_goals_for_avg_3",
    "opponent_goals_against_avg_3",
    "opponent_goals_for_avg_5",
    "opponent_goals_against_avg_5",
    "expected_data_source_available",
    "defensive_data_source_available",
    "status_flag_pre_deadline",
    "news_flag_pre_deadline",
)


@dataclass(frozen=True)
class EvidenceRecord:
    title: str
    url: str
    source_name: str
    category: str
    published_at: str
    snippet: str
    content: str
    player_name: str = ""
    team_name: str = ""


@dataclass(frozen=True)
class LLMTrainingExample:
    season: str
    week: int
    deadline_ts: str
    messages: Sequence[Dict[str, str]]
    metadata: Dict[str, object]


def _snapshot_to_forecast(snapshot: Mapping[str, object], season: str, week: int) -> PlayerForecast:
    return PlayerForecast(
        season=season,
        week=week,
        player_id=int(snapshot["player_id"]),
        player_name=str(snapshot["player_name"]),
        team_id=int(snapshot["team_id"]),
        position=str(snapshot["position"]),
        price=float(snapshot["price"]),
        predicted_minutes=float(snapshot["predicted_minutes"]),
        predicted_points_1gw=float(snapshot["predicted_points_1gw"]),
        predicted_points_3gw=float(snapshot["predicted_points_3gw"]),
        predicted_points_5gw=float(snapshot["predicted_points_5gw"]),
        appearance_probability=float(snapshot["appearance_probability"]),
        fixture_count=1,
        uncertainty=0.0,
    )


def _snapshot_to_squad_player(snapshot: Mapping[str, object]) -> SquadPlayer:
    return SquadPlayer(
        player_id=int(snapshot["player_id"]),
        player_name=str(snapshot["player_name"]),
        team_id=int(snapshot["team_id"]),
        position=str(snapshot["position"]),
        sell_price=float(snapshot["price"]),
    )


def _parse_timestamp(value: str) -> Optional[datetime]:
    if not value:
        return None
    normalized = str(value).replace("Z", "+00:00")
    try:
        timestamp = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            timestamp = parsedate_to_datetime(str(value))
        except (TypeError, ValueError, IndexError):
            return None
    if timestamp.tzinfo is None:
        return timestamp.replace(tzinfo=timezone.utc)
    return timestamp.astimezone(timezone.utc)


def _normalize_text(value: object) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _clean_optional_text(value: object) -> str:
    text = _normalize_text(value)
    return "" if text.lower() in {"nan", "none", "null"} else text


def _domain(url: str) -> str:
    return urlparse(url).netloc.lower()


def _is_curated_url(url: str) -> bool:
    document_domain = _domain(url)
    for source in DEFAULT_CURATED_SOURCES:
        source_domain = _domain(source.url)
        if source_domain in document_domain or document_domain in source_domain:
            return True
    return False


def _category_priority(category: str) -> int:
    priority = {
        "official_club": 0,
        "official_fpl": 1,
        "official_premier_league": 2,
        "official_scout": 3,
        "trusted_news": 4,
        "reddit": 5,
    }
    return priority.get(str(category), 9)


def _looks_like_outcome_leakage_evidence(record: Mapping[str, object]) -> bool:
    """Reject articles whose timestamps are known to be unreliable for pre-deadline use."""
    title = _normalize_text(record.get("title", "")).lower()
    content = _normalize_text(record.get("content", "")).lower()
    snippet = _normalize_text(record.get("snippet", "")).lower()
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


def _records_from_evidence_path(path: Path) -> List[Dict[str, object]]:
    if path.suffix.lower() == ".jsonl":
        # Split on newlines only: splitlines() also breaks on U+2028/U+2029,
        # which appear unescaped inside article text written with ensure_ascii=False.
        return [json.loads(line) for line in path.read_text().split("\n") if line.strip()]
    if path.suffix.lower() == ".json":
        payload = json.loads(path.read_text())
        if isinstance(payload, list):
            return payload
        if isinstance(payload, dict):
            return list(payload.get("documents", []))
        raise ValueError(f"Unsupported JSON payload in {path}")
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path).to_dict(orient="records")
    raise ValueError(f"Unsupported evidence format: {path.suffix}")


def normalize_evidence_records(records: Sequence[Mapping[str, object]], curated_only: bool = True) -> pd.DataFrame:
    frame = pd.DataFrame(list(records))

    rename_map = {
        "text": "content",
        "body": "content",
        "description": "snippet",
        "source": "source_name",
        "published": "published_at",
        "published_time": "published_at",
        "created_at": "published_at",
        "selftext": "content",
        "permalink": "url",
    }
    frame = frame.rename(columns={key: value for key, value in rename_map.items() if key in frame.columns})
    if "published_at" not in frame.columns and "created_utc" in frame.columns:
        frame["published_at"] = frame["created_utc"].map(
            lambda value: datetime.fromtimestamp(float(value), tz=timezone.utc).isoformat()
            if pd.notna(value) and str(value).strip()
            else ""
        )
    elif "published_at" in frame.columns and "created_utc" in frame.columns:
        missing_published = frame["published_at"].isna() | (frame["published_at"].astype(str).str.strip() == "")
        frame.loc[missing_published, "published_at"] = frame.loc[missing_published, "created_utc"].map(
            lambda value: datetime.fromtimestamp(float(value), tz=timezone.utc).isoformat()
            if pd.notna(value) and str(value).strip()
            else ""
        )
    required_defaults = {
        "title": "",
        "url": "",
        "source_name": "",
        "category": "",
        "published_at": "",
        "snippet": "",
        "content": "",
        "timestamp_quality": "",
    }
    for column, default in required_defaults.items():
        if column not in frame.columns:
            frame[column] = default
        else:
            frame[column] = frame[column].fillna(default)

    if "subreddit" in frame.columns:
        subreddit = frame["subreddit"].map(_normalize_text)
        missing_source = frame["source_name"].map(_normalize_text) == ""
        frame.loc[missing_source & (subreddit != ""), "source_name"] = "r/" + subreddit
        missing_category = frame["category"].map(_normalize_text) == ""
        frame.loc[missing_category & (subreddit != ""), "category"] = "reddit"
    reddit_url = frame["url"].map(_normalize_text).str.startswith("/r/")
    frame.loc[reddit_url, "url"] = frame.loc[reddit_url, "url"].map(lambda value: urljoin("https://www.reddit.com", value))

    for column in required_defaults:
        frame[column] = frame[column].map(_normalize_text)
    frame["is_curated"] = frame["url"].map(_is_curated_url)
    frame["published_ts"] = frame["published_at"].map(_parse_timestamp)
    frame = frame.loc[frame["published_ts"].notna()].copy()
    frame = frame.loc[~frame.apply(_looks_like_outcome_leakage_evidence, axis=1)].copy()
    if curated_only:
        frame = frame.loc[frame["is_curated"]].copy()
    frame = frame.drop_duplicates(subset=["url", "published_at", "title"]).sort_values(
        ["published_ts", "source_name", "title"],
        ascending=[False, True, True],
    )
    return frame.reset_index(drop=True)


def normalize_evidence_corpus(input_path: str, curated_only: bool = True) -> pd.DataFrame:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(path)

    records: List[Dict[str, object]] = []
    if path.is_dir():
        supported = {".jsonl", ".json", ".csv"}
        for child in sorted(candidate for candidate in path.rglob("*") if candidate.is_file() and candidate.suffix.lower() in supported):
            records.extend(_records_from_evidence_path(child))
    else:
        records.extend(_records_from_evidence_path(path))
    return normalize_evidence_records(records, curated_only=curated_only)


def write_normalized_evidence(frame: pd.DataFrame, output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    records = frame.copy()
    records["published_ts"] = records["published_ts"].astype(str)
    with path.open("w") as handle:
        for record in records.to_dict(orient="records"):
            handle.write(json.dumps(record) + "\n")


def select_evidence_for_deadline(
    evidence_frame: pd.DataFrame,
    deadline_ts: str,
    max_documents: int = 6,
    lookback_days: int = 14,
) -> List[EvidenceRecord]:
    if evidence_frame.empty or not deadline_ts:
        return []
    deadline = _parse_timestamp(deadline_ts)
    if deadline is None:
        return []
    earliest = deadline - timedelta(days=lookback_days)
    eligible = evidence_frame.loc[
        evidence_frame["published_ts"].map(lambda value: value is not None and earliest <= value <= deadline)
    ].copy()
    if eligible.empty:
        return []
    eligible["category_priority"] = eligible["category"].map(_category_priority)
    eligible["hours_before_deadline"] = eligible["published_ts"].map(
        lambda value: abs((deadline - value).total_seconds()) / 3600.0
    )
    eligible = eligible.sort_values(
        ["category_priority", "hours_before_deadline", "source_name", "title"],
        ascending=[True, True, True, True],
    ).head(max_documents)
    return [
        EvidenceRecord(
            title=_normalize_text(record["title"]),
            url=_normalize_text(record["url"]),
            source_name=_normalize_text(record["source_name"]),
            category=_normalize_text(record["category"]),
            published_at=_normalize_text(record["published_at"]),
            snippet=_normalize_text(record["snippet"]),
            content=_normalize_text(record.get("content", "")),
            player_name=_normalize_text(record.get("player_name", "")),
            team_name=_normalize_text(record.get("team_name", "")),
        )
        for record in eligible.to_dict(orient="records")
    ]


def _selected_player_names(week_payload: Mapping[str, object], roles: Sequence[str]) -> List[str]:
    players = []
    for player in week_payload.get("squad", []):
        if player.get("selected_role") in roles:
            players.append(str(player["player_name"]))
    return players


def _bench_order_names(week_payload: Mapping[str, object]) -> List[str]:
    bench_rows = [
        player
        for player in week_payload.get("squad", [])
        if str(player.get("selected_role", "")).startswith("Bench")
    ]
    bench_rows.sort(key=lambda player: str(player["selected_role"]))
    return [str(player["player_name"]) for player in bench_rows]


def _pre_move_squad_rows(week_payload: Mapping[str, object]) -> List[Mapping[str, object]]:
    rows = list(week_payload.get("pre_move_squad", []))
    if rows:
        return rows
    return list(week_payload.get("squad", []))


def _pre_move_squad_lines(week_payload: Mapping[str, object]) -> List[str]:
    players = _pre_move_squad_rows(week_payload)
    players.sort(
        key=lambda player: (
            str(player.get("position")),
            -float(player.get("predicted_points_3gw", 0.0) or 0.0),
            str(player.get("player_name")),
        )
    )
    lines: List[str] = []
    for player in players:
        lines.append(
            "- "
            + f"{player['player_name']} ({player['position']}, {player['price']:.1f}) "
            + f"pred1={player['predicted_points_1gw']:.2f} "
            + f"pred3={player['predicted_points_3gw']:.2f} pred5={player['predicted_points_5gw']:.2f} "
            + f"pred_min={player['predicted_minutes']:.1f} appearance={player['appearance_probability']:.2f}"
        )
    return lines


def _candidate_transfer_lines(week_payload: Mapping[str, object]) -> List[str]:
    candidates = list(week_payload.get("candidate_transfers", []))
    if not candidates:
        return ["- No positive transfer candidate cleared the search threshold in this week."]
    lines: List[str] = []
    for index, candidate in enumerate(candidates, start=1):
        lines.append(
            "- "
            + f"[{index}] OUT {', '.join(candidate['players_out'])} | "
            + f"IN {', '.join(candidate['players_in'])} | "
            + f"gain={float(candidate['projected_gain']):.2f} | hit={int(candidate['hit_cost'])}"
        )
        explanation = _normalize_text(candidate.get("explanation", ""))
        if explanation:
            lines.append(f"  Explanation: {explanation}")
    return lines


def _evidence_lines(documents: Sequence[EvidenceRecord]) -> List[str]:
    if not documents:
        return ["Evidence snapshot:", "- No deadline-scoped evidence snapshot was attached."]
    lines: List[str] = []
    lines.append("Evidence snapshot:")
    lines.append(f"- Documents: {len(documents)}")
    player_counts: Dict[str, int] = {}
    team_counts: Dict[str, int] = {}
    for document in documents:
        if document.player_name:
            player_counts[document.player_name] = player_counts.get(document.player_name, 0) + 1
        if document.team_name:
            team_counts[document.team_name] = team_counts.get(document.team_name, 0) + 1
    if player_counts:
        lines.append("Player evidence summaries:")
        for name, count in sorted(player_counts.items(), key=lambda item: (-item[1], item[0]))[:5]:
            snippets = [doc.snippet for doc in documents if doc.player_name == name and doc.snippet][:2]
            lines.append(f"- {name}: docs={count}, notes={' | '.join(snippets) if snippets else 'no snippets'}")
    if team_counts:
        lines.append("Team evidence summaries:")
        for name, count in sorted(team_counts.items(), key=lambda item: (-item[1], item[0]))[:5]:
            snippets = [doc.snippet for doc in documents if doc.team_name == name and doc.snippet][:2]
            lines.append(f"- {name}: docs={count}, notes={' | '.join(snippets) if snippets else 'no snippets'}")
    lines.append("Selected source documents:")
    for index, document in enumerate(documents, start=1):
        snippet = document.snippet or document.content[:180]
        lines.append(
            f"- [{index}] {document.source_name} | {document.title} | {document.published_at} | {document.url}"
        )
        if snippet:
            lines.append(f"  Snippet: {snippet}")
    return lines


def _evidence_fulltext_lines(documents: Sequence[EvidenceRecord], max_chars_per_document: int = 6000) -> List[str]:
    if not documents:
        return ["Evidence documents:", "- No deadline-scoped evidence was attached."]
    lines = ["Evidence documents:"]
    for index, document in enumerate(documents, start=1):
        body = _clean_optional_text(document.content) or _clean_optional_text(document.snippet)
        if max_chars_per_document > 0 and len(body) > max_chars_per_document:
            body = body[:max_chars_per_document].rstrip() + " [TRUNCATED]"
        lines.extend(
            [
                f"[{index}] Source: {document.source_name}",
                f"Title: {document.title}",
                f"Published: {document.published_at}",
                f"URL: {document.url}",
                "Text:",
                body if body else "(empty)",
                "",
            ]
        )
    return lines


def _assistant_target(week_payload: Mapping[str, object]) -> str:
    transfers = [
        {
            "players_out": list(move["players_out"]),
            "players_in": list(move["players_in"]),
            "projected_gain": move["projected_gain"],
            "hit_cost": move["hit_cost"],
        }
        for move in week_payload.get("transfers_applied", [])
    ]
    target = {
        "transfers": transfers,
        "captain": week_payload["captain_name"],
        "vice_captain": week_payload["vice_captain_name"],
        "starters": _selected_player_names(week_payload, ("Captain", "Vice Captain", "XI")),
        "bench_order": _bench_order_names(week_payload),
        "chip": week_payload["chip_used"],
        "reasoning_summary": [
            *([f"Chip rationale: {week_payload['chip_reason']}"] if week_payload.get("chip_reason") else []),
            *list(week_payload.get("notes", []))[:3],
        ],
    }
    return json.dumps(target, ensure_ascii=True, indent=2)


def _player_value(record: Mapping[str, object], column: str) -> object:
    value = record.get(column)
    if value is None:
        return 0.0
    if isinstance(value, str):
        stripped = value.strip()
        if not stripped:
            return ""
        return stripped
    return value


def _player_feature_lines(record: Mapping[str, object]) -> List[str]:
    lines: List[str] = []
    for column in PLAYER_FORECAST_PROMPT_FIELDS:
        if column not in record:
            continue
        value = _player_value(record, column)
        if isinstance(value, bool):
            normalized = int(value)
        elif isinstance(value, (int, float)):
            normalized = f"{float(value):.4f}"
        else:
            normalized = str(value)
        lines.append(f"- {column}: {normalized}")
    return lines


def _player_forecast_prompt(
    record: Mapping[str, object],
    deadline_ts: str,
    evidence_documents: Sequence[EvidenceRecord],
) -> str:
    news_text = _clean_optional_text(record.get("news_pre_deadline") or record.get("news") or "")
    sections = [
        "Forecast this FPL player's post-deadline outcomes using only the provided pre-deadline information.",
        "",
        "Return exactly one JSON object with numeric fields:",
        '- "predicted_points_1gw"',
        '- "predicted_points_3gw"',
        '- "predicted_points_5gw"',
        '- "predicted_minutes_1gw"',
        '- "predicted_appearance_probability"',
        "",
        "Do not include markdown, prose, or code fences.",
        "",
        f"Season: {record['season']}",
        f"Gameweek: {int(record['week'])}",
        f"Deadline: {deadline_ts}",
        f"Player: {record['player_name']}",
        f"Player ID: {int(record['player_id'])}",
        f"Team ID: {int(record['team_id'])}",
        f"Position: {record['position']}",
        f"Status pre-deadline: {_clean_optional_text(record.get('status_pre_deadline') or record.get('status') or '')}",
        f"News pre-deadline: {news_text if news_text else 'none'}",
        "",
        "Structured pre-deadline features:",
        *_player_feature_lines(record),
    ]
    if evidence_documents:
        sections.extend(["", "Curated timestamp-safe evidence:", *_evidence_lines(evidence_documents)])
    return "\n".join(sections)


def _baseline_forecast_payload(forecast: Optional[PlayerForecast]) -> Dict[str, float]:
    if forecast is None:
        return {}
    return {
        "baseline_points_1gw": round(float(forecast.predicted_points_1gw), 4),
        "baseline_points_3gw": round(float(forecast.predicted_points_3gw), 4),
        "baseline_points_5gw": round(float(forecast.predicted_points_5gw), 4),
        "baseline_minutes_1gw": round(float(forecast.predicted_minutes), 4),
        "baseline_appearance_probability": round(float(forecast.appearance_probability), 4),
        "baseline_uncertainty": round(float(forecast.uncertainty), 4),
    }


def _player_forecast_adjustment_prompt(
    record: Mapping[str, object],
    deadline_ts: str,
    evidence_documents: Sequence[EvidenceRecord],
    baseline_forecast: Optional[PlayerForecast],
    max_chars_per_document: int = 6000,
) -> str:
    news_text = _clean_optional_text(record.get("news_pre_deadline") or record.get("news") or "")
    baseline = _baseline_forecast_payload(baseline_forecast)
    baseline_json = json.dumps(baseline, ensure_ascii=True, indent=2) if baseline else "{}"
    sections = [
        "Adjust a baseline FPL player forecast using timestamp-safe text evidence.",
        "",
        "Use only information available before the deadline. The baseline forecast is produced by a classic ML model from structured historical features. Do not ask for hidden features.",
        "",
        "Return exactly one JSON object with numeric fields:",
        '- "predicted_points_1gw"',
        '- "predicted_points_3gw"',
        '- "predicted_points_5gw"',
        '- "predicted_minutes_1gw"',
        '- "predicted_appearance_probability"',
        "",
        "Do not include markdown, prose, or code fences.",
        "",
        "Player context:",
        f"- Season: {record['season']}",
        f"- Gameweek: {int(record['week'])}",
        f"- Deadline: {deadline_ts}",
        f"- Player: {record['player_name']}",
        f"- Player ID: {int(record['player_id'])}",
        f"- Team ID: {int(record['team_id'])}",
        f"- Position: {record['position']}",
        f"- Status pre-deadline: {_clean_optional_text(record.get('status_pre_deadline') or record.get('status') or '') or 'none'}",
        f"- Official player news pre-deadline: {news_text if news_text else 'none'}",
        "",
        "Classic ML baseline forecast:",
        baseline_json,
        "",
        "Timestamp-safe text evidence:",
        *_evidence_fulltext_lines(evidence_documents, max_chars_per_document=max_chars_per_document),
    ]
    return "\n".join(sections)


def _player_forecast_target(record: Mapping[str, object]) -> str:
    return json.dumps(
        {
            "predicted_points_1gw": round(float(record["label_points_1gw"]), 4),
            "predicted_points_3gw": round(float(record["label_points_3gw"]), 4),
            "predicted_points_5gw": round(float(record["label_points_5gw"]), 4),
            "predicted_minutes_1gw": round(float(record["label_minutes_1gw"]), 4),
            "predicted_appearance_probability": round(float(record["label_appearance_probability"]), 4),
        },
        ensure_ascii=True,
        indent=2,
    )


def _player_forecast_metadata(
    record: Mapping[str, object],
    evidence_documents: Sequence[EvidenceRecord],
    deadline_ts: Optional[str] = None,
    baseline_forecast: Optional[PlayerForecast] = None,
    include_feature_snapshot: bool = True,
) -> Dict[str, object]:
    payload: Dict[str, object] = {
        "task": "player_forecast",
        "season": str(record["season"]),
        "week": int(record["week"]),
        "player_id": int(record["player_id"]),
        "player_name": str(record["player_name"]),
        "team_id": int(record["team_id"]),
        "position": str(record["position"]),
        "deadline_ts": str(deadline_ts or record.get("kickoff_time", "")),
        "status_pre_deadline": _clean_optional_text(record.get("status_pre_deadline") or record.get("status") or ""),
        "news_pre_deadline": _clean_optional_text(record.get("news_pre_deadline") or record.get("news") or ""),
        "baseline_forecast": _baseline_forecast_payload(baseline_forecast),
        "labels": {
            "points_1gw": float(record["label_points_1gw"]),
            "points_3gw": float(record["label_points_3gw"]),
            "points_5gw": float(record["label_points_5gw"]),
            "minutes_1gw": float(record["label_minutes_1gw"]),
            "appearance_probability": float(record["label_appearance_probability"]),
        },
        "evidence_documents": [asdict(document) for document in evidence_documents],
    }
    if include_feature_snapshot:
        payload["feature_columns"] = [column for column in PLAYER_FORECAST_PROMPT_FIELDS if column in record]
        payload["feature_snapshot"] = {
            column: _player_value(record, column)
            for column in PLAYER_FORECAST_PROMPT_FIELDS
            if column in record
        }
    return payload


def _transfer_choice_option_payloads(week_payload: Mapping[str, object]) -> List[Dict[str, Any]]:
    season = str(week_payload["season"])
    week = int(week_payload["week"])
    pre_move_squad = [_snapshot_to_squad_player(player) for player in week_payload.get("pre_move_squad", [])]
    if not pre_move_squad:
        pre_move_squad = [_snapshot_to_squad_player(player) for player in week_payload.get("squad", [])]

    forecast_by_id: Dict[int, PlayerForecast] = {}
    for player in [*list(week_payload.get("pre_move_squad", [])), *list(week_payload.get("squad", []))]:
        forecast_by_id[int(player["player_id"])] = _snapshot_to_forecast(player, season=season, week=week)
    for candidate in week_payload.get("candidate_transfers", []):
        for player in candidate.get("incoming_players", []):
            forecast_by_id[int(player["player_id"])] = _snapshot_to_forecast(player, season=season, week=week)
        for player in candidate.get("outgoing_players", []):
            forecast_by_id[int(player["player_id"])] = _snapshot_to_forecast(player, season=season, week=week)

    metadata = _example_metadata(week_payload, evidence_documents=[])
    options: List[Dict[str, Any]] = []

    raw_options = [{"players_out": [], "players_in": [], "projected_gain": 0.0, "hit_cost": 0, "label": "Hold squad"}]
    raw_options.extend(list(week_payload.get("candidate_transfers", [])))

    for option_id, option in enumerate(raw_options):
        players_out = list(option.get("players_out", []))
        players_in = list(option.get("players_in", []))
        outgoing_ids = {
            player.player_id for player in pre_move_squad if player.player_name in set(players_out)
        }
        incoming_forecasts = [
            forecast
            for forecast in forecast_by_id.values()
            if forecast.player_name in set(players_in)
        ]
        updated_squad = [player for player in pre_move_squad if player.player_id not in outgoing_ids]
        updated_squad.extend(
            [
                SquadPlayer(
                    player_id=forecast.player_id,
                    player_name=forecast.player_name,
                    team_id=forecast.team_id,
                    position=forecast.position,
                    sell_price=forecast.price,
                )
                for forecast in incoming_forecasts
            ]
        )
        starters, bench_order, captain_id, vice_captain_id, starter_score = _optimize_lineup(updated_squad, forecast_by_id)
        captain_name = forecast_by_id[captain_id].player_name
        vice_captain_name = forecast_by_id[vice_captain_id].player_name
        prediction_bundle = {
            "transfers": (
                []
                if not players_in
                else [
                    {
                        "players_out": players_out,
                        "players_in": players_in,
                        "projected_gain": round(float(option.get("projected_gain", 0.0)), 2),
                        "hit_cost": int(option.get("hit_cost", 0)),
                    }
                ]
            ),
            "captain": captain_name,
            "vice_captain": vice_captain_name,
            "starters": [forecast_by_id[player_id].player_name for player_id in starters],
            "bench_order": [forecast_by_id[player_id].player_name for player_id in bench_order],
            "chip": str(week_payload.get("chip_used", "none") or "none"),
            "reasoning_summary": [],
        }
        predicted_score = round(
            starter_score
            + forecast_by_id[captain_id].predicted_points_1gw
            + (
                forecast_by_id[captain_id].predicted_points_1gw
                if str(week_payload.get("chip_used", "none")) == "triple_captain"
                else 0.0
            )
            - int(option.get("hit_cost", 0)),
            2,
        )
        actual_score = _score_prediction_bundle(metadata, prediction_bundle)
        label = str(option.get("label") or "").strip()
        if not label:
            if players_in:
                label = f"OUT {', '.join(players_out)} | IN {', '.join(players_in)}"
            else:
                label = "Hold squad"
        options.append(
            {
                "option_id": option_id,
                "label": label,
                "players_out": players_out,
                "players_in": players_in,
                "projected_gain": round(float(option.get("projected_gain", 0.0)), 2),
                "hit_cost": int(option.get("hit_cost", 0)),
                "predicted_score": predicted_score,
                "actual_score": actual_score,
                "captain": captain_name,
                "vice_captain": vice_captain_name,
                "starters": prediction_bundle["starters"],
                "bench_order": prediction_bundle["bench_order"],
                "chip": prediction_bundle["chip"],
                "prediction_bundle": prediction_bundle,
            }
        )
    options.sort(key=lambda option: (-float(option["actual_score"]), -float(option["predicted_score"]), int(option["option_id"])))
    return options


def _transfer_choice_prompt(
    season: str,
    week: int,
    deadline_ts: str,
    week_payload: Mapping[str, object],
    evidence_documents: Sequence[EvidenceRecord],
    options: Sequence[Mapping[str, Any]],
) -> str:
    option_lines: List[str] = []
    for option in sorted(options, key=lambda item: int(item["option_id"])):
        transfer_text = "Hold squad"
        if option["players_in"]:
            transfer_text = f"OUT {', '.join(option['players_out'])} | IN {', '.join(option['players_in'])}"
        option_lines.append(
            f"- [{option['option_id']}] {transfer_text} | pred_score={float(option['predicted_score']):.2f} | "
            f"captain={option['captain']} | vice={option['vice_captain']} | chip={option['chip']}"
        )
    return build_hybrid_decision_prompt(
        season=season,
        week=week,
        deadline_ts=deadline_ts,
        bank=float(week_payload["bank_before"]),
        free_transfers=int(week_payload["free_transfers_before"]),
        squad_lines=_pre_move_squad_lines(week_payload),
        evidence_lines=_evidence_lines(evidence_documents),
        candidate_lines=option_lines,
    )


def _transfer_choice_metadata(
    week_payload: Mapping[str, object],
    options: Sequence[Mapping[str, Any]],
    evidence_documents: Sequence[EvidenceRecord],
) -> Dict[str, object]:
    metadata = _example_metadata(week_payload, evidence_documents)
    metadata["candidate_options"] = [
        {
            "option_id": int(option["option_id"]),
            "label": option["label"],
            "players_out": list(option["players_out"]),
            "players_in": list(option["players_in"]),
            "predicted_score": float(option["predicted_score"]),
            "actual_score": float(option["actual_score"]),
            "captain": option["captain"],
            "vice_captain": option["vice_captain"],
            "chip": option["chip"],
        }
        for option in sorted(options, key=lambda item: int(item["option_id"]))
    ]
    return metadata


def _user_prompt(
    season: str,
    week: int,
    deadline_ts: str,
    week_payload: Mapping[str, object],
    evidence_documents: Sequence[EvidenceRecord],
) -> str:
    return "\n".join(
        [
            "You are building an FPL recommendation for a single pre-deadline week.",
            f"Season: {season}",
            f"Week: {week}",
            f"Deadline: {deadline_ts}",
            f"Bank before moves: {week_payload['bank_before']:.2f}",
            f"Free transfers before moves: {week_payload['free_transfers_before']}",
            "",
            "Current squad before moves and model forecasts:",
            *_pre_move_squad_lines(week_payload),
            "",
            "Candidate transfer shortlist:",
            *_candidate_transfer_lines(week_payload),
            "",
            "Curated evidence available before the deadline:",
            *_evidence_lines(evidence_documents),
            "",
            "Task:",
            "Choose a transfer plan from the shortlist or keep the squad unchanged, then set captain, vice_captain, starters, bench_order, chip, reasoning_summary.",
            "If you choose a transfer, assume the incoming players replace the outgoing players before you set the lineup.",
            "Return JSON with keys transfers, captain, vice_captain, starters, bench_order, chip, reasoning_summary.",
            "Use only information available before the deadline. Do not mention future outcomes.",
        ]
    )


def _example_metadata(
    week_payload: Mapping[str, object],
    evidence_documents: Sequence[EvidenceRecord],
) -> Dict[str, object]:
    player_rows: Dict[str, Mapping[str, object]] = {}
    for player in [*list(week_payload.get("pre_move_squad", [])), *list(week_payload.get("squad", []))]:
        player_rows[str(player["player_name"])] = player
    for candidate in week_payload.get("candidate_transfers", []):
        for key in ("incoming_players", "outgoing_players"):
            for player in candidate.get(key, []):
                player_rows[str(player["player_name"])] = player
    return {
        "season": week_payload["season"],
        "week": week_payload["week"],
        "bank_before": week_payload["bank_before"],
        "bank_after": week_payload["bank_after"],
        "free_transfers_before": week_payload["free_transfers_before"],
        "free_transfers_after": week_payload["free_transfers_after"],
        "team_predicted_score": week_payload["predicted_score"],
        "team_actual_score": week_payload["actual_score"],
        "league_average_score": week_payload.get("league_average_score"),
        "chip_used": week_payload["chip_used"],
        "chip_reason": week_payload.get("chip_reason", ""),
        "effective_captain_name": week_payload["effective_captain_name"],
        "evidence_count": len(evidence_documents),
        "evidence_urls": [document.url for document in evidence_documents],
        "player_actual_points": {
            player_name: player["actual_points_1gw"] for player_name, player in player_rows.items()
        },
        "player_actual_minutes": {
            player_name: player["actual_minutes"] for player_name, player in player_rows.items()
        },
        "player_positions": {
            player_name: player["position"] for player_name, player in player_rows.items()
        },
        "current_squad_names": [player["player_name"] for player in _pre_move_squad_rows(week_payload)],
        "post_move_squad_names": [player["player_name"] for player in week_payload.get("squad", [])],
        "candidate_transfers": [
            {
                "players_out": list(candidate["players_out"]),
                "players_in": list(candidate["players_in"]),
                "projected_gain": candidate["projected_gain"],
                "hit_cost": candidate["hit_cost"],
            }
            for candidate in week_payload.get("candidate_transfers", [])
        ],
    }


def _build_examples_from_report_payload(
    dataset: CanonicalDataset,
    report_payload: Mapping[str, object],
    evidence_frame: Optional[pd.DataFrame] = None,
    max_documents_per_week: int = 6,
    lookback_days: int = 14,
) -> List[LLMTrainingExample]:
    examples: List[LLMTrainingExample] = []
    for week_payload in report_payload.get("weeks", []):
        season = str(week_payload["season"])
        week = int(week_payload["week"])
        week_state = dataset.build_week_state((season, week))
        evidence_documents = select_evidence_for_deadline(
            evidence_frame if evidence_frame is not None else pd.DataFrame(),
            deadline_ts=week_state.deadline_ts,
            max_documents=max_documents_per_week,
            lookback_days=lookback_days,
        )
        examples.append(
            LLMTrainingExample(
                season=season,
                week=week,
                deadline_ts=week_state.deadline_ts,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an FPL decision assistant. Base recommendations on structured forecasts first, "
                            "then use timestamp-safe curated evidence for injury/news adjustments. Return strict JSON."
                        ),
                    },
                    {
                        "role": "user",
                        "content": _user_prompt(
                            season=season,
                            week=week,
                            deadline_ts=week_state.deadline_ts,
                            week_payload=week_payload,
                            evidence_documents=evidence_documents,
                        ),
                    },
                    {"role": "assistant", "content": _assistant_target(week_payload)},
                ],
                metadata=_example_metadata(week_payload, evidence_documents),
            )
        )
    return examples


def build_decision_sft_examples(
    dataset: CanonicalDataset,
    backtest_report_path: str,
    evidence_frame: Optional[pd.DataFrame] = None,
    max_documents_per_week: int = 6,
    lookback_days: int = 14,
) -> List[LLMTrainingExample]:
    report_payload = json.loads(Path(backtest_report_path).read_text())
    return _build_examples_from_report_payload(
        dataset=dataset,
        report_payload=report_payload,
        evidence_frame=evidence_frame,
        max_documents_per_week=max_documents_per_week,
        lookback_days=lookback_days,
    )


def build_multiseason_decision_sft_examples(
    dataset: CanonicalDataset,
    seasons: Optional[Sequence[str]] = None,
    initial_train_week_max: int = 10,
    start_week: Optional[int] = None,
    end_week: Optional[int] = None,
    alpha: float = 1.0,
    initial_budget: float = 100.0,
    max_free_transfers: int = 2,
    max_transfers_per_week: int = 1,
    min_projected_gain: float = 0.0,
    evidence_frame: Optional[pd.DataFrame] = None,
    max_documents_per_week: int = 6,
    lookback_days: int = 14,
) -> List[LLMTrainingExample]:
    available_seasons = sorted(
        dataset.training_frame.loc[dataset.training_frame["eligible_for_backtest"], "season"].astype(str).unique().tolist(),
        key=parse_season_start_year,
    )
    selected_seasons = list(seasons) if seasons is not None else available_seasons
    examples: List[LLMTrainingExample] = []
    for season in sorted(selected_seasons, key=parse_season_start_year):
        season_frame = dataset.training_frame.loc[
            (dataset.training_frame["season"].astype(str) == season) & dataset.training_frame["eligible_for_backtest"]
        ].copy()
        season_weeks = sorted(season_frame["week"].astype(int).unique().tolist())
        if not season_weeks:
            continue
        season_start_week = max(start_week or (initial_train_week_max + 1), min(season_weeks))
        season_end_week = min(end_week or max(season_weeks), max(season_weeks))
        if season_start_week > season_end_week:
            continue
        try:
            report = run_rolling_squad_backtest(
                dataset=dataset,
                test_season=season,
                initial_train_week_max=initial_train_week_max,
                start_week=season_start_week,
                end_week=season_end_week,
                alpha=alpha,
                initial_budget=initial_budget,
                max_free_transfers=max_free_transfers,
                max_transfers_per_week=max_transfers_per_week,
                min_projected_gain=min_projected_gain,
                league_average_by_week=None,
            )
        except ValueError:
            continue
        examples.extend(
            _build_examples_from_report_payload(
                dataset=dataset,
                report_payload=asdict(report),
                evidence_frame=evidence_frame,
                max_documents_per_week=max_documents_per_week,
                lookback_days=lookback_days,
            )
        )
    return sorted(examples, key=lambda example: (parse_season_start_year(example.season), int(example.week)))


def build_multiseason_transfer_choice_examples(
    dataset: CanonicalDataset,
    seasons: Optional[Sequence[str]] = None,
    initial_train_week_max: int = 10,
    start_week: Optional[int] = None,
    end_week: Optional[int] = None,
    alpha: float = 1.0,
    initial_budget: float = 100.0,
    max_free_transfers: int = 2,
    max_transfers_per_week: int = 1,
    min_projected_gain: float = 0.0,
    evidence_frame: Optional[pd.DataFrame] = None,
    max_documents_per_week: int = 6,
    lookback_days: int = 14,
) -> List[LLMTrainingExample]:
    available_seasons = sorted(
        dataset.training_frame.loc[dataset.training_frame["eligible_for_backtest"], "season"].astype(str).unique().tolist(),
        key=parse_season_start_year,
    )
    selected_seasons = list(seasons) if seasons is not None else available_seasons
    examples: List[LLMTrainingExample] = []
    for season in sorted(selected_seasons, key=parse_season_start_year):
        season_frame = dataset.training_frame.loc[
            (dataset.training_frame["season"].astype(str) == season) & dataset.training_frame["eligible_for_backtest"]
        ].copy()
        season_weeks = sorted(season_frame["week"].astype(int).unique().tolist())
        if not season_weeks:
            continue
        season_start_week = max(start_week or (initial_train_week_max + 1), min(season_weeks))
        season_end_week = min(end_week or max(season_weeks), max(season_weeks))
        if season_start_week > season_end_week:
            continue
        try:
            report = run_rolling_squad_backtest(
                dataset=dataset,
                test_season=season,
                initial_train_week_max=initial_train_week_max,
                start_week=season_start_week,
                end_week=season_end_week,
                alpha=alpha,
                initial_budget=initial_budget,
                max_free_transfers=max_free_transfers,
                max_transfers_per_week=max_transfers_per_week,
                min_projected_gain=min_projected_gain,
                league_average_by_week=None,
            )
        except ValueError:
            continue

        for week_payload in asdict(report).get("weeks", []):
            week_state = dataset.build_week_state((str(week_payload["season"]), int(week_payload["week"])))
            evidence_documents = select_evidence_for_deadline(
                evidence_frame if evidence_frame is not None else pd.DataFrame(),
                deadline_ts=week_state.deadline_ts,
                max_documents=max_documents_per_week,
                lookback_days=lookback_days,
            )
            options = _transfer_choice_option_payloads(week_payload)
            if len(options) < 2:
                continue
            best_option = options[0]
            examples.append(
                LLMTrainingExample(
                    season=str(week_payload["season"]),
                    week=int(week_payload["week"]),
                    deadline_ts=week_state.deadline_ts,
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are an FPL transfer-choice assistant. "
                                "Choose among legal pre-deadline options using structured forecasts first and "
                                "timestamp-safe evidence second. Return strict JSON."
                            ),
                        },
                        {
                            "role": "user",
                            "content": _transfer_choice_prompt(
                                season=str(week_payload["season"]),
                                week=int(week_payload["week"]),
                                deadline_ts=week_state.deadline_ts,
                                week_payload=week_payload,
                                evidence_documents=evidence_documents,
                                options=options,
                            ),
                        },
                        {
                            "role": "assistant",
                            "content": json.dumps(
                                {
                                    "selected_option": int(best_option["option_id"]),
                                    "reasoning_summary": [],
                                },
                                ensure_ascii=True,
                                indent=2,
                            ),
                        },
                    ],
                    metadata=_transfer_choice_metadata(
                        week_payload=week_payload,
                        options=options,
                        evidence_documents=evidence_documents,
                    ),
                )
            )
    return sorted(examples, key=lambda example: (parse_season_start_year(example.season), int(example.week)))


def build_multiseason_player_forecast_examples(
    dataset: CanonicalDataset,
    seasons: Optional[Sequence[str]] = None,
    start_week: Optional[int] = None,
    end_week: Optional[int] = None,
    evidence_frame: Optional[pd.DataFrame] = None,
    max_documents_per_week: int = 3,
    lookback_days: int = 7,
    prompt_style: str = "features",
    max_evidence_chars_per_document: int = 6000,
) -> List[LLMTrainingExample]:
    available_seasons = sorted(
        dataset.training_frame.loc[dataset.training_frame["eligible_for_training"], "season"].astype(str).unique().tolist(),
        key=parse_season_start_year,
    )
    selected_seasons = list(seasons) if seasons is not None else available_seasons
    examples: List[LLMTrainingExample] = []

    for season in sorted(selected_seasons, key=parse_season_start_year):
        season_frame = dataset.training_frame.loc[
            (dataset.training_frame["season"].astype(str) == season) & dataset.training_frame["eligible_for_training"]
        ].copy()
        season_weeks = sorted(season_frame["week"].astype(int).unique().tolist())
        if not season_weeks:
            continue
        season_start_week = max(start_week or min(season_weeks), min(season_weeks))
        season_end_week = min(end_week or max(season_weeks), max(season_weeks))
        if season_start_week > season_end_week:
            continue

        for week in season_weeks:
            if week < season_start_week or week > season_end_week:
                continue
            week_state = dataset.build_week_state((season, week))
            evidence_documents = select_evidence_for_deadline(
                evidence_frame if evidence_frame is not None else pd.DataFrame(),
                deadline_ts=week_state.deadline_ts,
                max_documents=max_documents_per_week,
                lookback_days=lookback_days,
            )
            week_frame = dataset.week_frame((season, week))
            week_frame = week_frame.loc[week_frame["eligible_for_training"]].copy()
            baseline_forecasts: Dict[int, PlayerForecast] = {}
            if prompt_style == "baseline_adjustment":
                train_frame = training_rows_asof(dataset.training_frame, season, int(week))
                if not train_frame.empty:
                    model_suite = fit_model_suite_from_frame(
                        train_frame=train_frame,
                        feature_names=dataset.feature_columns,
                    )
                    baseline_forecasts = {
                        forecast.player_id: forecast
                        for forecast in model_suite.predict_frame(week_frame)
                    }
            for record in week_frame.to_dict(orient="records"):
                baseline_forecast = baseline_forecasts.get(int(record["player_id"]))
                if prompt_style == "baseline_adjustment":
                    system_content = (
                        "You are an FPL forecast adjustment assistant. "
                        "Use the classic ML baseline plus timestamp-safe text evidence to predict actual post-deadline outcomes. "
                        "Return strict JSON."
                    )
                    user_content = _player_forecast_adjustment_prompt(
                        record=record,
                        deadline_ts=week_state.deadline_ts,
                        evidence_documents=evidence_documents,
                        baseline_forecast=baseline_forecast,
                        max_chars_per_document=max_evidence_chars_per_document,
                    )
                    include_feature_snapshot = False
                else:
                    system_content = (
                        "You are an FPL player forecasting assistant. "
                        "Predict post-deadline player outcomes from structured pre-deadline inputs only. "
                        "Return strict JSON."
                    )
                    user_content = _player_forecast_prompt(
                        record=record,
                        deadline_ts=week_state.deadline_ts,
                        evidence_documents=evidence_documents,
                    )
                    include_feature_snapshot = True
                examples.append(
                    LLMTrainingExample(
                        season=season,
                        week=int(week),
                        deadline_ts=week_state.deadline_ts,
                        messages=[
                            {
                                "role": "system",
                                "content": system_content,
                            },
                            {
                                "role": "user",
                                "content": user_content,
                            },
                            {
                                "role": "assistant",
                                "content": _player_forecast_target(record),
                            },
                        ],
                        metadata=_player_forecast_metadata(
                            record=record,
                            evidence_documents=evidence_documents,
                            deadline_ts=week_state.deadline_ts,
                            baseline_forecast=baseline_forecast,
                            include_feature_snapshot=include_feature_snapshot,
                        ),
                    )
                )

    return sorted(
        examples,
        key=lambda example: (
            parse_season_start_year(example.season),
            int(example.week),
            int(example.metadata.get("player_id", 0)),
        ),
    )


def split_llm_examples_by_time(
    examples: Sequence[object],
    eval_season: str,
    eval_week_min: int,
    eval_week_max: Optional[int] = None,
) -> Dict[str, List[object]]:
    train_examples: List[object] = []
    eval_examples: List[object] = []
    eval_start_key = parse_season_start_year(eval_season) * 100 + int(eval_week_min)
    eval_end_key = parse_season_start_year(eval_season) * 100 + (
        int(eval_week_max) if eval_week_max is not None else 99
    )
    for example in examples:
        if isinstance(example, LLMTrainingExample):
            season = example.season
            week = int(example.week)
        else:
            season = str(example["season"])
            week = int(example["week"])
        example_key = parse_season_start_year(season) * 100 + week
        if season == eval_season and eval_start_key <= example_key <= eval_end_key:
            eval_examples.append(example)
        elif example_key < eval_start_key:
            train_examples.append(example)
    return {"train": train_examples, "eval": eval_examples}


def write_llm_training_examples(examples: Sequence[object], output_path: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        for example in examples:
            payload = asdict(example) if isinstance(example, LLMTrainingExample) else dict(example)
            handle.write(json.dumps(payload, ensure_ascii=True) + "\n")


def write_llm_training_split(split_payload: Mapping[str, Sequence[object]], output_dir: str) -> Dict[str, str]:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    train_path = output_path / "train.jsonl"
    eval_path = output_path / "eval.jsonl"
    summary_path = output_path / "split_summary.json"
    write_llm_training_examples(split_payload.get("train", []), str(train_path))
    write_llm_training_examples(split_payload.get("eval", []), str(eval_path))
    summary = {
        "train_examples": len(split_payload.get("train", [])),
        "eval_examples": len(split_payload.get("eval", [])),
        "train_path": str(train_path),
        "eval_path": str(eval_path),
    }
    summary_path.write_text(json.dumps(summary, indent=2))
    return {"train": str(train_path), "eval": str(eval_path), "summary": str(summary_path)}

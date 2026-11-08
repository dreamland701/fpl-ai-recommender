#!/usr/bin/env python3
"""Build clipped residual player-forecast SFT splits from a multi-season corpus.

Differences from build_residual_player_forecast_split.py (v1):

- Consumes a flat corpus JSONL (from `fpl-ai export-llm-player-forecast-corpus`)
  instead of a pre-split source dir, and supports multiple seasons.
- Chronological cutoffs are (season, week) pairs, not bare week numbers.
- Residual delta labels are SHRUNK then CLIPPED. Realized deltas are dominated
  by outcome noise (sd ~3.5 pts on 1GW for the top-128 pool, roughly zero
  mean), so the expected component of an observed delta is only a fraction of
  it; training on shrunk deltas targets that expected component instead of the
  noise. Clipping alone saturated ~75% of labels at the bound, which teaches
  a degenerate "always output the bound" policy.
- Deltas are rounded coarsely (points 1dp, minutes integer, probability 2dp)
  so the completion token distribution is easier to learn.
- Adds `evidence_present` to metadata and states it explicitly in the prompt.
- Prompt framing: the LLM is the forecaster; the classic ML forecast is one
  input signal it conditions on. The output stays parametrized as deltas
  relative to that signal because bounded corrections train stably.

Usage:

  python3 scripts/build_residual_player_forecast_split_v2.py \
    --corpus reports/llm_player_forecast_multiseason_2022_26_baseline_adjustment_v1.jsonl \
    --output-dir reports/llm_residual_v2_train_2022_26_thru_gw11_eval_gw12_30 \
    --train-through 2025-26:11 \
    --eval-weeks 2025-26:12-30 \
    --top-n 128
"""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


DELTA_SPECS = {
    # delta_key: (baseline_key, label_key, clip_abs, round_digits)
    "delta_points_1gw": ("baseline_points_1gw", "points_1gw", 2.0, 1),
    "delta_points_3gw": ("baseline_points_3gw", "points_3gw", 4.0, 1),
    "delta_points_5gw": ("baseline_points_5gw", "points_5gw", 6.0, 1),
    "delta_minutes_1gw": ("baseline_minutes_1gw", "minutes_1gw", 20.0, 0),
    "delta_appearance_probability": (
        "baseline_appearance_probability",
        "appearance_probability",
        0.25,
        2,
    ),
}


def _load_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open() as handle:
        for line in handle:
            line = line.strip()
            if line:
                yield json.loads(line)


def _write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def parse_season_start_year(season: str) -> int:
    return int(str(season).split("-", 1)[0])


def season_week_key(season: str, week: int) -> int:
    return parse_season_start_year(season) * 100 + int(week)


def _parse_cutoff(raw: str) -> int:
    season, week = raw.split(":", 1)
    return season_week_key(season.strip(), int(week))


def _parse_eval_weeks(raw: str) -> set[int]:
    """Parse '2025-26:12-30' or '2025-26:12,14,16' into season-week keys."""
    season, weeks_raw = raw.split(":", 1)
    keys: set[int] = set()
    for part in weeks_raw.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            start, end = part.split("-", 1)
            weeks = range(int(start), int(end) + 1)
        else:
            weeks = [int(part)]
        keys.update(season_week_key(season.strip(), week) for week in weeks)
    return keys


def _baseline_score(row: dict[str, Any]) -> float:
    baseline = row.get("metadata", {}).get("baseline_forecast", {}) or {}
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


# Pre-GW scout-report/preview genre: team-news-dense articles (Sky scout
# reports live; Guardian match previews historically). Wes flagged these as
# markedly higher-quality than generic news — when preferred, they rank
# first and get a larger character budget.
# Two taxonomies. E11-full (the live champion) was TRAINED with the narrow
# one, so live decodes must use it too or train/live prompts diverge — the
# same parity rule applied to the E13a market line. The broad taxonomy is
# what E15 trained on; select it with FPL_BROAD_SCOUT_PATTERN=1.
_SCOUT_NARROW = r"scout report|team news|predicted line|preview|tips"
_SCOUT_BROAD = (
    r"scout report|scout selection|team news|predicted line|preview|tips|"
    r"transfer radar|ones to watch|differentials?|best (fpl )?captain|"
    r"captain for gameweek|lessons from|fpl|fantasy premier league|"
    r"bonus points|price (rise|fall|change)|injur(y|ies) (list|round|update)|"
    r"squad for|defensive contribution"
    # REVERTED terms (false positives, 2026-09-10): "deadline day" and
    # "who (is|could|are)" matched Guardian transfer live-blogs; "in fantasy"
    # matched "Mike Dean ... 'in fantasy land'".
)
SCOUT_TITLE_PATTERN = re.compile(
    _SCOUT_BROAD if os.environ.get("FPL_BROAD_SCOUT_PATTERN", "0") == "1" else _SCOUT_NARROW,
    re.IGNORECASE,
)


# E21 (2026-10-10): article-type control from the out-of-sample source study
# (reports/review_fixes_2026_10/article_source_value.md). Titles matching
# FPL_EVIDENCE_DROP are removed (price-change/transfer-trend and transfer-news
# articles made the SFT's availability AUC worse); titles matching
# FPL_EVIDENCE_PRIORITY rank first (Guardian team news / predicted line-ups,
# the most informative type). Unset = E20 behaviour.
EVIDENCE_DROP = re.compile(os.environ["FPL_EVIDENCE_DROP"], re.IGNORECASE) if os.environ.get("FPL_EVIDENCE_DROP") else None
EVIDENCE_PRIORITY = re.compile(os.environ["FPL_EVIDENCE_PRIORITY"], re.IGNORECASE) if os.environ.get("FPL_EVIDENCE_PRIORITY") else None


def _mention_pattern(player_name: str) -> re.Pattern | None:
    """Same word-boundary surname pattern used at attach time (see
    attach_player_evidence_to_corpus.py:_name_pattern), duplicated here
    because this stage truncates independently and needs to find the same
    mention to center on."""
    cleaned = str(player_name or "").strip()
    tokens = [token for token in cleaned.split() if len(token) > 1]
    if not tokens:
        return None
    alternatives = {re.escape(cleaned)} | {re.escape(tokens[-1])}
    return re.compile(r"\b(?:" + "|".join(sorted(alternatives, key=len, reverse=True)) + r")\b", re.IGNORECASE)


MULTI_WINDOW_MAX = 3
MULTI_WINDOW_MIN_CHARS = 110


def _windowed_content(content: str, budget: int, player_name: str = "") -> str:
    """Truncate to `budget` chars around the player's mentions.

    Plain prefix truncation silently discards the player-specific text
    whenever a document is much longer than the budget (40-50k char podcast
    transcripts, 25-29k char match live-blogs).

    Single-window centering (the pre-2026-09-10 behaviour) fixed that but
    still showed only the FIRST mention. In a 29k-char match report that is
    an arbitrary choice: GW4 2026-27 Calafiori was mentioned 10 times in one
    report, and the single window landed on "67 min: Double substitution ...
    replace Calafiori" — a true but unrepresentative slice that omitted his
    assist for the winner. Wes: "if the article is 25,000 words we cannot
    just use it directly."

    So: collect up to MULTI_WINDOW_MAX mention windows, merge overlaps, and
    join them with an ellipsis, spending the same total budget. Documents
    shorter than the budget are returned whole (unchanged behaviour), and a
    document with no mention still falls back to the prefix.
    """
    if len(content) <= budget:
        return content
    pattern = _mention_pattern(player_name)
    matches = list(pattern.finditer(content)) if pattern else []
    if not matches:
        return content[:budget]
    n_windows = min(MULTI_WINDOW_MAX, max(1, budget // MULTI_WINDOW_MIN_CHARS), len(matches))
    if n_windows <= 1:
        center = matches[0].start()
        half = budget // 2
        start = max(0, min(center - half, len(content) - budget))
        return content[start : start + budget]

    # Spread the budget over the first N mentions, then merge overlaps so
    # adjacent mentions read as one continuous passage instead of repeating.
    picked = matches[:n_windows]
    per = budget // len(picked)
    half = per // 2
    spans = []
    for m in picked:
        start = max(0, min(m.start() - half, len(content) - per))
        spans.append([start, start + per])
    spans.sort()
    merged = [spans[0]]
    for start, end in spans[1:]:
        if start <= merged[-1][1] + 40:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    total = sum(e - s for s, e in merged)
    if total > budget:  # merging can overshoot; trim the last span
        merged[-1][1] -= total - budget
    pieces = [content[s:e].strip() for s, e in merged if e > s]
    return " … ".join(pieces)


def _evidence_lines(
    documents: list[dict[str, Any]],
    max_docs: int,
    max_chars: int,
    prefer_scout: bool = False,
    preferred_chars: int = 800,
    player_name: str = "",
) -> str:
    if EVIDENCE_DROP is not None:
        documents = [doc for doc in documents if not EVIDENCE_DROP.search(str(doc.get("title") or ""))]
    if prefer_scout:
        documents = sorted(
            documents,
            key=lambda doc: 0 if SCOUT_TITLE_PATTERN.search(str(doc.get("title") or "")) else 1,
        )
    if EVIDENCE_PRIORITY is not None:  # stable sort: priority titles first, the scout order kept within tiers
        documents = sorted(documents, key=lambda doc: 0 if EVIDENCE_PRIORITY.search(str(doc.get("title") or "")) else 1)
    lines: list[str] = []
    for index, doc in enumerate(documents[:max_docs], start=1):
        budget = max_chars
        if prefer_scout and SCOUT_TITLE_PATTERN.search(str(doc.get("title") or "")):
            budget = preferred_chars
        content = " ".join(str(doc.get("content") or doc.get("snippet") or "").split())
        windowed = _windowed_content(content, budget, player_name)
        if len(windowed) < len(content):
            prefix = "... " if windowed != content[: len(windowed)] else ""
            windowed = prefix + windowed.rsplit(" ", 1)[0] + " ..."
        lines.append(
            "\n".join(
                [
                    f"[{index}] {doc.get('source_name') or 'unknown'} | {doc.get('published_at') or 'unknown time'}",
                    f"Title: {doc.get('title') or ''}",
                    f"Text: {windowed}",
                ]
            )
        )
    return "\n\n".join(lines)


def _round_delta(value: float, digits: int) -> float:
    rounded = round(value, digits) if digits > 0 else float(int(round(value)))
    # Avoid emitting "-0.0" tokens.
    return abs(rounded) if rounded == 0 else rounded


def _fixture_outlook_line(metadata: dict[str, Any]) -> str:
    """Compact schedule block, e.g. 'GW13: BOU (H, diff 2); GW14: LIV (A, diff 5); GW15: blank'."""
    outlook = metadata.get("fixture_outlook") or []
    if not outlook:
        return ""
    parts: list[str] = []
    for entry in outlook:
        if entry.get("opponent") is None:
            parts.append(f"GW{entry['gw']}: blank")
        else:
            parts.append(f"GW{entry['gw']}: {entry['opponent']} ({entry['venue']}, diff {entry['difficulty']})")
    return "; ".join(parts)


# What the classic ridge actually consumes (dataset.SAFE_FEATURE_COLUMNS) vs
# what it cannot see. Stated in the prompt so the LLM adjusts only for its
# genuine information edge instead of double-counting priced-in signals.
BASELINE_PROVENANCE_TEXT = (
    "The classic signal already prices in recent form, xG/ICT trends, team/opponent form, this GW's "
    "fixture (incl. blanks/doubles), market trends, and a binary injury flag. It cannot see status/news "
    "wording, fixtures beyond this GW, cup congestion, or post-break effects — adjust only for those."
)

# E17 (FPL_PROMPT_V17=1). The v1 text above is WRONG about the fixture and
# measurably suppressed the one correction the anchor most needed.
#
# Measured 2026-09-18 (Wes's Evanilson-v-Liverpool case): the anchor's
# standardized coefficient on opponent_goals_against_avg_3 was +0.0041
# (top feature 0.4843) and -0.0163 on the 5-week version (wrong sign). It
# leaned on the subjective FDR integer instead. Real 1GW points swing
# 25-34% between the toughest and leakiest opponent quartile; the forecast
# swung ~2%. Yet the prompt asserted opponent form and this GW's fixture
# were "already priced" and told the model to "adjust only for" news,
# congestion and future fixtures. On the GW5 decode the adapter obeyed:
# corr(delta_1gw, opponent goals conceded) = -0.048, while
# corr(delta_1gw, baseline) = -0.708 — the channel had collapsed to
# unconditional shrink, identical in every fixture quartile.
#
# v17 states the blind spot honestly and names the opponent adjustment as
# in-scope. Pair it with FPL_OPPONENT_INTERACTION=1 so the anchor is also
# fixed; the claim then describes a real anchor rather than a promise.
BASELINE_PROVENANCE_TEXT_V17 = (
    "The classic signal prices in recent form, xG/ICT trends, team form, blanks/doubles, market trends, "
    "and a binary injury flag. Two known weaknesses you SHOULD correct: (1) it judges the fixture mostly "
    "by the league's coarse 1-5 difficulty rating, so it under-reacts to how good the specific opponent's "
    "defence has actually been lately — discount attackers facing a mean defence and promote them against "
    "a leaky one; (2) it sees only the player's OWN injury flag, never his team-mates', so it misses role "
    "changes when a rival at his position is out. It also cannot see status/news wording, fixtures beyond "
    "this GW, cup congestion, or post-break effects."
)


def _opponent_record_line(metadata: dict) -> str:
    """Opponent's measured recent defensive/attacking record (E17).

    The anchor consumes these as numbers but weights them at ~0; stating
    them in words gives the text channel something concrete to reason with,
    instead of the bare FDR integer already in the fixture-outlook line.
    """
    opponent = metadata.get("opponent_context") or {}
    if not opponent:
        return ""
    parts = []
    name = opponent.get("name")
    conceded_3 = opponent.get("goals_against_avg_3")
    conceded_5 = opponent.get("goals_against_avg_5")
    scored_3 = opponent.get("goals_for_avg_3")
    rank = opponent.get("defence_rank")
    if name:
        parts.append(f"Opponent: {name}")
    if conceded_3 is not None:
        text = f"conceding {float(conceded_3):.2f}/game over their last 3"
        if conceded_5 is not None:
            text += f" ({float(conceded_5):.2f} over 5)"
        parts.append(text)
    if rank is not None:
        rank_int = int(rank)
        suffix = "th" if 10 <= rank_int % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(rank_int % 10, "th")
        parts.append(f"{rank_int}{suffix}-meanest defence in the league on that measure")
    if scored_3 is not None:
        parts.append(f"scoring {float(scored_3):.2f}/game")
    return "; ".join(parts) if parts else ""


def _depth_chart_line(metadata: dict) -> str:
    """Same-position team-mates and their availability (E17).

    Added for Wes's Konsa case: Konsa carried a cold-start P(app) of 0.74
    while Saliba sat injured, and NOTHING in the prompt could say so. His
    GW5 prompt mentioned none of Saliba, Mosquera, Gabriel, Timber,
    Calafiori or White, because evidence windows are mention-centered — an
    article about Saliba attaches to Saliba's prompt, never Konsa's.

    This is also why four earlier regex team-context attempts failed: they
    tried to recover from prose something that ships as a structured status
    field. Built from the official feed, so it is deterministic and
    chrono-legal (pre-deadline snapshot only).
    """
    teammates = metadata.get("depth_chart") or []
    if not teammates:
        return ""
    lines = []
    for mate in teammates[:8]:
        name = mate.get("name")
        if not name:
            continue
        bits = []
        status = str(mate.get("status") or "a").lower()
        if status != "a":
            label = {"i": "INJURED", "d": "doubtful", "s": "suspended", "u": "unavailable"}.get(status, status)
            chance = mate.get("chance_of_playing")
            bits.append(f"{label}{'' if chance is None else f' ({int(chance)}% chance)'}")
            news = (mate.get("news") or "").strip()
            if news:
                bits.append(news)
        else:
            bits.append("available")
        minutes = mate.get("minutes_avg_3")
        if minutes is not None:
            bits.append(f"{float(minutes):.0f} min/game last 3")
        lines.append(f"  - {name}: " + ", ".join(bits))
    return "\n".join(lines)



_DECOMP_LABELS = {
    "intercept": "league-avg base",
    "recent_form": "form",
    "minutes": "minutes",
    "attack_threat": "attack",
    "defence": "defence",
    "team_vs_opponent": "team/opp",
    "fixture_context": "fixture",
    "market": "market",
    "status_flags": "status",
}


def _decomposition_line(metadata: dict[str, Any]) -> str:
    """Exact additive breakdown of the classic 1GW forecast (ridge is linear),
    e.g. 'league-average base 2.1; recent form +1.4; minutes/starts +0.6'.
    Near-zero groups are dropped to save tokens."""
    decomposition = metadata.get("baseline_decomposition") or {}
    if not decomposition:
        return ""
    parts: list[str] = []
    for key, label in _DECOMP_LABELS.items():
        value = decomposition.get(key)
        if value is None:
            continue
        if key == "intercept":
            parts.append(f"{label} {float(value):.1f}")
        elif abs(float(value)) >= 0.1:
            parts.append(f"{label} {float(value):+.1f}")
    return "; ".join(parts)


def _role_line(metadata: dict[str, Any]) -> str:
    """Recent starting pattern vs usual role, with a fragility read, e.g.
    'started 100% of last 3 GWs (84 min/GW) vs 45% over 8 — recently promoted;
    spot at risk if a regular returns'. Lets the model connect returning
    players (status/news, post-break flags) to minutes risk."""
    role = metadata.get("role_context") or {}
    if not role:
        return ""
    app_3 = float(role.get("app_3") or 0.0)
    app_8 = float(role.get("app_8") or 0.0)
    minutes_3 = float(role.get("minutes_3") or 0.0)
    base = f"L3 starts {app_3:.0%} ({minutes_3:.0f} min/GW), L8 {app_8:.0%}"
    if app_8 >= 0.85 and app_3 >= 0.67:
        read = "nailed starter"
    elif app_3 - app_8 >= 0.25:
        read = "recently promoted; spot at risk if a regular returns"
    elif app_8 - app_3 >= 0.25:
        read = "losing his spot"
    elif app_8 >= 0.4:
        read = "rotation risk"
    else:
        read = "fringe player"
    return f"{base} — {read}"


def _role_prompt_line(metadata: dict[str, Any]) -> str:
    role_line = _role_line(metadata)
    return f"\n- Recent role: {role_line}" if role_line else ""


def _defcon_prompt_line(metadata: dict[str, Any]) -> str:
    """Surface the defensive-contribution signal (invisible to the adapter
    before E11 — spot-checked 2026-08-21: no numeric DefCon input existed
    anywhere in the prompt, and both E9/E10 were measurably worse than
    classic on DefCon-bonus weeks). Rendered only for DefCon-era rows
    (2025-26+); absence == the rule didn't exist, matching reality."""
    defcon = metadata.get("defcon") or {}
    if not defcon.get("tracked"):
        return ""
    return (
        f"\n- Defensive contribution (rule since 2025-26: +2 pts at 10+ for DEF, 12+ for MID/FWD, per match): "
        f"L3 avg {defcon.get('avg_3', 0):.1f}/GW, L5 avg {defcon.get('avg_5', 0):.1f}/GW"
    )


def _market_prompt_line(metadata: dict[str, Any]) -> str:
    """E13a: price + crowd ownership. The adapter's learned shrink was
    band-unconditional (GW2 2026-27: it cut Haaland exactly like one-game
    wonders; premium band −2.19 vs realized WITH the adapter) because
    nothing in the prompt distinguished a £15.5m 60%-owned premium from a
    £4.5m unknown. Both values are deadline-time facts (chrono-legal)."""
    market = metadata.get("market") or {}
    if not market:
        return ""
    return (
        f"\n- Market: £{market.get('price', 0):.1f}m, "
        f"owned by {market.get('selected_by_percent', 0):.1f}% of managers"
    )


def _congestion_line(metadata: dict[str, Any]) -> str:
    """e.g. 'UCL match 3d before this GW; UCL match 3d after; 16d since last PL match (post-break)'."""
    congestion = metadata.get("congestion") or {}
    parts: list[str] = []
    competition = congestion.get("euro_competition")
    if competition and congestion.get("euro_days_before_gw") is not None:
        parts.append(f"{competition} match {congestion['euro_days_before_gw']}d before this GW (fatigue risk)")
    if competition and congestion.get("euro_days_after_gw") is not None:
        parts.append(f"{competition} match {congestion['euro_days_after_gw']}d after this GW (rotation risk)")
    days_since = congestion.get("days_since_last_pl")
    if days_since is not None and days_since >= 13:
        parts.append(f"{days_since}d since last PL match (first GW after a break)")
    return "; ".join(parts)


def _build_user_prompt(
    metadata: dict[str, Any],
    documents: list[dict[str, Any]],
    max_docs: int,
    max_chars: int,
    clip_text: str,
    no_evidence: bool,
    include_fixtures: bool,
    include_congestion: bool = False,
    include_provenance: bool = False,
    include_decomposition: bool = False,
    include_role: bool = False,
    compact_context: bool = False,
    prefer_scout: bool = False,
    preferred_chars: int = 800,
    include_defcon: bool = False,
    include_market: bool = False,
) -> str:
    baseline = metadata["baseline_forecast"]
    if documents:
        evidence_block = _evidence_lines(
            documents, max_docs=max_docs, max_chars=max_chars,
            prefer_scout=prefer_scout, preferred_chars=preferred_chars,
            player_name=str(metadata.get("player_name") or ""),
        )
    else:
        evidence_block = (
            "No timestamp-safe text evidence is available for this player-week. "
            "Without evidence, prefer deltas at or near zero."
        )
    id_lines = "" if compact_context else f"""
- Player ID: {metadata.get('player_id')}
- Team ID: {metadata.get('team_id')}"""
    body = f"""Player context:
- Season: {metadata.get('season')}
- Gameweek: {metadata.get('week')}
- Deadline: {metadata.get('deadline_ts')}
- Player: {metadata.get('player_name')}{id_lines}
- Position: {metadata.get('position')}
- Status pre-deadline: {metadata.get('status_pre_deadline') or 'none'}
- Official player news pre-deadline: {metadata.get('news_pre_deadline') or 'none'}{_role_prompt_line(metadata) if include_role else ''}{_defcon_prompt_line(metadata) if include_defcon else ''}{_market_prompt_line(metadata) if include_market else ''}

Classic ML signal (statistical forecast from structured pre-deadline features):
{json.dumps(baseline, indent=2)}
"""
    if include_decomposition:
        decomposition_line = _decomposition_line(metadata)
        if decomposition_line:
            body += f"""
Classic 1GW forecast composition (additive, exact):
{decomposition_line}
"""
    if include_provenance:
        provenance = (
            BASELINE_PROVENANCE_TEXT_V17
            if os.environ.get("FPL_PROMPT_V17", "0") == "1"
            else BASELINE_PROVENANCE_TEXT
        )
        body += f"""
Baseline provenance:
{provenance}
"""
    if os.environ.get("FPL_PROMPT_V17", "0") == "1":
        opponent_line = _opponent_record_line(metadata)
        if opponent_line:
            body += f"""
Opponent recent record (the anchor under-weights this — see provenance):
{opponent_line}
"""
        depth_line = _depth_chart_line(metadata)
        if depth_line:
            body += f"""
Positional depth chart (team-mates competing for this player's place):
{depth_line}
"""
    if include_fixtures:
        fixture_line = _fixture_outlook_line(metadata)
        if fixture_line:
            body += f"""
Fixture outlook (team schedule, diff 1=easiest to 5=hardest):
{fixture_line}
"""
    if include_congestion:
        congestion_line = _congestion_line(metadata)
        if congestion_line:
            body += f"""
Squad-rotation context (other competitions and breaks):
{congestion_line}
"""
    if no_evidence:
        header = (
            "Forecast this player's post-deadline FPL outcomes. You are the forecaster; the classic ML signal below "
            "is one statistical input alongside the structured player context. Express your forecast as bounded "
            "deltas to add to the ML signal.\n\n"
            f"Delta bounds (values outside are clipped): {clip_text}.\n"
            "Use deltas at or near zero when the context gives no clear reason to move.\n\n"
        )
    else:
        body += f"""
Timestamp-safe text evidence:
{evidence_block}
"""
        header = (
            "Forecast this player's post-deadline FPL outcomes. You are the forecaster; the classic ML signal below is "
            "one statistical input, and the text evidence tells you what it cannot see (injuries, rotation, form "
            "context, tactical changes). Express your forecast as bounded deltas to add to the ML signal.\n\n"
            f"Delta bounds (values outside are clipped): {clip_text}.\n"
            "Use deltas at or near zero when the evidence gives no clear reason to move.\n\n"
        )
    return (
        header
        + "Return exactly one JSON object, no prose/markdown/extra text, with numeric fields:\n"
        "- \"delta_points_1gw\"\n"
        "- \"delta_points_3gw\"\n"
        "- \"delta_points_5gw\"\n"
        "- \"delta_minutes_1gw\"\n"
        "- \"delta_appearance_probability\"\n\n"
        "Example:\n"
        "{\"delta_points_1gw\": -0.5, \"delta_points_3gw\": 1.2, \"delta_points_5gw\": 2.0, "
        "\"delta_minutes_1gw\": -8, \"delta_appearance_probability\": -0.1}\n\n"
        + body
    )


def _to_residual_row(
    row: dict[str, Any],
    clip_scale: float,
    shrink: float,
    max_docs: int,
    max_chars: int,
    keep_full_metadata: bool,
    no_evidence: bool,
    include_fixtures: bool,
    include_congestion: bool = False,
    include_provenance: bool = False,
    include_decomposition: bool = False,
    include_role: bool = False,
    compact_context: bool = False,
    prefer_scout: bool = False,
    preferred_chars: int = 800,
    include_defcon: bool = False,
    include_market: bool = False,
) -> dict[str, Any]:
    metadata = dict(row["metadata"])
    documents = [] if no_evidence else _clean_evidence_documents(metadata)
    baseline = metadata["baseline_forecast"]
    labels = metadata["labels"]

    deltas: dict[str, float] = {}
    unclipped: dict[str, float] = {}
    for delta_key, (baseline_key, label_key, clip_abs, digits) in DELTA_SPECS.items():
        base_value = float(baseline.get(baseline_key) or 0.0)
        label_value = float(labels.get(label_key) or 0.0)
        raw_delta = label_value - base_value
        bound = clip_abs * clip_scale
        shrunk = raw_delta * shrink
        deltas[delta_key] = _round_delta(max(-bound, min(bound, shrunk)), digits)
        unclipped[delta_key] = round(raw_delta, 4)

    clip_text = ", ".join(
        f"{key} in [-{spec[2] * clip_scale:g}, {spec[2] * clip_scale:g}]"
        for key, spec in DELTA_SPECS.items()
    )

    if no_evidence:
        system = (
            "You are an FPL player forecaster. You refine a classic ML statistical signal using structured "
            "pre-deadline player context and output bounded forecast deltas as strict JSON. No hidden reasoning, "
            "no extra text."
        )
    else:
        system = (
            "You are an FPL player forecaster. You combine a classic ML statistical signal with pre-deadline text "
            "evidence and output bounded forecast deltas as strict JSON. No hidden reasoning, no extra text."
        )
    user = _build_user_prompt(
        metadata,
        documents,
        max_docs=max_docs,
        max_chars=max_chars,
        clip_text=clip_text,
        no_evidence=no_evidence,
        include_fixtures=include_fixtures,
        include_congestion=include_congestion,
        include_provenance=include_provenance,
        include_decomposition=include_decomposition,
        include_role=include_role,
        include_defcon=include_defcon,
        include_market=include_market,
        compact_context=compact_context,
        prefer_scout=prefer_scout,
        preferred_chars=preferred_chars,
    )
    prompt = (
        f"<|turn>system\n{system}<|turn>\n<|turn>user\n{user}<|turn>\n<|turn>model\n"
    )
    completion = json.dumps(deltas, ensure_ascii=False, separators=(",", ":"))

    out_metadata = {
        "season": metadata.get("season"),
        "week": metadata.get("week"),
        "deadline_ts": metadata.get("deadline_ts"),
        "player_id": metadata.get("player_id"),
        "player_name": metadata.get("player_name"),
        "team_id": metadata.get("team_id"),
        "position": metadata.get("position"),
        "baseline_forecast": baseline,
        "labels": labels,
        "residual_labels_clipped": deltas,
        "residual_labels_unclipped": unclipped,
        "evidence_present": bool(documents),
        "evidence_document_count": len(documents),
    }
    if keep_full_metadata:
        out_metadata["evidence_documents"] = documents

    return {
        "season": row["season"],
        "week": row["week"],
        "deadline_ts": row["deadline_ts"],
        "prompt": prompt,
        "completion": completion,
        "metadata": out_metadata,
    }


def _select_top_per_week(rows: list[dict[str, Any]], top_n: int) -> list[dict[str, Any]]:
    by_week: dict[tuple[str, int], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_week[(str(row["season"]), int(row["week"]))].append(row)

    selected: list[dict[str, Any]] = []
    for key in sorted(by_week, key=lambda item: season_week_key(item[0], item[1])):
        ranked = sorted(by_week[key], key=_baseline_score, reverse=True)
        selected.extend(ranked[:top_n] if top_n > 0 else ranked)
    return selected


def _counts(rows: Iterable[dict[str, Any]]) -> dict[str, int]:
    return {
        f"{season}:{week}": count
        for (season, week), count in sorted(
            Counter((str(row["season"]), int(row["week"])) for row in rows).items(),
            key=lambda item: season_week_key(item[0][0], item[0][1]),
        )
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--corpus", required=True, type=Path, help="Flat corpus JSONL from export-llm-player-forecast-corpus.")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--train-through", required=True, help="Chronological train cutoff, e.g. 2025-26:11 (inclusive).")
    parser.add_argument("--eval-weeks", required=True, help="Eval season-weeks, e.g. 2025-26:12-30.")
    parser.add_argument("--top-n", type=int, default=128, help="Top-N players per season-week by baseline score; <=0 keeps all.")
    parser.add_argument("--clip-scale", type=float, default=1.0, help="Multiplier on default clip bounds (E3 sweeps this).")
    parser.add_argument(
        "--shrink",
        type=float,
        default=0.35,
        help="Shrinkage on raw realized deltas before clipping; targets the expected component of a noisy delta (E3 sweeps this).",
    )
    parser.add_argument("--max-evidence-docs", type=int, default=2)
    parser.add_argument("--max-evidence-chars", type=int, default=260)
    parser.add_argument("--keep-full-metadata", action="store_true", help="Keep evidence documents in output metadata (larger files).")
    parser.add_argument(
        "--include-fixtures",
        action="store_true",
        help="Render metadata.fixture_outlook (from attach_fixture_outlook_to_corpus.py) as a schedule block.",
    )
    parser.add_argument(
        "--include-congestion",
        action="store_true",
        help="Render metadata.congestion (from attach_congestion_to_corpus.py): Euro-match proximity and post-break flags.",
    )
    parser.add_argument(
        "--include-provenance",
        action="store_true",
        help="State what the classic baseline already prices in vs its blind spots, to prevent double-counting.",
    )
    parser.add_argument(
        "--include-decomposition",
        action="store_true",
        help="Render metadata.baseline_decomposition (from attach_baseline_decomposition_to_corpus.py): exact additive breakdown of the classic 1GW forecast.",
    )
    parser.add_argument(
        "--include-defcon",
        action="store_true",
        help="Render metadata.defcon (from attach_defcon_to_corpus.py): lagged defensive-contribution averages, DefCon-era rows only.",
    )
    parser.add_argument(
        "--include-role",
        action="store_true",
        help="Render metadata.role_context (from attach_role_context_to_corpus.py): recent vs usual starter pattern with a fragility read.",
    )
    parser.add_argument(
        "--include-market",
        action="store_true",
        help="Render metadata.market (from attach_market_to_corpus.py): price + selected-by%% — E13a band-conditioning inputs.",
    )
    parser.add_argument(
        "--compact-context",
        action="store_true",
        help="Omit numeric Player ID / Team ID prompt lines (useless to the model; saves ~20 tokens).",
    )
    parser.add_argument(
        "--prefer-scout",
        action="store_true",
        help="Rank scout-report/preview-genre evidence first (title match: scout report/team news/predicted line/preview/tips) and give it --preferred-chars.",
    )
    parser.add_argument("--preferred-chars", type=int, default=800)
    parser.add_argument(
        "--no-evidence",
        action="store_true",
        help="E1 mode: structured features only; omit the text-evidence section from prompts entirely.",
    )
    parser.add_argument("--require-baseline", action="store_true", default=True)
    parser.add_argument(
        "--allow-empty-eval",
        action="store_true",
        help="Permit an empty eval split (deployment/consolidation builds that train on every available week; pair with FPL_GEMMA_EVAL_STRATEGY=no).",
    )
    args = parser.parse_args()

    train_cutoff = _parse_cutoff(args.train_through)
    eval_keys = _parse_eval_weeks(args.eval_weeks)
    if any(key <= train_cutoff for key in eval_keys):
        raise ValueError("Eval weeks must be strictly after the train cutoff.")

    train_candidates: list[dict[str, Any]] = []
    eval_candidates: list[dict[str, Any]] = []
    skipped_no_baseline = 0
    for row in _load_jsonl(args.corpus):
        key = season_week_key(str(row["season"]), int(row["week"]))
        baseline = (row.get("metadata") or {}).get("baseline_forecast") or {}
        if not baseline or all(not value for value in baseline.values()):
            # First weeks of the earliest season have no strictly-prior data to
            # fit a baseline on; the residual task is undefined there.
            skipped_no_baseline += 1
            continue
        if key <= train_cutoff:
            train_candidates.append(row)
        elif key in eval_keys:
            eval_candidates.append(row)

    train_rows = [
        _to_residual_row(row, args.clip_scale, args.shrink, args.max_evidence_docs, args.max_evidence_chars, args.keep_full_metadata, args.no_evidence, args.include_fixtures, args.include_congestion, args.include_provenance, args.include_decomposition, args.include_role, args.compact_context, args.prefer_scout, args.preferred_chars, include_defcon=args.include_defcon, include_market=args.include_market)
        for row in _select_top_per_week(train_candidates, args.top_n)
    ]
    eval_rows = [
        _to_residual_row(row, args.clip_scale, args.shrink, args.max_evidence_docs, args.max_evidence_chars, args.keep_full_metadata, args.no_evidence, args.include_fixtures, args.include_congestion, args.include_provenance, args.include_decomposition, args.include_role, args.compact_context, args.prefer_scout, args.preferred_chars, include_defcon=args.include_defcon, include_market=args.include_market)
        for row in _select_top_per_week(eval_candidates, args.top_n)
    ]
    if args.allow_empty_eval and not eval_rows:
        pass  # consolidation builds train on ALL data; eval seeded separately
    elif not train_rows or not eval_rows:
        raise ValueError(f"No rows selected (train={len(train_rows)}, eval={len(eval_rows)}).")

    train_count = _write_jsonl(args.output_dir / "train.jsonl", train_rows)
    eval_count = _write_jsonl(args.output_dir / "eval.jsonl", eval_rows)

    evidence_train = sum(1 for row in train_rows if row["metadata"]["evidence_present"])
    evidence_eval = sum(1 for row in eval_rows if row["metadata"]["evidence_present"])
    summary = {
        "corpus": str(args.corpus),
        "output_dir": str(args.output_dir),
        "task": "player_forecast_residual_delta_clipped_v2"
        + ("_structured_only" if args.no_evidence else ""),
        "no_evidence": args.no_evidence,
        "include_fixtures": args.include_fixtures,
        "include_congestion": args.include_congestion,
        "include_provenance": args.include_provenance,
        "include_decomposition": args.include_decomposition,
        "include_role": args.include_role,
        "compact_context": args.compact_context,
        "prefer_scout": args.prefer_scout,
        "preferred_chars": args.preferred_chars,
        "train_through": args.train_through,
        "eval_weeks": args.eval_weeks,
        "top_n": args.top_n,
        "clip_scale": args.clip_scale,
        "shrink": args.shrink,
        "clip_bounds": {key: spec[2] * args.clip_scale for key, spec in DELTA_SPECS.items()},
        "skipped_no_baseline": skipped_no_baseline,
        "train_count": train_count,
        "eval_count": eval_count,
        "train_evidence_present": evidence_train,
        "eval_evidence_present": evidence_eval,
        "train_counts_by_week": _counts(train_rows),
        "eval_counts_by_week": _counts(eval_rows),
    }
    (args.output_dir / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({key: value for key, value in summary.items() if "counts_by_week" not in key}, indent=2))


if __name__ == "__main__":
    main()

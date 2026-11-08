"""F15 news horizon (2026-10-14): how many of the coming gameweeks the official news text says a player misses.

The pre-deadline news field is structured: "Hamstring injury - Expected back 11 Jan", "Suspended until 04 Dec",
"Ankle injury - 75% chance of playing", "Knee injury - Unknown return date", "Loaned to Stoke City". The binary
status flag already prices THIS week; the 3- and 5-week heads, which drive transfers, have never seen a return
date. Features per player-week (FPL_NEWS_HORIZON=1):
  out_weeks_3 / out_weeks_5   gameweeks among the next 3 / 5 (this one included) whose first kickoff falls before
                              the stated return date; status u/n (left the club, ineligible) count as all of them
  return_known                1 when the news carries a date
  unknown_return              1 when the status is i/s/n/u and no date is given (open-ended absence)
Dates carry no year, so the year is taken relative to the snapshot: a month earlier than the snapshot's is next year.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta, timezone
from typing import Iterable, List, Optional, Sequence

import pandas as pd

FEATURES = ["out_weeks_3", "out_weeks_5", "return_known", "unknown_return"]
DATE_RE = re.compile(r"(?:Expected back|Suspended until|until|back on)\s+(\d{1,2})\s*(?:/|\s)?\s*([A-Za-z]{3,9}|\d{1,2})\b", re.IGNORECASE)
MONTHS = {m.lower(): i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}
GONE = {"u", "n"}
ABSENT = {"i", "s", "n", "u"}


def parse_return_date(news: str, reference: Optional[datetime]) -> Optional[datetime]:
    """The return date named in the news, as a UTC datetime, or None."""
    if not isinstance(news, str) or not news or reference is None or pd.isna(reference):
        return None
    match = DATE_RE.search(news)
    if not match:
        return None
    day = int(match.group(1))
    month_text = match.group(2).lower()
    month = MONTHS.get(month_text[:3]) if not month_text.isdigit() else int(month_text)
    if not month or not 1 <= month <= 12 or not 1 <= day <= 31:
        return None
    year = reference.year
    if month < reference.month - 1:   # a month well before the snapshot's month means next year
        year += 1
    try:
        return datetime(year, month, day, tzinfo=timezone.utc)
    except ValueError:
        return None


def horizon_features(status: str, news: str, reference: Optional[datetime], kickoffs: Sequence[Optional[datetime]]) -> List[float]:
    """[out_weeks_3, out_weeks_5, return_known, unknown_return] for one row.

    kickoffs = first kickoff of this week and the following ones (at least 5 entries; None when unknown)."""
    letter = (status or "").strip().lower()
    if letter in GONE:
        return [3.0, 5.0, 0.0, 1.0]
    back = parse_return_date(news, reference)
    out = [0.0, 0.0, 1.0 if back is not None else 0.0, 1.0 if (letter in ABSENT and back is None) else 0.0]
    if back is None:
        return out
    for horizon, slot in ((3, 0), (5, 1)):
        count = 0
        for kickoff in list(kickoffs)[:horizon]:
            if kickoff is None or pd.isna(kickoff):
                continue
            if back > kickoff:
                count += 1
        out[slot] = float(count)
    return out


def add_news_horizon(player_week: pd.DataFrame) -> pd.DataFrame:
    """Training path: per (season, week) first kickoff from the frame itself, then the row features."""
    kick = pd.to_datetime(player_week["kickoff_time"], errors="coerce", utc=True)
    first = kick.groupby([player_week["season"], player_week["week"]]).min()
    first_by_key = {(s, int(w)): t for (s, w), t in first.items()}
    reference = kick.fillna(pd.Series([first_by_key.get((s, int(w))) for s, w in zip(player_week["season"], player_week["week"])],
                                      index=player_week.index))
    rows = []
    for season, week, status, news, ref in zip(player_week["season"], player_week["week"], player_week.get("status_pre_deadline"),
                                               player_week.get("news_pre_deadline"), reference):
        kickoffs = [first_by_key.get((season, int(week) + k)) for k in range(5)]
        rows.append(horizon_features(status, news, ref.to_pydatetime() if pd.notna(ref) else None, kickoffs))
    frame = pd.DataFrame(rows, columns=FEATURES, index=player_week.index)
    for column in FEATURES:
        player_week[column] = frame[column].astype(float)
    return player_week


def live_news_horizon(status: pd.Series, news: pd.Series, deadline: datetime, kickoffs: Sequence[Optional[datetime]]) -> pd.DataFrame:
    """Live path: the same features from the snapshot's status/news, the deadline and the next kickoffs."""
    rows = [horizon_features(s, n, deadline, kickoffs) for s, n in zip(status, news)]
    return pd.DataFrame(rows, columns=FEATURES, index=status.index)

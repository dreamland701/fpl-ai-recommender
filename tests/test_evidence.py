import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.evidence import build_evidence_snapshot, build_evidence_snapshot_from_path
from fpl_ai.service import FPLRecommender
from fpl_ai.types import WeekEligibility, WeekState


class FakeSnapshotService:
    def build_week_state(self, deadline_ts: str) -> WeekState:
        return WeekState(
            season="2025-26",
            week=30,
            deadline_ts=deadline_ts,
            eligible=WeekEligibility(
                season="2025-26",
                week=30,
                eligible_for_training=True,
                eligible_for_backtest=True,
                reason="ok",
            ),
            fixture_count=10,
            player_count=600,
            notes=[],
            source_timestamps={},
        )


class EvidenceSnapshotTestCase(unittest.TestCase):
    def test_build_evidence_snapshot_aggregates_player_and_team_mentions(self):
        frame = pd.DataFrame(
            [
                {
                    "title": "Official update",
                    "url": "https://www.premierleague.com/news/1",
                    "source_name": "Premier League",
                    "category": "official_premier_league",
                    "published_at": "2025-08-15T10:00:00Z",
                    "snippet": "Saka trained.",
                    "content": "Saka trained fully.",
                    "player_name": "Bukayo Saka",
                    "team_name": "Arsenal",
                    "published_ts": pd.Timestamp("2025-08-15T10:00:00Z"),
                },
                {
                    "title": "Reddit thread",
                    "url": "https://www.reddit.com/r/FantasyPL/comments/abc",
                    "source_name": "r/FantasyPL",
                    "category": "reddit",
                    "published_at": "2025-08-15T11:00:00Z",
                    "snippet": "Likely start.",
                    "content": "Multiple users think Saka starts.",
                    "player_name": "Bukayo Saka",
                    "team_name": "Arsenal",
                    "published_ts": pd.Timestamp("2025-08-15T11:00:00Z"),
                },
                {
                    "title": "Too late",
                    "url": "https://www.premierleague.com/news/2",
                    "source_name": "Premier League",
                    "category": "official_premier_league",
                    "published_at": "2025-08-17T11:31:00Z",
                    "snippet": "After deadline.",
                    "content": "Ignore.",
                    "player_name": "Bukayo Saka",
                    "team_name": "Arsenal",
                    "published_ts": pd.Timestamp("2025-08-17T11:31:00Z"),
                },
            ]
        )

        snapshot = build_evidence_snapshot(
            season="2025-26",
            week=2,
            deadline_ts="2025-08-16T11:30:00Z",
            evidence_frame=frame,
            max_documents=5,
            lookback_days=3,
        )

        self.assertEqual(snapshot.document_count, 2)
        self.assertEqual(snapshot.source_counts["Premier League"], 1)
        self.assertEqual(snapshot.source_counts["r/FantasyPL"], 1)
        self.assertEqual(snapshot.player_summaries[0].entity_name, "Bukayo Saka")
        self.assertEqual(snapshot.player_summaries[0].document_count, 2)
        self.assertEqual(snapshot.team_summaries[0].entity_name, "Arsenal")
        self.assertTrue(any("low-trust Reddit" in note for note in snapshot.notes))

    def test_build_evidence_snapshot_from_path_filters_to_curated_sources(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "evidence.json"
            path.write_text(
                json.dumps(
                    [
                        {
                            "title": "Official update",
                            "url": "https://www.premierleague.com/news/123",
                            "source_name": "Premier League",
                            "category": "official_premier_league",
                            "published_at": "2025-08-15T10:00:00Z",
                            "snippet": "Team news",
                            "player_name": "Cole Palmer",
                            "team_name": "Chelsea",
                        },
                        {
                            "title": "Unknown source",
                            "url": "https://example.com/post",
                            "source_name": "Example",
                            "category": "blog",
                            "published_at": "2025-08-15T11:00:00Z",
                            "snippet": "Ignore me too",
                            "player_name": "Cole Palmer",
                            "team_name": "Chelsea",
                        },
                    ]
                )
            )
            snapshot = build_evidence_snapshot_from_path(
                season="2025-26",
                week=2,
                deadline_ts="2025-08-16T11:30:00Z",
                input_path=str(path),
            )

        self.assertEqual(snapshot.document_count, 1)
        self.assertEqual(snapshot.documents[0].title, "Official update")

    def test_recommender_build_evidence_snapshot_uses_deadline_week_state(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "evidence.json"
            path.write_text(
                json.dumps(
                    [
                        {
                            "title": "Official update",
                            "url": "https://www.premierleague.com/news/123",
                            "source_name": "Premier League",
                            "category": "official_premier_league",
                            "published_at": "2025-08-15T10:00:00Z",
                            "snippet": "Team news",
                        }
                    ]
                )
            )
            recommender = FPLRecommender(snapshot_service=FakeSnapshotService())
            snapshot = recommender.build_evidence_snapshot(
                deadline_ts="2025-08-16T11:30:00Z",
                evidence_path=str(path),
            )

        self.assertEqual(snapshot.season, "2025-26")
        self.assertEqual(snapshot.week, 30)
        self.assertEqual(snapshot.document_count, 1)


if __name__ == "__main__":
    unittest.main()

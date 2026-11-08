import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.dataset import CanonicalDataset, build_training_frame
from fpl_ai.llm_data import (
    EvidenceRecord,
    _transfer_choice_prompt,
    build_decision_sft_examples,
    normalize_evidence_corpus,
    select_evidence_for_deadline,
)
from tests.test_dataset import synthetic_raw_history


class LLMDataTestCase(unittest.TestCase):
    def test_normalize_evidence_filters_to_curated_and_valid_timestamps(self):
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
                        },
                        {
                            "title": "Bad timestamp",
                            "url": "https://www.bbc.com/sport/football/xyz",
                            "source_name": "BBC",
                            "category": "trusted_news",
                            "published_at": "not-a-date",
                            "snippet": "Ignore me",
                        },
                        {
                            "title": "Unknown source",
                            "url": "https://example.com/post",
                            "source_name": "Example",
                            "category": "blog",
                            "published_at": "2025-08-15T11:00:00Z",
                            "snippet": "Ignore me too",
                        },
                    ]
                )
            )
            frame = normalize_evidence_corpus(str(path))
        self.assertEqual(len(frame), 1)
        self.assertEqual(frame.iloc[0]["title"], "Official update")

    def test_select_evidence_for_deadline_excludes_future_documents(self):
        frame = pd.DataFrame(
            [
                {
                    "title": "Before deadline",
                    "url": "https://www.premierleague.com/news/123",
                    "source_name": "Premier League",
                    "category": "official_premier_league",
                    "published_at": "2025-08-15T10:00:00Z",
                    "snippet": "Good",
                    "content": "",
                    "published_ts": pd.Timestamp("2025-08-15T10:00:00Z"),
                },
                {
                    "title": "After deadline",
                    "url": "https://www.premierleague.com/news/124",
                    "source_name": "Premier League",
                    "category": "official_premier_league",
                    "published_at": "2025-08-17T10:00:00Z",
                    "snippet": "Too late",
                    "content": "",
                    "published_ts": pd.Timestamp("2025-08-17T10:00:00Z"),
                },
            ]
        )
        docs = select_evidence_for_deadline(
            frame,
            deadline_ts="2025-08-16T11:30:00Z",
            max_documents=5,
            lookback_days=3,
        )
        self.assertEqual([doc.title for doc in docs], ["Before deadline"])

    def test_normalize_evidence_filters_outcome_recap_articles_with_bad_timestamps(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "evidence.json"
            path.write_text(
                json.dumps(
                    [
                        {
                            "title": "Who's got FPL defensive contribution points in Gameweek 5? - Premier League",
                            "url": "https://www.premierleague.com/en/news/defensive-contribution-gw5",
                            "source_name": "Premier League",
                            "category": "official_scout",
                            "published_at": "2025-09-20T07:00:00Z",
                            "snippet": "See all the players who have picked up two extra FPL points so far in this Gameweek",
                            "content": "Defensive contributions are subject to change up until one hour after the final whistle.",
                        },
                        {
                            "title": "Scout Selection: Best Fantasy team for Gameweek 5 - Premier League",
                            "url": "https://www.premierleague.com/en/news/scout-selection-gw5",
                            "source_name": "Premier League",
                            "category": "official_scout",
                            "published_at": "2025-09-19T07:00:00Z",
                            "snippet": "The Scout picks the best team before the deadline.",
                            "content": "This article discusses captaincy, fixtures and transfer targets.",
                        },
                    ]
                )
            )

            frame = normalize_evidence_corpus(str(path))

        self.assertEqual([row["title"] for row in frame.to_dict(orient="records")], ["Scout Selection: Best Fantasy team for Gameweek 5 - Premier League"])

    def test_normalize_evidence_accepts_reddit_archive_shape(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "reddit.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "title": "Saka injury thread",
                        "selftext": "Saka is reportedly back in training before the FPL deadline.",
                        "permalink": "/r/FantasyPL/comments/abc/saka_injury_thread/",
                        "subreddit": "FantasyPL",
                        "created_utc": 1779019200,
                    }
                )
                + "\n"
            )

            frame = normalize_evidence_corpus(str(path))

        self.assertEqual(len(frame), 1)
        self.assertEqual(frame.iloc[0]["category"], "reddit")
        self.assertEqual(frame.iloc[0]["source_name"], "r/FantasyPL")
        self.assertTrue(frame.iloc[0]["url"].startswith("https://www.reddit.com/r/FantasyPL/"))

    def test_normalize_evidence_corpus_accepts_directory_input(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "one.json").write_text(
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
            (root / "nested").mkdir()
            (root / "nested" / "two.jsonl").write_text(
                json.dumps(
                    {
                        "title": "BBC update",
                        "url": "https://www.bbc.com/sport/football/xyz",
                        "source_name": "BBC",
                        "category": "trusted_news",
                        "published_at": "2025-08-15T11:00:00Z",
                        "snippet": "Another note",
                    }
                )
                + "\n"
            )
            frame = normalize_evidence_corpus(str(root))

        self.assertEqual(len(frame), 2)
        self.assertEqual(set(frame["source_name"]), {"Premier League", "BBC"})

    def test_build_decision_sft_examples_exports_messages_and_metadata(self):
        dataset = CanonicalDataset(build_training_frame(synthetic_raw_history()))
        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = Path(tmpdir) / "backtest.json"
            report_path.write_text(
                json.dumps(
                    {
                        "weeks": [
                            {
                                "season": "2025-26",
                                "week": 4,
                                "bank_before": 0.5,
                                "bank_after": 0.7,
                                "free_transfers_before": 1,
                                "free_transfers_after": 2,
                                "transfers_applied": [],
                                "chip_used": "none",
                                "chip_reason": "",
                                "chip_advisories": [],
                                "predicted_score": 55.0,
                                "actual_score": 49.0,
                                "league_average_score": 44.0,
                                "captain_name": "Mid One",
                                "vice_captain_name": "Fwd Two",
                                "effective_captain_name": "Mid One",
                                "notes": ["No transfer was applied this week."],
                                "squad": [
                                    {
                                        "player_id": 1,
                                        "player_name": "Mid One",
                                        "position": "MID",
                                        "team_id": 1,
                                        "price": 8.2,
                                        "selected_role": "Captain",
                                        "realized_role": "Captain",
                                        "predicted_points_1gw": 7.0,
                                        "predicted_points_3gw": 18.0,
                                        "predicted_points_5gw": 28.0,
                                        "actual_points_1gw": 7.0,
                                        "predicted_minutes": 88.0,
                                        "actual_minutes": 88.0,
                                        "appearance_probability": 0.95,
                                    },
                                    {
                                        "player_id": 2,
                                        "player_name": "Fwd Two",
                                        "position": "FWD",
                                        "team_id": 2,
                                        "price": 7.8,
                                        "selected_role": "Vice Captain",
                                        "realized_role": "XI",
                                        "predicted_points_1gw": 6.0,
                                        "predicted_points_3gw": 15.0,
                                        "predicted_points_5gw": 23.0,
                                        "actual_points_1gw": 9.0,
                                        "predicted_minutes": 90.0,
                                        "actual_minutes": 90.0,
                                        "appearance_probability": 0.98,
                                    },
                                ],
                            }
                        ]
                    }
                )
            )
            examples = build_decision_sft_examples(dataset, str(report_path), evidence_frame=pd.DataFrame())
        self.assertEqual(len(examples), 1)
        self.assertEqual(examples[0].season, "2025-26")
        self.assertEqual(examples[0].week, 4)
        self.assertEqual(examples[0].messages[0]["role"], "system")
        self.assertIn("Current squad before moves and model forecasts", examples[0].messages[1]["content"])
        self.assertIn("Candidate transfer shortlist", examples[0].messages[1]["content"])
        self.assertIn('"captain": "Mid One"', examples[0].messages[2]["content"])
        self.assertEqual(examples[0].metadata["team_actual_score"], 49.0)
        self.assertEqual(examples[0].metadata["current_squad_names"], ["Mid One", "Fwd Two"])

    def test_transfer_choice_prompt_uses_hybrid_prompt_schema(self):
        prompt = _transfer_choice_prompt(
            season="2025-26",
            week=11,
            deadline_ts="2025-11-01T10:00:00Z",
            week_payload={
                "bank_before": 1.5,
                "free_transfers_before": 1,
                "pre_move_squad": [
                    {
                        "player_name": "Mid One",
                        "position": "MID",
                        "price": 8.2,
                        "predicted_points_1gw": 7.0,
                        "predicted_points_3gw": 18.0,
                        "predicted_points_5gw": 28.0,
                        "predicted_minutes": 88.0,
                        "appearance_probability": 0.95,
                    }
                ],
            },
            evidence_documents=[
                EvidenceRecord(
                    title="Official update",
                    url="https://www.premierleague.com/news/123",
                    source_name="Premier League",
                    category="official_premier_league",
                    published_at="2025-10-31T09:00:00Z",
                    snippet="Player trained fully.",
                    content="",
                    player_name="Mid One",
                    team_name="Arsenal",
                )
            ],
            options=[
                {
                    "option_id": 0,
                    "players_out": [],
                    "players_in": [],
                    "predicted_score": 58.4,
                    "captain": "Mid One",
                    "vice_captain": "Fwd Two",
                    "chip": "none",
                }
            ],
        )

        self.assertIn("Current squad and structured ML forecasts:", prompt)
        self.assertIn("Evidence snapshot:", prompt)
        self.assertIn("Player evidence summaries:", prompt)
        self.assertIn("Legal candidate options from the optimizer:", prompt)
        self.assertIn("selected_option", prompt)


if __name__ == "__main__":
    unittest.main()

import unittest

from fpl_ai.hybrid import build_hybrid_decision_context
from fpl_ai.types import (
    CandidateDecisionOption,
    EvidenceDocument,
    EvidenceEntitySummary,
    EvidenceSnapshot,
    RecommendationBundle,
    SquadPlayer,
    SquadState,
    WeekEligibility,
    WeekState,
    PlayerForecast,
)


class HybridDecisionContextTestCase(unittest.TestCase):
    def test_build_hybrid_decision_context_includes_evidence_and_candidate_options(self):
        week_state = WeekState(
            season="2025-26",
            week=30,
            deadline_ts="2026-04-04T10:00:00Z",
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
        squad_state = SquadState(
            season="2025-26",
            week=30,
            squad_players=[
                SquadPlayer(8, "MID Star", 6, "MID", 12.0),
                SquadPlayer(13, "FWD One", 11, "FWD", 8.5),
            ],
            bank=1.5,
            free_transfers=1,
            chips_available={"triple_captain": True},
        )
        forecasts = [
            PlayerForecast(
                season="2025-26",
                week=30,
                player_id=8,
                player_name="MID Star",
                team_id=6,
                position="MID",
                price=12.0,
                predicted_minutes=88.0,
                predicted_points_1gw=8.4,
                predicted_points_3gw=20.0,
                predicted_points_5gw=31.0,
                appearance_probability=0.91,
                fixture_count=1,
                uncertainty=0.2,
            ),
            PlayerForecast(
                season="2025-26",
                week=30,
                player_id=13,
                player_name="FWD One",
                team_id=11,
                position="FWD",
                price=8.5,
                predicted_minutes=84.0,
                predicted_points_1gw=6.2,
                predicted_points_3gw=15.0,
                predicted_points_5gw=24.0,
                appearance_probability=0.87,
                fixture_count=1,
                uncertainty=0.25,
            ),
        ]
        evidence_snapshot = EvidenceSnapshot(
            season="2025-26",
            week=30,
            deadline_ts="2026-04-04T10:00:00Z",
            lookback_days=7,
            document_count=1,
            source_counts={"Premier League": 1},
            category_counts={"official_premier_league": 1},
            documents=[
                EvidenceDocument(
                    title="Official update",
                    url="https://www.premierleague.com/news/123",
                    source_name="Premier League",
                    category="official_premier_league",
                    published_at="2026-04-03T09:00:00Z",
                    snippet="Player trained.",
                )
            ],
            player_summaries=[
                EvidenceEntitySummary(
                    entity_type="player",
                    entity_name="MID Star",
                    document_count=1,
                    latest_published_at="2026-04-03T09:00:00Z",
                    source_names=["Premier League"],
                    categories=["official_premier_league"],
                    snippets=["Player trained."],
                )
            ],
            team_summaries=[],
            notes=["Selected 1 timestamp-safe document before the deadline."],
        )
        bundle = RecommendationBundle(
            season="2025-26",
            week=30,
            transfers=[],
            captain_id=8,
            vice_captain_id=13,
            starters=[8, 13],
            bench_order=[],
            chip_advisories=[],
            confidence=0.76,
            assumptions=[],
            supporting_sources=[],
            candidate_options=[
                CandidateDecisionOption(
                    option_id=0,
                    label="Hold squad",
                    players_out=[],
                    players_in=[],
                    players_out_names=[],
                    players_in_names=[],
                    projected_gain=0.0,
                    hit_cost=0,
                    predicted_score=14.6,
                    captain_id=8,
                    captain_name="MID Star",
                    vice_captain_id=13,
                    vice_captain_name="FWD One",
                    starters=["MID Star", "FWD One"],
                    bench_order=[],
                    chip="triple_captain",
                    chip_confidence=0.63,
                    rationale="Keep the current squad.",
                )
            ],
            evidence_snapshot=evidence_snapshot,
        )

        context = build_hybrid_decision_context(
            week_state=week_state,
            squad_state=squad_state,
            forecasts=forecasts,
            recommendation_bundle=bundle,
        )

        self.assertEqual(context.week, 30)
        self.assertEqual(len(context.candidate_options), 1)
        self.assertIn("Evidence snapshot:", context.prompt)
        self.assertIn("MID Star", context.prompt)
        self.assertIn("Legal candidate options from the optimizer:", context.prompt)
        self.assertIn("selected_option", context.prompt)


if __name__ == "__main__":
    unittest.main()

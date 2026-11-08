import unittest

from fpl_ai.decision import recommend_actions
from fpl_ai.types import EvidenceSnapshot, EvidenceDocument, PlayerForecast, SquadPlayer, SquadState


def make_forecast(player_id, name, team_id, position, price, p1, p3, p5=None, minutes=85, appearance=0.9, fixtures=1):
    return PlayerForecast(
        season="2025-26",
        week=30,
        player_id=player_id,
        player_name=name,
        team_id=team_id,
        position=position,
        price=price,
        predicted_minutes=minutes,
        predicted_points_1gw=p1,
        predicted_points_3gw=p3,
        predicted_points_5gw=p5 if p5 is not None else p3 + p1,
        appearance_probability=appearance,
        fixture_count=fixtures,
        uncertainty=0.2,
    )


class DecisionTestCase(unittest.TestCase):
    def test_recommend_actions_returns_legal_lineup_and_transfer(self):
        squad_players = [
            SquadPlayer(1, "GK One", 1, "GK", 4.5),
            SquadPlayer(2, "GK Two", 2, "GK", 4.0),
            SquadPlayer(3, "DEF One", 1, "DEF", 5.0),
            SquadPlayer(4, "DEF Weak", 2, "DEF", 4.5),
            SquadPlayer(5, "DEF Three", 3, "DEF", 4.8),
            SquadPlayer(6, "DEF Four", 4, "DEF", 4.7),
            SquadPlayer(7, "DEF Five", 5, "DEF", 4.6),
            SquadPlayer(8, "MID Star", 6, "MID", 12.0),
            SquadPlayer(9, "MID Two", 7, "MID", 8.0),
            SquadPlayer(10, "MID Three", 8, "MID", 7.5),
            SquadPlayer(11, "MID Four", 9, "MID", 6.0),
            SquadPlayer(12, "MID Five", 10, "MID", 5.5),
            SquadPlayer(13, "FWD One", 11, "FWD", 8.5),
            SquadPlayer(14, "FWD Two", 12, "FWD", 7.0),
            SquadPlayer(15, "FWD Three", 13, "FWD", 6.5),
        ]
        forecasts = [
            make_forecast(1, "GK One", 1, "GK", 4.5, 4, 11),
            make_forecast(2, "GK Two", 2, "GK", 4.0, 2, 6),
            make_forecast(3, "DEF One", 1, "DEF", 5.0, 5, 12),
            make_forecast(4, "DEF Weak", 2, "DEF", 4.5, 1, 2),
            make_forecast(5, "DEF Three", 3, "DEF", 4.8, 4, 10),
            make_forecast(6, "DEF Four", 4, "DEF", 4.7, 4, 9),
            make_forecast(7, "DEF Five", 5, "DEF", 4.6, 3, 8),
            make_forecast(8, "MID Star", 6, "MID", 12.0, 9, 24),
            make_forecast(9, "MID Two", 7, "MID", 8.0, 6, 16),
            make_forecast(10, "MID Three", 8, "MID", 7.5, 5, 14),
            make_forecast(11, "MID Four", 9, "MID", 6.0, 4, 10),
            make_forecast(12, "MID Five", 10, "MID", 5.5, 3, 7),
            make_forecast(13, "FWD One", 11, "FWD", 8.5, 7, 18),
            make_forecast(14, "FWD Two", 12, "FWD", 7.0, 5, 12),
            make_forecast(15, "FWD Three", 13, "FWD", 6.5, 2, 6),
            make_forecast(101, "DEF Upgrade", 14, "DEF", 4.9, 7, 18),
            make_forecast(102, "MID Upgrade", 15, "MID", 7.3, 6, 17),
        ]
        squad_state = SquadState(
            season="2025-26",
            week=30,
            squad_players=squad_players,
            bank=0.6,
            free_transfers=1,
            chips_available={"bench_boost": True, "wildcard": True},
        )

        bundle = recommend_actions(squad_state, forecasts)
        starter_ids = set(bundle.starters)

        self.assertEqual(len(bundle.starters), 11)
        self.assertEqual(bundle.captain_id, 8)
        self.assertEqual(len(bundle.bench_order), 4)
        self.assertTrue(bundle.transfers)
        self.assertEqual(bundle.transfers[0].players_out, [4])
        self.assertEqual(bundle.transfers[0].players_in, [101])
        self.assertNotIn(2, starter_ids)
        self.assertTrue(bundle.candidate_options)
        self.assertEqual(bundle.candidate_options[0].label, "Hold squad")
        self.assertEqual(bundle.candidate_options[1].players_in_names, ["DEF Upgrade"])

    def test_chip_advisories_surface_bench_boost_and_triple_captain_in_double_gameweek_shapes(self):
        squad_players = [
            SquadPlayer(1, "GK One", 1, "GK", 4.5),
            SquadPlayer(2, "GK Two", 2, "GK", 4.0),
            SquadPlayer(3, "DEF One", 1, "DEF", 5.0),
            SquadPlayer(4, "DEF Two", 2, "DEF", 4.5),
            SquadPlayer(5, "DEF Three", 3, "DEF", 4.8),
            SquadPlayer(6, "DEF Four", 4, "DEF", 4.7),
            SquadPlayer(7, "DEF Five", 5, "DEF", 4.6),
            SquadPlayer(8, "MID Star", 6, "MID", 12.0),
            SquadPlayer(9, "MID Two", 7, "MID", 8.0),
            SquadPlayer(10, "MID Three", 8, "MID", 7.5),
            SquadPlayer(11, "MID Four", 9, "MID", 6.0),
            SquadPlayer(12, "MID Five", 10, "MID", 5.5),
            SquadPlayer(13, "FWD One", 11, "FWD", 8.5),
            SquadPlayer(14, "FWD Two", 12, "FWD", 7.0),
            SquadPlayer(15, "FWD Three", 13, "FWD", 6.5),
        ]
        forecasts = [
            make_forecast(1, "GK One", 1, "GK", 4.5, 5, 13, fixtures=2),
            make_forecast(2, "GK Two", 2, "GK", 4.0, 4, 10, fixtures=1),
            make_forecast(3, "DEF One", 1, "DEF", 5.0, 6, 16, fixtures=2),
            make_forecast(4, "DEF Two", 2, "DEF", 4.5, 5, 14, fixtures=1),
            make_forecast(5, "DEF Three", 3, "DEF", 4.8, 5, 14, fixtures=1),
            make_forecast(6, "DEF Four", 4, "DEF", 4.7, 4, 11, fixtures=1),
            make_forecast(7, "DEF Five", 5, "DEF", 4.6, 4, 11, fixtures=1),
            make_forecast(8, "MID Star", 6, "MID", 12.0, 11, 28, fixtures=2),
            make_forecast(9, "MID Two", 7, "MID", 8.0, 7, 18, fixtures=1),
            make_forecast(10, "MID Three", 8, "MID", 7.5, 6, 15, fixtures=1),
            make_forecast(11, "MID Four", 9, "MID", 6.0, 5, 13, fixtures=1),
            make_forecast(12, "MID Five", 10, "MID", 5.5, 5, 13, fixtures=1),
            make_forecast(13, "FWD One", 11, "FWD", 8.5, 8, 20, fixtures=1),
            make_forecast(14, "FWD Two", 12, "FWD", 7.0, 5, 13, fixtures=1),
            make_forecast(15, "FWD Three", 13, "FWD", 6.5, 5, 12, fixtures=1),
        ]
        squad_state = SquadState(
            season="2025-26",
            week=26,
            squad_players=squad_players,
            bank=0.0,
            free_transfers=1,
            chips_available={"bench_boost": True, "triple_captain": True},
        )

        bundle = recommend_actions(squad_state, forecasts)
        chips = {advisory.chip for advisory in bundle.chip_advisories}

        self.assertIn("bench_boost", chips)
        self.assertIn("triple_captain", chips)

    def test_recommend_actions_merges_evidence_snapshot_documents_into_supporting_sources(self):
        squad_players = [
            SquadPlayer(1, "GK One", 1, "GK", 4.5),
            SquadPlayer(2, "GK Two", 2, "GK", 4.0),
            SquadPlayer(3, "DEF One", 1, "DEF", 5.0),
            SquadPlayer(4, "DEF Two", 2, "DEF", 4.5),
            SquadPlayer(5, "DEF Three", 3, "DEF", 4.8),
            SquadPlayer(6, "DEF Four", 4, "DEF", 4.7),
            SquadPlayer(7, "DEF Five", 5, "DEF", 4.6),
            SquadPlayer(8, "MID Star", 6, "MID", 12.0),
            SquadPlayer(9, "MID Two", 7, "MID", 8.0),
            SquadPlayer(10, "MID Three", 8, "MID", 7.5),
            SquadPlayer(11, "MID Four", 9, "MID", 6.0),
            SquadPlayer(12, "MID Five", 10, "MID", 5.5),
            SquadPlayer(13, "FWD One", 11, "FWD", 8.5),
            SquadPlayer(14, "FWD Two", 12, "FWD", 7.0),
            SquadPlayer(15, "FWD Three", 13, "FWD", 6.5),
        ]
        forecasts = [
            make_forecast(1, "GK One", 1, "GK", 4.5, 4, 11),
            make_forecast(2, "GK Two", 2, "GK", 4.0, 2, 6),
            make_forecast(3, "DEF One", 1, "DEF", 5.0, 5, 12),
            make_forecast(4, "DEF Two", 2, "DEF", 4.5, 3, 8),
            make_forecast(5, "DEF Three", 3, "DEF", 4.8, 4, 10),
            make_forecast(6, "DEF Four", 4, "DEF", 4.7, 4, 9),
            make_forecast(7, "DEF Five", 5, "DEF", 4.6, 3, 8),
            make_forecast(8, "MID Star", 6, "MID", 12.0, 9, 24),
            make_forecast(9, "MID Two", 7, "MID", 8.0, 6, 16),
            make_forecast(10, "MID Three", 8, "MID", 7.5, 5, 14),
            make_forecast(11, "MID Four", 9, "MID", 6.0, 4, 10),
            make_forecast(12, "MID Five", 10, "MID", 5.5, 3, 7),
            make_forecast(13, "FWD One", 11, "FWD", 8.5, 7, 18),
            make_forecast(14, "FWD Two", 12, "FWD", 7.0, 5, 12),
            make_forecast(15, "FWD Three", 13, "FWD", 6.5, 2, 6),
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
            player_summaries=[],
            team_summaries=[],
            notes=["Selected 1 timestamp-safe document before the deadline."],
        )
        squad_state = SquadState(
            season="2025-26",
            week=30,
            squad_players=squad_players,
            bank=0.0,
            free_transfers=1,
            chips_available={},
        )

        bundle = recommend_actions(squad_state, forecasts, evidence_snapshot=evidence_snapshot)

        self.assertEqual(len(bundle.supporting_sources), 1)
        self.assertEqual(bundle.supporting_sources[0].title, "Official update")
        self.assertIsNotNone(bundle.evidence_snapshot)
        self.assertTrue(any("timestamp-safe evidence documents" in item for item in bundle.assumptions))


if __name__ == "__main__":
    unittest.main()

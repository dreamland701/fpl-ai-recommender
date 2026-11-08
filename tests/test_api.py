import unittest

from fpl_ai.api import OfficialFPLClient, OfficialSnapshotService


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class FakeSession:
    def __init__(self, payloads):
        self.payloads = payloads

    def get(self, url, timeout=20):
        if url.endswith("bootstrap-static/"):
            return FakeResponse(self.payloads["bootstrap"])
        if url.endswith("fixtures/"):
            return FakeResponse(self.payloads["fixtures"])
        raise AssertionError(f"Unexpected URL {url}")


class ApiTestCase(unittest.TestCase):
    def test_average_entry_scores_reads_event_metadata(self):
        session = FakeSession(
            {
                "bootstrap": {
                    "events": [
                        {"id": 10, "average_entry_score": 52},
                        {"id": 11, "average_entry_score": 61},
                    ],
                    "elements": [],
                },
                "fixtures": [],
            }
        )
        client = OfficialFPLClient(session=session)
        self.assertEqual(client.average_entry_scores(), {10: 52.0, 11: 61.0})

    def test_build_week_state_selects_nearest_deadline(self):
        session = FakeSession(
            {
                "bootstrap": {
                    "events": [
                        {"id": 30, "deadline_time": "2026-04-04T10:00:00Z"},
                        {"id": 31, "deadline_time": "2026-04-11T10:00:00Z"},
                    ],
                    "elements": [{"id": 1}, {"id": 2}, {"id": 3}],
                },
                "fixtures": [
                    {"event": 30, "finished": False},
                    {"event": 30, "finished": False},
                    {"event": 31, "finished": False},
                ],
            }
        )
        client = OfficialFPLClient(session=session)
        service = OfficialSnapshotService(client)
        week_state = service.build_week_state("2026-04-03T12:00:00+00:00")

        self.assertEqual(week_state.week, 30)
        self.assertEqual(week_state.season, "2025-26")
        self.assertEqual(week_state.fixture_count, 2)

    def test_current_week_frame_counts_fixtures_ahead(self):
        # Team 1 doubles in GW30 and blanks in GW31; team 2 plays in GW30 and GW32 only. Over the three
        # events to the season's end (30, 31, 32) team 1 has 3 fixtures and team 2 has 2.
        session = FakeSession(
            {
                "bootstrap": {
                    "events": [{"id": 30, "deadline_time": "2026-04-04T10:00:00Z"},
                               {"id": 31, "deadline_time": "2026-04-11T10:00:00Z"},
                               {"id": 32, "deadline_time": "2026-04-18T10:00:00Z"}],
                    "elements": [{"id": 1, "web_name": "a", "team": 1, "element_type": 3, "now_cost": 50, "selected_by_percent": "1.0",
                                  "transfers_in_event": 0, "transfers_out_event": 0, "status": "a", "news": ""},
                                 {"id": 2, "web_name": "b", "team": 2, "element_type": 3, "now_cost": 50, "selected_by_percent": "1.0",
                                  "transfers_in_event": 0, "transfers_out_event": 0, "status": "a", "news": ""}],
                },
                "fixtures": [
                    {"event": 30, "team_h": 1, "team_a": 3, "team_h_difficulty": 2, "team_a_difficulty": 3},
                    {"event": 30, "team_h": 4, "team_a": 1, "team_h_difficulty": 2, "team_a_difficulty": 3},
                    {"event": 30, "team_h": 2, "team_a": 5, "team_h_difficulty": 2, "team_a_difficulty": 3},
                    {"event": 31, "team_h": 4, "team_a": 3, "team_h_difficulty": 2, "team_a_difficulty": 3},
                    {"event": 32, "team_h": 1, "team_a": 2, "team_h_difficulty": 2, "team_a_difficulty": 3},
                ],
            }
        )
        service = OfficialSnapshotService(OfficialFPLClient(session=session))
        players = service.build_current_week_frame("2026-04-03T12:00:00+00:00").set_index("player_id")
        self.assertEqual(int(players.loc[1, "fixture_count"]), 2)
        self.assertEqual(players.loc[1, "fixtures_next_3"], 3.0)
        self.assertEqual(players.loc[2, "fixtures_next_3"], 2.0)
        # only three events remain, so the 5-week count is scaled to a 5-week rate
        self.assertAlmostEqual(players.loc[1, "fixtures_next_5"], 3.0 * 5 / 3)


if __name__ == "__main__":
    unittest.main()

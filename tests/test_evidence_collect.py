import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

from fpl_ai.evidence_collect import collect_and_write_evidence, collect_evidence_records


class FakeResponse:
    def __init__(self, text: str, status_code: int = 200, payload=None):
        self.text = text
        self.status_code = status_code
        self.payload = payload

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        if self.payload is not None:
            return self.payload
        return json.loads(self.text)


class FakeSession:
    def __init__(self, payload_by_url):
        self.payload_by_url = payload_by_url

    def get(self, url, timeout=20, headers=None, params=None):
        if url not in self.payload_by_url:
            raise AssertionError(f"Unexpected URL {url}")
        payload = self.payload_by_url[url]
        if isinstance(payload, FakeResponse):
            return payload
        return FakeResponse(payload)

    def post(self, url, auth=None, data=None, headers=None, timeout=20):
        if url not in self.payload_by_url:
            raise AssertionError(f"Unexpected URL {url}")
        payload = self.payload_by_url[url]
        if isinstance(payload, FakeResponse):
            return payload
        return FakeResponse(payload)


class FakeFPLClient:
    def bootstrap_static(self):
        return {
            "elements": [
                {"id": 1, "first_name": "Bukayo", "second_name": "Saka", "web_name": "Saka", "team": 1},
                {"id": 2, "first_name": "Mohamed", "second_name": "Salah", "web_name": "Salah", "team": 2},
            ],
            "teams": [
                {"id": 1, "name": "Arsenal", "short_name": "ARS"},
                {"id": 2, "name": "Liverpool", "short_name": "LIV"},
            ],
        }


class EvidenceCollectTestCase(unittest.TestCase):
    def test_collect_evidence_records_parses_rss_and_tags_entities(self):
        rss = """<?xml version="1.0"?>
        <rss version="2.0">
          <channel>
            <item>
              <title>Saka returns for Arsenal ahead of FPL deadline</title>
              <link>https://www.bbc.com/sport/football/articles/example</link>
              <pubDate>Mon, 17 May 2026 08:00:00 GMT</pubDate>
              <description>Saka is back in training for Arsenal.</description>
            </item>
            <item>
              <title>Arsenal owner discusses club accounts</title>
              <link>https://www.bbc.com/sport/football/articles/noise</link>
              <pubDate>Mon, 17 May 2026 09:00:00 GMT</pubDate>
              <description>Arsenal financial results are published.</description>
            </item>
          </channel>
        </rss>
        """
        session = FakeSession(
            {
                "https://feeds.bbci.co.uk/sport/football/rss.xml": rss,
                "https://www.theguardian.com/football/rss": "<?xml version='1.0'?><rss><channel></channel></rss>",
            }
        )

        records = collect_evidence_records(
            source_keys=["bbc_football_rss", "guardian_football_rss"],
            lookback_days=7,
            max_items_per_source=10,
            session=session,
            client=FakeFPLClient(),
            now=datetime(2026, 5, 18, tzinfo=timezone.utc),
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["player_name"], "Bukayo Saka")
        self.assertEqual(records[0]["team_name"], "Arsenal")
        self.assertEqual(records[0]["source_name"], "BBC Sport Football")
        self.assertEqual(records[0]["relevance_reason"], "fpl_keyword")

    def test_collect_evidence_records_avoids_first_name_only_player_matches(self):
        rss = """<?xml version="1.0"?>
        <rss version="2.0">
          <channel>
            <item>
              <title>Bryan handball controversy discussed</title>
              <link>https://www.bbc.com/sport/football/articles/example</link>
              <pubDate>Mon, 17 May 2026 08:00:00 GMT</pubDate>
              <description>Bryan was mentioned in a refereeing discussion.</description>
            </item>
          </channel>
        </rss>
        """
        session = FakeSession(
            {
                "https://feeds.bbci.co.uk/sport/football/rss.xml": rss,
            }
        )
        client = FakeFPLClient()
        client.bootstrap_static = lambda: {
            "elements": [
                {"first_name": "Bryan", "second_name": "Mbeumo", "web_name": "Bryan"},
            ],
            "teams": [],
        }

        records = collect_evidence_records(
            source_keys=["bbc_football_rss"],
            lookback_days=7,
            max_items_per_source=10,
            session=session,
            client=client,
            now=datetime(2026, 5, 18, tzinfo=timezone.utc),
        )

        self.assertEqual(records, [])

    def test_collect_and_write_evidence_merges_local_inputs(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "evidence.jsonl"
            local_path = Path(tmpdir) / "local.json"
            local_path.write_text(
                json.dumps(
                    [
                        {
                            "title": "Local club update",
                            "url": "https://www.premierleague.com/news/123",
                            "source_name": "Premier League",
                            "category": "official_premier_league",
                            "published_at": "2026-05-17T08:00:00Z",
                            "snippet": "Arsenal update.",
                            "player_name": "Bukayo Saka",
                            "team_name": "Arsenal",
                        }
                    ]
                )
            )
            frame = collect_and_write_evidence(
                output_path=str(output_path),
                local_inputs=[str(local_path)],
                source_keys=[],
                client=FakeFPLClient(),
            )

            self.assertEqual(len(frame), 1)
            self.assertTrue(output_path.exists())
            written = [json.loads(line) for line in output_path.read_text().splitlines() if line.strip()]
            self.assertEqual(written[0]["title"], "Local club update")

    def test_collect_evidence_records_includes_official_fpl_snapshot_with_collection_timestamp(self):
        client = FakeFPLClient()
        client.bootstrap_static = lambda: {
            "elements": [
                {
                    "id": 1,
                    "first_name": "Bukayo",
                    "second_name": "Saka",
                    "web_name": "Saka",
                    "team": 1,
                    "status": "d",
                    "chance_of_playing_this_round": 75,
                    "chance_of_playing_next_round": 75,
                    "news": "Ankle injury - 75% chance of playing",
                }
            ],
            "teams": [{"id": 1, "name": "Arsenal", "short_name": "ARS"}],
        }

        records = collect_evidence_records(
            source_keys=["official_fpl_status"],
            max_items_per_source=10,
            client=client,
            now=datetime(2026, 5, 18, 10, 0, tzinfo=timezone.utc),
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["category"], "official_fpl")
        self.assertEqual(records[0]["timestamp_quality"], "collected_at_snapshot")
        self.assertEqual(records[0]["published_at"], "2026-05-18T10:00:00+00:00")

    def test_collect_evidence_records_parses_premierleague_article_timestamps(self):
        index_html = '<a href="/en/news/123/saka-injury-update">Article</a>'
        article_html = """
        <html><head>
          <meta property="og:title" content="Saka injury update for FPL managers">
          <meta property="og:description" content="Arsenal winger Saka is back in training.">
          <script type="application/ld+json">{"datePublished":"2026-05-17T08:00:00Z"}</script>
        </head></html>
        """
        session = FakeSession(
            {
                "https://www.premierleague.com/news": index_html,
                "https://www.premierleague.com/en/news/123/saka-injury-update": article_html,
            }
        )

        records = collect_evidence_records(
            source_keys=["premierleague_news"],
            lookback_days=7,
            max_items_per_source=10,
            session=session,
            client=FakeFPLClient(),
            now=datetime(2026, 5, 18, tzinfo=timezone.utc),
        )

        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["source_name"], "The Scout")
        self.assertEqual(records[0]["timestamp_quality"], "published_at")
        self.assertEqual(records[0]["player_name"], "Bukayo Saka")


if __name__ == "__main__":
    unittest.main()

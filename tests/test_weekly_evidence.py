import json
import tempfile
import unittest
from pathlib import Path

import pandas as pd

from fpl_ai.dataset import CanonicalDataset
from fpl_ai.weekly_evidence import WeekEvidenceWindow, _fetch_sky_podcast_feed_rows, backfill_weekly_google_news_evidence
from fpl_ai.weekly_evidence import (
    SearchResolutionBlocked,
    _clean_sky_podcast_episode_text,
    _extract_generic_article_text,
    _extract_premierleague_article_text,
    _resolve_article_url,
)


class FakeResponse:
    def __init__(self, text: str, headers=None):
        self.text = text
        self.headers = headers or {}

    def raise_for_status(self):
        return None


class FakeSession:
    def __init__(self, rss: str):
        self.rss = rss
        self.requests = []

    def get(self, url, params=None, headers=None, timeout=30, allow_redirects=True):
        self.requests.append({"url": url, "params": params or {}})
        return FakeResponse(self.rss)


class FakeUrlSession:
    def __init__(self, payload_by_url):
        self.payload_by_url = payload_by_url

    def get(self, url, params=None, headers=None, timeout=30, allow_redirects=True):
        if url not in self.payload_by_url:
            raise AssertionError(f"Unexpected URL {url}")
        return FakeResponse(self.payload_by_url[url])


class FakeSearchSession:
    def __init__(self, html: str, location: str = ""):
        self.html = html
        self.location = location
        self.requests = []

    def get(self, url, params=None, headers=None, timeout=30, allow_redirects=True):
        self.requests.append({"url": url, "params": params or {}, "allow_redirects": allow_redirects})
        return FakeResponse(self.html, headers={"location": self.location} if self.location else {})


class WeeklyEvidenceTestCase(unittest.TestCase):
    def test_extract_premierleague_article_text_keeps_article_paragraphs(self):
        html = """
        <article>
          <p class="article__summary">Summary text.</p>
          <p>First useful paragraph with <a href="/x">link</a>.</p>
          <p>First useful paragraph with <a href="/x">link</a>.</p>
        </article>
        """
        text = _extract_premierleague_article_text(html)

        self.assertIn("Summary text.", text)
        self.assertIn("First useful paragraph with link", text)
        self.assertEqual(text.count("First useful paragraph"), 1)

    def test_extract_generic_article_text_dedupes_paragraphs(self):
        html = """
        <main>
          <p>Liam Rosenior has named his Chelsea side to face Newcastle United in the Premier League.</p>
          <p>Liam Rosenior has named his Chelsea side to face Newcastle United in the Premier League.</p>
          <p>Advertisement</p>
        </main>
        """
        text = _extract_generic_article_text(html)

        self.assertIn("Chelsea side", text)
        self.assertEqual(text.count("Chelsea side"), 1)
        self.assertNotIn("Advertisement", text)

    def test_fetch_sky_podcast_feed_rows_keeps_episode_descriptions(self):
        rss = """<?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0"><channel>
          <item>
            <title>FPL Gameweek 30 | Best captain picks</title>
            <link>https://example.com/episode</link>
            <pubDate>Fri, 13 Mar 2026 12:00:00 +0000</pubDate>
            <description><![CDATA[James and Mark discuss Haaland, Salah and captaincy before the deadline. Listen to every episode of the Sky Sports Fantasy Podcast here: skysports.com/sky-sports-fantasy-podcast]]></description>
            <content:encoded><![CDATA[<p>James and Mark discuss Haaland, Salah and captaincy before the deadline.</p><p>They debate whether to sell an injured forward.</p><p>Listen to every episode of the Sky Sports Fantasy Podcast here: skysports.com/sky-sports-fantasy-podcast</p>]]></content:encoded>
          </item>
        </channel></rss>
        """
        rss = rss.replace("<rss version=\"2.0\">", '<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">')
        rows = _fetch_sky_podcast_feed_rows(
            session=FakeUrlSession(
                {
                    "https://feeds.captivate.fm/sky-sports-fantasy/": rss,
                    "https://feeds.captivate.fm/sky-sports-premierleague/": "<?xml version='1.0'?><rss><channel></channel></rss>",
                }
            ),
            windows=[
                WeekEvidenceWindow(
                    season="2025-26",
                    week=30,
                    window_start="2026-03-10T00:00:00+00:00",
                    deadline_ts="2026-03-14T13:30:00+00:00",
                )
            ],
            player_aliases={"haaland": "Erling Haaland", "salah": "Mohamed Salah"},
            team_aliases={},
        )

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["source_name"], "Sky Sports Fantasy Podcast")
        self.assertEqual(rows[0]["extraction_status"], "rss_episode_summary")
        self.assertIn("captaincy", rows[0]["full_text"])
        self.assertIn("injured forward", rows[0]["full_text"])
        self.assertNotIn("Listen to every episode", rows[0]["full_text"])

    def test_clean_sky_podcast_episode_text_strips_promotional_boilerplate(self):
        text = (
            "James and Mark discuss the best captaincy options. "
            "They explain why Mohamed Salah is risky this week. "
            "Listen to every episode of the Sky Sports Fantasy Podcast here: skysports.com/x "
            "For all the latest Premier League news, head to skysports.com/premier-league"
        )

        cleaned = _clean_sky_podcast_episode_text(text)

        self.assertIn("best captaincy options", cleaned)
        self.assertIn("Mohamed Salah is risky", cleaned)
        self.assertNotIn("Listen to every episode", cleaned)
        self.assertNotIn("For all the latest", cleaned)

    def test_extract_generic_article_text_reads_json_ld_article_body(self):
        html = """
        <html><head>
          <script type="application/ld+json">
            {
              "@type": "NewsArticle",
              "articleBody": "Manchester City confirmed Erling Haaland returned to training before the deadline. Pep Guardiola said he would be assessed after the final session."
            }
          </script>
        </head><body><p>Advertisement</p></body></html>
        """
        text = _extract_generic_article_text(html)

        self.assertIn("Haaland returned to training", text)
        self.assertNotIn("Advertisement", text)

    def test_extract_generic_article_text_reads_escaped_article_body(self):
        html = r'''
        <script>
          {"props":{"pageProps":{"articleBody":"Arsenal manager Mikel Arteta said \"Bukayo Saka\" was available after returning to full training before the Gameweek deadline."}}}
        </script>
        '''
        text = _extract_generic_article_text(html)

        self.assertIn('"Bukayo Saka" was available', text)

    def test_resolve_article_url_allows_bbc_equivalent_domain_from_search_html(self):
        html = '<a href="/url?q=https%3A%2F%2Fwww.bbc.co.uk%2Fsport%2Ffootball%2F12345&sa=U">BBC result</a>'
        session = FakeSearchSession(html)

        resolved = _resolve_article_url(
            title="Premier League and FPL team news - BBC",
            source_name="BBC",
            source_url="https://www.bbc.com",
            session=session,
        )

        self.assertEqual(resolved, "https://www.bbc.co.uk/sport/football/12345")

    def test_resolve_article_url_reports_search_block(self):
        session = FakeSearchSession("", location="https://www.google.com/sorry/index?continue=blocked")

        with self.assertRaises(SearchResolutionBlocked):
            _resolve_article_url(
                title="FPL gameweek 30 tips - BBC",
                source_name="BBC",
                source_url="https://www.bbc.com",
                session=session,
            )

    def test_backfill_weekly_google_news_filters_to_pre_deadline_packets(self):
        rss = """<?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0"><channel>
          <item>
            <title>Fantasy Premier League GW1 injury news - BBC Sport</title>
            <link>https://news.google.com/rss/articles/good</link>
            <pubDate>Fri, 15 Aug 2025 10:00:00 GMT</pubDate>
            <source url="https://www.bbc.com">BBC Sport</source>
            <description>Saka fitness update before the deadline.</description>
          </item>
          <item>
            <title>Fantasy Premier League GW1 late news - BBC Sport</title>
            <link>https://news.google.com/rss/articles/future</link>
            <pubDate>Fri, 15 Aug 2025 19:00:00 GMT</pubDate>
            <source url="https://www.bbc.com">BBC Sport</source>
            <description>This is after deadline and must not attach.</description>
          </item>
        </channel></rss>
        """
        dataset = CanonicalDataset(
            pd.DataFrame(
                [
                    {
                        "season": "2025-26",
                        "week": 1,
                        "kickoff_time": "2025-08-15T19:30:00Z",
                        "player_id": 1,
                        "player_name": "Bukayo Saka",
                        "team_name": "Arsenal",
                        "eligible_for_training": True,
                        "eligible_for_backtest": True,
                    }
                ]
            )
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            docs = Path(tmpdir) / "docs.jsonl"
            packets = Path(tmpdir) / "packets.jsonl"
            report = Path(tmpdir) / "report.json"
            result = backfill_weekly_google_news_evidence(
                dataset=dataset,
                season="2025-26",
                start_week=1,
                end_week=1,
                documents_output=str(docs),
                packets_output=str(packets),
                report_output=str(report),
                max_items_per_query=10,
                sleep_seconds=0.0,
                session=FakeSession(rss),
            )

            self.assertEqual(result.packet_rows, 1)
            packet = json.loads(packets.read_text().splitlines()[0])
            self.assertEqual(packet["document_count"], 1)
            self.assertIn("injury news", packet["documents"][0]["title"])
            self.assertNotIn("late news", json.dumps(packet))


if __name__ == "__main__":
    unittest.main()

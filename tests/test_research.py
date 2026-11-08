import unittest

from fpl_ai.research import generate_cited_report
from fpl_ai.types import RecommendationBundle, SourceDocument


class ResearchTestCase(unittest.TestCase):
    def test_generate_cited_report_flags_stale_sources(self):
        bundle = RecommendationBundle(
            season="2025-26",
            week=30,
            transfers=[],
            captain_id=8,
            vice_captain_id=9,
            starters=[1, 3, 5, 6, 8, 9, 10, 11, 13, 14, 15],
            bench_order=[2, 4, 7, 12],
            chip_advisories=[],
            confidence=0.71,
            assumptions=["Structured data drives forecasts."],
            supporting_sources=[
                SourceDocument(
                    title="Injury update",
                    url="https://www.premierleague.com/news/example",
                    source_name="Premier League",
                    category="official_premier_league",
                    published_at="2020-01-01T00:00:00+00:00",
                    snippet="Old update.",
                ),
                SourceDocument(
                    title="Fresh note",
                    url="https://www.reddit.com/r/FantasyPL/comments/example",
                    source_name="r/FantasyPL",
                    category="reddit",
                    published_at="2099-01-01T00:00:00+00:00",
                    snippet="Fresh thread.",
                ),
            ],
        )

        report = generate_cited_report(bundle)
        self.assertEqual(len(report.citations), 2)
        self.assertTrue(report.stale_sources)
        self.assertIn("Captain: 8", report.body)


if __name__ == "__main__":
    unittest.main()

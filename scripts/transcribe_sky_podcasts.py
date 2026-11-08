#!/usr/bin/env python3
"""Download and transcribe Sky Sports podcast episodes into evidence rows.

Feed audit (2026-07-05):
- Sky Sports Premier League Podcast: episodes + MP3 enclosures back to 2015-11.
- Sky Sports Fantasy Podcast: episodes + MP3 enclosures back to 2024-08 only.

Transcription runs Whisper large-v3 through transformers on CUDA (CTranslate2
has no CUDA support on this aarch64 box, so faster-whisper is not usable).
Measured ~2-4x realtime; transcribe one season per overnight run and do not
schedule against SFT training runs for GPU time.

Output: JSONL evidence rows compatible with the existing evidence corpus
schema (published_at from episode pubDate, extraction_status
"whisper_large_v3_transcript"), one row per episode.

Usage:
  python3 scripts/transcribe_sky_podcasts.py \
    --feed premierleague --since 2025-08-01 --until 2026-04-10 \
    --output reports/evidence_sky_podcast_transcripts_2025_26.jsonl \
    [--limit 5] [--skip-existing]
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
import time
import urllib.request
import xml.etree.ElementTree as ElementTree
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

FEEDS = {
    "fantasy": ("Sky Sports Fantasy Podcast", "https://feeds.captivate.fm/sky-sports-fantasy/"),
    "premierleague": ("Sky Sports Premier League Podcast", "https://feeds.captivate.fm/sky-sports-premierleague/"),
}

# Episodes whose titles match none of these are skipped (trailers, other
# competitions, cross-promos). Keep permissive: false positives only cost
# transcription time, false negatives lose evidence.
RELEVANT_TITLE_PATTERN = re.compile(
    r"premier league|fpl|fantasy|gameweek|gw\d|transfer|injur|team news|preview|deadline|double|wildcard|chip",
    re.IGNORECASE,
)


def _parse_date(value: str) -> datetime:
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)


def fetch_episodes(feed_key: str, since: datetime, until: datetime, relevant_only: bool) -> list[dict]:
    source_name, feed_url = FEEDS[feed_key]
    request = urllib.request.Request(feed_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        root = ElementTree.fromstring(response.read())

    episodes = []
    for item in root.findall(".//item"):
        pub_el = item.find("pubDate")
        enclosure = item.find("enclosure")
        if pub_el is None or not pub_el.text or enclosure is None:
            continue
        try:
            published = parsedate_to_datetime(pub_el.text)
        except (TypeError, ValueError):
            continue
        if published < since or published > until:
            continue
        title = (item.findtext("title") or "").strip()
        if relevant_only and not RELEVANT_TITLE_PATTERN.search(title):
            continue
        episodes.append(
            {
                "source_name": source_name,
                "feed_url": feed_url,
                "title": title,
                "link": (item.findtext("link") or feed_url).strip(),
                "published_at": published.isoformat(),
                "audio_url": enclosure.get("url"),
                "audio_bytes": int(enclosure.get("length") or 0),
                "description": (item.findtext("description") or "").strip(),
            }
        )
    episodes.sort(key=lambda ep: ep["published_at"])
    return episodes


def load_transcriber():
    import torch
    from transformers import pipeline

    return pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-large-v3",
        torch_dtype=torch.bfloat16,
        device="cuda:0",
        chunk_length_s=30,
        batch_size=8,
        ignore_warning=True,
    )


def transcribe_episode(asr, audio_url: str) -> tuple[str, float]:
    import librosa
    import soundfile as sf

    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp:
        request = urllib.request.Request(audio_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=300) as response:
            tmp.write(response.read())
        tmp.flush()
        audio, sr = sf.read(tmp.name)
    if audio.ndim > 1:
        audio = audio.mean(axis=1)
    if sr != 16000:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16000)
    duration_s = len(audio) / 16000
    result = asr({"raw": audio, "sampling_rate": 16000}, return_timestamps=True, generate_kwargs={"language": "en"})
    return result["text"].strip(), duration_s


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--feed", required=True, choices=sorted(FEEDS))
    parser.add_argument("--since", required=True, help="ISO date, inclusive (episode pubDate).")
    parser.add_argument("--until", required=True, help="ISO date, inclusive.")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--limit", type=int, default=0, help="Transcribe at most N episodes (0 = all).")
    parser.add_argument("--all-titles", action="store_true", help="Skip the relevance title filter.")
    parser.add_argument("--skip-existing", action="store_true", help="Skip episodes whose audio_url already exists in the output file.")
    args = parser.parse_args()

    episodes = fetch_episodes(args.feed, _parse_date(args.since), _parse_date(args.until), relevant_only=not args.all_titles)
    print(f"{len(episodes)} episodes in window after filtering")

    done_urls: set[str] = set()
    if args.skip_existing and args.output.exists():
        with args.output.open() as handle:
            for line in handle:
                try:
                    done_urls.add(json.loads(line).get("audio_url") or "")
                except json.JSONDecodeError:
                    continue
        episodes = [ep for ep in episodes if ep["audio_url"] not in done_urls]
        print(f"{len(episodes)} remain after skipping {len(done_urls)} already transcribed")
    if args.limit > 0:
        episodes = episodes[: args.limit]
    if not episodes:
        return

    asr = load_transcriber()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("a") as handle:
        for index, episode in enumerate(episodes, start=1):
            start = time.time()
            try:
                text, duration_s = transcribe_episode(asr, episode["audio_url"])
            except Exception as exc:
                print(f"[{index}/{len(episodes)}] FAILED {episode['title'][:60]}: {type(exc).__name__}: {exc}")
                continue
            elapsed = time.time() - start
            row = {
                "title": episode["title"],
                "url": episode["link"],
                "audio_url": episode["audio_url"],
                "source_url": episode["feed_url"],
                "source_name": episode["source_name"],
                "category": "trusted_news",
                "published_at": episode["published_at"],
                "snippet": episode["description"][:500],
                "content": text,
                "full_text": text,
                "full_text_chars": len(text),
                "audio_duration_s": round(duration_s, 1),
                "relevance_reason": "sky_podcast_transcript",
                "source_key": f"sky_sports_podcast_transcript_{args.feed}",
                "timestamp_quality": "published_at",
                "extraction_status": "whisper_large_v3_transcript",
            }
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            handle.flush()
            rate = duration_s / elapsed if elapsed else 0.0
            print(
                f"[{index}/{len(episodes)}] {episode['published_at'][:10]} {episode['title'][:60]!r} "
                f"{duration_s/60:.0f}min audio in {elapsed/60:.1f}min ({rate:.1f}x realtime, {len(text)} chars)"
            )


if __name__ == "__main__":
    main()

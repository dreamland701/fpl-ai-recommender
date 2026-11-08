#!/usr/bin/env python3
"""Build the LLM-extraction pilot set (Wes, 2026-08-22: "option 3").

~16 (article, player) pairs — the six hand-reviewed window cases plus
stratified random draws (scout vs general press) — each rendered as an
extraction prompt for the LOCAL base Gemma (same <|turn|>-template
messages pattern G2's condensation validated, incl. its 'nothing'
sentinel; tail-cleanup is applied at read time by the report stage).

Wes's explicit quality requirement: blank/'nothing' extractions must be
SURFACED, not hidden — the report stage marks them and pairs every
extraction with the current mechanical window for side-by-side judging.

Stage 1 (this script, CPU): select pairs, write prompts JSONL + a
reference JSONL (article text, current window, player, source).
Stage 2 (chain, GPU after E11): eval_gemma_responses.py --> extractions.
Stage 3 (report): scripts/report_evidence_extraction_pilot.py.
"""
from __future__ import annotations

import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPTS_OUT = ROOT / "reports" / "evidence_extraction_pilot_prompts.jsonl"
REF_OUT = ROOT / "reports" / "evidence_extraction_pilot_reference.jsonl"

KNOWN_CASES = {  # (corpus_file, player_name, title_substring)
    ("live", "Rice", "preview No 1: Arsenal"),
    ("live", "Saka", "preview No 1: Arsenal"),
    ("train", "Morgan Rogers", "Quick Fantasy tips"),
    ("train", "Cristian Romero", "preview No 18: Tottenham"),
    ("train", "Destiny Udogie", "Uefa Super Cup"),
    ("train", "Brandon Austin", "Uefa Super Cup"),
}
CORPORA = {
    "live": ROOT / "reports" / "live_gw1_2627_corpus_full_wed.jsonl",
    "train": ROOT / "reports" / "llm_player_forecast_multiseason_2022_26_baseline_adjustment_v10_e11_full.jsonl",
}
ARTICLE_CHARS = 12000


def extraction_prompt(doc: dict, player: str) -> str:
    content = " ".join(str(doc.get("content") or doc.get("snippet") or "").split())[:ARTICLE_CHARS]
    return (
        f"Article ({doc.get('source_name') or 'unknown'}, {doc.get('published_at') or ''}): "
        f"{doc.get('title') or ''}\n{content}\n\n"
        f"In at most 60 words, extract only what this article says about {player} that matters "
        "for fantasy football: fitness/injury, starts and minutes, role, form, set pieces, price, "
        "transfers, defensive contribution. Quote or closely paraphrase the text — do not infer or "
        "add outside knowledge. If it says nothing meaningful about him, reply exactly: nothing."
    )


def rows_from(corpus_path: Path, wanted_players=None, sample_pool=None, season_filter="2025-26"):
    for line in corpus_path.open():
        row = json.loads(line)
        md = row["metadata"]
        if str(md.get("season") or row.get("season")) not in (season_filter, "2026-27"):
            continue
        player = str(md.get("player_name") or "")
        for doc in md.get("evidence_documents") or []:
            item = (player, doc)
            if wanted_players is not None:
                for key in list(wanted_players):
                    _, want_player, want_title = key
                    if want_player in player and want_title in str(doc.get("title") or ""):
                        yield ("known", player, doc)
                        wanted_players.discard(key)
            if sample_pool is not None:
                sample_pool.append((player, doc))


def main() -> None:
    rng = random.Random(20260822)
    prompts, refs = [], []
    seen_pairs = set()

    def add(kind, player, doc):
        key = (player, str(doc.get("url") or doc.get("title")))
        if key in seen_pairs:
            return False
        seen_pairs.add(key)
        idx = len(prompts)
        prompts.append({
            "season": "pilot", "week": idx,
            "messages": [{"role": "user", "content": extraction_prompt(doc, player)}],
            "completion": "",
            "metadata": {"pilot_index": idx},
        })
        content = " ".join(str(doc.get("content") or "").split())
        refs.append({
            "pilot_index": idx, "kind": kind, "player": player,
            "source": doc.get("source_name"), "title": doc.get("title"),
            "published_at": doc.get("published_at"),
            "article_chars": len(content),
            "article_head": content[:400],
        })
        return True

    for corpus_key in ("live", "train"):
        wanted = {c for c in KNOWN_CASES if c[0] == corpus_key}
        pool: list = []
        for kind, player, doc in rows_from(CORPORA[corpus_key], wanted_players=wanted, sample_pool=pool):
            add("known", player, doc)
        rng.shuffle(pool)
        scout = [(p, d) for p, d in pool if str(d.get("source_name")) == "Premier League"]
        general = [(p, d) for p, d in pool if str(d.get("source_name")) != "Premier League"]
        want_scout = 3 if corpus_key == "train" else 2
        want_general = 3 if corpus_key == "train" else 2
        for p, d in scout:
            if want_scout <= 0: break
            if add("random_scout", p, d): want_scout -= 1
        for p, d in general:
            if want_general <= 0: break
            if add("random_general", p, d): want_general -= 1

    PROMPTS_OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in prompts))
    REF_OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in refs))
    from collections import Counter
    print(f"pilot pairs: {len(prompts)} -> {PROMPTS_OUT.name}")
    print("mix:", dict(Counter(r['kind'] for r in refs)), "| sources:", dict(Counter(str(r['source']) for r in refs)))


if __name__ == "__main__":
    main()

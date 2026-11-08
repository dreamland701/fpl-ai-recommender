#!/usr/bin/env python3
"""Route the evidence stores into the documents an availability extractor should read (2026-10-22, the
"read facts, not snippets" path after F16).

Scope: Guardian 2022-23..2026-27 documents tagged with a Premier League club (or football/premierleague), not
women's football, not live blogs (/live/ URLs), whose title or standfirst carries a cue of one of three classes:
  avail (team news, injury, press conference, ruled out, doubt, fitness, suspension, return, rotation, dropped ...),
  role  (starts, captaincy, penalties, set pieces, position, pecking order ...),
  sign  (signs, joins, loan, transfer, deal ...),
plus Premier League Scout documents whose title, description or lead carries an avail/role cue. Each document is
assigned to the next Premier League deadline after its publication (deadline = 90 min before the first kickoff of
the round, from fixtures.csv) with the hours before that deadline, so a downstream feature builder can key facts to
(season, gw) and weight recency. --classes picks the classes (default avail,role).

The Guardian "predicted lineups" articles are NOT routed to the LLM (scripts/build_team_news_table.py parses them
deterministically); their per-fixture segments become ground-truth "team blocks" for the extractor pilot: the text of
one fixture (two teams' Subs from / Doubtful / Injured / Suspended lists) with the parser's lists as truth.

usage: build_extract_docs.py --out reports/extract_facts/docs_all.jsonl                      (full scope)
       build_extract_docs.py --pilot 60 --team-blocks 30 --seed 7 --out reports/extract_facts/pilot_docs.jsonl
       build_extract_docs.py --stats                                                           (tier counts + samples)
Output rows: doc_id, kind (prose|team_block), season, gw, hours_before, published_at, source, title, url, hit, text,
             truth (team blocks only: {team_name: {sub, doubtful, injured, suspended}}).
"""
from __future__ import annotations
import argparse
import collections
import csv
import datetime as dt
import glob
import hashlib
import json
import random
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_team_news_table import BLOCK, HDR, TITLE, deadlines, names, team_resolver  # noqa: E402

GUARDIAN = {
    "2022-23": ["reports/evidence_guardian_football_2022_23.jsonl"],
    "2023-24": ["reports/evidence_guardian_football_2023_24.jsonl"],
    "2024-25": ["reports/evidence_guardian_football_2024_25.jsonl"],
    "2025-26": ["reports/evidence_guardian_football_2025_26.jsonl"],
    "2026-27": sorted(glob.glob(str(ROOT / "reports/evidence_guardian_football_2627_gw*.jsonl")))
    + ["reports/evidence_guardian_football_2026_prelaunch.jsonl", "reports/evidence_guardian_football_2026_wed.jsonl"],
}
SCOUT = (["reports/evidence_pl_scout_2022_26.jsonl", "reports/evidence_pl_scout_2026_prelaunch.jsonl",
          "reports/evidence_pl_scout_2026_wed.jsonl"] + sorted(glob.glob(str(ROOT / "reports/evidence_pl_scout_2627_gw*.jsonl"))))

CUES = {
    "avail": re.compile(r"team news|injur|press conference|ruled out|\bdoubt|fitness|\bfit\b|suspend|sidelined|line-?ups?|"
                        r"returns? (to|from|for|in)\b|\bscan\b|surgery|hamstring|\bknee\b|ankle|\bgroin|\bcalf\b|out for|"
                        r"(will|could|set to|may|to) miss|rested|rotat|dropped|\bbench|absen|back in (training|contention)|"
                        r"unavailable|setback|\bban\b|banned|\bruled\b|illness|\bill\b|concussion|fractur|operation|recover|"
                        r"\bblow\b|lay-?off|weeks out|months out|out until|available again", re.I),
    "role": re.compile(r"\bstarts?\b|\bstarting\b|captain|penalt|set[- ]piece|new role|pecking order|first[- ]choice|"
                       r"\bno ?9\b|\bno ?10\b|wing-?back|number one|\bkeeper\b|goalkeeper|rotation|position", re.I),
    "sign": re.compile(r"\bsign(s|ed|ing)?\b|\bjoins?\b|completes?|\bloan\b|transfer|\bdeal\b|\bbid\b|\bagrees?\b|\bfee\b|"
                       r"arriv|unveil|swoop|move to|moves to|\bexit\b|leaves?\b|departs?\b", re.I),
}
EXCLUDE_TITLE = re.compile(r"as it happened|live!|– live|player ratings|podcast|football daily|quiz|crossword|fiver|clockwatch|"
                           r"how (we|they) rated|obituary|premier league table|results|golden boot|\bwomen|wsl|lionesses", re.I)
CLUB_ALIAS = {"man city": "football/manchestercity", "man utd": "football/manchester-united", "nott'm forest": "football/nottinghamforest",
              "spurs": "football/tottenham-hotspur", "wolves": "football/wolves", "brighton": "football/brightonfootball",
              "newcastle": "football/newcastleunited", "leeds": "football/leedsunited", "west ham": "football/westhamunited",
              "sheffield utd": "football/sheffieldunited", "luton": "football/lutontown", "leicester": "football/leicestercity",
              "ipswich": "football/ipswichtown", "coventry": "football/coventry", "hull": "football/hullcity"}
SEASON_START = {"2022-23": "2022-07-01", "2023-24": "2023-07-01", "2024-25": "2024-07-01", "2025-26": "2025-07-01", "2026-27": "2026-07-01"}


def norm_slug(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z]", "", s.lower())


def club_tags(season: str, vocab: collections.Counter) -> set[str]:
    """Guardian tag slugs of the season's 20 clubs (derived from teams.csv against the store's tag vocabulary)."""
    out = {"football/premierleague"}
    for r in csv.DictReader(open(ROOT / "data/fpl_history" / season / "teams.csv")):
        name = r["name"]; n = norm_slug(name)
        if name.lower() in CLUB_ALIAS:
            out.add(CLUB_ALIAS[name.lower()]); continue
        cands = [t for t in vocab if t.startswith("football/") and "women" not in t and "fc-" not in t
                 and (norm_slug(t.split("/", 1)[1]).startswith(n[:6]) or n in norm_slug(t.split("/", 1)[1]))]
        if cands:
            out.add(max(cands, key=lambda c: vocab[c]))
    return out


def season_of(ts: dt.datetime) -> str | None:
    for season, start in sorted(SEASON_START.items()):
        s = dt.datetime.fromisoformat(start + "T00:00:00+00:00")
        if s <= ts < s.replace(year=s.year + 1):
            return season
    return None


def doc_id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def load_store(path: str) -> list[dict]:
    p = ROOT / path if not str(path).startswith("/") else Path(path)
    return [json.loads(l) for l in open(p)] if p.exists() else []


def assign(ts: dt.datetime, dl_cache: dict) -> tuple[str, int, float] | None:
    season = season_of(ts)
    if season is None:
        return None
    if season not in dl_cache:
        try:
            dl_cache[season] = deadlines(season)
        except FileNotFoundError:
            dl_cache[season] = {}
    nxt = [(g, x) for g, x in dl_cache[season].items() if x >= ts]
    if not nxt:
        return None
    g, x = min(nxt, key=lambda y: y[1])
    return season, g, (x - ts).total_seconds() / 3600


def classify(title: str, standfirst: str, lead: str) -> str | None:
    """'title:<class>' | 'standfirst:<class>' | 'lead:avail' with avail > role > sign priority, else None.
    The lead tier (first 800 chars) needs two distinct availability cues: one cue there is mostly match-report noise."""
    for where, text in (("title", title), ("standfirst", standfirst)):
        for cls in ("avail", "role", "sign"):
            if text and CUES[cls].search(text):
                return f"{where}:{cls}"
    if lead and len({m.group(0).lower()[:5] for m in CUES["avail"].finditer(lead)}) >= 2:
        return "lead:avail"
    return None


PRIORITY = {"title:avail": 1, "standfirst:avail": 1, "lead:avail": 2, "title:role": 3, "standfirst:role": 3, "title:sign": 4,
            "standfirst:sign": 4}


def route(max_chars: int, classes: set[str]) -> tuple[list[dict], list[dict]]:
    seen: set[str] = set(); prose: list[dict] = []; lineups: list[dict] = []; dl_cache: dict = {}
    for season, paths in GUARDIAN.items():
        docs = [d for p in paths for d in load_store(p)]
        vocab = collections.Counter(t for d in docs for t in (d.get("tags") or []))
        clubs = club_tags(season, vocab)
        for d in docs:
            url = d.get("url") or ""
            if not url or url in seen:
                continue
            seen.add(url)
            title = str(d.get("title") or ""); text = str(d.get("full_text") or d.get("content") or "")
            if not d.get("published_at") or len(text) < 200:
                continue
            ts = dt.datetime.fromisoformat(d["published_at"].replace("Z", "+00:00"))
            a = assign(ts, dl_cache)
            if a is None:
                continue
            s, gw, hours = a
            base = {"doc_id": doc_id(url), "season": s, "gw": gw, "hours_before": round(hours, 1), "published_at": d["published_at"],
                    "source": "guardian", "title": title, "url": url}
            if TITLE.search(title):
                lineups.append({**base, "text": text}); continue
            tags = set(d.get("tags") or [])
            if "/live/" in url or EXCLUDE_TITLE.search(title) or not (tags & clubs) or any("women" in t for t in tags):
                continue
            hit = classify(title, str(d.get("snippet") or ""), text[:800])
            if hit is None or hit.split(":")[1] not in classes:
                continue
            prose.append({**base, "kind": "prose", "hit": hit, "priority": PRIORITY[hit], "text": text[:max_chars]})
    for d in [d for p in SCOUT for d in load_store(p)]:
        url = d.get("url") or ""
        if not url or url in seen:
            continue
        seen.add(url)
        title = str(d.get("title") or ""); text = str(d.get("full_text") or d.get("content") or "")
        if not d.get("published_at") or len(text) < 200:
            continue
        ts = dt.datetime.fromisoformat(d["published_at"].replace("Z", "+00:00"))
        a = assign(ts, dl_cache)
        if a is None:
            continue
        s, gw, hours = a
        hit = classify(title, str(d.get("description") or ""), text[:800])
        if hit is None or hit.split(":")[1] == "sign" or hit.split(":")[1] not in classes:
            continue
        prose.append({"doc_id": doc_id(url), "season": s, "gw": gw, "hours_before": round(hours, 1), "published_at": d["published_at"],
                      "source": "scout", "title": title, "url": url, "kind": "prose", "hit": hit,
                      "priority": 2 if hit.endswith("avail") else 3, "text": text[:max_chars]})
    return prose, lineups


def team_blocks(lineups: list[dict]) -> list[dict]:
    """One row per fixture segment of a predicted-lineups article, with the parser's lists as truth."""
    out = []
    for d in lineups:
        resolve = team_resolver(d["season"]); text = d["text"]
        hdrs = list(HDR.finditer(text))
        for i, m in enumerate(hdrs):
            seg = text[m.start(): hdrs[i + 1].start() if i + 1 < len(hdrs) else len(text)]
            blocks = list(BLOCK.finditer(seg[m.end() - m.start():]))
            if len(blocks) < 2:
                continue
            truth = {}
            for team_name, b in zip((m.group("home"), m.group("away")), blocks[:2]):
                if resolve(team_name) is None:
                    continue
                truth[team_name.strip()] = {"sub": names(b.group("subs")), "doubtful": names(b.group("doubt")),
                                            "injured": names(b.group("inj")), "suspended": names(b.group("susp"))}
            if len(truth) != 2:
                continue
            out.append({**{k: v for k, v in d.items() if k != "text"}, "doc_id": d["doc_id"] + f"_{i:02d}", "kind": "team_block",
                        "text": seg.strip()[:4000], "truth": truth})
    return out


def sample_strata(rows: list[dict], key, n: int, rng: random.Random) -> list[dict]:
    strata = collections.defaultdict(list)
    for r in rows:
        strata[key(r)].append(r)
    keys = sorted(strata); per = max(1, n // max(1, len(keys))); picked = []
    for k in keys:
        pool = sorted(strata[k], key=lambda r: r["doc_id"]); rng.shuffle(pool); picked.extend(pool[:per])
    return picked[:n]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=None)
    ap.add_argument("--classes", default="avail,role")
    ap.add_argument("--max-chars", type=int, default=9000)
    ap.add_argument("--pilot", type=int, default=0, help="sample N prose docs (stratified by season/source) instead of the full scope")
    ap.add_argument("--team-blocks", type=int, default=0, help="add N predicted-lineups fixture segments with parser truth")
    ap.add_argument("--max-hours", type=float, default=168.0, help="pilot prose docs must be within this many hours of the deadline")
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--stats", action="store_true", help="print tier/class counts and sample titles, write nothing")
    args = ap.parse_args()
    classes = set(args.classes.split(",")) if not args.stats else {"avail", "role", "sign"}
    prose, lineups = route(args.max_chars, classes)
    rng = random.Random(args.seed)
    if args.stats:
        by = collections.Counter((r["source"], r["hit"]) for r in prose)
        for k in sorted(by):
            print(f"{k[0]:9s} {k[1]:18s} {by[k]:5d}")
        for hit in sorted({r["hit"] for r in prose}):
            pool = [r for r in prose if r["hit"] == hit]; rng.shuffle(pool)
            print(f"--- {hit} ({len(pool)}) ---")
            for r in pool[:8]:
                print(f"   {r['season']} {r['source']:8s} {r['hours_before']:7.1f}h | {r['title'][:95]}")
        chars = collections.Counter(); n = collections.Counter()
        for r in prose:
            chars[r["hit"].split(":")[1]] += len(r["text"]); n[r["hit"].split(":")[1]] += 1
        print("class docs / ~tokens:", {c: (n[c], chars[c] // 4) for c in n})
        return
    rows: list[dict] = []
    if args.pilot:
        pool = [d for d in prose if d["hours_before"] <= args.max_hours]
        rows = sample_strata(pool, lambda r: (r["season"] if r["source"] == "guardian" else "scout"), args.pilot, rng)
    else:
        rows = sorted(prose, key=lambda r: (r["priority"], r["season"], r["gw"], r["hours_before"]))
    if args.team_blocks:
        rows.extend(sample_strata(team_blocks(lineups), lambda r: r["season"], args.team_blocks, rng))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    by = collections.Counter((r["season"], r["source"], r["kind"]) for r in rows)
    print(f"routed prose {len(prose)} | lineups articles {len(lineups)} | wrote {len(rows)} rows -> {args.out}")
    for k in sorted(by):
        print("  ", k, by[k])
    print("chars total", sum(len(r["text"]) for r in rows), "| ~tokens", sum(len(r["text"]) for r in rows) // 4)


if __name__ == "__main__":
    main()

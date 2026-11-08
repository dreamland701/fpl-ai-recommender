#!/usr/bin/env python3
"""Score the availability-extractor pilot (2026-10-22): Gemma-4-31B-it (nf4) vs Gemma-4-E4B-it vs Haiku on the same
documents and prompt (scripts/extract_availability_facts.py).

Three measurements per arm:
  1. Team blocks (Guardian predicted-lineups fixture segments): the parser's lists are the truth
     (Subs from -> bench, Doubtful -> doubt, Injured/Suspended -> out). Precision/recall of (surname, status) pairs,
     name recall ignoring status, and the status confusion.
  2. Prose documents: pairwise agreement between arms on (surname, status) pairs and on names alone (Jaccard per
     document, averaged over documents where either arm found something), plus facts per document, parse rate,
     truncation rate, seconds per document.
  3. Outcome validity on prose documents: each fact is joined to the player's row in the next gameweek
     (data/fpl_history/<season>/merged_gw.csv, by surname within the season, team-disambiguated when given);
     appearance and start rates by extracted status. Expect: out -> near 0% appearance, xi -> high start rate.
Haiku outputs come from subagents as one JSON file per document under --haiku-dir (<stem>.out.json next to
<stem>.prompt.txt); they are merged into the extractor's row format first.

usage: score_extract_pilot.py --docs reports/extract_facts/pilot_docs.jsonl --pred e4b=... --pred 31b=... \
         [--haiku-dir reports/extract_facts/haiku] --out reports/extract_facts/pilot.md
"""
from __future__ import annotations
import argparse
import collections
import csv
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from extract_availability_facts import STATUSES, parse_facts  # noqa: E402

TRUTH_STATUS = {"sub": "bench", "doubtful": "doubt", "injured": "out", "suspended": "out"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z\- ]", "", s.lower()).strip()


def surname(name: str) -> str:
    toks = [t for t in norm(name).replace("-", " ").split() if len(t) > 1 or t.isalpha()]
    return toks[-1] if toks else ""


def merge_haiku(haiku_dir: Path, out_path: Path) -> dict[str, dict]:
    rows = {}
    for p in sorted(haiku_dir.glob("batch_*/*.prompt.txt")):
        doc_id = p.name.split("_", 2)[2].replace(".prompt.txt", "")
        o = p.with_name(p.name.replace(".prompt.txt", ".out.json"))
        if not o.exists():
            rows[doc_id] = {"doc_id": doc_id, "model": "haiku", "facts": [], "parse_ok": False, "n_facts": 0, "missing": True}
            continue
        facts, ok = parse_facts(o.read_text())
        rows[doc_id] = {"doc_id": doc_id, "model": "haiku", "facts": facts, "parse_ok": ok, "n_facts": len(facts)}
    with open(out_path, "w") as f:
        for r in rows.values():
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    return rows


def load_pred(path: str) -> dict[str, dict]:
    return {r["doc_id"]: r for r in (json.loads(l) for l in open(path))}


def pairs(facts: list[dict]) -> set[tuple[str, str]]:
    return {(surname(f["player"]), f["status"]) for f in facts if surname(f["player"])}


def jaccard(a: set, b: set) -> float | None:
    return None if not a and not b else len(a & b) / len(a | b)


def team_block_scores(docs: list[dict], pred: dict[str, dict]):
    tp = fp = fn = 0; name_hit = name_tot = 0; conf = collections.Counter(); n = 0
    for d in docs:
        r = pred.get(d["doc_id"])
        if r is None:
            continue
        n += 1
        truth = {}
        for team, cats in d["truth"].items():
            for cat, nms in cats.items():
                for nm in nms:
                    if surname(nm):
                        truth[surname(nm)] = TRUTH_STATUS[cat]
        got = {}
        for f in r["facts"]:
            if surname(f["player"]):
                got.setdefault(surname(f["player"]), f["status"])
        for s, st in got.items():
            if s in truth:
                if truth[s] == st:
                    tp += 1
                else:
                    fp += 1; conf[(truth[s], st)] += 1
            else:
                fp += 1; conf[("not listed", st)] += 1
        for s, st in truth.items():
            name_tot += 1
            if s in got:
                name_hit += 1
                if got[s] != st:
                    fn += 1
            else:
                fn += 1; conf[(st, "missed")] += 1
    prec = tp / (tp + fp) if tp + fp else 0.0; rec = tp / (tp + fn) if tp + fn else 0.0
    return {"docs": n, "tp": tp, "fp": fp, "fn": fn, "precision": prec, "recall": rec,
            "name_recall": name_hit / name_tot if name_tot else 0.0, "confusion": conf}


def load_outcomes(season: str) -> dict[tuple[str, int], dict]:
    """(surname, gw) -> {names: {full name: {team, appeared, started}}} from merged_gw.csv."""
    p = ROOT / "data/fpl_history" / season / "merged_gw.csv"
    if not p.exists():
        return {}
    out: dict = collections.defaultdict(dict)
    with open(p, newline="") as f:
        rd = csv.DictReader(f)
        gwcol = "GW" if "GW" in rd.fieldnames else "round"
        for r in rd:
            try:
                gw = int(float(r[gwcol])); mins = int(float(r.get("minutes") or 0)); st = int(float(r.get("starts") or 0))
            except ValueError:
                continue
            key = (surname(r["name"]), gw); rec = out[key].setdefault(r["name"], {"team": r.get("team", ""), "appeared": 0, "started": 0})
            rec["appeared"] = max(rec["appeared"], int(mins > 0)); rec["started"] = max(rec["started"], st)
    return out


def outcome_scores(docs: list[dict], pred: dict[str, dict], cache: dict):
    by = collections.defaultdict(lambda: [0, 0, 0, 0])  # status -> [n, matched, appeared, started]
    for d in docs:
        r = pred.get(d["doc_id"])
        if r is None:
            continue
        if d["season"] not in cache:
            cache[d["season"]] = load_outcomes(d["season"])
        oc = cache[d["season"]]
        for f in r["facts"]:
            st = f["status"] if f["status"] in STATUSES else "other"
            by[st][0] += 1
            cands = oc.get((surname(f["player"]), d["gw"]), {})
            if len(cands) > 1 and f.get("team"):
                t = norm(f["team"]).split()[0] if norm(f["team"]) else ""
                cands = {k: v for k, v in cands.items() if t and t in norm(v["team"])} or cands
            if len(cands) == 1:
                v = next(iter(cands.values())); by[st][1] += 1; by[st][2] += v["appeared"]; by[st][3] += v["started"]
    return by


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", required=True); ap.add_argument("--pred", action="append", default=[])
    ap.add_argument("--haiku-dir", action="append", default=[], help="label=dir of per-document .out.json files (repeatable); a bare dir is labelled haiku")
    ap.add_argument("--out", required=True)
    ap.add_argument("--show", type=int, default=12, help="disagreement cases to print for a hand audit")
    args = ap.parse_args()
    docs = [json.loads(l) for l in open(args.docs)]
    prose = [d for d in docs if d["kind"] == "prose"]; blocks = [d for d in docs if d["kind"] == "team_block"]
    arms: dict[str, dict[str, dict]] = {}
    for spec in args.pred:
        label, path = spec.split("=", 1); arms[label] = load_pred(path)
    for spec in args.haiku_dir:
        label, d = spec.split("=", 1) if "=" in spec else ("haiku", spec)
        arms[label] = merge_haiku(Path(d), Path(d) / "merged.jsonl")
        for r in arms[label].values():
            r["model"] = label
    L = []
    L.append(f"# Extractor pilot: {', '.join(arms)} on {len(prose)} prose documents + {len(blocks)} lineups team blocks\n")
    L.append("## Throughput and form\n")
    L.append("| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |")
    L.append("|---|---|---|---|---|---|---|---|")
    for a, pred in arms.items():
        rows = [pred[d["doc_id"]] for d in docs if d["doc_id"] in pred]
        pr = [pred[d["doc_id"]] for d in prose if d["doc_id"] in pred]
        tout = sorted(r.get("tokens_out", 0) for r in rows); secs = [r["seconds"] for r in rows if "seconds" in r]
        L.append(f"| {a} | {len(rows)} | {sum(r['parse_ok'] for r in rows) / max(1, len(rows)):.0%} | "
                 f"{sum(bool(r.get('truncated')) for r in rows)} | {sum(r['n_facts'] for r in pr) / max(1, len(pr)):.1f} | "
                 f"{sum(r['n_facts'] == 0 for r in pr)} | {tout[len(tout) // 2] if tout else '-'} | "
                 f"{sum(secs) / len(secs):.1f} |" if secs else
                 f"| {a} | {len(rows)} | {sum(r['parse_ok'] for r in rows) / max(1, len(rows)):.0%} | "
                 f"{sum(bool(r.get('truncated')) for r in rows)} | {sum(r['n_facts'] for r in pr) / max(1, len(pr)):.1f} | "
                 f"{sum(r['n_facts'] == 0 for r in pr)} | - | - |")
    L.append("\n## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)\n")
    L.append("| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    for a, pred in arms.items():
        s = team_block_scores(blocks, pred)
        conf = ", ".join(f"{k[0]}->{k[1]} {v}" for k, v in s["confusion"].most_common(4))
        L.append(f"| {a} | {s['docs']} | {s['precision']:.2f} | {s['recall']:.2f} | {s['name_recall']:.2f} | {s['tp']} | {s['fp']} | {s['fn']} | {conf} |")
    L.append("\n## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)\n")
    L.append("| pair | docs | (name, status) | names only |")
    L.append("|---|---|---|---|")
    labels = list(arms)
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            a, b = labels[i], labels[j]; js = []; jn = []
            for d in prose:
                ra, rb = arms[a].get(d["doc_id"]), arms[b].get(d["doc_id"])
                if ra is None or rb is None:
                    continue
                pa, pb = pairs(ra["facts"]), pairs(rb["facts"])
                v = jaccard(pa, pb)
                if v is not None:
                    js.append(v); jn.append(jaccard({x for x, _ in pa}, {x for x, _ in pb}))
            L.append(f"| {a} vs {b} | {len(js)} | {sum(js) / max(1, len(js)):.2f} | {sum(jn) / max(1, len(jn)):.2f} |")
    L.append("\n## Outcome validity on prose documents (facts joined to the next gameweek's minutes)\n")
    L.append("| arm | status | facts | matched to a player | appeared | started |")
    L.append("|---|---|---|---|---|---|")
    cache: dict = {}
    for a, pred in arms.items():
        by = outcome_scores(prose, pred, cache)
        for st in list(STATUSES) + ["other"]:
            n, m, ap_, st_ = by.get(st, [0, 0, 0, 0])
            if n:
                L.append(f"| {a} | {st} | {n} | {m} | {ap_ / m:.0%} | {st_ / m:.0%} |" if m else f"| {a} | {st} | {n} | 0 | - | - |")
    L.append(f"\n## Disagreement cases for a hand audit (first {args.show})\n")
    shown = 0
    for d in prose:
        sets = {a: pairs(arms[a][d["doc_id"]]["facts"]) for a in arms if d["doc_id"] in arms[a]}
        if len(sets) < 2 or len({frozenset(s) for s in sets.values()}) == 1:
            continue
        L.append(f"**{d['season']} GW{d['gw']} {d['source']} {d['hours_before']}h** {d['title'][:100]}  ")
        for a in sets:
            facts = arms[a][d["doc_id"]]["facts"]
            L.append(f"- {a}: " + ("; ".join(f"{f['player']} [{f['status']}] {f['detail']}" for f in facts[:10]) or "(none)") + "  ")
        L.append("")
        shown += 1
        if shown >= args.show:
            break
    Path(args.out).write_text("\n".join(L) + "\n")
    print("\n".join(L[:40]))
    print(f"... -> {args.out}")


if __name__ == "__main__":
    main()

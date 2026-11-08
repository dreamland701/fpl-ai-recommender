#!/usr/bin/env python
"""Audit the text evidence inside an SFT corpus (2026-10-18, Wes: "how good are the articles going into SFT?").

For every prompt: evidence docs (source, timestamp, title, snippet), coverage, recency vs deadline, whether the
snippet names the player, availability / lineup cues, duplication across players, and ACTIONABILITY: on rows where
the outcome surprised the classic signal (nailed starter who did not play / was benched) how often the pre-deadline
text named the player with an availability cue, against the same rate on unsurprising rows.
usage: sft_article_audit.py --corpus <dir> [--corpus <dir> ...] --out reports/sft_article_audit
"""
import argparse, collections, json, re, unicodedata
from pathlib import Path
import numpy as np, pandas as pd

DOC = re.compile(r"\[(\d+)\] (.+?) \| (\S+)\nTitle: (.*?)\nText: (.*?)(?=\n\n\[\d+\] |\n<\|turn>|\Z)", re.S)
AVAIL = re.compile(r"\b(injur|doubt|ruled out|out for|out of|miss(es|ed|ing)?\b|sidelined|fitness|knock|suspend|banned?\b|rested|rest\b|rotat|benched|dropped|unavailable|return(s|ed|ing)?\b|back in training|fit\b|fit to|will start|starts?\b|starting|line-?up|\bxi\b|team news|setback|surgery|hamstring|groin|ankle|calf|thigh|illness|\bill\b|concussion|withdrawn|substitut|limped|scan)", re.I)
LIVEBLOG = re.compile(r"as it happened|live!|live blog|minute-by-minute|clockwatch", re.I)
TEAMNEWS = re.compile(r"team news|predicted line-?ups?|injury (news|update|latest)|press conference|confirms|ruled out|doubt", re.I)

def norm(s): return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()

def parse(row):
    p = row["prompt"]; m = row["metadata"]; docs = []
    block = p.split("Timestamp-safe text evidence:", 1)
    if len(block) == 2:
        for n, src, ts, title, text in DOC.findall(block[1]):
            docs.append({"n": int(n), "source": src.strip(), "ts": ts, "title": title.strip(), "text": text.strip()})
    status = re.search(r"Status pre-deadline: (\S+)", p); news = re.search(r"Official player news pre-deadline: (.*)", p)
    return docs, (status.group(1) if status else ""), (news.group(1).strip() if news else "")

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--corpus", action="append", required=True); ap.add_argument("--out", default="reports/sft_article_audit"); a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    rows, docrows = [], []
    for cdir in a.corpus:
        for split in ("train", "eval", "live_eval"):
            f = Path(cdir) / f"{split}.jsonl"
            if not f.is_file(): continue
            for line in open(f):
                r = json.loads(line); m = r["metadata"]; docs, status, news = parse(r)
                name = m["player_name"]; sur = norm(name).split()[-1] if name else ""; full = norm(name)
                dl = pd.Timestamp(m["deadline_ts"]); lab = m.get("labels", {}); base = m.get("baseline_forecast", {})
                ndoc = len(docs); mention = 0; avail = 0; ages = []; dup_keys = []
                for d in docs:
                    t = norm(d["title"] + " " + d["text"]); men = (sur and sur in t) or (full and full in t)
                    cue = bool(AVAIL.search(d["text"])) ; mention += men; avail += (men and cue)
                    try: ages.append((dl - pd.Timestamp(d["ts"])).total_seconds() / 3600)
                    except Exception: ages.append(np.nan)
                    docrows.append({"corpus": Path(cdir).name[-28:], "split": split, "season": m["season"], "week": m["week"], "player": name, "source": d["source"], "age_h": ages[-1], "chars": len(d["text"]), "mention": men, "cue": cue, "liveblog": bool(LIVEBLOG.search(d["title"])), "teamnews": bool(TEAMNEWS.search(d["title"] + " " + d["text"][:200])), "key": (m["season"], m["week"], d["source"], d["ts"], d["title"])})
                rows.append({"corpus": Path(cdir).name[-28:], "split": split, "season": m["season"], "week": m["week"], "player": name, "status": status, "news": news, "ndoc": ndoc, "mention": mention, "avail": avail, "min_age": np.nanmin(ages) if ages and not all(np.isnan(ages)) else np.nan,
                             "b_app": base.get("baseline_appearance_probability", np.nan), "b_min": base.get("baseline_minutes_1gw", np.nan), "b_pts": base.get("baseline_points_1gw", np.nan), "l_min": lab.get("minutes_1gw", np.nan), "l_pts": lab.get("points_1gw", np.nan)})
    R = pd.DataFrame(rows); D = pd.DataFrame(docrows)
    L = [f"# SFT article audit ({', '.join(a.corpus)})\n", f"Rows {len(R)} (train {int((R.split=='train').sum())}, eval {int((R.split=='eval').sum())}, live {int((R.split=='live_eval').sum())}); docs {len(D)}.\n"]
    L.append("## Coverage, recency, relevance\n\n| split | rows | rows with ≥1 doc | docs/row (mean) | docs naming the player | …with an availability cue | median age of newest doc (h) | docs ≤24 h | docs ≤72 h | liveblog/match-report docs | snippet chars (median) |\n|---|---|---|---|---|---|---|---|---|---|---|")
    for split, g in R.groupby("split", sort=False):
        d = D[D.split == split]
        L.append(f"| {split} | {len(g)} | {(g.ndoc>0).mean():.2f} | {g.ndoc.mean():.2f} | {d.mention.mean() if len(d) else float('nan'):.2f} | {(d.mention & d.cue).mean() if len(d) else float('nan'):.2f} | {g.min_age.median():.0f} | {(d.age_h<=24).mean() if len(d) else float('nan'):.2f} | {(d.age_h<=72).mean() if len(d) else float('nan'):.2f} | {d.liveblog.mean() if len(d) else float('nan'):.2f} | {d.chars.median() if len(d) else float('nan'):.0f} |")
    L.append("\n## By season (train+eval)\n\n| season | rows | rows with docs | docs/row | docs naming player | availability-cue docs | newest doc age median (h) |\n|---|---|---|---|---|---|---|")
    for s, g in R.groupby("season"):
        d = D[D.season == s]; L.append(f"| {s} | {len(g)} | {(g.ndoc>0).mean():.2f} | {g.ndoc.mean():.2f} | {d.mention.mean() if len(d) else float('nan'):.2f} | {(d.mention & d.cue).mean() if len(d) else float('nan'):.2f} | {g.min_age.median():.0f} |")
    L.append("\n## Sources\n\n| source | docs | share | naming player | availability cue | median age (h) | liveblog |\n|---|---|---|---|---|---|---|")
    for src, d in D.groupby("source"):
        if len(d) < 20: continue
        L.append(f"| {src} | {len(d)} | {len(d)/len(D):.3f} | {d.mention.mean():.2f} | {(d.mention & d.cue).mean():.2f} | {d.age_h.median():.0f} | {d.liveblog.mean():.2f} |")
    dup = D.groupby("key").size(); L.append(f"\n## Duplication\n\nDistinct docs {len(dup)} for {len(D)} doc slots: a doc appears in {dup.mean():.1f} prompts on average (max {dup.max()}); {(dup>=5).mean():.2f} of distinct docs sit in ≥5 players' prompts of the same week.\n")
    # actionability
    L.append("## Actionability: did the text say it before it happened?\n")
    R["grp"] = "other"
    nailed = (R.b_app >= 0.75) & (R.b_min >= 60)
    R.loc[nailed & (R.l_min == 0), "grp"] = "nailed starter, did NOT play"
    R.loc[nailed & (R.l_min > 0) & (R.l_min < 45), "grp"] = "nailed starter, <45 min"
    R.loc[nailed & (R.l_min >= 60), "grp"] = "nailed starter, played ≥60"
    R.loc[(R.b_app < 0.5) & (R.l_min >= 60), "grp"] = "unexpected starter (P<0.5, ≥60 min)"
    L.append("| group (status 'a' rows only, i.e. the flag did not warn) | rows | any doc | doc names player | names player + availability cue |\n|---|---|---|---|---|")
    for grp in ["nailed starter, played ≥60", "nailed starter, <45 min", "nailed starter, did NOT play", "unexpected starter (P<0.5, ≥60 min)"]:
        g = R[(R.grp == grp) & (R.status == "a")]
        if len(g): L.append(f"| {grp} | {len(g)} | {(g.ndoc>0).mean():.2f} | {(g.mention>0).mean():.2f} | {(g.avail>0).mean():.2f} |")
    L.append("\nSame groups, all statuses:\n\n| group | rows | flagged (status≠a) | any doc | names player + cue |\n|---|---|---|---|---|")
    for grp in ["nailed starter, played ≥60", "nailed starter, <45 min", "nailed starter, did NOT play", "unexpected starter (P<0.5, ≥60 min)"]:
        g = R[R.grp == grp]
        if len(g): L.append(f"| {grp} | {len(g)} | {(g.status!='a').mean():.2f} | {(g.ndoc>0).mean():.2f} | {(g.avail>0).mean():.2f} |")
    # by source: hit rate on the surprise group
    sg = R[(R.grp == "nailed starter, did NOT play") & (R.status == "a")][["season", "week", "player"]]
    if len(sg):
        key = set(map(tuple, sg.to_numpy())); d = D[[ (s, w, p) in key for s, w, p in zip(D.season, D.week, D.player)]]
        L.append("\nDocs attached to the 'nailed starter, did NOT play' rows, by source:\n\n| source | docs | naming player | with cue |\n|---|---|---|---|")
        for src, dd in d.groupby("source"): L.append(f"| {src} | {len(dd)} | {dd.mention.mean():.2f} | {(dd.mention & dd.cue).mean():.2f} |")
    (out / "summary.md").write_text("\n".join(L) + "\n"); R.to_csv(out / "rows.csv", index=False); D.drop(columns=["key"]).to_csv(out / "docs.csv", index=False)
    print("\n".join(L))

if __name__ == "__main__":
    main()

"""Does the Premier League Scout know something the classic model doesn't?

For every player-week in the SFT corpora (2022-23 to 2025-26 GW26 training rows, the 2025-26
GW27-38 holdout, 2026-27 GW2-5; the classic forecast is walk-forward in all of them), rows whose
prompt carries a Scout article from the Premier League site (Scout picks, captaincy, ones to watch,
tips) are compared with rows that have no Premier League article, at the same classic forecast
(0.5-point bins, same season). If the Scout adds information, Scout-mentioned players should beat
their classic forecast by more than similar unmentioned players do.

usage: scout_signal.py
"""
import json
import re
from collections import defaultdict

import numpy as np

ROOT = "/home/wescheng/projects/fpl/fpl"
FILES = [f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/train.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl"]
DOC = re.compile(r"\n\[\d+\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)")
SUBTYPES = [("Scout Selection (the Scout's XI)", r"scout selection"),
            ("Captaincy articles", r"captain"),
            ("Ones to watch / differentials / experts", r"ones to watch|differential|experts|bargain|budget"),
            ("Other Scout / FPL tips", r".")]


def main() -> None:
    rows = []
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            docs = DOC.findall("\n" + r["prompt"].split("Timestamp-safe text evidence:", 1)[-1])
            pl = [t.lower() for s, ts, t in docs if s.strip().startswith("Premier League")
                  and not re.search(r"price|most.?bought|most.?sold|risers|fallers|injur|team news", t.lower())]
            sub = None
            if pl:
                sub = next(name for name, pat in SUBTYPES if any(re.search(pat, t) for t in pl))
            rows.append((m["season"], int(r["week"]), float(m["baseline_forecast"]["baseline_points_1gw"]),
                         float(m["labels"]["points_1gw"]), float(m["labels"]["minutes_1gw"]) > 0,
                         bool(pl), sub, any(s.strip().startswith("Premier League") for s, _, _ in docs)))
    season = np.array([r[0] for r in rows]); base = np.array([r[2] for r in rows]); act = np.array([r[3] for r in rows])
    played = np.array([r[4] for r in rows]); scout = np.array([r[5] for r in rows]); sub = np.array([r[6] or "" for r in rows])
    any_pl = np.array([r[7] for r in rows])
    resid = act - base
    binned = np.round(base * 2) / 2
    control = ~any_pl
    expected = defaultdict(list)
    for s, b, e in zip(season[control], binned[control], resid[control]):
        expected[(s, b)].append(e)
    exp_resid = np.array([np.mean(expected[(s, b)]) if len(expected.get((s, b), [])) >= 10 else np.nan for s, b in zip(season, binned)])
    excess = resid - exp_resid
    ok = ~np.isnan(excess)
    print(f"player-weeks: {len(rows)}; with a Scout article: {scout.sum()} ({scout.mean():.0%})")
    print(f"classic forecast, Scout-mentioned vs not: {base[scout].mean():.2f} vs {base[~scout].mean():.2f} points "
          f"(Scout-mentioned players are already the ones classic rates highly)")
    for label, sel in [("All Scout-mentioned", scout & ok)] + [(n, (sub == n) & ok) for n, _ in SUBTYPES]:
        if sel.sum() < 30:
            continue
        e = excess[sel]
        print(f"  {label:42s} n {sel.sum():5d} | beat classic by {e.mean():+.2f} pts vs similar unmentioned players "
              f"(se {e.std() / np.sqrt(len(e)):.2f}) | raw surprise {resid[sel].mean():+.2f} | played {played[sel].mean():.0%}")
    print("  by season (all Scout-mentioned):")
    for s in sorted(set(season)):
        sel = scout & ok & (season == s)
        if sel.sum() >= 30:
            e = excess[sel]
            print(f"    {s}: {e.mean():+.2f} (se {e.std() / np.sqrt(len(e)):.2f}, n {sel.sum()})")
    # are Scout picks better than classic at ranking within the top of the market?
    top = ok & (base >= 4)
    for label, sel in (("classic >= 4, Scout-mentioned", top & scout), ("classic >= 4, not mentioned", top & ~any_pl)):
        print(f"  {label:32s} n {sel.sum():4d} | surprise {resid[sel].mean():+.2f} (se {resid[sel].std() / np.sqrt(max(sel.sum(), 1)):.2f})")


if __name__ == "__main__":
    main()

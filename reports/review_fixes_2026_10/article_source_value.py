"""Which kinds of article help the SFT? Out-of-sample, by article type.

For every player-week in the 2025-26 holdout (GW27-38) and the 2026-27 live weeks (GW2-5), with
E20's forecasts and the real outcome, rows are grouped by the types of article in the prompt
(a row with two types counts in both). Per type:
  - points: does the SFT's player-specific adjustment (its average delta minus that week's generic
    shrink, a straight-line fit on the classic forecast) point the same way as the real surprise
    (actual - classic)? Correlation, and the RMSE of classic vs classic + SFT average.
  - availability: AUC for "played at all" of classic P(appear) vs the SFT's P(appear).
  - how many of the type's articles come from the last 24 h before the deadline, which a live
    decision (snapshot ~17 h before) never sees.
Rows without any article are the reference.

usage: article_source_value.py <out.md>
"""
import json
import re
import sys
from collections import defaultdict
from datetime import datetime

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

ROOT = "/home/wescheng/projects/fpl/fpl"
SETS = [
    ("holdout", f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl",
     f"{ROOT}/reports/gemma4_e4b_residual_e20_gw27_38_sft_predictions.jsonl",
     f"{ROOT}/reports/gemma4_e4b_residual_e20_gw27_38_expectation_predictions.jsonl"),
    ("live", f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl",
     f"{ROOT}/reports/gemma4_e4b_residual_e20_2627_gw2_5_sft_predictions.jsonl",
     f"{ROOT}/reports/gemma4_e4b_residual_e20_2627_gw2_5_expectation_predictions.jsonl"),
]
DOC = re.compile(r"\n\[\d+\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)")
TYPES = [  # first match wins
    ("Guardian: team news / predicted line-ups", lambda s, t: "team news" in t),
    ("PL site: injury and team news", lambda s, t: s.startswith("Premier League") and re.search(r"injur|team news|press conference|ruled out|fitness|doubt", t) is not None),
    ("PL site: price changes and transfer trends", lambda s, t: s.startswith("Premier League") and re.search(r"price|most.?bought|most.?sold|transfers in|risers|fallers", t) is not None),
    ("PL site: Scout picks, captaincy, tips", lambda s, t: s.startswith("Premier League")),
    ("Guardian: international matches", lambda s, t: re.search(r"nations league|world cup|qualif|euro 20|friendly|international", t) is not None),
    ("Guardian: transfer news", lambda s, t: "transfer" in t),
    ("Guardian: previews and talking points", lambda s, t: re.search(r"preview|talking points|things we learned|analysis|ratings", t) is not None),
    ("Guardian: live blogs (as it happened)", lambda s, t: re.search(r"as it happened|live", t) is not None),
    ("Guardian: match reports", lambda s, t: re.search(r"\d+-\d+", t) is not None),
    ("Guardian: other news", lambda s, t: True),
]


def auc(score, label):
    order = np.argsort(score)
    ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool)
    n1, n0 = pos.sum(), (~pos).sum()
    return float((ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)) if n1 and n0 else float("nan")


def load(path):
    out = {}
    for line in open(path):
        p = json.loads(line)
        out[(str(p["season"]), int(p["week"]), int(p["metadata"]["player_id"]))] = parse_delta_response(p["response"]) or {}
    return out


def main() -> None:
    rows = []
    for name, ex, g, e in SETS:
        greedy, expected = load(g), load(e)
        for line in open(ex):
            r = json.loads(line); m = r["metadata"]
            k = (str(r["season"]), int(r["week"]), int(m["player_id"]))
            b = m["baseline_forecast"]; lab = m["labels"]
            deadline = datetime.fromisoformat(r["deadline_ts"].replace("Z", "+00:00"))
            docs = DOC.findall("\n" + r["prompt"].split("Timestamp-safe text evidence:", 1)[-1])
            types, late = set(), defaultdict(list)
            for src, ts, title in docs:
                tname = next(n for n, f in TYPES if f(src.strip(), title.lower()))
                types.add(tname)
                late[tname].append((deadline - datetime.fromisoformat(ts.replace("Z", "+00:00"))).total_seconds() < 86400)
            rows.append({"set": name, "week": (name, int(r["week"])), "base": b["baseline_points_1gw"],
                         "avg": expected[k].get("delta_points_1gw", 0.0), "actual": lab["points_1gw"],
                         "p_classic": b["baseline_appearance_probability"],
                         "p_sft": min(1.0, max(0.0, b["baseline_appearance_probability"] + greedy[k].get("delta_appearance_probability", 0.0))),
                         "played": float(lab["minutes_1gw"]) > 0, "types": types, "late": late})
    # player-specific part: remove each week's straight-line shrink on the classic forecast
    by_week = defaultdict(list)
    for i, r in enumerate(rows):
        by_week[r["week"]].append(i)
    for idx in by_week.values():
        base = np.array([rows[i]["base"] for i in idx]); avg = np.array([rows[i]["avg"] for i in idx])
        slope, icpt = np.polyfit(base, avg, 1)
        for i in idx:
            rows[i]["specific"] = rows[i]["avg"] - (slope * rows[i]["base"] + icpt)
    groups = [("No article (reference)", lambda r: not r["types"])] + [(n, (lambda n: lambda r: n in r["types"])(n)) for n, _ in TYPES]
    lines = ["# Which article types help the SFT? (out of sample: 2025-26 GW27-38 + 2026-27 GW2-5, E20)", "",
             "| Article type | Player-weeks | Articles from last 24 h | Points: SFT signal vs real surprise (corr) | "
             "Points RMSE classic → SFT average | Availability AUC classic → SFT |", "|---|---|---|---|---|---|"]
    for name, sel in groups:
        g = [r for r in rows if sel(r)]
        if len(g) < 40:
            continue
        spec = np.array([r["specific"] for r in g]); resid = np.array([r["actual"] - r["base"] for r in g])
        base = np.array([r["base"] for r in g]); avg = np.array([r["avg"] for r in g]); act = np.array([r["actual"] for r in g])
        corr = float(np.corrcoef(spec, resid)[0, 1])
        se = 1 / np.sqrt(len(g) - 3)
        rm = lambda x: float(np.sqrt(np.mean((x - act) ** 2)))  # noqa: E731
        played = np.array([r["played"] for r in g])
        a_c = auc(np.array([r["p_classic"] for r in g]), played); a_s = auc(np.array([r["p_sft"] for r in g]), played)
        late = [x for r in g for x in r["late"].get(name, [])]
        late_share = f"{np.mean(late):.0%}" if late else "–"
        lines.append(f"| {name} | {len(g)} | {late_share} | {corr:+.3f} (±{1.96 * se:.3f}) | {rm(base):.3f} → {rm(base + avg):.3f} | {a_c:.3f} → {a_s:.3f} |")
    lines += ["", "Correlation: between the SFT's player-specific adjustment and the real surprise; ± is the 95% interval. "
              "A type helps if that correlation is clearly above zero and the SFT's availability AUC beats classic's."]
    open(sys.argv[1], "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

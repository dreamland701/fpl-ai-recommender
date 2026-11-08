"""Does the classic model already capture what the articles say?

Simple, transparent signals are read from each player's article snippets (only articles published
at least 12 h before the deadline, as a live decision would have): injury/doubt words, return/fitness
words, suspension words, a Guardian team-news piece, a Premier League Scout mention. Then, holding
out one season at a time (fit on the others), they are added on top of the classic forecast:
  - availability: logistic regression of "played" on logit(classic P(appear)) [+ text signals]
  - points: linear regression of the surprise (actual - classic) on the text signals
If the text signals add nothing out of season, the classic model already has that information.

usage: classic_covers_text.py <out.md>
"""
import json
import re
import sys
from datetime import datetime

import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression

ROOT = "/home/wescheng/projects/fpl/fpl"
FILES = [f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/train.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl"]
DOC = re.compile(r"\n\[\d+\] ([^|\n]+)\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\nTitle: ([^\n]*)\nText: ([^\n]*)")
SIGNALS = {
    "injury / doubt words": r"injur|doubt|ruled out|out for|hamstring|knee|ankle|thigh|groin|calf|knock|fitness test|sidelined|scan|illness|limp",
    "return / fit words": r"back in training|returned to training|fit again|available again|back from injury|recovered|return(s|ed)? to (the )?(squad|side|team)",
    "suspension words": r"suspen|red card|ban(ned)?\b|sent off",
    "rotation / bench words": r"rotat|benched|on the bench|dropped|left out|rested|substitute",
    "Guardian team-news piece": None,
    "Premier League Scout mention": None,
}


def features(prompt, deadline):
    docs = [d for d in DOC.findall("\n" + prompt.split("Timestamp-safe text evidence:", 1)[-1])
            if deadline is None or (deadline - datetime.fromisoformat(d[1].replace("Z", "+00:00"))).total_seconds() >= 12 * 3600]
    text = " ".join(d[3].lower() for d in docs)
    out = []
    for name, pat in SIGNALS.items():
        if name == "Guardian team-news piece":
            out.append(float(any("team news" in d[2].lower() for d in docs)))
        elif name == "Premier League Scout mention":
            out.append(float(any(d[0].strip().startswith("Premier League") for d in docs)))
        else:
            out.append(float(re.search(pat, text) is not None))
    return out


def auc(score, label):
    order = np.argsort(score); ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool); n1, n0 = pos.sum(), (~pos).sum()
    return float((ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def main() -> None:
    S, X, P, B, Y, M = [], [], [], [], [], []
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            d = r.get("deadline_ts")
            deadline = datetime.fromisoformat(str(d).replace("Z", "+00:00")) if isinstance(d, str) and d not in ("", "nan") else None
            S.append(m["season"]); X.append(features(r["prompt"], deadline))
            P.append(m["baseline_forecast"]["baseline_appearance_probability"]); B.append(m["baseline_forecast"]["baseline_points_1gw"])
            Y.append(m["labels"]["points_1gw"]); M.append(float(m["labels"]["minutes_1gw"]) > 0)
    S, X, P, B, Y, M = np.array(S), np.array(X), np.array(P), np.array(B), np.array(Y), np.array(M)
    logit = np.log(np.clip(P, 0.01, 0.99) / (1 - np.clip(P, 0.01, 0.99)))
    lines = ["# Does the classic model already capture what the articles say?", "",
             f"{len(Y)} player-weeks, 2022-23 to 2026-27 GW5; articles at least 12 h before the deadline only.", "",
             "How often each signal fires, and what happens next relative to classic:", "",
             "| Signal | Fires on | Played (fires / not) | Classic P(appear) (fires / not) | Surprise vs classic (fires / not) |",
             "|---|---|---|---|---|"]
    resid = Y - B
    for j, name in enumerate(SIGNALS):
        f = X[:, j] > 0
        lines.append(f"| {name} | {f.mean():.1%} | {M[f].mean():.0%} / {M[~f].mean():.0%} | {P[f].mean():.0%} / {P[~f].mean():.0%} | "
                     f"{resid[f].mean():+.2f} / {resid[~f].mean():+.2f} |")
    lines += ["", "Out of season (fit on the other seasons, score the held-out one):", "",
              "| Held-out season | Rows | Availability AUC: classic → classic + text | Points RMSE: classic → classic + text |", "|---|---|---|---|"]
    for season in sorted(set(S)):
        te = S == season; tr = ~te
        if te.sum() < 300:
            continue
        base = LogisticRegression(max_iter=1000).fit(logit[tr, None], M[tr])
        full = LogisticRegression(max_iter=1000).fit(np.column_stack([logit[tr], X[tr]]), M[tr])
        a0 = auc(base.predict_proba(logit[te, None])[:, 1], M[te]); a1 = auc(full.predict_proba(np.column_stack([logit[te], X[te]]))[:, 1], M[te])
        reg = LinearRegression().fit(X[tr], resid[tr])
        r0 = np.sqrt(np.mean(resid[te] ** 2)); r1 = np.sqrt(np.mean((resid[te] - reg.predict(X[te])) ** 2))
        lines.append(f"| {season} | {te.sum()} | {a0:.3f} → {a1:.3f} ({a1 - a0:+.3f}) | {r0:.3f} → {r1:.3f} ({r1 - r0:+.3f}) |")
    full = LogisticRegression(max_iter=1000).fit(np.column_stack([logit, X]), M)
    reg = LinearRegression().fit(X, resid)
    lines += ["", "Fitted on all seasons (direction of each signal, beyond classic):", "",
              "| Signal | Availability log-odds | Points surprise |", "|---|---|---|"]
    for j, name in enumerate(SIGNALS):
        lines.append(f"| {name} | {full.coef_[0][j + 1]:+.2f} | {reg.coef_[j]:+.2f} |")
    open(sys.argv[1], "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

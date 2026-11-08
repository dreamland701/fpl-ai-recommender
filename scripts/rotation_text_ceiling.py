#!/usr/bin/env python3
"""Rotation risk: what the numbers carry vs what the best text carries (Wes, 2026-10-28, Calafiori).

Question: a player who has started the last three games reads as nailed to the minutes head. Does (a) his
prior-season rotation profile and (b) the Guardian's predicted-lineup article for THIS week predict that he
does not start, and how much of the surprise non-starts could any text reader have foreseen?

Rows: data/fpl_training_rows_v3_contract_f6_teamnews.csv (F16 table: gn_xi/gn_sub/gn_doubtful/gn_out from the
Guardian predicted-lineups article, gn_article = an article existed inside 72 h of the deadline).
Nailed-looking = started all of the last three games with >= 75 min on average and no status flag at the deadline.
Started = label_minutes_1gw >= 60. Prior-season profile keyed on `code` (player_id is re-used across seasons).

Output: reports/gw9_packet_2026_10/rotation_text_ceiling.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "data/fpl_training_rows_v3_contract_f6_teamnews.csv"
OUT = ROOT / "reports/gw9_packet_2026_10/rotation_text_ceiling.md"
SEASONS = ["2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]


def summ(df: pd.DataFrame, by) -> pd.DataFrame:
    g = df.groupby(by, observed=True).agg(rows=("started", "size"), non_start=("started", lambda s: 1 - s.mean()),
                                          mins=("label_minutes_1gw", "mean"), pts=("label_points_1gw", "mean"))
    g["se"] = np.sqrt(g.non_start * (1 - g.non_start) / g.rows)
    return g


def md(g: pd.DataFrame, key: str) -> list[str]:
    lines = [f"| {key} | n | non-start rate | ± | minutes | points |", "|---|---|---|---|---|---|"]
    for idx, r in g.iterrows():
        k = " / ".join(map(str, idx)) if isinstance(idx, tuple) else str(idx)
        lines.append(f"| {k} | {int(r.rows)} | {r.non_start:.3f} | {2 * r.se:.3f} | {r.mins:.1f} | {r.pts:.2f} |")
    return lines + [""]


def main() -> None:
    t = pd.read_csv(TABLE, low_memory=False)
    t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    t = t.dropna(subset=["code"]).copy()
    t["code"] = t.code.astype(int)
    t["started"] = (t.label_minutes_1gw >= 60).astype(int)
    prev = {s: SEASONS[i - 1] for i, s in enumerate(SEASONS) if i > 0}
    art = t[t.gn_article == 1]
    prof = art.groupby(["season", "code"]).agg(p_art_weeks=("gn_sub", "size"), p_sub_share=("gn_sub", "mean")).reset_index()
    st = t.groupby(["season", "code"]).agg(p_start_share=("label_minutes_1gw", lambda s: (s >= 60).mean())).reset_index()
    prof = prof.merge(st, on=["season", "code"])
    prof["season"] = prof.season.map({v: k for k, v in prev.items()})  # profile of season S attaches to rows of S+1
    prof = prof.dropna(subset=["season"])
    t = t.merge(prof, on=["season", "code"], how="left")
    flag = t.status_flag_pre_deadline.fillna(0)
    nailed = (t.minutes_avg_3 >= 75) & (t.starts_avg_3 >= 0.99) & (flag == 0) & t.season.isin(SEASONS[1:])
    n = t[nailed].copy()
    n["gn_cat"] = np.select([n.gn_article == 0, n.gn_xi == 1, n.gn_sub == 1, n.gn_doubtful == 1, n.gn_out == 1],
                            ["no article", "XI", "sub", "doubtful", "out"], "article, unlisted")
    lines = ["# Rotation risk: numbers vs text (nailed-looking players, 2023-24 to 2026-27 GW8)", "",
             f"{len(n)} player-weeks that looked nailed at the deadline (started the last three with >= 75 min, unflagged). "
             "Non-start = under 60 minutes. ± is 2 standard errors.", "",
             "## 1. This week's Guardian predicted lineup (the best text we have)", ""]
    lines += md(summ(n, "gn_cat"), "Guardian category")
    ns = n[n.started == 0]
    wa = ns[ns.gn_article == 1]
    fore = wa.gn_cat.isin(["sub", "doubtful", "out"]).mean()
    lines += [f"Of the {len(ns)} surprise non-starts, {len(wa)} ({(ns.gn_article == 1).mean():.0%}) had an article; "
              f"the article had foreseen {fore:.1%} of those (sub / doubtful / out), and listed {(wa.gn_cat == 'XI').mean():.1%} in the XI.", ""]
    for lab, m in [("defenders", n.position == "DEF"), ("2025-26", n.season == "2025-26"), ("2026-27", n.season == "2026-27")]:
        s = n[m]; sn = s[s.started == 0]; swa = sn[sn.gn_article == 1]
        f = swa.gn_cat.isin(["sub", "doubtful", "out"]).mean() if len(swa) else float("nan")
        lines.append(f"- {lab}: {len(s)} nailed rows, non-start rate {1 - s.started.mean():.3f}; {len(swa)} non-starts with an article, "
                     f"{f:.1%} foreseen; article present on {(s.gn_article == 1).mean():.0%} of rows.")
    lines += ["", "## 2. Prior-season rotation profile (share of last season's articles listing the player as a sub)", ""]
    p = n[n.p_art_weeks.ge(10)].copy()
    p["prior_rotation"] = pd.cut(p.p_sub_share, [-0.01, 0.1, 0.25, 0.5, 1.0], labels=["sub < 10%", "10-25%", "25-50%", "50%+"])
    p["prior_starts"] = pd.cut(p.p_start_share, [-0.01, 0.4, 0.6, 0.8, 1.0], labels=["< 40%", "40-60%", "60-80%", "80%+"])
    lines += md(summ(p, "prior_rotation"), "prior-season sub share")
    lines += ["Defenders only:", ""] + md(summ(p[p.position == "DEF"], "prior_rotation"), "prior-season sub share")
    lines += ["Weeks 1-10 only:", ""] + md(summ(p[p.week <= 10], "prior_rotation"), "prior-season sub share")
    lines += ["By prior-season start share:", ""] + md(summ(p, "prior_starts"), "prior-season start share")
    lines += ["## 3. Both together", ""]
    lines += md(summ(p[p.gn_cat.isin(["XI", "sub"])], ["prior_rotation", "gn_cat"]), "prior sub share / this week's article")
    c = t[(t.code == 466075) & (t.season == "2026-27")].head(1)
    if len(c):
        r = c.iloc[0]
        lines.append(f"Calafiori's 2026-27 profile: prior-season sub share {r.p_sub_share:.2f} over {int(r.p_art_weeks)} articles, "
                     f"prior start share {r.p_start_share:.2f}.")
    lines += ["", "Caveat: these are raw rates, not residuals against the model's forecast; the controlled version (excess vs same-forecast peers) "
              "is in minutes_prior_study.md, where the same gradient is about 2-3 minutes and 0.1-0.2 points a week for defenders."]
    OUT.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())

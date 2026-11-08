"""Do players start and score less in the first gameweek after an international break?

Post-break GWs are those whose first kickoff comes 12-30 days after the previous
GW's last kickoff (international windows; the 2022 World Cup and 2020 COVID gaps
are excluded by the 30-day cap). For regular starters going into the week
(60+ minutes in each of their last three appearances, so form is comparable),
compares start rate, appearance rate and points with normal weeks, overall and
for premiums (price >= 10.0), City players, and Haaland himself.
"""
import json
import sys
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = "/home/wescheng/projects/fpl/fpl"


def gw_gaps():
    rows = []
    for season in ("2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"):
        fx = pd.read_csv(f"{ROOT}/data/fpl_history/{season}/fixtures.csv", low_memory=False)
        fx = fx.dropna(subset=["event", "kickoff_time"])
        fx["kickoff"] = pd.to_datetime(fx["kickoff_time"], utc=True)
        span = fx.groupby("event")["kickoff"].agg(["min", "max"]).sort_index()
        previous_end = span["max"].shift(1)
        for event, rec in span.iterrows():
            gap = (rec["min"] - previous_end.loc[event]).days if pd.notna(previous_end.loc[event]) else None
            rows.append({"season": season, "week": int(event), "gap_days": gap})
    gaps = pd.DataFrame(rows)
    gaps["post_break"] = gaps["gap_days"].between(12, 30)
    return gaps


def main() -> None:
    gaps = gw_gaps()
    cols = ["season", "week", "player_id", "player_name", "team_id", "position", "price_pre_deadline",
            "minutes_avg_3", "label_minutes_1gw", "label_points_1gw", "fixture_count"]
    t = pd.read_csv(f"{ROOT}/data/fpl_training_rows_v3_contract_f6.csv", low_memory=False, usecols=cols)
    t = t.loc[t["fixture_count"] == 1].merge(gaps, on=["season", "week"], how="left")
    t = t.sort_values(["season", "player_id", "week"])
    last3 = t.groupby(["season", "player_id"])["label_minutes_1gw"].transform(
        lambda s: s.shift(1).rolling(3, min_periods=3).min())
    regular = t.loc[last3 >= 60].copy()
    regular["started"] = regular["label_minutes_1gw"] >= 60
    regular["appeared"] = regular["label_minutes_1gw"] > 0
    out = {"post_break_weeks": gaps.loc[gaps["post_break"], ["season", "week", "gap_days"]].to_dict("records")}

    def summarise(frame, label):
        res = {}
        for flag, name in ((True, "post_break"), (False, "normal")):
            f = frame.loc[frame["post_break"] == flag]
            res[name] = {"n": int(len(f)), "start_rate": round(float(f["started"].mean()), 3),
                         "appear_rate": round(float(f["appeared"].mean()), 3),
                         "points": round(float(f["label_points_1gw"].mean()), 3)}
        res["start_rate_diff"] = round(res["post_break"]["start_rate"] - res["normal"]["start_rate"], 3)
        res["points_diff"] = round(res["post_break"]["points"] - res["normal"]["points"], 3)
        out[label] = res
        print(f"{label:34s} post-break n={res['post_break']['n']:5d} start {res['post_break']['start_rate']:.3f} "
              f"pts {res['post_break']['points']:.2f} | normal n={res['normal']['n']:6d} start {res['normal']['start_rate']:.3f} "
              f"pts {res['normal']['points']:.2f} | diff start {res['start_rate_diff']:+.3f} pts {res['points_diff']:+.2f}")

    summarise(regular, "regular starters, all")
    summarise(regular.loc[regular["season"] >= "2022-23"], "regular starters, 2022-26")
    summarise(regular.loc[regular["price_pre_deadline"] >= 10.0], "regular starters, price >= 10")
    summarise(regular.loc[regular["price_pre_deadline"].between(7.5, 9.9)], "regular starters, price 7.5-9.9")
    # Man City is team 13 in every season from 2019-20 to 2025-26 (ids follow the
    # alphabetical order of that season's clubs); 2026-27 renumbered (13 = Leeds).
    city = regular.loc[(regular["team_id"] == 13) & regular["season"].between("2022-23", "2025-26")]
    summarise(city, "regular Man City starters, 2022-26")

    h = t.loc[t["player_name"].astype(str).str.contains("Haaland")].copy()
    h = h.loc[h["season"] >= "2022-23"]
    post = h.loc[h["post_break"] == True]  # noqa: E712
    normal = h.loc[h["post_break"] == False]  # noqa: E712
    out["haaland_post_break_games"] = post[["season", "week", "gap_days", "label_minutes_1gw", "label_points_1gw"]].to_dict("records")
    out["haaland_summary"] = {
        "post_break": {"games": int(len(post)), "mean_minutes": round(float(post["label_minutes_1gw"].mean()), 1),
                       "mean_points": round(float(post["label_points_1gw"].mean()), 2),
                       "started": int((post["label_minutes_1gw"] >= 60).sum())},
        "normal": {"games": int(len(normal)), "mean_minutes": round(float(normal["label_minutes_1gw"].mean()), 1),
                   "mean_points": round(float(normal["label_points_1gw"].mean()), 2),
                   "started": int((normal["label_minutes_1gw"] >= 60).sum())},
    }
    print("\nHaaland, first GW after each international break (2022-23 onwards):")
    for r in out["haaland_post_break_games"]:
        print(f"  {r['season']} GW{r['week']:>2} (gap {r['gap_days']}d): {r['label_minutes_1gw']:.0f} min, {r['label_points_1gw']:.0f} pts")
    print("  summary:", out["haaland_summary"])
    json.dump(out, open(f"{ROOT}/reports/gw6_packet_2026_10/post_break_study.json", "w"), indent=1, default=str)


if __name__ == "__main__":
    main()

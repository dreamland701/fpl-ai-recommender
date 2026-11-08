import pandas as pd
import numpy as np

old = pd.read_csv("data/fpl_training_rows_blend_f6.csv", low_memory=False)
new = pd.read_csv("data/fpl_training_rows_v3_contract_f6.csv", low_memory=False)

# Weeks where ownership sum exceeds 1500 noticeably
pw = new.drop_duplicates(["season", "week", "player_id"])
tot = pw.groupby(["season", "week"])["selected_by_percent_pre_deadline"].sum()
print("weeks with ownership sum > 1510:")
print(tot[tot > 1510].round(0).to_string())
print()

# Movers: team_id changes within season
def movers(frame, season):
    sub = frame.loc[frame["season"] == season, ["player_id", "player_name", "week", "team_id"]]
    n_teams = sub.groupby("player_id")["team_id"].nunique()
    ids = n_teams[n_teams > 1].index
    return sub, ids

for season in ["2023-24", "2024-25", "2025-26"]:
    sub_new, ids_new = movers(new, season)
    sub_old, ids_old = movers(old, season)
    print(season, "players with >1 team_id within season: old", len(ids_old), "new", len(ids_new))
    for pid in list(ids_new)[:6]:
        rows = sub_new.loc[sub_new["player_id"] == pid].sort_values("week")
        changes = rows.loc[rows["team_id"].ne(rows["team_id"].shift())]
        print("   ", rows["player_name"].iloc[0], [(int(w), int(t)) for w, t in zip(changes["week"], changes["team_id"])])
print()

teams = pd.read_csv("data/fpl_history/2025-26/teams.csv")
print(teams[["id", "name"]].to_string(index=False))
for nm in ["Eze", "Madueke", "Gyökeres", "Mbeumo", "Cunha", "Kudus", "Wirtz"]:
    for label, frame in (("old", old), ("new", new)):
        sub = frame.loc[(frame["season"] == "2025-26") & frame["player_name"].astype(str).str.contains(nm), ["player_name", "week", "team_id"]]
        if sub.empty:
            continue
        sub = sub.sort_values("week")
        print(label, nm, "first rows:", [(int(w), int(t)) for w, t in zip(sub["week"].head(3), sub["team_id"].head(3))])
print()

# F6 / F12 sanity
f_cols = [c for c in new.columns if c.startswith("opp_") or "interaction" in c or "league" in c or "attack" in c]
print("F6/F12-ish columns:", f_cols)
for c in f_cols:
    a = pd.to_numeric(old[c], errors="coerce")
    b = pd.to_numeric(new[c], errors="coerce")
    print(f"{c:45s} old mean {a.mean():+.4f} sd {a.std():.4f} | new mean {b.mean():+.4f} sd {b.std():.4f} | corr {a.corr(b):.4f}")
print()
for c in ["price_pre_deadline", "price_change_1", "selected_change_1", "status_flag_pre_deadline"]:
    if c in new.columns:
        a = pd.to_numeric(old[c], errors="coerce"); b = pd.to_numeric(new[c], errors="coerce")
        print(f"{c:30s} old mean {a.mean():+.4f} sd {a.std():.4f} | new mean {b.mean():+.4f} sd {b.std():.4f}")
print()
# label maturity: labels are stored complete; masking happens at fit time. Check label NaN share by season tail
for c in ["label_points_3gw", "label_points_5gw"]:
    print(c, "NaN share by season:", new.groupby("season")[c].apply(lambda x: float(x.isna().mean())).round(3).to_dict())

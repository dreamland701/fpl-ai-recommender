"""Compare rebuilt contract tables against the pre-fix tables on real data."""
import sys
import pandas as pd
import numpy as np

OLD = "data/fpl_training_rows_blend_f6.csv"
NEW = "data/fpl_training_rows_v3_contract_f6.csv"

cols = None
old = pd.read_csv(OLD, low_memory=False)
new = pd.read_csv(NEW, low_memory=False)
print("rows old/new:", len(old), len(new))
print("cols old/new:", old.shape[1], new.shape[1])
print("cols only in old:", sorted(set(old.columns) - set(new.columns)))
print("cols only in new:", sorted(set(new.columns) - set(old.columns)))
print()
print("rows by season (old, new):")
print(pd.concat([old.groupby("season").size().rename("old"), new.groupby("season").size().rename("new")], axis=1))
print()

# 1) Ownership units
for name, frame in (("old", old), ("new", new)):
    s = pd.to_numeric(frame["selected_by_percent_pre_deadline"], errors="coerce")
    print(f"{name} selected_by_percent_pre_deadline: max={s.max():.1f} p99={s.quantile(.99):.2f} "
          f"median={s.median():.3f} share>100={float((s > 100).mean()):.3f}")
print()
print("new ownership by season (max, p99, median):")
s = pd.to_numeric(new["selected_by_percent_pre_deadline"], errors="coerce")
print(new.assign(s=s).groupby("season")["s"].agg(["max", lambda x: x.quantile(.99), "median"]))
print()
# famous premiums
for nm in ["Haaland", "Salah", "Palmer"]:
    mask = new["player_name"].astype(str).str.contains(nm, case=False)
    sub = new.loc[mask, ["season", "week", "player_name", "selected_by_percent_pre_deadline", "price_pre_deadline"]]
    sub = sub.sort_values(["season", "week"])
    print(nm, "\n", sub.groupby("season").agg(own_mean=("selected_by_percent_pre_deadline", "mean"),
                                           own_max=("selected_by_percent_pre_deadline", "max")).round(1))
print()
# 15-player identity per week in new table (only meaningful if 1 row per player-week)
pw = new.drop_duplicates(["season", "week", "player_id"])
tot = pw.groupby(["season", "week"])["selected_by_percent_pre_deadline"].sum()
print("sum of ownership% per week (should be <= ~1500, ~1500 on weeks where previous snapshot exists):")
print(tot.groupby(level=0).agg(["min", "median", "max"]).round(0))
print()

# 2) Status provenance
for name, frame in (("old", old), ("new", new)):
    flag_col = [c for c in frame.columns if c.startswith("status_flag") or c == "status_flag_pre_deadline" or c == "flagged_pre_deadline"]
    print(name, "status-ish columns:", [c for c in frame.columns if "status" in c.lower()][:10])
print()
st = new["status_pre_deadline"].fillna("").astype(str)
print("new status value counts by season:")
print(pd.crosstab(new["season"], st.where(st.isin(["a", "", "d", "i", "s", "u", "n"]), "other")))
print()
st_old = old["status_pre_deadline"].fillna("").astype(str)
print("old status value counts by season:")
print(pd.crosstab(old["season"], st_old.where(st_old.isin(["a", "", "d", "i", "s", "u", "n"]), "other")))

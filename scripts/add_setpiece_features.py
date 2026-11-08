#!/usr/bin/env python
"""Programme item 4 (2026-10-17): weekly set-piece duty features from the pre-deadline snapshots
(data/fpl_history/<season>/weekly_setpiece.csv, written by backfill_history_status_from_vaastav.py --setpiece).

Joins by (season, week, player_id) onto a copy of the production table, forward-filling within a season for weeks
without a snapshot (duties persist), and writes:
  pen_taker        1 if first-choice penalty taker
  pen_order_inv    1/penalty order (1, 0.5, 0.33 ...), 0 if not listed
  corner_taker     1 if first on corners / indirect free kicks
  fk_taker         1 if first on direct free kicks
  setpiece_score   pen_taker + 0.5 * corner_taker + 0.5 * fk_taker
usage: add_setpiece_features.py --table data/..._f6_status.csv --out data/..._f6_setpiece.csv
"""
import argparse
from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parents[1]
FEATURES = ["pen_taker", "pen_order_inv", "corner_taker", "fk_taker", "setpiece_score"]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
    table = pd.read_csv(a.table, low_memory=False)
    frames = []
    for d in sorted((ROOT / "data/fpl_history").glob("*/weekly_setpiece.csv")):
        w = pd.read_csv(d, usecols=lambda c: c in ("player_id", "week", "pen_order", "corner_order", "fk_order"))
        w["season"] = d.parent.name; frames.append(w)
    sp = pd.concat(frames, ignore_index=True)
    for c in ("pen_order", "corner_order", "fk_order"):
        sp[c] = pd.to_numeric(sp[c], errors="coerce")
    sp = sp.drop_duplicates(["season", "week", "player_id"])
    merged = table[["season", "week", "player_id"]].merge(sp, on=["season", "week", "player_id"], how="left")
    merged = merged.sort_values(["season", "player_id", "week"])
    # forward-fill duties within a season for weeks without a snapshot; a snapshot with no duty is an explicit NaN
    # in the source, so mark snapshot presence first and only fill the missing-snapshot weeks
    have = merged.set_index(["season", "week"]).index.isin(sp.set_index(["season", "week"]).index)
    for c in ("pen_order", "corner_order", "fk_order"):
        merged.loc[~have, c] = np.nan
        merged[c] = merged.groupby(["season", "player_id"])[c].transform(lambda x: x.ffill())
    merged = merged.sort_index()
    table["pen_taker"] = (merged["pen_order"] == 1).astype(float).to_numpy()
    table["pen_order_inv"] = (1.0 / merged["pen_order"]).fillna(0.0).to_numpy()
    table["corner_taker"] = (merged["corner_order"] == 1).astype(float).to_numpy()
    table["fk_taker"] = (merged["fk_order"] == 1).astype(float).to_numpy()
    table["setpiece_score"] = table.pen_taker + 0.5 * table.corner_taker + 0.5 * table.fk_taker
    cov = table.groupby("season")[["pen_taker", "corner_taker", "fk_taker"]].mean().round(3)
    print(cov.to_string())
    table.to_csv(a.out, index=False); print(f"wrote {a.out}: {len(table)} rows, {len(table.columns)} columns")

if __name__ == "__main__":
    main()

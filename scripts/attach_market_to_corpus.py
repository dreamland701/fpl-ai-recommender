#!/usr/bin/env python3
"""Attach metadata.market = {price, selected_by_percent} per player-week.

E13a: the adapter's shrink policy is band-unconditional partly because
prompts never expose who is a premium or what the crowd holds (price only
leaks via quoted article text; ownership never appears). Joined from the
training table's own-week values, which for FPL are deadline-time facts
(price and ownership snapshots are known before kickoff), so this is
chrono-legal like the DefCon attach.
"""
from __future__ import annotations

import argparse
import csv
import json


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--training-data", default="data/fpl_training_rows.csv")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    market = {}
    for row in csv.DictReader(open(args.training_data)):
        try:
            key = (row["season"], int(float(row["player_id"])), int(float(row["week"])))
            market[key] = {
                "price": round(float(row["price"]), 1),
                "selected_by_percent": round(float(row["selected_by_percent"]), 1),
            }
        except (ValueError, KeyError):
            continue

    attached = missing = 0
    with open(args.output, "w") as out:
        for line in open(args.corpus):
            row = json.loads(line)
            md = row["metadata"]
            key = (md["season"], int(md["player_id"]), int(md["week"]))
            info = market.get(key)
            if info is not None:
                md["market"] = info
                attached += 1
            else:
                md["market"] = None
                missing += 1
            out.write(json.dumps(row) + "\n")
    print(f"market attached: {attached} | missing: {missing} -> {args.output}")


if __name__ == "__main__":
    main()

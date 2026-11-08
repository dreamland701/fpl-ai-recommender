#!/usr/bin/env python3
"""Replay confirmed transfers that the public FPL API hides until the deadline onto a packet's entry_state.json
(GW9: the João Pedro -> Isak move stayed invisible until the deadline, [[fpl-entry-id]]).

usage: apply_hand_edit.py --entry-state <packet>/entry_state.json --bootstrap <packet>/snapshot/bootstrap_static.json \
         --moves <file: OUT_NAME:IN_NAME[:IN_PRICE] per line; a name may be an element id> [--note TEXT]
A move whose IN player is already in the squad is skipped (the API has caught up). Bank += OUT selling price - IN price
(default: the snapshot's current price); free transfers -= 1 per move, floor 0 (hits are the optimizer's business).
The original state is kept as entry_state_api.json next to it; the state records the replayed moves under "hand_edit".
"""
import argparse, json, shutil
from pathlib import Path

ap = argparse.ArgumentParser(); ap.add_argument("--entry-state", required=True); ap.add_argument("--bootstrap", required=True)
ap.add_argument("--moves", required=True); ap.add_argument("--note", default="")
a = ap.parse_args()
moves_path = Path(a.moves)
if not moves_path.exists() or not moves_path.read_text().strip():
    print("no hand edit (no moves file)"); raise SystemExit(0)
state_path = Path(a.entry_state); state = json.loads(state_path.read_text())
elements = json.load(open(a.bootstrap))["elements"]
by_id = {e["id"]: e for e in elements}


def resolve(label):
    label = label.strip()
    if label.isdigit() and int(label) in by_id:
        return by_id[int(label)]
    hits = [e for e in elements if e["web_name"].lower() == label.lower()]
    if len(hits) != 1:
        raise SystemExit(f"{label!r}: {len(hits)} matches {[(e['id'], e['web_name'], e['team']) for e in hits]} - use the element id")
    return hits[0]


applied = []
for line in moves_path.read_text().splitlines():
    line = line.strip()
    if not line or line.startswith("#"):
        continue
    parts = line.split(":")
    out_e, in_e = resolve(parts[0]), resolve(parts[1])
    price = float(parts[2]) if len(parts) > 2 and parts[2].strip() else in_e["now_cost"] / 10.0
    names = {s["player_id"] for s in state["squad"]}
    if in_e["id"] in names:
        print(f"skip {out_e['web_name']} -> {in_e['web_name']}: already in the API squad"); continue
    out_row = next((s for s in state["squad"] if s["player_id"] == out_e["id"]), None)
    if out_row is None:
        raise SystemExit(f"{out_e['web_name']} is not in the squad")
    new_row = dict(out_row, player_id=in_e["id"], name=in_e["web_name"], purchase_price=price, current_price=in_e["now_cost"] / 10.0,
                   selling_price=price, app_selling_price=None)
    state["squad"] = [new_row if s["player_id"] == out_e["id"] else s for s in state["squad"]]
    state["bank"] = round(state["bank"] + out_row["selling_price"] - price, 1)
    state["free_transfers"] = max(0, int(state["free_transfers"]) - 1)
    applied.append(f"{out_e['web_name']} (sell {out_row['selling_price']}) -> {in_e['web_name']} ({price})")
if applied:
    api_copy = state_path.with_name(state_path.stem + "_api.json")
    if not api_copy.exists():
        shutil.copy(state_path, api_copy)
    state["hand_edit"] = {"moves": applied, "note": a.note}
    state_path.write_text(json.dumps(state, indent=1, ensure_ascii=False))
    print("hand edit:", "; ".join(applied), f"| bank {state['bank']} FT {state['free_transfers']}")
else:
    print("hand edit: nothing to apply")

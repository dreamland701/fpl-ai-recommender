"""Reconstruct the entered squad, purchase prices and selling prices from the FPL API.

Reads entry/ (picks, transfers, history) and snapshot/ (current prices), and the
launch prices from the 2026-27 merged_gw round 1 rows. Writes entry/state.json and
checks the selling prices against the values Wes pasted from the app on 2026-10-04.
"""
import json
import os
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.rules import selling_price  # noqa: E402

PACKET = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
ENTRY = PACKET / "entry"
APP_SELL = {  # pasted from the app's Transfers screen, 2026-10-04
    "Donnarumma": 5.5, "Sels": 5.0, "Konsa": 4.5, "Mitchell": 4.5, "Bijol": 5.0, "Justin": 4.5,
    "N.Williams": 5.0, "Saka": 9.5, "Groß": 5.7, "Cherki": 7.7, "B.Fernandes": 11.9, "Cunha": 7.9,
    "Evanilson": 6.0, "João Pedro": 7.6, "Isak": 9.1,
}


def main() -> None:
    picks = json.loads((ENTRY / "picks_gw5.json").read_text())
    transfers = json.loads((ENTRY / "transfers.json").read_text())
    history = json.loads((ENTRY / "history.json").read_text())
    bootstrap = json.loads((PACKET / "snapshot" / "bootstrap_static.json").read_text())
    elements = {e["id"]: e for e in bootstrap["elements"]}
    merged = pd.read_csv("/home/wescheng/projects/fpl/fpl/data/fpl_history/2026-27/merged_gw.csv", low_memory=False)
    launch = merged.loc[merged["round"] == 1].drop_duplicates("element").set_index("element")["value"] / 10.0
    bought = {}
    for t in sorted(transfers, key=lambda t: t["time"]):
        bought[t["element_in"]] = t["element_in_cost"] / 10.0
    picks_event = int(picks.get("entry_history", {}).get("event", history["current"][-1]["event"]))
    # Transfers already made for the coming deadline are not in the last picks yet.
    pending = [t for t in sorted(transfers, key=lambda t: t["time"]) if int(t["event"]) > picks_event]
    owned = [p["element"] for p in sorted(picks["picks"], key=lambda p: p["position"])]
    bank_delta = 0.0
    for t in pending:
        out_pid, in_pid = t["element_out"], t["element_in"]
        out_purchase = bought.get(out_pid, float(launch.get(out_pid, elements[out_pid]["now_cost"] / 10.0)))
        bank_delta += selling_price(out_purchase, elements[out_pid]["now_cost"] / 10.0) - t["element_in_cost"] / 10.0
        owned = [in_pid if pid == out_pid else pid for pid in owned]
    position_of = {p["element"]: p["position"] for p in picks["picks"]}
    squad = []
    for pid in owned:
        pick = {"position": position_of.get(pid)}
        purchase = bought.get(pid, float(launch.get(pid, elements[pid]["now_cost"] / 10.0)))
        current = elements[pid]["now_cost"] / 10.0
        sell = selling_price(purchase, current)
        name = elements[pid]["web_name"]
        squad.append({"player_id": pid, "name": name, "purchase_price": purchase, "current_price": current,
                      "selling_price": sell, "app_selling_price": APP_SELL.get(name),
                      "gw5_position": pick["position"]})
    last = history["current"][-1]
    used = {c["name"] for c in history.get("chips", [])}
    state = {
        "entry_id": 6535607,
        "bank": round(last["bank"] / 10.0 + bank_delta, 1),
        # GW2-5 each used the one free transfer (no hits), so GW6 opens with 1.
        "free_transfers": max(0, 1 - len(pending)),
        "pending_transfers": [{"out": elements[t["element_out"]]["web_name"], "in": elements[t["element_in"]]["web_name"],
                               "event": t["event"]} for t in pending],
        "chips_used": sorted(used),
        "squad": squad,
    }
    mismatches = [s for s in squad if s["app_selling_price"] is not None and abs(s["selling_price"] - s["app_selling_price"]) > 1e-9]
    state["selling_price_check"] = "all match the app" if not mismatches else [
        f"{s['name']}: computed {s['selling_price']} vs app {s['app_selling_price']}" for s in mismatches]
    out = PACKET / "entry_state.json"
    out.write_text(json.dumps(state, indent=1, ensure_ascii=False))
    for s in squad:
        print(f"{s['name']:12s} bought {s['purchase_price']:5.1f} now {s['current_price']:5.1f} sells {s['selling_price']:5.1f}"
              f" (app {s['app_selling_price']})")
    print("bank", state["bank"], "| chips used", state["chips_used"] or "none", "|", state["selling_price_check"])


if __name__ == "__main__":
    main()

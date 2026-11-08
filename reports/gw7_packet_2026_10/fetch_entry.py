"""Fetch Wes's entered team from the public FPL API into <PACKET_DIR>/entry/."""
import json
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENTRY_ID = 6535607
PACKET = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
BASE = "https://fantasy.premierleague.com/api"


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(request, timeout=30).read())


def main() -> None:
    out = PACKET / "entry"
    out.mkdir(parents=True, exist_ok=True)
    entry = get(f"{BASE}/entry/{ENTRY_ID}/")
    last_event = int(entry["current_event"])
    payload = {
        "entry": entry,
        "history": get(f"{BASE}/entry/{ENTRY_ID}/history/"),
        "picks_gw5": get(f"{BASE}/entry/{ENTRY_ID}/event/{last_event}/picks/"),
        "transfers": get(f"{BASE}/entry/{ENTRY_ID}/transfers/"),
    }
    for name, data in payload.items():
        (out / f"{name}.json").write_text(json.dumps(data))
    retrieved = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (out / "manifest.json").write_text(json.dumps({"entry_id": ENTRY_ID, "last_event": last_event,
                                                    "retrieved_at_utc": retrieved}))
    print(f"entry {ENTRY_ID} fetched at {retrieved} (last event {last_event})")


if __name__ == "__main__":
    main()

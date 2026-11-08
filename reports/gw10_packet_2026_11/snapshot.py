"""Freeze one official FPL snapshot for the GW10 deadline packet.

Both the pre-fix and the fixed pipelines read these files through a frozen
client, so any difference in their forecasts comes from the pipelines, not
from prices or news moving between two API calls.
"""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.api import OfficialFPLClient  # noqa: E402

OUT = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent)) / "snapshot"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    client = OfficialFPLClient()
    bootstrap = client.bootstrap_static()
    fixtures = client.fixtures()
    retrieved = datetime.now(timezone.utc).isoformat(timespec="seconds")
    event = next(e for e in bootstrap["events"] if e["id"] == 10)
    (OUT / "bootstrap_static.json").write_text(json.dumps(bootstrap))
    (OUT / "fixtures.json").write_text(json.dumps(fixtures))
    (OUT / "manifest.json").write_text(json.dumps({
        "retrieved_at_utc": retrieved,
        "event": 10,
        "deadline_time": event["deadline_time"],
        "players": len(bootstrap["elements"]),
        "fixtures_gw10": sum(1 for f in fixtures if f.get("event") == 10),
    }, indent=1))
    print(f"snapshot frozen at {retrieved}; GW10 deadline {event['deadline_time']}")


if __name__ == "__main__":
    main()

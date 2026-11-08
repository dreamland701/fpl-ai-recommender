"""Legal GW10 lineups (fixed pipeline) for hold, the named candidate routes and the exact optimizer's best 1/2-move routes."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from decide import BANK, SQUAD_SELL, load, to_forecast  # noqa: E402
from fpl_ai.decision import _optimize_lineup  # noqa: E402
from fpl_ai.types import SquadPlayer  # noqa: E402

PACKET = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
NAMED = {  # GW10 candidates by name: (out names, in names)
    "hold": ([], []),
}


def main() -> None:
    forecasts = load("forecasts_new_pipeline.jsonl")
    by_name = {r["name"]: r for r in forecasts.values()}
    lookup = {pid: to_forecast(r) for pid, r in forecasts.items()}
    routes = dict(NAMED)
    milp_path = PACKET / "milp_transfers.json"
    if milp_path.exists():
        milp = json.loads(milp_path.read_text())
        for key in ("GW10-14_max1", "GW10-14_max2", "GW10 only_max1"):
            r = milp.get(key)
            if r and r["in"]:
                label = f"{' + '.join(r['out'])} -> {' + '.join(r['in'])} ({key.replace('_max', ', max ')} moves, hit {r['hit']})"
                routes.setdefault(label, (r["out"], r["in"]))
    out = {}
    for label, (outs, ins) in routes.items():
        out_ids = [by_name[n]["player_id"] for n in outs if n in by_name]
        if len(out_ids) != len(outs) or any(pid not in SQUAD_SELL for pid in out_ids) or any(n not in by_name for n in ins):
            print(f"skip {label}: names not found or not in squad")
            continue
        incoming = [by_name[n] for n in ins]
        squad = [SquadPlayer(pid, forecasts[pid]["name"], forecasts[pid]["team_id"], forecasts[pid]["pos"], sell)
                 for pid, sell in SQUAD_SELL.items() if pid not in out_ids]
        squad += [SquadPlayer(r["player_id"], r["name"], r["team_id"], r["pos"], r["price"]) for r in incoming]
        bank = round(BANK + sum(SQUAD_SELL[p] for p in out_ids) - sum(r["price"] for r in incoming), 1)
        starters, bench, captain, vice, _ = _optimize_lineup(squad, lookup)
        name = lambda i: forecasts[i]["name"]  # noqa: E731
        xi_points = sum(forecasts[i]["p1"] for i in starters) + forecasts[captain]["p1"]
        out[label] = {"bank_after": bank, "xi": [name(i) for i in starters], "bench_order": [name(i) for i in bench],
                      "captain": name(captain), "vice": name(vice), "gw10_xi_points_incl_captain": round(xi_points, 1)}
        print(f"\n{label}  (bank after {bank:.1f})")
        print("  XI:", ", ".join(out[label]["xi"]))
        print("  bench:", " > ".join(out[label]["bench_order"]), f"| C {name(captain)} VC {name(vice)}",
              f"| GW10 XI forecast {xi_points:.1f}")
    (PACKET / "route_lineups.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

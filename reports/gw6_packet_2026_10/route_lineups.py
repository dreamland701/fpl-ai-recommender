"""Legal GW6 lineups (fixed pipeline) for hold and the leading transfer routes."""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from decide import BANK, SQUAD_SELL, load, to_forecast  # noqa: E402
from fpl_ai.decision import _optimize_lineup  # noqa: E402
from fpl_ai.types import SquadPlayer  # noqa: E402

ROUTES = {
    "hold": ([], []),
    "Bijol -> De Cuyper (1 FT, no hit)": ([327], ["De Cuyper"]),
    "Bruno + Isak -> Haaland + Le Fée (-4)": ([426, 379], ["Haaland", "E.Le Fée"]),
    "Bruno + Isak -> Haaland + Xhaka (-4)": ([426, 379], ["Haaland", "Xhaka"]),
    "Bijol + Bruno + Isak -> De Cuyper + Le Fée + Haaland (-8)": ([327, 426, 379], ["De Cuyper", "E.Le Fée", "Haaland"]),
}


def main() -> None:
    forecasts = load("forecasts_new_pipeline.jsonl")
    by_name = {r["name"]: r for r in forecasts.values()}
    lookup = {pid: to_forecast(r) for pid, r in forecasts.items()}
    out = {}
    for label, (outs, ins) in ROUTES.items():
        if any(pid not in SQUAD_SELL for pid in outs) or any(name not in by_name for name in ins):
            continue
        incoming = [by_name[name] for name in ins]
        squad = [SquadPlayer(pid, forecasts[pid]["name"], forecasts[pid]["team_id"], forecasts[pid]["pos"], sell)
                 for pid, sell in SQUAD_SELL.items() if pid not in outs]
        squad += [SquadPlayer(r["player_id"], r["name"], r["team_id"], r["pos"], r["price"]) for r in incoming]
        bank = round(BANK + sum(SQUAD_SELL[p] for p in outs) - sum(r["price"] for r in incoming), 1)
        starters, bench, captain, vice, _ = _optimize_lineup(squad, lookup)
        name = lambda i: forecasts[i]["name"]  # noqa: E731
        xi_points = sum(forecasts[i]["p1"] for i in starters) + forecasts[captain]["p1"]
        out[label] = {"bank_after": bank, "xi": [name(i) for i in starters], "bench_order": [name(i) for i in bench],
                      "captain": name(captain), "vice": name(vice), "gw6_xi_points_incl_captain": round(xi_points, 1)}
        print(f"\n{label}  (bank after {bank:.1f})")
        print("  XI:", ", ".join(out[label]["xi"]))
        print("  bench:", " > ".join(out[label]["bench_order"]), f"| C {name(captain)} VC {name(vice)}",
              f"| GW6 XI forecast {xi_points:.1f}")
    (Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent)) / "route_lineups.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

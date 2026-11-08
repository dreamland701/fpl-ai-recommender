"""Pre-register the GW7 wildcard proposal (2026-10-07) so it can be scored after GW7.

Freezes, from the 2026-10-06 interim forecasts (the ones the proposal was made
on), three GW7 squads with their GW7 XI, bench order (GK first), captain and vice:

  wildcard_playable  primary: exact optimizer, every new signing P(app) >= 0.6
  wildcard_fodder    secondary: pure optimizer output (non-playing bench fodder)
  plan               reference: GW6 Bijol -> De Cuyper, GW7 Bruno + Isak -> Haaland + Xhaka

GW7 lineups are picked on (5GW - 1GW) / 4, the average of the GW7-10
forecasts: no separate GW7 forecast existed when the proposal was made. The
output records the source file's md5 and the creation time.
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKET = Path("/home/wescheng/projects/fpl/fpl/reports/gw6_packet_2026_10")
OUT = Path(__file__).resolve().parent
os.environ["PACKET_DIR"] = str(PACKET / "interim_1006")
sys.path.insert(0, str(PACKET))
from decide import BANK, SQUAD_SELL, load, route_ev  # noqa: E402
from squad_milp import optimize  # noqa: E402

XI_BOUNDS = {"GK": (1, 1), "DEF": (3, 5), "MID": (2, 5), "FWD": (1, 3)}


def pick_lineup(F, squad, value):
    by = {pos: sorted((i for i in squad if F[i]["pos"] == pos), key=lambda i: -value[i]) for pos in XI_BOUNDS}
    best = None
    for d in range(3, 6):
        for f in range(1, 4):
            m = 10 - d - f
            if not 2 <= m <= 5:
                continue
            xi = by["GK"][:1] + by["DEF"][:d] + by["MID"][:m] + by["FWD"][:f]
            score = sum(value[i] for i in xi)
            if best is None or score > best[0]:
                best = (score, xi)
    xi = best[1]
    ranked = sorted(xi, key=lambda i: -value[i])
    bench_gk = [i for i in by["GK"] if i not in xi]
    bench_out = sorted((i for i in squad if i not in xi and F[i]["pos"] != "GK"), key=lambda i: -value[i])
    return {"xi": xi, "bench": bench_gk + bench_out, "captain": ranked[0], "vice": ranked[1]}


def describe(F, squad, lineup, projected):
    name = lambda i: F[i]["name"]  # noqa: E731
    return {
        "squad": [{"player_id": i, "name": name(i), "pos": F[i]["pos"], "price": F[i]["price"]} for i in squad],
        "gw7_xi": [name(i) for i in lineup["xi"]], "gw7_xi_ids": lineup["xi"],
        "gw7_bench_order": [name(i) for i in lineup["bench"]], "gw7_bench_ids": lineup["bench"],
        "gw7_captain": name(lineup["captain"]), "gw7_captain_id": lineup["captain"],
        "gw7_vice": name(lineup["vice"]), "gw7_vice_id": lineup["vice"],
        "projected_gw7_10_gain_vs_keeping": round(projected, 1),
    }


def main() -> None:
    source = PACKET / "interim_1006" / "forecasts_new_pipeline.jsonl"
    F = load("forecasts_new_pipeline.jsonl")
    by = {r["name"]: pid for pid, r in F.items()}
    rest = {pid: r["p5"] - r["p1"] for pid, r in F.items()}
    gw7 = {pid: v / 4.0 for pid, v in rest.items()}
    sell7 = {pid: s for pid, s in SQUAD_SELL.items() if pid != by["Bijol"]}
    sell7[by["De Cuyper"]] = F[by["De Cuyper"]]["price"]
    bank7 = round(BANK + SQUAD_SELL[by["Bijol"]] - F[by["De Cuyper"]]["price"], 1)
    hold7 = route_ev(F, list(sell7), lambda i: rest[i])

    playing = {pid: r for pid, r in F.items() if pid in sell7 or r["papp"] >= 0.6}
    wc_play = optimize(playing, rest, sell7, bank7, wildcard=True)
    wc_fod = optimize(F, rest, sell7, bank7, wildcard=True)
    plan = [i for i in sell7 if i not in (by["B.Fernandes"], by["Isak"])] + [by["Haaland"], by["Xhaka"]]
    proposal = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "entry_id": 6535607,
        "source_forecasts": str(source),
        "source_md5": hashlib.md5(source.read_bytes()).hexdigest(),
        "assumptions": [
            "GW6: Bijol -> De Cuyper in every scenario (Wes's plan).",
            "Wildcard squads use the post-GW6 selling prices and bank (£0.3m) and pay no hits.",
            "GW7 lineups are picked on the GW7-10 average forecast; no transfers after GW7.",
            "Scoring: official GW7 points, automatic substitutions in bench order, vice takes the armband if the captain does not play.",
        ],
        "wildcard_playable": describe(F, wc_play["squad"], pick_lineup(F, wc_play["squad"], gw7), wc_play["net"] - hold7),
        "wildcard_fodder": describe(F, wc_fod["squad"], pick_lineup(F, wc_fod["squad"], gw7), wc_fod["net"] - hold7),
        "plan": describe(F, plan, pick_lineup(F, plan, gw7), route_ev(F, plan, lambda i: rest[i]) - 4 - hold7),
    }
    proposal["plan"]["gw7_hit"] = 4
    path = OUT / "proposal_frozen_2026-10-07.json"
    if path.exists():
        raise SystemExit(f"{path} already exists; a pre-registration is not overwritten")
    path.write_text(json.dumps(proposal, indent=1, ensure_ascii=False))
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    (OUT / "proposal_frozen_2026-10-07.sha256").write_text(f"{digest}  {path.name}\n")
    for key in ("wildcard_playable", "wildcard_fodder", "plan"):
        p = proposal[key]
        print(f"{key}: projected {p['projected_gw7_10_gain_vs_keeping']:+.1f} | C {p['gw7_captain']} VC {p['gw7_vice']}")
        print("   XI:", ", ".join(p["gw7_xi"]), "| bench:", " > ".join(p["gw7_bench_order"]))
    print("frozen:", path, "sha256", digest[:16])


if __name__ == "__main__":
    main()

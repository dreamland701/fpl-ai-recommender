"""GW7 decision sheet from both pipelines' forecasts, for the entered squad.

Squad, selling prices, bank and free transfers come from entry_state.json (the
FPL API, checked against the app); the 2026-09-28 record is only a fallback.
Writes decision_sheet.json under PACKET_DIR and prints the sheet.
"""
import itertools
import json
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.backtest import build_initial_squad  # noqa: E402
from fpl_ai.decision import recommend_actions  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer, SquadState  # noqa: E402

HERE = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
FALLBACK_SELL = {  # 2026-09-28 record
    467: 5.0, 384: 5.5, 327: 5.0, 204: 4.5, 332: 4.5, 469: 5.0, 31: 4.5,
    426: 11.9, 428: 7.9, 12: 9.5, 124: 5.6, 399: 7.7, 165: 7.6, 379: 9.1, 79: 6.0,
}
HAALAND = 411
HIT = 4


def entry_state():
    path = HERE / "entry_state.json"
    if path.exists():
        state = json.loads(path.read_text())
        return {s["player_id"]: s["selling_price"] for s in state["squad"]}, state["bank"], state["free_transfers"], state
    return dict(FALLBACK_SELL), 0.3, 1, None


SQUAD_SELL, BANK, FREE_TRANSFERS, STATE = entry_state()


def load(name):
    return {r["player_id"]: r for r in map(json.loads, open(HERE / name))}


def to_forecast(r):
    return PlayerForecast(
        season="2026-27", week=7, player_id=r["player_id"], player_name=r["name"], team_id=r["team_id"],
        position=r["pos"], price=r["price"], predicted_minutes=r["mins"], predicted_points_1gw=r["p1"],
        predicted_points_3gw=r["p3"], predicted_points_5gw=r["p5"], appearance_probability=r["papp"],
        fixture_count=r.get("fixtures", 1), uncertainty=r["unc"],
    )


def route_ev(F, ids, key):
    """Best legal XI by `key` + captain doubled + 0.1 x outfield bench (haaland_routes.py)."""
    by = {"GK": [], "DEF": [], "MID": [], "FWD": []}
    for i in ids:
        by[F[i]["pos"]].append(i)
    for pos in by:
        by[pos].sort(key=lambda i: -key(i))
    best = None
    for d in range(3, 6):
        for f in range(1, 4):
            m = 10 - d - f
            if not 2 <= m <= 5 or len(by["DEF"]) < d or len(by["MID"]) < m or len(by["FWD"]) < f:
                continue
            xi = by["GK"][:1] + by["DEF"][:d] + by["MID"][:m] + by["FWD"][:f]
            bench = [i for i in ids if i not in xi and F[i]["pos"] != "GK"]
            score = sum(key(i) for i in xi) + max(key(i) for i in xi) + 0.1 * sum(key(i) for i in bench)
            best = score if best is None else max(best, score)
    return best


def routes(F, sell):
    squad = list(sell)
    p1 = lambda i: F[i]["p1"]  # noqa: E731
    p5 = lambda i: F[i]["p5"]  # noqa: E731
    rest = lambda i: F[i]["p5"] - F[i]["p1"]  # noqa: E731
    hold_now = route_ev(F, squad, p5)
    hold_roll = route_ev(F, squad, p1) + route_ev(F, squad, rest)
    pool = {}
    for pos in ("GK", "DEF", "MID", "FWD"):
        cands = [r for r in F.values() if r["pos"] == pos and r["status"] not in ("u", "i", "s", "n")
                 and r["player_id"] not in sell]
        pool[pos] = [r["player_id"] for r in sorted(cands, key=lambda r: -r["p5"])[:30]]
    out = []
    for k in (1, 2, 3):
        for outs in itertools.combinations(squad, k):
            budget = BANK + sum(sell[i] for i in outs)
            need = Counter(F[i]["pos"] for i in outs)
            choices = [list(itertools.combinations(pool[pos][:18 if k == 3 else 30], n)) for pos, n in need.items()]
            for combo in itertools.product(*choices):
                ins = [i for group in combo for i in group]
                cost = sum(F[i]["price"] for i in ins)
                if cost > budget + 1e-9:
                    continue
                new = [i for i in squad if i not in outs] + ins
                if max(Counter(F[i]["team_id"] for i in new).values()) > 3:
                    continue
                now = route_ev(F, new, p5) - HIT * max(0, k - FREE_TRANSFERS) - hold_now
                roll = route_ev(F, squad, p1) + route_ev(F, new, rest) - HIT * max(0, k - FREE_TRANSFERS - 1) - hold_roll
                out.append({"k": k, "out": list(outs), "in": ins, "gain_now": round(now, 2), "gain_roll": round(roll, 2),
                            "itb": round(budget - cost, 1), "haaland": HAALAND in ins})
    return hold_now, hold_roll, out


def chip_rebuilds(F, sell):
    """Wildcard (GW7-11 value) and Free Hit (GW7 only) rebuilds under the full selling budget."""
    budget = BANK + sum(sell.values())
    forecasts = [to_forecast(r) for r in F.values() if r["status"] not in ("u", "i", "s", "n")]
    p1 = lambda i: F[i]["p1"]  # noqa: E731
    p5 = lambda i: F[i]["p5"]  # noqa: E731
    result = {}
    for chip, horizon_key, key in (("wildcard", "5gw", p5), ("free_hit", "1gw", p1)):
        ranked = [f if horizon_key == "5gw" else
                  PlayerForecast(**{**f.__dict__, "predicted_points_5gw": f.predicted_points_1gw * 5,
                                    "predicted_points_3gw": f.predicted_points_1gw * 3})
                  for f in forecasts]
        squad, bank = build_initial_squad(ranked, budget=budget, beam_width=800)
        ids = [p.player_id for p in squad]
        gain = route_ev(F, ids, key) - route_ev(F, list(sell), key)
        result[chip] = {"gain": round(gain, 1), "horizon": "GW7-11" if chip == "wildcard" else "GW7 only",
                        "squad": [F[i]["name"] for i in ids], "bank_after": round(bank, 1)}
    return result


def sheet(F, label):
    squad = [SquadPlayer(pid, F[pid]["name"], F[pid]["team_id"], F[pid]["pos"], sell) for pid, sell in SQUAD_SELL.items()]
    state = SquadState(season="2026-27", week=7, squad_players=squad, bank=BANK, free_transfers=FREE_TRANSFERS,
                       chips_available={})
    bundle = recommend_actions(state, [to_forecast(r) for r in F.values()], top_n_transfers=5, max_transfers_considered=2)
    name = lambda i: F[i]["name"]  # noqa: E731
    hold_now, hold_roll, rts = routes(F, SQUAD_SELL)
    best = {}
    for haaland in (True, False):
        for k in (1, 2, 3):
            sub = [r for r in rts if r["k"] == k and r["haaland"] == haaland]
            best[f"{'with' if haaland else 'without'}_haaland_{k}"] = {
                "now": sorted(sub, key=lambda r: -r["gain_now"])[:3],
                "roll": sorted(sub, key=lambda r: -r["gain_roll"])[:2],
            }
    return {
        "pipeline": label,
        "starting_xi": [name(i) for i in bundle.starters],
        "bench_order": [name(i) for i in bundle.bench_order],
        "captain": name(bundle.captain_id),
        "vice_captain": name(bundle.vice_captain_id),
        "decision_layer_transfers": [
            {"out": [name(i) for i in t.players_out], "in": [name(i) for i in t.players_in],
             "gain": round(t.projected_gain, 2), "hit": t.hit_cost}
            for t in bundle.transfers
        ],
        "route_hold_ev_gw7_11": round(hold_now, 1),
        "routes": {key: {when: [{**r, "out": [name(i) for i in r["out"]], "in": [name(i) for i in r["in"]]}
                                for r in rows] for when, rows in value.items()} for key, value in best.items()},
        "chips": chip_rebuilds(F, SQUAD_SELL),
    }


def main() -> None:
    new = load("forecasts_new_pipeline.jsonl")
    old_path = HERE / "forecasts_old_pipeline.jsonl"
    result = {"squad_source": "entry_state.json (FPL API, matches the app)" if STATE else "2026-09-28 record",
              "bank": BANK, "free_transfers": FREE_TRANSFERS, "new": sheet(new, "fixed pipeline")}
    if old_path.exists():
        result["old"] = sheet(load(old_path.name), "pre-fix pipeline")
    (HERE / "decision_sheet.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
    for side in ("new", "old"):
        if side not in result:
            continue
        s = result[side]
        print(f"\n== {s['pipeline']} == hold EV {s['route_hold_ev_gw7_11']}")
        print("XI:", ", ".join(s["starting_xi"]), "| bench:", " > ".join(s["bench_order"]),
              "| C", s["captain"], "VC", s["vice_captain"])
        for key, value in s["routes"].items():
            top = value["now"][:1]
            if top:
                r = top[0]
                print(f"  {key:20s} {r['gain_now']:+6.1f}  OUT {'+'.join(r['out'])} IN {'+'.join(r['in'])} (itb {r['itb']})"
                      f" | roll {value['roll'][0]['gain_roll']:+.1f}")
        for chip, info in s["chips"].items():
            print(f"  {chip:20s} {info['gain']:+6.1f} ({info['horizon']}) bank after {info['bank_after']}: {', '.join(info['squad'])}")


if __name__ == "__main__":
    main()

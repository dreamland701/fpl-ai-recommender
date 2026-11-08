"""Two-week transfer plans for GW7/GW7, valued over GW7-11, with a Haaland GW7 fatigue discount.

Uses the route scorer from decide.py (best legal XI + captain doubled + 0.1 x
outfield bench): GW7 is scored on 1GW forecasts with the GW7 squad, GW7-10 on
(5GW - 1GW) with the squad after the GW7 moves. Free transfers: 1 now, +1 next
week (max 5). `haaland_gw7_factor` scales his GW7 forecast only: 1.0 is the
model, 0.75 / 0.6 price in the fatigue news (benched, limited minutes or held out).
Konsa's GW7 forecast already carries his 75% flag.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
os.environ.setdefault("PACKET_DIR", str(Path(__file__).resolve().parent / "interim_1006"))
from decide import BANK, SQUAD_SELL, load, route_ev  # noqa: E402

HIT = 4


def main() -> None:
    F = load("forecasts_new_pipeline.jsonl")
    by = {r["name"]: pid for pid, r in F.items()}
    HAAL, XHAKA, DC = by["Haaland"], by["Xhaka"], by["De Cuyper"]
    BRUNO, ISAK, BIJOL, KONSA = by["B.Fernandes"], by["Isak"], by["Bijol"], by["Konsa"]
    squad = list(SQUAD_SELL)

    def swap(ids, outs, ins):
        return [i for i in ids if i not in outs] + list(ins)

    def bank_after(outs, ins, bank):
        return round(bank + sum(SQUAD_SELL.get(i, F[i]["price"]) for i in outs) - sum(F[i]["price"] for i in ins), 1)

    haaland_double = ([BRUNO, ISAK], [HAAL, XHAKA])
    bijol_dc = ([BIJOL], [DC])
    plans = {
        "hold everything": ([], [], 0, 0),
        "GW7 Bijol->De Cuyper only": (bijol_dc, None, 0, 0),
        "GW7 Bruno+Isak->Haaland+Xhaka (-4)": (haaland_double, None, HIT, 0),
        "GW7 roll, GW7 Bruno+Isak->Haaland+Xhaka (2 FT)": (None, haaland_double, 0, 0),
        "GW7 Bijol->De Cuyper, GW7 Haaland double (-4)": (bijol_dc, haaland_double, 0, HIT),
        "GW7 Haaland double (-4), GW7 Bijol->De Cuyper": (haaland_double, bijol_dc, HIT, 0),
        "GW7 roll, GW7 Haaland double + Bijol->De Cuyper (-4)": (None, (haaland_double[0] + bijol_dc[0], haaland_double[1] + bijol_dc[1]), 0, HIT),
    }
    results = {}
    for factor in (1.0, 0.75, 0.6):
        p1 = lambda i: F[i]["p1"] * (factor if i == HAAL else 1.0)  # noqa: E731
        rest = lambda i: F[i]["p5"] - F[i]["p1"]  # noqa: E731
        base = route_ev(F, squad, p1) + route_ev(F, squad, rest)
        rows = {}
        for name, (gw7, gw7, hit6, hit7) in plans.items():
            s6 = swap(squad, *gw7) if gw7 else list(squad)
            s7 = swap(s6, *gw7) if gw7 else list(s6)
            bank6 = bank_after(*gw7, BANK) if gw7 else BANK
            bank7 = bank_after(*gw7, bank6) if gw7 else bank6
            if min(bank6, bank7) < -1e-9:
                rows[name] = None
                continue
            value = route_ev(F, s6, p1) + route_ev(F, s7, rest) - hit6 - hit7 - base
            rows[name] = {"gain": round(value, 1), "bank_after": bank7}
        results[f"haaland_gw7_factor_{factor}"] = rows
    print(f"{'plan':56s} {'model':>7s} {'x0.75':>7s} {'x0.60':>7s}  bank")
    for name in plans:
        vals = [results[f"haaland_gw7_factor_{f}"][name] for f in (1.0, 0.75, 0.6)]
        if any(v is None for v in vals):
            print(f"{name:56s}  illegal (budget)")
            continue
        print(f"{name:56s} {vals[0]['gain']:+7.1f} {vals[1]['gain']:+7.1f} {vals[2]['gain']:+7.1f}  {vals[0]['bank_after']}")
    budget = SQUAD_SELL[KONSA] + BANK
    defenders = sorted((r for r in F.values() if r["pos"] == "DEF" and r["price"] <= budget + 1e-9
                        and r["player_id"] not in SQUAD_SELL and r["status"] == "a"), key=lambda r: -r["p5"])[:5]
    print(f"\nKonsa (GW7 {F[KONSA]['p1']:.2f}, GW7-11 {F[KONSA]['p5']:.1f}) -> best available defenders at <= £{budget:.1f}m:")
    for r in defenders:
        print(f"  {r['name']:16s} £{r['price']:.1f} GW7 {r['p1']:.2f} GW7-11 {r['p5']:.1f} P(app) {r['papp']:.2f}")
    results["konsa_replacements"] = [{k: r[k] for k in ("name", "price", "p1", "p5", "papp")} for r in defenders]
    (Path(os.environ["PACKET_DIR"]) / "plans.json").write_text(json.dumps(results, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

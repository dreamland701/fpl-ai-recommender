"""Should a chip be played in GW7? Exact-optimizer comparison on the interim forecasts.

Assumes the GW6 move Bijol -> De Cuyper. GW7 decisions are valued over GW7-10
(5GW - 1GW forecasts; GW11+ is outside the forecast horizon, which understates
a wildcard's lasting value). All rows are measured against keeping the
post-GW6 squad unchanged. Also checks the optimizer against the route enumerator
on GW6 (it should match or beat +12.1).
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
os.environ.setdefault("PACKET_DIR", str(HERE / "interim_1006"))
from decide import BANK, SQUAD_SELL, load, route_ev  # noqa: E402
from squad_milp import optimize  # noqa: E402


def main() -> None:
    F = load("forecasts_new_pipeline.jsonl")
    by = {r["name"]: pid for pid, r in F.items()}
    name = lambda i: F[i]["name"]  # noqa: E731
    p5 = {pid: r["p5"] for pid, r in F.items()}
    rest = {pid: r["p5"] - r["p1"] for pid, r in F.items()}
    out = {}

    # --- sanity: GW6 with 1 FT should match or beat the route enumerator (+12.1)
    hold6 = route_ev(F, list(SQUAD_SELL), lambda i: p5[i])
    best6 = optimize(F, p5, SQUAD_SELL, BANK, free_transfers=1)
    out["gw6_best_transfers"] = {"gain": round(best6["net"] - hold6, 1), "out": [name(i) for i in best6["out"]],
                                 "in": [name(i) for i in best6["in"]], "hits": best6["hits"],
                                 "bank_after": best6["bank_after"]}
    wc6 = optimize(F, p5, SQUAD_SELL, BANK, wildcard=True)
    out["gw6_wildcard"] = {"gain": round(wc6["net"] - hold6, 1), "squad": [name(i) for i in wc6["squad"]],
                           "captain": name(wc6["captain"]), "bank_after": wc6["bank_after"]}

    # --- GW7 after Bijol -> De Cuyper
    sell7 = {pid: s for pid, s in SQUAD_SELL.items() if pid != by["Bijol"]}
    sell7[by["De Cuyper"]] = F[by["De Cuyper"]]["price"]
    bank7 = round(BANK + SQUAD_SELL[by["Bijol"]] - F[by["De Cuyper"]]["price"], 1)
    hold7 = route_ev(F, list(sell7), lambda i: rest[i])
    plan_squad = [i for i in sell7 if i not in (by["B.Fernandes"], by["Isak"])] + [by["Haaland"], by["Xhaka"]]
    out["gw7_plan_haaland_xhaka"] = {"gain": round(route_ev(F, plan_squad, lambda i: rest[i]) - 4 - hold7, 1)}
    for k in (1, 2, 3):
        res = optimize(F, rest, sell7, bank7, free_transfers=1, max_transfers=k)
        out[f"gw7_best_{k}_transfers"] = {"gain": round(res["net"] - hold7, 1), "out": [name(i) for i in res["out"]],
                                          "in": [name(i) for i in res["in"]], "hits": res["hits"],
                                          "captain": name(res["captain"]), "bank_after": res["bank_after"]}
    free_any = optimize(F, rest, sell7, bank7, free_transfers=1)
    out["gw7_best_any_transfers"] = {"gain": round(free_any["net"] - hold7, 1), "out": [name(i) for i in free_any["out"]],
                                     "in": [name(i) for i in free_any["in"]], "hits": free_any["hits"]}
    wc7 = optimize(F, rest, sell7, bank7, wildcard=True)
    out["gw7_wildcard"] = {"gain": round(wc7["net"] - hold7, 1), "squad": [name(i) for i in wc7["squad"]],
                           "xi": [name(i) for i in wc7["xi"]], "captain": name(wc7["captain"]),
                           "keeps": [name(i) for i in wc7["squad"] if i in sell7], "bank_after": wc7["bank_after"]}
    wc7_h = optimize(F, rest, sell7, bank7, wildcard=True, forced_in=[by["Haaland"]])
    out["gw7_wildcard_with_haaland"] = {"gain": round(wc7_h["net"] - hold7, 1),
                                        "squad": [name(i) for i in wc7_h["squad"]], "captain": name(wc7_h["captain"])}
    (Path(os.environ["PACKET_DIR"]) / "chips_gw7.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    for key, value in out.items():
        line = f"{key:28s} {value['gain']:+6.1f}"
        if "out" in value:
            line += f"  OUT {', '.join(value['out'])} | IN {', '.join(value['in'])} (hits {value['hits']})"
        if "keeps" in value:
            line += f"  keeps {len(value['keeps'])}: {', '.join(value['keeps'])} | C {value['captain']}"
        print(line)
    print("GW7 wildcard squad:", ", ".join(out["gw7_wildcard"]["squad"]), "| bank", out["gw7_wildcard"]["bank_after"])


if __name__ == "__main__":
    main()

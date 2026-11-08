"""Cost every legal 1-3 transfer route for GW6 (and the roll-to-GW7 variant)
on classic+F6 forecasts, with and without Haaland, from Wes's actual squad.

EV over GW6-10 = best legal XI by points + captain doubled + 0.1 x bench.
Roll variant: GW6 played by the current squad (1gw), transfers land in GW7
(5gw - 1gw for the remaining four weeks), one extra free transfer banked.
"""
import itertools
import json
from collections import Counter

T = "/home/wescheng/projects/fpl/fpl/reports/adapter_bench_2026_09_29"
F = {r["player_id"]: r for r in map(json.loads, open(f"{T}/gw6_2627_classic_f6_forecasts.jsonl"))}
TEAM = {t["id"]: t["short_name"] for t in json.load(open(f"{T}/bootstrap_2026_09_28.json"))["teams"]}

# Squad after GW5 with selling prices reconstructed from purchase prices.
SQUAD = {  # player_id: selling price
    467: 5.0, 384: 5.5,                          # Sels, Donnarumma
    327: 5.0, 204: 4.5, 332: 4.5, 469: 5.0, 31: 4.5,   # Bijol Mitchell Justin N.Williams Konsa
    426: 11.9, 428: 7.9, 12: 9.5, 124: 5.6, 399: 7.7,  # Bruno Cunha Saka Groß Cherki
    165: 7.6, 379: 9.1, 79: 6.0,                  # João Pedro Isak Evanilson
}
BANK = 0.3
HAALAND = 411
FORMATIONS = [(d, m, f) for d in range(3, 6) for m in range(2, 6) for f in range(1, 4) if d + m + f == 10]


def ev(ids, key):
    by = {"GK": [], "DEF": [], "MID": [], "FWD": []}
    for i in ids:
        by[F[i]["pos"]].append(i)
    for pos in by:
        by[pos].sort(key=lambda i: -key(i))
    best = None
    for d, m, f in FORMATIONS:
        if len(by["DEF"]) < d or len(by["MID"]) < m or len(by["FWD"]) < f:
            continue
        xi = by["GK"][:1] + by["DEF"][:d] + by["MID"][:m] + by["FWD"][:f]
        bench = [i for i in ids if i not in xi]
        score = sum(key(i) for i in xi) + max(key(i) for i in xi) + 0.1 * sum(key(i) for i in bench if F[i]["pos"] != "GK")
        if best is None or score > best[0]:
            best = (score, xi, max(xi, key=key))
    return best


p1 = lambda i: F[i]["p1"]  # noqa: E731
p5 = lambda i: F[i]["p5"]  # noqa: E731
rest = lambda i: F[i]["p5"] - F[i]["p1"]  # noqa: E731

squad = list(SQUAD)
hold_now = ev(squad, p5)[0]
hold_roll = ev(squad, p1)[0] + ev(squad, rest)[0]

# Candidate pool: top 30 per position by 5gw, excluding unavailable.
pool = {}
for pos in ("GK", "DEF", "MID", "FWD"):
    cands = [r for r in F.values() if r["pos"] == pos and r["status"] not in ("u", "i", "s") and r["player_id"] not in SQUAD]
    pool[pos] = [r["player_id"] for r in sorted(cands, key=lambda r: -r["p5"])[:30]]


def legal(ids):
    teams = Counter(F[i]["team_id"] for i in ids)
    return max(teams.values()) <= 3


results = []
for k in (1, 2, 3):
    for outs in itertools.combinations(squad, k):
        out_pos = sorted(F[i]["pos"] for i in outs)
        budget = BANK + sum(SQUAD[i] for i in outs)
        # candidate ins: product over positions (small pools keep this tractable)
        pos_need = Counter(out_pos)
        per_pos_choices = []
        for pos, n in pos_need.items():
            per_pos_choices.append(list(itertools.combinations(pool[pos][:18 if k == 3 else 30], n)))
        for combo in itertools.product(*per_pos_choices):
            ins = [i for group in combo for i in group]
            cost = sum(F[i]["price"] for i in ins)
            if cost > budget + 1e-9:
                continue
            new = [i for i in squad if i not in outs] + ins
            if not legal(new):
                continue
            now = ev(new, p5)[0] - 4 * max(0, k - 1)
            roll = ev(squad, p1)[0] + ev(new, rest)[0] - 4 * max(0, k - 2)
            results.append((k, outs, tuple(ins), now, roll, round(budget - cost, 1)))

name = lambda i: F[i]["name"]  # noqa: E731
print(f"HOLD: GW6-10 EV {hold_now:.1f} (transfer now baseline) | {hold_roll:.1f} (roll baseline)")
for label, filt in [("with Haaland", lambda r: HAALAND in r[2]), ("without Haaland", lambda r: HAALAND not in r[2])]:
    for k in (1, 2, 3):
        sub = [r for r in results if r[0] == k and filt(r)]
        if not sub:
            print(f"\n{label}, {k} transfer(s): no legal route")
            continue
        print(f"\n{label}, {k} transfer(s) — best 4 if done in GW6 (hit {4*max(0,k-1)}):")
        for r in sorted(sub, key=lambda r: -r[3])[:4]:
            print(f"  {r[3]-hold_now:+6.1f}  OUT {', '.join(map(name, r[1]))} | IN {', '.join(map(name, r[2]))}  (itb {r[5]})")
        print(f"{label}, {k} transfer(s) — best 3 if rolled to GW7 (hit {4*max(0,k-2)}):")
        for r in sorted(sub, key=lambda r: -r[4])[:3]:
            print(f"  {r[4]-hold_roll:+6.1f}  OUT {', '.join(map(name, r[1]))} | IN {', '.join(map(name, r[2]))}  (itb {r[5]})")

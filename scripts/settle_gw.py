"""Settle a finished gameweek for entry 6535607 from the public FPL API (written 2026-11-03 for GW9).

Fetches the settled entry files into <packet>/entry/ (same names as the GW8 settlement), prints the entered XI with
realised minutes/points, the API's own auto-subs and the history row, then scores hindsight XIs (a JSON list of
{label, xi, bench, captain, vice, expected, hit}) with the FPL auto-sub rules: bench GK replaces only the GK; outfield
bench players come on in bench order for the first non-player that keeps the formation legal (1 GK, 3-5 DEF, 2-5 MID,
1-3 FWD); the vice takes the armband when the captain has 0 minutes. Names resolve through the packet's forecast file
(web_name as used in every packet sheet), so the expected points column is the packet's own forecast.

Usage: PYTHONPATH=src python3 scripts/settle_gw.py --gw 9 --packet-dir reports/gw9_packet_2026_10 \
         --forecasts final/forecasts_new_pipeline.jsonl --xis final/hindsight_xis.json --out final/hindsight_gw9.json
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ENTRY_ID = 6535607
BASE = "https://fantasy.premierleague.com/api"
POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}
LIMITS = {"GK": (1, 1), "DEF": (3, 5), "MID": (2, 5), "FWD": (1, 3)}


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def fetch(gw: int, out: Path) -> dict:
    out.mkdir(parents=True, exist_ok=True)
    boot = get(f"{BASE}/bootstrap-static/")
    files = {
        f"elements_gw{gw}_settled": boot["elements"],
        "entry_settled": get(f"{BASE}/entry/{ENTRY_ID}/"),
        "history_settled": get(f"{BASE}/entry/{ENTRY_ID}/history/"),
        "transfers_settled": get(f"{BASE}/entry/{ENTRY_ID}/transfers/"),
        f"picks_gw{gw}": get(f"{BASE}/entry/{ENTRY_ID}/event/{gw}/picks/"),
        f"live_gw{gw}": get(f"{BASE}/event/{gw}/live/"),
        f"fixtures_gw{gw}": get(f"{BASE}/fixtures/?event={gw}"),
    }
    for name, data in files.items():
        (out / f"{name}.json").write_text(json.dumps(data))
    event = next(e for e in boot["events"] if e["id"] == gw)
    manifest = {"entry_id": ENTRY_ID, "gw": gw, "retrieved_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "finished": event["finished"], "data_checked": event["data_checked"], "average_entry_score": event["average_entry_score"],
                "highest_score": event["highest_score"], "most_captained": event.get("most_captained")}
    (out / "manifest_settled.json").write_text(json.dumps(manifest))
    files["manifest"] = manifest
    files["teams"] = boot["teams"]
    return files


def formation_ok(pos_counts: dict) -> bool:
    return sum(pos_counts.values()) == 11 and all(LIMITS[p][0] <= pos_counts.get(p, 0) <= LIMITS[p][1] for p in LIMITS)


def score_xi(xi, bench, captain, vice, info, multiplier=2):
    """xi/bench: element ids (bench[0] must be the GK); info[id] = {pos, minutes, points, name}. Returns dict."""
    final = list(xi)
    subs = []
    played = lambda e: info[e]["minutes"] > 0
    # bench GK
    gk = [e for e in final if info[e]["pos"] == "GK"][0]
    if not played(gk) and played(bench[0]):
        final[final.index(gk)] = bench[0]; subs.append((gk, bench[0]))
    for b in bench[1:]:
        if not played(b):
            continue
        for s in list(final):
            if played(s) or info[s]["pos"] == "GK" or s in [x[1] for x in subs]:
                continue
            trial = [b if e == s else e for e in final]
            counts = {}
            for e in trial:
                counts[info[e]["pos"]] = counts.get(info[e]["pos"], 0) + 1
            if formation_ok(counts):
                final = trial; subs.append((s, b)); break
    cap = captain if played(captain) else (vice if played(vice) else None)
    pts = sum(info[e]["points"] for e in final)
    cap_bonus = (multiplier - 1) * info[cap]["points"] if cap is not None and cap in final else 0
    return {"points": pts + cap_bonus, "xi_points": pts, "captain_used": info[cap]["name"] if cap else None, "captain_bonus": cap_bonus,
            "final_xi": [info[e]["name"] for e in final], "auto_subs": [(info[a]["name"], info[b]["name"], info[b]["points"]) for a, b in subs],
            "bench_points": sum(info[e]["points"] for e in bench if e not in final)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gw", type=int, required=True)
    ap.add_argument("--packet-dir", required=True)
    ap.add_argument("--forecasts", default="final/forecasts_new_pipeline.jsonl")
    ap.add_argument("--xis", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    packet = Path(a.packet_dir)
    files = fetch(a.gw, packet / "entry")
    live = {e["id"]: e["stats"] for e in files[f"live_gw{a.gw}"]["elements"]}
    elements = {e["id"]: e for e in files[f"elements_gw{a.gw}_settled"]}
    teams = {t["id"]: t["short_name"] for t in files["teams"]}
    fc = {}
    for line in open(packet / a.forecasts):
        r = json.loads(line); fc[r["player_id"]] = r
    info = {}
    for eid, e in elements.items():
        st = live.get(eid, {})
        info[eid] = {"name": e["web_name"], "pos": POS[e["element_type"]], "team": teams[e["team"]], "minutes": st.get("minutes", 0),
                     "points": st.get("total_points", 0), "bonus": st.get("bonus", 0), "goals": st.get("goals_scored", 0),
                     "assists": st.get("assists", 0), "cs": st.get("clean_sheets", 0), "dc": st.get("defensive_contribution", 0),
                     "p1": fc.get(eid, {}).get("p1"), "papp": fc.get(eid, {}).get("papp"), "mins_fc": fc.get(eid, {}).get("mins"),
                     "status": fc.get(eid, {}).get("status"), "news": fc.get(eid, {}).get("news")}
    by_name = {}
    for eid, r in fc.items():
        by_name.setdefault(r["name"], []).append(eid)

    def resolve(name):
        ids = by_name.get(name, [])
        if len(ids) != 1:
            ids = [eid for eid, e in elements.items() if e["web_name"] == name]
        if len(ids) != 1:
            raise SystemExit(f"cannot resolve {name!r}: {ids}")
        return ids[0]

    picks = files[f"picks_gw{a.gw}"]
    hist = next(h for h in files["history_settled"]["current"] if h["event"] == a.gw)
    print(f"GW{a.gw} entry {ENTRY_ID}: points {hist['points']} (bench {hist['points_on_bench']}), total {hist['total_points']}, "
          f"overall rank {hist['overall_rank']:,}, gw rank {hist['rank']:,}, transfers {hist['event_transfers']} (cost {hist['event_transfers_cost']}), "
          f"bank {hist['bank'] / 10:.1f}, value {hist['value'] / 10:.1f}; chip {picks['active_chip']}; league avg {files['manifest']['average_entry_score']}")
    print("entered squad (position order):")
    xi_ids, bench_ids, cap, vice = [], [], None, None
    for p in picks["picks"]:
        e = info[p["element"]]
        flag = " (C)" if p["is_captain"] else " (VC)" if p["is_vice_captain"] else ""
        print(f"  {p['position']:2d} {e['name']:<12} {e['pos']:<3} {e['team']:<4} min {e['minutes']:3d} pts {e['points']:3d} x{p['multiplier']}{flag}"
              f"  | fc {e['p1']} papp {e['papp']} status {e['status']}")
        (xi_ids if p["position"] <= 11 else bench_ids).append(p["element"])
        if p["is_captain"]:
            cap = p["element"]
        if p["is_vice_captain"]:
            vice = p["element"]
    print("API auto-subs:", [(info[s['element_out']]['name'], info[s['element_in']]['name']) for s in picks.get("automatic_subs", [])])
    mult = 3 if picks["active_chip"] == "3xc" else 2
    check = score_xi(xi_ids, bench_ids, cap, vice, info, mult)
    print(f"evaluator on the entered team: {check['points']} (API {hist['points']}); subs {check['auto_subs']}; captain {check['captain_used']}")
    transfers = [t for t in files["transfers_settled"] if t["event"] == a.gw]
    print("transfers this GW:", [(info[t['element_out']]['name'], t['element_out_cost'] / 10, '->', info[t['element_in']]['name'], t['element_in_cost'] / 10) for t in transfers])
    results = {"entered": {"points": hist["points"], "chip": picks["active_chip"], "bench": hist["points_on_bench"], "rank": hist["overall_rank"],
                           "total": hist["total_points"], "captain": info[cap]["name"], "vice": info[vice]["name"],
                           "xi": [info[e]["name"] for e in xi_ids], "bench_order": [info[e]["name"] for e in bench_ids],
                           "auto_subs": check["auto_subs"], "transfers": [(info[t['element_out']]['name'], info[t['element_in']]['name']) for t in transfers],
                           "league_avg": files["manifest"]["average_entry_score"]},
               "players": {info[e]["name"]: info[e] for e in xi_ids + bench_ids}, "hindsight": []}
    if a.xis:
        for spec in json.load(open(packet / a.xis)):
            xi = [resolve(n) for n in spec["xi"]]; bench = [resolve(n) for n in spec["bench"]]
            r = score_xi(xi, bench, resolve(spec["captain"]), resolve(spec["vice"]), info, spec.get("multiplier", 2))
            exp = sum(info[e]["p1"] or 0 for e in xi) + (info[resolve(spec["captain"])]["p1"] or 0) * (spec.get("multiplier", 2) - 1)
            r.update({"label": spec["label"], "expected_packet": round(exp, 1), "expected_sheet": spec.get("expected"), "hit": spec.get("hit", 0),
                      "net": r["points"] - spec.get("hit", 0)})
            results["hindsight"].append(r)
            print(f"{spec['label']:<70} expected {r['expected_packet']:5.1f} realised {r['points']:3d} net {r['net']:3d}  subs {r['auto_subs']}  C {r['captain_used']}")
    for n in sorted(set(sum([s["xi"] + s["bench"] for s in (json.load(open(packet / a.xis)) if a.xis else [])], [])) | set(results["players"])):
        e = info[resolve(n)]
        results["players"][n] = e
    if a.out:
        (packet / a.out).write_text(json.dumps(results, indent=1, ensure_ascii=False))
        print("wrote", packet / a.out)


if __name__ == "__main__":
    main()

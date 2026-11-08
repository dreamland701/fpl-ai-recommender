"""Shadow read: an adapter's GW7 deltas against its own classic baselines.

usage: shadow_sheet.py <examples.jsonl> <predictions.jsonl> <label>

Deltas go through the same parser and apply function as the backtests
(fpl_ai.llm_adjust). Reports the entered squad and the main targets, the
availability calls where the adapter disagrees with classic, and what the
decision layer would do on each forecast set. Writes shadow_<label>.json under
PACKET_DIR. The adapter is in shadow: classic + F6 makes the GW7 decision.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.decision import recommend_actions  # noqa: E402
from fpl_ai.llm_adjust import apply_deltas_to_forecast, parse_delta_response  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer, SquadState  # noqa: E402

HERE = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
TARGETS = ("Haaland", "De Cuyper", "E.Le Fée", "Xhaka", "Rogers", "Hall", "Mbeumo", "Semenyo", "Palmer")


def main() -> None:
    examples_path, predictions_path, label = sys.argv[1], sys.argv[2], sys.argv[3]
    examples = [json.loads(line) for line in open(examples_path) if line.strip()]
    predictions = {}
    for line in open(predictions_path):
        if line.strip():
            row = json.loads(line)
            predictions[int(row["metadata"]["player_id"])] = row
    if len(predictions) != len(examples):
        raise SystemExit(f"{len(predictions)} predictions for {len(examples)} examples")
    bootstrap = json.loads((HERE / "snapshot" / "bootstrap_static.json").read_text())
    price = {e["id"]: e["now_cost"] / 10.0 for e in bootstrap["elements"]}
    state = json.loads((HERE / "entry_state.json").read_text())
    classic, adapted, parsed = {}, {}, 0
    for example in examples:
        m = example["metadata"]
        b = m["baseline_forecast"]
        pid = int(m["player_id"])
        forecast = PlayerForecast(
            season=str(m["season"]), week=int(m["week"]), player_id=pid, player_name=str(m["player_name"]),
            team_id=int(m["team_id"]), position=str(m["position"]), price=price.get(pid, 0.0),
            predicted_minutes=float(b["baseline_minutes_1gw"]), predicted_points_1gw=float(b["baseline_points_1gw"]),
            predicted_points_3gw=float(b["baseline_points_3gw"]), predicted_points_5gw=float(b["baseline_points_5gw"]),
            appearance_probability=float(b["baseline_appearance_probability"]),
            fixture_count=int(m.get("fixture_count", 1)), uncertainty=float(b.get("baseline_uncertainty") or 0.2),
        )
        deltas = parse_delta_response(str(predictions[pid].get("response") or ""))
        parsed += deltas is not None
        classic[pid] = forecast
        adapted[pid] = apply_deltas_to_forecast(forecast, deltas, "all")
    by_name = {f.player_name: pid for pid, f in classic.items()}
    squad_ids = [s["player_id"] for s in state["squad"]]
    rows = []
    for pid in squad_ids + [by_name[n] for n in TARGETS if n in by_name]:
        c, a = classic[pid], adapted[pid]
        rows.append({"player": c.player_name, "in_squad": pid in squad_ids,
                     "classic": {"p1": round(c.predicted_points_1gw, 2), "p5": round(c.predicted_points_5gw, 2),
                                 "papp": round(c.appearance_probability, 2)},
                     "adapter": {"p1": round(a.predicted_points_1gw, 2), "p5": round(a.predicted_points_5gw, 2),
                                 "papp": round(a.appearance_probability, 2)}})
    disagreements = sorted(
        ({"player": classic[p].player_name, "classic_papp": round(classic[p].appearance_probability, 2),
          "adapter_papp": round(adapted[p].appearance_probability, 2)}
         for p in classic
         if classic[p].appearance_probability >= 0.3 and classic[p].predicted_points_1gw >= 2.5
         and abs(adapted[p].appearance_probability - classic[p].appearance_probability) >= 0.10),
        key=lambda r: r["adapter_papp"] - r["classic_papp"])
    squad = [SquadPlayer(s["player_id"], s["name"], classic[s["player_id"]].team_id, classic[s["player_id"]].position,
                         s["selling_price"], s["purchase_price"]) for s in state["squad"]]
    decisions = {}
    for side, forecasts in (("classic", classic), ("adapter", adapted)):
        bundle = recommend_actions(
            SquadState(season="2026-27", week=6, squad_players=squad, bank=state["bank"],
                       free_transfers=state["free_transfers"], chips_available={}),
            list(forecasts.values()), top_n_transfers=3, max_transfers_considered=2)
        name = lambda i: forecasts[i].player_name  # noqa: E731
        decisions[side] = {
            "xi": [name(i) for i in bundle.starters], "bench": [name(i) for i in bundle.bench_order],
            "captain": name(bundle.captain_id), "vice": name(bundle.vice_captain_id),
            "transfers": [{"out": [name(i) for i in t.players_out], "in": [name(i) for i in t.players_in],
                           "gain": round(t.projected_gain, 2), "hit": t.hit_cost} for t in bundle.transfers],
        }
    result = {"label": label, "examples": len(examples), "parsed": parsed, "rows": rows,
              "availability_disagreements": disagreements, "decisions": decisions}
    (HERE / f"shadow_{label}.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
    print(f"{label}: parsed {parsed}/{len(examples)}")
    for r in rows:
        c, a = r["classic"], r["adapter"]
        print(f"  {'*' if r['in_squad'] else ' '} {r['player']:12s} p1 {c['p1']:5.2f} -> {a['p1']:5.2f}  "
              f"p5 {c['p5']:5.1f} -> {a['p5']:5.1f}  P(app) {c['papp']:.2f} -> {a['papp']:.2f}")
    print("  availability disagreements (likely starters):",
          ", ".join(f"{d['player']} {d['classic_papp']}->{d['adapter_papp']}" for d in disagreements) or "none")
    for side, d in decisions.items():
        moves = "; ".join(f"{'+'.join(t['out'])}->{'+'.join(t['in'])} {t['gain']:+.1f}" for t in d["transfers"][:2])
        print(f"  {side:8s} C {d['captain']} VC {d['vice']} | top moves: {moves}")
    # Wes (2026-10-07): every week, show classic's best XI next to classic + SFT,
    # with the text the adapter read behind each move.
    import subprocess
    subprocess.run([sys.executable, str(Path(__file__).resolve().parents[2] / "scripts" / "sft_side_by_side.py"),
                    "--examples", examples_path, "--predictions", predictions_path,
                    "--entry-state", str(HERE / "entry_state.json"), "--label", label,
                    "--output-md", str(HERE / f"sft_side_by_side_{label}.md")], check=False)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Weekly sheet: classic best XI next to classic + SFT, and why the SFT moved each player.

The adapter outputs bare JSON deltas, so the "why" shown is what it read: the
status/news line and the evidence snippets in its prompt. Each 1GW points delta
is split into a generic part (this week's linear shrink on the baseline,
fitted across every player decoded, so it is the same rule for everyone) and a
player-specific remainder, which is the part worth reading the evidence for.

The written delta is the greedy decode: the single most likely value, which
for a skewed spread can sit far from the adapter's average belief. With
--expected-predictions (scripts/expectation_decode.py output) the sheet also
shows the expected deltas and P(cut), and a third XI built from them.

usage: sft_side_by_side.py --examples E --predictions P --entry-state S --label L --output-md M
       [--transfer OUT_NAME:IN_NAME ...]   (apply planned moves before picking the XI)
       [--expected-predictions X]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.decision import _optimize_lineup  # noqa: E402
from fpl_ai.llm_adjust import apply_deltas_to_forecast, parse_delta_response  # noqa: E402
from fpl_ai.types import PlayerForecast, SquadPlayer  # noqa: E402

TARGETS = ("Haaland", "De Cuyper", "E.Le Fée", "Xhaka", "Rogers", "Hall", "Semenyo", "Mbeumo")


def evidence_snippets(prompt: str, limit: int = 2, chars: int = 280):
    section = prompt.split("Timestamp-safe text evidence:", 1)
    if len(section) < 2 or "No timestamp-safe text evidence is available" in section[1][:200]:
        return []
    docs = re.split(r"\n\[\d+\] ", "\n" + section[1].split("<|turn>", 1)[0].strip())
    out = []
    for doc in docs:
        doc = doc.strip()
        if not doc:
            continue
        lines = doc.splitlines()
        header = lines[0].strip()
        title = next((l[len("Title:"):].strip() for l in lines if l.startswith("Title:")), "")
        text = " ".join(l[len("Text:"):].strip() if l.startswith("Text:") else "" for l in lines).strip()
        out.append({"source": header, "title": title, "text": text[:chars]})
    return out[:limit]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--examples", required=True)
    ap.add_argument("--predictions", required=True)
    ap.add_argument("--entry-state", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--output-md", required=True)
    ap.add_argument("--transfer", action="append", default=[], help="OUT_NAME:IN_NAME, applied before the XI is picked")
    ap.add_argument("--expected-predictions", help="expectation_decode.py output: adds expected deltas, P(cut) and a third XI")
    args = ap.parse_args()

    examples = [json.loads(l) for l in open(args.examples) if l.strip()]
    preds = {}
    for l in open(args.predictions):
        if l.strip():
            p = json.loads(l)
            preds[int(p["metadata"]["player_id"])] = p
    expected_preds = {}
    if args.expected_predictions:
        for l in open(args.expected_predictions):
            if l.strip():
                p = json.loads(l)
                expected_preds[int(p["metadata"]["player_id"])] = p
    state = json.loads(Path(args.entry_state).read_text())
    classic, adapted, expected, info = {}, {}, {}, {}
    for e in examples:
        m = e["metadata"]; b = m["baseline_forecast"]; pid = int(m["player_id"])
        f = PlayerForecast(
            season=str(m["season"]), week=int(m["week"]), player_id=pid, player_name=str(m["player_name"]),
            team_id=int(m["team_id"]), position=str(m["position"]), price=0.0,
            predicted_minutes=float(b["baseline_minutes_1gw"]), predicted_points_1gw=float(b["baseline_points_1gw"]),
            predicted_points_3gw=float(b["baseline_points_3gw"]), predicted_points_5gw=float(b["baseline_points_5gw"]),
            appearance_probability=float(b["baseline_appearance_probability"]),
            fixture_count=int(m.get("fixture_count", 1)), uncertainty=float(b.get("baseline_uncertainty") or 0.2))
        raw = parse_delta_response(str(preds.get(pid, {}).get("response") or "")) or {}
        classic[pid] = f
        adapted[pid] = apply_deltas_to_forecast(f, raw, "all")
        info[pid] = {"prompt": e["prompt"], "deltas": raw}
        if pid in expected_preds:
            ep = expected_preds[pid]
            expected[pid] = apply_deltas_to_forecast(f, parse_delta_response(str(ep["response"])) or {}, "all")
            info[pid]["p_cut"] = ep.get("expectation_diagnostics", {}).get("delta_points_1gw", {}).get("p_cut")
    base = np.array([classic[p].predicted_points_1gw for p in classic])
    d1 = np.array([adapted[p].predicted_points_1gw - classic[p].predicted_points_1gw for p in classic])
    slope, intercept = np.polyfit(base, d1, 1)
    generic = {p: slope * classic[p].predicted_points_1gw + intercept for p in classic}

    by_name = {f.player_name: pid for pid, f in classic.items()}
    sell = {s["player_id"]: s["selling_price"] for s in state["squad"]}
    for move in args.transfer:
        out_name, in_name = move.split(":")
        sell.pop(by_name[out_name])
        sell[by_name[in_name]] = 0.0
    squad = [SquadPlayer(pid, classic[pid].player_name, classic[pid].team_id, classic[pid].position, price)
             for pid, price in sell.items()]
    picks = {}
    full_expected = bool(expected) and all(pid in expected for pid in sell)
    sides = [("classic", classic), ("sft", adapted)] + ([("expected", expected)] if full_expected else [])
    for side, forecasts in sides:
        xi, bench, cap, vice, _ = _optimize_lineup(squad, forecasts)
        total = sum(forecasts[i].predicted_points_1gw for i in xi) + forecasts[cap].predicted_points_1gw
        picks[side] = {"xi": xi, "bench": bench, "captain": cap, "vice": vice, "total": total}
    name = lambda i: classic[i].player_name  # noqa: E731

    def status_line(pid):
        text = info[pid]["prompt"]
        status = re.search(r"Status pre-deadline: (.*)", text)
        news = re.search(r"Official player news pre-deadline: (.*)", text)
        return (status.group(1).strip() if status else "?"), (news.group(1).strip() if news else "")

    lines = [f"# Classic vs classic + SFT ({args.label}), GW{examples[0]['week']}", "",
             f"Planned moves applied: {', '.join(args.transfer) or 'none'}. The decision still comes from classic; this sheet shows what the adapter would change and why.",
             "",
             f"This week's generic SFT shrink: delta = {slope:+.3f} x classic forecast {intercept:+.3f}. "
             f"For a 2-point player that is {slope * 2 + intercept:+.2f}; for an 8-point player {slope * 8 + intercept:+.2f}. "
             "That part is the same rule for everyone (the adapter aiming at the typical outcome rather than the average); "
             "the player-specific remainder is what reflects the text it read.", "",
             "## Lineups", ""]
    cols = [c for c in ("classic", "sft", "expected") if c in picks]
    head = {"classic": "Classic", "sft": "Classic + SFT (as written)", "expected": "Classic + SFT (its average)"}
    lines += ["| | " + " | ".join(head[c] for c in cols) + " |", "|---" * (len(cols) + 1) + "|"]
    for key, label in (("xi", "XI"), ("bench", "Bench (in order)")):
        lines.append(f"| {label} | " + " | ".join(", ".join(name(i) for i in picks[c][key]) for c in cols) + " |")
    lines.append("| Captain / vice | " + " | ".join(f"{name(picks[c]['captain'])} / {name(picks[c]['vice'])}" for c in cols) + " |")
    lines.append("| Expected GW points (incl. captain, own forecasts) | " + " | ".join(f"{picks[c]['total']:.1f}" for c in cols) + " |")
    changed = [i for i in set(picks["classic"]["xi"]) ^ set(picks["sft"]["xi"])]
    if changed:
        lines += ["", "XI differences: " + ", ".join(
            f"{name(i)} ({'classic only' if i in picks['classic']['xi'] else 'SFT only'})" for i in changed)]
    rows = [pid for pid in sell] + [by_name[n] for n in TARGETS if n in by_name and by_name[n] not in sell]
    exp_cols = bool(expected)
    lines += ["", "## Every squad player and the main targets", "",
              "| Player | Status / news | Classic GW | SFT GW | Generic shrink | Player-specific | "
              + ("SFT average GW | P(cut) | " if exp_cols else "") + "P(appear) classic → SFT |",
              "|---|---|---|---|---|---|---|" + ("---|---|" if exp_cols else "")]
    for pid in rows:
        c, a = classic[pid], adapted[pid]
        delta = a.predicted_points_1gw - c.predicted_points_1gw
        status, news = status_line(pid)
        flag = status if not news or news == "none" else f"{status}: {news[:50]}"
        lines.append(f"| {'**' + c.player_name + '**' if pid in sell else c.player_name} | {flag} | {c.predicted_points_1gw:.2f} | "
                     f"{a.predicted_points_1gw:.2f} | {generic[pid]:+.2f} | {delta - generic[pid]:+.2f} | "
                     + (f"{expected[pid].predicted_points_1gw:.2f} | {info[pid].get('p_cut') or 0:.0%} | " if exp_cols and pid in expected
                        else ("– | – | " if exp_cols else ""))
                     + f"{c.appearance_probability:.2f} → {a.appearance_probability:.2f} |")
    notable = [pid for pid in rows if abs((adapted[pid].predicted_points_1gw - classic[pid].predicted_points_1gw) - generic[pid]) >= 0.3
               or abs(adapted[pid].appearance_probability - classic[pid].appearance_probability) >= 0.1]
    lines += ["", "## What the adapter read for the players it singled out", "",
              "Listed when the player-specific part is at least 0.3 points or P(appear) moved by 0.1 or more. "
              "The text is exactly what was in the prompt; the adapter gives no reasons of its own.", ""]
    for pid in notable:
        c, a = classic[pid], adapted[pid]
        status, news = status_line(pid)
        delta = a.predicted_points_1gw - c.predicted_points_1gw
        lines.append(f"### {c.player_name}: {c.predicted_points_1gw:.2f} → {a.predicted_points_1gw:.2f} "
                     f"(generic {generic[pid]:+.2f}, specific {delta - generic[pid]:+.2f}); "
                     f"P(appear) {c.appearance_probability:.2f} → {a.appearance_probability:.2f}")
        if pid in expected:
            lines.append(f"- Written {delta:+.1f}, but its average over the full spread is "
                         f"{expected[pid].predicted_points_1gw - c.predicted_points_1gw:+.2f} (P(cut) {info[pid].get('p_cut') or 0:.0%}).")
        lines.append(f"- Status: {status}; news: {news or 'none'}")
        docs = evidence_snippets(info[pid]["prompt"])
        if not docs:
            lines.append("- No text evidence in the prompt: the move comes from the numbers and status alone.")
        for doc in docs:
            lines.append(f"- *{doc['source']}* — {doc['title']}: \"{doc['text']}\"")
        lines.append("")
    Path(args.output_md).write_text("\n".join(lines) + "\n")
    print(f"wrote {args.output_md} ({len(notable)} players with notable SFT moves)")


if __name__ == "__main__":
    main()

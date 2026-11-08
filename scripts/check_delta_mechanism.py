#!/usr/bin/env python3
"""Does the adapter actually RESPOND to the signal it was built to use?

WHY THIS EXISTS (2026-09-21, the E17 lesson)
--------------------------------------------
E17 won its decision backtest (300 vs 260) and looked like a ship candidate.
It wasn't. Its deltas turned out to be uncorrelated with BOTH signals the run
was designed around: partial correlation with the opponent's goals-conceded
-0.0506, with injured team-mates -0.0328. The prompt asked for a fixture
adjustment; the model declined. Whatever produced the +40, it was not the
mechanism we built, so the result carried no transferable claim.

An outcome without a mechanism is a coincidence until proven otherwise. From
E18 on, every adapter reports this alongside its decision value.

THE CONFOUND THIS CONTROLS FOR
------------------------------
Raw correlations are useless here because the adapter's dominant behaviour is
a shrink proportional to the baseline (corr(delta, baseline) ~= -0.69). Any
signal that correlates with the baseline — and opponent weakness does, since
good fixtures raise forecasts — will show a spurious correlation with the
delta. So every number below is a PARTIAL correlation with the baseline
regressed out of both sides.

READING IT
----------
  |partial| < 0.05   the channel is OFF. The model ignores this signal.
  0.05-0.15           weak; real only if the sign is right and n is large.
  > 0.15              the model is genuinely responding.
Sign matters as much as size: for opponent goals-conceded, a POSITIVE partial
is correct (leakier opponent -> revise up).
"""

from __future__ import annotations

import argparse
import json
import re

import numpy as np


SIGNALS = {
    # name: (regex over the prompt, "higher means" description, expected sign)
    "opponent goals conceded": (
        re.compile(r"conceding ([0-9.]+)/game"),
        "leakier opponent",
        +1,
    ),
    "opponent defence rank": (
        re.compile(r"([0-9]+)(?:st|nd|rd|th)-meanest defence"),
        "worse-ranked defence",
        +1,
    ),
}
COUNT_SIGNALS = {
    "injured/doubtful team-mates": (
        re.compile(r"INJURED|doubtful|suspended|unavailable"),
        "more rivals out",
        +1,
    ),
}

# The count regexes must only be applied inside their own prompt block. Found
# 2026-09-26 on E19: the injury words matched inside the attached NEWS text, so
# a run with no depth-chart block at all reported the signal as "present" and
# then flagged it WRONG SIGN. The partial was in fact −0.079, which is the model
# correctly marking down a player whose own evidence mentions an injury — right
# behaviour, wrong label. Scope the search to the block or the reading is junk.
BLOCK_HEADINGS = {
    "injured/doubtful team-mates": "Positional depth chart",
}


def _section(text: str, heading: str) -> str:
    """The prompt text belonging to one block, or "" when the block is absent."""
    start = text.find(heading)
    if start < 0:
        return ""
    rest = text[start + len(heading):]
    # blocks are separated by a blank line followed by a new capitalised label
    end = rest.find("\n\n")
    return rest if end < 0 else rest[:end]


def partial_corr(x, y, control):
    """corr(x, y) with `control` linearly regressed out of both."""
    x, y, control = np.asarray(x, float), np.asarray(y, float), np.asarray(control, float)
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(control)
    x, y, control = x[ok], y[ok], control[ok]
    if len(x) < 50 or np.std(control) == 0:
        return float("nan"), len(x)
    rx = x - np.poly1d(np.polyfit(control, x, 1))(control)
    ry = y - np.poly1d(np.polyfit(control, y, 1))(control)
    if np.std(rx) == 0 or np.std(ry) == 0:
        return float("nan"), len(x)
    return float(np.corrcoef(rx, ry)[0, 1]), len(x)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--examples", required=True, help="the split's eval.jsonl (carries the prompts)")
    ap.add_argument("--predictions", required=True, help="decoded predictions, same order")
    ap.add_argument("--label", default="adapter")
    ap.add_argument("--field", default="delta_points_1gw")
    args = ap.parse_args()

    examples = [json.loads(line) for line in open(args.examples) if line.strip()]
    predictions = [json.loads(line) for line in open(args.predictions) if line.strip()]
    if len(examples) != len(predictions):
        print(f"WARNING: {len(examples)} examples vs {len(predictions)} predictions; zipping to the shorter")

    deltas, baselines, texts = [], [], []
    for example, prediction in zip(examples, predictions):
        try:
            parsed = json.loads(prediction["response"])
        except Exception:
            continue
        baseline = (prediction.get("metadata", {}).get("baseline_forecast") or {}).get("baseline_points_1gw")
        if baseline is None:
            continue
        deltas.append(float(parsed.get(args.field, 0.0)))
        baselines.append(float(baseline))
        texts.append(example.get("text") or example.get("prompt") or json.dumps(example))

    if not deltas:
        print("no usable rows")
        return 1

    shrink = np.corrcoef(deltas, baselines)[0, 1]
    print(f"[{args.label}] n={len(deltas)}  mean {args.field} {np.mean(deltas):+.3f}")
    print(f"[{args.label}] corr({args.field}, baseline) = {shrink:+.3f}   <- the shrink being controlled for")
    print()
    print(f"{'signal':30s} {'higher means':22s} {'partial':>8s} {'n':>6s}  verdict")

    any_live = False
    any_present = False
    for name, (pattern, meaning, expected) in SIGNALS.items():
        values = []
        for text in texts:
            match = pattern.search(text)
            values.append(float(match.group(1)) if match else np.nan)
        if np.isfinite(values).sum() < 50:
            print(f"{name:30s} {meaning:22s} {'--':>8s} {int(np.isfinite(values).sum()):>6d}  absent from prompts")
            continue
        any_present = True
        r, n = partial_corr(values, deltas, baselines)
        verdict = _verdict(r, expected)
        any_live |= abs(r) >= 0.05 and np.sign(r) == expected
        print(f"{name:30s} {meaning:22s} {r:+8.4f} {n:>6d}  {verdict}")

    for name, (pattern, meaning, expected) in COUNT_SIGNALS.items():
        heading = BLOCK_HEADINGS.get(name)
        scoped = [_section(t, heading) if heading else t for t in texts]
        values = [float(len(pattern.findall(chunk))) for chunk in scoped]
        if np.std(values) == 0:
            print(f"{name:30s} {meaning:22s} {'--':>8s} {len(values):>6d}  absent from prompts")
            continue
        any_present = True
        r, n = partial_corr(values, deltas, baselines)
        verdict = _verdict(r, expected)
        any_live |= abs(r) >= 0.05 and np.sign(r) == expected
        print(f"{name:30s} {meaning:22s} {r:+8.4f} {n:>6d}  {verdict}")

    print()
    # Distinguish "the model ignored a signal it was shown" from "the signal was
    # never in the prompt". E18 exposed this: it runs v1 prompts with no
    # opponent or depth-chart block, and the gate wrongly announced the channel
    # was dead when there was simply nothing to respond to.
    if not any_present:
        print("MECHANISM: N/A — none of the designed signals appear in these prompts,")
        print("so there is nothing for the adapter to respond to. This is expected for a")
        print("run that deliberately omits them; it is NOT evidence of a dead channel.")
    elif any_live:
        print("MECHANISM: at least one designed signal is live.")
    else:
        print("MECHANISM: the signals ARE in the prompts and NONE of them moved the delta.")
        print("Any win here is unexplained — treat it as a coincidence until a mechanism")
        print("is found.")
    return 0


def _verdict(r: float, expected: int) -> str:
    if not np.isfinite(r):
        return "n/a"
    if abs(r) < 0.05:
        return "OFF (channel unused)"
    if np.sign(r) != expected:
        return "WRONG SIGN"
    return "responding" if abs(r) >= 0.15 else "weak but correct"


if __name__ == "__main__":
    raise SystemExit(main())

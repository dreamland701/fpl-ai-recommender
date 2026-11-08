#!/usr/bin/env python3
"""Mechanism check for the team-sheet retrain (H4, 2026-10-23): does the head's P(appear) move on the rows where the
team sheet carries a fact, and in the right direction on the rows where the classic model was surprised?

Compares two prediction files on identical rows (reghead_predict.py record shape: response = JSON deltas incl.
delta_appearance_probability, metadata = baseline_forecast + labels) against the team-sheet split's metadata
(team_sheet_own_facts, team_sheet_facts, team_sheet_guardian from scripts/attach_team_sheet_to_split.py).

Slices: own fact / team fact only / no fact; surprise rows = classic P >= 0.8 and did not play, or classic P <= 0.5
and played. For each slice and arm: n, AUC, Brier, mean |delta P|, and on surprise rows the mean movement toward the
truth (positive = helped). Also the correlation between the two arms' deltas and the share of rows where the arms
disagree by more than 0.1. The E17 lesson: a block is "used" only if predictions move where it carries information.

usage: team_sheet_mechanism_check.py --examples <ts split eval.jsonl> --base h1=<pred.jsonl> --test h4=<pred.jsonl> [--out md]
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

import numpy as np
from sklearn.metrics import brier_score_loss, roc_auc_score


def load_pred(path: str) -> dict[str, dict]:
    out = {}
    for line in open(path):
        r = json.loads(line); m = r["metadata"]
        key = f"{m['season']}|{m['week']}|{m['player_id']}"
        d = json.loads(r["response"]) if isinstance(r["response"], str) else r["response"]
        b = float(m["baseline_forecast"]["baseline_appearance_probability"])
        out[key] = {"b": b, "p": min(1.0, max(0.0, b + float(d.get("delta_appearance_probability", 0.0)))),
                    "y": float(m["labels"]["appearance_probability"] > 0.5), "dp": float(d.get("delta_points_1gw", 0.0)),
                    "bp": float(m["baseline_forecast"]["baseline_points_1gw"]), "yp": float(m["labels"]["points_1gw"])}
    return out


def auc(y, p):
    return roc_auc_score(y, p) if len(y) > 10 and 0 < y.mean() < 1 else float("nan")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--examples", required=True); ap.add_argument("--base", required=True); ap.add_argument("--test", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    bl, bp = args.base.split("=", 1); tl, tp = args.test.split("=", 1)
    base, test = load_pred(bp), load_pred(tp)
    meta = {}
    for line in open(args.examples):
        r = json.loads(line); m = r["metadata"]
        meta[f"{m['season']}|{m['week']}|{m['player_id']}"] = m
        i = r["prompt"].find("- This player (")
        if i >= 0:
            rest = r["prompt"][i:r["prompt"].find("\n", i)].split("): ", 1)[-1]
            m["_own_status"] = None if rest.startswith("no pre-deadline") else rest.split(" (", 1)[0]
    keys = [k for k in meta if k in base and k in test]
    y = np.array([base[k]["y"] for k in keys]); b = np.array([base[k]["b"] for k in keys])
    pb = np.array([base[k]["p"] for k in keys]); pt = np.array([test[k]["p"] for k in keys])
    own = np.array([meta[k].get("team_sheet_own_facts", 0) > 0 for k in keys])
    team = np.array([meta[k].get("team_sheet_facts", 0) > 0 for k in keys]) & ~own
    none = ~own & ~team
    surprise = ((b >= 0.8) & (y == 0)) | ((b <= 0.5) & (y == 1))
    L = [f"# Team-sheet mechanism check: {tl} vs {bl} on {len(keys)} rows ({Path(args.examples).name})\n",
         "| slice | n | played | AUC classic | AUC " + bl + " | AUC " + tl + " | Brier classic | Brier " + bl + " | Brier " + tl +
         " | mean abs dP " + bl + " | mean abs dP " + tl + " |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    for name, mask in (("own fact", own), ("team fact only", team), ("no fact", none), ("all", np.ones_like(own)),
                       ("surprise rows", surprise), ("surprise & own fact", surprise & own), ("surprise & team fact", surprise & team)):
        if mask.sum() == 0:
            continue
        L.append(f"| {name} | {int(mask.sum())} | {y[mask].mean():.2f} | {auc(y[mask], b[mask]):.3f} | {auc(y[mask], pb[mask]):.3f} | {auc(y[mask], pt[mask]):.3f} "
                 f"| {brier_score_loss(y[mask], b[mask]):.4f} | {brier_score_loss(y[mask], pb[mask]):.4f} | {brier_score_loss(y[mask], pt[mask]):.4f} "
                 f"| {np.abs(pb[mask] - b[mask]).mean():.3f} | {np.abs(pt[mask] - b[mask]).mean():.3f} |")
    L.append("\n## Movement toward the truth on surprise rows (mean of (p - b) * sign(y - b); positive = helped)\n")
    L.append(f"| slice | n | {bl} | {tl} |"); L.append("|---|---|---|---|")
    for name, mask in (("surprise rows", surprise), ("surprise & own fact", surprise & own), ("surprise & team fact", surprise & team), ("surprise & no fact", surprise & none)):
        if mask.sum() == 0:
            continue
        sgn = np.sign(y[mask] - b[mask])
        L.append(f"| {name} | {int(mask.sum())} | {((pb[mask] - b[mask]) * sgn).mean():+.3f} | {((pt[mask] - b[mask]) * sgn).mean():+.3f} |")
    corr = np.corrcoef(pb - b, pt - b)[0, 1] if len(keys) > 2 else float("nan")
    L.append(f"\nCorrelation of the two arms' availability deltas: {corr:.3f}; rows where they differ by > 0.1: "
             f"{(np.abs(pb - pt) > 0.1).mean():.1%} (own-fact rows: {(np.abs(pb - pt)[own] > 0.1).mean():.1%} of {int(own.sum())}).")
    dpb = np.array([base[k]["dp"] for k in keys]); dpt = np.array([test[k]["dp"] for k in keys])
    L.append(f"Points deltas: mean {bl} {dpb.mean():+.3f} (sd {dpb.std():.3f}), {tl} {dpt.mean():+.3f} (sd {dpt.std():.3f}); "
             f"own-fact rows {tl} {dpt[own].mean():+.3f} vs no-fact {dpt[none].mean():+.3f}.")
    # Points (1GW): the head is a median-like constant shrink in H1-H4; a mean-targeting head (H5) should move where facts are
    role = np.array([meta[k].get("_own_status") == "role" for k in keys])
    bp = np.array([base[k]["bp"] for k in keys]); yp = np.array([base[k]["yp"] for k in keys]); res = yp - bp
    L.append("\n## Points 1GW: does the delta move where the sheet carries a fact, and toward the realised residual?\n")
    L.append(f"| slice | n | MAE classic / {bl} / {tl} | RMSE classic / {bl} / {tl} | mean dP {bl} / {tl} | sd dP {bl} / {tl} | corr(dP, residual) {bl} / {tl} | closer than classic {bl} / {tl} |")
    L.append("|---|---|---|---|---|---|---|---|")
    def _corr(a, b):
        return np.corrcoef(a, b)[0, 1] if len(a) > 2 and a.std() > 1e-9 and b.std() > 1e-9 else float("nan")
    for name, mask in (("own fact", own), ("own role fact", role), ("team fact only", team), ("no fact", none), ("all", np.ones_like(own))):
        if mask.sum() == 0:
            continue
        yb, bb = yp[mask], bp[mask]; pb_, pt_ = bb + dpb[mask], bb + dpt[mask]
        L.append(f"| {name} | {int(mask.sum())} | {np.abs(bb - yb).mean():.3f} / {np.abs(pb_ - yb).mean():.3f} / {np.abs(pt_ - yb).mean():.3f} "
                 f"| {np.sqrt(((bb - yb) ** 2).mean()):.3f} / {np.sqrt(((pb_ - yb) ** 2).mean()):.3f} / {np.sqrt(((pt_ - yb) ** 2).mean()):.3f} "
                 f"| {dpb[mask].mean():+.3f} / {dpt[mask].mean():+.3f} | {dpb[mask].std():.3f} / {dpt[mask].std():.3f} "
                 f"| {_corr(dpb[mask], res[mask]):+.3f} / {_corr(dpt[mask], res[mask]):+.3f} "
                 f"| {(np.abs(pb_ - yb) < np.abs(bb - yb)).mean():.0%} / {(np.abs(pt_ - yb) < np.abs(bb - yb)).mean():.0%} |")
    text = "\n".join(L) + "\n"
    print(text)
    if args.out:
        Path(args.out).write_text(text)


if __name__ == "__main__":
    main()

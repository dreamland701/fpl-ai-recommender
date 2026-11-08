#!/usr/bin/env python3
"""Tiny numeric chip policy, trained on the exact chip-timing tables (scripts/chip_timing_tables.py).

Wes (2026-10-11): "build a smaller policy model (without the 4B LLM) to make decisions faster". This is that
test: a ~2k-parameter network sees each week's observation (forecast captain/bench outlook for 5 weeks,
priced free hit / wildcard options, chips left, weeks left, double/blank gameweek sizes up to 6 weeks
ahead) and picks this week's chip. The return is the whole half-season, so a chip saved for a double
gameweek is paid for by the weeks that follow, with no guessed value for held chips. One rollout is a
table walk, so training takes seconds and the question "is there anything to win in chip timing?" is
answered with every season held out in turn (leave-one-season-out), not two halves.

usage: train_tiny_chip_policy.py [--updates 400] [--rollouts 64] [--seed 0]
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parents[1]
import os
TABLES = ROOT / "reports" / os.environ.get("FPL_CHIP_TABLES_DIR", "chip_timing")
ACTIONS = ["none", "triple_captain", "bench_boost", "free_hit", "wildcard"]
HELD_OUT = ["2025-26:2", "2023-24:2"]  # the G7b / G8 comparison halves


class Half:
    def __init__(self, path: Path):
        d = json.load(open(path))
        self.name = f"{d['season']}:{d['half']}"
        self.weeks = d["weeks"]
        self.traj = {(t["wc"], t["fh"]): t["weeks"] for t in d["trajectories"]}
        self.planner = d["ceilings"]["planner"]
        self.ceiling = d["ceilings"]["hindsight_all_chips"]

    def selectable(self, action, week, wc, fh):
        """A wildcard / free hit whose trajectory failed to build is off the table."""
        if action == "wildcard":
            return (week, fh) in self.traj
        if action == "free_hit":
            return (wc, week) in self.traj
        return True

    def features(self, rec, i, held, history=()):
        n = len(self.weeks)
        cap, bench = rec["cap_outlook"], rec["bench_outlook"]
        later_cap, later_bench = max(cap[1:]), max(bench[1:])
        # v2: squad health + how the squad has actually been scoring (its own past weeks, known at i)
        recent = [h["realized"] for h in history[-3:]]
        health = [rec.get("squad_papp_mean", 0.9), rec.get("squad_flagged", 0) / 5, rec.get("squad_p1_sum", 60) / 80, rec.get("squad_p5_sum", 300) / 400,
                  (np.mean(recent) / 60 if recent else 0.0), (np.mean(recent) - rec.get("squad_p1_sum", 60)) / 20 if recent else 0.0]
        return np.array([i / n, (n - i) / n, *[float(a in held) for a in ACTIONS[1:]], rec["bank"] / 5, rec["free_transfers"] / 5, *health,
                         *[c / 10 for c in cap], *[b / 10 for b in bench], (cap[0] - later_cap) / 5, (bench[0] - later_bench) / 5,
                         rec["xi_proj"] / 60, rec["fh_gain_proj"] / 20, rec["wc_gain_proj"] / 20,
                         rec["squad_double"] / 15, rec["squad_blank"] / 15, *rec["league_double"], *rec["league_blank"]], dtype=np.float32)

    def play(self, policy, greedy=False, rng=None, batch=1):
        """`batch` half-seasons in lockstep (one network call per week); returns totals, chip weeks and
        the (features, action, mask) arrays for the policy gradient."""
        held = [set(ACTIONS[1:]) for _ in range(batch)]
        wc, fh = [None] * batch, [None] * batch
        totals, used = np.zeros(batch), [[] for _ in range(batch)]
        X, A, M = [], [], []
        for i, week in enumerate(self.weeks):
            x = np.stack([self.features(self.traj[(wc[b], fh[b])][i], i, held[b], self.traj[(wc[b], fh[b])][:i]) for b in range(batch)])
            mask = np.array([[True] + [a in held[b] and self.selectable(a, week, wc[b], fh[b]) for a in ACTIONS[1:]] for b in range(batch)])
            acts = policy(x, mask, greedy, rng)
            for b, a in enumerate(acts):
                action = ACTIONS[a]
                if action == "wildcard":
                    wc[b] = week
                elif action == "free_hit":
                    fh[b] = week
                rec = self.traj[(wc[b], fh[b])][i]  # the WC/FH trajectory from this week on
                reward = rec["realized"]
                if action == "triple_captain":
                    reward += rec["captain_points"]
                elif action == "bench_boost":
                    reward += rec["bench_extra"]
                if action != "none":
                    held[b].discard(action); used[b].append((week, action))
                totals[b] += reward
            X.append(x); A.append(np.array(acts)); M.append(mask)
        return totals, used, (np.concatenate(X), np.concatenate(A), np.concatenate(M))


N_FEAT = 2 + 4 + 2 + 6 + 5 + 5 + 2 + 3 + 2 + 7 + 7


class Policy(torch.nn.Module):
    def __init__(self, hidden=32):
        super().__init__()
        self.net = torch.nn.Sequential(torch.nn.Linear(N_FEAT, hidden), torch.nn.Tanh(), torch.nn.Linear(hidden, len(ACTIONS)))
        torch.nn.init.zeros_(self.net[-1].weight); torch.nn.init.zeros_(self.net[-1].bias)

    def logits(self, x, mask):
        out = self.net(x)
        return out.masked_fill(~mask, -1e9)

    def act(self, x, mask, greedy, rng):
        with torch.no_grad():
            logit = self.logits(torch.from_numpy(x), torch.from_numpy(mask))
        if greedy:
            return logit.argmax(-1).tolist()
        p = torch.softmax(logit, -1).numpy()
        return [int(rng.choice(len(ACTIONS), p=row / row.sum())) for row in p]


def train(halves, updates, rollouts, seed, lr=0.01, entropy=0.01):
    torch.manual_seed(seed); rng = np.random.default_rng(seed)
    pol = Policy(); opt = torch.optim.Adam(pol.parameters(), lr=lr)
    for _ in range(updates):
        opt.zero_grad()
        for h in halves:
            returns, _, (X, A, M) = h.play(pol.act, False, rng, batch=rollouts)
            adv = (returns - returns.mean()) / (returns.std() + 1e-6)
            X, A, M = torch.from_numpy(X), torch.from_numpy(A), torch.from_numpy(M)
            W = torch.tensor(np.tile(adv, len(h.weeks)), dtype=torch.float32)  # week-major, like X
            logp = torch.log_softmax(pol.logits(X, M), -1)
            ent = -(logp.exp() * logp.masked_fill(~M, 0)).sum(-1).mean()
            loss = -(W * logp.gather(1, A[:, None])[:, 0]).mean() / len(halves) - entropy * ent / len(halves)
            loss.backward()
        opt.step()
    return pol


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--updates", type=int, default=300)
    ap.add_argument("--rollouts", type=int, default=64)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    halves = {h.name: h for h in (Half(p) for p in sorted(TABLES.glob("*_h*.json")))}
    seasons = sorted({n.split(":")[0] for n in halves})
    lines = ["# Tiny chip policy vs planner (whole-half returns, chips only, forecast captain)", "",
             f"{len(halves)} half-seasons; policy = {sum(p.numel() for p in Policy().parameters())} parameters; "
             f"{args.updates} updates x {args.rollouts} rollouts per half; greedy play at test time.", "",
             "| Held-out half | Planner | Tiny policy | vs planner | Hindsight ceiling | Policy chips |", "|---|---|---|---|---|---|"]
    tot = {"planner": 0.0, "policy": 0.0, "ceiling": 0.0}
    # leave-one-season-out: every season scored by a policy that never saw it
    for season in seasons:
        train_halves = [h for n, h in halves.items() if not n.startswith(season)]
        pol = train(train_halves, args.updates, args.rollouts, args.seed)
        for n, h in halves.items():
            if n.startswith(season):
                total, used = (lambda r: (r[0][0], r[1][0]))(h.play(pol.act, greedy=True))
                tot["planner"] += h.planner; tot["policy"] += total; tot["ceiling"] += h.ceiling
                lines.append(f"| {n} | {h.planner:.0f} | {total:.0f} | {total - h.planner:+.0f} | {h.ceiling:.0f} | {used} |")
                print(lines[-1], flush=True)
    lines.append(f"| **total** | {tot['planner']:.0f} | {tot['policy']:.0f} | {tot['policy'] - tot['planner']:+.0f} | {tot['ceiling']:.0f} | |")
    # the G7b/G8 split, for the like-for-like comparison with the LLM policies
    pol = train([h for n, h in halves.items() if n not in HELD_OUT], args.updates, args.rollouts, args.seed)
    g = [(n, (lambda r: (r[0][0], r[1][0]))(halves[n].play(pol.act, greedy=True))) for n in HELD_OUT if n in halves]
    held = sum(r[0] for _, r in g); plan = sum(halves[n].planner for n, _ in g)
    lines += ["", f"G7b/G8 split (train on the other {len(halves) - len(g)} halves): held-out {held:.0f} vs planner {plan:.0f} ({held - plan:+.0f}); "
              + "; ".join(f"{n}: {r[0]:.0f} chips {r[1]}" for n, r in g)]
    torch.save(pol.state_dict(), TABLES / "tiny_policy_g7b_split.pt")
    (TABLES / "tiny_policy.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines[-2:]))


if __name__ == "__main__":
    main()

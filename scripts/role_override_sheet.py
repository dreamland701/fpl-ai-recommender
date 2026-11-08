#!/usr/bin/env python3
"""Role-override sheet (2026-10-21, the Konsa case).

The classic model's form windows carry a new signing's bedding-in weeks for eight gameweeks (Konsa: 0 and 11
minutes in GW1-2, then five 90s -> eight-week minutes average 66, forecast 73 minutes / 3.2 points). The population
he then resembles (three straight starts, eight-week minutes average 55-75) really does play about 70 minutes the
next week, so the ridge is right about the population and nothing structured (new-signing flag, positional rival
unavailable) separates "new signing, now nailed" from "rotation player on a streak"; the adapters' reads never
singled him out either. That separation is a judgment call, so this sheet makes it with the model's own
arithmetic: chosen squad players are re-forecast as if their history at the club started at the first start of
their current run (`--override NAME:SINCE_GW`, or `--auto` for every squad player in the cell: started each of the
last three weeks, eight-week minutes average under --max-minutes-8, status a), and the XI is shown under the
standard and the overridden forecasts. Nothing else changes: same fitted model, same snapshot, same squad.

usage: PACKET_DIR=<dir with snapshot/> PYTHONPATH=src FPL_PER_FIXTURE=1 FPL_PER_FIXTURE_HORIZON=0 \\
       FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 python3 scripts/role_override_sheet.py \\
         --table data/fpl_training_rows_v3_contract_f6.csv --entry-state <entry_state.json> --asof-week 8 \\
         [--transfer OUT:IN]... [--override NAME:SINCE_GW]... [--auto] --out-md <md> [--out-jsonl <forecasts.jsonl>]
The jsonl has the packet forecast record shape, so decide/milp_routes/route_lineups can be re-run on it.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
import warnings
from pathlib import Path

import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PRIOR_BLEND", "1")
os.environ.setdefault("FPL_OPPONENT_INTERACTION", "1")

from fpl_ai.api import OfficialSnapshotService  # noqa: E402
from fpl_ai.dataset import CanonicalDataset, training_rows_asof  # noqa: E402
from fpl_ai.decision import _optimize_lineup  # noqa: E402
from fpl_ai.models import fit_model_suite_from_frame  # noqa: E402
from fpl_ai.types import SquadPlayer  # noqa: E402

POS_ORDER = {"GK": 0, "GKP": 0, "DEF": 1, "MID": 2, "FWD": 3}


class FrozenClient:
    def __init__(self, snap: Path) -> None:
        self.snap = snap

    def bootstrap_static(self):
        return json.loads((self.snap / "bootstrap_static.json").read_text())

    def fixtures(self):
        return json.loads((self.snap / "fixtures.json").read_text())


def gw_column(frame: pd.DataFrame) -> str:
    return next(c for c in ("round", "GW", "gw", "event") if c in frame.columns)


def trailing_start_run(rows: pd.DataFrame, gwcol: str) -> tuple[int | None, int]:
    """(first week, length) of the trailing run of starts in one player's live-season rows."""
    since, length = None, 0
    for _, r in rows.sort_values(gwcol)[::-1].iterrows():
        if float(r.get("starts", 0) or 0) >= 1:
            since, length = int(r[gwcol]), length + 1
        else:
            break
    return since, length


def build_override_history(history_root: Path, season: str, overrides: dict[int, int], workdir: Path,
                           drops: dict[int, set[int]] | None = None) -> Path:
    """A history root where each overridden player's live-season rows before SINCE_GW are removed, and each dropped
    (player, week) row is removed (2026-10-28, the Isak case: a returner's injury blank read as rotation)."""
    root = workdir / "fpl_history"
    if root.exists():
        shutil.rmtree(root)
    root.mkdir(parents=True)
    for child in history_root.iterdir():
        if child.name == season:
            (root / season).mkdir()
            for f in child.iterdir():
                if f.name != "merged_gw.csv" and f.is_file():
                    shutil.copy(f, root / season / f.name)
        else:
            (root / child.name).symlink_to(child.resolve())
    g = pd.read_csv(history_root / season / "merged_gw.csv", low_memory=False)
    gwcol = gw_column(g)
    drop = pd.Series(False, index=g.index)
    for pid, since in overrides.items():
        drop |= (g["element"] == pid) & (g[gwcol] < since)
    for pid, weeks in (drops or {}).items():
        drop |= (g["element"] == pid) & (g[gwcol].isin(sorted(weeks)))
    g[~drop].to_csv(root / season / "merged_gw.csv", index=False)
    return root


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--packet-dir", default=os.environ.get("PACKET_DIR"), help="directory holding snapshot/")
    ap.add_argument("--table", required=True)
    ap.add_argument("--entry-state", required=True)
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--asof-week", type=int, required=True, help="the gameweek being forecast")
    ap.add_argument("--history-root", default="data/fpl_history")
    ap.add_argument("--transfer", action="append", default=[], help="OUT_NAME:IN_NAME, applied before the XI is picked")
    ap.add_argument("--override", action="append", default=[], help="NAME:SINCE_GW, restart the player's history there")
    ap.add_argument("--drop", action="append", default=[], help="NAME:GW, remove that live-season week from the player's history (a returner's injury blank)")
    ap.add_argument("--auto", action="store_true", help="override every squad player in the Konsa cell")
    ap.add_argument("--max-minutes-8", type=float, default=75.0)
    ap.add_argument("--out-md", required=True)
    ap.add_argument("--out-jsonl")
    ap.add_argument("--workdir", help="scratch dir for the override history (default: <packet-dir>/_role_override_work)")
    args = ap.parse_args()
    if not args.packet_dir:
        sys.exit("--packet-dir or PACKET_DIR is required")
    packet = Path(args.packet_dir)
    snap = packet / "snapshot"
    deadline = json.loads((snap / "manifest.json").read_text())["deadline_time"]

    dataset = CanonicalDataset.from_csv(args.table)
    train_frame = training_rows_asof(dataset.training_frame, args.season, args.asof_week)
    suite = fit_model_suite_from_frame(train_frame=train_frame, feature_names=dataset.feature_columns)
    official = OfficialSnapshotService(client=FrozenClient(snap)).build_current_week_frame(deadline)
    official_by_id = official.set_index("player_id")
    live = dataset.build_live_week_frame(official, history_root=args.history_root)
    live_by_id = live.set_index("player_id")
    base = {f.player_id: f for f in suite.predict_frame(live)}
    by_name = {f.player_name: pid for pid, f in base.items()}

    state = json.loads(Path(args.entry_state).read_text())
    sell = {int(s["player_id"]): float(s["selling_price"]) for s in state["squad"]}
    for move in args.transfer:
        out_name, in_name = move.split(":")
        sell.pop(by_name[out_name])
        sell[by_name[in_name]] = 0.0

    hist = pd.read_csv(Path(args.history_root) / args.season / "merged_gw.csv", low_memory=False)
    gwcol = gw_column(hist)
    overrides: dict[int, int] = {}
    reasons: dict[int, str] = {}
    for item in args.override:
        name, since = item.split(":")
        overrides[by_name[name]] = int(since)
        reasons[by_name[name]] = "manual"
    drops: dict[int, set[int]] = {}
    for item in args.drop:
        name, gw = item.split(":")
        drops.setdefault(by_name[name], set()).add(int(gw))
        overrides.setdefault(by_name[name], 0)
        reasons[by_name[name]] = f"manual: GW{gw} row removed (injury blank, not rotation)"
    if args.auto:
        for pid in sell:
            if pid in overrides or pid not in live_by_id.index:
                continue
            row = live_by_id.loc[pid]
            if str(official_by_id.loc[pid].get("status", "a")) != "a":
                continue
            if float(row.get("starts_avg_3", 0) or 0) < 0.999 or float(row.get("minutes_avg_8", 90) or 90) >= args.max_minutes_8:
                continue
            since, length = trailing_start_run(hist[hist["element"] == pid], gwcol)
            if since is None or since <= 1 or length < 3:
                continue
            overrides[pid] = since
            reasons[pid] = f"auto: {length} straight starts since GW{since}, 8-week minutes avg {float(row['minutes_avg_8']):.0f}"

    if overrides:
        workdir = Path(args.workdir) if args.workdir else packet / "_role_override_work"
        root = build_override_history(Path(args.history_root), args.season, overrides, workdir, drops)
        live_ov = dataset.build_live_week_frame(official, history_root=str(root))
        ov = {f.player_id: f for f in suite.predict_frame(live_ov)}
        live_ov_by_id = live_ov.set_index("player_id")
        shutil.rmtree(workdir, ignore_errors=True)
    else:
        ov, live_ov_by_id = dict(base), live_by_id

    squad = [SquadPlayer(pid, base[pid].player_name, base[pid].team_id, base[pid].position, price) for pid, price in sell.items()]
    picks = {}
    for side, fc in (("standard", base), ("override", ov)):
        xi, bench, cap, vice, _ = _optimize_lineup(squad, fc)
        total = sum(fc[i].predicted_points_1gw for i in xi) + fc[cap].predicted_points_1gw
        picks[side] = {"xi": xi, "bench": bench, "cap": cap, "vice": vice, "total": total}

    def names(ids, fc, sort=True):
        ids = sorted(ids, key=lambda i: (POS_ORDER.get(fc[i].position, 9), -fc[i].predicted_points_1gw)) if sort else list(ids)
        return ", ".join(fc[i].player_name for i in ids)

    week = int(live_by_id.loc[next(iter(sell))]["week"]) if "week" in live.columns else args.asof_week
    lines = [f"# Role override sheet, GW{week}", "",
             f"Planned moves applied: {', '.join(args.transfer) or 'none'}. Same fitted classic model, same snapshot; the only "
             "change is that the players below are re-forecast as if their history at the club began at the first start of "
             "their current run, i.e. as nailed starters. Whether they really are nailed is the manager's call; this shows "
             "what the call is worth in the model's own numbers.", ""]
    if overrides:
        lines += ["## Players re-forecast as nailed", "",
                  "| Player | Why | Standard: GW / 3GW / 5GW, mins, P(app) | If nailed: GW / 3GW / 5GW, mins, P(app) |",
                  "|---|---|---|---|"]
        for pid, since in overrides.items():
            b, o = base[pid], ov[pid]
            lines.append(f"| **{b.player_name}** | {reasons[pid]}{f' (history restarted at GW{since})' if since else ''} | "
                         f"{b.predicted_points_1gw:.2f} / {b.predicted_points_3gw:.2f} / {b.predicted_points_5gw:.2f}, "
                         f"{b.predicted_minutes:.0f} min, {b.appearance_probability:.2f} | "
                         f"{o.predicted_points_1gw:.2f} / {o.predicted_points_3gw:.2f} / {o.predicted_points_5gw:.2f}, "
                         f"{o.predicted_minutes:.0f} min, {o.appearance_probability:.2f} |")
    else:
        lines += ["No squad player is in the cell this week (no override applied).", ""]
    s, o = picks["standard"], picks["override"]
    lines += ["", "## Lineups", "", "| | Standard | If nailed |", "|---|---|---|",
              f"| XI | {names(s['xi'], base)} | {names(o['xi'], ov)} |",
              f"| Bench (in order) | {names(s['bench'], base, sort=False)} | {names(o['bench'], ov, sort=False)} |",
              f"| Captain / vice | {base[s['cap']].player_name} / {base[s['vice']].player_name} | {ov[o['cap']].player_name} / {ov[o['vice']].player_name} |",
              f"| Expected GW points (incl. captain, own forecasts) | {s['total']:.1f} | {o['total']:.1f} |", ""]
    only_o = [ov[i].player_name for i in o["xi"] if i not in s["xi"]]
    only_s = [base[i].player_name for i in s["xi"] if i not in o["xi"]]
    lines.append("XI differences: " + (", ".join(f"{n} (if nailed only)" for n in only_o) + (", " if only_o and only_s else "")
                                        + ", ".join(f"{n} (standard only)" for n in only_s) if (only_o or only_s) else "none"))
    lines += ["", "## Every squad player", "", "| Player | Pos | GW standard | GW if nailed | 5GW standard | 5GW if nailed | P(app) standard → if nailed |",
              "|---|---|---|---|---|---|---|"]
    for pid in sorted(sell, key=lambda i: (POS_ORDER.get(base[i].position, 9), -base[i].predicted_points_1gw)):
        b, v = base[pid], ov[pid]
        mark = "**" if pid in overrides else ""
        lines.append(f"| {mark}{b.player_name}{mark} | {b.position} | {b.predicted_points_1gw:.2f} | {v.predicted_points_1gw:.2f} | "
                     f"{b.predicted_points_5gw:.2f} | {v.predicted_points_5gw:.2f} | {b.appearance_probability:.2f} → {v.appearance_probability:.2f} |")
    Path(args.out_md).write_text("\n".join(lines) + "\n")
    print(f"overrides: {[(base[p].player_name, g) for p, g in overrides.items()]}; standard {s['total']:.1f} vs if-nailed {o['total']:.1f} -> {args.out_md}")

    if args.out_jsonl:
        with open(args.out_jsonl, "w") as handle:
            for pid, f in ov.items():
                oj = official_by_id.loc[pid]
                row = live_ov_by_id.loc[pid] if pid in live_ov_by_id.index else {}
                handle.write(json.dumps({
                    "player_id": int(pid), "name": f.player_name, "team_id": int(f.team_id), "pos": f.position,
                    "price": float(oj.get("price") or 0), "own": float(oj.get("selected_by_percent") or 0),
                    "status": str(oj.get("status") or "a"), "news": str(oj.get("news") or ""),
                    "p1": round(f.predicted_points_1gw, 3), "p3": round(f.predicted_points_3gw, 3),
                    "p5": round(f.predicted_points_5gw, 3), "mins": round(f.predicted_minutes, 1),
                    "papp": round(f.appearance_probability, 3), "unc": round(f.uncertainty, 3),
                    "fixtures": int(f.fixture_count),
                    "feat_selected_pct": float(row.get("selected_by_percent_pre_deadline", 0) or 0),
                    "feat_selected_change": float(row.get("selected_change_1", 0) or 0),
                    "feat_points_avg_3": float(row.get("points_avg_3", 0) or 0),
                    "role_override_since_gw": overrides.get(pid),
                }, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""G4 gate 1: decision value of an adapter's deltas on held-out week-states.

For each state in the eval cache, decode the adapter on the decision-
relevant players (prompts from the E11 split; eval.jsonl covers GW35-38,
train.jsonl covers GW30-34 — E11 saw those labels in SFT, so GW35-38 is
the cleaner sub-window), apply ALL deltas at once (deployment semantics),
run the deterministic decision, score realized points. Compare adapters.

  python3 scripts/run_g4_decision_eval.py --model-path artifacts/gemma4_e4b_merged_e11_defcon \
     --adapter-path artifacts/gemma4_e4b_g4_forecast_v1 --tag g4 \
     --states reports/grpo_states/2025-26-late.jsonl
  (run once with no --adapter-path and --tag e11 for the reference line:
   merged model == E11)
"""
from __future__ import annotations

import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_forecast_env import ForecastRewardEnv, parse_delta_completion, realized_points_for_forecasts  # noqa: E402
from fpl_ai.llm_adjust import apply_llm_deltas  # noqa: E402

SPLIT = ROOT / "reports" / "llm_residual_v2_e11_defcon_top256_thru_2526_34_eval_2526_35_38"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--model-path", required=True)
    p.add_argument("--adapter-path")
    p.add_argument("--tag", required=True)
    p.add_argument("--states", default=str(ROOT / "reports/grpo_states/2025-26-late.jsonl"))
    p.add_argument("--skip-decode", action="store_true")
    p.add_argument("--predictions-from", nargs=2, metavar=("EXAMPLES", "PREDICTIONS"),
                   help="Reuse an existing decode (examples + predictions JSONL) keyed by (week, player_id) instead of decoding; states without coverage are skipped.")
    a = p.parse_args()

    prompts = {}
    for name in ("train.jsonl", "eval.jsonl"):
        for line in open(SPLIT / name):
            row = json.loads(line); md = row["metadata"]
            prompts[(md["season"], int(md["week"]), int(md["player_id"]))] = row["prompt"]

    states = load_states(a.states)
    envs = [ForecastRewardEnv(s) for s in states]
    examples_path = ROOT / f"reports/g4_eval_examples_{a.tag}.jsonl"
    preds_path = ROOT / f"reports/g4_eval_predictions_{a.tag}.jsonl"
    rows = []
    for env in envs:
        for pid in env.relevant_players:
            pr = prompts.get((env.state.season, env.state.week, pid))
            if pr:
                rows.append({"season": env.state.season, "week": env.state.week, "prompt": pr,
                             "metadata": {"season": env.state.season, "week": env.state.week, "player_id": pid}})
    with open(examples_path, "w") as f:
        for r in rows: f.write(json.dumps(r) + "\n")
    print(f"{a.tag}: {len(rows)} prompts across {len(envs)} states")
    if a.predictions_from:
        ex_path, pr_path = a.predictions_from
        ex = [json.loads(l) for l in open(ex_path)]
        pr = [json.loads(l) for l in open(pr_path)]
        existing = {(int(e["metadata"]["week"]), int(e["metadata"]["player_id"])): p for e, p in zip(ex, pr)}
        covered_weeks = {w for (w, _) in existing}
        rows = [r for r in rows if r["metadata"]["week"] in covered_weeks]
        envs = [e for e in envs if e.state.week in covered_weeks]
        preds = [existing.get((r["metadata"]["week"], r["metadata"]["player_id"]), {"response": ""}) for r in rows]
        print(f"reusing decode: weeks {sorted(covered_weeks)} | rows with predictions {sum(1 for p in preds if p.get('response'))}/{len(rows)}")
    elif not a.skip_decode:
        cmd = [sys.executable, "-u", str(ROOT / "eval_gemma_responses.py"), "--model-path", a.model_path,
               "--examples", str(examples_path), "--output", str(preds_path), "--max-new-tokens", "96",
               "--no-4bit", "--batch-size", "8", "--resume"]
        if a.adapter_path: cmd += ["--adapter-path", a.adapter_path]
        subprocess.run(cmd, check=True)
        preds = [json.loads(l) for l in open(preds_path)]
    else:
        preds = [json.loads(l) for l in open(preds_path)]
    deltas_by_state: dict = {}
    strict = 0
    for r, pr in zip(rows, preds):
        md = r["metadata"]
        d = parse_delta_completion(pr.get("response") or pr.get("completion") or "")
        if d is None: continue
        strict += 1
        deltas_by_state.setdefault(md["week"], {})[(md["week"], md["player_id"])] = d
    out = []
    for env in envs:
        lookup = deltas_by_state.get(env.state.week, {})
        adjusted = apply_llm_deltas(env.state.forecasts, lookup, env.state.week, fields="all")
        realized, detail = realized_points_for_forecasts(env.state, adjusted)
        out.append({"week": env.state.week, "classic": env.classic_realized, a.tag: realized, "transfer": detail["transfer"]})
        print(f"GW{env.state.week}: classic {env.classic_realized:.0f} | {a.tag} {realized:.0f} ({realized - env.classic_realized:+.0f})")
    total = sum(o[a.tag] for o in out); base = sum(o["classic"] for o in out)
    print(f"TOTAL {a.tag} {total:.0f} vs classic {base:.0f} ({total - base:+.0f}) | strict {strict}/{len(rows)}")
    json.dump(out, open(ROOT / f"reports/g4_decision_eval_{a.tag}.json", "w"), indent=2)


if __name__ == "__main__":
    main()

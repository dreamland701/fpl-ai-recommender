#!/usr/bin/env python3
"""Evaluate a GRPO decision adapter on the held-out 2025-26 GW12-30 states.

For each weekly state: build the decision prompt, greedy-decode one action,
roll it through the deterministic optimizer against realized outcomes, and
compare season-total realized points vs the classic default action on the
same states (paired, per-week).

Note: the env's realized score (starters + effective captain − hit) excludes
autosubs and chips, so totals here are not directly comparable to the full
backtest's 1,058 gate — the paired delta vs the default action on identical
states is the decision-quality metric.

Usage (GPU):
  python3 scripts/run_grpo_decision_eval.py \
    --adapter-path artifacts/gemma4_e4b_grpo_decision_v1 \
    --output reports/grpo_decision_eval_2526.json

CPU smoke test (no model; default + availability-soft canned actions):
  python3 scripts/run_grpo_decision_eval.py --mock --output /tmp/mock.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.grpo_env import WeeklyBanditEnv, load_states, parse_action  # noqa: E402

EVAL_STATES = "reports/grpo_states/2025-26.jsonl"


def generate_responses(prompts: list[str], model_path: str, adapter_path: str | None) -> list[str]:
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.padding_side = "left"
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto")
    if adapter_path:
        from peft import PeftModel

        model = PeftModel.from_pretrained(model, adapter_path)
    model.eval()
    responses = []
    for prompt in prompts:
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=96, do_sample=False)
        responses.append(tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
    return responses


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--states", default=EVAL_STATES)
    parser.add_argument("--model-path", default="google/gemma-4-E4B-it")
    parser.add_argument("--adapter-path")
    parser.add_argument("--output", required=True)
    parser.add_argument("--mock", action="store_true", help="CPU smoke test with a canned action, no model.")
    args = parser.parse_args()

    states = load_states(args.states)
    envs = [WeeklyBanditEnv(state) for state in states]
    prompts = [env.state_prompt(top_n_candidates=24) for env in envs]

    if args.mock:
        responses = ['{"availability": "soft", "soft_knee": 0.8}'] * len(prompts)
    else:
        responses = generate_responses(prompts, args.model_path, args.adapter_path)

    weeks = []
    policy_total = 0.0
    baseline_total = 0.0
    unparseable = 0
    wins = losses = ties = 0
    for env, response in zip(envs, responses):
        baseline = env.baseline_realized()
        action = parse_action(response)
        if action is None:
            unparseable += 1
            realized, detail = baseline, {"note": "unparseable -> baseline"}
        else:
            realized, detail = env._realized_for_action(action)
        delta = realized - baseline
        wins += delta > 0
        losses += delta < 0
        ties += delta == 0
        policy_total += realized
        baseline_total += baseline
        weeks.append(
            {
                "week": env.state.week,
                "baseline": baseline,
                "policy": realized,
                "delta": delta,
                "response": response[:200],
                "detail": {k: v for k, v in detail.items() if k != "note"} if action else detail,
            }
        )

    summary = {
        "states": len(states),
        "policy_total": policy_total,
        "baseline_total": baseline_total,
        "delta_total": policy_total - baseline_total,
        "delta_per_week": round((policy_total - baseline_total) / max(len(states), 1), 2),
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "unparseable": unparseable,
        "weeks": weeks,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(summary, indent=2))
    print(
        f"policy {policy_total:.0f} vs baseline {baseline_total:.0f} "
        f"({policy_total - baseline_total:+.0f}; {wins}W/{losses}L/{ties}T; {unparseable} unparseable)"
    )
    print(f"written -> {args.output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Evaluate a G2 plan adapter on held-out 2025-26 GW12-30 episodes.

For each non-overlapping 6-week episode: build the plan prompt,
greedy-decode one K-week plan, roll it through the chained weekly states
(squad/bank/FTs evolving under the plan, chips scored), and compare
cumulative realized points vs the all-defaults sequential baseline on the
same window (paired).

Run twice for the composed-stack comparison:
  --states reports/grpo_states/2025-26.jsonl           (classic forecasts)
  --states reports/grpo_states_adjusted/2025-26.jsonl  (E7-adjusted + deltas
                                                        + scout snippets)

Note: env scoring excludes autosubs, so totals are not comparable to the
1,058 backtest gate — the paired per-window delta is the metric.

Usage (GPU):
  python3 scripts/run_grpo_plan_eval.py \
    --adapter-path artifacts/gemma4_e4b_grpo_plan_v1 \
    --states reports/grpo_states_adjusted/2025-26.jsonl \
    --output reports/grpo_plan_eval_2526_adjusted.json

CPU smoke test:  python3 scripts/run_grpo_plan_eval.py --mock --output /tmp/mock.json
"""

from __future__ import annotations

import argparse
import os
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env import CHIPS, build_episodes, parse_plan  # noqa: E402

EVAL_STATES = "reports/grpo_states/2025-26.jsonl"


def load_generator(model_path: str, adapter_path: str | None, base_adapter: str | None = None, chat_template: bool = False):
    """Load tokenizer+model once; returns a generate_one(prompt, min_new_tokens) closure.

    Sequential per-prompt generation (not batched) is required here because
    each window's prompt depends on the season-level chip budget remaining
    after the *previous* window's response was rolled out — see main()'s
    per-episode loop. Decode cost for a handful of windows is trivial next
    to a training run, so batching is not worth the added complexity.
    """
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.padding_side = "left"
    # FPL_GEN_DEVICE_MAP=gpu loads everything on the GPU: on the GB10's unified memory, "auto" can misjudge
    # free memory while another job trains and offload layers to the CPU, which makes generation crawl.
    device_map = {"": 0} if os.environ.get("FPL_GEN_DEVICE_MAP") == "gpu" else "auto"
    kwargs = {}
    if os.environ.get("FPL_GEN_4BIT") == "1":  # needed for the 31B: bf16 load exceeds the GB10's unified memory
        from transformers import BitsAndBytesConfig
        kwargs["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                                           bnb_4bit_compute_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map=device_map, **kwargs)
    if base_adapter:
        # v2b stacking: the GRPO adapter was trained on base+SFT-merged
        # weights, so merge the SFT adapter first, then load the policy.
        from peft import PeftModel

        model = PeftModel.from_pretrained(model, base_adapter).merge_and_unload()
    if adapter_path:
        from peft import PeftModel

        # target_parameters LoRA re-registers a parametrization on every wrapped weight per forward
        # call (~1.4 s on the GB10); merged decoding is identical and ~9x faster (2026-10-09).
        model = PeftModel.from_pretrained(model, adapter_path).merge_and_unload()
    model.eval()

    def generate_one(prompt: str, min_new_tokens: int = 0) -> str:
        if chat_template:  # G5 trains on chat-templated prompts; G2/G3 on raw text
            prompt = tokenizer.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False,
                                                   add_generation_prompt=True)
        inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=not chat_template).to(model.device)
        with torch.no_grad():
            output = model.generate(
                **inputs, max_new_tokens=512, do_sample=False, min_new_tokens=min_new_tokens or None
            )
        return tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)

    return generate_one


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--states", default=EVAL_STATES)
    parser.add_argument("--model-path", default="google/gemma-4-E4B-it")
    parser.add_argument("--adapter-path")
    parser.add_argument("--horizon", type=int, default=6)
    parser.add_argument("--output", required=True)
    parser.add_argument("--mock", action="store_true", help="CPU smoke test with a canned plan, no model.")
    parser.add_argument(
        "--base-adapter",
        help="Merge this SFT adapter into the base before loading "
        "--adapter-path (for v2b policies trained on merged weights).",
    )
    parser.add_argument(
        "--min-new-tokens", type=int, default=0,
        help="Block the policy's immediate-EOS mode at decode (GRPO left an "
        "empty-completion attractor; all-empty groups get zero advantage so "
        "training never penalized it). 8 is the deployment setting.",
    )
    args = parser.parse_args()

    states = load_states(args.states)
    episodes = build_episodes(states, horizon=args.horizon, stride=args.horizon)

    if args.mock:
        canned = json.dumps([{"availability": "soft"}] + [{} for _ in range(args.horizon - 1)])
        generate_one = lambda prompt, min_new_tokens=0: canned  # noqa: E731
    else:
        generate_one = load_generator(args.model_path, args.adapter_path, base_adapter=args.base_adapter)

    # Season-level chip budget, per half (1 = GW<=19, 2 = GW>=20 — each chip
    # has one independent copy per half, the second renewing at GW20
    # regardless of first-half usage). Episodes come back grouped by season,
    # in window order within each season (build_episodes' by-season dict +
    # ascending start). A chip played in an earlier window of the same half
    # is illegal in a later window of that SAME half — carry the remaining
    # per-half budget forward sequentially instead of letting every window
    # start with a fresh bench_boost/triple_captain (the bug this fix
    # addresses), while still renewing correctly at the GW20 boundary.
    remaining_chips: dict[str, dict[int, frozenset]] = {}

    windows = []
    policy_total = 0.0
    baseline_total = 0.0
    unparseable = 0
    wins = losses = ties = 0
    for env in episodes:
        season = env.states[0].season
        env.available_chips = remaining_chips.get(season, {1: frozenset(CHIPS), 2: frozenset(CHIPS)})
        prompt = env.state_prompt()
        response = generate_one(prompt, args.min_new_tokens)

        baseline = env.baseline_total()
        plan = parse_plan(response, env.horizon)
        if plan is None:
            unparseable += 1
            realized, details = baseline, [{"note": "unparseable -> baseline"}]
        else:
            realized, details = env.rollout(plan)
        remaining_chips[season] = {
            1: env.available_chips[1] - env.chips_used_in_rollout[1],
            2: env.available_chips[2] - env.chips_used_in_rollout[2],
        }

        delta = realized - baseline
        wins += delta > 0
        losses += delta < 0
        ties += delta == 0
        policy_total += realized
        baseline_total += baseline
        windows.append(
            {
                "start_week": env.states[0].week,
                "weeks": [state.week for state in env.states],
                "baseline": baseline,
                "policy": realized,
                "delta": delta,
                "chips": [d.get("chip") for d in details if isinstance(d, dict) and d.get("chip") not in (None, "none")],
                "chips_available_this_window": {
                    "half1_gw1_19": sorted(env.available_chips[1]),
                    "half2_gw20_38": sorted(env.available_chips[2]),
                },
                "response": response[:400],
            }
        )

    summary = {
        "states_file": args.states,
        "min_new_tokens": args.min_new_tokens,
        "episodes": len(episodes),
        "horizon": args.horizon,
        "policy_total": policy_total,
        "baseline_total": baseline_total,
        "delta_total": policy_total - baseline_total,
        "delta_per_window": round((policy_total - baseline_total) / max(len(episodes), 1), 2),
        "wins": wins,
        "losses": losses,
        "ties": ties,
        "unparseable": unparseable,
        "windows": windows,
    }
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(summary, indent=2))
    print(
        f"policy {policy_total:.0f} vs baseline {baseline_total:.0f} "
        f"({policy_total - baseline_total:+.0f} over {len(episodes)} windows; "
        f"{wins}W/{losses}L/{ties}T; {unparseable} unparseable)"
    )
    print(f"written -> {args.output}")


if __name__ == "__main__":
    main()

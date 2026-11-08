#!/usr/bin/env python3
"""G6 imitation data: the same-chips planner's plan as the target for each G5 training window.

G5's untrained policy starts 17 points behind the planner over the 2025-26 holdout, and GRPO from
there never moved (take 3: trained = untrained). G6 first imitates the planner, so RL starts at
planner level and only has to find improvements (WC/FH timing, captains, holds), the usual
imitation-then-RL recipe. Prompts are the exact chat-templated text GRPO sees; each window appears
once per chip budget (all four, TC only, BB only, none) so the plan is learned as a function of the
chips line. The completion ends with <turn|> so the policy learns to stop where GRPO stops.

usage: build_g6_imitation_data.py <out_dir>   (writes train.jsonl from the four G5 training state
       files and eval.jsonl from the 2025-26 holdout)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, PlanEnvV2  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

HORIZON = 5
BUDGETS = [frozenset(CHIPS), frozenset({"triple_captain"}), frozenset({"bench_boost"}), frozenset()]
TRAIN_KEYS = ["2022-23", "2023-24", "2024-25", "2025-26-train"]


def windows(key):
    states = sorted(load_states(ROOT / "reports" / "grpo_states_v2" / f"{key}.jsonl"), key=lambda s: s.week)
    for start in range(0, len(states) - HORIZON + 1):
        window = states[start:start + HORIZON]
        if [s.week for s in window] == list(range(window[0].week, window[0].week + HORIZON)):
            yield window


def main() -> None:
    from transformers import AutoTokenizer

    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    tok = AutoTokenizer.from_pretrained("google/gemma-4-E4B-it")
    for split, keys in (("train", TRAIN_KEYS), ("eval", ["2025-26-holdout"])):
        n = 0
        with (out / f"{split}.jsonl").open("w") as f:
            for key in keys:
                for window in windows(key):
                    for budget in BUDGETS:
                        env = PlanEnvV2(window, optimize, chips={1: budget, 2: budget})
                        plan = [{"transfer": a.transfer, "captain": a.captain, "chip": a.chip} for a in env.baseline_plan()]
                        prompt = tok.apply_chat_template([{"role": "user", "content": env.state_prompt()}], tokenize=False,
                                                         add_generation_prompt=True)
                        f.write(json.dumps({"prompt": prompt, "completion": json.dumps(plan) + "<turn|>",
                                            "metadata": {"key": key, "week": window[0].week, "chips": sorted(budget)}}) + "\n")
                        n += 1
        print(f"{split}: {n} examples -> {out / f'{split}.jsonl'}")


if __name__ == "__main__":
    main()

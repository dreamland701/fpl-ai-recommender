#!/usr/bin/env python3
"""G7: GRPO on the chip and captain advisor (src/fpl_ai/chip_advisor.py).

Each training prompt is one week's decision from a historical trajectory state: priced options,
"this week vs the coming weeks" per chip, weeks to expiry, a short reasoning, then a JSON choice of
chip, captain and transfer count. Reward = receding_value(choice) - receding_value(planner's move):
this week's action, then the same-chips planner re-planned from where it leaves you, plus held-chip
values (free hit / wildcard), so spending a chip in an ordinary week scores below keeping it.
The untrained model, zero-shot, lost to the planner by 49 points over two half-seasons by spending
free hit and wildcard every half; this teaches it from outcomes when to wait.

Held out: 2025-26 GW20-38 (trained on 2022-23, 2023-24, 2024-25 and 2025-26 GW2-19).

usage: train_gemma_grpo_chip_advisor.py [--dry-run]
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from fpl_ai.chip_advisor import options_prompt, parse_week_choice  # noqa: E402
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, FIRST_HALF_LAST_WEEK, PlanEnvV2, WeekAction, chip_half, receding_value  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402
from train_gemma_grpo_plan_v2 import UNPARSEABLE_MARGIN, merged_generation  # noqa: E402

MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", "google/gemma-4-E4B-it")
STATES_DIR = ROOT / "reports" / "grpo_states_v2"
OUTPUT_DIR = Path(os.environ.get("FPL_GRPO_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_e4b_grpo_chip_advisor_g7"))
NUM_GENERATIONS = int(os.environ.get("FPL_GRPO_NUM_GENERATIONS", "8"))
LEARNING_RATE = float(os.environ.get("FPL_GRPO_LEARNING_RATE", "5e-5"))
NUM_EPOCHS = float(os.environ.get("FPL_GRPO_NUM_EPOCHS", "2"))
TEMPERATURE = float(os.environ.get("FPL_GRPO_TEMPERATURE", "1.0"))
MAX_COMPLETION_LENGTH = int(os.environ.get("FPL_GRPO_MAX_COMPLETION_LENGTH", "256"))
MAX_PROMPT_LENGTH = int(os.environ.get("FPL_GRPO_MAX_PROMPT_LENGTH", "1536"))
# (state file, last week used): G7 trained on 2022-23..2024-25 + 2025-26 GW2-19. G7b adds 2020-21 and 2021-22
# and also holds out 2023-24 GW20-38, so two half-seasons are unseen (FPL_G7_SPLIT=g7b).
TRAIN = {"g7": [("2022-23", None), ("2023-24", None), ("2024-25", None), ("2025-26-train", FIRST_HALF_LAST_WEEK)],
         "g7b": [("2020-21", None), ("2021-22", None), ("2022-23", None), ("2023-24", FIRST_HALF_LAST_WEEK),
                 ("2024-25", None), ("2025-26-train", FIRST_HALF_LAST_WEEK)]}[os.environ.get("FPL_G7_SPLIT", "g7")]
KL_BETA = float(os.environ.get("FPL_GRPO_KL_BETA", "0.0"))
# Chip budgets per origin: everything fresh most often, scarcity otherwise (same idea as G5).
BUDGETS = [frozenset(CHIPS), frozenset({"bench_boost", "triple_captain"}), frozenset({"triple_captain"}),
           frozenset({"bench_boost"}), frozenset({"wildcard", "free_hit"}), frozenset({"free_hit"})]
BUDGET_WEIGHTS = [0.4, 0.2, 0.1, 0.1, 0.1, 0.1]


def build_envs():
    envs, facts, rows = {}, {}, []
    for key, last_week in TRAIN:
        states = sorted(load_states(STATES_DIR / f"{key}.jsonl"), key=lambda s: s.week)
        if last_week is not None:
            states = [s for s in states if s.week <= last_week]
        for i, state in enumerate(states):
            window = [state] + [s for s in states[i + 1:i + 5] if chip_half(s.week) == chip_half(state.week)]
            ekey = f"{key}:{state.week}"
            budget = random.Random(f"g7:{ekey}").choices(BUDGETS, weights=BUDGET_WEIGHTS, k=1)[0]
            env = PlanEnvV2(window, optimize, chips={1: budget, 2: budget})
            prompt, fact = options_prompt(env)
            envs[ekey], facts[ekey] = env, fact
            rows.append({"prompt": [{"role": "user", "content": prompt}], "state_key": ekey})
    return envs, facts, rows


def make_reward_func(envs, facts):
    values = json.loads((STATES_DIR / "chip_values.json").read_text())
    chip_values = {c: float(values[c]) for c in ("free_hit", "wildcard")}
    cache, base = {}, {}

    def value(key, action):
        if key not in base:
            base[key] = receding_value(envs[key], envs[key].baseline_plan()[0], chip_values)
        k = (key, action.transfer, action.captain, action.chip)
        if k not in cache:
            cache[k] = receding_value(envs[key], action, chip_values)
        return cache[k] - base[key]

    def advisor_reward(prompts, completions, state_key, **kwargs):
        valid = []
        for completion, key in zip(completions, state_key):
            text = completion if isinstance(completion, str) else completion[0].get("content", "")
            choice = parse_week_choice(text, facts[key])
            valid.append(None if choice is None else value(key, choice))
        rewards = []
        for r, key in zip(valid, state_key):
            if r is None:
                group = [x for x, k in zip(valid, state_key) if k == key and x is not None]
                r = min(group + [value(key, WeekAction(transfer="hold"))]) - UNPARSEABLE_MARGIN
            rewards.append(r)
        return rewards

    advisor_reward.__name__ = "advisor_reward"
    return advisor_reward


def dry_run() -> None:
    from transformers import AutoTokenizer

    t0 = time.time()
    envs, facts, rows = build_envs()
    tok = AutoTokenizer.from_pretrained(MODEL_PATH)
    longest = max(len(tok(tok.apply_chat_template(r["prompt"], tokenize=False, add_generation_prompt=True),
                          add_special_tokens=False)["input_ids"]) for r in rows)
    print(f"prompts {len(rows)} | built in {time.time() - t0:.0f}s | prompt tokens max {longest} (budget {MAX_PROMPT_LENGTH})")
    assert longest <= MAX_PROMPT_LENGTH
    reward = make_reward_func(envs, facts)
    gains = {c: [] for c in ("none", "triple_captain", "bench_boost", "free_hit", "wildcard")}
    for key in list(envs)[::10]:
        f = facts[key]
        texts = [json.dumps({"chip": c, "captain": f["captains"][0], "transfer": "best1"}) for c in gains if c == "none" or c in f["chips"]]
        rs = reward([""] * (len(texts) + 1), texts + ["garbage"], [key] * (len(texts) + 1))
        assert rs[-1] < min(rs[:-1]), "garbage must score worst"
        for t, r in zip(texts, rs):
            gains[json.loads(t)["chip"]].append(r)
    print("reward path OK; mean reward vs planner by week-1 choice: " +
          ", ".join(f"{c} {sum(v) / len(v):+.1f} (n {len(v)})" for c, v in gains.items() if v))


def main() -> None:
    if "--dry-run" in sys.argv:
        dry_run()
        return
    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer

    envs, facts, rows = build_envs()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    tokenizer.eos_token = "<turn|>"  # Gemma ends a turn with <turn|> (106); TRL stops and masks at eos
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto")
    suffixes = ("self_attn.q_proj.weight", "self_attn.k_proj.weight", "self_attn.v_proj.weight", "self_attn.o_proj.weight")
    targets = sorted(n for n, _ in model.named_parameters() if n.startswith("model.language_model.layers.") and n.endswith(suffixes))
    peft_config = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=None,
                             target_parameters=targets)
    args = GRPOConfig(output_dir=str(OUTPUT_DIR), num_generations=NUM_GENERATIONS, per_device_train_batch_size=NUM_GENERATIONS,
                      gradient_accumulation_steps=2, learning_rate=LEARNING_RATE, num_train_epochs=NUM_EPOCHS,
                      temperature=TEMPERATURE, beta=KL_BETA, max_completion_length=MAX_COMPLETION_LENGTH, logging_steps=1,
                      save_steps=50, save_total_limit=3, bf16=True, report_to="none")
    trainer = GRPOTrainer(model=model, reward_funcs=make_reward_func(envs, facts), args=args,
                          train_dataset=Dataset.from_list(rows), processing_class=tokenizer, peft_config=peft_config)
    print(f"merged-weight generation on {merged_generation(trainer.model)} LoRA-wrapped weights", flush=True)
    trainer.train()
    trainer.save_model(str(OUTPUT_DIR))
    tokenizer.save_pretrained(str(OUTPUT_DIR))


if __name__ == "__main__":
    main()

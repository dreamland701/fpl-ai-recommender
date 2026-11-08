"""GRPO Phase-1 training: decision-layer policy over the weekly-bandit env.

Per docs/decision_layer_plan_2026_07_09.md §4 (Wes-approved queue 2026-07-10):
the policy (Gemma-4-E4B + fresh LoRA) reads a weekly decision state and emits
bounded JSON (DecisionWeights + captain pick + transfer aggressiveness). Each
completion is rolled through the deterministic optimizer against realized
outcomes; reward = realized points − the classic baseline's realized points
on the same state. TRL's GRPOTrainer group-normalizes advantages over
num_generations samples per state.

Training states come from `scripts/build_grpo_state_cache.py` (seasons
2022-23..2024-25 GW12-30). 2025-26 GW12-30 is the untouched held-out gate —
never include it in FPL_GRPO_TRAIN_SEASONS.

Config via env vars (mirrors train_gemma_sft.py conventions). CPU dry-run:
  python3 train_gemma_grpo.py --dry-run
validates states, prompts, and the reward path without loading the model.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.grpo_env import WeeklyBanditEnv, load_states  # noqa: E402

MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", "google/gemma-4-E4B-it")
STATES_DIR = Path(os.environ.get("FPL_GRPO_STATES_DIR", ROOT / "reports" / "grpo_states"))
TRAIN_SEASONS = os.environ.get(
    "FPL_GRPO_TRAIN_SEASONS", "2022-23,2023-24,2024-25,2025-26-early"
).split(",")
OUTPUT_DIR = Path(os.environ.get("FPL_GRPO_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_e4b_grpo_decision_v1"))
NUM_GENERATIONS = int(os.environ.get("FPL_GRPO_NUM_GENERATIONS", "8"))
LEARNING_RATE = float(os.environ.get("FPL_GRPO_LEARNING_RATE", "1e-5"))
NUM_EPOCHS = float(os.environ.get("FPL_GRPO_NUM_EPOCHS", "8"))
MAX_STEPS = int(os.environ.get("FPL_GRPO_MAX_STEPS", "-1"))
TEMPERATURE = float(os.environ.get("FPL_GRPO_TEMPERATURE", "0.8"))
KL_BETA = float(os.environ.get("FPL_GRPO_KL_BETA", "0.04"))
MAX_PROMPT_LENGTH = int(os.environ.get("FPL_GRPO_MAX_PROMPT_LENGTH", "1536"))
MAX_COMPLETION_LENGTH = int(os.environ.get("FPL_GRPO_MAX_COMPLETION_LENGTH", "96"))
TOP_N_CANDIDATES = int(os.environ.get("FPL_GRPO_TOP_N_CANDIDATES", "24"))
SAVE_STEPS = int(os.environ.get("FPL_GRPO_SAVE_STEPS", "50"))
LOGGING_STEPS = int(os.environ.get("FPL_GRPO_LOGGING_STEPS", "1"))

UNPARSEABLE_REWARD = -1.0


def build_envs_and_rows():
    envs: dict[str, WeeklyBanditEnv] = {}
    rows: list[dict[str, str]] = []
    for season in TRAIN_SEASONS:
        season = season.strip()
        path = STATES_DIR / f"{season}.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"missing state cache {path}; run scripts/build_grpo_state_cache.py")
        for state in load_states(path):
            key = f"{state.season}:{state.week}"
            env = WeeklyBanditEnv(state)
            envs[key] = env
            rows.append({"prompt": env.state_prompt(top_n_candidates=TOP_N_CANDIDATES), "state_key": key})
    return envs, rows


def make_reward_func(envs: dict[str, WeeklyBanditEnv]):
    def decision_reward(prompts, completions, state_key, **kwargs):
        from fpl_ai.grpo_env import parse_action

        rewards = []
        for completion, key in zip(completions, state_key):
            text = completion if isinstance(completion, str) else completion[0].get("content", "")
            env = envs[key]
            action = parse_action(text)
            if action is None:
                rewards.append(UNPARSEABLE_REWARD)
                continue
            realized, _ = env._realized_for_action(action)
            rewards.append(realized - env.baseline_realized())
        return rewards

    decision_reward.__name__ = "decision_reward"
    return decision_reward


def dry_run() -> None:
    envs, rows = build_envs_and_rows()
    print(f"states: {len(rows)} across {TRAIN_SEASONS}")
    lengths = [len(row["prompt"]) for row in rows]
    print(f"prompt chars: min {min(lengths)} / max {max(lengths)} (~{max(lengths)//4} tokens)")
    reward_func = make_reward_func(envs)
    canned = [
        "{}",
        '{"availability": "soft", "soft_knee": 0.8}',
        '{"horizon": "blend5", "transfer_aggressiveness": 0.5}',
        "garbage",
    ]
    sample = rows[: max(1, len(rows) // 10)]
    all_rewards = []
    for row in sample:
        rewards = reward_func(
            prompts=[row["prompt"]] * len(canned),
            completions=canned,
            state_key=[row["state_key"]] * len(canned),
        )
        all_rewards.extend(rewards)
    parsed = [reward for reward in all_rewards if reward != UNPARSEABLE_REWARD]
    print(
        f"reward path OK over {len(sample)} states x {len(canned)} actions: "
        f"mean {sum(parsed)/len(parsed):+.2f}, min {min(parsed):+.1f}, max {max(parsed):+.1f}"
    )
    zero_default = [
        reward
        for row in sample
        for reward in [reward_func(prompts=[row["prompt"]], completions=["{}"], state_key=[row["state_key"]])[0]]
    ]
    assert all(reward == 0.0 for reward in zero_default), "default action must be reward-neutral"
    print("default-action neutrality: OK")


def main() -> None:
    if "--dry-run" in sys.argv:
        dry_run()
        return

    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer

    envs, rows = build_envs_and_rows()
    dataset = Dataset.from_list(rows)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    longest = max(len(tokenizer(row["prompt"])["input_ids"]) for row in rows)
    assert longest <= MAX_PROMPT_LENGTH, (
        f"prompt exceeds budget: {longest} > {MAX_PROMPT_LENGTH} tokens"
    )
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto")

    # Same LoRA targeting approach as train_gemma_sft.py (language-model layers).
    # Full parameter names including ".weight", exactly as train_gemma_sft.py
    # passes them — peft's target_parameters matches on parameter names.
    prefixes = ("model.language_model.layers.", "model.layers.")
    suffixes = (
        "self_attn.q_proj.weight",
        "self_attn.k_proj.weight",
        "self_attn.v_proj.weight",
        "self_attn.o_proj.weight",
    )
    target_parameters = None
    for prefix in prefixes:
        candidates = sorted(
            name
            for name, _ in model.named_parameters()
            if name.startswith(prefix) and any(name.endswith(suffix) for suffix in suffixes)
        )
        if candidates:
            target_parameters = candidates
            break
    if not target_parameters:
        raise RuntimeError("No Gemma language-model target parameters were found for LoRA.")
    print(f"Targeting {len(target_parameters)} language-model parameters for LoRA")
    peft_config = LoraConfig(
        r=int(os.environ.get("FPL_GEMMA_LORA_R", "16")),
        lora_alpha=int(os.environ.get("FPL_GEMMA_LORA_ALPHA", "32")),
        lora_dropout=0.0,
        task_type="CAUSAL_LM",
        target_modules=None,
        target_parameters=target_parameters,
    )

    args = GRPOConfig(
        output_dir=str(OUTPUT_DIR),
        num_generations=NUM_GENERATIONS,
        per_device_train_batch_size=NUM_GENERATIONS,
        gradient_accumulation_steps=int(os.environ.get("FPL_GRPO_GRAD_ACCUM", "2")),
        learning_rate=LEARNING_RATE,
        num_train_epochs=NUM_EPOCHS,
        max_steps=MAX_STEPS,
        temperature=TEMPERATURE,
        beta=KL_BETA,
        # TRL 1.0 dropped max_prompt_length; prompts are bounded by
        # construction (see WeeklyBanditEnv.state_prompt), asserted below.
        max_completion_length=MAX_COMPLETION_LENGTH,
        logging_steps=LOGGING_STEPS,
        save_steps=SAVE_STEPS,
        save_total_limit=3,
        bf16=True,
        report_to="none",
    )
    trainer = GRPOTrainer(
        model=model,
        reward_funcs=make_reward_func(envs),
        args=args,
        train_dataset=dataset,
        processing_class=tokenizer,
        peft_config=peft_config,
    )
    trainer.train(resume_from_checkpoint=os.environ.get("FPL_GRPO_RESUME_FROM_CHECKPOINT"))
    trainer.save_model(str(OUTPUT_DIR))
    tokenizer.save_pretrained(str(OUTPUT_DIR))


if __name__ == "__main__":
    main()

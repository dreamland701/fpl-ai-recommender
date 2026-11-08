"""G5 GRPO training on the rebuilt plan environment (src/fpl_ai/grpo_plan_env_v2.py).

Same TRL/LoRA recipe as train_gemma_grpo_plan.py; what changed is the task.
The policy reads an origin-only state and emits five weekly actions (hold /
best single / best two transfers from the exact optimizer, a captain, and any
of the four chips). Reward = realised points minus a deterministic planner
holding the same chips and free transfers. Episodes: five consecutive weeks,
stride 1, from reports/grpo_states_v2 (2022-23..2025-26 GW26). Chip budgets are
sampled per episode and half-season so the policy has to read what it still has.

CPU dry-run (reward path, timing, neutrality of the planner's own plan):
  python3 train_gemma_grpo_plan_v2.py --dry-run
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

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, PlanEnvV2, WeekAction, chip_half, parse_plan, receding_value  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", "google/gemma-4-E4B-it")
STATES_DIR = Path(os.environ.get("FPL_GRPO_STATES_DIR", ROOT / "reports" / "grpo_states_v2"))
TRAIN_KEYS = os.environ.get("FPL_GRPO_TRAIN_KEYS", "2022-23,2023-24,2024-25,2025-26-train").split(",")
OUTPUT_DIR = Path(os.environ.get("FPL_GRPO_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_e4b_grpo_plan_g5"))
HORIZON = int(os.environ.get("FPL_GRPO_PLAN_HORIZON", "5"))
STRIDE = int(os.environ.get("FPL_GRPO_PLAN_STRIDE", "1"))
NUM_GENERATIONS = int(os.environ.get("FPL_GRPO_NUM_GENERATIONS", "8"))
LEARNING_RATE = float(os.environ.get("FPL_GRPO_LEARNING_RATE", "1e-5"))
NUM_EPOCHS = float(os.environ.get("FPL_GRPO_NUM_EPOCHS", "4"))
MAX_STEPS = int(os.environ.get("FPL_GRPO_MAX_STEPS", "-1"))
TEMPERATURE = float(os.environ.get("FPL_GRPO_TEMPERATURE", "0.8"))
KL_BETA = float(os.environ.get("FPL_GRPO_KL_BETA", "0.04"))
# Our own memory guard (TRL 1.0 never truncates prompts). G5 prompts reach
# ~1,700 tokens: the squad and outlook tables are number-dense (~1.9 chars/token).
MAX_PROMPT_LENGTH = int(os.environ.get("FPL_GRPO_MAX_PROMPT_LENGTH", "2048"))
MAX_COMPLETION_LENGTH = int(os.environ.get("FPL_GRPO_MAX_COMPLETION_LENGTH", "256"))
SAVE_STEPS = int(os.environ.get("FPL_GRPO_SAVE_STEPS", "50"))
# "receding" (default since G6): only the plan's first week is scored, followed by the planner
# re-planned from the state it leaves, plus held-chip values; this is how the closed-loop eval
# plays. "plan": the whole open-loop 5-week plan (G5, G5b), which taught chip procrastination
# and end-of-window chip dumping.
REWARD_MODE = os.environ.get("FPL_GRPO_REWARD_MODE", "receding")
CHIP_VALUES_PATH = Path(os.environ.get("FPL_GRPO_CHIP_VALUES", STATES_DIR / "chip_values.json"))

# Chip budgets per half-season: everything fresh is common early in a half,
# scarcity later; the policy must condition on the prompt's chips line.
BUDGETS = [frozenset(CHIPS), frozenset({"bench_boost", "triple_captain"}), frozenset({"triple_captain"}),
           frozenset({"bench_boost"}), frozenset({"wildcard", "free_hit"}), frozenset()]
BUDGET_WEIGHTS = [0.35, 0.2, 0.15, 0.1, 0.1, 0.1]


def sample_chips(key: str, weeks):
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    for half in sorted({chip_half(w) for w in weeks}):
        chips[half] = random.Random(f"chips:{key}:{half}").choices(BUDGETS, weights=BUDGET_WEIGHTS, k=1)[0]
    return chips


def build_envs():
    envs, rows = {}, []
    for key in TRAIN_KEYS:
        path = STATES_DIR / f"{key.strip()}.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"missing {path}; run scripts/build_grpo_state_cache_v2.py")
        states = sorted(load_states(path), key=lambda s: s.week)
        for start in range(0, len(states) - HORIZON + 1, STRIDE):
            window = states[start:start + HORIZON]
            if [s.week for s in window] != list(range(window[0].week, window[0].week + HORIZON)):
                continue
            ekey = f"{key}:{window[0].week}"
            env = PlanEnvV2(window, optimize, chips=sample_chips(ekey, [s.week for s in window]))
            envs[ekey] = env
            # Conversational, so TRL applies the chat template: untemplated, the instruct model writes
            # newline-separated objects instead of an array and 0/8 step-0 samples parsed; templated, 24/24.
            rows.append({"prompt": [{"role": "user", "content": env.state_prompt()}], "state_key": ekey})
    return envs, rows


UNPARSEABLE_MARGIN = 10.0


def make_reward_func(envs):
    """Reward relative to the same-chips planner (see REWARD_MODE). An unparseable plan scores below
    every valid plan in its group and below holding: a flat penalty (the env's -5) would beat
    bad-but-valid plans (step-0 samples reached -43) and teach the policy to emit garbage in hard weeks."""
    chip_values = {}
    if REWARD_MODE == "receding":
        values = json.loads(CHIP_VALUES_PATH.read_text())
        chip_values = {c: float(values[c]) for c in ("free_hit", "wildcard")}
    cache, base = {}, {}

    def value(key, plan):
        env = envs[key]
        if REWARD_MODE == "plan":
            return env.rollout(plan)[0] - env.baseline_total()
        first = plan[0]
        if key not in base:
            base[key] = receding_value(env, env.baseline_plan()[0], chip_values)
        k = (key, first.transfer, first.captain, first.chip)
        if k not in cache:
            cache[k] = receding_value(env, first, chip_values)
        return cache[k] - base[key]

    def hold_reward(key):
        return value(key, [WeekAction(transfer="hold", captain=None, chip="none")] * envs[key].horizon)

    def plan_reward(prompts, completions, state_key, **kwargs):
        valid = []
        for completion, key in zip(completions, state_key):
            text = completion if isinstance(completion, str) else completion[0].get("content", "")
            plan = parse_plan(text, envs[key].horizon)
            valid.append(None if plan is None else value(key, plan))
        rewards = []
        for r, key in zip(valid, state_key):
            if r is None:
                group = [x for x, k in zip(valid, state_key) if k == key and x is not None]
                r = min(group + [hold_reward(key)]) - UNPARSEABLE_MARGIN
            rewards.append(r)
        return rewards

    plan_reward.__name__ = "plan_reward"
    return plan_reward

def merged_generation(peft_model) -> int:
    """Generate with the LoRA deltas merged into the base weights, then restore them bit-exactly.

    target_parameters LoRA registers and removes a parametrization on every wrapped weight in each
    forward call (~1.4 s per call on the GB10), and generation makes one call per token: 270 s per
    GRPO step. Merged, a decode step takes ~0.16 s. Training forward/backward passes are untouched.
    Restoring from a copy (not subtracting the delta) keeps bf16 rounding from drifting the base weights.
    """
    import torch
    from peft.tuners.lora.layer import ParamWrapper

    wrappers = [m for m in peft_model.modules() if isinstance(m, ParamWrapper)]
    original = peft_model.generate

    def generate(*args, **kwargs):
        with torch.no_grad():
            saved = [getattr(m.get_base_layer(), m.parameter_name).data.clone() for m in wrappers]
            for m in wrappers:
                m.merge()
        try:
            return original(*args, **kwargs)
        finally:
            with torch.no_grad():
                for m, weight in zip(wrappers, saved):
                    m.merged_adapters.clear()
                    getattr(m.get_base_layer(), m.parameter_name).data.copy_(weight)

    peft_model.generate = generate
    return len(wrappers)


def dry_run() -> None:
    t0 = time.time()
    envs, rows = build_envs()
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(MODEL_PATH)
    longest = max(len(tok(tok.apply_chat_template(r["prompt"], tokenize=False, add_generation_prompt=True),
                          add_special_tokens=False)["input_ids"]) for r in rows)
    print(f"episodes {len(rows)} | prompt build {time.time() - t0:.0f}s | prompt tokens max {longest} (budget {MAX_PROMPT_LENGTH})")
    assert longest <= MAX_PROMPT_LENGTH, f"prompt exceeds budget: {longest} > {MAX_PROMPT_LENGTH}"
    reward = make_reward_func(envs)
    sample = list(envs.items())[:: max(1, len(envs) // 12)]
    t1 = time.time()
    gains = []
    for key, env in sample:
        planner = json.dumps([{"transfer": a.transfer, "captain": a.captain, "chip": a.chip} for a in env.baseline_plan()])
        hold = json.dumps([{"transfer": "hold", "captain": None, "chip": "none"}] * env.horizon)
        tc_now = json.dumps([{"transfer": "best1", "captain": None, "chip": "triple_captain"}] +
                            [{"transfer": "best1", "captain": None, "chip": "none"}] * (env.horizon - 1))
        rs = reward([""] * 4, [planner, hold, tc_now, "garbage"], [key] * 4)
        assert abs(rs[0]) < 1e-9, f"the planner's own plan must score 0, got {rs[0]} on {key}"
        assert rs[3] < min(rs[:3]), f"garbage must score below every valid plan, got {rs} on {key}"
        gains.append(rs[1:3])
    per_episode = (time.time() - t1) / len(sample)
    print(f"reward mode {REWARD_MODE}; reward path OK on {len(sample)} episodes ({per_episode:.1f}s per 4-plan group); "
          f"hold-all mean {sum(g[0] for g in gains) / len(gains):+.1f}, TC-week-1 mean {sum(g[1] for g in gains) / len(gains):+.1f}")


def main() -> None:
    if "--dry-run" in sys.argv:
        dry_run()
        return
    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer

    envs, rows = build_envs()
    dataset = Dataset.from_list(rows)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    longest = max(len(tokenizer(tokenizer.apply_chat_template(r["prompt"], tokenize=False, add_generation_prompt=True),
                                add_special_tokens=False)["input_ids"]) for r in rows)
    assert longest <= MAX_PROMPT_LENGTH, f"prompt exceeds budget: {longest} > {MAX_PROMPT_LENGTH}"
    # TRL stops generation at and masks after the tokenizer's eos. Gemma ends a turn with <turn|> (106);
    # left at <eos> (1), step-0 samples ran to the length cap repeating <turn|>.
    tokenizer.eos_token = "<turn|>"
    assert tokenizer.eos_token_id == 106, tokenizer.eos_token_id
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto")
    prefixes = ("model.language_model.layers.", "model.layers.")
    suffixes = ("self_attn.q_proj.weight", "self_attn.k_proj.weight", "self_attn.v_proj.weight", "self_attn.o_proj.weight")
    target_parameters = None
    for prefix in prefixes:
        found = sorted(n for n, _ in model.named_parameters() if n.startswith(prefix) and any(n.endswith(s) for s in suffixes))
        if found:
            target_parameters = found
            break
    if not target_parameters:
        raise RuntimeError("No Gemma language-model target parameters were found for LoRA.")
    peft_config = LoraConfig(r=int(os.environ.get("FPL_GEMMA_LORA_R", "16")),
                             lora_alpha=int(os.environ.get("FPL_GEMMA_LORA_ALPHA", "32")), lora_dropout=0.0,
                             task_type="CAUSAL_LM", target_modules=None, target_parameters=target_parameters)
    init_adapter = os.environ.get("FPL_GRPO_INIT_ADAPTER")
    if init_adapter:
        # G6: continue training the imitation adapter, so RL starts at planner level. Use
        # FPL_GRPO_KL_BETA=0: TRL's reference is the adapter-disabled base model, and a KL
        # term would pull the policy back toward it, away from the imitation policy.
        from peft import PeftModel

        model = PeftModel.from_pretrained(model, init_adapter, is_trainable=True)
        peft_config = None
        print(f"initialised from {init_adapter}", flush=True)
    args = GRPOConfig(output_dir=str(OUTPUT_DIR), num_generations=NUM_GENERATIONS,
                      per_device_train_batch_size=NUM_GENERATIONS,
                      gradient_accumulation_steps=int(os.environ.get("FPL_GRPO_GRAD_ACCUM", "2")),
                      learning_rate=LEARNING_RATE, num_train_epochs=NUM_EPOCHS, max_steps=MAX_STEPS,
                      temperature=TEMPERATURE, beta=KL_BETA, max_completion_length=MAX_COMPLETION_LENGTH,
                      logging_steps=1, save_steps=SAVE_STEPS, save_total_limit=3, bf16=True, report_to="none")
    trainer = GRPOTrainer(model=model, reward_funcs=make_reward_func(envs), args=args, train_dataset=dataset,
                          processing_class=tokenizer, peft_config=peft_config)
    if os.environ.get("FPL_GRPO_MERGED_GENERATION", "1") == "1":
        print(f"merged-weight generation on {merged_generation(trainer.model)} LoRA-wrapped weights", flush=True)
    trainer.train(resume_from_checkpoint=os.environ.get("FPL_GRPO_RESUME_FROM_CHECKPOINT"))
    trainer.save_model(str(OUTPUT_DIR))
    tokenizer.save_pretrained(str(OUTPUT_DIR))


if __name__ == "__main__":
    main()

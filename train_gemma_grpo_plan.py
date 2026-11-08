"""G2 GRPO training: plan-horizon decision policy over chained weekly states.

Per docs/decision_layer_plan_2026_07_09.md §4 extended by the G2 design
(Wes approved the G2 direction 2026-07-18): the policy reads a K-week plan
state (squad + candidates + week-by-week outlook) and emits one JSON array
of K bounded weekly actions — G1's knobs plus explicit free-transfer
banking and chip timing (bench_boost / triple_captain, each once per
window). The env rolls the plan through K weeks with the squad, bank, and
free transfers evolving under the policy's own choices; reward = cumulative
realized − the all-defaults plan's cumulative on the same window (paired
sequential baseline). TRL GRPOTrainer group-normalizes over
num_generations plans per episode.

Episodes come from the same state cache as G1 (2025-26 GW12-30 stays the
untouched held-out gate). Overlapping windows (stride 1) multiply training
episodes — the squad-diversity lever.

v3: each episode is also assigned a sampled chip-availability budget
(both/bench_boost-only/triple_captain-only/none) instead of always
assuming both chips are fresh — teaches the policy to read the prompt's
season-remaining-chips line and not spend a plan on a chip it can't
legally have. See CHIP_BUDGET_OPTIONS/_sample_chip_budget below.

CPU dry-run:  python3 train_gemma_grpo_plan.py --dry-run
"""

from __future__ import annotations

import os
import random
import sys
from dataclasses import replace as dc_replace
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env import CHIPS, PlanEpisodeEnv, build_episodes, chip_half  # noqa: E402
from fpl_ai.types import SquadPlayer  # noqa: E402

MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", "google/gemma-4-E4B-it")
STATES_DIR = Path(os.environ.get("FPL_GRPO_STATES_DIR", ROOT / "reports" / "grpo_states"))
TRAIN_SEASONS = os.environ.get(
    "FPL_GRPO_TRAIN_SEASONS", "2022-23,2023-24,2024-25,2025-26-early"
).split(",")
OUTPUT_DIR = Path(os.environ.get("FPL_GRPO_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_e4b_grpo_plan_v1"))
HORIZON = int(os.environ.get("FPL_GRPO_PLAN_HORIZON", "6"))
STRIDE = int(os.environ.get("FPL_GRPO_PLAN_STRIDE", "1"))
NUM_GENERATIONS = int(os.environ.get("FPL_GRPO_NUM_GENERATIONS", "8"))
LEARNING_RATE = float(os.environ.get("FPL_GRPO_LEARNING_RATE", "1e-5"))
NUM_EPOCHS = float(os.environ.get("FPL_GRPO_NUM_EPOCHS", "8"))
MAX_STEPS = int(os.environ.get("FPL_GRPO_MAX_STEPS", "-1"))
TEMPERATURE = float(os.environ.get("FPL_GRPO_TEMPERATURE", "0.8"))
KL_BETA = float(os.environ.get("FPL_GRPO_KL_BETA", "0.04"))
MAX_PROMPT_LENGTH = int(os.environ.get("FPL_GRPO_MAX_PROMPT_LENGTH", "1536"))
MAX_COMPLETION_LENGTH = int(os.environ.get("FPL_GRPO_MAX_COMPLETION_LENGTH", "512"))
TOP_N_CANDIDATES = int(os.environ.get("FPL_GRPO_TOP_N_CANDIDATES", "20"))
SAVE_STEPS = int(os.environ.get("FPL_GRPO_SAVE_STEPS", "50"))
LOGGING_STEPS = int(os.environ.get("FPL_GRPO_LOGGING_STEPS", "1"))
# Deployment-regime filter: drop weeks with no adapter deltas (e.g. 2023-24
# GW2-11 has no chronologically legal adapter), so every training state
# reflects the live-GW regime of classic + text adjustments.
REQUIRE_DELTAS = os.environ.get("FPL_GRPO_REQUIRE_DELTAS", "0") == "1"

UNPARSEABLE_REWARD = -1.0

# G2-v3 chip-budget curriculum (fixes the bug where v2 was trained
# believing every window has a fresh bench_boost/triple_captain, so it
# learned to request a chip almost every week regardless of context —
# harmless in isolated training episodes, but at real composed-season eval
# those requests are illegal replays that get masked to "none", wasting the
# plan's other decisions on a chip it can't have). Each overlapping
# training episode is independently a bandit sample (TRL's GRPOTrainer is
# single-turn, no real cross-episode season trajectory), so the fix is to
# vary which chips are still available across episodes and let the policy
# learn to condition on the prompt's "chips still available" line instead
# of always assuming both are fresh. Sampled per half-season (1 = GW<=19,
# 2 = GW>=20 — each chip has an independent copy per half that renews at
# GW20). Weights are a rough reflection of chip scarcity building up within
# a half (most windows still have at least one chip left in that half).
CHIP_BUDGET_OPTIONS = [frozenset(CHIPS), frozenset({"bench_boost"}), frozenset({"triple_captain"}), frozenset()]
CHIP_BUDGET_WEIGHTS = [0.5, 0.2, 0.2, 0.1]


def _sample_chip_budget(key: str, weeks: list[int]) -> dict[int, frozenset]:
    budget = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    for half in sorted({chip_half(week) for week in weeks}):
        rng = random.Random(f"chip_budget:{key}:h{half}")
        budget[half] = rng.choices(CHIP_BUDGET_OPTIONS, weights=CHIP_BUDGET_WEIGHTS, k=1)[0]
    return budget


# G3 squad-diversity augmentation: each extra variant perturbs the episode's
# STARTING squad (swap 1-3 players for same-position, similar-price
# alternatives, jitter the bank) so the policy trains on many more squad
# situations than the 59 canonical backtest trajectories. Only states[0]'s
# squad/bank matter for the trajectory — later weeks' squads evolve under
# the policy's own choices — so perturbing the first week multiplies
# genuinely distinct decision problems at zero data-collection cost.
# Legality preserved: position-for-position swaps, max 3 per club, bank
# stays non-negative. Seeded per (episode, variant) for reproducibility.
AUGMENT_VARIANTS = int(os.environ.get("FPL_GRPO_AUGMENT_VARIANTS", "0"))


def _augment_episode(env: PlanEpisodeEnv, key: str, variant: int) -> PlanEpisodeEnv | None:
    rng = random.Random(f"augment:{key}:v{variant}")
    start = env.states[0]
    squad = list(start.squad)
    squad_ids = {player.player_id for player in squad}
    forecast_by_id = {f.player_id: f for f in start.forecasts}
    team_counts: dict[int, int] = {}
    for player in squad:
        team_counts[player.team_id] = team_counts.get(player.team_id, 0) + 1

    bank = float(start.bank)
    n_swaps = rng.randint(1, 3)
    swapped = 0
    for _ in range(n_swaps * 4):  # a few attempts per desired swap
        if swapped >= n_swaps:
            break
        out_index = rng.randrange(len(squad))
        out_player = squad[out_index]
        candidates = [
            f for f in start.forecasts
            if f.position == out_player.position
            and f.player_id not in squad_ids
            and abs(f.price - out_player.sell_price) <= 0.5
            and f.price <= out_player.sell_price + bank
            # Club cap only enforceable when team ids are real; the G2 state
            # caches predate the team_id fix and carry -1 throughout (same
            # `> 0` guard the rollout itself uses).
            and (f.team_id <= 0 or team_counts.get(f.team_id, 0) < 3)
        ]
        if not candidates:
            continue
        incoming = rng.choice(candidates)
        bank += out_player.sell_price - incoming.price
        team_counts[out_player.team_id] -= 1
        team_counts[incoming.team_id] = team_counts.get(incoming.team_id, 0) + 1
        squad_ids.discard(out_player.player_id)
        squad_ids.add(incoming.player_id)
        squad[out_index] = SquadPlayer(
            player_id=incoming.player_id,
            player_name=incoming.player_name,
            team_id=incoming.team_id,
            position=incoming.position,
            sell_price=incoming.price,
        )
        swapped += 1
    if swapped == 0:
        return None
    bank = max(0.0, round(bank + rng.uniform(-0.5, 0.5), 1))
    new_start = dc_replace(start, squad=squad, bank=bank)
    return PlanEpisodeEnv([new_start, *env.states[1:]])


def build_episodes_and_rows():
    states = []
    for season in TRAIN_SEASONS:
        season = season.strip()
        path = STATES_DIR / f"{season}.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"missing state cache {path}; run scripts/build_grpo_state_cache.py")
        season_states = load_states(path)
        if REQUIRE_DELTAS:
            season_states = [state for state in season_states if state.llm_deltas]
        states.extend(season_states)
    episodes = build_episodes(states, horizon=HORIZON, stride=STRIDE)
    envs: dict[str, PlanEpisodeEnv] = {}
    rows: list[dict[str, str]] = []
    expanded: list[tuple[str, PlanEpisodeEnv]] = []
    for env in episodes:
        base_key = f"{env.states[0].season}:{env.states[0].week}:h{env.horizon}"
        expanded.append((base_key, env))
        for variant in range(1, AUGMENT_VARIANTS + 1):
            augmented = _augment_episode(env, base_key, variant)
            if augmented is not None:
                expanded.append((f"{base_key}:aug{variant}", augmented))
    for key, env in expanded:
        env.available_chips = _sample_chip_budget(key, [state.week for state in env.states])
        envs[key] = env
        rows.append({"prompt": env.state_prompt(top_n_candidates=TOP_N_CANDIDATES), "state_key": key})
    return envs, rows


def make_reward_func(envs: dict[str, PlanEpisodeEnv]):
    def plan_reward(prompts, completions, state_key, **kwargs):
        from fpl_ai.grpo_plan_env import parse_plan

        rewards = []
        for completion, key in zip(completions, state_key):
            text = completion if isinstance(completion, str) else completion[0].get("content", "")
            env = envs[key]
            plan = parse_plan(text, env.horizon)
            if plan is None:
                rewards.append(UNPARSEABLE_REWARD)
                continue
            realized, _ = env.rollout(plan)
            rewards.append(realized - env.baseline_total())
        return rewards

    plan_reward.__name__ = "plan_reward"
    return plan_reward


def dry_run() -> None:
    import json

    envs, rows = build_episodes_and_rows()
    print(f"episodes: {len(rows)} (horizon {HORIZON}, stride {STRIDE}) across {TRAIN_SEASONS}")
    lengths = [len(row["prompt"]) for row in rows]
    print(f"prompt chars: min {min(lengths)} / max {max(lengths)} (~{max(lengths)//4} tokens)")
    reward_func = make_reward_func(envs)
    default_plan = json.dumps([{} for _ in range(HORIZON)])
    canned = [
        default_plan,
        json.dumps([{"chip_play": "bench_boost"}] + [{} for _ in range(HORIZON - 1)]),
        json.dumps([{"bank_transfer": True}] + [{"transfer_aggressiveness": 1.5}] + [{} for _ in range(HORIZON - 2)]),
        "garbage",
    ]
    sample = list(envs.items())[: max(1, len(envs) // 5)]
    all_rewards = []
    for key, env in sample:
        rewards = reward_func(
            prompts=[""] * len(canned),
            completions=canned,
            state_key=[key] * len(canned),
        )
        all_rewards.append(rewards)
        assert rewards[0] == 0.0, f"default plan must be reward-neutral, got {rewards[0]} on {key}"
        assert rewards[3] == UNPARSEABLE_REWARD
    flat = [reward for rewards in all_rewards for reward in rewards[1:3]]
    print(
        f"reward path OK over {len(sample)} episodes: non-default actions "
        f"mean {sum(flat)/len(flat):+.2f}, min {min(flat):+.1f}, max {max(flat):+.1f}"
    )
    print("default-plan neutrality: OK")


def main() -> None:
    if "--dry-run" in sys.argv:
        dry_run()
        return

    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer

    envs, rows = build_episodes_and_rows()
    dataset = Dataset.from_list(rows)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    longest = max(len(tokenizer(row["prompt"])["input_ids"]) for row in rows)
    assert longest <= MAX_PROMPT_LENGTH, (
        f"prompt exceeds budget: {longest} > {MAX_PROMPT_LENGTH} tokens"
    )
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto")

    # v2b ablation: start GRPO from an existing SFT LoRA (e.g. E7) by MERGING
    # it into the base weights, then training a fresh LoRA on top. Merging
    # (rather than continuing the SFT adapter) sidesteps peft's one
    # target_parameters-adapter-per-model limit AND upgrades the ablation:
    # TRL's KL reference is the adapter-disabled model, which post-merge is
    # base+E7 — so the init anchors the KL term instead of washing out.
    # NOTE: the saved artifact is then a delta on the MERGED model; eval must
    # stack base + init adapter (merged) + this adapter.
    init_adapter = os.environ.get("FPL_GRPO_INIT_ADAPTER")
    if init_adapter:
        from peft import PeftModel

        model = PeftModel.from_pretrained(model, init_adapter).merge_and_unload()
        print(f"Merged init adapter into base: {init_adapter}")
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
        # TRL 1.0 has no max_prompt_length; prompts are bounded by
        # construction and asserted above.
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

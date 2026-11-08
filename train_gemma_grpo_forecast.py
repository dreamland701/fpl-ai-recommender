#!/usr/bin/env python3
"""G4: GRPO on the forecast layer — fine-tune the residual adapter with a
decision-value reward (docs/rl_forecast_design.md).

Policy init / KL reference = E11 merged into base weights
(artifacts/gemma4_e4b_merged_e11_defcon): a fresh LoRA trains on top, and
TRL's adapter-disabled reference IS E11, so deltas stay residual to the
champion. Rows = (E11 prompt for player p in week-state s); reward =
realized points of the week's decision with p's sampled delta swapped
into the classic pool, minus the classic-only realized points.

Env vars mirror train_gemma_grpo.py. CPU dry-run:
  python3 train_gemma_grpo_forecast.py --dry-run
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_forecast_env import ForecastRewardEnv, UNPARSEABLE_REWARD  # noqa: E402

MODEL_PATH = os.environ.get("FPL_GEMMA_MODEL_PATH", str(ROOT / "artifacts" / "gemma4_e4b_merged_e11_defcon"))
STATES_DIR = Path(os.environ.get("FPL_GRPO_STATES_DIR", ROOT / "reports" / "grpo_states_adjusted"))
# season key -> optional max week (inclusive) to keep; 2025-26 GW12-29 trains, GW30+ is held out.
TRAIN_SPEC = os.environ.get("FPL_G4_TRAIN_SPEC", "2023-24,2024-25,2025-26-early,2025-26:29")
PROMPTS_PATH = Path(os.environ.get(
    "FPL_G4_PROMPTS",
    ROOT / "reports" / "llm_residual_v2_e11_defcon_top256_thru_2526_34_eval_2526_35_38" / "train.jsonl",
))
OUTPUT_DIR = Path(os.environ.get("FPL_GRPO_OUTPUT_DIR", ROOT / "artifacts" / "gemma4_e4b_g4_forecast_v1"))
TRACE_PATH = Path(os.environ.get("FPL_G4_TRACE", ROOT / "logs" / "g4_reward_trace.jsonl"))
NUM_GENERATIONS = int(os.environ.get("FPL_GRPO_NUM_GENERATIONS", "4"))
LEARNING_RATE = float(os.environ.get("FPL_GRPO_LEARNING_RATE", "1e-5"))
NUM_EPOCHS = float(os.environ.get("FPL_GRPO_NUM_EPOCHS", "1"))
MAX_STEPS = int(os.environ.get("FPL_GRPO_MAX_STEPS", "-1"))
TEMPERATURE = float(os.environ.get("FPL_GRPO_TEMPERATURE", "0.8"))
KL_BETA = float(os.environ.get("FPL_GRPO_KL_BETA", "0.04"))
MAX_COMPLETION_LENGTH = int(os.environ.get("FPL_GRPO_MAX_COMPLETION_LENGTH", "96"))
MAX_PLAYERS_PER_STATE = int(os.environ.get("FPL_G4_MAX_PLAYERS_PER_STATE", "48"))
# v2 (2026-09-04): v1 spent ~70% of steps on zero-advantage groups (players
# nowhere near a decision boundary -> identical rewards -> no gradient) and
# sat at KL~1e-4 from E11. Keep only players whose decision outcome moves
# under a +big OR -big probe delta (both directions: a squad player who
# SHOULD be sold is boundary-sensitive downward).
BOUNDARY_ONLY = os.environ.get("FPL_G4_BOUNDARY_ONLY", "1") == "1"
PROBE_UP = '{"delta_points_1gw":2.0,"delta_points_3gw":4.0,"delta_points_5gw":6.0,"delta_minutes_1gw":0,"delta_appearance_probability":0.0}'
PROBE_DOWN = '{"delta_points_1gw":-2.0,"delta_points_3gw":-4.0,"delta_points_5gw":-6.0,"delta_minutes_1gw":0,"delta_appearance_probability":0.0}'

SAVE_STEPS = int(os.environ.get("FPL_GRPO_SAVE_STEPS", "100"))


def _parse_spec(spec: str):
    out = []
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" in part:
            key, max_week = part.split(":", 1)
            out.append((key.strip(), int(max_week)))
        else:
            out.append((part, None))
    return out


def load_prompts() -> dict:
    prompts = {}
    with PROMPTS_PATH.open() as handle:
        for line in handle:
            row = json.loads(line)
            md = row["metadata"]
            prompts[(str(md["season"]), int(md["week"]), int(md["player_id"]))] = row["prompt"]
    return prompts


def build_envs_and_rows():
    prompts = load_prompts()
    envs: dict[str, ForecastRewardEnv] = {}
    rows: list[dict] = []
    missing = 0
    for key, max_week in _parse_spec(TRAIN_SPEC):
        path = STATES_DIR / f"{key}.jsonl"
        if not path.exists():
            raise FileNotFoundError(f"missing state cache {path}")
        for state in load_states(path):
            if max_week is not None and state.week > max_week:
                continue
            env = ForecastRewardEnv(state)
            envs[env.key] = env
            kept = 0
            for pid in env.relevant_players:
                prompt = prompts.get((state.season, state.week, pid))
                if prompt is None:
                    missing += 1
                    continue
                if BOUNDARY_ONLY:
                    up, _, _ = env.reward(pid, PROBE_UP)
                    down, _, _ = env.reward(pid, PROBE_DOWN)
                    if abs(up) < 1e-9 and abs(down) < 1e-9:
                        continue
                rows.append({"prompt": prompt, "state_key": env.key, "player_id": int(pid)})
                kept += 1
                if kept >= MAX_PLAYERS_PER_STATE:
                    break
    print(f"states {len(envs)} | rows {len(rows)} | relevant players without prompt {missing}")
    return envs, rows


def make_reward_func(envs):
    TRACE_PATH.parent.mkdir(parents=True, exist_ok=True)

    def forecast_decision_reward(prompts, completions, state_key, player_id, **kwargs):
        rewards = []
        with TRACE_PATH.open("a") as trace:
            for completion, key, pid in zip(completions, state_key, player_id):
                text = completion if isinstance(completion, str) else completion[0].get("content", "")
                rel, absolute, ok = envs[key].reward(int(pid), text)
                rewards.append(rel if ok else UNPARSEABLE_REWARD)
                trace.write(json.dumps({"state": key, "player_id": int(pid), "reward_rel": rel,
                                        "realized_abs": absolute, "parsed": ok}) + "\n")
        return rewards

    forecast_decision_reward.__name__ = "forecast_decision_reward"
    return forecast_decision_reward


def dry_run() -> None:
    envs, rows = build_envs_and_rows()
    zero = '{"delta_points_1gw":0.0,"delta_points_3gw":0.0,"delta_points_5gw":0.0,"delta_minutes_1gw":0,"delta_appearance_probability":0.0}'
    big = '{"delta_points_1gw":2.0,"delta_points_3gw":4.0,"delta_points_5gw":6.0,"delta_minutes_1gw":0,"delta_appearance_probability":0.0}'
    checked = boundary = 0
    for env in list(envs.values())[:12]:
        for pid in env.relevant_players:
            r0, _, ok0 = env.reward(pid, zero)
            assert ok0 and abs(r0) < 1e-9, f"zero delta must reproduce classic decision: {env.key} {pid} {r0}"
            r2, _, _ = env.reward(pid, big)
            checked += 1
            boundary += abs(r2) > 1e-9
        assert env.reward(env.relevant_players[0], "not json")[2] is False
    print(f"reward invariants OK: {checked} zero-delta checks; boundary-sensitive players {boundary}/{checked} under a +2/+4/+6 delta")
    print("sample classic realized per state:", [round(e.classic_realized, 1) for e in list(envs.values())[:8]])


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
    dataset = Dataset.from_list(rows).shuffle(seed=11)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH, torch_dtype=torch.bfloat16, device_map="auto")
    prefixes = ("model.language_model.layers.", "model.layers.")
    suffixes = ("self_attn.q_proj.weight", "self_attn.k_proj.weight", "self_attn.v_proj.weight", "self_attn.o_proj.weight")
    target_parameters = None
    for prefix in prefixes:
        candidates = sorted(n for n, _ in model.named_parameters() if n.startswith(prefix) and any(n.endswith(s) for s in suffixes))
        if candidates:
            target_parameters = candidates
            break
    if not target_parameters:
        raise RuntimeError("No Gemma language-model target parameters were found for LoRA.")
    peft_config = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM",
                             target_modules=None, target_parameters=target_parameters)
    args = GRPOConfig(
        output_dir=str(OUTPUT_DIR),
        num_generations=NUM_GENERATIONS,
        per_device_train_batch_size=NUM_GENERATIONS,
        gradient_accumulation_steps=int(os.environ.get("FPL_GRPO_GRAD_ACCUM", "4")),
        learning_rate=LEARNING_RATE,
        num_train_epochs=NUM_EPOCHS,
        max_steps=MAX_STEPS,
        temperature=TEMPERATURE,
        beta=KL_BETA,
        max_completion_length=MAX_COMPLETION_LENGTH,
        logging_steps=1,
        save_steps=SAVE_STEPS,
        save_total_limit=3,
        bf16=True,
        report_to="none",
    )
    trainer = GRPOTrainer(model=model, reward_funcs=make_reward_func(envs), args=args,
                          train_dataset=dataset, processing_class=tokenizer, peft_config=peft_config)
    trainer.train(resume_from_checkpoint=os.environ.get("FPL_GRPO_RESUME_FROM_CHECKPOINT"))
    trainer.save_model(str(OUTPUT_DIR))
    tokenizer.save_pretrained(str(OUTPUT_DIR))


if __name__ == "__main__":
    main()

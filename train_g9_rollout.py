#!/usr/bin/env python3
"""G9: GRPO over the policy's own FULL-HALF rollouts (chips + captain; transfers by the disciplined planner).

G8 (5-week rollouts, held TC/BB valued at zero at the window end) learned to fire triple captain and
bench boost in weeks 1-2 and still beat the planner by +66 on the held-out halves through mid-half free
hits and wildcards. Wes (2026-10-12): "G8 cleanly showed gains and we should just scale it higher".
Here every rollout runs to the end of the half (GW19 / GW38) and the return is the points over that whole
stretch: an unused chip expires worthless, exactly as in the game, so when to play each chip and in what
order is learned from consequences, with no guessed value for held chips.

Starts: the first week of each training half with all chips, plus FPL_G9_MID_STARTS random mid-half
starts per half with a random subset of chips already used (so "two chips left, eight weeks to go"
states are trained on too). State = the compact advisor prompt + the schedule ahead (double/blank
gameweeks within six weeks) + squad health (src/fpl_ai/g8_state.py, detail "g9"). Initialised from the
G8 compact adapter (FPL_G9_INIT_ADAPTER). Resumable (FPL_G9_RESUME=1) from the checkpoint saved every
FPL_G9_SAVE_EVERY starts.

usage: FPL_PLANNER_DISCIPLINE=1 train_g9_rollout.py [--dry-run]
"""
from __future__ import annotations

import json
import os
import random
import sys
import time
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))
os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")

from fpl_ai.chip_advisor import parse_week_choice  # noqa: E402
from fpl_ai.g8_state import g8_prompt, schedule_ahead  # noqa: E402
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, FIRST_HALF_LAST_WEEK, MAX_HORIZON, PlanEnvV2, chip_half  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

GROUP = int(os.environ.get("FPL_G9_GROUP", "4"))
MID_STARTS = int(os.environ.get("FPL_G9_MID_STARTS", "3"))
EPOCHS = int(os.environ.get("FPL_G9_EPOCHS", "1"))
LR = float(os.environ.get("FPL_G9_LR", "2e-5"))
TEMPERATURE = float(os.environ.get("FPL_G9_TEMPERATURE", "1.0"))
MAX_NEW = int(os.environ.get("FPL_G9_MAX_NEW_TOKENS", "200"))
SAVE_EVERY = int(os.environ.get("FPL_G9_SAVE_EVERY", "5"))
INVALID_PENALTY = 10.0
OUTPUT = Path(os.environ.get("FPL_G9_OUTPUT", ROOT / "artifacts" / "gemma4_e4b_g9"))
INIT_ADAPTER = os.environ.get("FPL_G9_INIT_ADAPTER", str(ROOT / "artifacts" / "gemma4_e4b_g8_compact"))
TRAIN = [("2020-21", None), ("2021-22", None), ("2022-23", None), ("2023-24", FIRST_HALF_LAST_WEEK),
         ("2024-25", None), ("2025-26-train", FIRST_HALF_LAST_WEEK)]


def starts(seed: int = 0):
    """(key, half states, start index, chips already used) — the first week with all chips, then random mid-half starts."""
    rng = random.Random(seed)
    out = []
    for key, last_week in TRAIN:
        states = sorted(load_states(ROOT / "reports" / "grpo_states_v2" / f"{key}.jsonl"), key=lambda s: s.week)
        if last_week is not None:
            states = [s for s in states if s.week <= last_week]
        for half in (1, 2):
            hs = [s for s in states if chip_half(s.week) == half]
            if len(hs) < 6:
                continue
            out.append((key, hs, 0, frozenset()))
            for _ in range(MID_STARTS):
                i = rng.randint(3, len(hs) - 4)
                used = frozenset(rng.sample(CHIPS, rng.randint(1, 3)))
                out.append((key, hs, i, used))
    return out


def fresh_chips(used):
    return {1: frozenset(c for c in CHIPS if c not in used), 2: frozenset(c for c in CHIPS if c not in used)}


def play(hs, i, used, choose):
    """One rollout from hs[i] to the end of the half; choose(env, k, schedule, recent) -> (action, invalid, record)."""
    chips = fresh_chips(used)
    carried, total, invalid, records, recent = None, 0.0, 0, [], []
    for k in range(len(hs) - i):
        state = hs[i + k]
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state] + list(hs[i + k + 1:i + k + MAX_HORIZON]), optimize, chips=chips)
        action, bad, rec = choose(env, k, schedule_ahead(hs, i + k), list(recent))
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([action], return_state=True)
        chips = carried["chips"]
        total += realized
        invalid += bad
        recent.append(realized)
        records.append({**(rec or {}), "chip": detail[0]["chip"], "realized": realized})
    return total - INVALID_PENALTY * invalid, records


def dry_run():
    st = starts()
    print(f"starts {len(st)} (group {GROUP}, mid starts {MID_STARTS}); rollout lengths "
          f"{sorted({len(hs) - i for _, hs, i, _ in st})}; decisions per epoch {sum(len(hs) - i for _, hs, i, _ in st) * GROUP}")
    key, hs, i, used = st[1]
    prompt, facts = g8_prompt(PlanEnvV2(hs[i:i + MAX_HORIZON], optimize, chips=fresh_chips(used)), "g9",
                              schedule=schedule_ahead(hs, i), recent=[55.0, 61.0, 48.0])
    print(f"--- example prompt ({key} GW{hs[i].week}, used {sorted(used)}), {len(prompt)} chars ---\n{prompt}")
    t = time.time()
    planner = play(hs, i, used, lambda env, k, s, r: (env.baseline_plan()[0], 0, None))
    print(f"planner rollout from {key} GW{hs[i].week} to the half end: return {planner[0]:.1f} in {time.time() - t:.1f}s")


def main():
    if "--dry-run" in sys.argv:
        dry_run()
        return
    import torch
    from peft import LoraConfig, PeftModel, get_peft_model, set_peft_model_state_dict
    from safetensors.torch import load_file
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from train_gemma_grpo_plan_v2 import merged_generation

    random.seed(0)
    tok = AutoTokenizer.from_pretrained("google/gemma-4-E4B-it")
    tok.padding_side = "left"
    turn_end = tok.convert_tokens_to_ids("<turn|>")
    model = AutoModelForCausalLM.from_pretrained("google/gemma-4-E4B-it", dtype=torch.bfloat16, device_map={"": 0})
    if INIT_ADAPTER and Path(INIT_ADAPTER, "adapter_model.safetensors").exists():
        model = PeftModel.from_pretrained(model, INIT_ADAPTER, is_trainable=True)
        print(f"initialised from {INIT_ADAPTER}", flush=True)
    else:
        targets = sorted(n for n, _ in model.named_parameters() if n.startswith("model.language_model.layers.")
                         and n.endswith(("self_attn.q_proj.weight", "self_attn.k_proj.weight", "self_attn.v_proj.weight", "self_attn.o_proj.weight")))
        model = get_peft_model(model, LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM",
                                                 target_modules=None, target_parameters=targets))
    done = 0
    if os.environ.get("FPL_G9_RESUME") == "1" and (OUTPUT / "adapter_model.safetensors").exists():
        res = set_peft_model_state_dict(model, load_file(str(OUTPUT / "adapter_model.safetensors")))
        assert not res.unexpected_keys, res.unexpected_keys
        records = [json.loads(l) for l in open(OUTPUT / "train_log.jsonl")] if (OUTPUT / "train_log.jsonl").exists() else []
        done = max((r["step"] for r in records), default=0) // SAVE_EVERY * SAVE_EVERY
        with open(OUTPUT / "train_log.jsonl", "w") as f:
            f.writelines(json.dumps(r) + "\n" for r in records if r["step"] <= done)
        print(f"resumed from checkpoint at start {done}", flush=True)
    model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
    model.enable_input_require_grads()
    merged_generation(model)
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=LR)
    OUTPUT.mkdir(parents=True, exist_ok=True)
    log = open(OUTPUT / "train_log.jsonl", "a")
    plan = starts()
    if os.environ.get("FPL_G9_MAX_STARTS"):
        plan = plan[: int(os.environ["FPL_G9_MAX_STARTS"])]

    for epoch in range(EPOCHS):
        random.shuffle(plan)
        for n, (key, hs, i, used) in enumerate(plan, start=1):
            if epoch == 0 and n <= done:
                continue
            t0 = time.time()
            length = len(hs) - i
            # --- G rollouts in lockstep to the end of the half: each week, generate for all G ---
            chips = [fresh_chips(used) for _ in range(GROUP)]
            carried = [None] * GROUP
            totals, invalid = [0.0] * GROUP, [0] * GROUP
            decisions = [[] for _ in range(GROUP)]
            chip_log = [[] for _ in range(GROUP)]
            recent = [[] for _ in range(GROUP)]
            model.eval()
            for k in range(length):
                envs, prompts, facts = [], [], []
                sched = schedule_ahead(hs, i + k)
                for g in range(GROUP):
                    state = hs[i + k] if carried[g] is None else replace(hs[i + k], squad=carried[g]["squad"],
                                                                         bank=carried[g]["bank"], free_transfers=carried[g]["free_transfers"])
                    env = PlanEnvV2([state] + list(hs[i + k + 1:i + k + MAX_HORIZON]), optimize, chips=chips[g])
                    p, f = g8_prompt(env, "g9", schedule=sched, recent=recent[g][-3:])
                    envs.append((env, state)); facts.append(f)
                    prompts.append(tok.apply_chat_template([{"role": "user", "content": p}], tokenize=False, add_generation_prompt=True))
                enc = tok(prompts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
                with torch.no_grad():
                    out = model.generate(**enc, max_new_tokens=MAX_NEW, do_sample=True, temperature=TEMPERATURE,
                                         top_p=1.0, top_k=0, eos_token_id=[turn_end, tok.eos_token_id], pad_token_id=tok.pad_token_id)
                L = enc["input_ids"].shape[1]
                for g in range(GROUP):
                    prompt_ids = enc["input_ids"][g][enc["attention_mask"][g].bool()].tolist()
                    comp = out[g, L:].tolist()
                    if turn_end in comp:
                        comp = comp[:comp.index(turn_end) + 1]
                    comp = [c for c in comp if c != tok.pad_token_id] or [turn_end]
                    text = tok.decode(comp, skip_special_tokens=True)
                    env, state = envs[g]
                    action = parse_week_choice(text, facts[g])
                    if action is None:
                        invalid[g] += 1
                        action = env.baseline_plan()[0]
                    realized, detail, carried[g] = PlanEnvV2([state], optimize, chips=chips[g]).rollout([action], return_state=True)
                    chips[g] = carried[g]["chips"]
                    totals[g] += realized
                    recent[g].append(realized)
                    decisions[g].append((prompt_ids, comp))
                    chip_log[g].append(detail[0]["chip"])
            returns = [totals[g] - INVALID_PENALTY * invalid[g] for g in range(GROUP)]
            planner_return = play(hs, i, used, lambda env, k, s, r: (env.baseline_plan()[0], 0, None))[0]
            mean = sum(returns) / GROUP
            std = (sum((r - mean) ** 2 for r in returns) / GROUP) ** 0.5
            # --- policy gradient: advantage x mean token log-prob, every decision of each rollout ---
            if std > 1e-6:
                model.train()
                n_tok = sum(len(c) for g in range(GROUP) for _, c in decisions[g])
                for g in range(GROUP):
                    adv = (returns[g] - mean) / std
                    for prompt_ids, comp in decisions[g]:
                        ids = torch.tensor([prompt_ids + comp], device=model.device)
                        logits = model(input_ids=ids, mm_token_type_ids=torch.zeros_like(ids),
                                       logits_to_keep=len(comp) + 1).logits[0, :-1].float()
                        logp = torch.log_softmax(logits, -1).gather(-1, torch.tensor(comp, device=model.device)[:, None]).sum()
                        (-adv * logp / n_tok).backward()
                torch.nn.utils.clip_grad_norm_([p for p in model.parameters() if p.requires_grad], 1.0)
                opt.step()
                opt.zero_grad(set_to_none=True)
            rec = {"epoch": epoch, "step": n, "start": f"{key}:{hs[i].week}", "used": sorted(used), "length": length,
                   "returns": [round(r, 1) for r in returns], "mean": round(mean, 1), "planner": round(planner_return, 1),
                   "vs_planner": round(mean - planner_return, 1), "invalid": invalid,
                   "chips": [[(hs[i + k].week, c) for k, c in enumerate(cl) if c != "none"] for cl in chip_log], "seconds": round(time.time() - t0)}
            log.write(json.dumps(rec) + "\n"); log.flush()
            print(f"[{n}/{len(plan)}] {rec['start']} used {rec['used']} len {length}: mean {mean:.1f} vs planner {planner_return:.1f} "
                  f"({mean - planner_return:+.1f}) | invalid {sum(invalid)} | chips {rec['chips'][0]} | {rec['seconds']}s", flush=True)
            if n % SAVE_EVERY == 0:
                model.save_pretrained(OUTPUT)
    model.save_pretrained(OUTPUT)
    tok.save_pretrained(OUTPUT)
    print("G9 TRAINING DONE", flush=True)


if __name__ == "__main__":
    main()

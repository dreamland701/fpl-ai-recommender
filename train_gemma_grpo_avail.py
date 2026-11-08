#!/usr/bin/env python3
"""R4: GRPO on the availability question with the Brier-improvement reward (src/fpl_ai/avail_rl.py).
Env: FPL_R4_SPLIT (train.jsonl dir), FPL_R4_OUTPUT, FPL_R4_MAX_PROMPTS (1200), FPL_R4_NUM_GEN (6), FPL_R4_LR (1e-5),
FPL_R4_TEMPERATURE (1.0), FPL_R4_KL_BETA (0.04), FPL_R4_MAX_COMPLETION (96), FPL_R4_GRAD_ACCUM (2), FPL_R4_SAVE_STEPS (50).
FPL_R4_MAX_PROMPT_TOKENS (1400): prompts above it are dropped (TRL 1.0 has no max_prompt_length).
CPU dry run: --dry-run (prompt/reward invariants on 20 rows)."""
from __future__ import annotations

import json
import os
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai import avail_rl as AR  # noqa: E402
from fpl_ai.reghead import MODEL, MODULE_REGEX  # noqa: E402

SPLIT = Path(os.environ.get("FPL_R4_SPLIT", ROOT / "reports/llm_residual_v2_e22_top96_thru_2526_26_eval_2526_27_38"))
OUT = Path(os.environ.get("FPL_R4_OUTPUT", ROOT / "artifacts/gemma4_e4b_r4_avail_grpo"))
MAX_PROMPTS = int(os.environ.get("FPL_R4_MAX_PROMPTS", "1200")); NUM_GEN = int(os.environ.get("FPL_R4_NUM_GEN", "6"))
LR = float(os.environ.get("FPL_R4_LR", "1e-5")); TEMP = float(os.environ.get("FPL_R4_TEMPERATURE", "1.0"))
BETA = float(os.environ.get("FPL_R4_KL_BETA", "0.04")); MAXC = int(os.environ.get("FPL_R4_MAX_COMPLETION", "96"))
ACCUM = int(os.environ.get("FPL_R4_GRAD_ACCUM", "2")); SAVE = int(os.environ.get("FPL_R4_SAVE_STEPS", "50"))
TRACE = Path(os.environ.get("FPL_R4_TRACE", ROOT / "logs/r4_reward_trace.jsonl"))


def build_rows(seed: int = 11):
    rows = []
    for l in open(SPLIT / "train.jsonl"):
        r = json.loads(l); m = r["metadata"]
        b = float(m["baseline_forecast"]["baseline_appearance_probability"])
        if not AR.text_could_matter(m) or not 0.05 <= b <= 0.97:
            continue
        rows.append({"prompt": AR.availability_prompt(r["prompt"], b), "y": float(m["labels"]["appearance_probability"] > 0.5), "b": b,
                     "key": f"{m['season']}:{m['week']}:{m['player_id']}"})
    random.Random(seed).shuffle(rows)
    return rows[:MAX_PROMPTS]


def make_reward():
    trace = open(TRACE, "a")

    def brier_improvement(prompts, completions, y, b, key, **kwargs):
        out = []
        for c, yy, bb, k in zip(completions, y, b, key):
            text = c if isinstance(c, str) else c[0]["content"]
            r = AR.brier_reward(text, float(yy), float(bb)); out.append(r["reward"])
            trace.write(json.dumps({"key": k, "y": yy, "b": bb, "p": r["p"], "reward": r["reward"], "ok": r["ok"]}) + "\n")
        trace.flush()
        return out
    brier_improvement.__name__ = "brier_improvement"
    return brier_improvement


def dry_run():
    rows = build_rows()
    print(f"{len(rows)} prompts; played share {sum(r['y'] for r in rows) / len(rows):.3f}; mean baseline {sum(r['b'] for r in rows) / len(rows):.3f}")
    print(rows[0]["prompt"][-900:])
    f = make_reward()
    print("rewards:", f(["x"] * 3, ['{"reasoning": "fit", "p_play": 0.9}', '{"reasoning": "out", "p_play": 0.1}', "no json"], [1.0] * 3, [0.6] * 3, ["k"] * 3))


def main():
    if "--dry-run" in sys.argv:
        dry_run(); return
    import torch
    from datasets import Dataset
    from peft import LoraConfig
    from transformers import AutoModelForCausalLM, AutoTokenizer
    from trl import GRPOConfig, GRPOTrainer
    try:
        open(f"/proc/{os.getpid()}/oom_score_adj", "w").write("800")
    except OSError:
        pass
    rows = build_rows()
    print(f"{len(rows)} prompts", flush=True)
    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, extra_special_tokens={})
    # TRL 1.0 has no max_prompt_length (2026-10-15 fix): bound the prompts by construction and assert the bound.
    maxtok = int(os.environ.get("FPL_R4_MAX_PROMPT_TOKENS", "1400"))
    lens = [len(tok(r["prompt"])["input_ids"]) for r in rows]
    rows = [r for r, n in zip(rows, lens) if n <= maxtok]
    print(f"prompt tokens max {max(lens)} mean {sum(lens) / len(lens):.0f}; kept {len(rows)} <= {maxtok}", flush=True)
    assert rows and max(n for n in lens if n <= maxtok) <= 1536
    model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, attn_implementation="sdpa")
    peft_config = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=MODULE_REGEX)
    args = GRPOConfig(output_dir=str(OUT), num_generations=NUM_GEN, per_device_train_batch_size=NUM_GEN, gradient_accumulation_steps=ACCUM,
                      learning_rate=LR, num_train_epochs=1, temperature=TEMP, beta=BETA, max_completion_length=MAXC,
                      logging_steps=1, save_steps=SAVE, save_total_limit=2, bf16=True, report_to="none", gradient_checkpointing=True)
    trainer = GRPOTrainer(model=model, reward_funcs=make_reward(), args=args, train_dataset=Dataset.from_list(rows), processing_class=tok,
                          peft_config=peft_config)
    t0 = time.time(); trainer.train(resume_from_checkpoint=os.environ.get("FPL_R4_RESUME")); trainer.save_model(str(OUT)); tok.save_pretrained(str(OUT))
    print(f"DONE {OUT} in {(time.time() - t0) / 3600:.2f} h", flush=True)


if __name__ == "__main__":
    main()

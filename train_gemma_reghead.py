#!/usr/bin/env python3
"""H-series trainer: LoRA backbone + regression head on the residual-forecast corpus (src/fpl_ai/reghead.py).

Env: FPL_RH_DATA_DIR (split dir with train.jsonl), FPL_RH_OUTPUT_DIR, FPL_RH_LORA_MODE=modules|params,
FPL_RH_BATCH, FPL_RH_ACCUM, FPL_RH_CKPT=1, FPL_RH_LR, FPL_RH_HEAD_LR, FPL_RH_EPOCHS, FPL_RH_MAX_STEPS,
FPL_RH_MAXLEN, FPL_RH_SAVE_STEPS, FPL_RH_MAX_ROWS, FPL_RH_FIELDS=all|availability (loss on P(appear) only),
FPL_RH_COMPACT=1 (strip the output-format instructions from the prompt).
FPL_RH_LOSS=huber|mse (points/minutes head loss on standardised residuals; mse = mean-targeting), FPL_RH_HUBER_DELTA (1.0).
"""
from __future__ import annotations

import json
import math
import os
import random
import re
import sys
import time
from pathlib import Path

import torch
import torch.nn.functional as F
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai import reghead as RH  # noqa: E402

DATA = Path(os.environ["FPL_RH_DATA_DIR"]); OUT = Path(os.environ["FPL_RH_OUTPUT_DIR"])
MODEL = os.environ.get("FPL_RH_MODEL", RH.MODEL)
LORA_MODE = os.environ.get("FPL_RH_LORA_MODE", "modules")
BS = int(os.environ.get("FPL_RH_BATCH", "2")); ACCUM = int(os.environ.get("FPL_RH_ACCUM", "8"))
CKPT = os.environ.get("FPL_RH_CKPT", "1") == "1"
LR = float(os.environ.get("FPL_RH_LR", "5e-5")); HEAD_LR = float(os.environ.get("FPL_RH_HEAD_LR", "5e-4"))
EPOCHS = float(os.environ.get("FPL_RH_EPOCHS", "1")); MAX_STEPS = int(os.environ.get("FPL_RH_MAX_STEPS", "-1"))
MAXLEN = int(os.environ.get("FPL_RH_MAXLEN", "1536")); SAVE_STEPS = int(os.environ.get("FPL_RH_SAVE_STEPS", "200"))
MAX_ROWS = int(os.environ.get("FPL_RH_MAX_ROWS", "0")); FIELDS = os.environ.get("FPL_RH_FIELDS", "all")
COMPACT = os.environ.get("FPL_RH_COMPACT", "1") == "1"; SEED = int(os.environ.get("FPL_RH_SEED", "7"))
WARMUP = int(os.environ.get("FPL_RH_WARMUP", "30"))
LOSS = os.environ.get("FPL_RH_LOSS", "huber")  # huber (H1-H4: median-like shrink) | mse (mean-targeting, H5 2026-10-25)
HUBER_DELTA = float(os.environ.get("FPL_RH_HUBER_DELTA", "1.0"))
# 2026-10-18 (31B capacity run under the 55 GB one-job rule): FPL_RH_4BIT=1 loads the backbone in bitsandbytes nf4
# (double quant, bf16 compute) and prepares it for k-bit LoRA training; the head and LoRA stay bf16/fp32.
FOURBIT = os.environ.get("FPL_RH_4BIT", "0") == "1"
LOSS_W = [1.0, 1.0, 1.0, 0.5]; APP_W = 2.0


def log(msg):
    print(f"{time.strftime('%F %T')} {msg}", flush=True)


def main():
    try:
        open(f"/proc/{os.getpid()}/oom_score_adj", "w").write("800")
    except OSError:
        pass
    random.seed(SEED); torch.manual_seed(SEED)
    rows = [json.loads(l) for l in open(DATA / "train.jsonl") if l.strip()]
    random.shuffle(rows)
    if MAX_ROWS > 0:
        rows = rows[:MAX_ROWS]
    targets = [RH.targets_from_metadata(r["metadata"]) for r in rows]
    std = RH.Standardiser.fit(targets)
    log(f"{len(rows)} rows; residual means {[round(m, 3) for m in std.mean]} stds {[round(s, 3) for s in std.std]}; "
        f"played share {sum(t['appearance'] for t in targets) / len(targets):.3f}")
    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, extra_special_tokens={})
    pad = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    enc = [tok(RH.compact_prompt(r["prompt"]) if COMPACT else r["prompt"], add_special_tokens=False)["input_ids"][:MAXLEN] for r in rows]
    log(f"tokens mean {sum(map(len, enc)) / len(enc):.0f} max {max(map(len, enc))}")
    load_kw = dict(dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, attn_implementation="sdpa")
    if FOURBIT:
        from transformers import BitsAndBytesConfig
        load_kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                                            bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(MODEL, **load_kw)
    model.config.use_cache = False
    if FOURBIT:
        from peft import prepare_model_for_kbit_training
        model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=CKPT,
                                                gradient_checkpointing_kwargs={"use_reentrant": False})
        log(f"4-bit backbone loaded: {torch.cuda.memory_allocated() / 1e9:.1f} GB allocated")
    if LORA_MODE == "params":
        tp = sorted(n for n, _ in model.named_parameters() if n.startswith("model.language_model.layers.") and re.search(RH.SUFFIX + r"\.weight$", n))
        cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=None, target_parameters=tp)
    else:
        cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=RH.MODULE_REGEX)
    model = get_peft_model(model, cfg)
    if CKPT:
        model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
        model.enable_input_require_grads()
    needs_mm = RH.needs_mm_ids(model)
    hidden = model.config.get_text_config().hidden_size if hasattr(model.config, "get_text_config") else model.config.hidden_size
    head = RH.RegHead(hidden).to(model.device)
    lora_params = [p for p in model.parameters() if p.requires_grad]
    log(f"LoRA {LORA_MODE}: {sum(p.numel() for p in lora_params) / 1e6:.1f}M params; head {sum(p.numel() for p in head.parameters()) / 1e3:.1f}K; hidden {hidden}")
    opt = torch.optim.AdamW([{"params": lora_params, "lr": LR}, {"params": head.parameters(), "lr": HEAD_LR}], weight_decay=0.0)
    steps_per_epoch = math.ceil(len(rows) / (BS * ACCUM))
    total = MAX_STEPS if MAX_STEPS > 0 else math.ceil(steps_per_epoch * EPOCHS)
    sched = torch.optim.lr_scheduler.LambdaLR(opt, lambda s: min(1.0, (s + 1) / WARMUP) * 0.5 * (1 + math.cos(math.pi * min(s, total) / total)))
    log(f"optimizer steps {total} (batch {BS} x accum {ACCUM}, ckpt {CKPT})")
    model.train(); head.train()
    dev = model.device; step = 0; micro = 0; t0 = time.time(); acc = {"reg": 0.0, "app": 0.0, "n": 0}
    order = list(range(len(rows)))
    epoch = 0
    while step < total:
        for i in range(0, len(order), BS):
            idx = order[i:i + BS]
            L = max(len(enc[j]) for j in idx)
            ids = torch.tensor([enc[j] + [pad] * (L - len(enc[j])) for j in idx], device=dev)
            att = torch.tensor([[1] * len(enc[j]) + [0] * (L - len(enc[j])) for j in idx], device=dev)
            z = torch.tensor([std.encode(targets[j]) for j in idx], device=dev)
            y = torch.tensor([targets[j]["appearance"] for j in idx], device=dev)
            off = torch.tensor([RH.logit(targets[j]["baseline_appearance"]) for j in idx], device=dev)
            h = RH.backbone_hidden(model, ids, att, needs_mm)
            out = head(h)
            w = torch.tensor(LOSS_W, device=dev)
            reg_el = F.mse_loss(out[:, :4], z, reduction="none") if LOSS == "mse" else F.huber_loss(out[:, :4], z, reduction="none", delta=HUBER_DELTA)
            reg = (reg_el * w).sum(1).mean()
            app = F.binary_cross_entropy_with_logits(out[:, 4] + off, y)
            loss = (app * APP_W) if FIELDS == "availability" else (reg + APP_W * app)
            (loss / ACCUM).backward()
            acc["reg"] += reg.item(); acc["app"] += app.item(); acc["n"] += 1
            micro += 1
            if micro % ACCUM == 0:
                torch.nn.utils.clip_grad_norm_(lora_params + list(head.parameters()), 1.0)
                opt.step(); sched.step(); opt.zero_grad(set_to_none=True); step += 1
                if step % 10 == 0 or step == 1:
                    el = time.time() - t0
                    log(f"step {step}/{total} reg {acc['reg'] / acc['n']:.4f} app {acc['app'] / acc['n']:.4f} lr {sched.get_last_lr()[0]:.2e} "
                        f"{el / step:.1f}s/step eta {(total - step) * el / step / 3600:.2f}h peak {torch.cuda.max_memory_allocated() / 1e9:.1f}G")
                    acc = {"reg": 0.0, "app": 0.0, "n": 0}
                if step % SAVE_STEPS == 0:
                    ck = OUT / f"checkpoint-{step}"; model.save_pretrained(ck); RH.save_head(head, std, ck, {"step": step})
                    for old in sorted(OUT.glob("checkpoint-*"), key=lambda p: int(p.name.split("-")[1]))[:-2]:
                        import shutil; shutil.rmtree(old, ignore_errors=True)
                if step >= total:
                    break
        epoch += 1
        random.shuffle(order)
    model.save_pretrained(OUT); tok.save_pretrained(OUT)
    RH.save_head(head, std, OUT, {"step": step, "model": MODEL, "lora_mode": LORA_MODE, "compact": COMPACT, "fields": FIELDS,
                                  "rows": len(rows), "batch": BS, "accum": ACCUM, "lr": LR, "head_lr": HEAD_LR})
    log(f"DONE: {OUT} ({step} steps, {(time.time() - t0) / 3600:.2f} h)")


if __name__ == "__main__":
    main()

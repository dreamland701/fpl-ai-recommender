"""Throughput probe for E4B LoRA training: target_parameters (ParamWrapper, ~1.4 s/call overhead) vs
module-level target_modules LoRA, at several batch sizes, with and without gradient checkpointing.
Each config: fresh model, 2 warm-up + 8 timed optimizer steps on real E21 prompt/completion rows.
usage: probe_lora_throughput.py <train.jsonl> [config,config,...]   (writes one JSON line per config)"""
import gc, inspect, json, os, re, sys, time
import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "google/gemma-4-E4B-it"
MAXLEN = 1536
SUFFIX = r"(self_attn\.(q|k|v|o)_proj|mlp\.(gate|up|down)_proj)"
MODULE_REGEX = r"model\.language_model\.layers\.\d+\." + SUFFIX
CONFIGS = {  # name: (mode, batch, checkpointing)
    "modules_b1_ckpt": ("modules", 1, True), "params_b1_ckpt": ("params", 1, True),
    "modules_b2_ckpt": ("modules", 2, True), "modules_b4_ckpt": ("modules", 4, True),
    "modules_b2_nockpt": ("modules", 2, False), "modules_b4_nockpt": ("modules", 4, False),
}


def main():
    rows = [json.loads(l) for l in open(sys.argv[1]) if l.strip()][:80]
    names = sys.argv[2].split(",") if len(sys.argv) > 2 else list(CONFIGS)
    try:
        open(f"/proc/{os.getpid()}/oom_score_adj", "w").write("800")
    except OSError:
        pass
    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, extra_special_tokens={})
    pad = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    enc = []
    for r in rows:
        p = tok(r["prompt"], add_special_tokens=False)["input_ids"]
        c = tok(r["completion"] + "<turn|>", add_special_tokens=False)["input_ids"]
        ids = (p + c)[:MAXLEN]; lab = ([-100] * len(p) + c)[:MAXLEN]
        enc.append((ids, lab))
    print(f"rows {len(enc)} mean tokens {sum(len(i) for i, _ in enc) / len(enc):.0f} max {max(len(i) for i, _ in enc)}", flush=True)
    for name in names:
        mode, bs, ckpt = CONFIGS[name]
        gc.collect(); torch.cuda.empty_cache(); torch.cuda.reset_peak_memory_stats()
        model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto",
                                                     trust_remote_code=True, attn_implementation="sdpa")
        model.config.use_cache = False
        needs_mm = "mm_token_type_ids" in inspect.signature(model.forward).parameters
        if mode == "params":
            tp = sorted(n for n, _ in model.named_parameters() if n.startswith("model.language_model.layers.")
                        and re.search(SUFFIX + r"\.weight$", n))
            cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=None, target_parameters=tp)
        else:
            cfg = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.0, task_type="CAUSAL_LM", target_modules=MODULE_REGEX)
        model = get_peft_model(model, cfg)
        if ckpt:
            model.gradient_checkpointing_enable(gradient_checkpointing_kwargs={"use_reentrant": False})
            model.enable_input_require_grads()
        trainable = [p for p in model.parameters() if p.requires_grad]
        print(f"{name}: trainable params {sum(p.numel() for p in trainable) / 1e6:.1f}M", flush=True)
        opt = torch.optim.AdamW(trainable, lr=5e-5)
        model.train()
        times = []; toks = 0; ok = True
        try:
            for step in range(10):
                batch = enc[(step * bs) % len(enc):(step * bs) % len(enc) + bs]
                L = max(len(i) for i, _ in batch)
                ids = torch.tensor([i + [pad] * (L - len(i)) for i, _ in batch], device=model.device)
                lab = torch.tensor([l + [-100] * (L - len(l)) for _, l in batch], device=model.device)
                att = (ids != pad).long()
                kw = dict(input_ids=ids, attention_mask=att, labels=lab)
                if needs_mm:
                    kw["mm_token_type_ids"] = torch.zeros_like(ids)
                torch.cuda.synchronize(); t0 = time.time()
                out = model(**kw); out.loss.backward(); opt.step(); opt.zero_grad(set_to_none=True)
                torch.cuda.synchronize(); dt = time.time() - t0
                if step >= 2:
                    times.append(dt); toks += int(att.sum())
                print(f"  step {step} {dt:.2f}s loss {out.loss.item():.3f} L {L}", flush=True)
        except Exception as e:  # noqa: BLE001
            ok = False; print(f"{name} FAILED: {type(e).__name__}: {str(e)[:200]}", flush=True)
        res = {"config": name, "ok": ok, "s_per_step": round(sum(times) / max(len(times), 1), 2),
               "s_per_sample": round(sum(times) / max(len(times) * bs, 1), 2), "tok_per_s": round(toks / max(sum(times), 1e-9)),
               "peak_gb": round(torch.cuda.max_memory_allocated() / 1e9, 1)}
        print("RESULT " + json.dumps(res), flush=True)
        del model, opt, trainable; gc.collect(); torch.cuda.empty_cache()


if __name__ == "__main__":
    main()

"""Predict residual deltas with a regression-head adapter; output has the decoder's record shape.
usage: reghead_predict.py <examples.jsonl> <adapter_dir> <out.jsonl> [batch]"""
import json
import os
import sys
import time
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fpl_ai import reghead as RH  # noqa: E402


def main():
    ex_path, adapter, out_path = sys.argv[1:4]
    bs = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    rows = [json.loads(l) for l in open(ex_path) if l.strip()]
    cfg = json.loads((Path(adapter) / "head.json").read_text())
    model_name = cfg.get("model", RH.MODEL); compact = cfg.get("compact", True)
    tok = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True, extra_special_tokens={})
    pad = tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    load_kw = dict(dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, attn_implementation="sdpa")
    fourbit = os.environ.get("FPL_RH_4BIT", "0") == "1"  # 2026-10-18: 31B adapter; LoRA stays unmerged on a 4-bit base
    if fourbit:
        from transformers import BitsAndBytesConfig
        load_kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(model_name, **load_kw)
    model = PeftModel.from_pretrained(model, adapter)
    model = (model if fourbit else model.merge_and_unload()).eval()
    head, std, _ = RH.load_head(Path(adapter), model.device)
    needs_mm = RH.needs_mm_ids(model)
    enc = [tok(RH.compact_prompt(r["prompt"]) if compact else r["prompt"], add_special_tokens=False)["input_ids"][:1536] for r in rows]
    order = sorted(range(len(rows)), key=lambda i: len(enc[i]))
    outs = [None] * len(rows); t0 = time.time()
    with torch.no_grad():
        for s in range(0, len(order), bs):
            idx = order[s:s + bs]; L = max(len(enc[i]) for i in idx)
            ids = torch.tensor([enc[i] + [pad] * (L - len(enc[i])) for i in idx], device=model.device)
            att = torch.tensor([[1] * len(enc[i]) + [0] * (L - len(enc[i])) for i in idx], device=model.device)
            o = head(RH.backbone_hidden(model, ids, att, needs_mm)).float().cpu().tolist()
            for i, v in zip(idx, o):
                outs[i] = v
            if (s // bs) % 20 == 0:
                print(f"{s + len(idx)}/{len(rows)} {(time.time() - t0) / (s + len(idx)):.2f}s/row", flush=True)
    with open(out_path, "w") as f:
        for r, o in zip(rows, outs):
            m = r["metadata"]
            d = RH.deltas_from_output(o, float(m["baseline_forecast"]["baseline_appearance_probability"]), std)
            f.write(json.dumps({"season": r["season"], "week": r["week"], "response": json.dumps(d), "metadata": m}, ensure_ascii=False) + "\n")
    print(f"wrote {len(rows)} rows -> {out_path} ({(time.time() - t0) / 60:.1f} min)")


if __name__ == "__main__":
    main()

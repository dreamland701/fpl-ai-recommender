"""Greedy availability answers for eval rows: zero-shot base, an R4 adapter, or the 31B reader.
usage: avail_policy_eval.py <examples.jsonl> <out.jsonl> [--adapter DIR] [--model PATH] [--4bit] [--batch N] [--subset all|matter]
Writes one row per example: key, y, b (classic), p (policy), ok, reasoning; prints AUC/Brier for classic vs policy."""
import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import brier_score_loss, roc_auc_score
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from fpl_ai import avail_rl as AR  # noqa: E402
from fpl_ai.reghead import MODEL  # noqa: E402


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("examples"); ap.add_argument("out"); ap.add_argument("--adapter"); ap.add_argument("--model", default=MODEL)
    ap.add_argument("--4bit", dest="four", action="store_true"); ap.add_argument("--batch", type=int, default=8); ap.add_argument("--subset", default="all")
    ap.add_argument("--max-new-tokens", type=int, default=96); ap.add_argument("--resume", action="store_true")
    a = ap.parse_args()
    rows = []
    for l in open(a.examples):
        r = json.loads(l); m = r["metadata"]
        if a.subset == "matter" and not AR.text_could_matter(m):
            continue
        b = float(m["baseline_forecast"]["baseline_appearance_probability"])
        rows.append({"key": f"{m['season']}:{m['week']}:{m['player_id']}", "name": m["player_name"], "y": float(m["labels"]["appearance_probability"] > 0.5), "b": b,
                     "status": m.get("status_pre_deadline") or "", "prompt": AR.availability_prompt(r["prompt"], b)})
    done = {}
    if a.resume and Path(a.out).exists():
        done = {json.loads(l)["key"]: json.loads(l) for l in open(a.out) if l.strip()}
    todo = [r for r in rows if r["key"] not in done]
    print(f"{len(rows)} rows, {len(todo)} to decode", flush=True)
    tok = AutoTokenizer.from_pretrained(a.model, trust_remote_code=True, extra_special_tokens={}); tok.padding_side = "left"
    kw = dict(dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, attn_implementation="sdpa")
    if a.four:
        kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)
    model = AutoModelForCausalLM.from_pretrained(a.model, **kw)
    if a.adapter:
        from peft import PeftModel
        model = PeftModel.from_pretrained(model, a.adapter).merge_and_unload()
    model.eval()
    t0 = time.time()
    with open(a.out, "a" if a.resume else "w") as f, torch.no_grad():
        todo.sort(key=lambda r: len(r["prompt"]))
        for s in range(0, len(todo), a.batch):
            batch = todo[s:s + a.batch]
            enc = tok([r["prompt"] for r in batch], return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            gen = model.generate(**enc, max_new_tokens=a.max_new_tokens, do_sample=False)
            texts = tok.batch_decode(gen[:, enc["input_ids"].shape[1]:], skip_special_tokens=True)
            for r, t in zip(batch, texts):
                res = AR.brier_reward(t, r["y"], r["b"])
                rec = {k: r[k] for k in ("key", "name", "y", "b", "status")}; rec.update({"p": res["p"], "ok": res["ok"], "reward": res["reward"], "text": t[:400]})
                f.write(json.dumps(rec, ensure_ascii=False) + "\n"); done[r["key"]] = rec
            f.flush()
            if (s // a.batch) % 10 == 0:
                print(f"{s + len(batch)}/{len(todo)} {(time.time() - t0) / (s + len(batch)):.2f}s/row", flush=True)
    recs = [done[r["key"]] for r in rows if r["key"] in done]
    y = np.array([r["y"] for r in recs]); b = np.array([r["b"] for r in recs])
    p = np.array([r["p"] if r["ok"] else r["b"] for r in recs]); ok = np.mean([r["ok"] for r in recs])
    unc = (b > 0.15) & (b < 0.95)
    def auc(yy, pp):
        return roc_auc_score(yy, pp) if len(yy) > 10 and 0 < yy.mean() < 1 else float("nan")
    print(f"AVAIL-POLICY {Path(a.out).name}: n {len(recs)} parsed {ok:.3f} played {y.mean():.3f} | AUC classic {auc(y, b):.4f} policy {auc(y, p):.4f} | "
          f"Brier classic {brier_score_loss(y, b):.4f} policy {brier_score_loss(y, p):.4f} | uncertain {unc.sum()}: AUC {auc(y[unc], b[unc]):.4f} -> {auc(y[unc], p[unc]):.4f}, "
          f"Brier {brier_score_loss(y[unc], b[unc]) if unc.sum() else float('nan'):.4f} -> {brier_score_loss(y[unc], p[unc]) if unc.sum() else float('nan'):.4f}", flush=True)


if __name__ == "__main__":
    main()

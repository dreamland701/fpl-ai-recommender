"""GPU check for train_gemma_grpo_plan_v2.merged_generation (not part of the CPU test suite).

With a trained target_parameters LoRA adapter loaded as trainable (as in GRPO):
  1. merged-weight greedy generation must equal the normal (unmerged) generation, token for token;
  2. every base weight must be bit-identical afterwards;
  3. the unmerged training forward must give the same logits before and after;
and it reports the speed of both.

usage: python tests/gpu_check_merged_generation.py [adapter_dir]
"""
import json
import sys
import time
from pathlib import Path

import torch
from peft import PeftModel
from peft.tuners.lora.layer import ParamWrapper
from transformers import AutoModelForCausalLM, AutoTokenizer

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from train_gemma_grpo_plan_v2 import merged_generation  # noqa: E402

adapter = sys.argv[1] if len(sys.argv) > 1 else str(ROOT / "artifacts/gemma4_e4b_lora_residual_v2_e20_contract")
tok = AutoTokenizer.from_pretrained("google/gemma-4-E4B-it")
model = AutoModelForCausalLM.from_pretrained("google/gemma-4-E4B-it", dtype=torch.bfloat16, device_map="auto")
model = PeftModel.from_pretrained(model, adapter, is_trainable=True)
prompt = json.loads(open(ROOT / "reports/live_gw6_2627_f6_examples.jsonl").readline())["prompt"]
enc = tok([prompt], return_tensors="pt").to(model.device)
wrappers = [m for m in model.modules() if isinstance(m, ParamWrapper)]
before = [getattr(m.get_base_layer(), m.parameter_name).data.clone() for m in wrappers]

with torch.no_grad():
    logits_before = model(**enc).logits[0, -1].float()
    t = time.time()
    plain = model.generate(**enc, max_new_tokens=40, do_sample=False)
    t_plain = time.time() - t
n = merged_generation(model)
with torch.no_grad():
    t = time.time()
    fast = model.generate(**enc, max_new_tokens=40, do_sample=False)
    t_fast = time.time() - t
    logits_after = model(**enc).logits[0, -1].float()

same_tokens = torch.equal(plain, fast)
restored = all(torch.equal(getattr(m.get_base_layer(), m.parameter_name).data, w) for m, w in zip(wrappers, before))
not_merged = all(not m.merged for m in wrappers)
same_logits = torch.equal(logits_before, logits_after)
print(f"{n} wrapped weights | generation: unmerged {t_plain:.1f}s, merged {t_fast:.1f}s")
print("same tokens:", same_tokens, "| base weights bit-identical:", restored, "| unmerged afterwards:", not_merged,
      "| training-path logits unchanged:", same_logits)
print("text:", tok.decode(fast[0, enc["input_ids"].shape[1]:], skip_special_tokens=True)[:100])
assert same_tokens and restored and not_merged and same_logits
print("MERGED GENERATION CHECK PASSED")

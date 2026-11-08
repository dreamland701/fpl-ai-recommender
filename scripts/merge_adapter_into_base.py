#!/usr/bin/env python3
"""Merge a LoRA adapter into base Gemma weights and save a full model dir.

G4 needs this: TRL's GRPOTrainer computes the KL reference with the PEFT
adapter DISABLED, i.e. against whatever model it was given. Training a
fresh LoRA on top of base Gemma would anchor to base, not to E11. Merging
E11 first makes "adapter disabled" == E11, so KL keeps deltas residual to
the champion forecaster (the G2-v2b stacking pattern).
"""
import argparse, torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

p = argparse.ArgumentParser()
p.add_argument("--base", default="google/gemma-4-E4B-it")
p.add_argument("--adapter", required=True)
p.add_argument("--output", required=True)
a = p.parse_args()
model = AutoModelForCausalLM.from_pretrained(a.base, torch_dtype=torch.bfloat16, device_map="auto")
model = PeftModel.from_pretrained(model, a.adapter).merge_and_unload()
model.save_pretrained(a.output, safe_serialization=True)
AutoTokenizer.from_pretrained(a.base).save_pretrained(a.output)
print("merged ->", a.output)

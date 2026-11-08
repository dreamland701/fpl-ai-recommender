"""Regression-head forecaster on the LLM backbone (H-series, 2026-10-15).

The token-trained adapters are median estimators (greedy decode = mode) and need ~3.5 s/row expectation
decoding to recover a mean. Here the backbone (Gemma-4-E4B + LoRA) reads the same prompt, and a small head on
the final hidden state predicts the five residuals directly: Huber loss on standardised point/minute deltas
(mean-targeted), and a logit offset on the classic P(appear) trained with cross-entropy. One forward pass per
row at inference, so the real decision bench is affordable.
"""
from __future__ import annotations

import inspect
import json
import math
import re
from pathlib import Path
from typing import Dict, List, Sequence

import torch
from torch import nn

MODEL = "google/gemma-4-E4B-it"
REG_FIELDS: List[tuple] = [("delta_points_1gw", 2.0), ("delta_points_3gw", 4.0), ("delta_points_5gw", 6.0), ("delta_minutes_1gw", 20.0)]
APP_FIELD = "delta_appearance_probability"
APP_BOUND = 0.25
N_OUT = len(REG_FIELDS) + 1
SUFFIX = r"(self_attn\.(q|k|v|o)_proj|mlp\.(gate|up|down)_proj)"
MODULE_REGEX = r"model\.language_model\.layers\.\d+\." + SUFFIX
SYSTEM = "<|turn>system\nYou are an FPL player forecaster reading a classic ML signal and pre-deadline text evidence.<|turn>\n"
_INSTRUCTIONS = re.compile(r"<\|turn>user\n.*?(?=Player context:)", re.S)
_SYSTEM = re.compile(r"^<\|turn>system\n.*?<\|turn>\n", re.S)


def compact_prompt(prompt: str) -> str:
    """Drop the output-format instructions (bounds, JSON example): the head does not emit text.
    Keeps the player context, classic signal, provenance, fixture outlook and evidence; ends at the model turn."""
    text = _SYSTEM.sub(SYSTEM, prompt, count=1)
    text = _INSTRUCTIONS.sub("<|turn>user\n", text, count=1)
    return text


class RegHead(nn.Module):
    def __init__(self, hidden: int, n_out: int = N_OUT):
        super().__init__()
        self.norm = nn.LayerNorm(hidden)
        self.proj = nn.Linear(hidden, n_out)
        nn.init.normal_(self.proj.weight, std=0.01)
        nn.init.zeros_(self.proj.bias)

    def forward(self, h: torch.Tensor) -> torch.Tensor:
        return self.proj(self.norm(h.float()))


def inner_model(model):
    base = model.get_base_model() if hasattr(model, "get_base_model") else model
    return getattr(base, "model", base)


def backbone_hidden(model, input_ids: torch.Tensor, attention_mask: torch.Tensor, needs_mm: bool) -> torch.Tensor:
    """Final-layer hidden state at the last real token of each row (right padding). Skips lm_head."""
    inner = inner_model(model)
    kw = dict(input_ids=input_ids, attention_mask=attention_mask)
    if needs_mm:
        kw["mm_token_type_ids"] = torch.zeros_like(input_ids)
    out = inner(**kw)
    h = out.last_hidden_state if hasattr(out, "last_hidden_state") else out[0]
    idx = attention_mask.sum(1) - 1
    return h[torch.arange(h.shape[0], device=h.device), idx]


def needs_mm_ids(model) -> bool:
    return "mm_token_type_ids" in inspect.signature(inner_model(model).forward).parameters


def targets_from_metadata(meta: Dict) -> Dict[str, float]:
    resid = meta["residual_labels_clipped"]
    out = {k: float(resid[k]) for k, _ in REG_FIELDS}
    out["appearance"] = float(meta["labels"]["appearance_probability"] > 0.5)
    out["baseline_appearance"] = float(meta["baseline_forecast"]["baseline_appearance_probability"])
    return out


def logit(p: float) -> float:
    p = min(max(p, 0.02), 0.98)
    return math.log(p / (1 - p))


class Standardiser:
    def __init__(self, mean: Sequence[float], std: Sequence[float]):
        self.mean = list(mean); self.std = [max(s, 1e-3) for s in std]

    @classmethod
    def fit(cls, rows: Sequence[Dict]) -> "Standardiser":
        import statistics
        cols = [[t[k] for t in rows] for k, _ in REG_FIELDS]
        return cls([statistics.fmean(c) for c in cols], [statistics.pstdev(c) for c in cols])

    def encode(self, t: Dict) -> List[float]:
        return [(t[k] - m) / s for (k, _), m, s in zip(REG_FIELDS, self.mean, self.std)]

    def decode(self, z: Sequence[float]) -> Dict[str, float]:
        return {k: max(-b, min(b, z_i * s + m)) for (k, b), z_i, m, s in zip(REG_FIELDS, z, self.mean, self.std)}

    def to_json(self) -> Dict:
        return {"mean": self.mean, "std": self.std}


def deltas_from_output(out: Sequence[float], baseline_appearance: float, std: Standardiser) -> Dict[str, float]:
    d = std.decode(out[: len(REG_FIELDS)])
    b = min(max(baseline_appearance, 0.02), 0.98)
    p = 1 / (1 + math.exp(-(logit(b) + float(out[len(REG_FIELDS)]))))
    d[APP_FIELD] = max(-APP_BOUND, min(APP_BOUND, p - baseline_appearance))
    return {k: round(v, 4) for k, v in d.items()}


def save_head(head: RegHead, std: Standardiser, out_dir: Path, extra: Dict | None = None) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    torch.save(head.state_dict(), out_dir / "head.pt")
    (out_dir / "head.json").write_text(json.dumps({"hidden": head.norm.normalized_shape[0], "n_out": head.proj.out_features,
                                                   "standardiser": std.to_json(), **(extra or {})}, indent=1))


def load_head(out_dir: Path, device) -> tuple:
    cfg = json.loads((out_dir / "head.json").read_text())
    head = RegHead(cfg["hidden"], cfg["n_out"])
    head.load_state_dict(torch.load(out_dir / "head.pt", map_location="cpu"))
    return head.to(device).eval(), Standardiser(**cfg["standardiser"]), cfg

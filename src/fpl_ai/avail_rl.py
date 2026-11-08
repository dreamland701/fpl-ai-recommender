"""R4 (2026-10-15): RL on availability with a verifiable, baseline-subtracted reward.

The policy reads the E22 prompt (official status/news line + article evidence) and answers one question:
will the player play at least a minute this gameweek? Reward = Brier improvement over the classic P(appear)
baseline, (y-b)^2 - (y-p)^2, so the forecast is a baseline to beat, never the target, and the realised
start is the only label (low noise given the text). Unparseable answers score -0.5.
"""
from __future__ import annotations

import json
import re
from typing import Dict, Optional

from .reghead import compact_prompt

QUESTION = ("\n\nQuestion: will this player play at least one minute in this gameweek? The classic model's probability is {b:.2f}. "
            "Reason in at most 40 words from the official status/news and the evidence, then output exactly one JSON object: "
            '{{"reasoning": "<text>", "p_play": <number between 0 and 1>}}')
SYSTEM = "<|turn>system\nYou are an FPL availability analyst. Use only pre-deadline information.<|turn>\n"
_TAIL = re.compile(r"\n?<\|turn>\n<\|turn>model\n\s*$")
_SYSTEM = re.compile(r"^<\|turn>system\n.*?<\|turn>\n", re.S)
_P = re.compile(r'"p_play"\s*:\s*([0-9]*\.?[0-9]+)')
UNPARSEABLE = -0.5


def availability_prompt(prompt: str, baseline_appearance: float) -> str:
    body = _SYSTEM.sub(SYSTEM, compact_prompt(prompt), count=1)
    body = _TAIL.sub("", body)
    return body + QUESTION.format(b=baseline_appearance) + "<|turn>\n<|turn>model\n"


def parse_p_play(text: str) -> Optional[float]:
    text = (text or "").strip()
    try:
        start = text.index("{"); end = text.rindex("}") + 1
        obj = json.loads(text[start:end])
        p = float(obj["p_play"])
    except (ValueError, KeyError, TypeError):
        m = _P.search(text)
        if not m:
            return None
        p = float(m.group(1))
    if not 0.0 <= p <= 1.0:
        return None
    return p


def brier_reward(completion: str, y: float, b: float) -> Dict[str, float]:
    p = parse_p_play(completion)
    if p is None:
        return {"reward": UNPARSEABLE, "p": float("nan"), "ok": 0.0}
    p = min(max(p, 0.01), 0.99)
    return {"reward": (y - b) ** 2 - (y - p) ** 2, "p": p, "ok": 1.0}


def text_could_matter(meta: Dict) -> bool:
    status = str(meta.get("status_pre_deadline") or "").strip().lower()
    news = str(meta.get("news_pre_deadline") or "").strip().lower()
    return bool(meta.get("evidence_present")) or (status not in ("", "a", "none")) or (news not in ("", "none"))

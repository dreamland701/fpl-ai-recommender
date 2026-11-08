#!/usr/bin/env python3
"""Zero-shot availability-fact extraction from news documents with a local Gemma-4 instruction model (2026-10-22).

One document per prompt, strict JSON out: {"facts": [{"player", "team", "status", "detail", "until"}]} with status in
{xi, bench, doubt, out, return, role}. The prompt (build_prompt) is shared with the Haiku comparison arm so the pilot
compares extractors, not prompts. Greedy decode, thinking channel off (the Gemma-4 template emits an empty thought
channel), left-padded batches sorted longest-first so an out-of-memory batch fails at the start, not after hours.

Resumable: rows already in --out (by doc_id) are skipped. Clean stop: touch --stop-file; also stops inside
--pause-window (ISO start/end) when --pause-flag exists (the GW8 Friday GPU gate), so a backfill never overlaps a
time-boxed GPU stage. Output rows: doc_id, model, facts, parse_ok, raw (when not parseable), tokens_in, tokens_out,
seconds. Memory: 31B needs --4bit (bitsandbytes nf4, ~18 GB weights, ~28 GB steady; 75-80 GB system transient during
the load, so nothing else may be on the GPU then); E4B runs in bf16.

usage: extract_availability_facts.py --docs D.jsonl --out O.jsonl --model PATH [--4bit] [--batch 8]
         [--max-new-tokens 768] [--limit N] [--stop-file logs/stop_extract] [--pause-window S/E --pause-flag F]
"""
from __future__ import annotations
import argparse
import datetime as dt
import json
import os
import re
import time
from pathlib import Path

STATUSES = ("xi", "bench", "doubt", "out", "return", "role")
PROMPT = """You extract Premier League player availability facts from one news article for a fantasy football forecasting model.
Article published: {published}. Next Premier League round: Gameweek {gw} ({hours} hours after publication).

Return STRICT JSON only, no prose, no markdown fences, exactly this shape:
{{"facts":[{{"player":"<name as written in the text>","team":"<club, or null if not stated>","status":"<xi|bench|doubt|out|return|role>","detail":"<max 12 words taken from the text>","until":"<expected return time if the text states one, else null>"}}]}}

Status definitions (about the player's NEXT Premier League match unless the text says otherwise):
- xi: expected or confirmed to start
- bench: expected to be a substitute, dropped, rested or rotated out
- doubt: a fitness doubt, late fitness test, 50-50
- out: ruled out (injury, suspension, illness, not registered, has left the club)
- return: back in training or available again after an absence
- role: a change in position, penalty or set-piece duty, captaincy, or a new signing expected to start

Rules: Premier League players only. Include every player whose status the article states, including names inside lists. Do not include players the article does not mention and do not infer beyond the text. A player with no stated status is not a fact. If nothing qualifies return {{"facts":[]}}.

ARTICLE TITLE: {title}
ARTICLE TEXT:
{text}"""


PROMPT_V2 = """You extract Premier League player availability facts from one news article for a fantasy football forecasting model.
Article published: {published}. Next Premier League round: Gameweek {gw} ({hours} hours after publication).

Return STRICT JSON only, no prose, no markdown fences, exactly this shape:
{{"facts":[{{"player":"<name as written in the text>","team":"<club, or null if not stated>","status":"<xi|bench|doubt|out|return|role>","detail":"<max 12 words taken from the text>","until":"<expected return time if the text states one, else null>"}}]}}

A fact is a statement about whether a player will be AVAILABLE or SELECTED for UPCOMING matches. Status definitions:
- xi: the text says he is expected or confirmed to start the next match, or has become a regular starter
- bench: the text says he is expected to be a substitute, has been dropped, is being rested or rotated out
- doubt: a fitness doubt, late fitness test, 50-50, "will be assessed"
- out: ruled out of upcoming matches (injury, suspension, illness, not registered, has left the club)
- return: back in training, back in the squad or available again after an absence
- role: a change of position, penalty or set-piece duty, captaincy, or a new signing expected to start

NOT facts (never include): who played, scored, assisted or was substituted in a match that has already been played; performance, praise or criticism; contract, transfer or price talk with no availability consequence; players outside the Premier League.
Include every player with a qualifying statement, including names inside lists such as "Subs from", "Doubtful", "Injured", "Suspended". Do not infer beyond the text. If nothing qualifies return {{"facts":[]}}.

ARTICLE TITLE: {title}
ARTICLE TEXT:
{text}"""
PROMPTS = {"v1": PROMPT, "v2": PROMPT_V2}


def build_prompt(doc: dict, max_chars: int = 9000, version: str = "v1") -> str:
    text = str(doc.get("text") or "")[:max_chars]
    return PROMPTS[version].format(published=str(doc.get("published_at", ""))[:16].replace("T", " ") + " UTC", gw=doc.get("gw", "?"),
                                   hours=int(round(float(doc.get("hours_before", 0) or 0))), title=doc.get("title", ""), text=text)


def parse_facts(raw: str) -> tuple[list[dict], bool]:
    """Strict JSON with light repair: strip fences, take the outermost braces, salvage a truncated facts list."""
    s = raw.strip()
    s = re.sub(r"^```(?:json)?\s*", "", s); s = re.sub(r"\s*```$", "", s)
    i, j = s.find("{"), s.rfind("}")
    if i < 0:
        return [], False
    cand = s[i: j + 1] if j > i else s[i:]
    for attempt in (cand, cand + "]}", cand + "}]}", cand[: cand.rfind("}")] + "}]}" if cand.rfind("}") > 0 else cand):
        try:
            obj = json.loads(attempt)
            facts = obj.get("facts", []) if isinstance(obj, dict) else []
            return [clean(f) for f in facts if isinstance(f, dict)], attempt == cand
        except (json.JSONDecodeError, AttributeError):
            continue
    return [], False


def clean(f: dict) -> dict:
    status = str(f.get("status") or "").strip().lower()
    return {"player": str(f.get("player") or "").strip(), "team": (str(f["team"]).strip() if f.get("team") else None),
            "status": status if status in STATUSES else "other:" + status[:20], "detail": str(f.get("detail") or "").strip()[:120],
            "until": (str(f["until"]).strip()[:40] if f.get("until") else None)}


def in_pause(window: str | None, flag: str | None) -> bool:
    if not window or not flag or not Path(flag).exists():
        return False
    a, b = window.split("/")
    now = dt.datetime.now(dt.timezone.utc)
    return dt.datetime.fromisoformat(a.replace("Z", "+00:00")) <= now <= dt.datetime.fromisoformat(b.replace("Z", "+00:00"))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--docs", required=True); ap.add_argument("--out", required=True); ap.add_argument("--model", required=True)
    ap.add_argument("--4bit", dest="four", action="store_true"); ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--max-new-tokens", type=int, default=768); ap.add_argument("--max-chars", type=int, default=9000)
    ap.add_argument("--limit", type=int, default=0); ap.add_argument("--stop-file", default="logs/stop_extract")
    ap.add_argument("--pause-window", default=None); ap.add_argument("--pause-flag", default=None)
    ap.add_argument("--label", default=None, help="model label written on every row (default: basename of --model)")
    ap.add_argument("--redo-truncated", action="store_true",
                    help="two-pass mode: rows already in --out whose output hit the cap are dropped and generated again")
    ap.add_argument("--prompt-version", default="v1", choices=sorted(PROMPTS),
                    help="v1 = pilot prompt shared with the Haiku arm; v2 = adds an explicit 'not facts' list (past matches, praise, contracts)")
    args = ap.parse_args()

    docs = [json.loads(l) for l in open(args.docs)]
    done = set()
    if Path(args.out).exists():
        rows = [json.loads(l) for l in open(args.out)]
        if args.redo_truncated:
            keep = [r for r in rows if not r.get("truncated")]
            if len(keep) < len(rows):
                with open(args.out, "w") as f:
                    for r in keep:
                        f.write(json.dumps(r, ensure_ascii=False) + "\n")
                print(f"redo: dropped {len(rows) - len(keep)} truncated rows for a second pass", flush=True)
            rows = keep
        done = {r["doc_id"] for r in rows}
    todo = [d for d in docs if d["doc_id"] not in done]
    if args.limit:
        todo = todo[: args.limit]
    label = args.label or os.path.basename(args.model.rstrip("/"))
    print(f"docs {len(docs)} done {len(done)} todo {len(todo)} model {label} batch {args.batch} 4bit {args.four}", flush=True)
    if not todo:
        return

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
    tok = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True, extra_special_tokens={})
    tok.padding_side = "left"
    kw = dict(dtype=torch.bfloat16, device_map="auto", trust_remote_code=True, attn_implementation="sdpa")
    if args.four:
        kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True,
                                                       bnb_4bit_compute_dtype=torch.bfloat16)
    t0 = time.time()
    model = AutoModelForCausalLM.from_pretrained(args.model, **kw).eval()
    print(f"loaded in {time.time() - t0:.0f}s; torch allocated {torch.cuda.memory_allocated() / 2**30:.1f} GB", flush=True)
    stop_ids = [i for i in (tok.eos_token_id, tok.convert_tokens_to_ids("<turn|>")) if isinstance(i, int) and i >= 0]

    prompts = {d["doc_id"]: tok.apply_chat_template([{"role": "user", "content": build_prompt(d, args.max_chars, args.prompt_version)}],
                                                    tokenize=False, add_generation_prompt=True, enable_thinking=False) for d in todo}
    todo.sort(key=lambda d: -len(prompts[d["doc_id"]]))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    n_done = 0; t_start = time.time()
    with open(args.out, "a") as out, torch.inference_mode():
        for s in range(0, len(todo), args.batch):
            if Path(args.stop_file).exists():
                print(f"stop file {args.stop_file} present; exiting cleanly after {n_done} docs", flush=True); break
            if in_pause(args.pause_window, args.pause_flag):
                print("inside the pause window with the pause flag present; exiting cleanly", flush=True); break
            batch = todo[s: s + args.batch]
            enc = tok([prompts[d["doc_id"]] for d in batch], return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            tb = time.time()
            gen = model.generate(**enc, max_new_tokens=args.max_new_tokens, do_sample=False, eos_token_id=stop_ids, pad_token_id=tok.pad_token_id)
            new = gen[:, enc["input_ids"].shape[1]:]
            texts = tok.batch_decode(new, skip_special_tokens=True)
            secs = (time.time() - tb) / len(batch)
            for k, (d, t, row) in enumerate(zip(batch, texts, new)):
                facts, ok = parse_facts(t)
                n_out = int((row != tok.pad_token_id).sum())
                rec = {"doc_id": d["doc_id"], "model": label, "facts": facts, "parse_ok": ok, "n_facts": len(facts),
                       "tokens_in": int(enc["attention_mask"][k].sum()),
                       "tokens_out": n_out, "truncated": bool(n_out >= args.max_new_tokens), "seconds": round(secs, 2)}
                if not ok:
                    rec["raw"] = t[-1500:]
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            out.flush(); n_done += len(batch)
            el = time.time() - t_start
            print(f"{n_done}/{len(todo)} {el / n_done:.1f}s/doc (batch {len(batch)}, in {enc['input_ids'].shape[1]} tok, "
                  f"out max {int((new != tok.pad_token_id).sum(1).max())}), peak {torch.cuda.max_memory_allocated() / 2**30:.1f} GB", flush=True)
    print(f"DONE {n_done} docs in {(time.time() - t_start) / 60:.1f} min; peak torch {torch.cuda.max_memory_allocated() / 2**30:.1f} GB", flush=True)


if __name__ == "__main__":
    main()

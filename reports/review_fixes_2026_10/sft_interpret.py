"""Why did the SFT adapter move a player? Prompt ablations + the full output distribution.

For each chosen player, the GW6 prompt is edited one factor at a time (no
evidence, one article at a time, neutral status line, minutes forecast capped
at 90, an average starter's forecast in place of his own, the provenance
"post-break" clause removed). For every version, the adapter's probability of
each delta_points_1gw value from -2.0 to +2.0 (its one-decimal output grid) is
read off by teacher forcing, giving the mean, the most likely value (what
greedy decoding emits) and P(cut). Comparing versions attributes the move to
inputs; the distribution shows how conservative and how uncertain it is.

usage: sft_interpret.py <examples.jsonl> <adapter_dir> <out.json> <player> [<player> ...]
"""
import json
import math
import re
import sys

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "google/gemma-4-E4B-it"
VALUES = [round(-2.0 + 0.1 * i, 1) for i in range(41)]
NO_EVIDENCE = ("Timestamp-safe text evidence:\nNo timestamp-safe text evidence is available for this player-week. "
               "Without evidence, prefer deltas at or near zero.")
TAIL = "\n<|turn>\n<|turn>model\n"


def fmt(v):
    s = f"{v:.1f}"
    return "0.0" if s == "-0.0" else s


def variants(prompt):
    out = {"original": prompt}
    head, sep, evidence = prompt.partition("Timestamp-safe text evidence:\n")
    body = evidence[: evidence.rfind(TAIL)] if TAIL in evidence else evidence
    if "No timestamp-safe text evidence" not in body:
        out["no_evidence"] = head + NO_EVIDENCE + TAIL
        docs = [d for d in re.split(r"\n(?=\[\d+\] )", body.strip()) if d.strip()]
        if len(docs) > 1:
            for i, doc in enumerate(docs, start=1):
                only = re.sub(r"^\[\d+\]", "[1]", doc.strip())
                out[f"article_{i}_only"] = head + sep + only + TAIL
    if not re.search(r"Status pre-deadline: a\n", prompt):
        p = re.sub(r"Status pre-deadline: .*", "Status pre-deadline: a", prompt)
        out["neutral_status"] = re.sub(r"Official player news pre-deadline: .*", "Official player news pre-deadline: none", p)
    minutes = re.search(r'"baseline_minutes_1gw": ([\d.]+)', prompt)
    if minutes and float(minutes.group(1)) > 90:
        out["minutes_capped_90"] = prompt.replace(minutes.group(0), '"baseline_minutes_1gw": 90.0')
    swap = re.sub(r'"baseline_points_1gw": [\d.]+', '"baseline_points_1gw": 4.0', prompt)
    swap = re.sub(r'"baseline_points_3gw": [\d.]+', '"baseline_points_3gw": 11.0', swap)
    out["average_starter_forecast"] = re.sub(r'"baseline_points_5gw": [\d.]+', '"baseline_points_5gw": 18.0', swap)
    out["no_post_break_clause"] = prompt.replace(", cup congestion, or post-break effects", ", or cup congestion")
    return out


def main() -> None:
    examples_path, adapter, out_path, players = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
    rows = {json.loads(l)["metadata"]["player_name"]: json.loads(l) for l in open(examples_path) if l.strip()}
    tok = AutoTokenizer.from_pretrained(MODEL)
    model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto")
    model = PeftModel.from_pretrained(model, adapter)
    model.eval()

    def distribution(prompt):
        prefix = prompt + '{"delta_points_1gw":'
        p_ids = tok(prefix, add_special_tokens=False)["input_ids"]
        groups = {}
        for v in VALUES:
            full = tok(prefix + fmt(v) + ",", add_special_tokens=False)["input_ids"]
            assert full[: len(p_ids)] == p_ids, "prefix tokenisation changed"
            groups.setdefault(len(full), []).append((v, full))
        scores = {}
        for length, members in groups.items():
            ids = torch.tensor([m[1] for m in members], device=model.device)
            n = length - len(p_ids)
            with torch.no_grad():
                logits = model(input_ids=ids, logits_to_keep=n + 1).logits.float()
            logp = torch.log_softmax(logits, dim=-1)
            for row, (v, full) in enumerate(members):
                tgt = torch.tensor(full[-n:], device=model.device)
                scores[v] = logp[row, :n].gather(-1, tgt[:, None]).sum().item()
        top = max(scores.values())
        weights = {v: math.exp(s - top) for v, s in scores.items()}
        z = sum(weights.values())
        probs = {v: w / z for v, w in weights.items()}
        mean = sum(v * p for v, p in probs.items())
        mode = max(probs, key=probs.get)
        return {"mean": round(mean, 3), "mode": mode, "p_cut": round(sum(p for v, p in probs.items() if v < 0), 3),
                "top5": sorted(((v, round(p, 3)) for v, p in probs.items()), key=lambda x: -x[1])[:5]}

    report = {}
    for name in players:
        prompt = rows[name]["prompt"]
        base = rows[name]["metadata"]["baseline_forecast"]["baseline_points_1gw"]
        report[name] = {"baseline_points_1gw": base, "variants": {k: distribution(p) for k, p in variants(prompt).items()}}
        o = report[name]["variants"]["original"]
        print(f"\n{name} (classic {base:.2f}): original mean {o['mean']:+.2f}, most likely {o['mode']:+.1f}, P(cut) {o['p_cut']:.2f}")
        for k, d in report[name]["variants"].items():
            if k != "original":
                print(f"   {k:26s} mean {d['mean']:+.2f} ({d['mean'] - o['mean']:+.2f})  most likely {d['mode']:+.1f}  P(cut) {d['p_cut']:.2f}")
    json.dump(report, open(out_path, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

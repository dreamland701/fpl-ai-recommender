"""Expectation decoding: replace the adapter's greedy points deltas with the mean of its own distribution.

Greedy decoding of a token-trained model returns roughly the most likely value
(its median-like "typical" outcome); squad decisions need the average. For each
row, the probability of every value on the delta_points_1gw grid (-2.0..+2.0) is
read off exactly (sign, digit, ".", digit: one prompt pass plus short cached
continuations), and the same for delta_points_3gw (+/-4) and delta_points_5gw
(+/-6) conditioned on the greedy text before them. The output has the decoder's
format, with the three points fields replaced by their means and the minutes
and appearance fields copied from the greedy response, so the backtests read it
unchanged. Also reports how often the scored greedy 1GW value equals the stored
greedy decode (a check that this scorer is the model that was decoded).

usage: expectation_decode.py <examples.jsonl> <greedy_predictions.jsonl> <adapter_dir> <out.jsonl> [<validate_rows>]
"""
import copy
import json
import sys
from pathlib import Path

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "google/gemma-4-E4B-it"
FIELDS = [("delta_points_1gw", 2), ("delta_points_3gw", 4), ("delta_points_5gw", 6)]


def main() -> None:
    ex_path, greedy_path, adapter, out_path = sys.argv[1:5]
    validate = int(sys.argv[5]) if len(sys.argv) > 5 else 0  # rows to re-score unbatched, as a check
    examples = [json.loads(l) for l in open(ex_path) if l.strip()]
    greedy = {}
    for l in open(greedy_path):
        p = json.loads(l)
        greedy[(p["season"], int(p["week"]), int(p["metadata"]["player_id"]))] = p["response"]
    out = Path(out_path)
    done = sum(1 for l in open(out) if l.strip()) if out.exists() else 0
    print(f"{len(examples)} rows, resuming after {done}")

    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, extra_special_tokens={})
    model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto",
                                                 trust_remote_code=True, attn_implementation="sdpa")
    # Merged: identical outputs, ~9x faster calls than target_parameters LoRA left unmerged (2026-10-09).
    model = PeftModel.from_pretrained(model, adapter).merge_and_unload().eval()
    dev = model.device
    t = {s: tok.convert_tokens_to_ids(s) for s in ["-", "."] + [str(d) for d in range(10)]}
    digits = [t[str(d)] for d in range(10)]

    def ids(text):
        return tok(text, add_special_tokens=False)["input_ids"]

    def field_stats(p0, cache, k, batched=True):
        """Mean, greedy value and P(cut) of one bounded one-decimal field, from the first-token
        distribution p0 and the cache that produced it. All 2(k+1) sign/digit branches run as
        one batch on a repeated copy of the cache (batched=False: one at a time, for checking)."""
        conts = [([t["-"], t[str(a)], t["."]], True, a) for a in range(k + 1)] + \
                [([t[str(a)], t["."], t["."]], False, a) for a in range(k + 1)]  # last "." of a positive row is padding
        if batched:
            c = copy.deepcopy(cache)
            c.batch_repeat_interleave(len(conts))
            with torch.no_grad():
                pr = torch.softmax(model(input_ids=torch.tensor([x[0] for x in conts], device=dev), past_key_values=c,
                                         use_cache=True).logits.float(), -1)
        else:
            rows = []
            for cont, _, _ in conts:
                with torch.no_grad():
                    rows.append(model(input_ids=torch.tensor([cont], device=dev), past_key_values=copy.deepcopy(cache),
                                      use_cache=True).logits[0].float())
            pr = torch.softmax(torch.stack(rows), -1)
        p_int = pr[0, 0]  # after "-"
        probs, dec_dist = {}, {}
        for row, (_, neg, a) in enumerate(conts):
            lead = p0[t["-"]].item() * p_int[t[str(a)]].item() if neg else p0[t[str(a)]].item()
            dot, dec = (pr[row, 1][t["."]].item(), pr[row, 2]) if neg else (pr[row, 0][t["."]].item(), pr[row, 1])
            dec_dist[(neg, a)] = dec
            for d in range(10):
                if (neg and a == 0 and d == 0) or (a == k and d > 0):
                    continue
                v = round(-(a + d / 10) if neg else a + d / 10, 1)
                probs[v] = probs.get(v, 0.0) + lead * dot * dec[digits[d]].item()
        z = sum(probs.values())
        mean = sum(v * p for v, p in probs.items()) / z
        p_cut = sum(p for v, p in probs.items() if v < 0) / z
        first = int(p0.argmax())
        neg = first == t["-"]
        a_tok = int(p_int.argmax()) if neg else first
        g = None
        if a_tok in digits and digits.index(a_tok) <= k:
            a = digits.index(a_tok)
            d_tok = int(dec_dist[(neg, a)].argmax())
            if d_tok in digits:
                g = round(-(a + digits.index(d_tok) / 10) if neg else a + digits.index(d_tok) / 10, 1)
        return mean, g, p_cut, z


    def stats_from(p0, branch, k):
        """branch[(neg, a)] = (dist after "-" [neg a=0 only, else None], P("."), decimal-digit distribution)."""
        p_int = branch[(True, 0)][0]
        probs = {}
        for (neg, a), (_, dot, dec) in branch.items():
            lead = p0[t["-"]].item() * p_int[t[str(a)]].item() if neg else p0[t[str(a)]].item()
            for d in range(10):
                if (neg and a == 0 and d == 0) or (a == k and d > 0):
                    continue
                v = round(-(a + d / 10) if neg else a + d / 10, 1)
                probs[v] = probs.get(v, 0.0) + lead * dot * dec[digits[d]].item()
        z = sum(probs.values())
        mean = sum(v * q for v, q in probs.items()) / z
        p_cut = sum(q for v, q in probs.items() if v < 0) / z
        first = int(p0.argmax())
        neg = first == t["-"]
        a_tok = int(p_int.argmax()) if neg else first
        g = None
        if a_tok in digits and digits.index(a_tok) <= k:
            a = digits.index(a_tok)
            d_tok = int(branch[(neg, a)][2].argmax())
            if d_tok in digits:
                g = round(-(a + digits.index(d_tok) / 10) if neg else a + digits.index(d_tok) / 10, 1)
        return mean, g, p_cut, z

    def score_row_fast(prompt, resp):
        """All three fields in two forward calls: the prompt, then every branch of every field as one batch
        continuing from a repeated prompt cache (later fields carry the greedy text before them). Each model
        call costs about a second of fixed overhead on this machine, so fewer, larger calls are faster
        (measured 2026-10-09: 3.5 s per row, against 6-8 s for one call per field)."""
        pre = torch.tensor([ids(prompt + '{"delta_points_1gw":')], device=dev)
        with torch.no_grad():
            o = model(input_ids=pre, use_cache=True, logits_to_keep=1)
        p0_first = torch.softmax(o.logits[0, -1].float(), -1)
        bridges, prefix = [], []
        for j in range(1, len(FIELDS)):
            start = resp.index(f'"{FIELDS[j - 1][0]}":') + len(f'"{FIELDS[j - 1][0]}":')
            prefix = prefix + ids(resp[start: resp.index(f'"{FIELDS[j][0]}":') + len(f'"{FIELDS[j][0]}":')])
            bridges.append(list(prefix))
        rows, meta = [], []
        for j, (field, k) in enumerate(FIELDS):
            lead = [] if j == 0 else bridges[j - 1]
            for neg in (True, False):
                for a in range(k + 1):
                    cont = ([t["-"]] if neg else []) + [t[str(a)], t["."]]
                    rows.append(lead + cont)
                    meta.append((j, neg, a, len(lead)))
        width = max(len(r) for r in rows)
        batch = torch.tensor([r + [t["."]] * (width - len(r)) for r in rows], device=dev)  # right padding, never attended
        c = copy.deepcopy(o.past_key_values)
        c.batch_repeat_interleave(len(rows))
        with torch.no_grad():
            logits = model(input_ids=batch, past_key_values=c, use_cache=True).logits
        out = []
        for j, (field, k) in enumerate(FIELDS):
            branch, p0 = {}, p0_first
            for row, (jj, neg, a, off) in enumerate(meta):
                if jj != j:
                    continue
                if j > 0 and p0 is p0_first:
                    p0 = torch.softmax(logits[row, off - 1].float(), -1)
                pr = torch.softmax(logits[row, off: off + 3].float(), -1)
                branch[(neg, a)] = (pr[0] if neg else None, (pr[1] if neg else pr[0])[t["."]].item(), pr[2] if neg else pr[1])
            out.append(stats_from(p0, branch, k))
        return out

    agree = n = 0
    import time
    t_start = time.time()
    with out.open("a") as handle:
        for i, ex in enumerate(examples[done:], start=done):
            m = ex["metadata"]
            resp = greedy[(ex["season"], int(ex["week"]), int(m["player_id"]))]
            g_json = json.loads(resp[: resp.index("}") + 1])
            result, diag = dict(g_json), {}
            fast_stats = score_row_fast(ex["prompt"], resp)
            if n < validate:  # the slow path: one field at a time, branches one at a time
                pre = torch.tensor([ids(ex["prompt"] + '{"delta_points_1gw":')], device=dev)
                with torch.no_grad():
                    o = model(input_ids=pre, use_cache=True, logits_to_keep=1)
                p0, cache = torch.softmax(o.logits[0, -1].float(), -1), o.past_key_values
                for j, (field, k) in enumerate(FIELDS):
                    if j > 0:
                        start = resp.index(f'"{FIELDS[j - 1][0]}":') + len(f'"{FIELDS[j - 1][0]}":')
                        bridge = resp[start: resp.index(f'"{field}":') + len(f'"{field}":')]
                        cache = copy.deepcopy(cache)
                        with torch.no_grad():
                            o = model(input_ids=torch.tensor([ids(bridge)], device=dev), past_key_values=cache, use_cache=True,
                                      logits_to_keep=1)
                        p0, cache = torch.softmax(o.logits[0, -1].float(), -1), o.past_key_values
                    m2, g2, _, _ = field_stats(p0, cache, k, batched=False)
                    print(f"  check row {i} {field}: fast mean {fast_stats[j][0]:+.3f} greedy {fast_stats[j][1]} | "
                          f"slow {m2:+.3f} {g2}", flush=True)
                    # bf16 rounding differs between batch shapes; the 3/5GW spreads are wide (+/-4, +/-6), so
                    # their means move more. Greedy values must agree exactly.
                    assert abs(fast_stats[j][0] - m2) < (0.03 if j == 0 else 0.10) and fast_stats[j][1] == g2, "fast scoring disagrees"
            for j, (field, k) in enumerate(FIELDS):
                mean, g, p_cut, cover = fast_stats[j]
                result[field] = round(mean, 2)
                diag[field] = {"greedy_scored": g, "greedy_decoded": g_json.get(field), "p_cut": round(p_cut, 3),
                               "coverage": round(cover, 3)}
            n += 1
            agree += diag["delta_points_1gw"]["greedy_scored"] == g_json.get("delta_points_1gw")
            record = {"season": ex["season"], "week": ex["week"], "response": json.dumps(result, separators=(",", ":")),
                      "metadata": m, "expectation_diagnostics": diag}
            handle.write(json.dumps(record) + "\n")
            if n % 50 == 0:
                handle.flush()
                print(f"{i + 1}/{len(examples)} | scored greedy 1GW == decoded greedy: {agree}/{n}", flush=True)
    print(f"done: scored greedy 1GW == decoded greedy on {agree}/{n} rows ({(time.time() - t_start) / max(n, 1):.2f}s per row)")


if __name__ == "__main__":
    main()

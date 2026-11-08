"""Why did the SFT adapter move a player? Exact output distribution + Shapley attribution.

v2 of sft_interpret.py, which loaded the model differently from the live decoder
(default attention, stock tokenizer) and whose "most likely" values did not
reproduce the decoded outputs. This version loads exactly as
eval_gemma_responses.py does and checks itself three ways per player: batch-1
greedy generation, the original left-padded batch of 16, and the greedy path
read off the scored distribution must agree with the live output.

Distribution: the adapter writes delta_points_1gw as sign, digit, ".", digit
(Gemma tokenises digits singly), so the probability of every value on its grid
(-2.0..+2.0 in 0.1 steps) comes from one prompt pass plus six short cached
continuations. Reported: the mean (its expected-value belief), the greedy
value (what it writes), P(cut).

Attribution: six player-specific inputs are each swapped for a neutral
version; the mean is computed for all 64 on/off combinations and split into
Shapley contributions, which add up exactly to (actual mean - fully neutral mean):
  forecast      classic 1/3/5GW points -> an average starter's 4.0 / 11.0 / 18.0
  playing_time  classic minutes, P(appear), status and news -> 85, 0.95, a, none
  fixtures      opponents and difficulties GW6-10 -> TBD, diff 3 (home/away kept)
  text          the articles -> the no-evidence sentence
  name          "Player: <name>" -> "Player: Player A"
  defcon        the defensive-contribution line -> removed (as in 2022-25 prompts)

usage: sft_interpret_v2.py <examples.jsonl> <adapter_dir> <decoded.jsonl> <out.json> <player> [...]
"""
import copy
import itertools
import json
import math
import re
import sys

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402

MODEL = "google/gemma-4-E4B-it"
HEAD = '{"delta_points_1gw":'
NO_EVIDENCE = ("No timestamp-safe text evidence is available for this player-week. "
               "Without evidence, prefer deltas at or near zero.")
FACTORS = ["forecast", "playing_time", "fixtures", "text", "name", "defcon"]
TAIL = "\n<|turn>\n<|turn>model\n"


def neutralise(prompt, factor):
    if factor == "forecast":
        for field, value in (("1gw", "4.0"), ("3gw", "11.0"), ("5gw", "18.0")):
            prompt = re.sub(rf'"baseline_points_{field}": [\d.]+', f'"baseline_points_{field}": {value}', prompt)
    elif factor == "playing_time":
        prompt = re.sub(r'"baseline_minutes_1gw": [\d.]+', '"baseline_minutes_1gw": 85.0', prompt)
        prompt = re.sub(r'"baseline_appearance_probability": [\d.]+', '"baseline_appearance_probability": 0.95', prompt)
        prompt = re.sub(r"Status pre-deadline: .*", "Status pre-deadline: a", prompt)
        prompt = re.sub(r"Official player news pre-deadline: .*", "Official player news pre-deadline: none", prompt)
    elif factor == "fixtures":
        prompt = re.sub(r"(GW\d+): [A-Z]{3} \(([HA]), diff \d\)", r"\1: TBD (\2, diff 3)", prompt)
    elif factor == "text":
        head, sep, rest = prompt.partition("Timestamp-safe text evidence:\n")
        prompt = head + sep + NO_EVIDENCE + rest[rest.rfind(TAIL):]
    elif factor == "name":
        prompt = re.sub(r"- Player: .*", "- Player: Player A", prompt)
    elif factor == "defcon":
        prompt = re.sub(r"- Defensive contribution \(rule since 2025-26.*\n", "", prompt)
    return prompt


def grid_value(neg, a, b):
    v = round(a + b / 10, 1)
    return -v if neg else v


def main() -> None:
    ex_path, adapter, decoded_path, out_path, players = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
    rows = [json.loads(l) for l in open(ex_path) if l.strip()]
    names = [r["metadata"]["player_name"] for r in rows]
    live = {}
    for l in open(decoded_path):
        p = json.loads(l)
        live[p["metadata"]["player_name"]] = (parse_delta_response(p["response"]) or {}).get("delta_points_1gw")

    tok = AutoTokenizer.from_pretrained(MODEL, trust_remote_code=True, extra_special_tokens={})
    if tok.pad_token is None:
        tok.pad_token = tok.eos_token
    model = AutoModelForCausalLM.from_pretrained(MODEL, torch_dtype=torch.bfloat16, device_map="auto",
                                                 trust_remote_code=True, attn_implementation="sdpa")
    # Merged: identical outputs, ~9x faster calls than target_parameters LoRA left unmerged (2026-10-09).
    model = PeftModel.from_pretrained(model, adapter).merge_and_unload().eval()
    dev = model.device
    tid = {s: tok.convert_tokens_to_ids(s) for s in ["-", ".", ",", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}
    digit_ids = [tid[str(d)] for d in range(10)]
    check = tok(HEAD + "-1.2,", add_special_tokens=False)["input_ids"][-5:]
    assert check == [tid["-"], tid["1"], tid["."], tid["2"], tid[","]], "value tokenisation is not digit-level"

    def step_probs(prompt, use_cache=True):
        """P(first token), and per branch P(int digit), P('.'), P(decimal digit)."""
        pre = tok(prompt + HEAD, add_special_tokens=False, return_tensors="pt")["input_ids"].to(dev)
        branches = [(True, a) for a in (0, 1, 2)] + [(False, a) for a in (0, 1, 2)]
        out = {}
        with torch.no_grad():
            first = model(input_ids=pre, use_cache=use_cache, logits_to_keep=1)
            p0 = torch.softmax(first.logits[0, -1].float(), -1)
            for neg, a in branches:
                cont = ([tid["-"]] if neg else []) + [tid[str(a)], tid["."]]
                if use_cache:
                    lg = model(input_ids=torch.tensor([cont], device=dev), past_key_values=copy.deepcopy(first.past_key_values),
                               use_cache=True).logits[0].float()
                else:
                    lg = model(input_ids=torch.cat([pre, torch.tensor([cont], device=dev)], 1),
                               logits_to_keep=len(cont)).logits[0].float()
                pr = torch.softmax(lg, -1)
                out[(neg, a)] = {"int": pr[0] if neg else None, "dot": pr[-2][tid["."]].item(), "dec": pr[-1]}
        return p0, out

    memo = {}

    def distribution(prompt, use_cache=True):
        if use_cache and prompt in memo:
            return memo[prompt]
        p0, br = step_probs(prompt, use_cache)
        p_int_neg = br[(True, 0)]["int"]
        probs = {}
        for (neg, a), b in br.items():
            lead = p0[tid["-"]].item() * p_int_neg[tid[str(a)]].item() if neg else p0[tid[str(a)]].item()
            for d in range(10):
                if (neg and a == 0 and d == 0) or (a == 2 and d > 0):
                    continue  # "-0.0" never trained; the grid stops at +/-2.0
                probs[grid_value(neg, a, d)] = probs.get(grid_value(neg, a, d), 0.0) + lead * b["dot"] * b["dec"][digit_ids[d]].item()
        covered = sum(probs.values())
        probs = {v: p / covered for v, p in probs.items()}
        # greedy path over the full vocabulary
        t0 = int(p0.argmax())
        if t0 == tid["-"]:
            a = digit_ids.index(int(p_int_neg.argmax())) if int(p_int_neg.argmax()) in digit_ids else None
            neg = True
        else:
            a = digit_ids.index(t0) if t0 in digit_ids else None
            neg = False
        greedy = None
        if a is not None and a <= 2:
            dec = br[(neg, a)]["dec"]
            d = digit_ids.index(int(dec.argmax())) if int(dec.argmax()) in digit_ids else None
            greedy = grid_value(neg, a, d) if d is not None else None
        mean = sum(v * p for v, p in probs.items())
        result = {"mean": round(mean, 3), "greedy": greedy, "p_cut": round(sum(p for v, p in probs.items() if v < 0), 3),
                "coverage": round(covered, 3),
                "top5": sorted(((v, round(p, 3)) for v, p in probs.items()), key=lambda x: -x[1])[:5],
                "probs": {f"{v:.1f}": round(p, 4) for v, p in sorted(probs.items())}}
        if use_cache:
            memo[prompt] = result
        return result

    def generate(prompts):
        tok.padding_side = "left"
        enc = tok(prompts, return_tensors="pt", padding=True).to(dev)
        enc["mm_token_type_ids"] = torch.zeros_like(enc["input_ids"])
        with torch.no_grad():
            seq = model.generate(**enc, max_new_tokens=14, do_sample=False, temperature=None, top_p=None, top_k=None,
                                 pad_token_id=tok.pad_token_id)
        texts = tok.batch_decode(seq[:, enc["input_ids"].shape[1]:], skip_special_tokens=True)
        out = []
        for t in texts:
            m = re.match(r'\{"delta_points_1gw":(-?\d+(?:\.\d+)?)', t)
            out.append(float(m.group(1)) if m else t)
        return out

    report = {}
    for n_done, name in enumerate(players):
        i = names.index(name)
        prompt = rows[i]["prompt"]
        if n_done == 0:  # the cached continuation must match a plain full pass
            a, b = distribution(prompt, True), distribution(prompt, False)
            diff = max(abs(a["probs"][k] - b["probs"][k]) for k in a["probs"])
            print(f"cache check on {name}: max |dP| {diff:.4f} (mean {a['mean']:+.3f} vs {b['mean']:+.3f})")
            assert diff < 0.02, "cached scoring disagrees with full passes"
        batch_start = (i // 16) * 16
        padded = generate([r["prompt"] for r in rows[batch_start:batch_start + 16]])[i - batch_start]
        single = generate([prompt])[0]
        means = {}
        dists = {}
        for keep in itertools.product([1, 0], repeat=len(FACTORS)):
            p = prompt
            for f, k in zip(FACTORS, keep):
                if not k:
                    p = neutralise(p, f)
            d = distribution(p)
            means[keep] = d["mean"]
            if sum(keep) in (len(FACTORS), 0) or sum(keep) == len(FACTORS) - 1:
                dists[keep] = d
        n = len(FACTORS)
        shap = {}
        for j, f in enumerate(FACTORS):
            total = 0.0
            for keep in means:
                if keep[j] == 0:
                    with_j = keep[:j] + (1,) + keep[j + 1:]
                    s = sum(keep)
                    total += math.factorial(s) * math.factorial(n - s - 1) / math.factorial(n) * (means[with_j] - means[keep])
            shap[f] = round(total, 3)
        full, none = dists[(1,) * n], dists[(0,) * n]
        report[name] = {
            "baseline_points_1gw": rows[i]["metadata"]["baseline_forecast"]["baseline_points_1gw"],
            "live_decode": live.get(name), "batch1_greedy": single, "padded_batch_greedy": padded,
            "original": full, "fully_neutral": none, "shapley": shap,
            "one_factor_off": {FACTORS[j]: dists[tuple(0 if k == j else 1 for k in range(n))]["mean"] for j in range(n)},
        }
        print(f"\n{name} (classic {report[name]['baseline_points_1gw']:.2f}): live {live.get(name)} | batch-1 greedy {single} | "
              f"padded batch {padded} | scored greedy {full['greedy']} | mean {full['mean']:+.2f} | P(cut) {full['p_cut']:.2f} | "
              f"coverage {full['coverage']:.2f}")
        print(f"   neutral player mean {none['mean']:+.2f}; contributions: " +
              ", ".join(f"{f} {v:+.2f}" for f, v in shap.items()) + f"  (sum {sum(shap.values()):+.2f})")
        json.dump(report, open(out_path, "w"), indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()

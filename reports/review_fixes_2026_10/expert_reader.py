"""Do the articles hold a "hidden pattern" a sharp human reader would spot, beyond the classic model and the
transfer market? (Wes, 2026-10-11: "have the article capture something that's deep in people's minds, something
that the model and the data cannot capture")

An untrained LLM (default: Gemma 4 31B) reads each player's pre-deadline article excerpts (12 h cutoff, the
focused E21 prompts) with only the player's name and position, and rates
  start_risk  0 no concern / 1 some doubt / 2 likely out or benched
  outlook     -2 much worse than his usual output .. +2 much better (0 when the text says nothing)
Then, on player-weeks the model cannot have memorised (2025-26 GW27-38 and 2026-27 GW2-5), the ratings are
tested on top of classic: does outlook predict the surprise (actual - classic)? Does start_risk predict not
playing beyond classic P(appear)? Classic already carries the market (ownership, transfers in/out).

usage: expert_reader.py rate <out_ratings.jsonl> [--model PATH]
       expert_reader.py score <ratings.jsonl> <out.md>
"""
import json
import re
import sys

import numpy as np

ROOT = "/home/wescheng/projects/fpl/fpl"
SETS = [f"{ROOT}/reports/llm_residual_v2_e21_clean_top96_thru_2526_26_eval_2526_27_38/eval.jsonl",
        f"{ROOT}/reports/llm_residual_v2_e21_clean_top96_eval_2627_2_5/eval.jsonl"]
PROMPT = ("You are an experienced Fantasy Premier League analyst. Below are pre-deadline article excerpts that mention "
          "{name} ({position}). Using only what they say, plus your football judgement, rate this gameweek:\n"
          "- start_risk: 0 = no concern he starts, 1 = some doubt (knock, rotation, competition), 2 = likely out or benched\n"
          "- outlook: compared with his usual output, will he do better or worse this gameweek? -2 = much worse, "
          "-1 = worse, 0 = no signal / as usual, 1 = better, 2 = much better\n"
          "Reply with one JSON object only: {{\"start_risk\": n, \"outlook\": n}}\n\nArticles:\n{articles}")


def evidence(prompt):
    part = prompt.split("Timestamp-safe text evidence:\n", 1)
    if len(part) < 2 or "No timestamp-safe text evidence is available" in part[1][:200]:
        return None
    return part[1].rsplit("\n<|turn>", 2)[0].strip()


def rate(out_path, model_path):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    rows = []
    for path in SETS:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            ev = evidence(r["prompt"])
            if ev:
                rows.append((r["season"], int(r["week"]), int(m["player_id"]), m["player_name"], m["position"], ev))
    tok = AutoTokenizer.from_pretrained(model_path)
    tok.padding_side = "left"
    # 4-bit: a bf16 31B needs ~120 GB at load on the GB10's unified memory (file pages + GPU copy) and was OOM-killed twice.
    from transformers import BitsAndBytesConfig
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map={"": 0}, quantization_config=BitsAndBytesConfig(
        load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)).eval()
    import os
    done = sum(1 for _ in open(out_path)) if os.path.exists(out_path) else 0  # resume after an interruption
    with open(out_path, "a") as f:
        for start in range(done - done % 8, len(rows), 8):
            batch = rows[start:start + 8]
            texts = [tok.apply_chat_template([{"role": "user", "content": PROMPT.format(name=b[3], position=b[4], articles=b[5])}],
                                             tokenize=False, add_generation_prompt=True) for b in batch]
            enc = tok(texts, return_tensors="pt", padding=True, add_special_tokens=False).to(model.device)
            with torch.no_grad():
                out = model.generate(**enc, max_new_tokens=24, do_sample=False, pad_token_id=tok.pad_token_id,
                                     eos_token_id=[tok.convert_tokens_to_ids("<turn|>"), tok.eos_token_id])
            for b, seq in zip(batch, out[:, enc["input_ids"].shape[1]:]):
                reply = tok.decode(seq, skip_special_tokens=True)
                m = re.search(r"\{[^{}]*\}", reply)
                try:
                    obj = json.loads(m.group(0)) if m else {}
                except json.JSONDecodeError:
                    obj = {}
                f.write(json.dumps({"season": b[0], "week": b[1], "player_id": b[2], "reply": reply,
                                    "start_risk": obj.get("start_risk"), "outlook": obj.get("outlook")}) + "\n")
            f.flush()
            print(f"{start + len(batch)}/{len(rows)}", flush=True)


def auc(score, label):
    order = np.argsort(score); ranks = np.empty(len(score)); ranks[order] = np.arange(1, len(score) + 1)
    pos = label.astype(bool); n1, n0 = pos.sum(), (~pos).sum()
    return float((ranks[pos].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def score(ratings_path, out_md):
    from sklearn.linear_model import LogisticRegression

    meta = {}
    for path in SETS:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            meta[(r["season"], int(r["week"]), int(m["player_id"]))] = m
    R = [json.loads(l) for l in open(ratings_path)]
    ok = [r for r in R if isinstance(r["start_risk"], (int, float)) and isinstance(r["outlook"], (int, float))]
    risk = np.array([float(r["start_risk"]) for r in ok]); out = np.array([float(r["outlook"]) for r in ok])
    keys = [(r["season"], r["week"], r["player_id"]) for r in ok]
    base = np.array([meta[k]["baseline_forecast"]["baseline_points_1gw"] for k in keys])
    papp = np.array([meta[k]["baseline_forecast"]["baseline_appearance_probability"] for k in keys])
    y = np.array([meta[k]["labels"]["points_1gw"] for k in keys]); played = np.array([float(meta[k]["labels"]["minutes_1gw"]) > 0 for k in keys])
    resid = y - base
    lines = ["# Expert-reader test: do the articles carry a signal beyond classic and the market?", "",
             f"{len(R)} player-weeks with articles rated, {len(ok)} parseable (2025-26 GW27-38 + 2026-27 GW2-5, top 96, 12 h cutoff).", "",
             "| Rating | Player-weeks | Classic forecast | Played | Real surprise vs classic |", "|---|---|---|---|---|"]
    for name, sel in [(f"outlook {v:+d}", out == v) for v in (-2, -1, 0, 1, 2)] + [(f"start_risk {v}", risk == v) for v in (0, 1, 2)]:
        if sel.sum() >= 10:
            se = resid[sel].std() / np.sqrt(sel.sum())
            lines.append(f"| {name} | {sel.sum()} | {base[sel].mean():.2f} | {played[sel].mean():.0%} | {resid[sel].mean():+.2f} (± {1.96 * se:.2f}) |")
    corr = np.corrcoef(out, resid)[0, 1]
    lines += ["", f"- Outlook vs real surprise (beyond classic): correlation {corr:+.3f} (95% interval ± {1.96 / np.sqrt(len(ok) - 3):.3f}).",
              "- Not playing: classic P(appear) alone vs with the reader's start_risk (fit on 2025-26, scored on 2026-27):"]
    logit = np.log(np.clip(papp, 0.01, 0.99) / (1 - np.clip(papp, 0.01, 0.99)))
    # per season: 2026-27 GW2-5 has only a handful of non-starters among these players, so its AUC is noise;
    # the combined model is cross-validated within a season (odd weeks fit, even weeks scored) to avoid a
    # season-to-season flip
    lines.append("  | Season | Player-weeks | Did not play | AUC classic P(appear) | AUC reader start_risk | AUC both (within-season CV) |")
    lines.append("  |---|---|---|---|---|---|")
    for season in sorted({k[0] for k in keys}):
        sel = np.array([k[0] == season for k in keys]); wk = np.array([k[1] for k in keys])
        y_s = played[sel]
        if (~y_s).sum() < 2:
            lines.append(f"  | {season} | {sel.sum()} | {(~y_s).sum()} | too few non-starters | | |")
            continue
        a_p, a_r = auc(papp[sel], y_s), auc(-risk[sel], y_s)
        pred = np.zeros(sel.sum())
        odd = (wk[sel] % 2 == 1)
        for fit, sc in ((odd, ~odd), (~odd, odd)):
            Xs = np.column_stack([logit[sel], risk[sel]])
            pred[sc] = LogisticRegression().fit(Xs[fit], y_s[fit]).predict_proba(Xs[sc])[:, 1]
        lines.append(f"  | {season} | {sel.sum()} | {(~y_s).sum()} | {a_p:.3f} | {a_r:.3f} | {auc(pred, y_s):.3f} |")
    open(out_md, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    if sys.argv[1] == "rate":
        model = sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else "/home/wescheng/models/gemma-4-31b-it"
        rate(sys.argv[2], model)
    else:
        score(sys.argv[2], sys.argv[3])

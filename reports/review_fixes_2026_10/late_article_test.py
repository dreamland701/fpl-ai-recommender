"""How much does E20 lean on articles from the last 24 hours before the deadline?

Live decisions snapshot ~17 h before the deadline, but the training, holdout and live-season
test prompts admitted articles right up to it. This rebuilds those prompts with articles
from the final 24 hours removed (the no-evidence sentence when none are left), so only the
changed rows need decoding, then merges the new decodes with the originals.

usage:
  late_article_test.py prepare <eval.jsonl> <out_changed.jsonl>
  late_article_test.py merge <eval.jsonl> <orig_preds.jsonl> <changed_preds.jsonl> <out_preds.jsonl>
"""
import json
import re
import sys
from datetime import datetime

CUTOFF_HOURS = 24.0
HEAD = "Timestamp-safe text evidence:\n"
TAIL = "\n<|turn>\n<|turn>model\n"
NO_EVIDENCE = ("No timestamp-safe text evidence is available for this player-week. "
               "Without evidence, prefer deltas at or near zero.")
TS = re.compile(r"^\[\d+\] [^|\n]+\| (\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)")


def strip_late(prompt, deadline):
    head, sep, rest = prompt.partition(HEAD)
    if not sep or "No timestamp-safe text evidence" in rest[:200]:
        return prompt
    body, tail = rest[: rest.rfind(TAIL)], rest[rest.rfind(TAIL):]
    docs = [d for d in re.split(r"\n(?=\[\d+\] )", body.strip()) if d.strip()]
    keep = []
    for d in docs:
        m = TS.match(d.strip())
        if m and (deadline - datetime.fromisoformat(m.group(1).replace("Z", "+00:00"))).total_seconds() / 3600 < CUTOFF_HOURS:
            continue
        keep.append(d.strip())
    if len(keep) == len(docs):
        return prompt
    if not keep:
        return head + sep + NO_EVIDENCE + tail
    renumbered = [re.sub(r"^\[\d+\]", f"[{i}]", d) for i, d in enumerate(keep, start=1)]
    return head + sep + "\n\n".join(renumbered) + tail


def key(r):
    return str(r["season"]), int(r["week"]), int(r["metadata"]["player_id"])


def main() -> None:
    mode = sys.argv[1]
    if mode == "prepare":
        src, out = sys.argv[2], sys.argv[3]
        n = changed = emptied = 0
        with open(out, "w") as f:
            for line in open(src):
                r = json.loads(line); n += 1
                deadline = datetime.fromisoformat(r["deadline_ts"].replace("Z", "+00:00"))
                new = strip_late(r["prompt"], deadline)
                if new != r["prompt"]:
                    changed += 1
                    emptied += NO_EVIDENCE in new
                    f.write(json.dumps({**r, "prompt": new}) + "\n")
        print(f"{src}: {changed}/{n} prompts changed ({emptied} left with no evidence) -> {out}")
    elif mode == "merge":
        src, orig, new, out = sys.argv[2:6]
        replaced = {key(json.loads(l)): l for l in open(new) if l.strip()}
        originals = {key(json.loads(l)): l for l in open(orig) if l.strip()}
        with open(out, "w") as f:
            for line in open(src):
                k = key(json.loads(line))
                f.write(replaced.get(k, originals[k]).rstrip("\n") + "\n")
        print(f"merged {len(replaced)} re-decoded rows into {out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Assemble the extraction-pilot report: extraction vs reference, with
blank/'nothing' cases explicitly surfaced (Wes: quality failures must be
visible, never silent). Applies G2's validated tail-cleanup and bare-
'nothing' sentinel handling at read time."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location("adj", ROOT / "scripts" / "build_adjusted_grpo_states.py")
adj = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(adj)

refs = {json.loads(l)["pilot_index"]: json.loads(l) for l in (ROOT / "reports" / "evidence_extraction_pilot_reference.jsonl").open()}
import sys
pred_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "reports" / "evidence_extraction_pilot_predictions.jsonl"
preds = [json.loads(l) for l in pred_path.open()]
preds.sort(key=lambda r: r.get("pilot_index", 10**9))

out = []
blanks = 0
for i, pred in enumerate(preds):
    ref = refs[i]
    raw = str(pred.get("response") or "")
    cleaned = adj.clean_condensation_response(raw)
    is_blank = cleaned.rstrip(".").strip().lower() == "nothing" or not cleaned.strip()
    blanks += is_blank
    out.append({**ref, "extraction_raw": raw[:400], "extraction": cleaned, "blank": is_blank})

report_path = ROOT / "reports" / (pred_path.stem.replace("predictions", "report") + ".json")
report_path.write_text(json.dumps(out, indent=1, ensure_ascii=False))
print(f"pilot report: {len(out)} extractions, {blanks} blank ({blanks/len(out):.0%}) -> {report_path.name}")
print()
for r in out:
    tag = "BLANK" if r["blank"] else "text "
    print(f"[{tag}] #{r['pilot_index']:>2} {r['kind']:<14} {str(r['player'])[:22]:<22} {str(r['source'])[:16]:<16} {str(r['title'])[:52]}")
    if not r["blank"]:
        print(f"        -> {r['extraction'][:220]}")

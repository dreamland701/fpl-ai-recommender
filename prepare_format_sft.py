from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "reports" / "llm_sft_split_2025_26_gw11_30"
OUTPUT_DIR = ROOT / "reports" / "llm_sft_split_2025_26_gw11_30_format_v3"

STRICT_SYSTEM_PROMPT = (
    "You are an FPL decision assistant. Base recommendations on structured forecasts first, "
    "then use timestamp-safe curated evidence for injury/news adjustments. "
    "Return exactly one valid JSON object with keys transfers, captain, vice_captain, starters, "
    "bench_order, chip, reasoning_summary. Do not output markdown, code fences, analysis, or any text "
    "before or after the JSON object. For each transfer use keys players_out, players_in, projected_gain, hit_cost."
)


def _load_jsonl(path: Path) -> List[Dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _write_jsonl(path: Path, records: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def _parse_response_json(value: Any) -> Optional[Dict[str, Any]]:
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start >= 0 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                return None
    return None


def _string_list(value: Any) -> List[str]:
    if not isinstance(value, list):
        return []
    cleaned: List[str] = []
    for item in value:
        text = str(item).strip()
        if text:
            cleaned.append(text)
    return cleaned


def _normalize_transfer(transfer: Any) -> Optional[Dict[str, Any]]:
    if not isinstance(transfer, Mapping):
        return None
    players_out = _string_list(transfer.get("players_out"))
    players_in = _string_list(transfer.get("players_in"))
    if not players_out and not players_in:
        players_out = _string_list(transfer.get("out"))
        players_in = _string_list(transfer.get("in"))
    if isinstance(transfer.get("out"), str):
        players_out = [str(transfer["out"]).strip()]
    if isinstance(transfer.get("in"), str):
        players_in = [str(transfer["in"]).strip()]
    projected_gain = transfer.get("projected_gain", transfer.get("gain", 0.0))
    hit_cost = transfer.get("hit_cost", transfer.get("hit", 0))
    return {
        "players_out": players_out,
        "players_in": players_in,
        "projected_gain": round(float(projected_gain or 0.0), 2),
        "hit_cost": int(hit_cost or 0),
    }


def _normalize_bundle(payload: Mapping[str, Any]) -> Dict[str, Any]:
    transfers = payload.get("transfers")
    normalized_transfers = []
    if isinstance(transfers, list):
        for transfer in transfers:
            normalized = _normalize_transfer(transfer)
            if normalized is not None:
                normalized_transfers.append(normalized)
    reasoning_summary = payload.get("reasoning_summary")
    if isinstance(reasoning_summary, str):
        reasoning_summary = [reasoning_summary.strip()] if reasoning_summary.strip() else []
    return {
        "transfers": normalized_transfers,
        "captain": str(payload.get("captain", "")).strip(),
        "vice_captain": str(payload.get("vice_captain", "")).strip(),
        "starters": _string_list(payload.get("starters")),
        "bench_order": _string_list(payload.get("bench_order")),
        "chip": str(payload.get("chip", "none") or "none").strip(),
        "reasoning_summary": _string_list(reasoning_summary),
    }


def _normalize_messages(messages: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    normalized: List[Dict[str, str]] = []
    for message in messages:
        role = str(message.get("role", "")).strip()
        content = message.get("content", "")
        if role == "system":
            normalized.append({"role": "system", "content": STRICT_SYSTEM_PROMPT})
        elif role == "assistant":
            parsed = _parse_response_json(content)
            if parsed is None:
                raise ValueError("Assistant message is not parseable JSON")
            canonical = _normalize_bundle(parsed)
            normalized.append(
                {
                    "role": "assistant",
                    "content": json.dumps(canonical, ensure_ascii=False, separators=(",", ":")),
                }
            )
        else:
            normalized.append({"role": role, "content": str(content)})
    if not any(message["role"] == "system" for message in normalized):
        normalized.insert(0, {"role": "system", "content": STRICT_SYSTEM_PROMPT})
    return normalized


def _normalize_record(record: Dict[str, Any]) -> Dict[str, Any]:
    normalized = dict(record)
    normalized["messages"] = _normalize_messages(list(record.get("messages", [])))
    return normalized


def main() -> None:
    summary: Dict[str, Any] = {"splits": {}}
    for split_name in ("train", "eval"):
        input_path = SOURCE_DIR / f"{split_name}.jsonl"
        output_path = OUTPUT_DIR / f"{split_name}.jsonl"
        records = _load_jsonl(input_path)
        normalized_records = [_normalize_record(record) for record in records]
        _write_jsonl(output_path, normalized_records)
        summary["splits"][split_name] = {
            "input": str(input_path),
            "output": str(output_path),
            "examples": len(normalized_records),
        }
    summary_path = OUTPUT_DIR / "summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()

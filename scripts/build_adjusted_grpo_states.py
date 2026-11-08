"""Build LLM-adjusted GRPO state caches (deployment-regime G2 training data).

Per Wes's 2026-07-18 direction: G2 must train on the forecasts it will see
at GW x — classic ridge adjusted by the chronologically legal scout-evidence
adapter — plus the *why*: per-player deltas and evidence snippets in the
state, so the decision policy can act on what the text moved.

For each season's state cache this script:
  1. loads adapter predictions from one or more (surface eval.jsonl,
     predictions.jsonl) pairs and applies bounded deltas to every state's
     forecast pool (fields=all, same pipeline as the gate backtests);
  2. records each adjusted player's delta_points_1gw / delta_appearance
     in a per-state `llm_deltas` map (the distilled text signal);
  3. attaches a per-player evidence snippet from corpus v7 — either a
     mention-centered window (--snippet-mode window, default) or an
     LLM-condensed summary (--snippet-mode llm --summaries <jsonl>);
  4. writes reports/grpo_states_adjusted/{season}.jsonl (same schema as
     build_grpo_state_cache.py plus the two optional maps — the loader
     treats both as optional).

--emit-condense-prompts writes an examples JSONL of condensation prompts
(one per player-week document) for eval_gemma_responses.py; its output
feeds back via --summaries. Greedy decode + this cache = deterministic.

Chronological legality map (adapter trained-through → may adjust):
  chrono-2425 (thru 24-25 GW11) → 2024-25 GW12-38, all 2025-26
  chrono-2324 (thru 23-24 GW11) → 2023-24 GW12-38, 2024-25 GW2-11
  E7          (thru 25-26 GW11) → 2025-26 GW12-30 (the held-out eval)
2022-23 and 2023-24 GW2-11 have no legal adapter and are not built here.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.llm_adjust import apply_llm_deltas, load_llm_delta_lookup  # noqa: E402

CORPUS = ROOT / "reports" / "llm_player_forecast_multiseason_2022_26_baseline_adjustment_v7_scout.jsonl"
STATES_DIR = ROOT / "reports" / "grpo_states"
R = ROOT / "reports"

# season key -> list of (surface eval.jsonl, sft predictions.jsonl)
SURFACES: dict[str, list[tuple[Path, Path]]] = {
    "2023-24": [
        (
            R / "llm_residual_v2_e7chrono2324_top256_scout_thru_2324gw11_eval_2324gw12_38" / "eval.jsonl",
            R / "gemma4_e4b_residual_e7chrono2324_2324gw12_38_sft_predictions.jsonl",
        ),
    ],
    "2024-25": [
        (
            R / "llm_residual_v2_e7chrono2425_evalext_2425gw12_38" / "eval.jsonl",
            R / "gemma4_e4b_residual_e7chrono2425_evalext_2425gw12_38_sft_predictions.jsonl",
        ),
        (
            R / "llm_residual_v2_e7chrono2324_evalext_2425gw2_11" / "eval.jsonl",
            R / "gemma4_e4b_residual_e7chrono2324_evalext_2425gw2_11_sft_predictions.jsonl",
        ),
    ],
    "2025-26-early": [
        (
            R / "llm_residual_v2_e7chrono2425_evalext_2526gw2_11" / "eval.jsonl",
            R / "gemma4_e4b_residual_e7chrono2425_evalext_2526gw2_11_sft_predictions.jsonl",
        ),
    ],
    "2025-26": [
        (
            R / "llm_residual_v2_e7_top256_scout_evidence_thru_gw11_eval_gw12_30" / "eval.jsonl",
            R / "gemma4_e4b_residual_e7_top256_gw12_30_sft_predictions.jsonl",
        ),
    ],
}

SCOUT_TITLE_PATTERN = re.compile(r"scout report|team news|predicted line|preview|tips", re.IGNORECASE)
SNIPPET_CHARS = 180
CONDENSE_ARTICLE_CHARS = 1200


def clean_condensation_response(text: str) -> str:
    """Strip trailing decoding-artifact garbage from base-model free-text
    completions: the custom <|turn|> template's stop cue is learned by
    JSON-task adapters (which halt right after the closing brace) but the
    base model has no such training for free-text answers here, so greedy
    decoding sometimes runs on past the real answer into stray non-Latin
    tokens or repeated-symbol tails (e.g. "...Fulham.แ", "nothingแ>>>>>")."""
    text = text.strip()
    while text and (ord(text[-1]) > 127 or text[-1] in "<>~=_*"):
        text = text[:-1].rstrip()
    return text


def load_evidence_index(seasons: set[str]) -> dict[tuple[str, int, int], list[dict]]:
    """(season, week, player_id) -> evidence documents, scout-titled first."""
    index: dict[tuple[str, int, int], list[dict]] = {}
    with CORPUS.open() as handle:
        for line in handle:
            row = json.loads(line)
            if row["season"] not in seasons:
                continue
            meta = row["metadata"]
            docs = meta.get("evidence_documents") or []
            if not docs:
                continue
            docs = sorted(
                docs,
                key=lambda doc: 0 if SCOUT_TITLE_PATTERN.search(str(doc.get("title") or "")) else 1,
            )
            index[(row["season"], int(row["week"]), int(meta["player_id"]))] = docs
    return index


def mention_window(content: str, player_name: str, width: int = SNIPPET_CHARS) -> str:
    """Window centered on the player's (last-)name mention; head fallback."""
    content = " ".join(content.split())
    needle = player_name.split()[-1] if player_name else ""
    pos = content.lower().find(needle.lower()) if needle else -1
    if pos == -1:
        return content[:width].rsplit(" ", 1)[0]
    start = max(0, pos - width // 2)
    window = content[start : start + width]
    if start > 0:
        window = window.split(" ", 1)[-1]
    return window.rsplit(" ", 1)[0] if len(window) == width else window


def window_snippet(docs: list[dict], player_name: str) -> str:
    doc = docs[0]
    content = str(doc.get("content") or doc.get("snippet") or "")
    return mention_window(content, player_name)


def condense_prompt(doc: dict, player_name: str) -> str:
    content = " ".join(str(doc.get("content") or doc.get("snippet") or "").split())[:CONDENSE_ARTICLE_CHARS]
    return (
        f"Article ({doc.get('source_name') or 'unknown'}, {doc.get('published_at') or ''}): "
        f"{doc.get('title') or ''}\n{content}\n\n"
        f"In at most 30 words, state only what this article says about {player_name} "
        "that matters for fantasy football (starts, fitness, form, set pieces, rotation). "
        "Facts from the text only. If it says nothing about him, reply: nothing."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seasons", default="2023-24,2024-25,2025-26-early,2025-26")
    parser.add_argument("--snippet-mode", choices=["window", "llm"], default="window")
    parser.add_argument("--summaries", help="predictions JSONL from the condensation pass (llm mode)")
    parser.add_argument("--emit-condense-prompts", help="write condensation examples JSONL here and exit")
    parser.add_argument("--output-dir", default=str(R / "grpo_states_adjusted"))
    parser.add_argument("--allow-missing-predictions", action="store_true",
                        help="skip surfaces whose predictions are absent (partial build)")
    args = parser.parse_args()

    seasons = [season.strip() for season in args.seasons.split(",") if season.strip()]
    evidence = load_evidence_index({season.replace("-early", "") for season in seasons})
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.emit_condense_prompts:
        rows = []
        seen: set[tuple[str, int, int]] = set()
        for season in seasons:
            corpus_season = season.replace("-early", "")
            for state in load_states(STATES_DIR / f"{season}.jsonl"):
                # Only players that can surface in a plan prompt: the squad
                # plus the top candidates (top-30 for margin vs the prompt's
                # top-20, since adjusted forecasts reorder slightly).
                squad_ids = {player.player_id for player in state.squad}
                candidates = sorted(
                    (f for f in state.forecasts if f.player_id not in squad_ids),
                    key=lambda f: f.predicted_points_3gw,
                    reverse=True,
                )[:30]
                prompt_players = [f for f in state.forecasts if f.player_id in squad_ids] + candidates
                for forecast in prompt_players:
                    key = (corpus_season, state.week, forecast.player_id)
                    docs = evidence.get(key)
                    if not docs or key in seen:
                        continue
                    seen.add(key)
                    rows.append({
                        "season": season, "week": state.week,
                        "messages": [
                            {"role": "user", "content": condense_prompt(docs[0], forecast.player_name)},
                        ],
                        "completion": "",
                        "metadata": {"season": season, "week": state.week, "player_id": forecast.player_id},
                    })
        with open(args.emit_condense_prompts, "w") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        print(f"wrote {len(rows)} condensation prompts -> {args.emit_condense_prompts}")
        return

    summaries: dict[tuple[str, int, int], str] = {}
    if args.snippet_mode == "llm":
        if not args.summaries:
            raise SystemExit("--snippet-mode llm requires --summaries")
        with open(args.summaries) as handle:
            for line in handle:
                row = json.loads(line)
                meta = row.get("metadata") or {}
                text = " ".join(str(row.get("response") or "").split())
                text = clean_condensation_response(text)
                if text and text.rstrip(".").lower() != "nothing":
                    summaries[(meta["season"], int(meta["week"]), int(meta["player_id"]))] = text[:SNIPPET_CHARS]

    for season in seasons:
        corpus_season = season.replace("-early", "")
        lookups = []
        for surface, predictions in SURFACES[season]:
            if not predictions.exists():
                message = f"missing predictions {predictions}"
                if args.allow_missing_predictions:
                    print(f"WARN {season}: {message} — skipping surface")
                    continue
                raise SystemExit(f"{season}: {message}")
            lookups.append(load_llm_delta_lookup(surface, predictions))
        raw_rows = [json.loads(line) for line in open(STATES_DIR / f"{season}.jsonl")]
        states = load_states(STATES_DIR / f"{season}.jsonl")
        adjusted_weeks = 0
        out_path = out_dir / f"{season}.jsonl"
        with out_path.open("w") as handle:
            for raw, state in zip(raw_rows, states):
                merged: dict[tuple[int, int], dict] = {}
                for lookup in lookups:
                    for key, value in lookup.items():
                        if len(key) == 3 and key[0] != corpus_season:
                            continue
                        if key[-2] == state.week:
                            merged[(key[-2], key[-1])] = dict(value)
                adjusted = apply_llm_deltas(state.forecasts, merged, state.week, fields="all")
                deltas_map = {}
                for player_id_key in merged:
                    deltas = merged[player_id_key]
                    deltas_map[player_id_key[1]] = {
                        "d1": round(deltas.get("delta_points_1gw", 0.0), 1),
                        "dP": round(deltas.get("delta_appearance_probability", 0.0), 2),
                    }
                snippets = {}
                for forecast in state.forecasts:
                    key = (corpus_season, state.week, forecast.player_id)
                    if args.snippet_mode == "llm":
                        text = summaries.get((season, state.week, forecast.player_id), "")
                    else:
                        docs = evidence.get(key)
                        text = window_snippet(docs, forecast.player_name) if docs else ""
                    if text:
                        snippets[forecast.player_id] = text
                if merged:
                    adjusted_weeks += 1
                raw["forecasts"] = [
                    {
                        "player_id": f.player_id, "player_name": f.player_name, "team_id": f.team_id,
                        "position": f.position, "price": f.price, "predicted_minutes": f.predicted_minutes,
                        "predicted_points_1gw": f.predicted_points_1gw,
                        "predicted_points_3gw": f.predicted_points_3gw,
                        "predicted_points_5gw": f.predicted_points_5gw,
                        "appearance_probability": f.appearance_probability,
                        "fixture_count": f.fixture_count, "uncertainty": f.uncertainty,
                    }
                    for f in adjusted
                ]
                raw["llm_deltas"] = {str(k): v for k, v in deltas_map.items()}
                raw["evidence_snippets"] = {str(k): v for k, v in snippets.items()}
                handle.write(json.dumps(raw, ensure_ascii=False) + "\n")
        print(f"{season}: {len(states)} states -> {out_path} ({adjusted_weeks} weeks with deltas)")


if __name__ == "__main__":
    main()

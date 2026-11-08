"""Read-only review diagnostics. All generated outputs stay under Codex/.

Run from repository root using the existing fpl-gemma-lite environment.
No API calls, model downloads, GPU inference, or production modifications.
"""
from __future__ import annotations

import copy
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys
from dataclasses import replace
from unittest.mock import patch

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai import dataset as ds
from fpl_ai.backtest import _training_frame_for_week, _apply_automatic_substitutions, _refresh_squad_prices
from fpl_ai.config import STARTING_FORMATIONS
from fpl_ai.decision import _optimize_lineup
from fpl_ai.grpo_env import WeeklyState, load_states
from fpl_ai.grpo_plan_env import PlanAction, PlanEpisodeEnv, build_episodes, parse_plan
from fpl_ai.llm_adjust import parse_delta_response, apply_llm_deltas
from fpl_ai.types import PlayerForecast, SquadPlayer

OUT = ROOT / "Codex" / "analysis"
OUT.mkdir(parents=True, exist_ok=True)


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, default=str, allow_nan=False) + "\n")
    print(f"Wrote {name}", flush=True)


def jsonl(path):
    with Path(path).open() as f:
        return [json.loads(line) for line in f if line.strip()]


def metrics(y, pred):
    y, pred = np.asarray(y), np.asarray(pred)
    return {"n": len(y), "mae": float(np.mean(np.abs(y-pred))),
            "rmse": float(np.sqrt(np.mean((y-pred)**2))),
            "mean_prediction": float(pred.mean()), "mean_actual": float(y.mean()),
            "bias_pred_minus_actual": float((pred-y).mean())}


def artifact_inventory():
    files = sorted(set(ROOT.glob("src/fpl_ai/*.py")) | set(ROOT.glob("scripts/*.py")) |
                   set(ROOT.glob("train_*.py")) | set(ROOT.glob("tests/*.py")))
    versions = {}
    for package in ["numpy", "pandas", "torch", "trl", "transformers", "peft", "pytest", "scipy", "scikit-learn"]:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    write("provenance.json", {"python": sys.version, "executable": sys.executable,
          "versions": versions, "source_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}})
    summaries = []
    for p in sorted((ROOT / "reports").glob("*_eval_summary.json")):
        d = json.loads(p.read_text())
        if "classic_ml" not in d or "sft_gemma_delta" not in d:
            continue
        row = {"path": str(p.relative_to(ROOT))}
        for model in ("classic_ml", "sft_gemma_delta"):
            for k, v in d[model].items():
                if isinstance(v, (float, int)):
                    row[model+"__"+k] = v
        summaries.append(row)
    pd.DataFrame(summaries).to_csv(OUT / "experiment_metrics.csv", index=False)
    backtests = []
    for p in sorted((ROOT / "reports").glob("backtest*/rolling_squad_backtest.json")):
        d = json.loads(p.read_text())
        backtests.append({"path": str(p.relative_to(ROOT)), **{k: d.get(k) for k in
            ("test_season", "simulated_weeks", "total_actual_points", "total_transfer_hits", "total_predicted_points")}})
    write("backtest_inventory.json", backtests)


def table_audit():
    frame = pd.read_csv(ROOT / "data/fpl_training_rows_blend_f6.csv", low_memory=False)
    data = ds.CanonicalDataset(frame)
    seasons = frame.groupby("season").agg(rows=("week", "size"), week_min=("week", "min"), week_max=("week", "max"))
    selected = _training_frame_for_week(data, "2025-26", 27)
    overlap = {}
    for horizon in [1, 3, 5]:
        unsafe = selected[(selected.season == "2025-26") & (selected.week + horizon - 1 >= 27)]
        overlap[str(horizon)] = {"rows": len(unsafe), "origin_weeks": sorted(unsafe.week.unique().tolist())}
    example = frame[(frame.season == "2025-26") & (frame.player_name.str.contains("Haaland")) & frame.week.between(23, 30)]
    write("table_audit.json", {"rows": len(frame), "seasons": seasons.reset_index().to_dict("records"),
        "features": list(data.feature_columns), "position_in_features": "position" in data.feature_columns,
        "duplicate_player_week_keys": int(frame.duplicated(["season", "week", "player_id"]).sum()),
        "train_rows_before_2526_gw27": len(selected), "label_overlap_at_2526_gw27": overlap,
        "example_player": example[["season", "week", "player_id", "player_name", "label_points_1gw", "label_points_3gw", "label_points_5gw"]].to_dict("records"),
        "minutes_above_90_single_fixture_rows": int(((frame.label_minutes_1gw > 90) & (frame.fixture_count == 1)).sum())})
    return frame


def units_and_status(frame):
    records=[]
    for season,g in frame.groupby("season"):
        raw=pd.read_csv(ROOT/f"data/fpl_history/{season}/merged_gw.csv",nrows=1)
        records.append({"season":season,
            "ownership_max":float(g.selected_by_percent_pre_deadline.max()),
            "ownership_median":float(g.selected_by_percent_pre_deadline.median()),
            "fraction_ownership_gt100":float((g.selected_by_percent_pre_deadline>100).mean()),
            "flagged_rate":float(g.status_flag_pre_deadline.mean()),
            "flag_change_players_after_w1":int((g[g.week>1].groupby("player_id").status_flag_pre_deadline.nunique()>1).sum()),
            "players":int(g.player_id.nunique()),"raw_has_status":"status" in raw,
            "gw1_zero_prices":int(((g.week==1)&(g.price_pre_deadline==0)).sum())})
    write("units_and_status.json",records)
    g=frame[frame.season=="2025-26"]
    prefix=g[g.week<27]
    write("season_centering.json",{"season":"2025-26","cutoff_week":27,
        "full_season_opponent_conceded_mean":float(g.opponent_goals_against_avg_3.mean()),
        "prefix_opponent_conceded_mean":float(prefix.opponent_goals_against_avg_3.mean()),
        "note":"F6 builds league_mean using all rows of a season before the training split. Changing future rows therefore changes earlier feature values. This diagnostic establishes dependence, not performance impact."})


def toy_state(week=12):
    positions = ["GK"]*2 + ["DEF"]*5 + ["MID"]*5 + ["FWD"]*3
    squad, forecasts = [], []
    for i, pos in enumerate(positions, 1):
        score = 10.0 if pos in ("DEF", "FWD") else 1.0
        squad.append(SquadPlayer(i, f"P{i}", i, pos, 5.0))
        forecasts.append(PlayerForecast("2025-26", week, i, f"P{i}", i, pos, 5.0,
            90., score, score*3, score*5, 1., 1, .1))
    return WeeklyState("2025-26", week, squad, 0., 1, forecasts,
                       {i: 2. for i in range(1,16)}, {i: 90. for i in range(1,16)})


def code_probes():
    s = toy_state()
    lookup = {f.player_id: f for f in s.forecasts}
    starters, bench, captain, vice, score = _optimize_lineup(s.squad, lookup)
    ideal_523 = [1,3,4,5,6,7,8,9,13,14,15]
    # Four absent outfield starters, but three available legal replacements.
    # Keep the nominal formation legal by removing MID/FWD slots that can
    # be replaced by the three actual bench players.
    normal_starters = [1,3,4,5,8,9,10,11,13,14,15]  # 3-4-3
    normal_bench = [2,6,7,12]
    minutes = dict(s.actual_minutes)
    for pid in (8,9,13,14):
        minutes[pid] = 0.
    final, notes = _apply_automatic_substitutions(s.squad, normal_starters, normal_bench, s.actual_points, minutes)
    env = PlanEpisodeEnv([s, toy_state(13)])
    before = env.state_prompt()
    future = copy.deepcopy(env.states[1])
    future = replace(future, forecasts=[replace(f, predicted_points_1gw=f.predicted_points_1gw+100) for f in future.forecasts])
    after = PlanEpisodeEnv([s, future]).state_prompt()
    default_score = env.baseline_total()
    boosted_score, _ = env.rollout([PlanAction(chip_play="bench_boost"), PlanAction()])
    ndjson = '\n'.join([json.dumps({"bank_transfer": True}), json.dumps({"chip_play": "bench_boost"})])
    parsed = parse_plan(ndjson, 2)
    _, _, _, next_ft, _ = env._week_realized(s, s.squad, 0., 4, PlanAction(bank_transfer=True))
    priced = _refresh_squad_prices([s.squad[0]], pd.DataFrame([{"player_id":1,"price":5.4,"price_pre_deadline":5.3}]))
    low = replace(s.forecasts[0], predicted_points_1gw=0.1)
    neg = apply_llm_deltas([low], {(12,1):{"delta_points_1gw":-2.}}, 12)[0]
    write("code_probes.json", {
        "missing_523": {"formations": list(STARTING_FORMATIONS), "chosen_score": score,
                        "legal_523_score": sum(lookup[i].predicted_points_1gw for i in ideal_523)},
        "partial_autosubs": {"absent_outfield": [8,9,13,14], "available_bench_outfield": [6,7,12],
                           "final_starters": final, "actual_subs": [i for i in normal_bench if i in final],
                           "expected_available_legal_subs": [6,7,12], "notes": notes},
        "future_information_prompt": {"future_forecast_only_change_alters_start_prompt": before != after,
            "before_outlook": before.split("Week-by-week outlook:")[1].split("Output a strict")[0],
            "after_outlook": after.split("Week-by-week outlook:")[1].split("Output a strict")[0]},
        "free_chip_advantage": {"no_chip_baseline": default_score, "otherwise_default_with_bench_boost": boosted_score, "gain": boosted_score-default_score},
        "ndjson_plan_partial_acceptance": {"input": ndjson, "parse_succeeds": parsed is not None,
           "result": [a.__dict__ for a in parsed]},
        "bank_four_free_transfers": {"expected_next_current_rules":5, "actual_next":next_ft},
        "selling_price": {"purchase":5., "market":5.4, "expected_current_rules":5.2, "actual":priced[0].sell_price},
        "negative_forecast_application": {"baseline":0.1, "delta":-2., "backtest_result":neg.predicted_points_1gw, "live_script_result":0.},
        "nonfinite_parser": {"nan_input_result":parse_delta_response('{"delta_points_1gw":NaN}')}
    })


def live_analysis(frame):
    results, all_records = [], []
    for week in range(1,6):
        if week == 1:
            ex = "live_gw1_2627_examples_wed.jsonl"; pred = "live_gw1_2627_e10_predictions_wed.jsonl"
        elif week == 2:
            ex = "live_gw2_2627_examples_v2.jsonl"; pred = "live_gw2_2627_e11full_predictions_v2.jsonl"
        elif week == 4:
            ex = "live_gw4_2627_examples_v2.jsonl"; pred = "live_gw4_2627_e11full_predictions.jsonl"
        else:
            ex = f"live_gw{week}_2627_examples.jsonl"; pred = f"live_gw{week}_2627_e11full_predictions.jsonl"
        examples, predictions = jsonl(ROOT/"reports"/ex), jsonl(ROOT/"reports"/pred)
        actual = frame[(frame.season == "2026-27") & (frame.week == week)].set_index("player_id")
        rows, mismatches, parse_fail = [], 0, 0
        for e,p in zip(examples,predictions):
            md = e["metadata"]; pid = md["player_id"]; base = md["baseline_forecast"]
            mismatches += p.get("metadata",{}).get("player_id",pid) != pid
            if pid not in actual.index:
                continue
            d = parse_delta_response(p.get("response", ""))
            parse_fail += d is None
            d = d or {}
            b = base["baseline_points_1gw"]; prob = base["baseline_appearance_probability"]
            r = {"week":week,"player_id":pid,"name":md["player_name"],"position":md["position"],
                 "baseline":b,"adjusted":max(0,b+d.get("delta_points_1gw",0)),"delta":d.get("delta_points_1gw",0),
                 "p_baseline":prob,"p_adjusted":np.clip(prob+d.get("delta_appearance_probability",0),0,1),
                 "delta_probability":d.get("delta_appearance_probability",0),
                 "actual":float(actual.loc[pid,"label_points_1gw"]),
                 "appeared":float(actual.loc[pid,"label_appearance_probability"]),
                 "evidence":bool(md.get("evidence_present"))}
            rows.append(r)
        d = pd.DataFrame(rows); all_records.extend(rows)
        subsets = {}
        for label, sub in [("all_matched",d),("baseline_probability_ge_05",d[d.p_baseline>=.5])]:
            subsets[label] = {"classic":metrics(sub.actual,sub.baseline),"sft":metrics(sub.actual,sub.adjusted),
                "classic_brier":float(np.mean((sub.appeared-sub.p_baseline)**2)),
                "sft_brier":float(np.mean((sub.appeared-sub.p_adjusted)**2))}
            for key in ("baseline","adjusted"):
                subsets[label][key+"_unconstrained_top11_actual_sum"] = float(sub.nlargest(11,key).actual.sum())
        results.append({"week":week,"examples":ex,"predictions":pred,"example_rows":len(examples),
            "prediction_rows":len(predictions),"id_mismatches":mismatches,"parse_failures":parse_fail,
            "matched_actual_rows":len(d),"zero_probability_deltas":int((d.delta_probability==0).sum()),
            "evidence_fraction":float(d.evidence.mean()),"mean_point_delta":float(d.delta.mean()),"subsets":subsets})
    pd.DataFrame(all_records).to_csv(OUT/"live_forecast_rows.csv",index=False)
    ledger = jsonl(ROOT/"reports/season_2627_ledger.jsonl")
    simple = [{"week":x["gw"],"actual":x.get("actual",x.get("final_actual")),
               "average":x.get("league_avg",x.get("league_average"))} for x in ledger]
    write("live_analysis.json", {"ledger":simple,"total_actual":sum(x["actual"] for x in simple),
        "sum_weekly_averages":sum(x["average"] for x in simple),"forecast_metrics":results,
        "warning":"These are saved player forecasts, not a replay of final entered squads. Top11 is unconstrained and is not legal squad performance. Current settled historical labels used for scoring."})


def e19_decomposition():
    d = json.loads((ROOT/"reports/e4b_residual_e19_gw27_38_eval_rows.json").read_text())
    rows = pd.DataFrame(d["sft_rows"])
    parts = []
    for week,g in rows.groupby("week"):
        x = g.baseline_points_1gw.to_numpy(); delta = g.delta_points_1gw.to_numpy()
        a = np.column_stack([np.ones(len(x)), x])
        coef = np.linalg.lstsq(a,delta,rcond=None)[0]
        fitted = a@coef
        z = g.copy(); z["shrink_only"] = x+fitted; z["remainder_only"] = x+delta-fitted
        parts.append(z)
    r = pd.concat(parts)
    write("e19_decomposition.json", {"warning":"Per-week regression uses the saved adapter deltas, not outcomes. Descriptive post-hoc mechanism analysis, not a fitted deployable challenger.",
          **{name:metrics(r.target_points_1gw,r[col]) for name,col in
             [("classic","baseline_points_1gw"),("sft","final_points_1gw"),("shrink_only","shrink_only"),("remainder_only","remainder_only")]}})


def prior_parity(frame):
    # The production helper slices to live_season before recomputing form.
    # Compare it with the same helper supplied prior-season context.
    os.environ["FPL_PRIOR_BLEND"] = "1"
    raw = ds.normalize_vaastav_history(ROOT/"data/fpl_history")
    data = ds.CanonicalDataset(frame)
    previous = raw[raw.season == "2025-26"]
    with patch.object(ds, "normalize_vaastav_history", return_value=raw):
        current_only = data._build_next_week_form_features(ROOT/"data/fpl_history","2026-27",6)
        original_build = ds.build_training_frame
        def with_prior(current):
            built = original_build(pd.concat([previous,current], ignore_index=True))
            return built.loc[built.season == "2026-27"]
        with patch.object(ds,"build_training_frame",side_effect=with_prior):
            with_context = data._build_next_week_form_features(ROOT/"data/fpl_history","2026-27",6)
    a = current_only.set_index("code"); b = with_context.set_index("code")
    records=[]
    for code in a.index.intersection(b.index):
        va,vb = float(a.loc[code,"points_avg_3"]),float(b.loc[code,"points_avg_3"])
        if abs(va-vb)>1e-8:
            records.append({"code":int(code),"player":a.loc[code,"player_name"],"live_helper_points_avg_3":va,
                            "with_prior_context_points_avg_3":vb,"absolute_difference":abs(va-vb)})
    records.sort(key=lambda r:r["absolute_difference"],reverse=True)
    write("prior_blend_parity.json", {"week":6,"blend_flag":"1","live_players":len(a),"different_players":len(records),"differences":records})


def rl_naive_benchmark():
    # Same flawed env as the historical reports; this isolates the weakness
    # of their no-chip comparator, not a recommendation for chip timing.
    results=[]
    for label in ["grpo_states","grpo_states_adjusted"]:
        states=load_states(str(ROOT/"reports"/label/"2025-26.jsonl"))
        remaining={1:set(["bench_boost","triple_captain"]),2:set(["bench_boost","triple_captain"])}
        total=base=0.; windows=[]
        for env in build_episodes(states,horizon=6,stride=6):
            env.available_chips={k:frozenset(v) for k,v in remaining.items()}
            plan=[]
            for s in env.states:
                half=1 if s.week<=19 else 2
                chip="bench_boost" if "bench_boost" in remaining[half] else ("triple_captain" if "triple_captain" in remaining[half] else "none")
                remaining[half].discard(chip)
                plan.append(PlanAction(chip_play=chip))
            baseline=env.baseline_total(); realized,details=env.rollout(plan)
            base+=baseline;total+=realized
            windows.append({"start":env.states[0].week,"delta":realized-baseline,"chips":[x["chip"] for x in details]})
        results.append({"states":label,"baseline":base,"naive_policy":total,"delta":total-base,"windows":windows})
    write("rl_naive_chip_benchmark.json", {"policy":"Play BB at first opportunity and TC at next opportunity each half; otherwise defaults. No model, no outcome selection.","limitations":"Uses the existing scorer and reset-window squads; not a clean season backtest or ship candidate.","results":results})


if __name__ == "__main__":
    artifact_inventory()
    frame=table_audit()
    units_and_status(frame)
    code_probes()
    live_analysis(frame)
    e19_decomposition()
    rl_naive_benchmark()
    prior_parity(frame)

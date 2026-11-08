"""Is the SFT adapter too conservative? Find the scale on its corrections that fits best.

Each 1GW points delta is split into this week's generic shrink (linear in the
baseline) and the player-specific remainder. For scale factors s, the forecast
classic + s_g * generic + s_p * specific is scored by RMSE (the squared error
that expected-points decisions care about) and MAE. Best s_p near 0 means the
player-specific signal is noise; near 1 means well judged; well above 1 means
too timid. Same for the appearance-probability delta (Brier score).
Training targets were 0.35 x realised residual, clipped to +/-2: shrunk on purpose.

usage: sft_scale_study.py <eval.jsonl> <predictions.jsonl> <label>
"""
import json
import sys

import numpy as np

sys.path.insert(0, "/home/wescheng/projects/fpl/fpl/src")
from fpl_ai.llm_adjust import load_llm_delta_lookup  # noqa: E402

SCALES = [0.0, 0.5, 1.0, 1.5, 2.0, 2.86]


def main() -> None:
    ex_path, pr_path, label = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = [json.loads(l) for l in open(ex_path) if l.strip()]
    lk = load_llm_delta_lookup(ex_path, pr_path)
    week, base, d1, y, pb, dp, app = [], [], [], [], [], [], []
    for r in rows:
        m = r["metadata"]; b = m["baseline_forecast"]
        d = lk.get((m["season"], int(r["week"]), int(m["player_id"])), {})
        week.append(int(r["week"])); base.append(b["baseline_points_1gw"]); d1.append(d.get("delta_points_1gw", 0.0))
        y.append(m["labels"]["points_1gw"]); pb.append(b["baseline_appearance_probability"])
        dp.append(d.get("delta_appearance_probability", 0.0)); app.append(float(m["labels"]["minutes_1gw"]) > 0)
    week, base, d1, y, pb, dp, app = map(np.array, (week, base, d1, y, pb, dp, app))
    generic = np.zeros_like(d1)
    for w in np.unique(week):
        sel = week == w
        slope, intercept = np.polyfit(base[sel], d1[sel], 1)
        generic[sel] = slope * base[sel] + intercept
    specific = d1 - generic
    print(f"{label}: {len(rows)} player-weeks; mean |generic| {np.abs(generic).mean():.2f}, mean |specific| {np.abs(specific).mean():.2f}")
    print("  RMSE (MAE) of classic + s_g*generic + s_p*specific:")
    print("  s_g \\ s_p " + "".join(f"{s:>16.2f}" for s in SCALES))
    for sg in (0.0, 1.0):
        cells = []
        for sp in SCALES:
            err = base + sg * generic + sp * specific - y
            cells.append(f"{np.sqrt(np.mean(err ** 2)):7.4f} ({np.mean(np.abs(err)):.3f})")
        print(f"  {sg:>8.2f}   " + " ".join(cells))
    print("  appearance Brier score of classic + s * delta_P:")
    print("   " + "  ".join(f"s={s}: {np.mean((np.clip(pb + s * dp, 0, 1) - app) ** 2):.4f}" for s in SCALES))


if __name__ == "__main__":
    main()

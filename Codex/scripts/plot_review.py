"""Render saved review measurements; no inference or source-data mutation."""
import json
import os
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/".plot_deps"))
os.environ.setdefault("MPLCONFIGDIR", str(Path(__file__).resolve().parents[1]/"logs/matplotlib"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

out=Path(__file__).resolve().parents[1]/"analysis"
d=json.loads((out/"live_analysis.json").read_text())
fig,axes=plt.subplots(2,2,figsize=(12,8),layout="constrained")
blue,orange="#245d87","#cc6531"
weeks=[x["week"] for x in d["ledger"]]
actual=np.cumsum([x["actual"] for x in d["ledger"]])
average=np.cumsum([x["average"] for x in d["ledger"]])
ax=axes[0,0]
ax.plot(weeks,actual,"o-",color=blue,label="Entered team (ledger)")
ax.plot(weeks,average,"o--",color="#777777",label="Sum of weekly league averages")
ax.set(title="Recorded team performance",ylabel="Cumulative FPL points")
ax.legend(fontsize=9)
for ax,key,title in [(axes[0,1],"mae","All-player absolute error"),(axes[1,0],"rmse","All-player squared-error diagnostic")]:
    for model,color,label in [("classic",blue,"Classic"),("sft",orange,"SFT-adjusted")]:
        values=[w["subsets"]["all_matched"][model][key] for w in d["forecast_metrics"]]
        ax.plot(weeks,values,"o-",color=color,label=label)
    ax.set(title=title,ylabel=f"{key.upper()} (points; lower is better)")
    ax.legend(fontsize=9)
ax=axes[1,1]
for model,color,label,shift in [("baseline",blue,"Classic",-.17),("adjusted",orange,"SFT-adjusted",.17)]:
    values=[w["subsets"]["all_matched"][model+"_unconstrained_top11_actual_sum"] for w in d["forecast_metrics"]]
    ax.bar(np.array(weeks)+shift,values,width=.34,color=color,label=label)
ax.set(title="Unconstrained top-11 ranking diagnostic",ylabel="Actual points (no captain multiplier)")
ax.legend(fontsize=9)
for ax in axes.ravel():
    ax.set_xlabel("2026-27 gameweek")
    ax.set_xticks(weeks)
    ax.grid(axis="y",alpha=.2)
    ax.spines[["top","right"]].set_visible(False)
fig.suptitle("Lower MAE did not translate into a better live ranking diagnostic",fontsize=15)
fig.supxlabel("Five weeks only. Saved forecast populations vary by week. Top-11 ignores budget and formation; it is not a playable team.",fontsize=9)
fig.savefig(out/"review_overview.png",dpi=170)
fig.savefig(out/"review_overview.svg")
print("Saved analysis/review_overview.png and .svg")

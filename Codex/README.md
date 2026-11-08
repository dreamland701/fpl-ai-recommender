# Independent FPL review — 3 October 2026

**Recommendation: repair the data and evaluation contract before spending more GPU time on SFT or RL.** The project has useful foundations, but several confirmed defects make historical improvements unreliable and change the inputs between training and live use. SFT currently improves a metric that is not sufficient for selecting a winning squad. The RL environment does not yet represent the strategy problem you want it to solve.

Start with [REVIEW.md](REVIEW.md), then [PLAN.md](PLAN.md). The actionable code findings are in [CODE_FINDINGS.md](CODE_FINDINGS.md). [EXPERIMENTS.md](EXPERIMENTS.md) documents measurements, limitations, and reproduction commands. [SOURCES.md](SOURCES.md) records official rules and technical references. [HISTORY.md](HISTORY.md) and [LOG.md](LOG.md) preserve the review history.

The most consequential findings:

1. Historical ownership **counts** are supplied as ownership **percentages**; live inference actually uses percentages. One saved SFT example literally says a player is owned by **6,072%** of managers.
2. Historical 3GW/5GW training labels cross prediction cutoffs. The RL plan prompt additionally reads later weeks' forecasts, which would not be available when the plan starts.
3. The live feature builder discards prior-season context before recomputing early-season form. A controlled GW6 reproduction changes the intended points-form input for **420 of 667 players** when that context is restored.
4. Across the five saved live weeks, SFT improves all-player MAE every week but worsens all-player RMSE every week. Its unconstrained top-11 ranking diagnostic never beats the classic baseline in those five weeks.
5. RL gets chips against a baseline with no chips; its actions allow only one transfer per week. A no-model chip schedule earns +13/+15 in the existing classic/adjusted environments.
6. The simulator has scoring/rule defects; the current suite returns **76 passed, 12 failed**.

The ledger records **283 points versus 297 summed weekly averages**. Five weeks do not establish the system's true long-run quality. The code and data defects are much stronger evidence for what to fix than those five outcomes alone.

All review files, diagnostic scripts, generated results, and logs are under this directory. Existing implementation and artifacts were not edited. No SFT/RL training, model download, live account action, or external message was performed. Small CPU model refits were used only for an isolated leakage sensitivity diagnostic.

**What this review does not claim:** it does not supply a newly validated winning model, reconstruct every conversational override, certify every historical snapshot, or assign an exact number of lost points to each defect. It provides a reproducible diagnosis and an implementation plan with acceptance gates.

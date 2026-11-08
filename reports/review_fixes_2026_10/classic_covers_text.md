# Does the classic model already capture what the articles say?

39936 player-weeks, 2022-23 to 2026-27 GW5; articles at least 12 h before the deadline only.

How often each signal fires, and what happens next relative to classic:

| Signal | Fires on | Played (fires / not) | Classic P(appear) (fires / not) | Surprise vs classic (fires / not) |
|---|---|---|---|---|
| injury / doubt words | 22.4% | 76% / 87% | 59% / 69% | -0.08 / +0.17 |
| return / fit words | 0.4% | 74% / 84% | 58% / 67% | +0.59 / +0.11 |
| suspension words | 15.7% | 76% / 86% | 57% / 69% | -0.12 / +0.15 |
| rotation / bench words | 5.6% | 87% / 84% | 65% / 67% | +0.15 / +0.11 |
| Guardian team-news piece | 14.0% | 75% / 86% | 56% / 68% | -0.15 / +0.15 |
| Premier League Scout mention | 11.6% | 91% / 84% | 74% / 66% | +0.28 / +0.09 |

Out of season (fit on the other seasons, score the held-out one):

| Held-out season | Rows | Availability AUC: classic → classic + text | Points RMSE: classic → classic + text |
|---|---|---|---|
| 2022-23 | 9728 | 0.718 → 0.719 (+0.001) | 3.134 → 3.131 (-0.003) |
| 2023-24 | 9728 | 0.713 → 0.722 (+0.009) | 3.088 → 3.083 (-0.005) |
| 2024-25 | 9728 | 0.729 → 0.739 (+0.010) | 3.096 → 3.088 (-0.008) |
| 2025-26 | 9728 | 0.702 → 0.715 (+0.013) | 3.039 → 3.041 (+0.002) |
| 2026-27 | 1024 | 0.726 → 0.733 (+0.007) | 3.086 → 3.082 (-0.003) |

Fitted on all seasons (direction of each signal, beyond classic):

| Signal | Availability log-odds | Points surprise |
|---|---|---|
| injury / doubt words | -0.45 | -0.16 |
| return / fit words | -0.17 | +0.54 |
| suspension words | -0.37 | -0.05 |
| rotation / bench words | +0.28 | +0.04 |
| Guardian team-news piece | +0.43 | -0.10 |
| Premier League Scout mention | +0.39 | +0.17 |

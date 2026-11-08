# Which article types help the SFT? (out of sample: 2025-26 GW27-38 + 2026-27 GW2-5, E20)

| Article type | Player-weeks | Articles from last 24 h | Points: SFT signal vs real surprise (corr) | Points RMSE classic → SFT average | Availability AUC classic → SFT |
|---|---|---|---|---|---|
| No article (reference) | 616 | – | +0.160 (±0.079) | 3.002 → 2.977 | 0.635 → 0.700 |
| Guardian: team news / predicted line-ups | 559 | 80% | +0.227 (±0.083) | 2.781 → 2.732 | 0.638 → 0.754 |
| PL site: price changes and transfer trends | 42 | 26% | +0.082 (±0.314) | 3.029 → 3.019 | 0.537 → 0.512 |
| PL site: Scout picks, captaincy, tips | 488 | 13% | +0.143 (±0.089) | 3.359 → 3.306 | 0.608 → 0.778 |
| Guardian: international matches | 88 | 27% | +0.202 (±0.213) | 2.919 → 2.864 | 0.674 → 0.735 |
| Guardian: transfer news | 72 | 8% | +0.106 (±0.236) | 3.145 → 3.134 | 0.824 → 0.777 |
| Guardian: previews and talking points | 91 | 1% | -0.026 (±0.209) | 2.685 → 2.696 | 0.689 → 0.739 |
| Guardian: live blogs (as it happened) | 2890 | 6% | +0.184 (±0.036) | 3.064 → 3.020 | 0.637 → 0.754 |
| Guardian: match reports | 42 | 0% | +0.254 (±0.314) | 2.937 → 2.899 | 0.375 → 0.382 |
| Guardian: other news | 1345 | 13% | +0.206 (±0.054) | 3.045 → 3.008 | 0.668 → 0.760 |

Correlation: between the SFT's player-specific adjustment and the real surprise; ± is the 95% interval. A type helps if that correlation is clearly above zero and the SFT's availability AUC beats classic's.

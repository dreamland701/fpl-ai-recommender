# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 249.40
- Total actual points: 280.00
- Average predicted points: 62.35
- Average actual points: 70.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 140908
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.78
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.46 | 10.09 | 16.40 | 6.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 3.29 | 9.07 | 14.86 | 1.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.77 | 12.66 | 20.25 | 1.00 | 100.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.3 | 4.24 | 12.14 | 19.92 | 0.00 | 87.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.94 | 11.41 | 18.24 | 6.00 | 91.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.91 | 10.44 | 16.97 | 0.00 | 90.2 | 90.0 |
| Bench 2 | Bench | Lewis Hall | DEF | 15 | 4.4 | 3.74 | 10.08 | 16.11 | 1.00 | 91.5 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.88 | 11.85 | 18.76 | 2.00 | 79.9 | 85.0 |
| Bench 3 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 2.84 | 7.93 | 12.96 | 2.00 | 70.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.88 | 6.58 | 10.50 | 1.00 | 59.9 | 13.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.11 | 22.21 | 36.23 | 13.00 | 114.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.94 | 19.51 | 31.98 | 2.00 | 104.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.36 | 16.55 | 26.43 | 2.00 | 106.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 4.22 | 14.58 | 23.92 | 3.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.84 | 10.99 | 17.68 | 2.00 | 78.0 | 81.0 |

## GW13

- Train rows: 141592
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.97
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.18) beats the best remaining Triple Captain opportunity (8.97).
- Autosub: Iliman Ndiaye replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 10.72 | 17.27 | 2.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.7 | 2.79 | 8.03 | 13.04 | 7.00 | 81.2 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.3 | 3.38 | 11.35 | 19.03 | 0.00 | 83.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.73 | 11.22 | 18.02 | 6.00 | 84.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 3.99 | 11.11 | 17.71 | 9.00 | 89.0 | 45.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.7 | 3.04 | 9.20 | 15.06 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Lewis Hall | DEF | 15 | 4.4 | 2.74 | 8.45 | 13.61 | 2.00 | 73.2 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 5 | 6.0 | 3.70 | 10.31 | 16.79 | 2.00 | 70.2 | 78.0 |
| Bench 2 | Autosub In | Iliman Ndiaye | FWD | 8 | 5.4 | 2.94 | 8.50 | 13.91 | 2.00 | 71.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 5.0 | 1.54 | 5.25 | 8.91 | 2.00 | 38.7 | 87.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 8.18 | 24.26 | 38.49 | 13.00 | 107.5 | 83.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.9 | 6.59 | 18.64 | 30.18 | 14.00 | 97.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.30 | 14.72 | 24.60 | 2.00 | 92.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 3.79 | 12.79 | 20.78 | 9.00 | 71.1 | 65.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.4 | 3.03 | 9.48 | 15.77 | 2.00 | 67.1 | 65.0 |

## GW14

- Train rows: 142282
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: wildcard
- Predicted score: 60.79
- Actual score: 76.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +13.63 squad value (threshold 12).
- Autosub: Leif Davis replaced Gabriel dos Santos Magalhães.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.59 | 9.99 | 16.25 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Robert Sánchez | GK | 6 | 4.8 | 3.57 | 9.46 | 15.06 | 0.00 | 90.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.29 | 12.68 | 20.52 | 1.00 | 97.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.06 | 11.75 | 18.85 | 1.00 | 87.9 | 28.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 3.72 | 10.67 | 17.20 | 0.00 | 76.5 | 0.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 3.90 | 10.21 | 16.31 | 1.00 | 91.8 | 90.0 |
| Bench 2 | Autosub In | Leif Davis | DEF | 10 | 4.5 | 3.07 | 9.02 | 14.76 | 2.00 | 81.1 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.29 | 9.96 | 16.10 | 2.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 17 | 5.1 | 2.72 | 7.83 | 12.07 | 1.00 | 68.6 | 61.0 |
| Bench 4 | Bench | Will Lankshear | FWD | 18 | 4.5 | 0.44 | 1.64 | 2.79 | 0.00 | 8.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.2 | 8.06 | 24.30 | 39.01 | 18.00 | 114.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 7.58 | 20.97 | 33.57 | 7.00 | 110.7 | 78.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.4 | 6.48 | 18.56 | 29.50 | 3.00 | 95.0 | 90.0 |
| XI | XI | Brennan Johnson | MID | 18 | 6.7 | 3.97 | 11.74 | 19.20 | 2.00 | 71.5 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.79 | 10.90 | 17.80 | 15.00 | 81.3 | 90.0 |

## GW15

- Train rows: 142975
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 61.85
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.65) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 1.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.65) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.77 | 10.92 | 17.63 | 2.00 | 90.7 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 6 | 4.8 | 1.33 | 4.65 | 8.27 | 0.00 | 41.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.08 | 11.67 | 18.49 | 9.00 | 88.7 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.4 | 2.86 | 9.88 | 16.74 | 0.00 | 66.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 2.94 | 9.34 | 15.99 | 3.00 | 67.9 | 90.0 |
| XI | XI | Leif Davis | DEF | 10 | 4.5 | 3.06 | 8.75 | 14.49 | 1.00 | 79.9 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 2.87 | 8.65 | 13.83 | 2.00 | 78.8 | 90.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.6 | 3.51 | 9.98 | 16.11 | 2.00 | 74.6 | 61.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 17 | 5.1 | 2.33 | 6.72 | 11.33 | 2.00 | 58.3 | 90.0 |
| Bench 4 | Bench Boost | Will Lankshear | FWD | 18 | 4.5 | 0.39 | 1.05 | 1.85 | 0.00 | 4.7 | 0.0 |
| Captain | XI | Mohamed Salah | MID | 12 | 13.2 | 7.38 | 23.33 | 38.89 | 0.00 | 91.5 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.4 | 6.68 | 19.68 | 31.17 | 2.00 | 92.5 | 90.0 |
| Vice Captain | Captain | Cole Palmer | MID | 6 | 11.0 | 6.90 | 19.64 | 31.84 | 18.00 | 97.7 | 90.0 |
| XI | XI | Alex Iwobi | MID | 9 | 5.6 | 3.29 | 10.96 | 18.01 | 2.00 | 82.6 | 90.0 |
| XI | XI | Brennan Johnson | MID | 18 | 6.7 | 3.08 | 10.31 | 17.03 | 4.00 | 70.1 | 52.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.92
- Total actual points: 176.00
- Average predicted points: 60.48
- Average actual points: 44.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 152512
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 73.29
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 10.94 | 17.67 | 3.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.44 | 1.15 | 1.79 | 0.00 | 7.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 16.54 | 26.74 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.09 | 19.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.43 | 11.76 | 18.53 | 6.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.40 | 7.05 | 11.29 | 2.00 | 64.5 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 6.19 | 9.93 | 1.00 | 76.9 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.78 | 14.80 | 24.72 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.76 | 13.15 | 20.99 | 2.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.68 | 5.90 | 9.76 | 0.00 | 54.4 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.93 | 29.18 | 47.71 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.89 | 18.69 | 30.34 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.05 | 17.51 | 28.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.75 | 14.77 | 23.67 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.52 | 13.73 | 22.34 | 5.00 | 84.7 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.33
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.53 | 17.17 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.65 | 1.48 | 2.22 | 0.00 | 7.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.52 | 23.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.31 | 19.84 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.70 | 14.62 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.12 | 6.69 | 11.01 | 0.00 | 64.8 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 6.01 | 9.66 | 0.00 | 77.1 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.26 | 18.26 | 28.71 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.01 | 11.91 | 19.22 | 8.00 | 73.8 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.61 | 5.03 | 8.47 | 7.00 | 34.5 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.75 | 45.41 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.69 | 16.74 | 27.00 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.54 | 16.24 | 25.46 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.80 | 15.09 | 26.01 | 0.00 | 69.8 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.35 | 16.71 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.74
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.92) beats the best remaining Bench Boost opportunity (6.99).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.92) beats the best remaining Bench Boost opportunity (6.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.39 | 12.54 | 19.78 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.68 | 1.48 | 2.22 | 0.00 | 8.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.30 | 12.40 | 20.04 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.10 | 11.22 | 17.89 | 6.00 | 84.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.89 | 10.08 | 16.02 | 2.00 | 65.6 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.73 | 5.34 | 8.72 | 0.00 | 63.3 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.26 | 4.53 | 7.87 | 1.00 | 41.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.68 | 10.46 | 17.54 | 5.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.26 | 6.99 | 12.93 | 0.00 | 32.9 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.61 | 10.93 | 7.00 | 50.6 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.76 | 23.45 | 39.91 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.80 | 13.40 | 21.96 | 0.00 | 74.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.69 | 13.37 | 22.56 | 8.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.44 | 10.85 | 19.54 | 6.00 | 29.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.67 | 8.23 | 14.60 | 3.00 | 49.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.55
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 11.51 | 18.18 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.52 | 1.42 | 2.27 | 0.00 | 8.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.61 | 13.42 | 21.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 12.19 | 19.14 | 9.00 | 89.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.39 | 10.03 | 15.50 | 8.00 | 67.9 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.85 | 5.36 | 8.84 | 0.00 | 52.6 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.29 | 3.80 | 6.65 | 0.00 | 45.6 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.46 | 10.91 | 18.15 | 2.00 | 73.3 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.28 | 6.70 | 10.93 | 1.00 | 50.0 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.50 | 5.51 | 11.45 | 0.00 | 20.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.60 | 24.94 | 41.12 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.90 | 15.54 | 26.77 | 1.00 | 70.5 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.00 | 14.88 | 24.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.38 | 10.28 | 17.18 | 1.00 | 74.1 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.01 | 4.67 | 9.52 | 0.00 | 11.5 | 0.0 |
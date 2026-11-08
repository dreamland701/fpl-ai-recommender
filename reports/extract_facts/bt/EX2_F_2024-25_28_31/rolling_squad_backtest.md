# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 246.99
- Total actual points: 176.00
- Average predicted points: 61.75
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
- Predicted score: 73.65
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.05 | 17.78 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.38 | 0.79 | 1.20 | 0.00 | 10.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.32 | 16.56 | 26.64 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.23 | 12.23 | 19.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.45 | 11.75 | 18.42 | 6.00 | 87.2 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.47 | 7.13 | 11.28 | 2.00 | 65.7 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.13 | 6.27 | 9.96 | 1.00 | 76.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.94 | 15.26 | 25.40 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.81 | 13.29 | 21.10 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.82 | 6.21 | 10.14 | 0.00 | 58.9 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.94 | 29.17 | 47.51 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.94 | 18.75 | 30.24 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.10 | 17.62 | 28.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.53 | 14.43 | 23.27 | 1.00 | 85.6 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.60 | 13.91 | 22.57 | 5.00 | 85.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 48.87
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.65 | 17.31 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.16 | 0.64 | 1.14 | 0.00 | 11.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.36 | 12.36 | 19.83 | 5.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 12.08 | 21.08 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 7.28 | 12.65 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.16 | 6.71 | 10.95 | 0.00 | 65.4 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.07 | 9.64 | 0.00 | 76.8 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.76 | 19.61 | 31.44 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.07 | 12.01 | 19.27 | 8.00 | 75.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.78 | 5.35 | 8.84 | 7.00 | 39.8 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.62 | 45.10 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.18 | 17.95 | 29.45 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 6.08 | 17.40 | 27.84 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.90 | 15.22 | 25.97 | 0.00 | 71.7 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.37 | 16.72 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.54
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.03) beats the best remaining Bench Boost opportunity (5.92).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.03) beats the best remaining Bench Boost opportunity (5.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.30 | 12.38 | 19.70 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.32 | 0.87 | 1.43 | 0.00 | 9.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.27 | 12.37 | 20.08 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 11.15 | 17.86 | 6.00 | 82.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.83 | 9.92 | 15.83 | 2.00 | 63.1 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.71 | 5.27 | 8.68 | 0.00 | 61.3 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.27 | 4.51 | 7.90 | 1.00 | 41.1 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.56 | 17.82 | 5.00 | 72.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.41 | 6.73 | 11.20 | 7.00 | 53.0 | 88.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.74 | 5.86 | 11.22 | 0.00 | 24.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.75 | 23.35 | 39.68 | 3.00 | 89.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.76 | 13.58 | 22.96 | 8.00 | 82.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.38 | 12.69 | 21.98 | 0.00 | 68.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.56 | 10.99 | 19.64 | 6.00 | 30.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.75 | 8.37 | 14.85 | 3.00 | 50.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.92
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.08) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.28, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.08) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.59 | 18.22 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.41 | 1.06 | 1.50 | 0.00 | 13.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 5.06 | 14.23 | 23.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 12.21 | 19.03 | 9.00 | 89.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.43 | 10.04 | 15.35 | 8.00 | 68.0 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.96 | 5.55 | 8.97 | 0.00 | 54.5 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.14 | 3.54 | 6.28 | 0.00 | 38.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.57 | 11.21 | 18.54 | 2.00 | 76.1 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.98 | 11.24 | 1.00 | 54.4 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.79 | 6.76 | 13.66 | 0.00 | 23.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 9.08 | 25.91 | 43.05 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.69 | 16.43 | 27.96 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.10 | 15.88 | 27.02 | 1.00 | 74.2 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.50 | 10.53 | 17.45 | 1.00 | 76.2 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.20 | 5.59 | 11.18 | 0.00 | 13.5 | 0.0 |
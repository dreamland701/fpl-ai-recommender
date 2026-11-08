# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 246.14
- Total actual points: 176.00
- Average predicted points: 61.53
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
- Predicted score: 73.62
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 10.97 | 17.74 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.10 | 1.85 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 16.53 | 26.65 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.19 | 12.17 | 19.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.41 | 11.70 | 18.40 | 6.00 | 86.2 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.40 | 7.02 | 11.20 | 2.00 | 63.6 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.20 | 9.92 | 1.00 | 75.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.90 | 15.21 | 25.36 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.78 | 13.27 | 21.12 | 2.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 6.05 | 10.01 | 0.00 | 55.9 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.95 | 29.20 | 47.57 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.91 | 18.71 | 30.25 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.59 | 28.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.78 | 14.84 | 23.72 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.56 | 13.87 | 22.55 | 5.00 | 84.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 48.48
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.70 | 10.58 | 17.27 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.33 | 1.10 | 1.91 | 0.00 | 12.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.32 | 19.82 | 5.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 11.95 | 20.97 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 7.18 | 12.57 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.11 | 6.63 | 10.89 | 0.00 | 63.8 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.05 | 6.01 | 9.62 | 0.00 | 75.7 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.76 | 19.62 | 31.45 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 11.96 | 19.27 | 8.00 | 74.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.64 | 5.12 | 8.64 | 7.00 | 35.5 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.74 | 45.24 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.18 | 17.95 | 29.48 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 6.06 | 17.36 | 27.81 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.86 | 15.17 | 25.97 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.46 | 16.83 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.69
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.89) beats the best remaining Bench Boost opportunity (5.77).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.89) beats the best remaining Bench Boost opportunity (5.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.36 | 12.50 | 19.74 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.23 | 1.20 | 2.13 | 0.00 | 13.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.48 | 20.12 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.12 | 11.27 | 17.91 | 6.00 | 83.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.86 | 9.98 | 15.82 | 2.00 | 63.5 | 75.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.74 | 5.36 | 8.70 | 0.00 | 62.0 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.27 | 4.54 | 7.86 | 1.00 | 40.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.76 | 10.71 | 17.90 | 5.00 | 74.0 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.72 | 11.12 | 7.00 | 51.7 | 88.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.64 | 5.71 | 11.04 | 0.00 | 22.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.76 | 23.41 | 39.68 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.82 | 13.71 | 23.03 | 8.00 | 84.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.37 | 12.83 | 22.20 | 0.00 | 68.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.56 | 11.03 | 19.66 | 6.00 | 30.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.74 | 8.39 | 14.82 | 3.00 | 50.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.36
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.08) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.61, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (9.08) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 11.51 | 18.19 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.53 | 1.36 | 2.26 | 0.00 | 13.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 5.07 | 14.25 | 23.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.16 | 19.02 | 9.00 | 88.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.37 | 9.94 | 15.28 | 8.00 | 66.3 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.87 | 5.41 | 8.88 | 0.00 | 52.0 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.31 | 3.80 | 6.61 | 0.00 | 44.4 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.53 | 11.15 | 18.51 | 2.00 | 75.0 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.31 | 6.81 | 11.12 | 1.00 | 51.6 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.84 | 6.41 | 12.82 | 0.00 | 24.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 9.08 | 25.90 | 43.09 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.64 | 16.35 | 27.93 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.02 | 15.75 | 26.95 | 1.00 | 72.1 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.43 | 10.42 | 17.37 | 1.00 | 74.3 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.26 | 5.26 | 10.36 | 0.00 | 15.3 | 0.0 |
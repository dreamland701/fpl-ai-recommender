# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 243.15
- Total actual points: 176.00
- Average predicted points: 60.79
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
- Predicted score: 73.50
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 10.93 | 17.71 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.32 | 1.01 | 1.78 | 0.00 | 10.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.29 | 16.51 | 26.67 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.18 | 12.14 | 19.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.43 | 11.75 | 18.50 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.48 | 7.21 | 11.61 | 2.00 | 67.2 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 6.16 | 9.75 | 1.00 | 77.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.89 | 15.20 | 25.39 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.79 | 13.28 | 21.22 | 2.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.87 | 6.48 | 10.68 | 0.00 | 59.9 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.93 | 29.14 | 47.61 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.88 | 18.64 | 30.25 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.07 | 17.58 | 28.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.76 | 14.80 | 23.71 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.57 | 13.88 | 22.60 | 5.00 | 85.0 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.73
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.54 | 17.24 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.27 | 1.00 | 1.83 | 0.00 | 11.6 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.43 | 22.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.34 | 19.87 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.66 | 14.54 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.19 | 6.84 | 11.33 | 0.00 | 67.5 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.05 | 5.96 | 9.44 | 0.00 | 77.4 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.35 | 18.61 | 29.32 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 11.93 | 19.18 | 8.00 | 76.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.58 | 5.02 | 8.55 | 7.00 | 34.6 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.61 | 45.12 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.72 | 16.84 | 27.17 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.57 | 16.34 | 25.63 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.86 | 15.18 | 26.21 | 0.00 | 72.8 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.36 | 16.72 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.85
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (6.44).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.50) beats the best remaining Bench Boost opportunity (6.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.39 | 12.55 | 19.85 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.18 | 1.10 | 2.05 | 0.00 | 12.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.46 | 20.13 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.10 | 11.22 | 17.88 | 6.00 | 83.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.98 | 10.29 | 16.41 | 2.00 | 68.0 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.81 | 5.53 | 9.08 | 0.00 | 65.5 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.20 | 4.42 | 7.74 | 1.00 | 39.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.72 | 10.54 | 17.62 | 5.00 | 74.9 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.31 | 7.27 | 13.51 | 0.00 | 32.9 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.53 | 7.14 | 11.77 | 7.00 | 55.6 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.75 | 23.38 | 39.74 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.87 | 13.56 | 22.15 | 0.00 | 77.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.74 | 13.53 | 22.82 | 8.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.36 | 10.62 | 19.21 | 6.00 | 27.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.86 | 8.75 | 15.41 | 3.00 | 53.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.07
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.31, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 11.51 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.47 | 1.25 | 2.16 | 0.00 | 12.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.60 | 13.37 | 21.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.16 | 19.07 | 9.00 | 88.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.47 | 10.18 | 15.80 | 8.00 | 70.3 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.01 | 5.80 | 9.48 | 0.00 | 55.7 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.23 | 3.67 | 6.48 | 0.00 | 43.2 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.50 | 11.02 | 18.26 | 2.00 | 76.0 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.45 | 7.20 | 11.73 | 1.00 | 55.3 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.58 | 5.86 | 12.15 | 0.00 | 20.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.57 | 24.82 | 40.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.97 | 15.68 | 27.06 | 1.00 | 73.4 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.05 | 15.04 | 24.92 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.42 | 10.34 | 17.18 | 1.00 | 75.8 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.00 | 4.73 | 9.70 | 0.00 | 11.1 | 0.0 |
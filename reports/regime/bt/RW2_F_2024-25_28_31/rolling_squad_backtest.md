# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.68
- Total actual points: 176.00
- Average predicted points: 60.67
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
- Predicted score: 73.30
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.67 | 10.66 | 17.29 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.32 | 0.95 | 1.63 | 0.00 | 10.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.17 | 16.32 | 26.38 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.06 | 11.89 | 19.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.52 | 11.76 | 18.49 | 6.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.35 | 6.81 | 10.79 | 2.00 | 63.6 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 6.12 | 9.83 | 1.00 | 75.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.95 | 15.63 | 25.81 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.81 | 13.31 | 21.30 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.70 | 6.08 | 10.08 | 0.00 | 56.2 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.87 | 29.22 | 47.69 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.84 | 18.63 | 30.01 | 1.00 | 89.6 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.09 | 17.65 | 28.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.85 | 14.83 | 23.66 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.61 | 14.20 | 23.12 | 5.00 | 87.0 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.96
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.61 | 10.50 | 17.08 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.29 | 0.95 | 1.73 | 0.00 | 11.9 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.56 | 23.29 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.27 | 12.33 | 19.70 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.87 | 14.93 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.20 | 6.75 | 11.00 | 0.00 | 64.7 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 5.99 | 9.59 | 0.00 | 75.6 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.45 | 19.04 | 29.75 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.06 | 11.90 | 19.36 | 8.00 | 75.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.74 | 5.35 | 8.99 | 7.00 | 36.1 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.80 | 45.45 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.68 | 16.94 | 26.54 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.67 | 16.81 | 27.06 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.76 | 14.87 | 25.66 | 0.00 | 66.9 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.62 | 17.08 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.29
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.49) beats the best remaining Bench Boost opportunity (6.42).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.49) beats the best remaining Bench Boost opportunity (6.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.31 | 12.48 | 19.71 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.18 | 1.05 | 2.00 | 0.00 | 13.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.22 | 12.32 | 19.87 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 11.29 | 17.87 | 6.00 | 83.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.98 | 10.42 | 16.70 | 2.00 | 64.3 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.69 | 5.17 | 8.47 | 0.00 | 61.1 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.30 | 4.57 | 7.98 | 1.00 | 41.1 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.68 | 10.41 | 17.58 | 5.00 | 73.1 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.32 | 7.29 | 13.44 | 0.00 | 34.5 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.64 | 11.19 | 7.00 | 51.5 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.74 | 23.85 | 40.60 | 3.00 | 87.3 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.96 | 13.95 | 22.83 | 0.00 | 76.3 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.63 | 13.29 | 22.42 | 8.00 | 81.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.35 | 10.44 | 18.81 | 6.00 | 26.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.76 | 8.58 | 15.29 | 3.00 | 49.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.13
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.86, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.65) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.50 | 18.15 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.50 | 1.28 | 2.17 | 0.00 | 13.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.69 | 13.57 | 21.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 12.12 | 18.96 | 9.00 | 89.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.51 | 10.06 | 15.56 | 8.00 | 68.6 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.76 | 5.12 | 8.42 | 0.00 | 51.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.28 | 3.68 | 6.53 | 0.00 | 43.6 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.51 | 11.06 | 18.50 | 2.00 | 76.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.33 | 6.82 | 11.43 | 1.00 | 53.0 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.65 | 5.47 | 11.38 | 0.00 | 22.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.65 | 25.52 | 42.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.90 | 15.08 | 25.60 | 1.00 | 69.7 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.02 | 14.76 | 24.40 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.53 | 10.77 | 18.11 | 1.00 | 75.2 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.04 | 4.69 | 9.79 | 0.00 | 12.6 | 0.0 |
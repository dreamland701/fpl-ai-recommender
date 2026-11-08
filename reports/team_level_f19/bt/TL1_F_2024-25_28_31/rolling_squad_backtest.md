# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.92
- Total actual points: 176.00
- Average predicted points: 60.73
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
- Predicted score: 73.83
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.93 | 17.76 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.42 | 1.16 | 1.80 | 0.00 | 10.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.33 | 16.38 | 26.50 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.17 | 12.14 | 19.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.54 | 11.91 | 18.67 | 6.00 | 86.7 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.45 | 7.21 | 11.49 | 2.00 | 63.8 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.99 | 5.90 | 9.41 | 1.00 | 76.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.93 | 15.07 | 25.26 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.80 | 13.28 | 21.23 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.69 | 5.96 | 9.81 | 0.00 | 55.8 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.95 | 29.04 | 47.42 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.96 | 18.74 | 30.31 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.59 | 28.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.79 | 14.71 | 23.57 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.56 | 13.80 | 22.47 | 5.00 | 85.6 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.68
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.62 | 17.37 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.75 | 1.51 | 2.27 | 0.00 | 10.6 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.31 | 22.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.35 | 12.43 | 20.02 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.79 | 14.70 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.15 | 6.80 | 11.17 | 0.00 | 64.5 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 1.92 | 5.78 | 9.18 | 0.00 | 76.3 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.44 | 18.67 | 29.30 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.02 | 12.11 | 19.46 | 8.00 | 75.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.56 | 4.89 | 8.34 | 7.00 | 36.0 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.45 | 44.90 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.72 | 16.98 | 27.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.54 | 16.28 | 25.52 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.85 | 14.92 | 25.77 | 0.00 | 69.2 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.25 | 16.55 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.99
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (6.97).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (6.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.36 | 12.58 | 19.93 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.66 | 1.42 | 2.19 | 0.00 | 11.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.30 | 12.49 | 20.21 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.24 | 11.45 | 18.21 | 6.00 | 82.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.01 | 10.17 | 16.08 | 2.00 | 64.6 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.61 | 5.11 | 8.25 | 0.00 | 62.3 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.30 | 4.65 | 8.10 | 1.00 | 41.5 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.73 | 10.66 | 17.85 | 5.00 | 73.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.35 | 7.27 | 13.43 | 0.00 | 34.9 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.31 | 6.53 | 10.84 | 7.00 | 52.1 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.68 | 23.21 | 39.53 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.95 | 13.68 | 22.28 | 0.00 | 76.0 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.76 | 13.61 | 22.89 | 8.00 | 83.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.43 | 10.72 | 19.30 | 6.00 | 28.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.63 | 8.15 | 14.53 | 3.00 | 49.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.41
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.52) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.26, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.52) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.81 | 11.50 | 18.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.61 | 1.51 | 2.33 | 0.00 | 11.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.57 | 13.34 | 21.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.07 | 12.24 | 19.28 | 9.00 | 88.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.40 | 10.06 | 15.53 | 8.00 | 67.3 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.89 | 5.64 | 9.21 | 0.00 | 52.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.18 | 3.41 | 6.04 | 0.00 | 44.8 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.53 | 11.13 | 18.52 | 2.00 | 75.0 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.24 | 6.63 | 10.81 | 1.00 | 51.5 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.61 | 5.85 | 12.07 | 0.00 | 22.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.52 | 24.72 | 40.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.87 | 15.45 | 26.63 | 1.00 | 70.3 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.09 | 15.11 | 25.02 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.36 | 10.25 | 17.14 | 1.00 | 74.2 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.04 | 4.69 | 9.65 | 0.00 | 12.8 | 0.0 |
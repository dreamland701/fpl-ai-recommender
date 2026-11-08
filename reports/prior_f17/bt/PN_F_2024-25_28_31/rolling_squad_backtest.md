# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.28
- Total actual points: 176.00
- Average predicted points: 60.57
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
- Predicted score: 73.41
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 10.97 | 17.77 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.42 | 1.12 | 1.80 | 0.00 | 11.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.27 | 16.43 | 26.53 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.19 | 12.19 | 19.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.35 | 11.43 | 17.90 | 6.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.42 | 7.11 | 11.39 | 2.00 | 64.3 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.03 | 6.00 | 9.54 | 1.00 | 74.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.91 | 15.29 | 25.55 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.82 | 13.38 | 21.41 | 2.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.66 | 5.85 | 9.66 | 0.00 | 54.7 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.89 | 29.06 | 47.52 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.88 | 18.68 | 30.36 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.60 | 28.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.76 | 14.80 | 23.72 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.58 | 13.90 | 22.60 | 5.00 | 85.4 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.61
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.57 | 17.30 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.63 | 1.44 | 2.21 | 0.00 | 11.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.41 | 22.97 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.35 | 12.40 | 19.99 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.37 | 14.06 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.13 | 6.72 | 11.07 | 0.00 | 64.7 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 1.98 | 5.81 | 9.29 | 0.00 | 74.3 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.37 | 18.70 | 29.49 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.05 | 12.08 | 19.57 | 8.00 | 75.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.59 | 4.96 | 8.34 | 7.00 | 34.4 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.54 | 45.13 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.73 | 16.89 | 27.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.58 | 16.36 | 25.65 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.76 | 15.01 | 25.90 | 0.00 | 69.0 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.38 | 16.82 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.83
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (7.06).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.94) beats the best remaining Bench Boost opportunity (7.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.39 | 12.57 | 19.90 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.65 | 1.44 | 2.20 | 0.00 | 12.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.50 | 20.21 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.11 | 11.26 | 17.95 | 6.00 | 83.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.82 | 9.77 | 15.44 | 2.00 | 61.5 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.67 | 5.14 | 8.35 | 0.00 | 60.5 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.30 | 4.64 | 8.04 | 1.00 | 41.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.74 | 10.73 | 18.04 | 5.00 | 74.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.38 | 7.40 | 13.64 | 0.00 | 34.2 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.32 | 6.53 | 10.80 | 7.00 | 50.5 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.70 | 23.26 | 39.56 | 3.00 | 89.1 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.87 | 13.61 | 22.30 | 0.00 | 75.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.74 | 13.57 | 22.91 | 8.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.40 | 10.72 | 19.33 | 6.00 | 28.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.70 | 8.31 | 14.73 | 3.00 | 49.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.43
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.28, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 11.54 | 18.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.49 | 1.36 | 2.23 | 0.00 | 12.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.61 | 13.43 | 21.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.07 | 12.21 | 19.15 | 9.00 | 89.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.32 | 9.68 | 14.82 | 8.00 | 64.1 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.88 | 5.47 | 9.02 | 0.00 | 52.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.24 | 3.60 | 6.28 | 0.00 | 42.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.52 | 11.18 | 18.64 | 2.00 | 75.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.23 | 6.57 | 10.73 | 1.00 | 49.7 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.63 | 5.94 | 12.16 | 0.00 | 21.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.54 | 24.70 | 40.67 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.88 | 15.45 | 26.59 | 1.00 | 69.5 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.05 | 15.05 | 24.92 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.41 | 10.35 | 17.27 | 1.00 | 74.0 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.07 | 4.85 | 9.81 | 0.00 | 12.4 | 0.0 |
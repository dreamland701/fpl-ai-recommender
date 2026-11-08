# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 238.30
- Total actual points: 176.00
- Average predicted points: 59.57
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
- Predicted score: 71.96
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.06 | 17.77 | 3.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.00 | 0.23 | 0.52 | 0.00 | 2.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 17.05 | 27.41 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.30 | 12.12 | 19.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.43 | 11.50 | 18.15 | 6.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.26 | 6.58 | 10.79 | 2.00 | 63.8 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.95 | 9.60 | 1.00 | 75.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.68 | 14.58 | 24.94 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.47 | 12.75 | 20.69 | 2.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.95 | 9.85 | 0.00 | 55.2 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.52 | 28.58 | 46.16 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.86 | 18.73 | 30.01 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.64 | 16.62 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.79 | 15.76 | 24.47 | 1.00 | 86.8 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.52 | 13.95 | 22.71 | 5.00 | 85.7 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.43
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.91 | 10.78 | 17.41 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.21 | 0.19 | 0.24 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.50 | 12.34 | 19.76 | 5.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 11.49 | 20.69 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 7.01 | 12.67 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.15 | 6.39 | 10.63 | 0.00 | 64.6 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.14 | 6.15 | 9.85 | 0.00 | 75.2 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.34 | 18.11 | 28.88 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.71 | 11.24 | 18.79 | 8.00 | 77.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.39 | 9.02 | 7.00 | 34.1 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.01 | 44.84 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.66 | 16.79 | 26.22 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.33 | 15.81 | 26.25 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.64 | 14.21 | 25.19 | 0.00 | 70.1 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 8.01 | 15.66 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.85
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (6.27).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.20) beats the best remaining Bench Boost opportunity (6.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.78 | 13.14 | 20.51 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Steven Benda | GK | 9 | 3.9 | 0.00 | 0.29 | 0.54 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.65 | 12.89 | 20.53 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.28 | 12.12 | 19.10 | 6.00 | 81.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.60 | 9.21 | 14.83 | 2.00 | 63.4 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.63 | 4.95 | 8.20 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.14 | 4.12 | 7.28 | 1.00 | 37.5 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.32 | 9.56 | 16.80 | 5.00 | 74.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.81 | 8.25 | 14.80 | 0.00 | 40.7 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.44 | 6.92 | 11.47 | 7.00 | 50.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.49 | 22.43 | 38.14 | 3.00 | 87.7 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.94 | 13.67 | 22.21 | 0.00 | 73.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.31 | 12.34 | 21.66 | 8.00 | 85.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.45 | 10.82 | 19.27 | 6.00 | 32.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.53 | 7.84 | 13.85 | 3.00 | 42.9 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.06
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.19, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.08 | 11.57 | 18.15 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.00 | 0.26 | 0.53 | 0.00 | 4.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.79 | 13.31 | 21.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.97 | 11.98 | 18.96 | 9.00 | 89.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.20 | 9.38 | 14.64 | 8.00 | 66.9 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.70 | 4.94 | 8.30 | 0.00 | 50.9 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.29 | 3.70 | 6.39 | 0.00 | 39.6 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.26 | 10.64 | 17.90 | 2.00 | 72.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.82 | 8.01 | 13.13 | 1.00 | 64.0 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.66 | 5.80 | 12.15 | 0.00 | 24.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.23 | 23.59 | 39.29 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.80 | 14.47 | 24.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.45 | 14.19 | 24.88 | 1.00 | 65.3 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.29 | 10.06 | 16.83 | 1.00 | 71.1 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.40 | 5.67 | 10.90 | 0.00 | 14.5 | 0.0 |
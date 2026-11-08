# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 237.59
- Total actual points: 176.00
- Average predicted points: 59.40
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
- Predicted score: 71.62
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.98 | 11.06 | 17.75 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.04 | 0.00 | 0.11 | 0.00 | 1.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.21 | 17.06 | 27.45 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.12 | 19.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.42 | 11.50 | 18.15 | 6.00 | 86.3 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.37 | 6.57 | 10.74 | 2.00 | 63.9 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.03 | 5.95 | 9.61 | 1.00 | 75.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.73 | 14.57 | 24.91 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.48 | 12.75 | 20.68 | 2.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.76 | 5.94 | 9.83 | 0.00 | 55.3 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.42 | 28.59 | 46.20 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.76 | 18.74 | 30.05 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.64 | 16.62 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.72 | 15.76 | 24.51 | 1.00 | 86.7 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.51 | 13.95 | 22.72 | 5.00 | 85.7 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.53
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 10.78 | 17.40 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.21 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.52 | 12.33 | 19.74 | 5.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 11.49 | 20.70 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 7.01 | 12.68 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.14 | 6.39 | 10.64 | 0.00 | 64.6 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.24 | 6.14 | 9.80 | 0.00 | 75.3 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.30 | 18.12 | 28.90 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.66 | 11.25 | 18.81 | 8.00 | 77.8 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.77 | 5.39 | 8.99 | 7.00 | 34.2 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.02 | 44.87 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.70 | 16.79 | 26.20 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.27 | 15.81 | 26.28 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.71 | 14.20 | 25.16 | 0.00 | 70.2 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 8.01 | 15.67 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.56
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.19) beats the best remaining Bench Boost opportunity (6.25).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.19) beats the best remaining Bench Boost opportunity (6.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.84 | 13.14 | 20.49 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Killian Cahill | GK | 5 | 3.9 | 0.01 | 0.14 | 0.27 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.70 | 12.88 | 20.51 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.21 | 12.12 | 19.14 | 6.00 | 81.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.49 | 9.22 | 14.87 | 2.00 | 63.2 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.60 | 4.95 | 8.21 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.16 | 4.12 | 7.28 | 1.00 | 37.6 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.38 | 9.55 | 16.78 | 5.00 | 74.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.68 | 8.26 | 14.85 | 0.00 | 40.5 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.92 | 11.47 | 7.00 | 50.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.46 | 22.43 | 38.15 | 3.00 | 87.7 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.95 | 13.67 | 22.21 | 0.00 | 73.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.34 | 12.34 | 21.64 | 8.00 | 85.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.33 | 10.83 | 19.32 | 6.00 | 32.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.55 | 7.84 | 13.84 | 3.00 | 42.9 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: William Saliba
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.88
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.19) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.19, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.19) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.13 | 11.56 | 18.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Killian Cahill | GK | 5 | 3.9 | 0.05 | 0.35 | 0.57 | 0.00 | 4.2 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.4 | 4.85 | 13.31 | 20.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.98 | 11.98 | 18.95 | 9.00 | 89.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.19 | 9.38 | 14.65 | 8.00 | 66.8 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.72 | 4.94 | 8.29 | 0.00 | 50.9 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.34 | 3.70 | 6.37 | 0.00 | 39.7 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.23 | 10.64 | 17.91 | 2.00 | 72.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.77 | 8.01 | 13.15 | 1.00 | 64.0 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.69 | 5.79 | 12.13 | 0.00 | 24.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.19 | 23.59 | 39.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.75 | 14.47 | 24.26 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.39 | 14.20 | 24.90 | 1.00 | 65.2 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.31 | 10.06 | 16.82 | 1.00 | 71.1 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.31 | 5.68 | 10.94 | 0.00 | 14.4 | 0.0 |
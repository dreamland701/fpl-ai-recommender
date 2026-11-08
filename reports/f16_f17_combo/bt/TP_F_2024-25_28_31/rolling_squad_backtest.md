# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 244.74
- Total actual points: 174.00
- Average predicted points: 61.18
- Average actual points: 43.50
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
- Predicted score: 73.61
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.92 | 11.15 | 17.93 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.24 | 0.68 | 1.11 | 0.00 | 4.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.25 | 16.12 | 25.82 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.43 | 19.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.53 | 11.96 | 18.76 | 6.00 | 89.2 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.38 | 6.72 | 10.51 | 2.00 | 62.4 | 68.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.12 | 6.33 | 10.35 | 2.00 | 83.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.92 | 15.12 | 25.13 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.93 | 13.64 | 21.78 | 2.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.74 | 5.92 | 9.62 | 0.00 | 56.7 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.80 | 28.52 | 46.44 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.95 | 18.69 | 30.22 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.07 | 17.37 | 27.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.50 | 14.24 | 22.97 | 1.00 | 84.9 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.63 | 13.85 | 22.39 | 5.00 | 86.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 47.32
- Actual score: 41.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 10.75 | 17.46 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.45 | 1.00 | 1.52 | 0.00 | 5.1 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.01 | 22.23 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.47 | 12.66 | 20.35 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.67 | 14.67 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.10 | 6.40 | 10.50 | 3.00 | 85.4 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.08 | 6.29 | 10.12 | 0.00 | 62.1 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.38 | 18.60 | 29.24 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.20 | 12.45 | 20.13 | 8.00 | 79.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.17 | 8.51 | 7.00 | 38.2 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.82 | 43.82 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.73 | 16.71 | 26.85 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.60 | 16.33 | 25.49 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.85 | 15.09 | 25.89 | 0.00 | 71.3 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.10 | 16.29 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.95
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.37) beats the best remaining Bench Boost opportunity (7.57).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.74, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.37) beats the best remaining Bench Boost opportunity (7.57).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.38 | 12.51 | 19.90 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.63 | 1.22 | 1.85 | 0.00 | 11.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.52 | 20.35 | 1.00 | 90.0 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.91 | 11.40 | 18.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.94 | 10.25 | 16.44 | 2.00 | 66.3 | 75.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.23 | 6.71 | 11.01 | 2.00 | 85.1 | 90.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.19 | 4.10 | 7.11 | 1.00 | 37.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.78 | 10.88 | 18.48 | 5.00 | 75.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.37 | 7.16 | 13.20 | 0.00 | 33.1 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.32 | 6.49 | 10.78 | 7.00 | 50.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.61 | 22.70 | 38.53 | 3.00 | 85.1 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.80 | 13.30 | 21.85 | 0.00 | 73.6 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.66 | 13.18 | 22.31 | 8.00 | 80.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.46 | 10.73 | 19.31 | 6.00 | 29.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.72 | 8.18 | 14.51 | 3.00 | 49.7 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.86
- Actual score: 32.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.69, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.51) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 11.72 | 18.46 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.31 | 0.92 | 1.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.75 | 13.83 | 21.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.53 | 10.34 | 15.93 | 8.00 | 71.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.45 | 7.04 | 11.42 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.87 | 5.14 | 8.22 | 0.00 | 51.1 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.23 | 4.83 | 9.48 | 0.00 | 31.5 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.11 | 12.72 | 19.00 | 2.00 | 60.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.66 | 11.48 | 19.06 | 2.00 | 79.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.77 | 10.90 | 1.00 | 52.4 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.51 | 24.31 | 39.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.99 | 15.51 | 26.46 | 1.00 | 72.1 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.05 | 14.77 | 24.25 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.48 | 10.30 | 16.98 | 1.00 | 75.5 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.03 | 5.07 | 10.35 | 0.00 | 10.9 | 0.0 |
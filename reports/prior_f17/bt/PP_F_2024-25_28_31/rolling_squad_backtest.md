# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.91
- Total actual points: 174.00
- Average predicted points: 60.73
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
- Predicted score: 73.43
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.02 | 17.82 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.31 | 0.83 | 1.37 | 0.00 | 8.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.22 | 16.08 | 25.81 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.25 | 12.31 | 19.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.47 | 11.86 | 18.69 | 6.00 | 87.9 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.31 | 6.60 | 10.42 | 2.00 | 60.3 | 68.0 |
| Bench 3 | Bench | Dara O'Shea | DEF | 10 | 3.9 | 2.04 | 6.19 | 10.22 | 2.00 | 81.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.88 | 15.04 | 25.06 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.88 | 13.58 | 21.76 | 2.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.63 | 5.75 | 9.47 | 0.00 | 53.6 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.80 | 28.54 | 46.49 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.89 | 18.61 | 30.18 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.04 | 17.34 | 27.78 | 2.00 | 89.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.75 | 14.65 | 23.41 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.58 | 13.78 | 22.34 | 5.00 | 85.3 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.70
- Actual score: 41.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.63 | 17.36 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.26 | 0.82 | 1.42 | 0.00 | 9.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.09 | 22.32 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.42 | 12.57 | 20.28 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.76 | 14.77 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.03 | 6.26 | 10.39 | 3.00 | 83.5 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.03 | 6.20 | 10.07 | 0.00 | 60.5 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.35 | 18.56 | 29.22 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.13 | 12.35 | 20.06 | 8.00 | 78.3 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.57 | 4.92 | 8.28 | 7.00 | 33.8 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.97 | 43.99 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.70 | 16.66 | 26.82 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.59 | 16.30 | 25.49 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.78 | 14.98 | 25.82 | 0.00 | 69.4 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.17 | 16.37 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.77
- Actual score: 45.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.93) beats the best remaining Bench Boost opportunity (6.96).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.93) beats the best remaining Bench Boost opportunity (6.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.43 | 12.61 | 19.92 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.17 | 0.92 | 1.62 | 0.00 | 10.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.38 | 12.60 | 20.37 | 1.00 | 90.0 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.96 | 11.48 | 18.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.96 | 10.30 | 16.42 | 2.00 | 66.7 | 75.0 |
| Bench 3 | Bench Boost | Dara O'Shea | DEF | 10 | 3.9 | 2.26 | 6.79 | 11.01 | 2.00 | 86.0 | 90.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.20 | 4.15 | 7.09 | 1.00 | 37.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.82 | 10.99 | 18.54 | 5.00 | 77.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.35 | 7.17 | 13.17 | 0.00 | 32.9 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.30 | 6.48 | 10.71 | 7.00 | 49.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.62 | 22.75 | 38.52 | 3.00 | 85.4 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.86 | 13.43 | 21.93 | 0.00 | 75.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.71 | 13.30 | 22.37 | 8.00 | 81.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.42 | 10.68 | 19.23 | 6.00 | 28.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.70 | 8.17 | 14.43 | 3.00 | 49.0 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.00
- Actual score: 32.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.89 | 11.60 | 18.37 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.47 | 1.06 | 1.72 | 0.00 | 10.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.72 | 13.76 | 21.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.46 | 10.20 | 15.81 | 8.00 | 69.5 | 90.0 |
| XI | XI | Dara O'Shea | DEF | 10 | 3.9 | 2.39 | 6.92 | 11.32 | 4.00 | 89.0 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.78 | 4.99 | 8.10 | 0.00 | 48.4 | 0.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.08 | 4.57 | 9.26 | 0.00 | 27.9 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.05 | 12.62 | 18.95 | 2.00 | 58.8 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.59 | 11.35 | 18.96 | 2.00 | 77.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.22 | 6.56 | 10.72 | 1.00 | 49.4 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.47 | 24.25 | 39.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.87 | 15.29 | 26.28 | 1.00 | 69.0 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.00 | 14.68 | 24.20 | 3.00 | 89.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.40 | 10.14 | 16.84 | 1.00 | 73.2 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.08 | 4.71 | 9.52 | 0.00 | 12.2 | 0.0 |
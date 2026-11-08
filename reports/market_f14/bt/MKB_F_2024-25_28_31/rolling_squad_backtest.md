# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 239.72
- Total actual points: 165.00
- Average predicted points: 59.93
- Average actual points: 41.25
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
- Predicted score: 72.92
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 10.99 | 17.75 | 3.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.10 | 0.50 | 0.97 | 0.00 | 7.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 16.57 | 26.83 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.20 | 12.16 | 19.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.39 | 11.58 | 18.20 | 6.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.32 | 6.81 | 10.93 | 2.00 | 62.3 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 6.22 | 9.95 | 1.00 | 74.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.84 | 15.10 | 25.28 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.68 | 13.06 | 20.91 | 2.00 | 83.8 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.78 | 6.10 | 9.97 | 0.00 | 54.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.81 | 28.93 | 47.36 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.84 | 18.55 | 30.11 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.93 | 17.29 | 27.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.72 | 14.70 | 23.63 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.58 | 13.95 | 22.71 | 5.00 | 85.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.71
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 10.57 | 17.24 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.03 | 0.42 | 0.94 | 0.00 | 8.3 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.41 | 22.91 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.36 | 12.35 | 19.86 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.57 | 14.40 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.12 | 6.66 | 10.98 | 0.00 | 63.3 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 6.13 | 9.84 | 0.00 | 75.1 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.43 | 18.76 | 29.53 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.93 | 11.77 | 19.10 | 8.00 | 74.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.64 | 5.14 | 8.69 | 7.00 | 34.5 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.42 | 44.84 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.74 | 16.81 | 26.32 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.66 | 16.72 | 27.03 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.58 | 14.53 | 25.18 | 0.00 | 66.1 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.05 | 16.26 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.38
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (6.21).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 6.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.15) beats the best remaining Bench Boost opportunity (6.21).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.55 | 12.90 | 20.31 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.00 | 0.59 | 1.25 | 0.00 | 9.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.42 | 12.66 | 20.37 | 1.00 | 90.0 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.94 | 11.33 | 18.36 | 2.00 | 87.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.71 | 9.61 | 15.27 | 2.00 | 61.9 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.67 | 5.16 | 8.41 | 0.00 | 61.1 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.11 | 4.19 | 7.36 | 1.00 | 36.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.53 | 10.18 | 17.21 | 5.00 | 70.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.64 | 7.96 | 14.48 | 0.00 | 40.8 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.72 | 11.16 | 7.00 | 50.9 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.52 | 22.85 | 38.90 | 3.00 | 86.7 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.85 | 13.55 | 22.18 | 0.00 | 74.0 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.55 | 13.09 | 22.20 | 8.00 | 81.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.52 | 10.97 | 19.71 | 6.00 | 32.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.48 | 7.75 | 13.85 | 3.00 | 43.3 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.71
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.37) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.78, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.37) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.92 | 11.70 | 18.47 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.24 | 0.70 | 1.31 | 0.00 | 8.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.67 | 13.52 | 21.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.28 | 9.69 | 14.97 | 8.00 | 65.6 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.40 | 5.29 | 10.28 | 0.00 | 31.4 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.72 | 5.06 | 8.39 | 0.00 | 50.2 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.18 | 3.50 | 6.17 | 0.00 | 40.0 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.19 | 13.06 | 19.71 | 2.00 | 61.7 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.32 | 10.67 | 17.88 | 2.00 | 72.3 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.85 | 8.05 | 13.02 | 1.00 | 63.2 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.37 | 24.35 | 40.14 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.86 | 14.58 | 24.26 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.52 | 14.51 | 25.23 | 1.00 | 63.9 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.28 | 10.08 | 16.86 | 1.00 | 71.0 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.25 | 5.26 | 10.45 | 0.00 | 15.3 | 0.0 |
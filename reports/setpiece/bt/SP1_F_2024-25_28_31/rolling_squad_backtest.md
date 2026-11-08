# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.88
- Total actual points: 165.00
- Average predicted points: 60.47
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
- Predicted score: 73.57
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.92 | 17.68 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.14 | 1.91 | 0.00 | 11.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.38 | 17.01 | 27.63 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.04 | 19.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.41 | 11.62 | 18.25 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.38 | 6.91 | 11.03 | 2.00 | 63.2 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.18 | 9.88 | 1.00 | 75.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.87 | 15.10 | 25.18 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.81 | 13.39 | 21.44 | 2.00 | 84.4 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.69 | 5.90 | 9.74 | 0.00 | 55.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.92 | 29.10 | 47.56 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.94 | 19.08 | 31.09 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.12 | 17.81 | 28.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.72 | 14.56 | 23.25 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.53 | 13.71 | 22.25 | 5.00 | 84.0 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.55
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.54 | 17.23 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.33 | 1.12 | 1.96 | 0.00 | 12.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.93 | 23.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.25 | 19.70 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.52 | 14.26 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.09 | 6.57 | 10.78 | 0.00 | 63.6 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.97 | 9.56 | 0.00 | 75.6 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.33 | 18.53 | 29.13 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 12.01 | 19.45 | 8.00 | 74.7 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.61 | 5.01 | 8.42 | 7.00 | 35.4 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.36 | 44.69 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.78 | 17.11 | 27.75 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.53 | 16.15 | 25.23 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.82 | 15.33 | 26.45 | 0.00 | 70.3 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.11 | 16.24 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.22
- Actual score: 43.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.55) beats the best remaining Bench Boost opportunity (6.50).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 5.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.55) beats the best remaining Bench Boost opportunity (6.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.38 | 12.54 | 19.84 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.23 | 1.21 | 2.15 | 0.00 | 13.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.30 | 12.36 | 19.94 | 1.00 | 90.0 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.84 | 11.09 | 18.03 | 2.00 | 88.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.88 | 9.99 | 15.83 | 2.00 | 64.1 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.72 | 5.30 | 8.63 | 0.00 | 61.7 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.25 | 4.49 | 7.78 | 1.00 | 40.6 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.72 | 10.67 | 17.98 | 5.00 | 73.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.35 | 7.36 | 13.53 | 0.00 | 33.3 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.54 | 10.79 | 7.00 | 51.3 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.72 | 23.23 | 39.50 | 3.00 | 89.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.79 | 13.79 | 23.39 | 8.00 | 82.8 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.82 | 13.42 | 21.92 | 0.00 | 74.3 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.47 | 11.12 | 20.02 | 6.00 | 29.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.67 | 8.12 | 14.36 | 3.00 | 49.0 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.54
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.56) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.48, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.56) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.82 | 11.47 | 18.14 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.53 | 1.35 | 2.25 | 0.00 | 13.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.58 | 13.26 | 20.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.36 | 9.83 | 15.10 | 8.00 | 66.3 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.85 | 5.35 | 8.80 | 0.00 | 51.4 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.00 | 4.33 | 8.83 | 0.00 | 25.3 | 0.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.28 | 3.73 | 6.50 | 0.00 | 44.0 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.07 | 12.55 | 18.77 | 2.00 | 60.6 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.51 | 11.11 | 18.55 | 2.00 | 74.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.27 | 6.64 | 10.83 | 1.00 | 51.1 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.56 | 24.72 | 40.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.91 | 15.71 | 27.05 | 1.00 | 70.7 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.09 | 15.23 | 25.33 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.38 | 10.19 | 16.96 | 1.00 | 73.7 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.01 | 4.64 | 9.39 | 0.00 | 10.9 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 245.61
- Total actual points: 176.00
- Average predicted points: 61.40
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
- Predicted score: 74.62
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.48 | 12.86 | 20.37 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.11 | 0.29 | 0.40 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.52 | 16.58 | 26.66 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.25 | 12.42 | 19.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.34 | 10.22 | 16.43 | 6.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.95 | 5.94 | 9.29 | 2.00 | 63.4 | 68.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.87 | 5.20 | 8.33 | 1.00 | 75.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.95 | 15.42 | 24.16 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.66 | 12.68 | 20.84 | 2.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 2.11 | 7.38 | 12.00 | 0.00 | 55.7 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.89 | 29.57 | 48.05 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 7.30 | 19.69 | 31.51 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.20 | 17.77 | 28.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.65 | 14.91 | 23.74 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.51 | 14.05 | 22.81 | 5.00 | 85.0 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.64
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.03 | 11.61 | 19.15 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.07 | 0.26 | 0.48 | 0.00 | 12.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.98 | 23.72 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.51 | 12.65 | 20.44 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.18 | 13.60 | 0.00 | 0.0 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 1.69 | 5.26 | 8.26 | 0.00 | 75.6 | 45.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.75 | 5.20 | 8.62 | 0.00 | 63.8 | 0.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 5.95 | 17.79 | 27.15 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.01 | 12.09 | 19.81 | 8.00 | 74.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.04 | 6.38 | 10.58 | 7.00 | 35.5 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.40 | 44.96 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.80 | 17.20 | 27.36 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.72 | 17.10 | 26.47 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 5.18 | 15.71 | 26.69 | 0.00 | 69.0 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.66 | 16.90 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.62
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.13) beats the best remaining Bench Boost opportunity (6.17).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.30, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.13) beats the best remaining Bench Boost opportunity (6.17).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.90 | 13.66 | 22.49 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.17 | 0.96 | 1.69 | 0.00 | 13.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.47 | 20.20 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.93 | 11.13 | 17.75 | 6.00 | 83.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.28 | 10.36 | 16.98 | 2.00 | 64.2 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.41 | 4.86 | 7.89 | 0.00 | 61.7 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 0.98 | 3.67 | 6.23 | 1.00 | 40.7 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.98 | 11.63 | 19.46 | 5.00 | 73.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.90 | 8.41 | 14.94 | 0.00 | 33.8 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.66 | 7.32 | 12.31 | 7.00 | 51.5 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.00 | 23.78 | 40.18 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 5.20 | 14.29 | 23.20 | 0.00 | 75.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.92 | 13.88 | 23.44 | 8.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.42 | 11.30 | 20.02 | 6.00 | 28.5 | 90.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 6.4 | 2.56 | 8.17 | 14.43 | 3.00 | 49.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: William Saliba
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.74
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.78) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 10.40, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.78) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.39 | 11.68 | 19.88 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.03 | 1.63 | 0.00 | 13.4 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 6.4 | 4.96 | 14.02 | 22.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.82 | 12.37 | 19.18 | 9.00 | 88.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.13 | 10.37 | 15.87 | 8.00 | 66.6 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.46 | 3.74 | 6.48 | 0.00 | 51.5 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.20 | 3.43 | 5.85 | 0.00 | 44.1 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.06 | 12.86 | 20.55 | 2.00 | 74.2 | 90.0 |
| XI | Bench | Chris Wood | FWD | 16 | 7.1 | 2.28 | 7.00 | 13.25 | 0.00 | 21.1 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.44 | 6.97 | 11.44 | 1.00 | 51.2 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.78 | 25.46 | 41.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.36 | 14.78 | 25.84 | 1.00 | 69.6 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.78 | 14.63 | 24.33 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.17 | 9.57 | 16.25 | 1.00 | 74.1 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.17 | 5.08 | 10.67 | 0.00 | 12.0 | 0.0 |
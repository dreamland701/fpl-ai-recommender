# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.14
- Total actual points: 176.00
- Average predicted points: 60.29
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
- Predicted score: 73.24
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.89 | 17.64 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.15 | 0.58 | 1.06 | 0.00 | 6.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.31 | 16.56 | 26.74 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.39 | 11.65 | 18.34 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.34 | 6.86 | 10.98 | 2.00 | 62.4 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.07 | 6.15 | 9.83 | 1.00 | 75.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.93 | 15.29 | 25.53 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.75 | 13.19 | 21.10 | 2.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.66 | 5.91 | 9.82 | 0.00 | 54.7 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.86 | 29.04 | 47.45 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.89 | 18.69 | 30.32 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.05 | 17.53 | 28.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.67 | 14.58 | 23.38 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.59 | 13.93 | 22.67 | 5.00 | 85.6 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.97
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.54 | 17.22 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.10 | 0.56 | 1.12 | 0.00 | 7.7 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.55 | 23.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.36 | 19.91 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.56 | 14.38 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.10 | 6.62 | 10.89 | 0.00 | 63.7 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.98 | 9.59 | 0.00 | 75.6 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.51 | 19.00 | 29.90 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.01 | 11.93 | 19.32 | 8.00 | 74.3 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.61 | 5.06 | 8.54 | 7.00 | 34.9 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.62 | 45.14 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.80 | 17.03 | 27.47 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.73 | 16.73 | 26.20 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.64 | 14.67 | 25.34 | 0.00 | 66.3 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.09 | 16.33 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.76
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.14) beats the best remaining Bench Boost opportunity (6.20).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.98, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.14) beats the best remaining Bench Boost opportunity (6.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.46 | 12.73 | 20.11 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.02 | 0.70 | 1.39 | 0.00 | 8.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.51 | 20.20 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 11.20 | 17.85 | 6.00 | 83.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.77 | 9.82 | 15.60 | 2.00 | 61.7 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.69 | 5.23 | 8.53 | 0.00 | 61.0 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.09 | 4.16 | 7.30 | 1.00 | 37.2 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.58 | 10.30 | 17.36 | 5.00 | 70.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.70 | 8.14 | 14.76 | 0.00 | 40.8 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.34 | 6.65 | 11.03 | 7.00 | 51.1 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.59 | 23.09 | 39.29 | 3.00 | 86.9 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.81 | 13.48 | 22.12 | 0.00 | 74.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.65 | 13.35 | 22.55 | 8.00 | 81.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.59 | 11.13 | 19.94 | 6.00 | 32.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.43 | 7.71 | 13.84 | 3.00 | 43.8 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.17
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.05, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.60 | 18.36 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.29 | 0.80 | 1.44 | 0.00 | 8.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.62 | 13.42 | 21.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.15 | 19.05 | 9.00 | 88.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.33 | 9.83 | 15.16 | 8.00 | 65.5 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.77 | 5.18 | 8.55 | 0.00 | 50.0 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.13 | 3.39 | 6.02 | 0.00 | 40.6 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.38 | 10.78 | 18.01 | 2.00 | 71.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.84 | 8.04 | 13.00 | 1.00 | 62.8 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.73 | 6.11 | 12.46 | 0.00 | 23.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.49 | 24.68 | 40.64 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.96 | 14.80 | 24.56 | 3.00 | 89.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.60 | 14.70 | 25.48 | 1.00 | 63.6 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.27 | 10.07 | 16.87 | 1.00 | 71.2 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.22 | 5.20 | 10.36 | 0.00 | 15.4 | 0.0 |
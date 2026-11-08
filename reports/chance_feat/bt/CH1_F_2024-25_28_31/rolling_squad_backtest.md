# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.17
- Total actual points: 176.00
- Average predicted points: 60.54
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
- Predicted score: 73.43
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 10.88 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.15 | 1.93 | 0.00 | 11.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.28 | 16.45 | 26.55 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.17 | 12.08 | 19.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.43 | 11.75 | 18.49 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.39 | 6.99 | 11.17 | 2.00 | 63.4 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.17 | 9.87 | 1.00 | 75.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.89 | 15.17 | 25.34 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.78 | 13.24 | 21.14 | 2.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.70 | 5.97 | 9.88 | 0.00 | 55.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.92 | 29.04 | 47.42 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.87 | 18.55 | 30.08 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.07 | 17.53 | 28.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.76 | 14.74 | 23.60 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.57 | 13.87 | 22.59 | 5.00 | 85.0 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.54
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.49 | 17.13 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.33 | 1.13 | 1.98 | 0.00 | 12.6 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.33 | 22.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.31 | 19.81 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.57 | 14.37 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.10 | 6.59 | 10.83 | 0.00 | 63.7 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.97 | 9.56 | 0.00 | 75.5 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.36 | 18.64 | 29.37 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.01 | 11.89 | 19.20 | 8.00 | 74.4 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.63 | 5.07 | 8.53 | 7.00 | 35.3 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.48 | 44.87 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.72 | 16.80 | 27.10 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.57 | 16.39 | 25.73 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.75 | 14.83 | 25.52 | 0.00 | 68.7 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.21 | 16.43 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.60
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.56) beats the best remaining Bench Boost opportunity (6.60).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.56) beats the best remaining Bench Boost opportunity (6.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.38 | 12.53 | 19.80 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.24 | 1.23 | 2.20 | 0.00 | 13.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.31 | 12.40 | 20.00 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 11.15 | 17.73 | 6.00 | 83.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.89 | 10.06 | 15.95 | 2.00 | 64.2 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.71 | 5.24 | 8.50 | 0.00 | 61.5 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.25 | 4.46 | 7.71 | 1.00 | 40.6 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.69 | 10.48 | 17.57 | 5.00 | 72.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.45 | 8.07 | 14.98 | 0.00 | 35.7 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.35 | 6.62 | 10.96 | 7.00 | 51.3 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.73 | 23.28 | 39.54 | 3.00 | 89.8 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.85 | 13.53 | 22.16 | 0.00 | 75.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.72 | 13.42 | 22.60 | 8.00 | 82.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.50 | 11.44 | 20.73 | 6.00 | 30.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.68 | 8.19 | 14.50 | 3.00 | 49.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.60
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 7.41, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 11.46 | 18.12 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.53 | 1.38 | 2.31 | 0.00 | 13.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.60 | 13.37 | 21.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.10 | 18.95 | 9.00 | 88.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.38 | 9.95 | 15.35 | 8.00 | 66.6 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.84 | 5.32 | 8.73 | 0.00 | 51.4 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.28 | 3.69 | 6.42 | 0.00 | 43.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.48 | 10.98 | 18.27 | 2.00 | 74.0 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.40 | 7.64 | 12.79 | 1.00 | 53.6 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.73 | 6.72 | 13.73 | 0.00 | 23.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.57 | 24.78 | 40.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.87 | 15.36 | 26.43 | 1.00 | 69.4 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.04 | 14.97 | 24.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.40 | 10.33 | 17.25 | 1.00 | 73.9 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.10 | 5.17 | 10.47 | 0.00 | 12.9 | 0.0 |
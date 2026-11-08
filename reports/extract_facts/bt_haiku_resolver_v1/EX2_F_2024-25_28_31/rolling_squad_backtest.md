# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 243.49
- Total actual points: 176.00
- Average predicted points: 60.87
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
- Predicted score: 72.99
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 11.03 | 17.75 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.24 | 0.90 | 1.62 | 0.00 | 6.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.32 | 16.54 | 26.62 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.22 | 12.22 | 19.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.45 | 11.76 | 18.42 | 6.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.46 | 7.11 | 11.25 | 2.00 | 65.5 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.13 | 6.26 | 9.93 | 1.00 | 76.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.94 | 15.27 | 25.39 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.82 | 13.31 | 21.17 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.82 | 6.19 | 10.12 | 0.00 | 58.8 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.73 | 29.32 | 47.60 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.94 | 18.77 | 30.29 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.10 | 17.62 | 28.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.31 | 14.56 | 23.35 | 1.00 | 79.3 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.59 | 13.91 | 22.56 | 5.00 | 85.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 47.73
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.64 | 17.28 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.20 | 0.90 | 1.68 | 0.00 | 8.0 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.38 | 22.85 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.35 | 12.36 | 19.82 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.58 | 14.44 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.15 | 6.69 | 10.91 | 0.00 | 65.2 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.06 | 9.63 | 0.00 | 76.8 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.32 | 18.52 | 29.09 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.07 | 12.04 | 19.34 | 8.00 | 75.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.78 | 5.36 | 8.84 | 7.00 | 39.8 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 27.59 | 46.88 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 6.29 | 18.14 | 28.55 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.73 | 16.84 | 27.07 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.90 | 15.25 | 25.99 | 0.00 | 71.7 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.38 | 16.72 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.26
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.03) beats the best remaining Bench Boost opportunity (5.92).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.03) beats the best remaining Bench Boost opportunity (5.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.30 | 12.37 | 19.69 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.26 | 1.22 | 2.24 | 0.00 | 14.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.27 | 12.35 | 20.06 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 11.14 | 17.85 | 6.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.83 | 9.91 | 15.84 | 2.00 | 63.0 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.70 | 5.25 | 8.65 | 0.00 | 61.1 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.26 | 4.48 | 7.85 | 1.00 | 40.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.56 | 17.82 | 5.00 | 72.3 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.40 | 6.72 | 11.19 | 7.00 | 52.8 | 88.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.81 | 6.06 | 11.65 | 0.00 | 23.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.75 | 23.38 | 39.72 | 3.00 | 89.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.76 | 13.58 | 22.94 | 8.00 | 82.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.11 | 12.60 | 21.50 | 0.00 | 70.3 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.55 | 10.99 | 19.64 | 6.00 | 30.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.75 | 8.37 | 14.85 | 3.00 | 50.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.51
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.34, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.58 | 18.22 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.39 | 1.15 | 2.01 | 0.00 | 8.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.95 | 14.28 | 22.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 12.19 | 19.02 | 9.00 | 89.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.43 | 10.04 | 15.38 | 8.00 | 67.9 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.96 | 5.54 | 8.97 | 0.00 | 54.5 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.14 | 3.53 | 6.28 | 0.00 | 38.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.57 | 11.21 | 18.55 | 2.00 | 75.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.98 | 11.24 | 1.00 | 54.3 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.77 | 6.76 | 13.61 | 0.00 | 22.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.62 | 24.90 | 40.83 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.80 | 17.26 | 28.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.08 | 15.86 | 27.01 | 1.00 | 73.7 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.50 | 10.53 | 17.44 | 1.00 | 76.2 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.18 | 5.60 | 11.12 | 0.00 | 13.2 | 0.0 |
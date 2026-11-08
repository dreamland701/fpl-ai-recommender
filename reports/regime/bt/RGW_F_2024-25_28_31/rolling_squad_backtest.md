# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.73
- Total actual points: 176.00
- Average predicted points: 60.43
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
- Predicted score: 73.06
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.70 | 10.74 | 17.35 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.28 | 0.83 | 1.44 | 0.00 | 6.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.16 | 16.32 | 26.41 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.04 | 11.83 | 19.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.50 | 11.72 | 18.45 | 6.00 | 88.7 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.35 | 6.83 | 10.85 | 2.00 | 64.6 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.08 | 6.05 | 9.76 | 1.00 | 77.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.84 | 15.25 | 25.22 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.78 | 13.20 | 21.12 | 2.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.68 | 5.98 | 9.91 | 0.00 | 55.1 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.86 | 29.24 | 47.75 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.85 | 18.69 | 30.09 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.05 | 17.57 | 28.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.84 | 14.82 | 23.65 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.57 | 14.04 | 22.86 | 5.00 | 86.7 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.69
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.63 | 10.55 | 17.11 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.55 | 1.15 | 1.60 | 0.00 | 5.9 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.62 | 23.41 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.25 | 12.26 | 19.62 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.85 | 14.93 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.20 | 6.78 | 11.07 | 0.00 | 65.6 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.06 | 5.95 | 9.54 | 0.00 | 76.9 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.35 | 18.69 | 29.17 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.05 | 11.87 | 19.28 | 8.00 | 74.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.27 | 8.85 | 7.00 | 35.3 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.91 | 45.65 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.64 | 16.83 | 26.35 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.64 | 16.70 | 26.87 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.79 | 15.01 | 25.87 | 0.00 | 67.5 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.62 | 17.07 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.92
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.19).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.19).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.34 | 12.53 | 19.76 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Steven Benda | GK | 9 | 3.9 | 0.12 | 0.82 | 1.43 | 0.00 | 6.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.19 | 12.23 | 19.73 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 11.27 | 17.84 | 6.00 | 84.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.96 | 10.38 | 16.66 | 2.00 | 65.6 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.67 | 5.14 | 8.44 | 0.00 | 62.5 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.29 | 4.55 | 7.96 | 1.00 | 42.2 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.66 | 10.32 | 17.41 | 5.00 | 72.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.22 | 6.93 | 12.83 | 0.00 | 33.9 | 0.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.33 | 6.57 | 11.06 | 7.00 | 50.7 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.73 | 23.88 | 40.69 | 3.00 | 89.1 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.90 | 13.74 | 22.49 | 0.00 | 75.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.58 | 13.13 | 22.16 | 8.00 | 81.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.38 | 10.59 | 19.06 | 6.00 | 27.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.73 | 8.50 | 15.16 | 3.00 | 49.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.07
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 9.30, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.66) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 11.55 | 18.19 | 2.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Steven Benda | GK | 9 | 3.9 | 0.15 | 0.82 | 1.41 | 0.00 | 7.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.68 | 13.57 | 21.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 12.12 | 18.97 | 9.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.51 | 10.06 | 15.59 | 8.00 | 69.7 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.75 | 5.10 | 8.39 | 0.00 | 52.3 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.26 | 3.65 | 6.51 | 0.00 | 45.0 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.49 | 10.97 | 18.31 | 2.00 | 75.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.33 | 6.80 | 11.36 | 1.00 | 52.0 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.52 | 5.03 | 10.62 | 0.00 | 21.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.66 | 25.60 | 42.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.92 | 15.15 | 25.73 | 1.00 | 70.3 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.96 | 14.59 | 24.12 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.49 | 10.66 | 17.94 | 1.00 | 75.3 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.00 | 4.54 | 9.53 | 0.00 | 12.2 | 0.0 |
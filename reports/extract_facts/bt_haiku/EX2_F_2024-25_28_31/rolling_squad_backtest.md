# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 243.89
- Total actual points: 176.00
- Average predicted points: 60.97
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
- Predicted score: 72.75
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.84 | 11.03 | 17.76 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.22 | 0.72 | 1.23 | 0.00 | 4.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.32 | 16.54 | 26.63 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.22 | 12.22 | 19.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.45 | 11.76 | 18.43 | 6.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.46 | 7.11 | 11.26 | 2.00 | 65.6 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.13 | 6.26 | 9.93 | 1.00 | 76.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.94 | 15.27 | 25.40 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.82 | 13.31 | 21.16 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.82 | 6.20 | 10.12 | 0.00 | 58.8 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.65 | 29.28 | 47.69 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.94 | 18.77 | 30.29 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.10 | 17.62 | 28.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.23 | 14.53 | 23.44 | 1.00 | 79.4 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.59 | 13.90 | 22.55 | 5.00 | 85.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Justin Kluivert
- Vice captain: Chris Wood
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 47.88
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.64 | 17.29 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.43 | 1.05 | 1.65 | 0.00 | 5.2 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.38 | 22.86 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.35 | 12.36 | 19.82 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.59 | 14.45 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.15 | 6.69 | 10.91 | 0.00 | 65.2 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.06 | 9.63 | 0.00 | 76.7 | 45.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.2 | 6.32 | 18.51 | 29.10 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.07 | 12.04 | 19.34 | 8.00 | 75.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.78 | 5.36 | 8.84 | 7.00 | 39.8 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 27.53 | 46.77 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.37 | 18.31 | 28.70 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.73 | 16.83 | 27.06 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.90 | 15.24 | 25.99 | 0.00 | 71.7 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.37 | 16.71 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.67
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.37) beats the best remaining Bench Boost opportunity (6.37).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.37) beats the best remaining Bench Boost opportunity (6.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.30 | 12.37 | 19.69 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Daniel Bentley | GK | 20 | 3.9 | 0.62 | 1.27 | 1.98 | 0.00 | 11.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.26 | 12.35 | 20.06 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 11.14 | 17.85 | 6.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.84 | 9.91 | 15.84 | 2.00 | 63.1 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.70 | 5.25 | 8.65 | 0.00 | 61.1 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.26 | 4.48 | 7.85 | 1.00 | 40.9 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.56 | 17.83 | 5.00 | 72.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.40 | 6.73 | 11.19 | 7.00 | 52.9 | 88.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.79 | 5.93 | 11.44 | 0.00 | 24.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.75 | 23.37 | 39.71 | 3.00 | 89.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.76 | 13.58 | 22.95 | 8.00 | 82.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.17 | 13.00 | 21.98 | 0.00 | 70.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.55 | 10.99 | 19.65 | 6.00 | 30.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.75 | 8.37 | 14.85 | 3.00 | 50.5 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.59
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.25, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.62) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.58 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Daniel Bentley | GK | 20 | 3.9 | 0.30 | 0.97 | 1.67 | 0.00 | 6.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.91 | 14.21 | 22.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 12.20 | 19.02 | 9.00 | 89.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.43 | 10.05 | 15.39 | 8.00 | 68.0 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.96 | 5.54 | 8.97 | 0.00 | 54.5 | 0.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.14 | 3.54 | 6.29 | 0.00 | 38.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.57 | 11.22 | 18.55 | 2.00 | 75.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.42 | 6.98 | 11.24 | 1.00 | 54.4 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.78 | 6.77 | 13.64 | 0.00 | 22.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.62 | 24.90 | 40.83 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.91 | 17.49 | 28.83 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.09 | 15.87 | 27.03 | 1.00 | 73.8 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.50 | 10.53 | 17.45 | 1.00 | 76.2 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.18 | 5.60 | 11.13 | 0.00 | 13.2 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.91
- Total actual points: 176.00
- Average predicted points: 60.73
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
- Predicted score: 73.17
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.60 | 10.48 | 17.00 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.20 | 0.56 | 0.90 | 0.00 | 6.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.05 | 16.14 | 26.06 | 2.00 | 90.0 | 88.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.60 | 11.82 | 18.57 | 6.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.99 | 11.74 | 18.87 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.31 | 6.66 | 10.49 | 2.00 | 64.3 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.12 | 6.11 | 9.87 | 1.00 | 76.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.95 | 15.85 | 26.01 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.83 | 13.30 | 21.30 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.67 | 6.11 | 10.17 | 0.00 | 56.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.82 | 29.35 | 47.95 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.84 | 18.69 | 30.02 | 1.00 | 88.6 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.12 | 17.73 | 28.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.91 | 14.92 | 23.68 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.63 | 14.45 | 23.54 | 5.00 | 88.1 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Justin Kluivert
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 47.09
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.54 | 10.44 | 16.93 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.44 | 0.83 | 1.17 | 0.00 | 7.8 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.73 | 23.56 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.22 | 12.31 | 19.56 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 9.15 | 15.41 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.24 | 6.74 | 11.00 | 0.00 | 65.4 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.10 | 5.98 | 9.61 | 0.00 | 75.8 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.49 | 19.40 | 30.14 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.12 | 11.90 | 19.42 | 8.00 | 76.5 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.79 | 5.53 | 9.25 | 7.00 | 36.2 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 27.13 | 45.92 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.70 | 17.25 | 27.03 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.65 | 16.80 | 27.08 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.76 | 14.78 | 25.69 | 0.00 | 66.0 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.90 | 17.46 | 0.00 | 0.0 | 0.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.28) beats the best remaining Bench Boost opportunity (6.22).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.28) beats the best remaining Bench Boost opportunity (6.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.23 | 12.37 | 19.55 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 8 | 3.9 | 0.00 | 0.28 | 0.74 | 0.00 | 9.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.21 | 19.67 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 11.35 | 17.85 | 6.00 | 83.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.98 | 10.51 | 17.00 | 2.00 | 62.9 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.66 | 5.06 | 8.36 | 0.00 | 60.3 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.29 | 4.44 | 7.89 | 1.00 | 40.7 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.69 | 10.34 | 17.51 | 5.00 | 73.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.39 | 7.42 | 13.60 | 0.00 | 36.2 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.33 | 6.60 | 11.20 | 7.00 | 51.6 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.70 | 24.08 | 41.12 | 3.00 | 84.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 5.04 | 14.14 | 23.13 | 0.00 | 76.5 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.57 | 13.16 | 22.22 | 8.00 | 80.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.32 | 10.29 | 18.67 | 6.00 | 25.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.77 | 8.69 | 15.55 | 3.00 | 47.9 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.73
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 9.24, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.71) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.50 | 18.12 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 8 | 3.9 | 0.02 | 0.47 | 0.85 | 0.00 | 9.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.77 | 13.76 | 21.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.15 | 12.20 | 19.04 | 9.00 | 89.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.62 | 10.21 | 15.80 | 8.00 | 69.8 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.68 | 4.93 | 8.08 | 0.00 | 51.0 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.25 | 3.55 | 6.42 | 0.00 | 42.2 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.55 | 11.18 | 18.78 | 2.00 | 78.7 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.39 | 6.85 | 11.67 | 1.00 | 55.1 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.67 | 5.25 | 11.10 | 0.00 | 24.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.71 | 25.96 | 42.93 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.97 | 15.10 | 25.38 | 1.00 | 71.4 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.99 | 14.63 | 24.22 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.60 | 11.02 | 18.60 | 1.00 | 75.4 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.04 | 4.57 | 9.87 | 0.00 | 13.1 | 0.0 |
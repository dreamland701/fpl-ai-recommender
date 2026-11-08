# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 244.30
- Total actual points: 176.00
- Average predicted points: 61.08
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
- Predicted score: 73.93
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 10.93 | 17.66 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.45 | 1.41 | 2.42 | 0.00 | 12.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.24 | 16.39 | 26.50 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.19 | 12.15 | 19.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.45 | 11.79 | 18.52 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.38 | 6.96 | 11.12 | 2.00 | 63.0 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.20 | 9.92 | 1.00 | 75.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.92 | 15.26 | 25.47 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.79 | 13.28 | 21.21 | 2.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.70 | 5.99 | 9.91 | 0.00 | 55.5 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 11.04 | 29.46 | 48.08 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.97 | 18.88 | 30.61 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.13 | 17.73 | 28.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.78 | 14.85 | 23.78 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.57 | 13.88 | 22.58 | 5.00 | 84.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.81
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.52 | 17.18 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.41 | 1.40 | 2.48 | 0.00 | 13.7 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.32 | 22.78 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.35 | 12.36 | 19.88 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.68 | 14.53 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.09 | 6.58 | 10.81 | 0.00 | 63.4 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.99 | 9.61 | 0.00 | 75.7 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.39 | 18.71 | 29.46 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.02 | 11.96 | 19.33 | 8.00 | 74.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.62 | 5.08 | 8.56 | 7.00 | 35.4 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.92 | 45.61 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.79 | 17.02 | 27.44 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.58 | 16.35 | 25.61 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.85 | 15.20 | 26.14 | 0.00 | 69.0 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.44 | 16.83 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.11
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (6.66).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 6.01, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (6.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.40 | 12.55 | 19.81 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.31 | 1.50 | 2.71 | 0.00 | 14.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.48 | 20.13 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.13 | 11.29 | 17.97 | 6.00 | 82.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.90 | 10.04 | 15.91 | 2.00 | 63.9 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.72 | 5.31 | 8.65 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.25 | 4.48 | 7.76 | 1.00 | 40.4 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.56 | 17.75 | 5.00 | 73.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.41 | 7.49 | 13.76 | 0.00 | 33.3 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.35 | 6.65 | 11.00 | 7.00 | 51.4 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.87 | 23.71 | 40.24 | 3.00 | 89.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.80 | 13.71 | 23.10 | 8.00 | 82.3 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.87 | 13.62 | 22.32 | 0.00 | 75.2 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.48 | 10.90 | 19.58 | 6.00 | 28.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.72 | 8.36 | 14.80 | 3.00 | 49.2 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.45
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.77) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.12, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.77) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.54 | 18.22 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.61 | 1.66 | 2.84 | 0.00 | 14.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.62 | 13.42 | 21.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 12.26 | 19.21 | 9.00 | 88.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.41 | 10.01 | 15.40 | 8.00 | 66.2 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.84 | 5.32 | 8.75 | 0.00 | 51.2 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.29 | 3.77 | 6.59 | 0.00 | 44.3 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.49 | 11.06 | 18.42 | 2.00 | 74.2 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.27 | 6.71 | 10.97 | 1.00 | 51.1 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.68 | 6.10 | 12.44 | 0.00 | 20.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.77 | 25.36 | 41.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.97 | 15.69 | 26.98 | 1.00 | 69.5 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.13 | 15.26 | 25.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.44 | 10.44 | 17.42 | 1.00 | 73.8 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.07 | 4.83 | 9.79 | 0.00 | 11.9 | 0.0 |
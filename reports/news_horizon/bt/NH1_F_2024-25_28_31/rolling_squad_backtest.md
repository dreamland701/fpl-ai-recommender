# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 243.03
- Total actual points: 176.00
- Average predicted points: 60.76
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
- Predicted score: 73.55
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 10.90 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.30 | 0.81 | 1.34 | 0.00 | 7.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.30 | 16.47 | 26.55 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.19 | 12.10 | 19.43 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.43 | 11.75 | 18.51 | 6.00 | 86.4 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.39 | 6.99 | 11.17 | 2.00 | 63.4 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.18 | 9.87 | 1.00 | 75.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.90 | 15.18 | 25.33 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.78 | 13.24 | 21.15 | 2.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.72 | 5.99 | 9.87 | 0.00 | 56.0 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.94 | 29.07 | 47.42 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.90 | 18.58 | 30.07 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.06 | 17.54 | 28.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.76 | 14.75 | 23.62 | 1.00 | 90.0 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.55 | 13.87 | 22.62 | 5.00 | 84.7 | 90.0 |

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
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.70 | 10.51 | 17.13 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.26 | 0.97 | 1.55 | 0.00 | 8.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.36 | 22.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.32 | 19.81 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.60 | 14.39 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.11 | 6.60 | 10.83 | 0.00 | 63.9 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.98 | 9.57 | 0.00 | 75.6 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.35 | 18.63 | 29.38 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 11.91 | 19.20 | 8.00 | 74.8 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.65 | 5.09 | 8.52 | 7.00 | 36.0 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.52 | 44.87 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.73 | 16.81 | 27.10 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.54 | 16.37 | 25.76 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.80 | 14.89 | 25.49 | 0.00 | 69.9 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.26 | 16.43 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.91
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.52) beats the best remaining Bench Boost opportunity (6.55).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.52) beats the best remaining Bench Boost opportunity (6.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.40 | 12.54 | 19.79 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Alfie Whiteman | GK | 18 | 3.9 | 0.14 | 0.79 | 1.38 | 0.00 | 9.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.42 | 20.00 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.12 | 11.18 | 17.73 | 6.00 | 83.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.90 | 10.07 | 15.95 | 2.00 | 64.4 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.73 | 5.26 | 8.51 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.28 | 4.48 | 7.69 | 1.00 | 41.3 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.71 | 10.51 | 17.58 | 5.00 | 73.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 2.45 | 7.85 | 14.52 | 0.00 | 35.5 | 0.0 |
| Bench 2 | Bench Boost | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.65 | 10.95 | 7.00 | 51.8 | 88.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.79 | 23.33 | 39.49 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.85 | 13.54 | 22.19 | 0.00 | 75.3 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.75 | 13.46 | 22.61 | 8.00 | 83.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.54 | 11.23 | 20.18 | 6.00 | 31.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.74 | 8.24 | 14.47 | 3.00 | 50.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.93
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.59) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 7.57, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.59) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.85 | 11.48 | 18.12 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Alfie Whiteman | GK | 18 | 3.9 | 0.60 | 1.22 | 1.86 | 0.00 | 10.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.59 | 13.37 | 21.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 12.12 | 18.95 | 9.00 | 88.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.39 | 9.97 | 15.35 | 8.00 | 66.7 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.86 | 5.34 | 8.74 | 0.00 | 51.7 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.33 | 3.73 | 6.39 | 0.00 | 44.9 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.52 | 11.01 | 18.25 | 2.00 | 74.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.36 | 7.35 | 12.30 | 1.00 | 52.5 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.81 | 6.53 | 13.15 | 0.00 | 24.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.59 | 24.80 | 40.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.00 | 15.44 | 26.29 | 1.00 | 72.1 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.08 | 15.01 | 24.76 | 3.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.45 | 10.37 | 17.20 | 1.00 | 75.0 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.17 | 5.32 | 10.67 | 0.00 | 14.3 | 0.0 |
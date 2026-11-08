# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.54
- Total actual points: 176.00
- Average predicted points: 60.64
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
- Predicted score: 72.66
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 10.95 | 17.71 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.38 | 1.11 | 1.85 | 0.00 | 11.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.29 | 16.51 | 26.63 | 2.00 | 90.0 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.18 | 12.15 | 19.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.41 | 11.71 | 18.41 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.39 | 7.00 | 11.17 | 2.00 | 63.5 | 68.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.19 | 9.89 | 1.00 | 75.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.90 | 15.21 | 25.35 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.79 | 13.28 | 21.18 | 2.00 | 84.0 | 90.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.71 | 6.03 | 9.99 | 0.00 | 55.7 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.64 | 29.28 | 47.73 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.91 | 18.73 | 30.29 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.59 | 28.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.47 | 14.92 | 23.86 | 1.00 | 87.2 | 45.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.56 | 13.86 | 22.53 | 5.00 | 84.8 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Justin Kluivert
- Vice captain: Chris Wood
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 47.41
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.69 | 10.57 | 17.25 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.33 | 1.10 | 1.91 | 0.00 | 12.5 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.47 | 22.95 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.31 | 19.81 | 5.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.70 | 14.57 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.10 | 6.60 | 10.85 | 0.00 | 63.7 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.05 | 6.00 | 9.61 | 0.00 | 75.7 | 45.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.2 | 6.30 | 18.48 | 29.08 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.03 | 11.98 | 19.33 | 8.00 | 74.6 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.64 | 5.13 | 8.64 | 7.00 | 35.5 | 45.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 27.73 | 46.96 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.36 | 18.27 | 28.68 | 2.00 | 90.0 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.70 | 16.79 | 27.05 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.86 | 15.18 | 25.98 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.46 | 16.82 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.51
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.92) beats the best remaining Bench Boost opportunity (5.81).
- Transfer: Trent Alexander-Arnold -> Joško Gvardiol (projected gain 5.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.92) beats the best remaining Bench Boost opportunity (5.81).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.36 | 12.48 | 19.74 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.23 | 1.20 | 2.13 | 0.00 | 13.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.47 | 20.11 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.12 | 11.26 | 17.91 | 6.00 | 83.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.86 | 9.98 | 15.84 | 2.00 | 63.5 | 75.0 |
| Bench 2 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.74 | 5.34 | 8.68 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.26 | 4.51 | 7.82 | 1.00 | 40.7 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.77 | 10.71 | 17.92 | 5.00 | 73.9 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.37 | 6.72 | 11.12 | 7.00 | 51.7 | 88.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 1.69 | 5.78 | 11.26 | 0.00 | 21.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.77 | 23.43 | 39.71 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.82 | 13.71 | 23.01 | 8.00 | 84.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.16 | 13.16 | 22.25 | 0.00 | 70.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.55 | 11.03 | 19.66 | 6.00 | 30.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.74 | 8.40 | 14.82 | 3.00 | 50.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.30 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.96
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.59) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 8.62, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.59) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.83 | 11.51 | 18.19 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.53 | 1.36 | 2.26 | 0.00 | 13.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.93 | 14.23 | 22.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.15 | 19.01 | 9.00 | 88.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.37 | 9.95 | 15.32 | 8.00 | 66.3 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.86 | 5.41 | 8.87 | 0.00 | 51.9 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.31 | 3.80 | 6.61 | 0.00 | 44.3 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.53 | 11.15 | 18.52 | 2.00 | 74.8 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.31 | 6.81 | 11.12 | 1.00 | 51.6 | 17.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.1 | 1.83 | 6.39 | 12.78 | 0.00 | 24.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.59 | 24.86 | 40.83 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.88 | 17.42 | 28.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 5.01 | 15.74 | 26.95 | 1.00 | 71.7 | 31.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.43 | 10.42 | 17.37 | 1.00 | 74.3 | 54.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.24 | 5.24 | 10.29 | 0.00 | 15.0 | 0.0 |
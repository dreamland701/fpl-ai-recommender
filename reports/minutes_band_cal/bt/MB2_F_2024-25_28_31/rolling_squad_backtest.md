# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 233.03
- Total actual points: 162.00
- Average predicted points: 58.26
- Average actual points: 40.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.43
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.29 | 9.50 | 15.71 | 3.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 20 | 4.0 | 0.31 | 0.81 | 1.30 | 0.00 | 8.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.79 | 15.08 | 24.67 | 2.00 | 83.0 | 88.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.71 | 10.94 | 17.87 | 2.00 | 82.6 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.93 | 10.32 | 16.50 | 6.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.48 | 7.23 | 11.65 | 2.00 | 67.5 | 68.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.17 | 9.85 | 1.00 | 76.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.40 | 13.77 | 23.39 | 2.00 | 83.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.72 | 13.12 | 20.92 | 2.00 | 82.1 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.49 | 10.96 | 17.28 | 2.00 | 75.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.43 | 27.71 | 45.61 | 15.00 | 83.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.38 | 17.21 | 28.26 | 1.00 | 83.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.58 | 16.15 | 26.28 | 2.00 | 83.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.50 | 13.72 | 22.30 | 5.00 | 83.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 5.27 | 13.37 | 21.72 | 1.00 | 83.0 | 45.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 46.15
- Actual score: 29.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.19 | 9.07 | 15.26 | 6.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 20 | 4.0 | 0.46 | 1.05 | 1.61 | 0.00 | 9.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.37 | 12.00 | 19.02 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 11.96 | 20.97 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 7.18 | 12.56 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.20 | 6.85 | 11.35 | 0.00 | 67.8 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.97 | 9.53 | 0.00 | 76.3 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 5.86 | 17.14 | 27.35 | 2.00 | 83.1 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.02 | 11.94 | 19.28 | 8.00 | 75.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.43 | 10.82 | 17.15 | 2.00 | 69.3 | 79.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 25.13 | 43.15 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.23 | 15.36 | 25.20 | 6.00 | 83.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.86 | 15.19 | 26.24 | 0.00 | 73.0 | 0.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.08 | 14.86 | 23.65 | 2.00 | 83.1 | 78.0 |
| Bench 4 | Bench | Dominik Szoboszlai | MID | 12 | 6.4 | 0.00 | 9.19 | 16.44 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 154090
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.42
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (7.08).
- Transfer: Trent Alexander-Arnold -> Gabriel dos Santos Magalhães (projected gain 5.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (7.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.89 | 11.06 | 17.88 | 2.00 | 83.1 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 20 | 4.0 | 0.57 | 1.18 | 1.76 | 0.00 | 10.1 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.04 | 11.04 | 17.59 | 6.00 | 81.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.4 | 3.83 | 10.97 | 18.16 | 1.00 | 83.1 | 15.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.99 | 10.29 | 16.42 | 2.00 | 68.2 | 75.0 |
| Bench 3 | Bench Boost | Jacob Greaves | DEF | 10 | 3.9 | 1.82 | 5.54 | 9.10 | 0.00 | 65.7 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.25 | 4.53 | 7.87 | 1.00 | 40.8 | 45.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.56 | 17.71 | 5.00 | 73.8 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.61 | 8.53 | 14.37 | 1.00 | 65.2 | 78.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.2 | 2.36 | 7.37 | 13.59 | 0.00 | 33.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.25 | 21.89 | 37.77 | 3.00 | 83.1 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.86 | 13.58 | 22.25 | 0.00 | 76.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.67 | 13.35 | 22.53 | 8.00 | 80.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.41 | 10.71 | 19.29 | 6.00 | 28.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 2.91 | 8.87 | 15.60 | 3.00 | 55.0 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.01
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.08) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 7.92, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.08) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.33 | 10.02 | 16.20 | 2.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 20 | 4.0 | 0.37 | 1.06 | 1.75 | 0.00 | 10.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.56 | 10.66 | 17.04 | 9.00 | 82.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.48 | 10.20 | 15.81 | 8.00 | 70.6 | 90.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.06 | 5.92 | 9.67 | 0.00 | 57.1 | 0.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.02 | 4.44 | 9.04 | 0.00 | 25.6 | 0.0 |
| Bench 2 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.28 | 3.77 | 6.60 | 0.00 | 44.1 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.5 | 4.22 | 13.15 | 19.93 | 2.00 | 65.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.49 | 11.03 | 18.38 | 2.00 | 74.9 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.70 | 9.05 | 15.17 | 2.00 | 68.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.08 | 23.32 | 38.85 | 2.00 | 83.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 4.98 | 15.70 | 27.07 | 1.00 | 73.7 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.55 | 13.54 | 22.89 | 3.00 | 83.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.4 | 3.41 | 10.35 | 17.29 | 1.00 | 74.8 | 54.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.06 | 4.82 | 9.79 | 0.00 | 12.0 | 0.0 |
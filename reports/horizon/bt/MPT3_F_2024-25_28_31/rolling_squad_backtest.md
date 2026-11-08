# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 247.79
- Total actual points: 169.00
- Average predicted points: 61.95
- Average actual points: 42.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.74
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 11.01 | 17.97 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.37 | 0.50 | 1.15 | 0.00 | 7.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.18 | 12.14 | 19.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.29 | 11.11 | 21.83 | 2.00 | 90.0 | 88.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.78 | 11.10 | 18.35 | 2.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.39 | 6.73 | 10.82 | 2.00 | 63.4 | 68.0 |
| Bench 4 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 2.09 | 6.11 | 9.76 | 1.00 | 75.4 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.2 | 4.89 | 15.19 | 25.39 | 2.00 | 90.0 | 86.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.79 | 12.80 | 20.76 | 2.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.40 | 10.16 | 15.81 | 2.00 | 71.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.93 | 19.83 | 39.17 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.88 | 18.50 | 30.33 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.07 | 17.34 | 28.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.57 | 13.54 | 22.07 | 5.00 | 85.0 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.66 | 10.76 | 17.58 | 2.00 | 78.3 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Bryan Mbeumo
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 54.86
- Actual score: 31.00
- Transfer: David Raya Martin -> Matz Sels (projected gain 0.76, hit 0)
- Autosub: Jacob Greaves replaced Aaron Cresswell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 4.07 | 11.22 | 17.84 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.00 | 0.70 | 2.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.86 | 13.12 | 24.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.37 | 23.95 | 5.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 10.16 | 20.68 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 2.10 | 6.47 | 10.68 | 0.00 | 63.8 | 0.0 |
| Bench 2 | Autosub In | Jacob Greaves | DEF | 10 | 3.9 | 2.04 | 5.90 | 9.38 | 0.00 | 75.6 | 45.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.2 | 6.35 | 18.05 | 28.74 | 2.00 | 90.0 | 79.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 4.02 | 11.52 | 18.67 | 8.00 | 74.6 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.34 | 10.08 | 15.63 | 2.00 | 65.2 | 79.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 19.24 | 38.87 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.72 | 16.74 | 27.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.57 | 15.72 | 24.85 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.76 | 15.36 | 26.33 | 0.00 | 69.0 | 0.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.37 | 10.00 | 16.64 | 2.00 | 79.3 | 84.0 |

## GW30

- Train rows: 154090
- Bank: 0.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Omar Marmoush
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 59.98
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.04).
- Transfer: Chris Wood -> Omar Marmoush (projected gain 14.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.31) beats the best remaining Bench Boost opportunity (6.04).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.06 | 8.79 | 14.58 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench Boost | John Ruddy | GK | 15 | 3.9 | 0.32 | 1.06 | 1.52 | 0.00 | 9.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.32 | 12.49 | 20.37 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.10 | 11.20 | 17.85 | 6.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.33 | 6.12 | 12.63 | 0.00 | 19.4 | 0.0 |
| XI | XI | Jacob Greaves | DEF | 10 | 3.9 | 1.72 | 5.09 | 8.30 | 0.00 | 61.7 | 0.0 |
| Bench 4 | Bench Boost | Aaron Cresswell | DEF | 19 | 3.9 | 1.26 | 4.60 | 8.01 | 1.00 | 40.7 | 45.0 |
| Vice Captain | XI | Omar Marmoush | FWD | 13 | 7.4 | 6.04 | 15.62 | 24.33 | 9.00 | 90.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.70 | 10.58 | 17.61 | 5.00 | 73.0 | 90.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.40 | 7.98 | 13.41 | 1.00 | 59.5 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.75 | 24.21 | 41.19 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.74 | 13.88 | 23.41 | 8.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.86 | 13.52 | 22.16 | 0.00 | 75.4 | 0.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.41 | 10.79 | 19.48 | 6.00 | 28.5 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.23 | 9.06 | 15.13 | 1.00 | 78.7 | 31.0 |

## GW31

- Train rows: 154881
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.20
- Actual score: 33.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 17.68, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.57) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Matz Sels | GK | 16 | 5.1 | 3.23 | 9.56 | 15.85 | 3.00 | 87.3 | 90.0 |
| Bench 1 | Bench | John Ruddy | GK | 15 | 3.9 | 0.52 | 1.34 | 1.92 | 0.00 | 10.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.60 | 17.55 | 21.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 15.77 | 18.72 | 9.00 | 88.9 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.84 | 6.14 | 11.85 | 0.00 | 24.9 | 0.0 |
| XI | Bench | Aaron Cresswell | DEF | 19 | 3.9 | 1.85 | 5.23 | 8.62 | 0.00 | 51.5 | 0.0 |
| Bench 3 | Bench | Jacob Greaves | DEF | 10 | 3.9 | 1.29 | 3.90 | 6.76 | 0.00 | 44.1 | 0.0 |
| XI | XI | Omar Marmoush | FWD | 13 | 7.4 | 4.13 | 15.96 | 18.08 | 2.00 | 61.2 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.49 | 10.82 | 17.95 | 2.00 | 74.2 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.61 | 8.50 | 14.33 | 2.00 | 64.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.57 | 25.42 | 42.18 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.05 | 14.94 | 24.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.88 | 14.71 | 25.56 | 1.00 | 69.6 | 31.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 2.59 | 7.95 | 13.49 | 3.00 | 61.4 | 82.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.06 | 5.03 | 10.09 | 0.00 | 12.0 | 0.0 |
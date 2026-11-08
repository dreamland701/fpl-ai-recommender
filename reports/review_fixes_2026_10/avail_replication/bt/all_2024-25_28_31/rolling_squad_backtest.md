# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 208.89
- Total actual points: 152.00
- Average predicted points: 52.22
- Average actual points: 38.00
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
- Predicted score: 56.91
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.6 | 3.73 | 9.61 | 15.05 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.14 | 9.19 | 15.14 | 3.00 | 91.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.73 | 12.56 | 20.74 | 2.00 | 97.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.56 | 10.91 | 17.31 | 2.00 | 94.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.18 | 9.65 | 15.39 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.98 | 9.37 | 15.09 | 1.00 | 84.4 | 86.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.7 | 3.21 | 9.02 | 14.30 | 5.00 | 87.9 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.06 | 9.44 | 14.84 | 2.00 | 79.2 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.02 | 9.14 | 15.39 | 9.00 | 64.4 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.97 | 2.31 | 3.76 | 0.00 | 6.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 9.26 | 25.04 | 41.45 | 15.00 | 126.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.08 | 14.73 | 23.90 | 2.00 | 90.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 5.26 | 14.69 | 24.32 | 1.00 | 93.1 | 72.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 3.56 | 11.63 | 17.97 | 5.00 | 85.8 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.03 | 9.26 | 14.97 | 2.00 | 76.2 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 49.01
- Actual score: 31.00
- Transfer: Pedro Porro -> Milos Kerkez (projected gain 1.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.05 | 8.84 | 14.32 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 1.68 | 6.13 | 10.50 | 0.00 | 48.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.70 | 12.43 | 18.86 | 1.00 | 113.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.53 | 11.26 | 18.51 | 5.00 | 100.8 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 2.71 | 10.65 | 18.52 | 0.00 | 50.2 | 0.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.2 | 3.81 | 10.15 | 15.29 | 4.00 | 104.8 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 7 | 4.7 | 1.62 | 5.79 | 10.21 | 0.00 | 43.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.19 | 9.77 | 15.86 | 1.00 | 74.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.74 | 9.17 | 14.37 | 2.00 | 71.7 | 79.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.06 | 0.97 | 1.89 | 0.00 | 5.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 6.15 | 22.62 | 39.14 | 0.00 | 81.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.82 | 14.43 | 23.37 | 6.00 | 101.8 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 4.83 | 14.13 | 21.80 | 2.00 | 108.2 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 3.17 | 12.07 | 20.64 | 0.00 | 62.3 | 0.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 2.87 | 9.04 | 15.22 | 2.00 | 82.2 | 84.0 |

## GW30

- Train rows: 154090
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: David Raya Martin
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 51.44
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.24) beats the best remaining Bench Boost opportunity (7.22).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 4.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.24) beats the best remaining Bench Boost opportunity (7.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | David Raya Martin | GK | 1 | 5.5 | 3.88 | 11.63 | 17.01 | 2.00 | 106.1 | 90.0 |
| Bench 1 | Bench Boost | Alisson Ramses Becker | GK | 12 | 5.6 | 1.98 | 5.58 | 9.57 | 0.00 | 65.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.64 | 11.21 | 17.10 | 1.00 | 97.6 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.65 | 10.20 | 14.85 | 6.00 | 84.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.31 | 9.83 | 14.92 | 2.00 | 92.2 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.2 | 2.71 | 7.21 | 11.38 | 1.00 | 63.6 | 90.0 |
| Bench 2 | Bench Boost | Marc Guéhi | DEF | 7 | 4.7 | 1.97 | 5.11 | 8.51 | 2.00 | 34.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.06 | 9.25 | 15.06 | 2.00 | 72.0 | 71.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 1.72 | 6.56 | 10.49 | 1.00 | 61.5 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.57 | 1.36 | 2.26 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 6.37 | 21.49 | 37.69 | 3.00 | 91.3 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 3.32 | 11.28 | 17.62 | 0.00 | 69.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.18 | 10.95 | 17.95 | 8.00 | 75.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 2.55 | 10.03 | 17.84 | 6.00 | 19.3 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.15 | 7.99 | 12.74 | 1.00 | 82.3 | 31.0 |

## GW31

- Train rows: 154881
- Bank: 1.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 51.53
- Actual score: 27.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mikkel Damsgaard -> Anthony Elanga (projected gain 3.04, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.34 | 10.00 | 15.26 | 2.00 | 95.2 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 1.34 | 4.58 | 8.33 | 0.00 | 29.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.04 | 11.42 | 17.56 | 2.00 | 109.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.06 | 9.05 | 13.65 | 9.00 | 92.4 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 5.2 | 2.74 | 8.57 | 13.24 | 1.00 | 82.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 7 | 4.7 | 2.24 | 6.50 | 10.31 | -1.00 | 80.8 | 89.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | -0.14 | 2.06 | 5.03 | 0.00 | 5.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.46 | 8.30 | 13.69 | 1.00 | 68.8 | 27.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.15 | 7.67 | 13.20 | 2.00 | 69.8 | 64.0 |
| Bench 2 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.27 | 0.95 | 1.63 | 0.00 | 6.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.00 | 20.68 | 34.64 | 2.00 | 106.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 4.13 | 13.70 | 24.08 | 1.00 | 74.0 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.30 | 10.80 | 18.56 | 3.00 | 69.1 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.5 | 3.06 | 9.81 | 15.94 | 1.00 | 77.3 | 45.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 0.12 | 3.30 | 7.36 | 0.00 | 5.8 | 0.0 |
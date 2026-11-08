# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 240.13
- Total actual points: 170.00
- Average predicted points: 60.03
- Average actual points: 42.50
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
- Predicted score: 64.81
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.6 | 4.07 | 10.56 | 16.78 | 3.00 | 97.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.44 | 10.02 | 16.25 | 3.00 | 90.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.82 | 15.18 | 24.55 | 2.00 | 97.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.94 | 11.47 | 18.52 | 2.00 | 91.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.40 | 11.11 | 17.47 | 6.00 | 87.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.55 | 10.37 | 17.01 | 2.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.35 | 10.02 | 16.55 | 1.00 | 81.4 | 86.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.47 | 10.50 | 16.49 | 2.00 | 73.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.60 | 10.35 | 17.12 | 9.00 | 65.4 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.97 | 2.31 | 3.76 | 0.00 | 6.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 9.84 | 26.73 | 43.82 | 15.00 | 127.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.26 | 17.07 | 27.78 | 1.00 | 93.1 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.55 | 15.98 | 25.73 | 2.00 | 90.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.29 | 12.88 | 20.98 | 5.00 | 86.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.65 | 9.47 | 15.08 | 6.00 | 73.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 57.15
- Actual score: 28.00
- Transfer: Trent Alexander-Arnold -> Ola Aina (projected gain 3.02, hit 0)
- Autosub: Enzo Fernández replaced Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.50 | 10.12 | 16.56 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 1.58 | 5.55 | 9.68 | 0.00 | 68.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 5.28 | 13.65 | 21.24 | 1.00 | 111.1 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.84 | 12.65 | 19.57 | 1.00 | 105.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.44 | 12.41 | 19.98 | 5.00 | 97.8 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.55 | 10.61 | 17.32 | 0.00 | 83.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 1.27 | 4.70 | 8.38 | 0.00 | 51.7 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.56 | 10.91 | 17.20 | 2.00 | 65.7 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.81 | 10.91 | 17.94 | 1.00 | 75.3 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.06 | 0.97 | 1.89 | 0.00 | 5.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 6.15 | 22.62 | 39.14 | 0.00 | 101.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.71 | 16.44 | 26.51 | 6.00 | 101.8 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 5.82 | 16.13 | 25.25 | 2.00 | 108.2 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.33 | 14.55 | 25.16 | 0.00 | 63.3 | 0.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.08 | 9.70 | 15.97 | 2.00 | 74.9 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 2.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ismaïla Sarr
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.11
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.36) beats the best remaining Bench Boost opportunity (8.42).
- Transfer: Enzo Fernández -> Ismaïla Sarr (projected gain 3.98, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.36) beats the best remaining Bench Boost opportunity (8.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.10 | 11.38 | 17.96 | 2.00 | 107.1 | 90.0 |
| Bench 1 | Bench Boost | Alisson Ramses Becker | GK | 12 | 5.6 | 2.28 | 7.30 | 12.96 | 0.00 | 52.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.98 | 11.52 | 18.66 | 1.00 | 95.6 | 15.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.32 | 10.79 | 17.21 | 2.00 | 64.5 | 75.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.62 | 10.00 | 15.98 | 6.00 | 82.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 2.66 | 8.00 | 12.98 | 1.00 | 73.7 | 39.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.44 | 7.86 | 13.56 | 0.00 | 50.8 | 2.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.41 | 9.91 | 16.09 | 2.00 | 67.0 | 71.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.07 | 7.30 | 12.47 | 1.00 | 55.5 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.57 | 1.36 | 2.26 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.06 | 21.88 | 37.29 | 3.00 | 86.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.23 | 13.62 | 24.24 | 6.00 | 29.3 | 90.0 |
| Vice Captain | XI | Ismaïla Sarr | MID | 7 | 5.7 | 5.57 | 13.31 | 21.37 | 2.00 | 66.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 3.99 | 11.68 | 19.26 | 0.00 | 70.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.74 | 11.45 | 19.55 | 8.00 | 76.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 57.06
- Actual score: 37.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.43) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 7.06, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.43) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.51 | 10.31 | 16.26 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 2.02 | 7.01 | 12.79 | 0.00 | 41.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.61 | 12.74 | 20.17 | 2.00 | 105.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.70 | 10.81 | 16.87 | 9.00 | 91.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.41 | 9.84 | 15.18 | 8.00 | 66.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.30 | 9.02 | 15.23 | 1.00 | 46.3 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.3 | 1.48 | 5.92 | 10.71 | 0.00 | 48.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.81 | 9.46 | 15.76 | 1.00 | 60.8 | 27.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.46 | 8.38 | 14.00 | 2.00 | 62.8 | 64.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.27 | 0.95 | 1.63 | 0.00 | 6.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.43 | 21.84 | 35.97 | 2.00 | 108.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 4.69 | 15.22 | 26.37 | 1.00 | 63.0 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.00 | 10.80 | 18.56 | 3.00 | 89.1 | 90.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.7 | 3.28 | 10.75 | 16.89 | 2.00 | 55.8 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.14 | 6.45 | 12.48 | 0.00 | 6.8 | 0.0 |
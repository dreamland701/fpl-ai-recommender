# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 262.39
- Total actual points: 170.00
- Average predicted points: 65.60
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
- Predicted score: 70.54
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | 12 | 5.6 | 4.43 | 11.51 | 18.25 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.89 | 17.64 | 3.00 | 91.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.33 | 16.56 | 26.74 | 2.00 | 97.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.51 | 2.00 | 94.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.72 | 11.96 | 18.83 | 6.00 | 90.7 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.90 | 11.40 | 18.66 | 2.00 | 87.8 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.70 | 11.03 | 18.18 | 1.00 | 84.4 | 86.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.82 | 11.53 | 18.09 | 2.00 | 79.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.96 | 11.40 | 18.87 | 9.00 | 64.4 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.97 | 2.31 | 3.76 | 0.00 | 6.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.66 | 29.04 | 47.45 | 15.00 | 126.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.86 | 18.69 | 30.32 | 1.00 | 93.1 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.53 | 28.20 | 2.00 | 90.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.76 | 14.22 | 23.14 | 5.00 | 85.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 4.02 | 10.44 | 16.61 | 6.00 | 77.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 2.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 58.44
- Actual score: 28.00
- Transfer: Trent Alexander-Arnold -> Ola Aina (projected gain 2.90, hit 0)
- Autosub: Enzo Fernández replaced Pedro Porro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.54 | 17.22 | 6.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 1.66 | 6.03 | 10.48 | 0.00 | 48.7 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 5.30 | 13.73 | 21.36 | 1.00 | 113.1 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.95 | 12.97 | 20.08 | 1.00 | 106.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.43 | 12.36 | 19.91 | 5.00 | 100.8 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.68 | 11.01 | 17.98 | 0.00 | 87.6 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 1.51 | 5.58 | 9.37 | 0.00 | 33.7 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.72 | 11.44 | 18.04 | 2.00 | 71.7 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.97 | 11.38 | 18.72 | 1.00 | 74.3 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.06 | 0.97 | 1.89 | 0.00 | 5.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 6.11 | 19.96 | 33.85 | 0.00 | 81.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.92 | 17.03 | 27.47 | 6.00 | 101.8 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.03 | 16.73 | 26.20 | 2.00 | 108.2 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.55 | 15.29 | 26.42 | 0.00 | 62.3 | 0.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.21 | 10.12 | 16.66 | 2.00 | 77.9 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 2.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ismaïla Sarr
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.85
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.37) beats the best remaining Bench Boost opportunity (9.72).
- Transfer: Enzo Fernández -> Ismaïla Sarr (projected gain 4.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.37) beats the best remaining Bench Boost opportunity (9.72).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.58 | 12.73 | 20.11 | 2.00 | 106.1 | 90.0 |
| Bench 1 | Bench Boost | Alisson Ramses Becker | GK | 12 | 5.6 | 2.58 | 8.28 | 14.72 | 0.00 | 65.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.51 | 20.20 | 1.00 | 97.6 | 15.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.81 | 11.88 | 18.87 | 2.00 | 46.5 | 75.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.13 | 11.45 | 18.24 | 6.00 | 84.5 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.15 | 9.39 | 15.18 | 1.00 | 75.7 | 39.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.75 | 8.87 | 15.32 | 0.00 | 40.8 | 2.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.91 | 11.37 | 18.42 | 2.00 | 72.0 | 71.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.47 | 8.64 | 14.69 | 1.00 | 61.5 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.57 | 1.36 | 2.26 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.80 | 24.08 | 40.99 | 3.00 | 91.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.69 | 15.59 | 27.91 | 6.00 | 19.3 | 90.0 |
| Vice Captain | XI | Ismaïla Sarr | MID | 7 | 5.7 | 6.22 | 14.70 | 23.51 | 2.00 | 49.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.2 | 4.68 | 13.65 | 22.40 | 0.00 | 69.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.38 | 13.35 | 22.55 | 8.00 | 75.4 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.56
- Actual score: 37.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> William Saliba (projected gain 6.44, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.60 | 18.36 | 2.00 | 95.2 | 90.0 |
| Bench 1 | Bench | Alisson Ramses Becker | GK | 12 | 5.6 | 2.27 | 7.90 | 14.36 | 0.00 | 29.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.4 | 4.84 | 13.42 | 21.26 | 2.00 | 109.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.16 | 12.15 | 19.05 | 9.00 | 92.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.88 | 11.17 | 17.23 | 8.00 | 75.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.69 | 10.04 | 16.93 | 1.00 | 31.3 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.3 | 1.80 | 7.10 | 12.81 | 0.00 | 56.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.24 | 10.88 | 18.12 | 1.00 | 68.8 | 27.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.84 | 9.66 | 16.16 | 2.00 | 69.8 | 64.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.27 | 0.95 | 1.63 | 0.00 | 6.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 24.68 | 40.64 | 2.00 | 106.8 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 5.31 | 17.22 | 29.85 | 1.00 | 74.0 | 31.0 |
| XI | XI | Ismaïla Sarr | MID | 7 | 5.7 | 3.79 | 12.44 | 19.54 | 2.00 | 64.8 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 3.66 | 11.06 | 18.35 | 3.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 1.01 | 7.28 | 14.50 | 0.00 | 5.8 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 255.61
- Total actual points: 175.00
- Average predicted points: 63.90
- Average actual points: 43.75
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
- Predicted score: 69.93
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.74 | 10.89 | 17.64 | 3.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.21 | 9.64 | 15.76 | 2.00 | 90.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.33 | 16.56 | 26.74 | 2.00 | 97.3 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.83 | 13.02 | 21.08 | 2.00 | 102.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.51 | 2.00 | 91.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.60 | 11.65 | 18.34 | 6.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.58 | 10.67 | 17.59 | 1.00 | 81.4 | 86.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.56 | 10.74 | 16.84 | 2.00 | 73.2 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.52 | 10.14 | 16.79 | 9.00 | 65.4 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.97 | 2.31 | 3.76 | 0.00 | 6.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.66 | 29.04 | 47.45 | 15.00 | 127.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.86 | 18.69 | 30.32 | 1.00 | 93.1 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.53 | 28.20 | 2.00 | 90.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.66 | 13.93 | 22.67 | 5.00 | 86.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.79 | 9.84 | 15.66 | 6.00 | 73.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 60.02
- Actual score: 24.00
- Transfer: Pedro Porro -> Ola Aina (projected gain 4.78, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.54 | 17.22 | 6.00 | 92.3 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.68 | 10.30 | 16.54 | 3.00 | 94.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.01 | 13.55 | 23.12 | 0.00 | 70.2 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.95 | 12.97 | 20.08 | 1.00 | 105.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.43 | 12.36 | 19.91 | 5.00 | 97.8 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.90 | 10.26 | 17.80 | 0.00 | 74.8 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 2.32 | 8.56 | 14.38 | 0.00 | 51.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.79 | 10.87 | 17.86 | 1.00 | 75.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.44 | 10.57 | 16.67 | 2.00 | 65.7 | 79.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.06 | 0.97 | 1.89 | 0.00 | 5.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.15 | 26.62 | 45.14 | 0.00 | 101.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.92 | 17.03 | 27.47 | 6.00 | 101.8 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.03 | 16.73 | 26.20 | 2.00 | 108.2 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.37 | 14.67 | 25.34 | 0.00 | 63.3 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.10 | 9.77 | 16.08 | 2.00 | 74.9 | 90.0 |

## GW30

- Train rows: 154090
- Bank: -0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.98
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.73) beats the best remaining Bench Boost opportunity (8.50).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 5.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.73) beats the best remaining Bench Boost opportunity (8.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.58 | 12.73 | 20.11 | 2.00 | 107.1 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.23 | 7.88 | 13.66 | 3.00 | 81.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.51 | 20.20 | 1.00 | 95.6 | 15.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.81 | 11.13 | 18.12 | 2.00 | 88.2 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.97 | 9.82 | 15.60 | 2.00 | 64.5 | 75.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.08 | 9.17 | 14.81 | 1.00 | 73.7 | 39.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.4 | 2.71 | 8.49 | 14.87 | 8.00 | 59.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.66 | 10.65 | 17.26 | 2.00 | 67.0 | 71.0 |
| Bench 3 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.22 | 7.76 | 13.19 | 1.00 | 55.5 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.57 | 1.36 | 2.26 | 0.00 | 6.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.47 | 23.09 | 39.29 | 3.00 | 86.3 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.62 | 13.48 | 22.12 | 0.00 | 70.9 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.38 | 13.35 | 22.55 | 8.00 | 76.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.35 | 11.13 | 19.94 | 6.00 | 29.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.51 | 10.02 | 16.28 | 11.00 | 71.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.68
- Actual score: 37.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> Joško Gvardiol (projected gain 12.67, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.94 | 11.60 | 18.36 | 2.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.79 | 8.90 | 14.92 | 3.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.84 | 13.42 | 21.26 | 2.00 | 105.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.1 | 4.16 | 12.15 | 19.05 | 9.00 | 91.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.94 | 11.61 | 19.07 | 1.00 | 89.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.41 | 9.83 | 15.16 | 8.00 | 66.0 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.3 | 1.57 | 6.19 | 11.17 | 0.00 | 48.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.86 | 9.60 | 15.99 | 1.00 | 60.8 | 27.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.55 | 8.67 | 14.50 | 2.00 | 62.8 | 64.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.27 | 0.95 | 1.63 | 0.00 | 6.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.40 | 24.68 | 40.64 | 2.00 | 108.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.90 | 14.80 | 24.56 | 3.00 | 89.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.53 | 14.70 | 25.48 | 1.00 | 63.0 | 31.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.34 | 10.40 | 17.32 | 2.00 | 73.7 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 6.1 | 0.72 | 5.20 | 10.36 | 0.00 | 6.8 | 0.0 |
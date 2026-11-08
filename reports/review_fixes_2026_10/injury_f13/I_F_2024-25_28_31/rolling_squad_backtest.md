# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 258.21
- Total actual points: 176.00
- Average predicted points: 64.55
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.05
- Actual score: 61.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.75 | 10.92 | 17.66 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.21 | 9.62 | 15.71 | 2.00 | 90.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.31 | 16.58 | 26.80 | 2.00 | 97.1 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.82 | 12.98 | 21.02 | 2.00 | 102.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.08 | 19.47 | 2.00 | 91.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.62 | 11.63 | 18.24 | 6.00 | 87.6 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.57 | 10.71 | 17.67 | 1.00 | 81.0 | 86.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.57 | 10.73 | 16.79 | 2.00 | 73.1 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.53 | 10.14 | 16.75 | 9.00 | 65.5 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.97 | 2.29 | 3.71 | 0.00 | 6.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.66 | 29.10 | 47.55 | 15.00 | 127.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.94 | 18.81 | 30.35 | 1.00 | 92.5 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.08 | 17.51 | 28.16 | 2.00 | 91.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.67 | 13.92 | 22.64 | 5.00 | 87.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.80 | 9.88 | 15.71 | 6.00 | 73.4 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Justin Kluivert
- Chip used: none
- Predicted score: 60.94
- Actual score: 24.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 3.95, hit 0)
- Autosub: Enzo Fernández replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.5 | 3.65 | 10.56 | 17.25 | 6.00 | 91.7 | 90.0 |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.69 | 10.28 | 16.49 | 3.00 | 94.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 5.32 | 13.72 | 21.31 | 1.00 | 111.1 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.99 | 13.57 | 23.19 | 0.00 | 69.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.43 | 12.34 | 19.86 | 5.00 | 98.0 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.59 | 17.31 | 0.00 | 83.2 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 2.34 | 8.55 | 14.30 | 0.00 | 51.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.80 | 10.87 | 17.84 | 1.00 | 75.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.46 | 10.57 | 16.62 | 2.00 | 65.6 | 79.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.06 | 0.94 | 1.83 | 0.00 | 5.1 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.15 | 26.69 | 45.27 | 0.00 | 100.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.92 | 17.02 | 27.43 | 6.00 | 101.9 | 90.0 |
| Vice Captain | Captain | Justin Kluivert | MID | 3 | 6.1 | 6.04 | 16.72 | 26.18 | 2.00 | 108.4 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.46 | 14.82 | 25.42 | 0.00 | 62.7 | 0.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.11 | 9.80 | 16.12 | 2.00 | 74.4 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.60
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.21) beats the best remaining Bench Boost opportunity (8.40).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 3.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.21) beats the best remaining Bench Boost opportunity (8.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.58 | 12.75 | 20.13 | 2.00 | 106.6 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.23 | 7.86 | 13.61 | 3.00 | 81.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.49 | 20.15 | 1.00 | 95.7 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.07 | 11.21 | 17.80 | 6.00 | 82.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.81 | 11.10 | 18.07 | 2.00 | 88.4 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.99 | 9.80 | 15.53 | 2.00 | 64.4 | 75.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.17 | 7.03 | 12.17 | 0.00 | 50.4 | 2.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.67 | 10.66 | 17.25 | 2.00 | 67.1 | 71.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.24 | 7.76 | 13.14 | 1.00 | 55.4 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.58 | 1.34 | 2.20 | 0.00 | 6.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.48 | 23.15 | 39.40 | 3.00 | 85.8 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.63 | 13.48 | 22.09 | 0.00 | 71.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.39 | 13.34 | 22.52 | 8.00 | 76.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.44 | 11.28 | 20.03 | 6.00 | 28.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.52 | 10.04 | 16.31 | 11.00 | 71.1 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.62
- Actual score: 41.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Justin Kluivert -> Luis Díaz (projected gain 4.84, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.42) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 11.63 | 18.38 | 2.00 | 93.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.80 | 8.89 | 14.87 | 3.00 | 88.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.84 | 13.40 | 21.22 | 2.00 | 106.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.19 | 12.17 | 19.01 | 9.00 | 91.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.44 | 9.84 | 15.09 | 8.00 | 65.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.72 | 7.46 | 12.60 | 1.00 | 45.9 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 0.86 | 5.14 | 10.09 | 0.00 | 24.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.88 | 9.61 | 15.98 | 1.00 | 60.9 | 27.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.58 | 8.67 | 14.43 | 2.00 | 62.6 | 64.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.28 | 0.93 | 1.58 | 0.00 | 6.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.42 | 24.74 | 40.74 | 2.00 | 108.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.64 | 14.88 | 25.58 | 1.00 | 62.2 | 31.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.93 | 14.82 | 24.53 | 3.00 | 89.1 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.44 | 13.30 | 22.21 | 6.00 | 73.9 | 35.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.34 | 10.43 | 17.35 | 2.00 | 73.1 | 90.0 |
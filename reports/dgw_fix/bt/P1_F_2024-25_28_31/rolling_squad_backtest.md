# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 245.92
- Total actual points: 190.00
- Average predicted points: 61.48
- Average actual points: 47.50
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
- Predicted score: 69.86
- Actual score: 68.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.76 | 10.89 | 17.64 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.23 | 9.64 | 15.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.31 | 16.56 | 26.74 | 2.00 | 90.0 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.83 | 13.02 | 21.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.16 | 12.11 | 19.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 4.39 | 11.65 | 18.34 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.60 | 10.67 | 17.59 | 1.00 | 82.0 | 86.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.41 | 10.74 | 16.84 | 2.00 | 71.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.43 | 10.14 | 16.79 | 9.00 | 64.0 | 90.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.98 | 2.31 | 3.76 | 0.00 | 6.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 10.86 | 29.04 | 47.45 | 15.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 6.89 | 18.69 | 30.32 | 1.00 | 90.0 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 6.05 | 17.53 | 28.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.59 | 13.93 | 22.67 | 5.00 | 85.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.71 | 9.84 | 15.66 | 6.00 | 73.7 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Justin Kluivert
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 48.54
- Actual score: 31.00
- Transfer: Virgil van Dijk -> Joško Gvardiol (projected gain 1.38, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.68 | 10.54 | 17.22 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.62 | 10.30 | 16.54 | 3.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.97 | 13.73 | 21.36 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.00 | 13.55 | 23.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.34 | 12.36 | 19.91 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.55 | 10.56 | 17.24 | 0.00 | 83.9 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 0.00 | 8.56 | 14.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.64 | 10.87 | 17.86 | 1.00 | 72.6 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.34 | 10.57 | 16.67 | 2.00 | 65.3 | 79.0 |
| XI | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.07 | 0.97 | 1.89 | 0.00 | 4.9 | 0.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 12 | 13.8 | 0.00 | 26.62 | 45.14 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 8.1 | 5.80 | 17.03 | 27.47 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.1 | 5.73 | 16.73 | 26.20 | 2.00 | 90.0 | 78.0 |
| XI | Bench | Cole Palmer | MID | 6 | 10.9 | 4.64 | 14.67 | 25.34 | 0.00 | 66.3 | 0.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.00 | 9.77 | 16.08 | 2.00 | 73.9 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.26
- Actual score: 50.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.46) beats the best remaining Bench Boost opportunity (8.66).
- Transfer: Trent Alexander-Arnold -> William Saliba (projected gain 3.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.46) beats the best remaining Bench Boost opportunity (8.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 4.46 | 12.73 | 20.11 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.40 | 7.88 | 13.66 | 3.00 | 83.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 4.33 | 12.51 | 20.20 | 1.00 | 90.0 | 15.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.09 | 11.20 | 17.85 | 6.00 | 83.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.83 | 11.13 | 18.12 | 2.00 | 87.9 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.77 | 9.82 | 15.60 | 2.00 | 61.7 | 75.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.18 | 7.01 | 12.10 | 0.00 | 50.6 | 2.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.61 | 10.65 | 17.26 | 2.00 | 67.3 | 71.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.31 | 7.76 | 13.19 | 1.00 | 57.6 | 78.0 |
| Bench 4 | Bench Boost | Shumaira Mheuka | FWD | 6 | 4.5 | 0.57 | 1.36 | 2.26 | 0.00 | 6.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.59 | 23.09 | 39.29 | 3.00 | 86.9 | 90.0 |
| Vice Captain | XI | Justin Kluivert | MID | 3 | 6.2 | 4.81 | 13.48 | 22.12 | 0.00 | 74.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.65 | 13.35 | 22.55 | 8.00 | 81.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 3.59 | 11.13 | 19.94 | 6.00 | 32.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.45 | 10.02 | 16.28 | 11.00 | 71.2 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 1.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.25
- Actual score: 41.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Justin Kluivert -> Luis Díaz (projected gain 4.80, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.49) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.87 | 11.60 | 18.36 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.85 | 8.90 | 14.92 | 3.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.62 | 13.42 | 21.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.05 | 12.15 | 19.05 | 9.00 | 88.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.33 | 9.83 | 15.16 | 8.00 | 65.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 2.71 | 7.44 | 12.54 | 1.00 | 45.6 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 1.32 | 5.16 | 10.13 | 0.00 | 32.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.82 | 9.60 | 15.99 | 1.00 | 61.0 | 27.0 |
| Bench 2 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.55 | 8.67 | 14.50 | 2.00 | 63.5 | 64.0 |
| Bench 4 | Bench | Shumaira Mheuka | FWD | 6 | 4.5 | 0.26 | 0.95 | 1.63 | 0.00 | 5.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.49 | 24.68 | 40.64 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.96 | 14.80 | 24.56 | 3.00 | 89.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.7 | 4.60 | 14.70 | 25.48 | 1.00 | 63.6 | 31.0 |
| XI | XI | Luis Díaz | MID | 12 | 7.5 | 4.48 | 13.31 | 22.24 | 6.00 | 74.0 | 35.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.33 | 10.40 | 17.32 | 2.00 | 75.0 | 90.0 |
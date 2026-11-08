# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 249.77
- Total actual points: 171.00
- Average predicted points: 62.44
- Average actual points: 42.75
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
- Predicted score: 65.67
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.67 | 10.88 | 17.88 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.10 | 9.55 | 15.73 | 2.00 | 87.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.74 | 15.91 | 25.98 | 2.00 | 90.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.57 | 12.58 | 20.44 | 2.00 | 100.7 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.57 | 10.90 | 18.01 | 2.00 | 81.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.59 | 10.77 | 17.92 | 1.00 | 79.5 | 86.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.84 | 10.64 | 17.18 | 6.00 | 79.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.45 | 10.27 | 16.38 | 2.00 | 70.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.38 | 9.79 | 16.36 | 9.00 | 63.0 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.4 | 2.66 | 8.33 | 13.65 | 2.00 | 73.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.77 | 28.32 | 46.33 | 15.00 | 122.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.79 | 18.83 | 30.43 | 1.00 | 91.3 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.97 | 17.16 | 28.02 | 2.00 | 87.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.70 | 14.21 | 23.60 | 5.00 | 82.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.81 | 10.29 | 16.35 | 6.00 | 75.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.70
- Actual score: 19.00
- Transfer: Virgil van Dijk -> Ola Aina (projected gain 0.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.58 | 10.67 | 17.52 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.27 | 9.39 | 15.44 | 3.00 | 85.3 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.07 | 13.70 | 23.33 | 0.00 | 68.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.64 | 10.73 | 17.53 | 1.00 | 83.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.59 | 10.47 | 17.17 | 1.00 | 82.9 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.31 | 10.34 | 17.26 | 0.00 | 77.0 | 0.0 |
| Bench 4 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 2.93 | 10.13 | 16.87 | 0.00 | 60.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.75 | 10.79 | 17.52 | 1.00 | 77.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.85 | 10.34 | 16.42 | 2.00 | 67.8 | 79.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.3 | 3.02 | 8.20 | 13.24 | 2.00 | 75.2 | 90.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.21 | 26.34 | 44.34 | 0.00 | 98.3 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | 6 | 11.0 | 5.46 | 16.26 | 27.10 | 0.00 | 78.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.12 | 15.40 | 25.38 | 6.00 | 87.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 4.89 | 14.49 | 23.82 | 2.00 | 86.0 | 78.0 |
| Bench 2 | Bench | Enzo Fernández | MID | 6 | 4.7 | 3.26 | 9.80 | 16.24 | 2.00 | 76.1 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.22
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (8.48).
- Transfer: Jamie Vardy -> Yoane Wissa (projected gain 2.15, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.19) beats the best remaining Triple Captain opportunity (8.48).
- Autosub outfielders: Norberto Bercique Gomes Betuncal, Daniel Muñoz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.71 | 11.00 | 18.11 | 2.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.90 | 9.39 | 15.55 | 3.00 | 89.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.19 | 11.79 | 18.16 | 6.00 | 83.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.72 | 11.62 | 20.11 | 0.00 | 55.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 3.78 | 10.84 | 16.98 | 1.00 | 82.7 | 39.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 5.0 | 2.97 | 8.27 | 13.99 | 2.00 | 48.8 | 75.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.22 | 7.27 | 12.66 | 0.00 | 48.6 | 2.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.97 | 11.69 | 19.15 | 5.00 | 78.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.77 | 10.77 | 17.55 | 2.00 | 71.7 | 71.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.04 | 9.56 | 15.78 | 1.00 | 66.6 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.19 | 22.18 | 37.93 | 3.00 | 79.3 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | 3 | 6.2 | 5.50 | 16.02 | 25.62 | 0.00 | 84.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.21 | 15.63 | 25.29 | 8.00 | 89.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 4.20 | 12.25 | 21.73 | 6.00 | 40.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.60 | 10.17 | 16.54 | 11.00 | 70.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.18
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.57) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 2.16, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.57) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.57 | 11.02 | 17.94 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.72 | 8.77 | 15.09 | 3.00 | 85.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.82 | 11.34 | 18.98 | 9.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.48 | 10.67 | 18.05 | 1.00 | 81.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.26 | 9.88 | 15.94 | 8.00 | 62.2 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.4 | 2.64 | 8.53 | 14.80 | 0.00 | 64.3 | 0.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.54 | 7.16 | 12.40 | 1.00 | 39.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.6 | 3.53 | 10.91 | 18.21 | 2.00 | 72.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 2.93 | 9.49 | 15.94 | 1.00 | 61.2 | 27.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.67 | 8.84 | 15.16 | 2.00 | 63.0 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.97 | 23.70 | 40.20 | 2.00 | 99.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.04 | 14.84 | 25.10 | 3.00 | 87.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.09 | 13.74 | 23.36 | 1.00 | 55.3 | 31.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.57 | 11.08 | 18.25 | 2.00 | 76.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.3 | 3.37 | 10.52 | 18.22 | 0.00 | 44.9 | 0.0 |
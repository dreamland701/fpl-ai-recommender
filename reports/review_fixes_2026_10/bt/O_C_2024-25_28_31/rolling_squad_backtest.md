# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 255.09
- Total actual points: 164.00
- Average predicted points: 63.77
- Average actual points: 41.00
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
- Predicted score: 64.88
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 11.17 | 18.34 | 3.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.5 | 3.31 | 9.38 | 15.23 | 10.00 | 82.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.55 | 15.73 | 25.80 | 2.00 | 92.8 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.36 | 12.21 | 19.89 | 2.00 | 99.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.81 | 11.27 | 18.71 | 1.00 | 82.6 | 86.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.68 | 11.25 | 18.56 | 2.00 | 83.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.89 | 11.03 | 17.85 | 6.00 | 82.2 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.76 | 10.82 | 17.20 | 2.00 | 73.5 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.67 | 10.53 | 17.49 | 9.00 | 66.1 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 3.00 | 9.16 | 15.49 | 8.00 | 50.0 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.11 | 26.84 | 44.23 | 15.00 | 120.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.58 | 18.20 | 29.47 | 1.00 | 88.8 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.87 | 17.40 | 28.46 | 2.00 | 89.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 5.30 | 15.55 | 25.69 | 5.00 | 89.6 | 90.0 |
| XI | XI | Mikkel Damsgaard | MID | 4 | 5.1 | 3.75 | 11.23 | 18.35 | 2.00 | 82.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.51
- Actual score: 20.00
- Transfer: Mikkel Damsgaard -> Enzo Fernández (projected gain 0.40, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 11.09 | 18.18 | 6.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.56 | 8.83 | 15.12 | 0.00 | 68.5 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.15 | 13.91 | 23.68 | 0.00 | 70.0 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.52 | 10.88 | 18.13 | 0.00 | 80.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.73 | 10.83 | 17.74 | 1.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 5.0 | 3.12 | 10.63 | 17.67 | 0.00 | 63.5 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.67 | 9.70 | 16.95 | 0.00 | 70.3 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 4.05 | 11.87 | 19.08 | 1.00 | 79.2 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 4.03 | 11.51 | 18.09 | 2.00 | 70.8 | 79.0 |
| Bench 2 | Bench | Raúl Jiménez | FWD | 9 | 5.5 | 3.55 | 10.30 | 16.62 | 2.00 | 60.0 | 62.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.8 | 8.09 | 26.06 | 43.89 | 0.00 | 96.6 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | 6 | 11.0 | 5.54 | 16.68 | 27.66 | 0.00 | 78.5 | 0.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 5.49 | 16.06 | 26.25 | 2.00 | 93.4 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.29 | 15.79 | 26.01 | 6.00 | 89.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.74 | 11.14 | 18.26 | 2.00 | 81.3 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.64
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.35) beats the best remaining Triple Captain opportunity (8.67).
- Transfer: Pedro Porro -> Ola Aina (projected gain 2.51, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.35) beats the best remaining Triple Captain opportunity (8.67).
- Autosub outfielders: Daniel Muñoz, Raúl Jiménez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 11.51 | 18.91 | 2.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 2.37 | 6.92 | 12.08 | 2.00 | 51.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.34 | 12.17 | 18.77 | 6.00 | 86.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.88 | 11.97 | 20.64 | 0.00 | 57.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.03 | 11.43 | 17.91 | 1.00 | 85.7 | 39.0 |
| Bench 2 | Autosub In | Daniel Muñoz | DEF | 7 | 5.0 | 3.18 | 8.98 | 15.20 | 2.00 | 54.1 | 75.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.62 | 8.31 | 14.64 | 8.00 | 57.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.83 | 11.40 | 18.44 | 2.00 | 73.3 | 71.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.40 | 10.74 | 17.55 | 1.00 | 71.7 | 78.0 |
| Bench 3 | Autosub In | Raúl Jiménez | FWD | 9 | 5.5 | 2.87 | 9.20 | 15.07 | 2.00 | 56.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 7.35 | 22.48 | 38.28 | 3.00 | 78.5 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | 3 | 6.2 | 5.77 | 16.73 | 26.82 | 0.00 | 90.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.36 | 16.14 | 26.09 | 8.00 | 91.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 4.10 | 11.89 | 21.19 | 6.00 | 38.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.93 | 10.85 | 17.68 | 11.00 | 75.3 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.40 -> 2.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.06
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.46) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Nikola Milenković (projected gain 0.81, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.46) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.80 | 11.53 | 18.76 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.6 | 2.77 | 8.43 | 14.07 | 3.00 | 72.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.89 | 11.58 | 19.33 | 9.00 | 83.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 4.9 | 3.36 | 10.71 | 17.82 | 1.00 | 87.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.48 | 10.63 | 17.97 | 1.00 | 80.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.48 | 10.35 | 16.69 | 8.00 | 65.3 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.4 | 2.80 | 8.98 | 15.52 | 0.00 | 67.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.20 | 10.11 | 16.84 | 1.00 | 63.1 | 27.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.12 | 9.97 | 16.98 | 2.00 | 69.6 | 64.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.5 | 2.77 | 8.44 | 14.15 | 1.00 | 61.3 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.01 | 23.82 | 40.32 | 2.00 | 98.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.43 | 15.76 | 26.44 | 3.00 | 90.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.21 | 13.75 | 23.42 | 1.00 | 55.4 | 31.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 4.01 | 11.94 | 19.67 | 2.00 | 81.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.3 | 3.71 | 11.30 | 19.48 | 0.00 | 49.7 | 0.0 |
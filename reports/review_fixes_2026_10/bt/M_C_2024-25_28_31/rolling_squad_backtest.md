# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 255.66
- Total actual points: 166.00
- Average predicted points: 63.91
- Average actual points: 41.50
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
- Predicted score: 65.02
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.78 | 11.18 | 18.35 | 3.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.5 | 3.32 | 9.37 | 15.21 | 10.00 | 82.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.53 | 15.76 | 25.90 | 2.00 | 92.8 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.34 | 12.21 | 19.95 | 2.00 | 99.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.83 | 11.35 | 18.94 | 1.00 | 82.6 | 86.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.66 | 11.31 | 18.60 | 2.00 | 83.5 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.90 | 11.04 | 17.91 | 6.00 | 82.2 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.73 | 10.87 | 17.40 | 2.00 | 73.5 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.68 | 10.61 | 17.73 | 9.00 | 66.1 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez | FWD | 9 | 5.6 | 3.02 | 9.21 | 15.65 | 8.00 | 50.0 | 68.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.09 | 26.93 | 44.56 | 15.00 | 120.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.59 | 18.27 | 29.72 | 1.00 | 88.8 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.90 | 17.48 | 28.63 | 2.00 | 89.8 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 5.27 | 15.60 | 25.87 | 5.00 | 89.6 | 90.0 |
| XI | XI | Yankuba Minteh | MID | 5 | 5.0 | 3.97 | 11.33 | 18.52 | 2.00 | 79.1 | 76.0 |

## GW29

- Train rows: 153301
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.62
- Actual score: 22.00
- Transfer: Yankuba Minteh -> Enzo Fernández (projected gain 0.87, hit 0)
- Autosub: Raúl Jiménez replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.79 | 11.13 | 18.29 | 6.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.5 | 2.56 | 8.83 | 15.12 | 0.00 | 68.5 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.15 | 13.99 | 23.94 | 0.00 | 70.0 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.93 | 18.25 | 0.00 | 80.5 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.75 | 10.88 | 17.88 | 1.00 | 84.3 | 90.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.9 | 3.12 | 10.60 | 17.67 | 0.00 | 63.5 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.67 | 9.74 | 17.08 | 0.00 | 70.3 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.04 | 11.96 | 19.36 | 1.00 | 79.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 4.00 | 11.61 | 18.41 | 2.00 | 70.8 | 79.0 |
| Bench 2 | Autosub In | Raúl Jiménez | FWD | 9 | 5.5 | 3.52 | 10.37 | 16.87 | 2.00 | 60.1 | 62.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.7 | 8.10 | 26.30 | 44.53 | 0.00 | 96.6 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | 6 | 11.0 | 5.57 | 16.83 | 28.09 | 0.00 | 78.4 | 0.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 5.52 | 16.15 | 26.41 | 2.00 | 93.4 | 78.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.32 | 15.92 | 26.36 | 6.00 | 89.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.77 | 11.24 | 18.44 | 2.00 | 81.2 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.50 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.63
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (8.68).
- Transfer: Pedro Porro -> Ola Aina (projected gain 2.56, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (8.68).
- Autosub: Daniel Muñoz replaced Trent Alexander-Arnold.
- Autosub: Raúl Jiménez replaced Justin Kluivert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.95 | 11.59 | 19.06 | 2.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.5 | 2.35 | 6.95 | 12.11 | 2.00 | 51.6 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.34 | 12.25 | 18.84 | 6.00 | 86.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 3.89 | 12.07 | 20.93 | 0.00 | 57.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.4 | 4.02 | 11.52 | 18.06 | 1.00 | 85.8 | 39.0 |
| Bench 2 | Autosub In | Daniel Muñoz | DEF | 7 | 4.9 | 3.16 | 9.02 | 15.23 | 2.00 | 54.1 | 75.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 2.63 | 8.41 | 14.81 | 8.00 | 57.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.86 | 11.52 | 18.68 | 2.00 | 73.3 | 71.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.39 | 10.83 | 17.72 | 1.00 | 71.7 | 78.0 |
| Bench 3 | Autosub In | Raúl Jiménez | FWD | 9 | 5.5 | 2.90 | 9.30 | 15.29 | 2.00 | 56.0 | 76.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.36 | 22.74 | 38.84 | 3.00 | 78.5 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | 3 | 6.1 | 5.77 | 16.87 | 26.98 | 0.00 | 90.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.34 | 16.20 | 26.41 | 8.00 | 92.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 4.08 | 11.99 | 21.63 | 6.00 | 38.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.91 | 10.95 | 18.01 | 11.00 | 75.3 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.40 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.38
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Marc Cucurella Saseta (projected gain 0.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.81 | 11.62 | 18.87 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 7 | 4.5 | 2.79 | 8.44 | 14.04 | 3.00 | 72.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.88 | 11.50 | 19.19 | 9.00 | 83.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 6 | 5.3 | 3.55 | 10.68 | 17.76 | 1.00 | 84.5 | 13.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.49 | 10.63 | 18.00 | 1.00 | 80.7 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.49 | 10.32 | 16.51 | 8.00 | 65.3 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.4 | 2.83 | 8.97 | 15.58 | 0.00 | 67.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.21 | 10.21 | 17.13 | 1.00 | 63.0 | 27.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.15 | 10.03 | 17.04 | 2.00 | 69.6 | 64.0 |
| Bench 4 | Bench Boost | Raúl Jiménez | FWD | 9 | 5.5 | 2.76 | 8.43 | 14.19 | 1.00 | 61.3 | 14.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.02 | 23.88 | 40.43 | 2.00 | 98.9 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.44 | 15.75 | 26.49 | 3.00 | 90.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.23 | 13.96 | 23.99 | 1.00 | 55.4 | 31.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 4.04 | 11.99 | 19.94 | 2.00 | 81.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 3.68 | 11.21 | 19.51 | 0.00 | 49.7 | 0.0 |
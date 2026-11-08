# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 250.22
- Total actual points: 175.00
- Average predicted points: 62.55
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.59
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.66 | 10.89 | 17.91 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.00 | 9.16 | 15.26 | 8.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.72 | 15.97 | 26.14 | 2.00 | 90.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.55 | 12.59 | 20.51 | 2.00 | 100.7 | 90.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 5.9 | 3.55 | 10.97 | 18.06 | 2.00 | 81.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.61 | 10.85 | 18.16 | 1.00 | 79.5 | 86.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 4.9 | 3.84 | 10.64 | 17.25 | 6.00 | 79.3 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.41 | 10.33 | 16.56 | 2.00 | 70.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.38 | 9.86 | 16.56 | 9.00 | 63.0 | 90.0 |
| Bench 4 | Bench | Liam Delap | FWD | 10 | 5.6 | 2.86 | 8.57 | 14.34 | 2.00 | 67.7 | 82.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 9.76 | 28.47 | 46.85 | 15.00 | 122.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.79 | 18.91 | 30.75 | 1.00 | 91.3 | 72.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 6.01 | 17.24 | 28.24 | 2.00 | 87.6 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.68 | 14.26 | 23.73 | 5.00 | 82.8 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.81 | 10.32 | 16.50 | 6.00 | 75.5 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.78
- Actual score: 23.00
- Transfer: Virgil van Dijk -> Ola Aina (projected gain 0.93, hit 0)
- Autosub: Enzo Fernández replaced Trent Alexander-Arnold.
- Autosub: Liam Delap replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.60 | 10.69 | 17.62 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.38 | 9.87 | 16.16 | 1.00 | 86.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 4.07 | 13.77 | 23.59 | 0.00 | 68.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.64 | 10.76 | 17.59 | 1.00 | 83.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.61 | 10.50 | 17.27 | 1.00 | 82.9 | 90.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.32 | 10.39 | 17.39 | 0.00 | 76.9 | 0.0 |
| Bench 3 | Bench | Daniel Muñoz | DEF | 7 | 4.9 | 2.93 | 10.09 | 16.86 | 0.00 | 60.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.74 | 10.84 | 17.65 | 1.00 | 77.1 | 90.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.81 | 10.41 | 16.56 | 2.00 | 67.9 | 79.0 |
| Bench 4 | Autosub In | Liam Delap | FWD | 10 | 5.6 | 2.64 | 8.38 | 13.86 | 2.00 | 63.1 | 78.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.7 | 8.22 | 26.59 | 45.02 | 0.00 | 98.3 | 0.0 |
| Vice Captain | Bench | Cole Palmer | MID | 6 | 11.0 | 5.49 | 16.40 | 27.49 | 0.00 | 78.8 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.15 | 15.52 | 25.75 | 6.00 | 87.5 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.0 | 4.91 | 14.57 | 23.92 | 2.00 | 86.0 | 78.0 |
| Bench 2 | Autosub In | Enzo Fernández | MID | 6 | 4.7 | 3.29 | 9.88 | 16.34 | 2.00 | 76.1 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 1.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Justin Kluivert
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.20
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (8.49).
- Transfer: Liam Delap -> Yoane Wissa (projected gain 2.12, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (8.49).
- Autosub: Daniel Muñoz replaced Trent Alexander-Arnold.
- Autosub: Norberto Bercique Gomes Betuncal replaced Justin Kluivert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.72 | 11.07 | 18.25 | 2.00 | 90.2 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 5.0 | 3.35 | 9.68 | 15.46 | 8.00 | 82.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 4.19 | 11.86 | 18.22 | 6.00 | 83.7 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 3.73 | 11.72 | 20.40 | 0.00 | 55.7 | 0.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.3 | 3.76 | 10.92 | 17.10 | 1.00 | 82.8 | 39.0 |
| Bench 3 | Autosub In | Daniel Muñoz | DEF | 7 | 4.9 | 2.95 | 8.31 | 14.00 | 2.00 | 48.8 | 75.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.3 | 2.23 | 7.32 | 12.75 | 0.00 | 48.6 | 2.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.95 | 11.76 | 19.35 | 5.00 | 78.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.80 | 10.91 | 17.74 | 2.00 | 71.7 | 71.0 |
| Bench 2 | Autosub In | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 3.03 | 9.66 | 15.94 | 1.00 | 66.6 | 78.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.20 | 22.43 | 38.48 | 3.00 | 79.2 | 90.0 |
| Vice Captain | Bench | Justin Kluivert | MID | 3 | 6.1 | 5.50 | 16.15 | 25.78 | 0.00 | 84.1 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.20 | 15.69 | 25.62 | 8.00 | 89.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.9 | 4.18 | 12.34 | 22.16 | 6.00 | 40.7 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.58 | 10.25 | 16.86 | 11.00 | 70.6 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.64
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.95) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 2.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.95) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.5 | 3.58 | 11.09 | 18.02 | 2.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 5.0 | 3.07 | 9.40 | 15.96 | 3.00 | 83.8 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.9 | 3.80 | 11.26 | 18.83 | 9.00 | 83.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.48 | 10.66 | 18.07 | 1.00 | 81.1 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.0 | 3.28 | 9.82 | 15.74 | 8.00 | 62.1 | 90.0 |
| Bench 3 | Bench Boost | Ola Aina | DEF | 16 | 5.3 | 2.66 | 8.51 | 14.84 | 0.00 | 64.2 | 0.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.3 | 2.52 | 7.21 | 12.53 | 1.00 | 39.0 | 90.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 6.5 | 3.55 | 10.89 | 18.31 | 2.00 | 72.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.94 | 9.57 | 16.22 | 1.00 | 61.2 | 27.0 |
| Bench 2 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.70 | 8.87 | 15.19 | 2.00 | 62.9 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 7.97 | 23.77 | 40.31 | 2.00 | 99.7 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 8.0 | 5.05 | 14.83 | 25.13 | 3.00 | 87.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.12 | 13.89 | 23.85 | 1.00 | 55.2 | 31.0 |
| XI | XI | Enzo Fernández | MID | 6 | 4.7 | 3.59 | 11.07 | 18.46 | 2.00 | 76.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 6.1 | 3.34 | 10.40 | 18.24 | 0.00 | 45.0 | 0.0 |
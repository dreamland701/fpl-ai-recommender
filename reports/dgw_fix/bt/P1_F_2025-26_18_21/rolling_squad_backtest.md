# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 248.99
- Total actual points: 196.00
- Average predicted points: 62.25
- Average actual points: 49.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW17 are included before the first simulated week.
- League-average scores were not available for this run.

## GW18

- Train rows: 173897
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Hugo Ekitiké
- Vice captain: Phil Foden
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 63.43
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Joško Gvardiol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.03 | 17.91 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.45 | 9.62 | 15.57 | 6.00 | 85.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 13.76 | 21.59 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.52 | 12.44 | 19.89 | 0.00 | 86.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.19 | 11.93 | 19.02 | 2.00 | 81.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.93 | 11.30 | 17.89 | 2.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 6.0 | 3.81 | 11.29 | 18.63 | 8.00 | 79.6 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.03 | 18.80 | 28.09 | 5.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.67 | 11.03 | 17.48 | 8.00 | 65.4 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.76 | 8.23 | 13.49 | 5.00 | 58.6 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.70 | 17.92 | 28.79 | 2.00 | 82.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.66 | 16.29 | 25.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.69 | 16.24 | 25.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.51 | 24.48 | 9.00 | 83.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.47 | 15.13 | 23.36 | 2.00 | 87.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 56.25
- Actual score: 30.00
- Transfer: Marcos Senesi Barón -> Patrick Dorgu (projected gain 0.27, hit 0)
- Autosub: Igor Jesus Maciel da Cruz replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.73 | 10.59 | 17.26 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.11 | 9.33 | 15.30 | 10.00 | 84.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 11.95 | 19.66 | 6.00 | 83.2 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.02 | 11.70 | 19.10 | 1.00 | 87.6 | 33.0 |
| XI | XI | Patrick Dorgu | DEF | 14 | 4.2 | 4.59 | 11.37 | 16.97 | 2.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Jurriën Timber | DEF | 1 | 6.4 | 1.74 | 5.78 | 10.76 | 9.00 | 26.4 | 82.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.43 | 13.46 | 20.89 | 2.00 | 54.9 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.96 | 9.80 | 16.47 | 1.00 | 54.0 | 20.0 |
| Bench 2 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.21 | 9.69 | 15.57 | 2.00 | 69.0 | 61.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.36 | 16.71 | 27.94 | 3.00 | 83.0 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.08 | 16.04 | 24.31 | 2.00 | 85.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.12 | 15.04 | 24.20 | 5.00 | 84.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 12.95 | 21.03 | 1.00 | 73.2 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.28 | 12.91 | 21.00 | 0.00 | 70.8 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 61.62
- Actual score: 41.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (7.20).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 5.50, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (7.20).
- Autosub: Dominic Calvert-Lewin replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.32 | 18.24 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.40 | 10.11 | 16.43 | 1.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.46 | 12.47 | 19.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.4 | 4.02 | 11.77 | 19.24 | 3.00 | 71.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.03 | 11.74 | 19.44 | 1.00 | 86.5 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.63 | 10.93 | 17.95 | 1.00 | 63.1 | 50.0 |
| Bench 4 | Bench | Patrick Dorgu | DEF | 14 | 4.2 | 2.32 | 6.75 | 10.43 | 1.00 | 56.5 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.61 | 14.24 | 23.36 | 0.00 | 68.4 | 0.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.32 | 9.66 | 16.24 | 2.00 | 48.2 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.76 | 8.52 | 14.54 | 2.00 | 55.0 | 82.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.86 | 17.83 | 29.26 | 2.00 | 87.4 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 5.87 | 16.77 | 26.43 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.33 | 24.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.95 | 24.00 | 4.00 | 74.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.34 | 10.72 | 17.64 | 9.00 | 54.0 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Phil Foden
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 67.69
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.90) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.90) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.54 | 10.21 | 16.69 | 6.00 | 86.1 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.63 | 9.89 | 15.86 | 3.00 | 87.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.21 | 19.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.48 | 17.55 | 6.00 | 84.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 3.44 | 10.19 | 16.79 | 6.00 | 68.3 | 90.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 3.13 | 9.42 | 16.10 | 0.00 | 57.1 | 0.0 |
| Bench 3 | Bench Boost | Patrick Dorgu | DEF | 14 | 4.2 | 3.13 | 8.12 | 13.07 | 5.00 | 66.0 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.78 | 16.05 | 25.55 | 12.00 | 90.0 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.18 | 10.23 | 16.62 | 8.00 | 62.4 | 86.0 |
| Bench 4 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.10 | 9.02 | 15.27 | 2.00 | 60.8 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 16.10 | 26.92 | 2.00 | 82.5 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.08 | 14.82 | 23.66 | 1.00 | 83.2 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.53 | 23.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.81 | 22.23 | 3.00 | 76.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.64 | 13.21 | 21.71 | 2.00 | 77.2 | 73.0 |
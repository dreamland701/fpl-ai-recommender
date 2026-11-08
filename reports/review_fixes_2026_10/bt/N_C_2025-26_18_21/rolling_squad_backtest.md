# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 251.27
- Total actual points: 186.00
- Average predicted points: 62.82
- Average actual points: 46.50
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
- Vice captain: Morgan Rogers
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 65.76
- Actual score: 45.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.97 | 11.41 | 18.52 | 2.00 | 93.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.51 | 9.74 | 15.84 | 6.00 | 87.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.09 | 13.75 | 21.69 | 2.00 | 98.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.74 | 12.81 | 20.49 | 0.00 | 91.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.12 | 12.03 | 19.27 | 2.00 | 82.2 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.97 | 11.52 | 18.27 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 3.94 | 11.16 | 18.26 | 0.00 | 84.0 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.29 | 18.11 | 27.18 | 5.00 | 99.1 | 85.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.97 | 11.16 | 17.68 | 8.00 | 66.0 | 84.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 3.19 | 9.12 | 15.11 | 9.00 | 69.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.87 | 17.98 | 28.83 | 2.00 | 82.5 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.3 | 6.21 | 16.81 | 26.27 | 1.00 | 106.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.99 | 16.63 | 26.13 | 5.00 | 101.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.52 | 15.79 | 24.93 | 9.00 | 86.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.68 | 15.05 | 23.30 | 2.00 | 90.2 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 55.66
- Actual score: 30.00
- Transfer: Jurriën Timber -> Joško Gvardiol (projected gain 1.18, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.65 | 10.56 | 17.28 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.21 | 9.65 | 15.84 | 10.00 | 87.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.69 | 20.32 | 2.00 | 92.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.28 | 12.09 | 19.67 | 1.00 | 88.6 | 33.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.87 | 19.57 | 6.00 | 82.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 3.94 | 11.17 | 18.26 | 1.00 | 83.5 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.72 | 11.03 | 17.41 | 3.00 | 84.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.44 | 13.43 | 20.86 | 2.00 | 53.3 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.07 | 9.92 | 16.65 | 1.00 | 50.9 | 20.0 |
| Bench 3 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 3.49 | 9.91 | 16.37 | 2.00 | 71.8 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.42 | 16.98 | 28.31 | 3.00 | 80.9 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.12 | 15.78 | 24.01 | 2.00 | 87.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.95 | 14.99 | 24.25 | 5.00 | 82.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.05 | 13.14 | 21.28 | 1.00 | 72.4 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.07 | 12.78 | 20.87 | 0.00 | 67.9 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 62.31
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.30).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 5.20, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (7.30).
- Autosub: Dominic Calvert-Lewin replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.75 | 10.99 | 17.88 | 1.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.62 | 10.45 | 16.99 | 1.00 | 92.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.39 | 19.93 | 2.00 | 95.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.05 | 11.82 | 19.61 | 1.00 | 86.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.83 | 11.02 | 18.35 | 1.00 | 82.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.59 | 10.65 | 17.66 | 1.00 | 61.8 | 50.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.5 | 3.03 | 10.03 | 17.03 | 4.00 | 77.2 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.62 | 14.36 | 23.56 | 0.00 | 67.3 | 0.0 |
| XI | XI | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 3.81 | 10.47 | 17.16 | 5.00 | 75.2 | 84.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.22 | 9.51 | 16.09 | 2.00 | 46.3 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.95 | 17.71 | 29.20 | 2.00 | 88.5 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 6.04 | 16.51 | 26.16 | 5.00 | 101.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.24 | 15.28 | 24.53 | 1.00 | 90.5 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.95 | 14.49 | 23.44 | 4.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.20 | 10.57 | 17.46 | 9.00 | 49.3 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.80 -> 0.00
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Phil Foden
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 67.54
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Raúl Jiménez Rodríguez -> Igor Thiago Nascimento Rodrigues (projected gain 7.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.46 | 10.13 | 16.64 | 6.00 | 84.6 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.74 | 10.00 | 16.10 | 3.00 | 89.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 12.04 | 19.35 | 6.00 | 89.5 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.5 | 3.69 | 10.80 | 18.07 | 3.00 | 81.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.28 | 10.39 | 17.49 | 6.00 | 83.6 | 90.0 |
| Bench 3 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 3.05 | 9.47 | 16.24 | 0.00 | 55.9 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.39 | 9.21 | 16.31 | 6.00 | 72.9 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 6.37 | 16.32 | 25.96 | 12.00 | 112.2 | 81.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.24 | 10.29 | 16.71 | 8.00 | 61.4 | 86.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.0 | 1.75 | 8.09 | 14.86 | 0.00 | 18.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.55 | 16.20 | 27.14 | 2.00 | 84.0 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.21 | 14.86 | 23.76 | 1.00 | 85.4 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.08 | 14.60 | 23.85 | 6.00 | 89.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.51 | 13.81 | 22.36 | 3.00 | 74.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.48 | 13.14 | 21.66 | 2.00 | 76.1 | 73.0 |
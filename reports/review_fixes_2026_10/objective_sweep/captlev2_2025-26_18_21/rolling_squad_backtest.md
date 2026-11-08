# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 251.88
- Total actual points: 190.00
- Average predicted points: 62.97
- Average actual points: 47.50
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
- Predicted score: 65.02
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Dominic Calvert-Lewin replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.03 | 17.91 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.48 | 9.62 | 15.57 | 6.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.10 | 13.76 | 21.59 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.60 | 12.44 | 19.89 | 0.00 | 88.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.93 | 19.02 | 2.00 | 80.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 11.30 | 17.89 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.84 | 11.29 | 18.63 | 8.00 | 79.4 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.46 | 18.80 | 28.09 | 5.00 | 97.9 | 85.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.86 | 11.03 | 17.48 | 8.00 | 67.2 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.80 | 8.23 | 13.49 | 5.00 | 59.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.71 | 17.92 | 28.79 | 2.00 | 82.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.3 | 6.02 | 16.29 | 25.50 | 1.00 | 106.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.83 | 16.24 | 25.52 | 5.00 | 99.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.35 | 15.51 | 24.48 | 9.00 | 84.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.70 | 15.13 | 23.36 | 2.00 | 91.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 56.33
- Actual score: 30.00
- Transfer: Jurriën Timber -> Reece James (projected gain 0.94, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.59 | 17.26 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.06 | 9.33 | 15.30 | 10.00 | 83.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.11 | 11.95 | 19.66 | 6.00 | 83.3 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.37 | 11.91 | 18.76 | 1.00 | 86.3 | 45.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 11.70 | 19.10 | 1.00 | 88.2 | 33.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.73 | 11.10 | 17.38 | 3.00 | 84.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.49 | 13.46 | 20.89 | 2.00 | 55.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.03 | 9.80 | 16.47 | 1.00 | 53.7 | 20.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.23 | 9.69 | 15.57 | 2.00 | 69.5 | 61.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.24 | 16.71 | 27.94 | 3.00 | 80.7 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.39 | 16.04 | 24.31 | 2.00 | 89.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.95 | 15.04 | 24.20 | 5.00 | 82.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.87 | 12.95 | 21.03 | 1.00 | 73.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.16 | 12.91 | 21.00 | 0.00 | 69.2 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Phil Foden
- Effective captain: Morgan Rogers
- Chip used: triple_captain
- Predicted score: 62.08
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (7.24).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 4.36, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (7.24).
- Autosub: Matheus Santos Carneiro da Cunha replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.89 | 11.32 | 18.24 | 1.00 | 94.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.42 | 10.11 | 16.43 | 1.00 | 90.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.47 | 19.94 | 2.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.74 | 19.44 | 1.00 | 86.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.90 | 11.23 | 18.59 | 1.00 | 85.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.57 | 10.93 | 17.95 | 1.00 | 61.6 | 50.0 |
| Bench 4 | Bench | Reece James | DEF | 7 | 5.7 | 2.37 | 8.66 | 14.93 | 1.00 | 63.6 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.57 | 14.24 | 23.36 | 0.00 | 68.5 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.42 | 9.66 | 16.24 | 2.00 | 49.3 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.78 | 8.52 | 14.54 | 2.00 | 55.2 | 82.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.82 | 17.83 | 29.26 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 6.13 | 16.77 | 26.43 | 5.00 | 102.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.22 | 15.33 | 24.54 | 1.00 | 92.6 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.95 | 24.00 | 4.00 | 73.5 | 90.0 |
| Bench 2 | Autosub In | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.26 | 10.72 | 17.64 | 9.00 | 51.8 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Phil Foden
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 68.45
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.47 | 10.21 | 16.69 | 6.00 | 85.4 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.67 | 9.89 | 15.86 | 3.00 | 88.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.21 | 19.59 | 6.00 | 91.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.63 | 10.59 | 17.14 | 1.00 | 80.3 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.27 | 10.48 | 17.55 | 6.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 3.00 | 9.42 | 16.10 | 0.00 | 54.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.41 | 9.29 | 16.40 | 6.00 | 74.0 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 6.08 | 16.05 | 25.55 | 12.00 | 110.9 | 81.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.14 | 10.23 | 16.62 | 8.00 | 61.2 | 86.0 |
| Bench 3 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.12 | 9.02 | 15.27 | 2.00 | 60.9 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.46 | 16.10 | 26.92 | 2.00 | 82.0 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.13 | 14.82 | 23.66 | 1.00 | 84.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.11 | 14.53 | 23.72 | 6.00 | 91.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.83 | 13.81 | 22.23 | 3.00 | 75.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.64 | 13.21 | 21.71 | 2.00 | 76.9 | 73.0 |
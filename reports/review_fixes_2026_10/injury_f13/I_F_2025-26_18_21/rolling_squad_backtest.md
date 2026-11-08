# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 252.06
- Total actual points: 190.00
- Average predicted points: 63.02
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
- Predicted score: 65.22
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Dominic Calvert-Lewin replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.77 | 10.94 | 17.81 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.45 | 9.56 | 15.51 | 6.00 | 86.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.07 | 13.69 | 21.51 | 2.00 | 96.5 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.58 | 12.41 | 19.87 | 0.00 | 88.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.08 | 11.91 | 19.02 | 2.00 | 80.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 11.31 | 17.91 | 2.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.82 | 11.27 | 18.61 | 8.00 | 79.1 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 7.59 | 19.10 | 28.49 | 5.00 | 97.4 | 85.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.84 | 11.02 | 17.50 | 8.00 | 67.6 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.83 | 8.31 | 13.57 | 5.00 | 59.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.59 | 17.63 | 28.41 | 2.00 | 83.2 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.3 | 6.11 | 16.47 | 25.70 | 1.00 | 105.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.89 | 16.38 | 25.69 | 5.00 | 98.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.36 | 15.57 | 24.56 | 9.00 | 84.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.70 | 15.16 | 23.41 | 2.00 | 91.2 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Matheus Santos Carneiro da Cunha
- Vice captain: Phil Foden
- Effective captain: Matheus Santos Carneiro da Cunha
- Chip used: none
- Predicted score: 56.21
- Actual score: 30.00
- Transfer: Jurriën Timber -> Reece James (projected gain 0.89, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.51 | 17.16 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.04 | 9.29 | 15.25 | 10.00 | 84.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.59 | 12.64 | 20.21 | 2.00 | 92.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.09 | 11.88 | 19.59 | 6.00 | 83.5 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.34 | 11.85 | 18.70 | 1.00 | 86.7 | 45.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.06 | 11.67 | 19.06 | 1.00 | 87.8 | 33.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.73 | 11.09 | 17.38 | 3.00 | 84.8 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.39 | 13.25 | 20.63 | 2.00 | 56.3 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.02 | 9.80 | 16.50 | 1.00 | 54.1 | 20.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.26 | 9.77 | 15.66 | 2.00 | 68.9 | 61.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.11 | 16.41 | 27.54 | 3.00 | 81.5 | 90.0 |
| Captain | Captain | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.41 | 16.12 | 24.43 | 2.00 | 89.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.96 | 15.09 | 24.27 | 5.00 | 81.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.98 | 13.17 | 21.29 | 1.00 | 73.4 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.23 | 13.09 | 21.21 | 0.00 | 68.3 | 0.0 |

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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.22) beats the best remaining Triple Captain opportunity (7.34).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 4.37, hit 0)
- Chip used: Triple Captain on Morgan Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (6.22) beats the best remaining Triple Captain opportunity (7.34).
- Autosub: Matheus Santos Carneiro da Cunha replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.25 | 18.15 | 1.00 | 94.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.40 | 10.06 | 16.37 | 1.00 | 90.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.38 | 12.46 | 19.95 | 2.00 | 94.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.98 | 11.68 | 19.37 | 1.00 | 87.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.90 | 11.24 | 18.60 | 1.00 | 85.1 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.55 | 10.91 | 17.93 | 1.00 | 61.3 | 50.0 |
| Bench 4 | Bench | Reece James | DEF | 7 | 5.7 | 2.35 | 8.62 | 14.89 | 1.00 | 64.0 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.47 | 14.01 | 23.07 | 0.00 | 69.2 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.39 | 9.62 | 16.23 | 2.00 | 49.7 | 90.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.81 | 8.58 | 14.61 | 2.00 | 54.5 | 82.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.71 | 17.56 | 28.90 | 2.00 | 87.4 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 6.22 | 16.95 | 26.66 | 5.00 | 102.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.23 | 15.37 | 24.60 | 1.00 | 92.1 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.94 | 15.06 | 24.15 | 4.00 | 73.5 | 90.0 |
| Bench 2 | Autosub In | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.30 | 10.84 | 17.81 | 9.00 | 51.1 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Phil Foden
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: bench_boost
- Predicted score: 68.56
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.44 | 10.15 | 16.62 | 6.00 | 85.8 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.65 | 9.83 | 15.80 | 3.00 | 88.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.20 | 19.59 | 6.00 | 90.7 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.61 | 10.55 | 17.09 | 1.00 | 80.6 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.26 | 10.44 | 17.51 | 6.00 | 84.2 | 90.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 2.97 | 9.40 | 16.08 | 0.00 | 54.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.41 | 9.29 | 16.42 | 6.00 | 74.1 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 6.15 | 16.20 | 25.72 | 12.00 | 110.7 | 81.0 |
| Bench 3 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.12 | 10.21 | 16.63 | 8.00 | 61.6 | 86.0 |
| Bench 2 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.15 | 9.07 | 15.34 | 2.00 | 60.3 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.35 | 15.85 | 26.59 | 2.00 | 82.7 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.18 | 14.91 | 23.76 | 1.00 | 84.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.12 | 14.56 | 23.77 | 6.00 | 90.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.93 | 14.02 | 22.49 | 3.00 | 75.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.68 | 13.30 | 21.84 | 2.00 | 76.2 | 73.0 |
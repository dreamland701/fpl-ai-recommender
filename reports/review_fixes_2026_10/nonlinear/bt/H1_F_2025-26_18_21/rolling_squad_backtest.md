# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 231.00
- Total actual points: 171.00
- Average predicted points: 57.75
- Average actual points: 42.75
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
- Captain: Phil Foden
- Vice captain: Hugo Ekitiké
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 58.71
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.88 | 11.03 | 17.91 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.86 | 9.62 | 15.57 | 6.00 | 88.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.33 | 13.76 | 21.59 | 2.00 | 85.4 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.76 | 12.44 | 19.89 | 0.00 | 83.4 | 0.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.3 | 3.17 | 11.93 | 19.02 | 2.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.87 | 11.30 | 17.89 | 2.00 | 81.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.34 | 11.29 | 18.63 | 8.00 | 82.3 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 5.59 | 18.80 | 28.09 | 5.00 | 81.5 | 85.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 4.46 | 11.03 | 17.48 | 8.00 | 75.3 | 84.0 |
| Bench 4 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.87 | 8.23 | 13.49 | 5.00 | 62.2 | 90.0 |
| Captain | Captain | Phil Foden | MID | 13 | 9.0 | 5.63 | 17.92 | 28.79 | 2.00 | 84.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 4.82 | 16.29 | 25.50 | 1.00 | 84.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.84 | 16.24 | 25.52 | 5.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.33 | 15.51 | 24.48 | 9.00 | 88.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.10 | 15.13 | 23.36 | 2.00 | 81.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Hugo Ekitiké
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Hugo Ekitiké
- Chip used: none
- Predicted score: 52.30
- Actual score: 30.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Jurriën Timber -> Reece James (projected gain 0.88, hit 0)
- Autosub: Marcos Senesi Barón replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.61 | 10.59 | 17.26 | 2.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.51 | 9.33 | 15.30 | 10.00 | 87.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.37 | 12.66 | 20.21 | 2.00 | 85.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 11.95 | 19.66 | 6.00 | 85.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.39 | 11.91 | 18.76 | 1.00 | 83.1 | 45.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.07 | 11.70 | 19.10 | 1.00 | 84.2 | 33.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.33 | 11.10 | 17.38 | 3.00 | 73.0 | 90.0 |
| Captain | Captain | Hugo Ekitiké | FWD | 12 | 9.0 | 5.69 | 13.46 | 20.89 | 2.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 2.72 | 9.80 | 16.47 | 1.00 | 73.9 | 20.0 |
| Bench 3 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.29 | 9.69 | 15.57 | 2.00 | 79.4 | 61.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 3.76 | 16.71 | 27.94 | 3.00 | 82.3 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.67 | 16.04 | 24.31 | 2.00 | 82.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.05 | 15.04 | 24.20 | 5.00 | 83.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.55 | 12.95 | 21.03 | 1.00 | 81.1 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.29 | 12.91 | 21.00 | 0.00 | 81.5 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.80 -> 1.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Morgan Rogers
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 56.66
- Actual score: 26.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.33) beats the best remaining Triple Captain opportunity (6.54).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 6.52, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (5.33) beats the best remaining Triple Captain opportunity (6.54).
- Autosub: Igor Jesus Maciel da Cruz replaced Hugo Ekitiké.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.04 | 11.32 | 18.24 | 1.00 | 87.9 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.75 | 10.11 | 16.43 | 1.00 | 89.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.58 | 12.47 | 19.94 | 2.00 | 85.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.77 | 11.74 | 19.44 | 1.00 | 84.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.55 | 11.23 | 18.59 | 1.00 | 88.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.15 | 10.93 | 17.95 | 1.00 | 64.9 | 50.0 |
| Bench 4 | Bench | Reece James | DEF | 7 | 5.7 | 2.08 | 8.66 | 14.93 | 1.00 | 57.8 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 4.41 | 14.24 | 23.36 | 0.00 | 76.2 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.42 | 9.66 | 16.24 | 2.00 | 68.7 | 90.0 |
| Bench 2 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 2.66 | 8.52 | 14.54 | 2.00 | 53.4 | 82.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.9 | 5.33 | 17.83 | 29.26 | 2.00 | 83.7 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.15 | 16.77 | 26.43 | 5.00 | 80.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.34 | 15.33 | 24.54 | 1.00 | 82.7 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.57 | 14.95 | 24.00 | 4.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 2.60 | 10.72 | 17.64 | 9.00 | 74.8 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Morgan Rogers
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Morgan Rogers
- Chip used: bench_boost
- Predicted score: 63.33
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.17, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.24 | 10.21 | 16.69 | 6.00 | 81.7 | 90.0 |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 4.38 | 9.89 | 15.86 | 3.00 | 86.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.34 | 12.21 | 19.59 | 6.00 | 89.7 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.62 | 10.59 | 17.14 | 1.00 | 81.0 | 25.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 12 | 5.9 | 2.36 | 10.48 | 17.55 | 6.00 | 80.3 | 90.0 |
| Bench 4 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 1.09 | 9.42 | 16.10 | 0.00 | 21.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.77 | 9.29 | 16.40 | 6.00 | 83.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 4.31 | 16.05 | 25.55 | 12.00 | 83.1 | 81.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.41 | 10.23 | 16.62 | 8.00 | 78.6 | 86.0 |
| Bench 2 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.8 | 3.38 | 9.02 | 15.27 | 2.00 | 70.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 4.79 | 16.10 | 26.92 | 2.00 | 82.4 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.78 | 14.82 | 23.66 | 1.00 | 81.0 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.72 | 14.53 | 23.72 | 6.00 | 87.8 | 90.0 |
| Captain | Captain | Morgan Rogers | MID | 2 | 7.4 | 5.52 | 13.81 | 22.23 | 3.00 | 84.2 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 5.11 | 13.21 | 21.71 | 2.00 | 84.2 | 73.0 |
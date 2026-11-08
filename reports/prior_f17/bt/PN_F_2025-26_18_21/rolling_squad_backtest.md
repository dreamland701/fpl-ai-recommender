# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 259.45
- Total actual points: 186.00
- Average predicted points: 64.86
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Hugo Ekitiké
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 67.74
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.02 | 8.88 | 14.89 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.10 | 0.26 | 0.41 | 0.00 | 4.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.02 | 13.69 | 21.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.15 | 11.86 | 18.97 | 2.00 | 81.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.97 | 11.42 | 18.07 | 2.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.51 | 11.97 | 2.00 | 67.3 | 90.0 |
| Bench 3 | Bench | Ayden Heaven | DEF | 14 | 3.8 | 2.21 | 5.87 | 8.67 | 8.00 | 60.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.40 | 24.75 | 41.01 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.84 | 18.31 | 27.34 | 5.00 | 85.8 | 85.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.20 | 0.53 | 0.79 | 0.00 | 0.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.69 | 17.92 | 28.81 | 2.00 | 82.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.41 | 25.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.66 | 16.30 | 25.52 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.59 | 24.65 | 9.00 | 83.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.53 | 15.31 | 23.64 | 2.00 | 89.4 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.46
- Actual score: 37.00
- Transfer: Marcos Senesi Barón -> Michael Keane (projected gain 0.19, hit 0)
- Autosub: Ayden Heaven replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.50 | 9.84 | 15.93 | 2.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.13 | 0.34 | 0.59 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.51 | 12.47 | 19.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.13 | 11.94 | 19.70 | 6.00 | 83.0 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.8 | 3.96 | 11.41 | 17.81 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Ayden Heaven | DEF | 14 | 3.8 | 3.06 | 7.51 | 11.33 | 2.00 | 69.8 | 74.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.40 | 7.47 | 12.12 | 8.00 | 68.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.01 | 23.80 | 39.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.38 | 13.34 | 20.68 | 2.00 | 53.4 | 90.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.49 | 0.76 | 1.09 | 0.00 | 1.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.78 | 28.08 | 3.00 | 83.4 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.11 | 16.15 | 24.47 | 2.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.14 | 15.16 | 24.42 | 5.00 | 85.4 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.42 | 13.27 | 21.55 | 0.00 | 73.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 13.20 | 21.39 | 1.00 | 75.3 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.45
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.69) beats the best remaining Bench Boost opportunity (6.24).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.69) beats the best remaining Bench Boost opportunity (6.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.46 | 8.58 | 14.42 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Remi Matthews | GK | 8 | 3.9 | 0.09 | 0.40 | 0.61 | 0.00 | 7.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.38 | 12.29 | 19.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.73 | 19.46 | 1.00 | 86.3 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.79 | 7.78 | 12.04 | 2.00 | 76.8 | 90.0 |
| Bench 2 | Bench Boost | Ayden Heaven | DEF | 14 | 3.8 | 2.42 | 6.84 | 11.20 | 4.00 | 64.1 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.8 | 1.98 | 6.25 | 10.85 | 0.00 | 42.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.19 | 24.21 | 40.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.49 | 13.96 | 22.95 | 0.00 | 65.4 | 0.0 |
| Bench 4 | Bench Boost | Chido Obi | FWD | 14 | 4.2 | 0.20 | 0.56 | 0.97 | 0.00 | 4.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.83 | 17.75 | 29.16 | 2.00 | 86.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.56 | 26.13 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.40 | 24.67 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.55 | 11.28 | 18.53 | 9.00 | 58.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 2.81 | 9.14 | 16.34 | 17.00 | 39.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.79
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.03) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.51, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.03) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.68 | 5.81 | 10.34 | 2.00 | 52.9 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.09 | 0.29 | 0.52 | 0.00 | 7.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.43 | 12.12 | 19.48 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.34 | 10.50 | 17.63 | 6.00 | 84.3 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.8 | 3.29 | 8.69 | 14.07 | 5.00 | 70.2 | 82.0 |
| Bench 2 | Bench | Ayden Heaven | DEF | 14 | 3.8 | 3.14 | 8.41 | 13.53 | 0.00 | 72.0 | 60.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.47 | 7.26 | 11.60 | 0.00 | 73.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.03 | 23.84 | 38.99 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.67 | 15.82 | 25.24 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.32 | 0.69 | 1.17 | 0.00 | 4.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.49 | 16.05 | 26.89 | 2.00 | 81.8 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.11 | 14.83 | 24.60 | 3.00 | 88.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.18 | 14.58 | 23.81 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.83 | 22.29 | 3.00 | 76.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.75 | 13.52 | 22.22 | 2.00 | 79.6 | 73.0 |
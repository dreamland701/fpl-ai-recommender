# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 257.73
- Total actual points: 185.00
- Average predicted points: 64.43
- Average actual points: 46.25
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
- Predicted score: 67.59
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.97 | 8.77 | 14.71 | 3.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.04 | 0.17 | 0.31 | 0.00 | 2.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.00 | 13.59 | 21.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.12 | 11.85 | 18.94 | 2.00 | 80.7 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.14 | 11.28 | 17.47 | 10.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.66 | 7.99 | 12.15 | 2.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.63 | 11.93 | 2.00 | 69.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.36 | 24.52 | 40.73 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.86 | 18.37 | 27.65 | 5.00 | 86.3 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.70 | 1.98 | 3.17 | 0.00 | 13.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.62 | 17.68 | 28.56 | 2.00 | 82.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.64 | 16.28 | 25.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.71 | 16.26 | 25.55 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.29 | 15.53 | 24.61 | 9.00 | 82.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.52 | 15.20 | 23.52 | 2.00 | 88.9 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.60
- Actual score: 42.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Jaka Bijol replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.44 | 9.63 | 15.70 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.42 | 19.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.20 | 12.13 | 19.87 | 6.00 | 81.9 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.7 | 3.95 | 11.34 | 17.83 | 0.00 | 89.5 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.47 | 7.46 | 12.18 | 7.00 | 69.3 | 90.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.38 | 7.30 | 11.92 | 8.00 | 70.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.92 | 39.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.50 | 13.71 | 21.18 | 2.00 | 53.8 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.43 | 1.48 | 2.55 | 0.00 | 6.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.42 | 16.90 | 28.05 | 3.00 | 83.3 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.05 | 15.95 | 24.27 | 2.00 | 85.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.14 | 15.17 | 24.42 | 5.00 | 83.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 13.22 | 21.41 | 1.00 | 74.6 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.38 | 13.16 | 21.35 | 0.00 | 73.5 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.77
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.97) beats the best remaining Bench Boost opportunity (6.33).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.97) beats the best remaining Bench Boost opportunity (6.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.44 | 8.54 | 14.30 | 0.00 | 89.4 | 0.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 3.9 | 0.09 | 0.19 | 0.32 | 0.00 | 3.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.22 | 19.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.73 | 19.51 | 1.00 | 85.5 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.86 | 7.82 | 12.81 | 4.00 | 74.9 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.74 | 7.71 | 11.87 | 2.00 | 79.1 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.7 | 1.97 | 6.21 | 10.83 | 0.00 | 42.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.19 | 24.13 | 39.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.54 | 14.13 | 23.29 | 0.00 | 66.3 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.37 | 2.45 | 0.00 | 7.9 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.81 | 17.71 | 29.10 | 2.00 | 86.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.75 | 16.45 | 26.05 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.45 | 24.70 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.59 | 11.36 | 18.50 | 9.00 | 57.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 2.76 | 8.95 | 16.07 | 17.00 | 38.8 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.77
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Michael Keane -> Micky van de Ven (projected gain 2.73, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.62 | 5.65 | 10.13 | 2.00 | 51.8 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.21 | 0.42 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.10 | 19.43 | 6.00 | 89.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.12 | 11.23 | 17.23 | 0.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.37 | 10.61 | 17.76 | 6.00 | 83.4 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.01 | 8.17 | 13.59 | 3.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.44 | 7.14 | 11.42 | 0.00 | 75.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.72 | 38.77 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 2.24 | 8.84 | 16.00 | 0.00 | 26.0 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.31 | 1.08 | 2.01 | 0.00 | 8.6 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.47 | 15.98 | 26.80 | 2.00 | 82.2 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.10 | 14.64 | 24.43 | 3.00 | 88.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.18 | 14.61 | 23.84 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.72 | 13.80 | 22.22 | 3.00 | 75.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.78 | 13.57 | 22.17 | 2.00 | 79.3 | 73.0 |
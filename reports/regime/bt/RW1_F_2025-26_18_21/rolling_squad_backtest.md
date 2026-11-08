# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 254.05
- Total actual points: 207.00
- Average predicted points: 63.51
- Average actual points: 51.75
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
- Predicted score: 66.92
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.43 | 9.65 | 15.72 | 6.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.02 | 0.00 | 0.02 | 0.00 | 2.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.94 | 13.34 | 20.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.16 | 11.52 | 18.02 | 10.00 | 86.6 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.97 | 11.13 | 17.69 | 0.00 | 81.8 | 0.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.57 | 7.79 | 12.41 | 2.00 | 68.4 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.69 | 7.65 | 12.33 | 2.00 | 71.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.92 | 23.75 | 38.87 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.93 | 17.16 | 26.19 | 5.00 | 88.2 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.66 | 1.94 | 3.02 | 0.00 | 13.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.55 | 16.69 | 27.35 | 2.00 | 84.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.72 | 16.30 | 25.29 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.79 | 15.89 | 24.81 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.51 | 14.80 | 23.14 | 2.00 | 85.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.08 | 14.49 | 22.46 | 9.00 | 83.4 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.50
- Actual score: 50.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.83, hit 0)
- Autosub: Gabriel Gudmundsson replaced Michael Keane.
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.02 | 9.44 | 15.60 | 10.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.5 | 0.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.7 | 3.91 | 11.64 | 18.27 | 0.00 | 88.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.95 | 11.44 | 18.77 | 6.00 | 82.7 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.43 | 11.30 | 17.16 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.52 | 12.22 | 8.00 | 72.9 | 90.0 |
| Bench 3 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.52 | 7.46 | 12.38 | 7.00 | 70.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.77 | 22.86 | 37.23 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.35 | 12.35 | 19.23 | 2.00 | 58.3 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.35 | 1.46 | 2.51 | 0.00 | 7.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.24 | 16.26 | 27.22 | 3.00 | 85.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.18 | 15.46 | 23.47 | 2.00 | 83.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.68 | 14.00 | 22.05 | 5.00 | 82.5 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.24 | 12.80 | 20.74 | 0.00 | 74.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.94 | 12.39 | 20.50 | 1.00 | 75.4 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.58
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.46) beats the best remaining Bench Boost opportunity (5.79).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.46) beats the best remaining Bench Boost opportunity (5.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.28 | 10.02 | 16.34 | 1.00 | 89.4 | 90.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 3.9 | 0.06 | 0.16 | 0.20 | 0.00 | 3.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.89 | 11.30 | 18.74 | 1.00 | 86.3 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.97 | 8.16 | 13.42 | 4.00 | 75.9 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.83 | 8.11 | 12.30 | 2.00 | 79.8 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.77 | 8.06 | 13.72 | 2.00 | 69.5 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.7 | 1.78 | 5.70 | 10.25 | 0.00 | 37.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.95 | 23.56 | 38.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.49 | 13.52 | 22.51 | 0.00 | 69.7 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.14 | 1.35 | 2.55 | 0.00 | 8.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.67 | 17.46 | 29.13 | 2.00 | 89.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.80 | 16.20 | 25.92 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.00 | 14.33 | 22.40 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.51 | 10.48 | 17.35 | 9.00 | 57.7 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.48 | 8.57 | 15.38 | 17.00 | 35.7 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.05
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.74, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.62 | 9.72 | 15.48 | 3.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.08 | 0.24 | 0.00 | 3.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.24 | 10.13 | 17.04 | 6.00 | 84.5 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.57 | 9.52 | 15.69 | 1.00 | 79.5 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 3.33 | 8.64 | 13.80 | 5.00 | 69.7 | 82.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.13 | 8.51 | 14.31 | 3.00 | 79.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.61 | 7.55 | 11.86 | 0.00 | 76.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.70 | 23.25 | 37.49 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.50 | 15.14 | 24.14 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.30 | 1.19 | 2.04 | 0.00 | 9.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.28 | 15.85 | 27.12 | 2.00 | 83.7 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.05 | 14.55 | 23.68 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.92 | 13.63 | 21.92 | 6.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.72 | 13.38 | 21.48 | 2.00 | 78.8 | 73.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.73 | 13.07 | 20.74 | 3.00 | 78.7 | 90.0 |
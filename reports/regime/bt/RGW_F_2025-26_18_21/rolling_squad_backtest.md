# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 255.75
- Total actual points: 207.00
- Average predicted points: 63.94
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
- Predicted score: 67.14
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.44 | 9.63 | 15.60 | 6.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.20 | 0.40 | 0.62 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.99 | 13.55 | 21.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.15 | 11.50 | 17.96 | 10.00 | 87.7 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 4.01 | 11.20 | 17.93 | 0.00 | 82.1 | 0.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.70 | 8.14 | 12.80 | 2.00 | 70.2 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.73 | 7.98 | 12.80 | 2.00 | 70.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 24.01 | 39.51 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.90 | 17.77 | 26.93 | 5.00 | 87.9 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.52 | 1.43 | 2.23 | 0.00 | 12.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.55 | 17.05 | 27.66 | 2.00 | 83.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.65 | 16.09 | 25.10 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.69 | 15.98 | 25.00 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.58 | 15.21 | 23.66 | 2.00 | 87.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.08 | 14.65 | 22.91 | 9.00 | 81.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.98
- Actual score: 50.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.92, hit 0)
- Autosub: Jaka Bijol replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.09 | 9.44 | 15.48 | 10.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.16 | 0.46 | 0.74 | 0.00 | 4.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.03 | 11.72 | 19.27 | 6.00 | 83.6 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.58 | 11.71 | 17.95 | 2.00 | 86.6 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.7 | 3.98 | 11.69 | 18.33 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.60 | 7.84 | 12.89 | 7.00 | 70.8 | 90.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.57 | 7.83 | 12.73 | 8.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.76 | 23.05 | 38.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.40 | 12.93 | 20.11 | 2.00 | 57.1 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.24 | 0.98 | 1.68 | 0.00 | 6.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.21 | 16.22 | 27.19 | 3.00 | 84.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.21 | 15.96 | 24.24 | 2.00 | 84.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.80 | 14.20 | 22.60 | 5.00 | 83.1 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.26 | 12.81 | 20.74 | 0.00 | 72.7 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.90 | 12.67 | 20.69 | 1.00 | 75.9 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 61.33
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.73) beats the best remaining Bench Boost opportunity (6.22).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.73) beats the best remaining Bench Boost opportunity (6.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.33 | 10.04 | 16.31 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.27 | 0.61 | 0.87 | 0.00 | 5.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.96 | 11.61 | 19.23 | 1.00 | 87.2 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.87 | 8.48 | 14.29 | 2.00 | 69.5 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.95 | 8.39 | 12.89 | 2.00 | 80.1 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.04 | 8.37 | 13.78 | 4.00 | 76.1 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.7 | 1.92 | 6.10 | 10.74 | 0.00 | 41.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.94 | 23.61 | 38.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.53 | 13.86 | 22.83 | 0.00 | 68.7 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.00 | 0.78 | 1.53 | 0.00 | 7.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.67 | 17.38 | 28.78 | 2.00 | 87.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.78 | 16.28 | 25.82 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.03 | 14.51 | 22.96 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.56 | 10.97 | 18.09 | 9.00 | 57.6 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.54 | 8.50 | 15.23 | 17.00 | 36.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.30
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.79) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.63 | 9.81 | 15.60 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.50 | 0.82 | 1.12 | 0.00 | 4.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.32 | 10.46 | 17.54 | 6.00 | 85.5 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.62 | 9.76 | 15.98 | 1.00 | 80.1 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 3.34 | 8.80 | 14.12 | 5.00 | 70.7 | 82.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.16 | 8.68 | 14.54 | 3.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.64 | 7.79 | 12.38 | 0.00 | 76.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.79 | 23.39 | 37.95 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.40 | 14.81 | 23.58 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.13 | 0.53 | 0.96 | 0.00 | 8.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.31 | 15.76 | 26.69 | 2.00 | 82.1 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.96 | 14.19 | 23.27 | 3.00 | 88.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 4.91 | 13.65 | 22.12 | 6.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.74 | 13.46 | 21.87 | 2.00 | 78.6 | 73.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.70 | 13.20 | 21.16 | 3.00 | 77.1 | 90.0 |
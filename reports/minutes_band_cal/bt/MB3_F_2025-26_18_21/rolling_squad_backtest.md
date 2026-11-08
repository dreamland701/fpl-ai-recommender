# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 262.10
- Total actual points: 183.00
- Average predicted points: 65.53
- Average actual points: 45.75
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
- Predicted score: 67.72
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.01 | 8.83 | 14.81 | 3.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.09 | 0.17 | 0.37 | 0.00 | 2.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.67 | 21.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.13 | 11.81 | 18.88 | 2.00 | 80.6 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.99 | 10.98 | 17.59 | 0.00 | 81.8 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.76 | 8.25 | 12.88 | 2.00 | 72.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.65 | 7.89 | 12.63 | 2.00 | 72.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.42 | 24.77 | 41.01 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.87 | 18.43 | 27.56 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.66 | 1.89 | 3.09 | 0.00 | 12.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.68 | 17.91 | 28.81 | 2.00 | 82.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.75 | 16.38 | 25.72 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.65 | 16.28 | 25.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.48 | 24.46 | 9.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.51 | 15.24 | 23.52 | 2.00 | 88.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.10
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.26, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.49 | 9.78 | 15.84 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.05 | 0.26 | 0.51 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.43 | 19.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.12 | 11.92 | 19.65 | 6.00 | 82.8 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.39 | 11.22 | 17.19 | 2.00 | 85.0 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 8.02 | 13.07 | 7.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.54 | 7.86 | 12.80 | 8.00 | 74.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.04 | 23.83 | 39.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.55 | 13.84 | 21.49 | 2.00 | 57.9 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.39 | 1.45 | 2.48 | 0.00 | 5.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.79 | 28.10 | 3.00 | 83.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.09 | 16.07 | 24.34 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.11 | 15.04 | 24.20 | 5.00 | 84.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.45 | 13.25 | 21.45 | 0.00 | 75.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.93 | 13.19 | 21.33 | 1.00 | 76.4 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.07
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.78) beats the best remaining Bench Boost opportunity (7.10).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.78) beats the best remaining Bench Boost opportunity (7.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.45 | 8.51 | 14.31 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.16 | 0.40 | 0.65 | 0.00 | 5.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.24 | 19.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.71 | 19.42 | 1.00 | 86.1 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.78 | 8.27 | 13.84 | 2.00 | 70.5 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.00 | 8.07 | 13.22 | 4.00 | 75.9 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.88 | 7.96 | 12.30 | 2.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.22 | 24.24 | 40.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.63 | 14.33 | 23.58 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.10 | 1.20 | 2.27 | 0.00 | 7.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.84 | 17.80 | 29.25 | 2.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.54 | 26.09 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.30 | 24.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.65 | 11.56 | 18.93 | 9.00 | 60.8 | 90.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.73 | 8.97 | 16.12 | 17.00 | 37.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.21
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.40, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.80 | 6.10 | 10.76 | 2.00 | 55.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.37 | 0.51 | 0.77 | 0.00 | 3.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.06 | 19.36 | 6.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.49 | 17.60 | 6.00 | 84.2 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.52 | 9.28 | 15.06 | 1.00 | 79.9 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.12 | 8.47 | 14.02 | 3.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.44 | 11.86 | 0.00 | 76.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 23.85 | 38.96 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.66 | 15.78 | 25.17 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.26 | 1.00 | 1.90 | 0.00 | 7.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.50 | 16.09 | 26.95 | 2.00 | 82.2 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.11 | 14.82 | 24.61 | 3.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.50 | 23.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.78 | 13.81 | 22.20 | 3.00 | 77.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.78 | 13.47 | 22.07 | 2.00 | 80.6 | 73.0 |
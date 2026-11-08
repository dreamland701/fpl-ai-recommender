# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 263.76
- Total actual points: 168.00
- Average predicted points: 65.94
- Average actual points: 42.00
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
- Predicted score: 67.75
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.92 | 8.74 | 14.72 | 3.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.09 | 0.15 | 0.25 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.67 | 21.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.15 | 11.82 | 18.89 | 2.00 | 80.6 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 4.00 | 10.99 | 17.61 | 0.00 | 81.8 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.58 | 7.94 | 12.42 | 2.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.63 | 12.22 | 2.00 | 68.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.42 | 24.77 | 41.01 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.87 | 18.43 | 27.56 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.57 | 1.87 | 3.09 | 0.00 | 13.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.74 | 17.97 | 28.87 | 2.00 | 82.3 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.75 | 16.38 | 25.72 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.65 | 16.28 | 25.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.31 | 15.51 | 24.49 | 9.00 | 82.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.51 | 15.24 | 23.52 | 2.00 | 88.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.18
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.49, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.49 | 9.78 | 15.84 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.11 | 0.25 | 0.39 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.43 | 19.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.14 | 11.93 | 19.67 | 6.00 | 82.8 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.39 | 11.22 | 17.19 | 2.00 | 85.0 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.53 | 7.79 | 12.68 | 7.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.42 | 7.61 | 12.40 | 8.00 | 70.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.04 | 23.83 | 39.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.43 | 13.48 | 20.93 | 2.00 | 54.6 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.45 | 1.58 | 2.62 | 0.00 | 7.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.44 | 16.84 | 28.15 | 3.00 | 83.5 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.12 | 16.10 | 24.36 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.06 | 14.99 | 24.15 | 5.00 | 84.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.55 | 13.37 | 21.62 | 0.00 | 73.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.98 | 13.28 | 21.47 | 1.00 | 74.8 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.13
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (6.95).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (6.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.45 | 8.51 | 14.31 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.18 | 0.32 | 0.00 | 5.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.24 | 19.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.71 | 19.42 | 1.00 | 86.1 | 90.0 |
| Bench 3 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.72 | 8.07 | 13.48 | 2.00 | 67.1 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.93 | 8.03 | 13.24 | 4.00 | 74.3 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.80 | 7.92 | 12.31 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.22 | 24.24 | 40.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.80 | 14.37 | 23.45 | 0.00 | 67.1 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.33 | 2.42 | 0.00 | 8.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.84 | 17.80 | 29.25 | 2.00 | 86.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.54 | 26.09 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.30 | 24.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.00 | 15.06 | 24.12 | 4.00 | 73.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.59 | 11.26 | 18.44 | 9.00 | 57.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.70
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.42, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.21 | 5.22 | 9.66 | 2.00 | 52.2 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.12 | 0.25 | 0.48 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.06 | 19.36 | 6.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.32 | 10.48 | 17.59 | 6.00 | 84.2 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.48 | 9.27 | 15.10 | 1.00 | 78.3 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.08 | 8.45 | 14.05 | 3.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.51 | 7.42 | 11.89 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 23.85 | 38.96 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.66 | 15.78 | 25.17 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.33 | 1.13 | 2.05 | 0.00 | 8.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.56 | 16.14 | 27.00 | 2.00 | 82.2 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.06 | 14.73 | 23.51 | 1.00 | 82.2 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.50 | 23.66 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.87 | 13.92 | 22.35 | 3.00 | 75.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.80 | 13.52 | 22.17 | 2.00 | 79.1 | 73.0 |
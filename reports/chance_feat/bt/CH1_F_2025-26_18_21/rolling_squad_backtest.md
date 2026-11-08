# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 260.99
- Total actual points: 183.00
- Average predicted points: 65.25
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
- Predicted score: 67.70
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.00 | 8.78 | 14.71 | 3.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.10 | 0.19 | 0.36 | 0.00 | 3.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.01 | 13.67 | 21.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.13 | 11.77 | 18.81 | 2.00 | 80.5 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.99 | 10.95 | 17.53 | 0.00 | 81.8 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.67 | 8.04 | 12.50 | 2.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.65 | 12.21 | 2.00 | 68.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.41 | 24.71 | 40.88 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.87 | 18.44 | 27.59 | 5.00 | 87.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.72 | 2.00 | 3.21 | 0.00 | 13.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.67 | 17.85 | 28.69 | 2.00 | 82.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.40 | 25.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.65 | 16.32 | 25.56 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.44 | 24.37 | 9.00 | 82.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.52 | 15.30 | 23.64 | 2.00 | 88.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.81
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.50, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.48 | 9.74 | 15.77 | 2.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.11 | 0.29 | 0.48 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.42 | 19.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.12 | 11.86 | 19.52 | 6.00 | 82.6 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.40 | 11.24 | 17.25 | 2.00 | 85.0 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.54 | 7.80 | 12.69 | 7.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.45 | 7.61 | 12.36 | 8.00 | 70.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.03 | 23.76 | 39.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.39 | 13.33 | 20.66 | 2.00 | 54.2 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.45 | 1.57 | 2.60 | 0.00 | 6.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.38 | 16.71 | 27.95 | 3.00 | 83.3 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.10 | 16.14 | 24.47 | 2.00 | 85.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.10 | 14.98 | 24.07 | 5.00 | 84.1 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.40 | 13.16 | 21.33 | 0.00 | 73.3 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.88 | 13.12 | 21.27 | 1.00 | 74.7 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.58
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.64) beats the best remaining Bench Boost opportunity (6.95).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.64) beats the best remaining Bench Boost opportunity (6.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.44 | 8.47 | 14.22 | 0.00 | 89.8 | 0.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.22 | 0.41 | 0.00 | 5.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.22 | 19.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.66 | 19.32 | 1.00 | 86.0 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.95 | 8.06 | 13.27 | 4.00 | 74.3 | 90.0 |
| Bench 3 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.69 | 8.01 | 13.37 | 2.00 | 67.0 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.83 | 7.92 | 12.28 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.21 | 24.19 | 40.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.53 | 14.04 | 23.05 | 0.00 | 66.9 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.33 | 2.42 | 0.00 | 8.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.83 | 17.75 | 29.15 | 2.00 | 86.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.59 | 26.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.29 | 24.46 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.51 | 11.14 | 18.26 | 9.00 | 57.4 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.79 | 9.00 | 16.05 | 17.00 | 38.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.92
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.41, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.65 | 5.64 | 10.03 | 2.00 | 52.0 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.13 | 0.29 | 0.56 | 0.00 | 5.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.02 | 19.29 | 6.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.46 | 17.53 | 6.00 | 84.1 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.48 | 9.25 | 15.08 | 1.00 | 78.3 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.08 | 8.46 | 14.05 | 3.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.51 | 7.41 | 11.85 | 0.00 | 75.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 23.81 | 38.87 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.66 | 15.78 | 25.18 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.33 | 1.14 | 2.06 | 0.00 | 8.7 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.50 | 16.04 | 26.86 | 2.00 | 82.1 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.12 | 14.87 | 24.69 | 3.00 | 88.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.16 | 14.48 | 23.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.74 | 13.75 | 22.15 | 3.00 | 75.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.74 | 13.45 | 22.09 | 2.00 | 79.1 | 73.0 |
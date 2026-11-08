# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 261.57
- Total actual points: 183.00
- Average predicted points: 65.39
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
- Predicted score: 68.39
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.00 | 8.83 | 14.89 | 3.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.06 | 0.12 | 0.32 | 0.00 | 4.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.93 | 13.51 | 21.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.78 | 18.89 | 2.00 | 79.3 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.92 | 10.88 | 17.53 | 0.00 | 79.8 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 7.94 | 12.44 | 2.00 | 67.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.51 | 7.57 | 12.19 | 2.00 | 67.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.60 | 24.97 | 41.77 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.89 | 18.28 | 27.83 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.79 | 2.13 | 3.44 | 0.00 | 15.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.85 | 18.11 | 29.58 | 2.00 | 89.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.94 | 16.52 | 25.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.86 | 16.44 | 26.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.49 | 15.94 | 25.09 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.22 | 15.37 | 24.33 | 9.00 | 80.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.37
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.33, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.46 | 9.74 | 15.85 | 2.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.13 | 0.29 | 0.50 | 0.00 | 5.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.45 | 12.32 | 19.80 | 2.00 | 88.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.10 | 11.89 | 19.65 | 6.00 | 81.7 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.30 | 11.01 | 16.99 | 2.00 | 82.6 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.50 | 7.73 | 12.67 | 7.00 | 68.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.42 | 7.58 | 12.41 | 8.00 | 69.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.77 | 39.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.40 | 13.47 | 20.92 | 2.00 | 53.7 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.54 | 1.73 | 2.85 | 0.00 | 9.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.83 | 28.19 | 3.00 | 82.6 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.92 | 15.72 | 23.89 | 2.00 | 81.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.08 | 15.01 | 24.19 | 5.00 | 83.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.42 | 13.26 | 21.56 | 0.00 | 72.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.86 | 13.11 | 21.31 | 1.00 | 73.4 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.77
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.99) beats the best remaining Bench Boost opportunity (7.32).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.99) beats the best remaining Bench Boost opportunity (7.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.50 | 8.63 | 14.41 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Krisztián Hegyi | GK | 19 | 3.9 | 0.27 | 0.56 | 0.73 | 0.00 | 8.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.30 | 19.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.83 | 19.49 | 1.00 | 87.6 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.78 | 8.20 | 13.57 | 2.00 | 68.8 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.00 | 8.13 | 13.31 | 4.00 | 75.5 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.88 | 8.01 | 12.37 | 2.00 | 79.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.25 | 24.32 | 40.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.90 | 14.89 | 24.46 | 0.00 | 73.9 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.30 | 1.57 | 2.63 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.91 | 17.94 | 29.33 | 2.00 | 88.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.70 | 16.36 | 25.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.35 | 24.47 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.61 | 11.37 | 18.51 | 9.00 | 59.1 | 90.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.64 | 10.12 | 17.64 | 17.00 | 36.7 | 90.0 |

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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.23, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 0.92 | 4.05 | 7.99 | 2.00 | 40.1 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.11 | 0.25 | 0.41 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.38 | 12.02 | 19.35 | 6.00 | 88.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.34 | 10.51 | 17.68 | 6.00 | 83.7 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.45 | 9.21 | 15.09 | 1.00 | 77.3 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.06 | 8.39 | 14.04 | 3.00 | 77.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.49 | 7.38 | 11.89 | 0.00 | 74.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.78 | 38.88 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.55 | 15.54 | 24.89 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.38 | 1.22 | 2.21 | 0.00 | 10.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.51 | 16.13 | 27.04 | 2.00 | 81.4 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.39 | 14.77 | 24.57 | 6.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.07 | 14.73 | 24.51 | 3.00 | 87.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.71 | 13.75 | 22.19 | 3.00 | 74.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.73 | 13.44 | 22.11 | 2.00 | 78.2 | 73.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 261.24
- Total actual points: 183.00
- Average predicted points: 65.31
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
- Predicted score: 67.59
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.02 | 8.80 | 14.71 | 3.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.02 | 0.10 | 0.30 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.02 | 13.68 | 21.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.12 | 11.78 | 18.84 | 2.00 | 80.3 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.98 | 10.95 | 17.55 | 0.00 | 81.6 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.66 | 8.03 | 12.52 | 2.00 | 68.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.65 | 12.23 | 2.00 | 68.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.41 | 24.71 | 40.89 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.84 | 18.41 | 27.61 | 5.00 | 86.3 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.72 | 2.00 | 3.21 | 0.00 | 13.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.67 | 17.86 | 28.72 | 2.00 | 82.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.40 | 25.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.62 | 16.29 | 25.60 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.25 | 15.43 | 24.41 | 9.00 | 82.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.49 | 15.27 | 23.68 | 2.00 | 88.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.84
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.49, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.51 | 9.76 | 15.76 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.09 | 0.27 | 0.48 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.42 | 19.89 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.12 | 11.87 | 19.54 | 6.00 | 82.6 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.38 | 11.23 | 17.27 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.52 | 7.79 | 12.71 | 7.00 | 68.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.44 | 7.61 | 12.37 | 8.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 23.79 | 39.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.41 | 13.36 | 20.69 | 2.00 | 54.6 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.47 | 1.57 | 2.56 | 0.00 | 7.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.74 | 27.97 | 3.00 | 83.7 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.06 | 16.11 | 24.51 | 2.00 | 84.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.09 | 14.99 | 24.10 | 5.00 | 84.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.40 | 13.18 | 21.36 | 0.00 | 73.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.88 | 13.13 | 21.30 | 1.00 | 74.6 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.77
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.85) beats the best remaining Bench Boost opportunity (7.15).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.85) beats the best remaining Bench Boost opportunity (7.15).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.47 | 8.49 | 14.21 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Krisztián Hegyi | GK | 19 | 3.9 | 0.15 | 0.39 | 0.64 | 0.00 | 5.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 12.23 | 19.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.67 | 19.34 | 1.00 | 85.9 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.93 | 8.04 | 13.29 | 4.00 | 73.8 | 90.0 |
| Bench 3 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.69 | 8.02 | 13.40 | 2.00 | 67.1 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.83 | 7.93 | 12.30 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.22 | 24.20 | 40.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.54 | 14.05 | 23.06 | 0.00 | 67.0 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.32 | 2.40 | 0.00 | 8.3 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.85 | 17.78 | 29.15 | 2.00 | 87.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.75 | 16.57 | 26.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.25 | 15.29 | 24.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.49 | 11.13 | 18.31 | 9.00 | 56.9 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.83 | 9.05 | 16.03 | 17.00 | 39.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.03
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.40, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.69 | 5.68 | 10.01 | 2.00 | 53.0 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 3.9 | 0.07 | 0.24 | 0.38 | 0.00 | 4.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.03 | 19.30 | 6.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.34 | 10.47 | 17.53 | 6.00 | 84.3 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.48 | 9.26 | 15.08 | 1.00 | 78.3 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.07 | 8.45 | 14.06 | 3.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.41 | 11.86 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.82 | 38.86 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.65 | 15.77 | 25.18 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.34 | 1.14 | 2.04 | 0.00 | 8.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 16.07 | 26.86 | 2.00 | 82.5 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.12 | 14.86 | 24.65 | 3.00 | 88.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.18 | 14.50 | 23.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.73 | 13.76 | 22.17 | 3.00 | 75.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.72 | 13.45 | 22.10 | 2.00 | 78.8 | 73.0 |
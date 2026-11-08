# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 260.32
- Total actual points: 183.00
- Average predicted points: 65.08
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
- Predicted score: 67.39
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.00 | 8.73 | 14.51 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.12 | 0.32 | 0.47 | 0.00 | 1.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 13.78 | 21.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.13 | 11.80 | 18.84 | 2.00 | 81.9 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 4.03 | 11.12 | 17.84 | 0.00 | 82.2 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.75 | 8.27 | 12.87 | 2.00 | 70.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.67 | 7.98 | 12.75 | 2.00 | 69.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 24.55 | 40.67 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.88 | 18.47 | 27.66 | 5.00 | 86.8 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.58 | 1.52 | 2.40 | 0.00 | 12.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.59 | 17.64 | 28.39 | 2.00 | 81.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.61 | 16.16 | 25.30 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.65 | 16.05 | 25.18 | 5.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.55 | 15.39 | 23.80 | 2.00 | 88.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.25 | 24.08 | 9.00 | 81.9 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.67
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.63, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.47 | 9.65 | 15.50 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.22 | 0.41 | 0.00 | 3.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.41 | 19.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.17 | 12.05 | 19.85 | 6.00 | 83.9 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.52 | 11.64 | 17.90 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 8.07 | 13.12 | 7.00 | 70.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.55 | 7.95 | 12.92 | 8.00 | 71.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.97 | 23.63 | 39.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.41 | 13.48 | 20.96 | 2.00 | 54.5 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.30 | 1.08 | 1.76 | 0.00 | 5.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.28 | 16.46 | 27.56 | 3.00 | 82.9 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.15 | 16.31 | 24.76 | 2.00 | 85.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.03 | 14.78 | 23.76 | 5.00 | 84.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.85 | 13.05 | 21.16 | 1.00 | 74.8 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.34 | 13.00 | 21.08 | 0.00 | 72.4 | 0.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.71
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.73) beats the best remaining Bench Boost opportunity (7.05).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.73) beats the best remaining Bench Boost opportunity (7.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.44 | 8.38 | 13.97 | 0.00 | 89.7 | 0.0 |
| Bench 1 | Bench Boost | Karl Darlow | GK | 11 | 3.9 | 0.21 | 0.52 | 0.77 | 0.00 | 4.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.33 | 19.72 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.07 | 11.91 | 19.70 | 1.00 | 87.7 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.82 | 8.46 | 14.11 | 2.00 | 68.1 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.05 | 8.34 | 13.72 | 4.00 | 75.5 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.96 | 8.33 | 12.95 | 2.00 | 79.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.16 | 24.08 | 39.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.53 | 14.09 | 23.15 | 0.00 | 67.4 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.00 | 0.78 | 1.46 | 0.00 | 7.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.75 | 17.51 | 28.77 | 2.00 | 86.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.71 | 16.37 | 25.82 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.18 | 15.05 | 24.08 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.58 | 11.37 | 18.69 | 9.00 | 57.7 | 90.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.70 | 8.75 | 15.68 | 17.00 | 38.1 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.56
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.02) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.65, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.02) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.65 | 5.63 | 9.92 | 2.00 | 52.0 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.21 | 0.59 | 0.91 | 0.00 | 5.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.43 | 12.14 | 19.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.41 | 10.74 | 17.98 | 6.00 | 85.9 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.58 | 9.61 | 15.66 | 1.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.15 | 8.69 | 14.43 | 3.00 | 79.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.63 | 7.81 | 12.51 | 0.00 | 76.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.02 | 23.75 | 38.80 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.50 | 15.25 | 24.24 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.15 | 0.52 | 0.99 | 0.00 | 7.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.42 | 15.81 | 26.49 | 2.00 | 81.4 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.98 | 14.39 | 23.87 | 3.00 | 87.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.07 | 14.18 | 23.12 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.70 | 13.65 | 22.00 | 3.00 | 75.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.75 | 13.51 | 22.21 | 2.00 | 79.4 | 73.0 |
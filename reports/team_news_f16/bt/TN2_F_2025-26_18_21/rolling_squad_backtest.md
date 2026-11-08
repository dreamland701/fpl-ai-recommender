# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 261.72
- Total actual points: 168.00
- Average predicted points: 65.43
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
- Predicted score: 66.81
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.97 | 8.76 | 14.81 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.08 | 0.21 | 0.47 | 0.00 | 2.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.95 | 13.55 | 21.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.08 | 11.70 | 18.84 | 2.00 | 79.2 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.92 | 10.85 | 17.52 | 0.00 | 79.9 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.62 | 7.93 | 12.47 | 2.00 | 67.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.57 | 12.22 | 2.00 | 67.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 24.61 | 40.91 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.76 | 18.23 | 27.41 | 5.00 | 84.3 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.77 | 2.09 | 3.39 | 0.00 | 15.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.61 | 17.77 | 28.74 | 2.00 | 80.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.66 | 16.22 | 25.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.56 | 16.10 | 25.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.35 | 24.38 | 9.00 | 81.1 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.40 | 15.04 | 23.38 | 2.00 | 85.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.22
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.44, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.45 | 9.71 | 15.81 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.10 | 0.38 | 0.00 | 4.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.45 | 12.32 | 19.83 | 2.00 | 88.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.82 | 19.60 | 6.00 | 81.6 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.33 | 11.10 | 17.14 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.49 | 7.71 | 12.67 | 7.00 | 68.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.41 | 7.56 | 12.40 | 8.00 | 69.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.98 | 23.72 | 39.71 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.37 | 13.38 | 20.87 | 2.00 | 53.7 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.52 | 1.68 | 2.79 | 0.00 | 8.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.34 | 16.69 | 28.05 | 3.00 | 82.1 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.99 | 15.89 | 24.21 | 2.00 | 83.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.05 | 14.93 | 24.14 | 5.00 | 82.9 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.37 | 13.14 | 21.44 | 0.00 | 72.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.83 | 13.05 | 21.29 | 1.00 | 73.4 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.36
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.93) beats the best remaining Bench Boost opportunity (7.24).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.93) beats the best remaining Bench Boost opportunity (7.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.49 | 8.58 | 14.35 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.11 | 0.28 | 0.00 | 0.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.29 | 19.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.06 | 11.78 | 19.45 | 1.00 | 87.4 | 90.0 |
| Bench 3 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.75 | 8.13 | 13.50 | 2.00 | 68.5 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.99 | 8.11 | 13.29 | 4.00 | 75.3 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.88 | 8.01 | 12.39 | 2.00 | 79.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.25 | 24.28 | 40.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.60 | 14.19 | 23.24 | 0.00 | 68.6 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.30 | 1.57 | 2.64 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.88 | 17.87 | 29.29 | 2.00 | 88.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.77 | 16.53 | 26.06 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.34 | 24.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.90 | 14.96 | 23.99 | 4.00 | 74.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.55 | 11.22 | 18.36 | 9.00 | 58.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.32
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.35, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.68 | 5.75 | 10.28 | 2.00 | 52.5 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.14 | 0.44 | 0.81 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 11.96 | 19.31 | 6.00 | 88.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.31 | 10.42 | 17.58 | 6.00 | 83.3 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.44 | 9.18 | 15.06 | 1.00 | 77.1 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.04 | 8.37 | 14.02 | 3.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.48 | 7.36 | 11.88 | 0.00 | 74.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.74 | 38.90 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.58 | 15.63 | 25.07 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.37 | 1.20 | 2.19 | 0.00 | 9.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.46 | 16.01 | 26.92 | 2.00 | 80.9 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.97 | 14.59 | 23.43 | 1.00 | 80.8 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.14 | 14.43 | 23.65 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.69 | 13.68 | 22.16 | 3.00 | 74.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.70 | 13.37 | 22.06 | 2.00 | 78.0 | 73.0 |
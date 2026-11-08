# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 256.39
- Total actual points: 207.00
- Average predicted points: 64.10
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
- Predicted score: 67.42
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.41 | 9.59 | 15.64 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.06 | 0.14 | 0.26 | 0.00 | 2.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.97 | 13.48 | 21.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 4.13 | 11.40 | 17.79 | 10.00 | 87.1 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.98 | 11.08 | 17.72 | 0.00 | 81.9 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.65 | 7.96 | 12.52 | 2.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.64 | 7.68 | 12.32 | 2.00 | 70.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.13 | 24.25 | 39.88 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.88 | 17.69 | 26.76 | 5.00 | 88.3 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.69 | 1.97 | 3.11 | 0.00 | 13.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.63 | 17.32 | 28.10 | 2.00 | 84.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.42 | 25.65 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.74 | 16.13 | 25.26 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.53 | 15.04 | 23.37 | 2.00 | 87.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.14 | 14.86 | 23.27 | 9.00 | 82.8 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.08
- Actual score: 50.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.76, hit 0)
- Autosub: Jaka Bijol replaced Michael Keane.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.04 | 9.34 | 15.44 | 10.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.00 | 0.10 | 0.00 | 3.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.63 | 19.13 | 6.00 | 82.7 | 90.0 |
| XI | Bench | Michael Keane | DEF | 9 | 4.7 | 3.95 | 11.58 | 18.14 | 0.00 | 89.4 | 0.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.46 | 11.32 | 17.30 | 2.00 | 85.8 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.54 | 7.61 | 12.52 | 7.00 | 69.8 | 90.0 |
| Bench 3 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.48 | 7.54 | 12.27 | 8.00 | 71.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.83 | 23.26 | 38.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.38 | 12.86 | 19.97 | 2.00 | 57.3 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.40 | 1.52 | 2.60 | 0.00 | 7.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.31 | 16.55 | 27.73 | 3.00 | 84.4 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.14 | 15.70 | 23.80 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.88 | 14.44 | 23.00 | 5.00 | 83.5 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.31 | 13.01 | 21.10 | 0.00 | 73.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.94 | 12.80 | 20.93 | 1.00 | 75.9 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 61.25
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.80) beats the best remaining Bench Boost opportunity (6.22).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.80) beats the best remaining Bench Boost opportunity (6.22).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.28 | 9.97 | 16.29 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench Boost | Karl Darlow | GK | 11 | 3.9 | 0.12 | 0.31 | 0.49 | 0.00 | 5.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.91 | 11.44 | 18.99 | 1.00 | 85.9 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.75 | 8.09 | 13.66 | 2.00 | 68.7 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.95 | 8.08 | 13.34 | 4.00 | 75.1 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.84 | 8.02 | 12.31 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench Boost | Michael Keane | DEF | 9 | 4.7 | 1.87 | 5.95 | 10.50 | 0.00 | 40.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.78 | 39.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.53 | 13.85 | 22.81 | 0.00 | 68.6 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.36 | 2.53 | 0.00 | 8.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.75 | 17.65 | 29.23 | 2.00 | 87.7 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.84 | 16.48 | 26.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.11 | 14.77 | 23.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.49 | 10.74 | 17.70 | 9.00 | 57.5 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.64 | 8.83 | 15.81 | 17.00 | 37.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.20 -> 2.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.63
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.01, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.82) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.58 | 9.74 | 15.58 | 3.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.09 | 0.30 | 0.53 | 0.00 | 5.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.26 | 10.23 | 17.19 | 6.00 | 84.0 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.53 | 9.44 | 15.45 | 1.00 | 79.1 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.7 | 3.29 | 8.59 | 13.78 | 5.00 | 69.5 | 82.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.09 | 8.44 | 14.16 | 3.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.53 | 7.42 | 11.79 | 0.00 | 75.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.82 | 23.48 | 38.10 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.56 | 15.36 | 24.52 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.32 | 1.18 | 2.07 | 0.00 | 9.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.38 | 16.00 | 27.09 | 2.00 | 82.6 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.09 | 14.63 | 24.03 | 3.00 | 89.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.01 | 13.98 | 22.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.72 | 13.39 | 21.75 | 2.00 | 78.4 | 73.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.75 | 13.35 | 21.41 | 3.00 | 77.3 | 90.0 |
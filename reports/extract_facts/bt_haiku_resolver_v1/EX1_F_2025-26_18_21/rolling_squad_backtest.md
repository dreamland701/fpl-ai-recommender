# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 263.90
- Total actual points: 157.00
- Average predicted points: 65.97
- Average actual points: 39.25
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
- Predicted score: 69.17
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.03 | 8.90 | 14.89 | 3.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.09 | 0.15 | 0.25 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.99 | 13.62 | 21.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.16 | 11.89 | 18.94 | 2.00 | 80.9 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.99 | 11.01 | 17.60 | 0.00 | 81.9 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.66 | 8.01 | 12.46 | 2.00 | 68.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.55 | 7.64 | 12.20 | 2.00 | 68.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.44 | 24.84 | 41.02 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.98 | 18.69 | 28.16 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.75 | 2.07 | 3.30 | 0.00 | 13.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 6.40 | 19.47 | 30.87 | 2.00 | 89.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.96 | 16.84 | 26.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.58 | 16.11 | 25.23 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.91 | 16.09 | 25.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.49 | 24.43 | 9.00 | 82.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.37
- Actual score: 36.00
- Transfer: Daniel Ballard -> Patrick Dorgu (projected gain 4.04, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.50 | 9.81 | 15.86 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.11 | 0.25 | 0.39 | 0.00 | 4.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.51 | 12.43 | 19.86 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 11.97 | 19.71 | 6.00 | 83.1 | 90.0 |
| XI | XI | Patrick Dorgu | DEF | 14 | 4.2 | 4.66 | 11.78 | 18.07 | 2.00 | 85.2 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.53 | 7.79 | 12.68 | 7.00 | 69.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.45 | 7.65 | 12.43 | 8.00 | 70.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.07 | 23.91 | 39.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.44 | 13.55 | 20.98 | 2.00 | 54.7 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.48 | 1.64 | 2.69 | 0.00 | 7.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.45 | 16.94 | 28.25 | 3.00 | 84.2 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.02 | 15.90 | 24.07 | 2.00 | 84.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.14 | 15.11 | 24.26 | 5.00 | 84.6 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.46 | 13.36 | 21.63 | 0.00 | 74.2 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.92 | 13.24 | 21.42 | 1.00 | 75.0 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.88
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.33) beats the best remaining Bench Boost opportunity (6.50).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.09, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.33) beats the best remaining Bench Boost opportunity (6.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.47 | 8.56 | 14.36 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Václav Hladký | GK | 3 | 3.9 | 0.00 | 0.18 | 0.32 | 0.00 | 5.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.38 | 12.28 | 19.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.04 | 11.78 | 19.49 | 1.00 | 86.5 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.97 | 8.08 | 13.29 | 4.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.84 | 7.96 | 12.34 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench Boost | Patrick Dorgu | DEF | 14 | 4.2 | 2.31 | 6.74 | 10.41 | 1.00 | 56.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.24 | 24.32 | 40.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.88 | 15.09 | 24.79 | 0.00 | 79.0 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.18 | 1.36 | 2.45 | 0.00 | 8.4 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.87 | 17.90 | 29.34 | 2.00 | 87.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.70 | 16.39 | 25.85 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.33 | 24.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.96 | 24.00 | 4.00 | 73.9 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.60 | 11.38 | 18.58 | 9.00 | 58.6 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.48
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel Gudmundsson -> Micky van de Ven (projected gain 3.42, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.06) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.70 | 5.82 | 10.32 | 2.00 | 52.7 | 90.0 |
| Bench 1 | Bench | Václav Hladký | GK | 3 | 3.9 | 0.12 | 0.26 | 0.48 | 0.00 | 5.6 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.44 | 12.13 | 19.43 | 6.00 | 89.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.14 | 11.30 | 17.25 | 0.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.37 | 10.58 | 17.70 | 6.00 | 84.6 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.09 | 8.48 | 14.08 | 3.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Patrick Dorgu | DEF | 14 | 4.2 | 3.06 | 7.95 | 12.81 | 5.00 | 64.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.92 | 38.96 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 2.33 | 9.05 | 16.22 | 0.00 | 28.8 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.34 | 1.15 | 2.07 | 0.00 | 8.8 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.56 | 16.24 | 27.10 | 2.00 | 83.0 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.43 | 15.16 | 24.83 | 6.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.03 | 14.71 | 23.45 | 1.00 | 82.0 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.87 | 22.28 | 3.00 | 75.8 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.78 | 13.56 | 22.21 | 2.00 | 79.5 | 73.0 |
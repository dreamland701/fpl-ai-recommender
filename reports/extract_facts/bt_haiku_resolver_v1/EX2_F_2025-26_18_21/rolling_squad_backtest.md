# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 262.28
- Total actual points: 157.00
- Average predicted points: 65.57
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
- Predicted score: 68.27
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.99 | 8.82 | 14.88 | 3.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.08 | 0.21 | 0.47 | 0.00 | 2.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.93 | 13.52 | 21.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.79 | 18.92 | 2.00 | 79.5 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.93 | 10.88 | 17.55 | 0.00 | 79.9 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.61 | 7.92 | 12.45 | 2.00 | 67.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.51 | 7.55 | 12.19 | 2.00 | 67.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.36 | 24.69 | 40.93 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.87 | 18.50 | 28.04 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.79 | 2.14 | 3.45 | 0.00 | 15.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 6.33 | 19.33 | 30.80 | 2.00 | 87.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.85 | 16.66 | 26.50 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.50 | 15.96 | 25.14 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.83 | 15.93 | 24.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.37 | 24.37 | 9.00 | 81.0 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.72
- Actual score: 36.00
- Transfer: Daniel Ballard -> Patrick Dorgu (projected gain 4.07, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.46 | 9.73 | 15.84 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.11 | 0.39 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.45 | 12.33 | 19.83 | 2.00 | 88.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.10 | 11.88 | 19.68 | 6.00 | 81.9 | 90.0 |
| XI | XI | Patrick Dorgu | DEF | 14 | 4.2 | 4.63 | 11.74 | 18.12 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.49 | 7.71 | 12.67 | 7.00 | 68.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.41 | 7.57 | 12.42 | 8.00 | 69.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.79 | 39.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.40 | 13.47 | 20.95 | 2.00 | 53.8 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.54 | 1.73 | 2.86 | 0.00 | 9.2 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.83 | 28.21 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.93 | 15.75 | 23.99 | 2.00 | 81.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.08 | 15.01 | 24.22 | 5.00 | 83.2 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.42 | 13.26 | 21.59 | 0.00 | 73.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.86 | 13.12 | 21.35 | 1.00 | 73.5 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.40
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.56) beats the best remaining Bench Boost opportunity (6.78).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.56) beats the best remaining Bench Boost opportunity (6.78).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.50 | 8.61 | 14.39 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Karl Darlow | GK | 11 | 3.9 | 0.00 | 0.13 | 0.31 | 0.00 | 0.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.41 | 12.32 | 19.61 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.08 | 11.83 | 19.51 | 1.00 | 87.6 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.00 | 8.13 | 13.30 | 4.00 | 75.4 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.88 | 8.01 | 12.37 | 2.00 | 79.6 | 90.0 |
| Bench 3 | Bench Boost | Patrick Dorgu | DEF | 14 | 4.2 | 2.38 | 6.83 | 10.48 | 1.00 | 57.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.26 | 24.34 | 40.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.90 | 15.10 | 24.77 | 0.00 | 79.3 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.31 | 1.58 | 2.65 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.91 | 17.95 | 29.36 | 2.00 | 88.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.71 | 16.39 | 25.83 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.37 | 24.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.91 | 14.98 | 24.00 | 4.00 | 74.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.62 | 11.39 | 18.55 | 9.00 | 59.3 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.89
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Gabriel Gudmundsson -> Micky van de Ven (projected gain 3.39, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.70 | 5.82 | 10.38 | 2.00 | 52.9 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 3.9 | 0.15 | 0.44 | 0.82 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.39 | 12.04 | 19.39 | 6.00 | 88.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.09 | 11.22 | 17.24 | 0.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.51 | 17.68 | 6.00 | 83.6 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.06 | 8.40 | 14.05 | 3.00 | 77.8 | 90.0 |
| Bench 2 | Bench | Patrick Dorgu | DEF | 14 | 4.2 | 3.04 | 7.90 | 12.83 | 5.00 | 63.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.80 | 38.91 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 2.35 | 9.07 | 16.30 | 0.00 | 29.5 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.38 | 1.22 | 2.21 | 0.00 | 10.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.51 | 16.14 | 27.07 | 2.00 | 81.5 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.38 | 15.05 | 24.79 | 6.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.97 | 14.61 | 23.42 | 1.00 | 80.6 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.71 | 13.76 | 22.23 | 3.00 | 74.3 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.73 | 13.47 | 22.16 | 2.00 | 78.3 | 73.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 258.00
- Total actual points: 178.00
- Average predicted points: 64.50
- Average actual points: 44.50
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
- Predicted score: 69.33
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.04 | 8.91 | 14.90 | 3.00 | 84.2 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.09 | 0.19 | 0.35 | 0.00 | 3.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.98 | 13.62 | 21.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.16 | 11.88 | 18.91 | 2.00 | 80.7 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.99 | 11.00 | 17.58 | 0.00 | 81.7 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.67 | 8.02 | 12.45 | 2.00 | 68.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.65 | 12.19 | 2.00 | 68.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.70 | 25.17 | 41.89 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.99 | 18.47 | 27.95 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.74 | 2.06 | 3.28 | 0.00 | 13.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.94 | 18.27 | 29.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.01 | 16.68 | 25.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.97 | 16.62 | 26.41 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.57 | 16.09 | 25.16 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.28 | 15.49 | 24.39 | 9.00 | 82.3 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.20
- Actual score: 42.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Gabriel Gudmundsson replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.50 | 9.82 | 15.87 | 2.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.09 | 0.26 | 0.41 | 0.00 | 3.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.50 | 12.42 | 19.83 | 2.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 11.98 | 19.68 | 6.00 | 82.8 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.54 | 7.80 | 12.67 | 7.00 | 69.0 | 90.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.46 | 7.65 | 12.42 | 8.00 | 70.7 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.7 | 1.79 | 5.83 | 10.64 | 0.00 | 40.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.89 | 39.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.44 | 13.55 | 20.95 | 2.00 | 54.5 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.48 | 1.63 | 2.68 | 0.00 | 7.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.44 | 16.93 | 28.23 | 3.00 | 84.1 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.00 | 15.87 | 23.97 | 2.00 | 83.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.14 | 15.11 | 24.23 | 5.00 | 84.3 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.46 | 13.35 | 21.59 | 0.00 | 74.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.91 | 13.22 | 21.37 | 1.00 | 74.8 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.86
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.39) beats the best remaining Bench Boost opportunity (5.32).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.39) beats the best remaining Bench Boost opportunity (5.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.48 | 8.58 | 14.39 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.11 | 0.43 | 0.67 | 0.00 | 5.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.37 | 12.26 | 19.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.04 | 11.78 | 19.48 | 1.00 | 86.4 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.97 | 8.08 | 13.29 | 4.00 | 74.5 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.84 | 7.96 | 12.33 | 2.00 | 78.5 | 90.0 |
| Bench 3 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.46 | 4.79 | 9.07 | 1.00 | 32.2 | 24.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.24 | 24.30 | 40.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.87 | 14.85 | 24.46 | 0.00 | 73.2 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.18 | 1.35 | 2.44 | 0.00 | 8.4 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 5.87 | 17.89 | 29.31 | 2.00 | 87.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.69 | 16.35 | 25.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.31 | 24.46 | 1.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.59 | 11.36 | 18.53 | 9.00 | 58.4 | 90.0 |
| Bench 2 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.64 | 9.89 | 17.11 | 17.00 | 37.0 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.61
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Micky van de Ven (projected gain 3.93, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 0.78 | 3.77 | 7.64 | 2.00 | 37.0 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.9 | 0.32 | 0.54 | 0.72 | 0.00 | 3.0 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.43 | 12.11 | 19.39 | 6.00 | 89.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.13 | 11.30 | 17.23 | 0.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.37 | 10.58 | 17.69 | 6.00 | 84.7 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.09 | 8.47 | 14.06 | 3.00 | 78.9 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.52 | 7.44 | 11.89 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 23.89 | 38.93 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 9.0 | 2.33 | 9.05 | 16.23 | 0.00 | 28.9 | 0.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.34 | 1.15 | 2.06 | 0.00 | 8.8 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.8 | 5.56 | 16.22 | 27.07 | 2.00 | 82.8 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.44 | 14.87 | 24.60 | 6.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.12 | 14.82 | 24.54 | 3.00 | 88.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.86 | 22.24 | 3.00 | 75.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.77 | 13.53 | 22.15 | 2.00 | 79.4 | 73.0 |
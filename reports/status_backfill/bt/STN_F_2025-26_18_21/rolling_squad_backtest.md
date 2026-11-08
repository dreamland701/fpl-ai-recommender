# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 261.88
- Total actual points: 183.00
- Average predicted points: 65.47
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
- Predicted score: 68.69
- Actual score: 37.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.96 | 8.83 | 14.81 | 3.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.06 | 0.08 | 0.19 | 0.00 | 3.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.06 | 13.67 | 21.46 | 2.00 | 95.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.05 | 11.81 | 18.88 | 2.00 | 79.4 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.7 | 3.99 | 10.98 | 17.59 | 0.00 | 81.7 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.67 | 8.03 | 12.50 | 2.00 | 68.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.65 | 7.67 | 12.25 | 2.00 | 69.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.32 | 24.77 | 41.01 | 2.00 | 116.9 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.31 | 18.43 | 27.56 | 5.00 | 94.8 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.71 | 2.02 | 3.23 | 0.00 | 13.1 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.70 | 17.91 | 28.81 | 2.00 | 82.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.89 | 16.38 | 25.72 | 5.00 | 100.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 6.01 | 16.28 | 25.50 | 1.00 | 105.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.33 | 15.48 | 24.46 | 9.00 | 84.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 5.74 | 15.24 | 23.52 | 2.00 | 92.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Matheus Santos Carneiro da Cunha
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.96
- Actual score: 36.00
- Transfer: Daniel Ballard -> Diogo Dalot Teixeira (projected gain 3.47, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.46 | 9.78 | 15.84 | 2.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.04 | 0.19 | 0.20 | 0.00 | 3.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.52 | 12.43 | 19.88 | 2.00 | 90.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.09 | 11.92 | 19.65 | 6.00 | 82.8 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 4.53 | 11.22 | 17.19 | 2.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.56 | 7.80 | 12.69 | 7.00 | 69.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.51 | 7.64 | 12.42 | 8.00 | 71.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.02 | 23.83 | 39.79 | 2.00 | 117.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.48 | 13.46 | 20.92 | 2.00 | 55.4 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.48 | 1.58 | 2.62 | 0.00 | 7.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.26 | 16.79 | 28.10 | 3.00 | 81.1 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.0 | 6.40 | 16.07 | 24.34 | 2.00 | 90.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.94 | 15.04 | 24.20 | 5.00 | 82.1 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.28 | 13.23 | 21.49 | 0.00 | 71.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.96 | 13.17 | 21.37 | 1.00 | 75.6 | 81.0 |

## GW20

- Train rows: 175452
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.20
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.44) beats the best remaining Bench Boost opportunity (6.76).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.44) beats the best remaining Bench Boost opportunity (6.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.38 | 8.51 | 14.31 | 0.00 | 89.1 | 0.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 3.9 | 0.00 | 0.11 | 0.17 | 0.00 | 4.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.31 | 12.24 | 19.59 | 2.00 | 93.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.99 | 11.71 | 19.42 | 1.00 | 86.4 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.99 | 8.05 | 13.27 | 4.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 2.67 | 8.05 | 13.46 | 2.00 | 65.8 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.86 | 7.95 | 12.35 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.12 | 24.24 | 40.14 | 2.00 | 112.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.51 | 14.10 | 23.19 | 0.00 | 67.2 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.17 | 1.33 | 2.42 | 0.00 | 8.5 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.80 | 17.80 | 29.25 | 2.00 | 86.3 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 6.04 | 16.54 | 26.09 | 5.00 | 100.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.30 | 24.49 | 1.00 | 92.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 3.44 | 11.18 | 18.37 | 9.00 | 55.4 | 90.0 |
| Bench 3 | Bench Boost | Declan Rice | MID | 1 | 7.1 | 2.60 | 9.10 | 16.27 | 17.00 | 35.7 | 90.0 |

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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.98) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.43, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.98) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 4.9 | 1.62 | 5.73 | 10.21 | 2.00 | 51.5 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 3.9 | 0.05 | 0.22 | 0.37 | 0.00 | 4.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 12.06 | 19.36 | 6.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.28 | 10.49 | 17.60 | 6.00 | 84.0 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 4.5 | 3.48 | 9.26 | 15.10 | 1.00 | 78.0 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.12 | 8.46 | 14.06 | 3.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.55 | 7.43 | 11.89 | 0.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.98 | 23.85 | 38.96 | 6.00 | 110.9 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.97 | 15.78 | 25.17 | 12.00 | 108.7 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.33 | 1.13 | 2.05 | 0.00 | 8.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.44 | 16.09 | 26.95 | 2.00 | 81.8 | 72.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.30 | 14.82 | 24.61 | 3.00 | 91.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.10 | 14.50 | 23.66 | 6.00 | 90.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.81 | 13.79 | 22.23 | 3.00 | 75.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 4.74 | 13.46 | 22.11 | 2.00 | 78.8 | 73.0 |
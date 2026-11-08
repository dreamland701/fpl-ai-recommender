# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 268.98
- Total actual points: 198.00
- Average predicted points: 67.25
- Average actual points: 49.50
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
- Predicted score: 68.50
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Omar Alderete replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 11.03 | 17.91 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.10 | 13.76 | 21.59 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.60 | 12.44 | 19.89 | 0.00 | 88.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.93 | 19.02 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.0 | 3.20 | 8.37 | 12.80 | 4.00 | 70.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.72 | 7.83 | 12.44 | 2.00 | 71.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.34 | 24.81 | 41.02 | 2.00 | 117.3 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.46 | 18.80 | 28.09 | 5.00 | 97.9 | 85.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.22 | 4.31 | 6.90 | 2.00 | 28.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.71 | 17.92 | 28.79 | 2.00 | 82.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 6.02 | 16.29 | 25.50 | 1.00 | 106.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.83 | 16.24 | 25.52 | 5.00 | 99.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.35 | 15.51 | 24.48 | 9.00 | 84.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.83 | 11.33 | 17.91 | 4.00 | 78.4 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.10
- Actual score: 39.00
- Transfer: Jurriën Timber -> Joško Gvardiol (projected gain 8.61, hit 0)
- Autosub: Omar Alderete replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.59 | 17.26 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.11 | 11.95 | 19.66 | 6.00 | 83.3 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.08 | 11.70 | 19.10 | 1.00 | 88.2 | 33.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.0 | 2.82 | 8.19 | 13.13 | 8.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.55 | 7.73 | 12.52 | 8.00 | 72.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.07 | 23.96 | 39.94 | 2.00 | 118.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.49 | 13.46 | 20.89 | 2.00 | 55.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.88 | 5.68 | 9.00 | 2.00 | 49.5 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.24 | 16.71 | 27.94 | 3.00 | 80.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.95 | 15.04 | 24.20 | 5.00 | 82.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.87 | 12.95 | 21.03 | 1.00 | 73.9 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.16 | 12.91 | 21.00 | 0.00 | 69.2 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.77 | 11.50 | 18.65 | 5.00 | 76.2 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.28
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.03) beats the best remaining Bench Boost opportunity (10.45).
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 6.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.03) beats the best remaining Bench Boost opportunity (10.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.89 | 11.32 | 18.24 | 1.00 | 94.2 | 90.0 |
| Bench 1 | Bench Boost | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.40 | 12.47 | 19.94 | 2.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.00 | 11.74 | 19.44 | 1.00 | 86.8 | 90.0 |
| Bench 2 | Bench Boost | Joško Gvardiol | DEF | 13 | 6.0 | 3.57 | 10.93 | 17.95 | 1.00 | 61.6 | 50.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.59 | 9.79 | 15.52 | 1.00 | 90.3 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.90 | 8.02 | 12.44 | 2.00 | 79.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.21 | 24.43 | 40.40 | 2.00 | 113.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.57 | 14.24 | 23.36 | 0.00 | 68.5 | 0.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.57 | 6.57 | 10.05 | 12.00 | 57.7 | 85.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.82 | 17.83 | 29.26 | 2.00 | 86.7 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 6.13 | 16.77 | 26.43 | 5.00 | 102.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.22 | 15.33 | 24.54 | 1.00 | 92.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 4.99 | 13.88 | 22.33 | 10.00 | 89.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.21 | 11.46 | 18.68 | 4.00 | 81.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.50 -> 2.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.11
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 14.58, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.47 | 10.21 | 16.69 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.21 | 19.59 | 6.00 | 91.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.27 | 10.48 | 17.55 | 6.00 | 83.9 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.26 | 9.54 | 15.20 | 1.00 | 88.3 | 82.0 |
| Bench 2 | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.00 | 9.42 | 16.10 | 0.00 | 54.7 | 0.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.59 | 7.53 | 12.03 | 0.00 | 76.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.05 | 24.01 | 39.19 | 6.00 | 112.3 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 6.08 | 16.05 | 25.55 | 12.00 | 110.9 | 81.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.71 | 7.92 | 11.71 | 9.00 | 66.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.46 | 16.10 | 26.92 | 2.00 | 82.0 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.11 | 14.53 | 23.72 | 6.00 | 91.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 5.10 | 14.13 | 22.87 | 11.00 | 90.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.83 | 13.81 | 22.23 | 3.00 | 75.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.98 | 11.00 | 18.39 | 2.00 | 81.2 | 79.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 267.90
- Total actual points: 182.00
- Average predicted points: 66.98
- Average actual points: 45.50
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
- Predicted score: 67.62
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Omar Alderete replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.03 | 17.91 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 13.76 | 21.59 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.52 | 12.44 | 19.89 | 0.00 | 86.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.19 | 11.93 | 19.02 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.0 | 3.14 | 8.37 | 12.80 | 4.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.64 | 7.83 | 12.44 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.43 | 24.81 | 41.02 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.03 | 18.80 | 28.09 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.28 | 4.31 | 6.90 | 2.00 | 29.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.70 | 17.92 | 28.79 | 2.00 | 82.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.66 | 16.29 | 25.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.69 | 16.24 | 25.52 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.51 | 24.48 | 9.00 | 83.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.76 | 11.33 | 17.91 | 4.00 | 78.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.68
- Actual score: 39.00
- Transfer: Jurriën Timber -> Reece James (projected gain 3.80, hit 0)
- Autosub: Omar Alderete replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.73 | 10.59 | 17.26 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.66 | 20.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 11.95 | 19.66 | 6.00 | 83.2 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.32 | 11.91 | 18.76 | 1.00 | 85.5 | 45.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.0 | 2.80 | 8.19 | 13.13 | 8.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.50 | 7.73 | 12.52 | 8.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.08 | 23.96 | 39.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.43 | 13.46 | 20.89 | 2.00 | 54.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.91 | 5.68 | 9.00 | 2.00 | 50.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.36 | 16.71 | 27.94 | 3.00 | 83.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.12 | 15.04 | 24.20 | 5.00 | 84.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 12.95 | 21.03 | 1.00 | 73.2 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.28 | 12.91 | 21.00 | 0.00 | 70.8 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.73 | 11.50 | 18.65 | 5.00 | 76.4 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 71.07
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.85) beats the best remaining Bench Boost opportunity (9.26).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 6.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.85) beats the best remaining Bench Boost opportunity (9.26).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.32 | 18.24 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.46 | 12.47 | 19.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.03 | 11.74 | 19.44 | 1.00 | 86.5 | 90.0 |
| XI | XI | Omar Alderete | DEF | 17 | 4.0 | 3.59 | 9.79 | 15.52 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Reece James | DEF | 7 | 5.7 | 2.42 | 8.66 | 14.93 | 1.00 | 64.6 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.87 | 8.02 | 12.44 | 2.00 | 79.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.43 | 40.40 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.61 | 14.24 | 23.36 | 0.00 | 68.4 | 0.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 6.57 | 10.05 | 12.00 | 58.0 | 85.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.86 | 17.83 | 29.26 | 2.00 | 87.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.87 | 16.77 | 26.43 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.33 | 24.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.95 | 24.00 | 4.00 | 74.2 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.16 | 11.46 | 18.68 | 4.00 | 81.2 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.00 -> 3.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 69.54
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.11) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.61, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.11) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.54 | 10.21 | 16.69 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.21 | 19.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.63 | 10.59 | 17.14 | 1.00 | 80.4 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.48 | 17.55 | 6.00 | 84.1 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.0 | 3.30 | 9.54 | 15.20 | 1.00 | 89.1 | 82.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.53 | 12.03 | 0.00 | 76.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.11 | 24.01 | 39.19 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.78 | 16.05 | 25.55 | 12.00 | 90.0 | 81.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.71 | 7.92 | 11.71 | 9.00 | 66.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 16.10 | 26.92 | 2.00 | 82.5 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.08 | 14.82 | 23.66 | 1.00 | 83.2 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.53 | 23.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.81 | 22.23 | 3.00 | 76.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.93 | 11.00 | 18.39 | 2.00 | 80.9 | 79.0 |
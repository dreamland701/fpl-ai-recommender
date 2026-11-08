# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 265.77
- Total actual points: 175.00
- Average predicted points: 66.44
- Average actual points: 43.75
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
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.22 | 18.26 | 2.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.05 | 13.90 | 21.92 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.52 | 12.40 | 20.01 | 0.00 | 86.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.19 | 12.01 | 19.18 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.67 | 8.07 | 12.50 | 2.00 | 68.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.64 | 7.82 | 12.43 | 2.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.43 | 25.37 | 42.15 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.03 | 17.87 | 27.13 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.43 | 4.38 | 7.40 | 1.00 | 29.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.70 | 17.70 | 28.45 | 2.00 | 82.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.69 | 16.16 | 25.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.66 | 15.76 | 24.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.30 | 15.33 | 24.31 | 9.00 | 83.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.76 | 11.28 | 17.76 | 4.00 | 78.1 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.68
- Actual score: 38.00
- Transfer: Jurriën Timber -> Reece James (projected gain 4.04, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.73 | 10.81 | 17.71 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.75 | 20.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.15 | 12.13 | 20.00 | 6.00 | 83.2 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.32 | 11.71 | 18.62 | 1.00 | 85.5 | 45.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.56 | 7.72 | 12.47 | 7.00 | 69.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.50 | 7.59 | 12.34 | 8.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.08 | 24.58 | 41.01 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.43 | 12.89 | 20.03 | 2.00 | 54.9 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.83 | 5.30 | 8.66 | 0.00 | 42.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.36 | 16.84 | 28.08 | 3.00 | 83.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.12 | 15.22 | 24.50 | 5.00 | 84.4 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.28 | 13.02 | 21.27 | 0.00 | 70.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.81 | 12.51 | 20.34 | 1.00 | 73.2 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.73 | 11.25 | 18.12 | 5.00 | 76.4 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.93
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.31) beats the best remaining Bench Boost opportunity (7.49).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 6.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.31) beats the best remaining Bench Boost opportunity (7.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.90 | 11.44 | 18.63 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Callan McKenna | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.46 | 12.62 | 20.36 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.03 | 11.83 | 19.72 | 1.00 | 86.5 | 90.0 |
| Bench 3 | Bench Boost | Reece James | DEF | 7 | 5.7 | 2.42 | 8.55 | 14.66 | 1.00 | 64.6 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.99 | 7.99 | 13.12 | 4.00 | 75.1 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.87 | 7.97 | 12.37 | 2.00 | 79.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.91 | 41.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.61 | 14.27 | 23.31 | 0.00 | 68.4 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.02 | 3.53 | 5.72 | 5.00 | 23.9 | 16.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.86 | 17.51 | 28.99 | 2.00 | 87.4 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.87 | 16.31 | 25.95 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.44 | 24.76 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.89 | 14.39 | 23.23 | 4.00 | 74.2 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.16 | 11.29 | 18.24 | 4.00 | 81.2 | 90.0 |

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
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.10, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.11) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.54 | 10.44 | 17.04 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Callan McKenna | GK | 4 | 3.9 | 0.01 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.36 | 19.98 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.33 | 10.57 | 17.81 | 6.00 | 84.1 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.63 | 10.40 | 16.82 | 1.00 | 80.4 | 25.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.13 | 8.45 | 13.98 | 3.00 | 79.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.56 | 7.42 | 11.82 | 0.00 | 76.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.11 | 24.52 | 40.24 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.78 | 15.44 | 24.82 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.39 | 4.22 | 6.94 | 7.00 | 27.9 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.52 | 15.91 | 26.68 | 2.00 | 82.5 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.17 | 14.81 | 24.14 | 6.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.08 | 14.41 | 23.08 | 1.00 | 83.2 | 17.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.76 | 13.45 | 21.58 | 3.00 | 76.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.93 | 10.73 | 17.90 | 2.00 | 80.9 | 79.0 |
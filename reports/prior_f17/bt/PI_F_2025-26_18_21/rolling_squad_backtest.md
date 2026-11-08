# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 263.20
- Total actual points: 175.00
- Average predicted points: 65.80
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
- Predicted score: 67.15
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 10.86 | 17.71 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.14 | 0.23 | 0.40 | 0.00 | 3.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.03 | 13.69 | 21.46 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.40 | 12.16 | 19.51 | 0.00 | 85.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.11 | 11.71 | 18.71 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.68 | 8.04 | 12.52 | 2.00 | 68.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.54 | 7.58 | 12.09 | 2.00 | 68.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.26 | 24.34 | 40.34 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.00 | 18.80 | 28.16 | 5.00 | 86.5 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.37 | 4.23 | 7.21 | 1.00 | 28.3 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.64 | 17.78 | 28.62 | 2.00 | 82.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.82 | 16.54 | 25.97 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.72 | 16.45 | 25.75 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.32 | 15.59 | 24.64 | 9.00 | 82.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.80 | 11.41 | 18.00 | 4.00 | 78.9 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.47
- Actual score: 38.00
- Transfer: Jurriën Timber -> Reece James (projected gain 4.05, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.65 | 10.41 | 17.02 | 2.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.10 | 0.33 | 0.54 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.47 | 12.31 | 19.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.14 | 11.92 | 19.63 | 6.00 | 82.5 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.27 | 11.80 | 18.62 | 1.00 | 84.7 | 45.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.53 | 7.80 | 12.69 | 7.00 | 69.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.42 | 7.54 | 12.25 | 8.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.88 | 23.39 | 39.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.51 | 13.75 | 21.38 | 2.00 | 54.3 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.75 | 5.26 | 8.55 | 0.00 | 40.6 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.32 | 16.60 | 27.79 | 3.00 | 83.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.13 | 15.08 | 24.26 | 5.00 | 84.1 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.47 | 13.38 | 21.72 | 0.00 | 73.2 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.96 | 13.37 | 21.67 | 1.00 | 74.3 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.81 | 11.71 | 18.96 | 5.00 | 77.7 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.25
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.52) beats the best remaining Bench Boost opportunity (7.79).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 6.31, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.52) beats the best remaining Bench Boost opportunity (7.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.76 | 10.98 | 17.75 | 1.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 3.9 | 0.21 | 0.47 | 0.68 | 0.00 | 6.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.31 | 12.07 | 19.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.01 | 11.70 | 19.38 | 1.00 | 85.8 | 90.0 |
| Bench 3 | Bench Boost | Reece James | DEF | 7 | 5.7 | 2.44 | 8.72 | 15.05 | 1.00 | 64.8 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.95 | 8.06 | 13.28 | 4.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.81 | 7.85 | 12.17 | 2.00 | 78.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.06 | 23.81 | 39.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.59 | 14.26 | 23.45 | 0.00 | 67.1 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 1.06 | 3.55 | 5.65 | 5.00 | 25.1 | 16.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.77 | 17.60 | 28.93 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.82 | 16.68 | 26.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.27 | 15.32 | 24.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.95 | 15.14 | 24.34 | 4.00 | 73.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.16 | 11.47 | 18.69 | 4.00 | 81.0 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.00 -> 3.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.34
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.90) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.89, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.90) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.44 | 9.97 | 16.36 | 6.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 3.9 | 0.42 | 0.57 | 0.80 | 0.00 | 4.9 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 11.91 | 19.12 | 6.00 | 89.7 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.61 | 10.57 | 17.13 | 1.00 | 79.5 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.34 | 10.49 | 17.58 | 6.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.09 | 8.47 | 14.09 | 3.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.49 | 7.33 | 11.71 | 0.00 | 75.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.90 | 23.43 | 38.31 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.47 | 15.28 | 24.41 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.33 | 4.11 | 6.78 | 7.00 | 27.0 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.44 | 15.89 | 26.64 | 2.00 | 82.4 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.09 | 14.88 | 23.77 | 1.00 | 81.9 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.18 | 14.51 | 23.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.81 | 13.97 | 22.49 | 3.00 | 75.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.91 | 10.96 | 18.34 | 2.00 | 80.0 | 79.0 |
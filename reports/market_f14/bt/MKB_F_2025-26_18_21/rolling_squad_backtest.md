# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 264.84
- Total actual points: 175.00
- Average predicted points: 66.21
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
- Predicted score: 67.48
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.95 | 11.23 | 18.19 | 2.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.04 | 13.75 | 21.58 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 4.60 | 12.64 | 20.17 | 0.00 | 86.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.21 | 11.97 | 19.08 | 2.00 | 81.6 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.71 | 8.07 | 12.53 | 2.00 | 68.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.66 | 7.83 | 12.44 | 2.00 | 70.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.33 | 24.57 | 40.67 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.02 | 18.78 | 28.07 | 5.00 | 90.0 | 85.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.44 | 4.40 | 7.43 | 1.00 | 29.2 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.69 | 17.90 | 28.74 | 2.00 | 82.8 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.76 | 16.41 | 25.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.55 | 16.05 | 25.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.26 | 15.43 | 24.39 | 9.00 | 83.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.77 | 11.30 | 17.85 | 4.00 | 77.7 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.84
- Actual score: 38.00
- Transfer: Jurriën Timber -> Reece James (projected gain 4.38, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 10.81 | 17.53 | 2.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.20 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.65 | 12.76 | 20.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 4.36 | 12.05 | 18.96 | 1.00 | 85.6 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.19 | 12.03 | 19.74 | 6.00 | 83.0 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.52 | 7.71 | 12.55 | 7.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.44 | 7.57 | 12.31 | 8.00 | 71.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.04 | 23.85 | 39.75 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.48 | 13.55 | 20.98 | 2.00 | 54.7 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.78 | 5.36 | 8.71 | 0.00 | 42.5 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.39 | 16.75 | 27.96 | 3.00 | 82.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.05 | 14.91 | 24.04 | 5.00 | 85.0 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.38 | 13.14 | 21.30 | 0.00 | 70.4 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.78 | 12.84 | 20.86 | 1.00 | 73.3 | 81.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.67 | 11.31 | 18.38 | 5.00 | 76.5 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.70 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.56
- Actual score: 36.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.26) beats the best remaining Bench Boost opportunity (7.43).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.26) beats the best remaining Bench Boost opportunity (7.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 11.56 | 18.56 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.42 | 12.40 | 19.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.07 | 11.85 | 19.57 | 1.00 | 86.2 | 90.0 |
| Bench 3 | Bench Boost | Reece James | DEF | 7 | 5.7 | 2.43 | 8.71 | 15.03 | 1.00 | 64.9 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.97 | 8.06 | 13.26 | 4.00 | 75.0 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.85 | 7.96 | 12.35 | 2.00 | 79.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.17 | 24.20 | 40.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.65 | 14.35 | 23.49 | 0.00 | 68.0 | 0.0 |
| Bench 4 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 0.97 | 3.36 | 5.35 | 5.00 | 24.1 | 16.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.79 | 17.70 | 29.10 | 2.00 | 88.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.85 | 16.72 | 26.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.21 | 15.18 | 24.34 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 4.88 | 14.95 | 24.03 | 4.00 | 74.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 4.12 | 11.35 | 18.52 | 4.00 | 81.1 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.00 -> 3.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 68.96
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.51, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.55 | 10.21 | 16.66 | 6.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.09 | 0.06 | 0.09 | 0.00 | 2.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.48 | 12.24 | 19.64 | 6.00 | 90.0 | 90.0 |
| XI | XI | Reece James | DEF | 7 | 5.7 | 3.67 | 10.70 | 17.28 | 1.00 | 80.1 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.32 | 10.45 | 17.52 | 6.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.06 | 8.40 | 14.00 | 3.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.50 | 7.38 | 11.84 | 0.00 | 76.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.00 | 23.80 | 38.89 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.71 | 15.81 | 25.18 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.40 | 4.30 | 7.02 | 7.00 | 27.8 | 63.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.45 | 15.95 | 26.72 | 2.00 | 83.0 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.06 | 14.81 | 23.65 | 1.00 | 83.6 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.16 | 14.51 | 23.70 | 6.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.74 | 13.75 | 22.14 | 3.00 | 76.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 4.8 | 3.84 | 10.78 | 18.10 | 2.00 | 81.2 | 79.0 |
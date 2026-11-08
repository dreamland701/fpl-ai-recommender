# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 266.77
- Total actual points: 180.00
- Average predicted points: 66.69
- Average actual points: 45.00
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
- Predicted score: 69.71
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaka Bijol replaced Jurriën Timber.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.40 | 11.87 | 19.07 | 2.00 | 97.1 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.74 | 14.59 | 22.69 | 2.00 | 108.0 | 90.0 |
| XI | Bench | Jurriën Timber | DEF | 1 | 6.5 | 5.29 | 13.25 | 20.84 | 0.00 | 96.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.80 | 11.34 | 18.06 | 2.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.96 | 8.28 | 12.72 | 2.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.90 | 7.96 | 12.54 | 2.00 | 71.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.13 | 24.30 | 40.14 | 2.00 | 114.1 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 7.27 | 18.39 | 27.38 | 5.00 | 93.8 | 85.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.02 | 0.14 | 0.18 | 0.00 | 0.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.83 | 17.92 | 28.61 | 2.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 6.39 | 16.95 | 26.42 | 5.00 | 106.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.12 | 15.41 | 24.67 | 1.00 | 98.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.64 | 14.81 | 23.79 | 9.00 | 76.6 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.95 | 12.47 | 19.66 | 11.00 | 94.4 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.93
- Actual score: 40.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 5.39, hit 0)
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.23 | 11.33 | 18.18 | 2.00 | 91.4 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.73 | 12.65 | 20.46 | 6.00 | 90.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.63 | 20.21 | 2.00 | 89.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.42 | 10.90 | 17.32 | 3.00 | 84.1 | 90.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.09 | 7.24 | 12.03 | 7.00 | 64.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.97 | 7.09 | 11.83 | 8.00 | 66.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.36 | 23.93 | 39.52 | 2.00 | 119.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.72 | 13.55 | 20.78 | 2.00 | 54.7 | 90.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.10 | 0.18 | 0.27 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.92 | 17.27 | 28.33 | 3.00 | 86.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.07 | 14.22 | 23.45 | 5.00 | 74.6 | 90.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.88 | 13.73 | 21.92 | 0.00 | 76.3 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.10 | 12.32 | 20.60 | 1.00 | 66.9 | 81.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.60 | 11.86 | 19.02 | 5.00 | 87.5 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 1.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.43
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.99) beats the best remaining Bench Boost opportunity (7.09).
- Transfer: Declan Rice -> Rayan Cherki (projected gain 7.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.99) beats the best remaining Bench Boost opportunity (7.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.25 | 11.87 | 18.98 | 1.00 | 97.3 | 90.0 |
| Bench 1 | Bench Boost | Dermot Mee | GK | 14 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 2.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.33 | 12.10 | 19.81 | 1.00 | 88.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 3.80 | 11.86 | 19.32 | 2.00 | 88.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.59 | 10.97 | 18.36 | 1.00 | 82.8 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.92 | 8.03 | 12.44 | 2.00 | 79.4 | 90.0 |
| Bench 2 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 2.93 | 7.97 | 13.12 | 4.00 | 73.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.02 | 23.98 | 39.62 | 2.00 | 113.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.82 | 14.50 | 23.60 | 0.00 | 68.9 | 0.0 |
| Bench 4 | Bench Boost | Chido Obi | FWD | 14 | 4.2 | 0.14 | 0.42 | 0.74 | 0.00 | 3.8 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.9 | 6.01 | 17.86 | 29.08 | 2.00 | 91.4 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 5.90 | 16.50 | 26.11 | 5.00 | 98.8 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.14 | 14.99 | 23.76 | 4.00 | 76.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.42 | 14.53 | 23.77 | 1.00 | 84.7 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.13 | 11.49 | 18.92 | 2.00 | 83.9 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 1.40 -> 3.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.70
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.91) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 6.15, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.91) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 10.66 | 17.22 | 6.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Dermot Mee | GK | 14 | 3.9 | 0.01 | 0.00 | 0.00 | 0.00 | 0.7 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.20 | 12.04 | 19.47 | 6.00 | 88.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 3.88 | 9.92 | 17.23 | 6.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 5.9 | 2.66 | 9.77 | 16.70 | 6.00 | 75.2 | 90.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 2.69 | 8.00 | 13.55 | 3.00 | 74.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.15 | 7.02 | 11.46 | 0.00 | 71.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.91 | 23.67 | 38.58 | 6.00 | 112.2 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 6.05 | 15.81 | 25.05 | 12.00 | 107.9 | 81.0 |
| Bench 4 | Bench | Chido Obi | FWD | 14 | 4.2 | 0.17 | 0.48 | 0.87 | 0.00 | 1.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.62 | 16.17 | 26.89 | 2.00 | 86.4 | 72.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.8 | 5.41 | 15.05 | 23.83 | 1.00 | 88.8 | 17.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.16 | 14.59 | 23.81 | 6.00 | 92.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.21 | 13.25 | 21.73 | 3.00 | 68.8 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 2.87 | 10.36 | 17.08 | 3.00 | 74.1 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW17
- Simulated weeks: GW18-GW21
- Total predicted points: 263.07
- Total actual points: 200.00
- Average predicted points: 65.77
- Average actual points: 50.00
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
- Predicted score: 66.60
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.81 | 10.98 | 18.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.21 | 0.28 | 0.58 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.02 | 13.82 | 21.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.16 | 12.02 | 19.41 | 2.00 | 83.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.83 | 11.42 | 19.06 | 8.00 | 81.5 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 2.52 | 7.65 | 11.98 | 2.00 | 63.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.43 | 7.33 | 11.82 | 2.00 | 64.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 24.33 | 40.41 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 6.72 | 18.16 | 27.30 | 5.00 | 82.9 | 85.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.78 | 2.06 | 3.29 | 0.00 | 14.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 9.0 | 5.57 | 17.55 | 28.29 | 2.00 | 78.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 5.64 | 16.41 | 25.92 | 1.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 5.69 | 16.31 | 25.80 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.32 | 15.78 | 25.18 | 9.00 | 86.0 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.29 | 11.88 | 19.19 | 11.00 | 84.6 | 90.0 |

## GW19

- Train rows: 174672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.30
- Actual score: 38.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Jaka Bijol replaced Declan Rice.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.67 | 10.56 | 17.43 | 2.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.00 | 0.17 | 0.52 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.52 | 12.62 | 20.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.16 | 12.14 | 20.17 | 6.00 | 85.4 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 4.01 | 11.73 | 19.34 | 1.00 | 88.3 | 33.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.40 | 7.48 | 12.27 | 7.00 | 64.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.31 | 7.30 | 11.96 | 8.00 | 65.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.90 | 23.40 | 39.16 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.33 | 13.28 | 20.72 | 2.00 | 52.1 | 90.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.52 | 1.63 | 2.66 | 0.00 | 8.2 | 0.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 9.0 | 5.27 | 16.39 | 27.47 | 3.00 | 78.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.16 | 15.38 | 24.95 | 5.00 | 88.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.93 | 13.38 | 21.86 | 1.00 | 77.7 | 81.0 |
| XI | Bench | Declan Rice | MID | 1 | 7.2 | 4.42 | 13.30 | 21.72 | 0.00 | 74.6 | 0.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 4.03 | 11.51 | 19.03 | 5.00 | 84.1 | 90.0 |

## GW20

- Train rows: 175452
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 69.36
- Actual score: 35.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.20) beats the best remaining Bench Boost opportunity (7.31).
- Transfer: Declan Rice -> Bruno Guimarães Rodriguez Moura (projected gain 6.55, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.20) beats the best remaining Bench Boost opportunity (7.31).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.32 | 18.32 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.21 | 0.67 | 1.01 | 0.00 | 9.8 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.63 | 20.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.13 | 12.09 | 20.02 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 6.0 | 3.84 | 11.47 | 18.79 | 1.00 | 70.1 | 50.0 |
| Bench 2 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 2.90 | 7.86 | 12.87 | 4.00 | 71.7 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.79 | 7.74 | 11.93 | 2.00 | 75.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.18 | 23.99 | 39.63 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 9.0 | 4.52 | 14.01 | 22.96 | 0.00 | 65.5 | 0.0 |
| Bench 4 | Bench Boost | Marc Guiu Paz | FWD | 7 | 4.3 | 0.30 | 1.50 | 2.51 | 0.00 | 11.3 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.9 | 5.80 | 17.48 | 28.57 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.4 | 5.84 | 16.82 | 26.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.39 | 15.73 | 25.22 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 5.07 | 14.39 | 23.17 | 10.00 | 90.0 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.86 | 11.43 | 19.06 | 2.00 | 85.5 | 90.0 |

## GW21

- Train rows: 176242
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.81
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Igor Thiago Nascimento Rodrigues (projected gain 7.15, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.94) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Jaka Bijol replaced Joško Gvardiol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.13 | 16.81 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Blondy Nna Noukeu | GK | 17 | 3.9 | 0.06 | 0.41 | 0.77 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.3 | 4.45 | 12.30 | 19.95 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 3.38 | 10.71 | 18.11 | 6.00 | 86.9 | 90.0 |
| XI | Bench | Joško Gvardiol | DEF | 13 | 6.0 | 3.27 | 9.85 | 16.93 | 0.00 | 62.1 | 0.0 |
| Bench 2 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 2.95 | 8.06 | 13.48 | 3.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.40 | 7.10 | 11.44 | 0.00 | 70.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.94 | 23.51 | 38.51 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.0 | 5.47 | 15.13 | 24.13 | 12.00 | 90.0 | 81.0 |
| Bench 4 | Bench | Marc Guiu Paz | FWD | 7 | 4.3 | 0.37 | 1.11 | 2.00 | 0.00 | 8.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.8 | 5.39 | 15.65 | 26.26 | 2.00 | 77.4 | 72.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.21 | 14.72 | 24.17 | 6.00 | 90.0 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.0 | 5.05 | 14.54 | 23.71 | 11.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.78 | 14.04 | 22.79 | 3.00 | 78.7 | 90.0 |
| XI | XI | Ryan Gravenberch | MID | 12 | 5.6 | 3.53 | 11.22 | 18.33 | 3.00 | 84.7 | 90.0 |
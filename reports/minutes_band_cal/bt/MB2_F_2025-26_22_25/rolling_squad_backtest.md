# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 257.42
- Total actual points: 213.00
- Average predicted points: 64.36
- Average actual points: 53.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW21 are included before the first simulated week.
- League-average scores were not available for this run.

## GW22

- Train rows: 177037
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.75
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 3.50 | 9.29 | 14.91 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.31 | 0.36 | 0.58 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.96 | 13.76 | 19.82 | 8.00 | 79.1 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.46 | 12.48 | 19.38 | 5.00 | 83.2 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 4.10 | 11.42 | 19.14 | 1.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.35 | 9.26 | 14.90 | 1.00 | 79.8 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.37 | 9.24 | 14.06 | 0.00 | 81.8 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.87 | 23.00 | 37.69 | 2.00 | 83.4 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.55 | 15.02 | 23.56 | 2.00 | 82.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.00 | 8.33 | 12.65 | 2.00 | 71.9 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.24 | 14.55 | 23.38 | 3.00 | 83.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.22 | 14.54 | 23.63 | 10.00 | 78.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.00 | 14.43 | 23.79 | 2.00 | 81.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.95 | 14.42 | 23.47 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.02 | 14.21 | 23.65 | 3.00 | 78.3 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.67
- Actual score: 31.00
- Transfer: Nathan Collins -> Nordi Mukiele (projected gain 0.52, hit 0)
- Autosub: Omar Alderete replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.63 | 8.04 | 13.49 | 1.00 | 75.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.01 | 0.29 | 0.00 | 5.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.60 | 13.35 | 20.01 | 1.00 | 79.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.30 | 12.15 | 18.93 | 1.00 | 83.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 4.09 | 11.15 | 17.65 | 4.00 | 82.1 | 82.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.00 | 8.71 | 14.80 | 1.00 | 76.4 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.81 | 5.58 | 9.14 | 0.00 | 43.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.92 | 21.68 | 35.92 | 1.00 | 83.4 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.31 | 14.35 | 23.01 | 2.00 | 82.4 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.63 | 8.16 | 13.12 | 2.00 | 73.3 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.24 | 14.83 | 24.18 | 2.00 | 79.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.24 | 14.47 | 23.22 | 8.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.00 | 14.45 | 22.62 | 1.00 | 83.4 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.70 | 13.67 | 22.46 | 0.00 | 79.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.71 | 13.48 | 22.04 | 8.00 | 78.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.38
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.34).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 5.19, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.81 | 8.19 | 13.72 | 2.00 | 78.6 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.04 | 0.13 | 0.27 | 0.00 | 3.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.56 | 12.99 | 20.69 | 8.00 | 80.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.02 | 11.68 | 19.04 | 5.00 | 80.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 4.20 | 11.13 | 17.68 | 9.00 | 79.2 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.39 | 8.92 | 14.51 | 6.00 | 79.3 | 85.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.04 | 3.62 | 7.22 | 0.00 | 26.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.73 | 20.10 | 34.17 | 5.00 | 79.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.50 | 21.93 | 2.00 | 80.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.04 | 8.24 | 13.65 | 2.00 | 70.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.47 | 15.46 | 24.96 | 7.00 | 83.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.10 | 14.99 | 23.77 | 3.00 | 83.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.08 | 14.17 | 22.80 | 2.00 | 83.5 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.14 | 14.02 | 22.29 | 8.00 | 79.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.42 | 13.31 | 22.49 | 12.00 | 74.5 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.62
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.30) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaka Bijol -> Marcos Senesi Barón (projected gain 0.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.30) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.60 | 7.85 | 12.87 | 1.00 | 75.9 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.09 | 13.94 | 22.21 | 6.00 | 82.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.45 | 12.20 | 19.71 | 6.00 | 79.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.01 | 11.17 | 17.84 | 2.00 | 83.6 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 3.59 | 11.00 | 17.98 | 1.00 | 78.6 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.70 | 8.30 | 13.35 | 1.00 | 78.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.25 | 19.18 | 32.78 | 11.00 | 83.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.92 | 12.64 | 20.95 | 5.00 | 74.9 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.01 | 8.78 | 14.38 | 2.00 | 72.5 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.42 | 15.32 | 24.71 | 5.00 | 83.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.04 | 15.15 | 25.01 | 2.00 | 83.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.92 | 14.54 | 23.96 | 2.00 | 83.4 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.63 | 13.87 | 22.21 | 2.00 | 77.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.74 | 13.66 | 21.91 | 10.00 | 78.9 | 90.0 |
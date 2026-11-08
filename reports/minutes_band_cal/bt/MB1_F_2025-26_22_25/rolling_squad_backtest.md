# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 257.32
- Total actual points: 213.00
- Average predicted points: 64.33
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
- Predicted score: 63.85
- Actual score: 42.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 3.59 | 9.43 | 15.10 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.28 | 0.28 | 0.49 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.99 | 13.76 | 19.73 | 8.00 | 80.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.54 | 12.62 | 19.57 | 5.00 | 84.3 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 5.0 | 4.19 | 11.56 | 19.33 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.44 | 9.41 | 15.09 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.46 | 9.38 | 14.25 | 0.00 | 82.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.77 | 22.70 | 37.34 | 2.00 | 83.1 | 79.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.63 | 15.17 | 23.76 | 2.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.01 | 8.35 | 12.69 | 2.00 | 71.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.09 | 14.57 | 23.98 | 2.00 | 82.7 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.25 | 14.54 | 23.55 | 10.00 | 79.1 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.13 | 14.25 | 23.02 | 3.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.05 | 14.20 | 23.56 | 3.00 | 79.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 4.85 | 14.12 | 23.11 | 2.00 | 83.1 | 90.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Florian Wirtz
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.52
- Actual score: 31.00
- Transfer: Nathan Collins -> Nordi Mukiele (projected gain 0.52, hit 0)
- Autosub: Omar Alderete replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.67 | 8.05 | 13.42 | 1.00 | 76.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.20 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.64 | 13.36 | 19.94 | 1.00 | 81.0 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.38 | 12.30 | 19.13 | 1.00 | 84.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 4.16 | 11.30 | 17.85 | 4.00 | 83.1 | 82.0 |
| Bench 2 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.04 | 8.71 | 14.73 | 1.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.77 | 5.50 | 9.04 | 0.00 | 43.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.82 | 21.37 | 35.55 | 1.00 | 83.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.20 | 14.04 | 22.64 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.64 | 8.18 | 13.16 | 2.00 | 73.1 | 90.0 |
| Vice Captain | XI | Florian Wirtz | MID | 12 | 8.2 | 5.32 | 14.98 | 24.38 | 2.00 | 80.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.13 | 14.16 | 22.86 | 8.00 | 83.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 4.89 | 14.14 | 22.25 | 1.00 | 83.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.74 | 13.67 | 22.39 | 0.00 | 80.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.74 | 13.48 | 21.97 | 8.00 | 79.9 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.35
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.37).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 5.37, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.77) beats the best remaining Triple Captain opportunity (7.37).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.85 | 8.19 | 13.66 | 2.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.01 | 0.05 | 0.18 | 0.00 | 2.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.46 | 12.70 | 20.33 | 8.00 | 79.8 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.05 | 11.68 | 18.97 | 5.00 | 81.4 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 4.28 | 11.29 | 17.90 | 9.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.42 | 8.92 | 14.45 | 6.00 | 80.5 | 85.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.00 | 3.54 | 7.13 | 0.00 | 26.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.77 | 20.10 | 34.11 | 5.00 | 80.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.41 | 13.50 | 21.87 | 2.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.06 | 8.26 | 13.68 | 2.00 | 70.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.37 | 15.16 | 24.60 | 7.00 | 83.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.00 | 14.70 | 23.41 | 3.00 | 83.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.23 | 14.19 | 22.51 | 8.00 | 80.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 13.87 | 22.43 | 2.00 | 83.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.43 | 13.34 | 22.53 | 12.00 | 74.4 | 86.0 |

## GW25

- Train rows: 179450
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.60
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.43) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jaka Bijol -> Marcos Senesi Barón (projected gain 0.38, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.43) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Becker | GK | 12 | 5.4 | 2.64 | 7.88 | 12.81 | 1.00 | 77.1 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.99 | 13.64 | 21.86 | 6.00 | 81.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.49 | 12.23 | 19.66 | 6.00 | 80.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.09 | 11.33 | 18.05 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 3.67 | 11.15 | 18.20 | 1.00 | 79.7 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.74 | 8.33 | 13.30 | 1.00 | 79.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.15 | 18.89 | 32.44 | 11.00 | 83.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.92 | 12.66 | 20.96 | 5.00 | 74.8 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.02 | 8.79 | 14.40 | 2.00 | 72.3 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.12 | 15.30 | 25.22 | 2.00 | 84.9 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.32 | 15.03 | 24.36 | 5.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.82 | 14.24 | 23.61 | 2.00 | 83.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.68 | 13.90 | 22.16 | 2.00 | 78.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.82 | 13.82 | 22.13 | 10.00 | 80.0 | 90.0 |
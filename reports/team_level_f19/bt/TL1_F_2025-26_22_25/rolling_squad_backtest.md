# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.61
- Total actual points: 225.00
- Average predicted points: 66.15
- Average actual points: 56.25
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.60
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nathan Collins replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.64 | 10.52 | 17.29 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.08 | 0.00 | 4.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.90 | 13.55 | 19.57 | 8.00 | 78.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.57 | 12.89 | 20.55 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.71 | 20.08 | 8.00 | 87.0 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 5.0 | 4.08 | 11.46 | 19.40 | 1.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.22 | 8.95 | 14.53 | 1.00 | 82.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.24 | 24.19 | 39.34 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.54 | 15.12 | 23.88 | 2.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.99 | 8.33 | 12.67 | 2.00 | 68.6 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.63 | 15.74 | 25.19 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.31 | 15.59 | 25.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.29 | 14.69 | 23.74 | 10.00 | 76.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.95 | 14.42 | 23.97 | 2.00 | 83.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 5.00 | 14.14 | 22.64 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.32
- Actual score: 50.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.44, hit 0)
- Autosub: Nathan Collins replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.77 | 10.76 | 17.44 | 1.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.38 | 0.27 | 0.58 | 0.00 | 5.5 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.96 | 13.52 | 21.79 | 4.00 | 89.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.55 | 13.26 | 19.81 | 1.00 | 79.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.32 | 11.92 | 18.07 | 11.00 | 88.2 | 90.0 |
| Bench 2 | Autosub In | Nathan Collins | DEF | 5 | 5.0 | 3.75 | 10.59 | 17.69 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.86 | 8.27 | 14.12 | 1.00 | 76.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 22.68 | 37.48 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.73 | 15.58 | 24.84 | 2.00 | 88.9 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.64 | 8.27 | 13.20 | 2.00 | 69.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.59 | 15.44 | 24.73 | 8.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.20 | 14.89 | 24.45 | 2.00 | 80.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.71 | 13.72 | 22.49 | 0.00 | 79.1 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.70 | 13.41 | 21.98 | 8.00 | 78.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.22 | 12.02 | 20.02 | 10.00 | 75.3 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.57
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.68) beats the best remaining Triple Captain opportunity (7.33).
- Transfer: Bruno Guimarães Rodriguez Moura -> Declan Rice (projected gain 7.68, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.68) beats the best remaining Triple Captain opportunity (7.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 10.92 | 17.52 | 6.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.05 | 0.14 | 0.00 | 4.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.99 | 14.26 | 22.39 | 8.00 | 86.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.95 | 19.67 | 2.00 | 82.0 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.81 | 11.29 | 17.92 | 0.00 | 87.7 | 45.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 5.0 | 2.86 | 9.20 | 15.61 | 1.00 | 79.8 | 30.0 |
| Bench 2 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.33 | 8.69 | 14.01 | 6.00 | 79.2 | 85.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.68 | 19.98 | 33.96 | 5.00 | 79.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.56 | 21.98 | 2.00 | 79.5 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.5 | 3.03 | 8.22 | 13.67 | 2.00 | 67.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.83 | 16.54 | 26.52 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.55 | 16.30 | 25.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.48 | 15.33 | 24.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.35 | 13.11 | 22.22 | 12.00 | 70.3 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.30 | 12.91 | 21.09 | 2.00 | 86.4 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 68.13
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Marcos Senesi Barón (projected gain 3.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.17 | 11.47 | 18.12 | 7.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.53 | 15.23 | 23.90 | 6.00 | 88.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.78 | 19.39 | 2.00 | 82.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.01 | 11.32 | 18.20 | 2.00 | 85.2 | 90.0 |
| Bench 3 | Bench Boost | Nathan Collins | DEF | 5 | 5.0 | 2.63 | 8.27 | 14.44 | 0.00 | 60.3 | 0.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.62 | 8.03 | 12.80 | 1.00 | 78.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.64 | 20.20 | 34.32 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.84 | 12.44 | 20.63 | 5.00 | 71.4 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 3.01 | 8.82 | 14.45 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.87 | 16.63 | 26.43 | 5.00 | 89.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.32 | 15.57 | 25.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.04 | 15.31 | 25.36 | 2.00 | 84.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.70 | 13.66 | 22.09 | 10.00 | 80.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.05 | 11.91 | 19.07 | 2.00 | 79.6 | 90.0 |
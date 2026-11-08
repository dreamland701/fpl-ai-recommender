# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 261.85
- Total actual points: 225.00
- Average predicted points: 65.46
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
- Predicted score: 65.47
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.68 | 10.71 | 17.49 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.34 | 0.41 | 0.63 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.95 | 13.74 | 19.77 | 8.00 | 77.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.64 | 20.35 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.63 | 19.96 | 8.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.15 | 10.94 | 17.40 | 0.00 | 81.0 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.35 | 9.27 | 14.28 | 0.00 | 83.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.27 | 39.51 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.53 | 15.05 | 23.78 | 2.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.00 | 12.41 | 19.57 | 2.00 | 74.2 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.66 | 15.83 | 25.19 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.37 | 15.70 | 25.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.98 | 14.46 | 24.00 | 2.00 | 82.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.01 | 14.19 | 23.60 | 3.00 | 77.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.92 | 13.91 | 22.43 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.71
- Actual score: 55.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.64, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 10.85 | 17.60 | 1.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.07 | 0.34 | 0.00 | 5.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.60 | 13.33 | 19.96 | 1.00 | 78.9 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.88 | 13.32 | 21.58 | 4.00 | 89.5 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.26 | 11.78 | 17.93 | 11.00 | 88.3 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.67 | 10.19 | 16.77 | 7.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.84 | 5.63 | 9.19 | 0.00 | 46.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 22.94 | 37.72 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.74 | 15.61 | 24.81 | 2.00 | 89.0 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.57 | 10.93 | 17.33 | 2.00 | 70.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.67 | 15.73 | 25.03 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.43 | 15.71 | 24.42 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.70 | 13.65 | 22.41 | 0.00 | 81.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.70 | 13.46 | 21.99 | 8.00 | 76.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.21 | 11.97 | 19.90 | 10.00 | 74.6 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.48
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.33).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.99, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (7.33).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.84 | 10.87 | 17.58 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.19 | 0.33 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.20 | 22.45 | 8.00 | 86.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.92 | 19.59 | 2.00 | 79.7 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.79 | 11.22 | 17.85 | 0.00 | 87.8 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.21 | 9.65 | 16.19 | 0.00 | 85.6 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.07 | 3.68 | 7.29 | 0.00 | 29.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.73 | 20.09 | 34.13 | 5.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.49 | 21.89 | 2.00 | 79.7 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.46 | 10.17 | 16.67 | 2.00 | 70.6 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.88 | 16.67 | 26.71 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.20 | 25.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 15.38 | 24.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.12 | 14.08 | 22.51 | 8.00 | 80.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.31 | 12.83 | 20.99 | 2.00 | 86.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.19
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.44) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 5.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.44) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 11.39 | 18.16 | 7.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.02 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.50 | 15.14 | 23.94 | 6.00 | 88.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.31 | 12.12 | 19.03 | 4.00 | 83.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 11.75 | 19.33 | 2.00 | 79.3 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.31 | 5.02 | 9.23 | 1.00 | 37.5 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.11 | 0.68 | 3.08 | 0.00 | 3.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.66 | 20.39 | 34.51 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.83 | 12.43 | 20.59 | 5.00 | 71.6 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.01 | 9.21 | 15.52 | 7.00 | 61.6 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.84 | 16.53 | 26.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.34 | 15.74 | 25.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.63 | 13.87 | 22.18 | 2.00 | 76.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.71 | 13.71 | 22.12 | 10.00 | 79.5 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.06 | 11.88 | 19.00 | 2.00 | 78.5 | 90.0 |
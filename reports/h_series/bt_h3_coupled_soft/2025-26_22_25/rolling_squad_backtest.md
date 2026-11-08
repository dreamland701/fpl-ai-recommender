# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 263.12
- Total actual points: 220.00
- Average predicted points: 65.78
- Average actual points: 55.00
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
- Predicted score: 65.64
- Actual score: 40.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.68 | 10.71 | 17.49 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.34 | 0.41 | 0.63 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.96 | 13.74 | 19.77 | 8.00 | 78.7 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.49 | 12.64 | 20.35 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.29 | 12.63 | 19.96 | 8.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.15 | 10.95 | 17.40 | 0.00 | 82.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.33 | 9.25 | 14.26 | 0.00 | 83.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 24.27 | 39.51 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.57 | 15.09 | 23.82 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.10 | 12.51 | 19.67 | 2.00 | 76.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.66 | 15.83 | 25.19 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.37 | 15.70 | 25.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.02 | 14.49 | 24.04 | 2.00 | 83.4 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.11 | 14.28 | 23.69 | 3.00 | 77.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.92 | 13.91 | 22.43 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.10 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.91
- Actual score: 50.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 1.70, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.82 | 10.85 | 17.60 | 1.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.07 | 0.34 | 0.00 | 5.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.61 | 13.34 | 19.96 | 1.00 | 79.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.88 | 13.32 | 21.58 | 4.00 | 89.5 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.26 | 11.78 | 17.93 | 11.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.66 | 10.19 | 16.77 | 7.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.55 | 5.33 | 8.90 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.35 | 22.94 | 37.72 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.74 | 15.61 | 24.81 | 2.00 | 89.0 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.69 | 11.06 | 17.45 | 2.00 | 72.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.67 | 15.73 | 25.03 | 8.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.43 | 15.71 | 24.42 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.76 | 13.71 | 22.47 | 0.00 | 79.3 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.76 | 13.52 | 22.05 | 8.00 | 78.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.27 | 12.03 | 19.97 | 10.00 | 75.2 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.30 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.97
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.86) beats the best remaining Triple Captain opportunity (7.47).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.97, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.86) beats the best remaining Triple Captain opportunity (7.47).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 10.84 | 17.55 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.08 | 0.19 | 0.33 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.20 | 22.45 | 8.00 | 86.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.00 | 11.92 | 19.59 | 2.00 | 81.9 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.79 | 11.22 | 17.85 | 0.00 | 87.8 | 45.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 2.90 | 9.34 | 15.88 | 0.00 | 85.3 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.51 | 3.04 | 6.53 | 0.00 | 27.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.86 | 20.22 | 34.27 | 5.00 | 79.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.44 | 13.56 | 21.96 | 2.00 | 79.6 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.58 | 10.29 | 16.78 | 2.00 | 72.0 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.88 | 16.67 | 26.71 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.52 | 16.20 | 25.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.50 | 15.38 | 24.55 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.18 | 14.13 | 22.56 | 8.00 | 81.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.31 | 12.83 | 20.99 | 2.00 | 86.3 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 64.60
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.44) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 6.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.44) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 11.38 | 18.14 | 7.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.00 | 0.02 | 0.00 | 1.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.50 | 15.14 | 23.94 | 6.00 | 88.8 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.32 | 12.13 | 19.04 | 4.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.07 | 11.76 | 19.33 | 2.00 | 82.0 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.14 | 4.80 | 8.99 | 1.00 | 38.5 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.11 | 0.68 | 3.08 | 0.00 | 3.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.66 | 20.39 | 34.51 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.99 | 12.60 | 20.76 | 5.00 | 71.5 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.18 | 9.38 | 15.70 | 7.00 | 63.6 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.84 | 16.53 | 26.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.34 | 15.74 | 25.69 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.74 | 13.98 | 22.29 | 2.00 | 77.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.79 | 13.79 | 22.20 | 10.00 | 80.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.13 | 11.94 | 19.07 | 2.00 | 79.5 | 90.0 |
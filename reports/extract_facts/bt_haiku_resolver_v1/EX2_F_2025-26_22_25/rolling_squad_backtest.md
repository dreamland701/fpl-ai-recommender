# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 263.08
- Total actual points: 228.00
- Average predicted points: 65.77
- Average actual points: 57.00
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
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 66.21
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Omar Alderete replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.74 | 10.82 | 17.58 | 6.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.45 | 0.60 | 0.81 | 0.00 | 6.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.88 | 13.60 | 19.52 | 8.00 | 77.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.54 | 12.74 | 20.41 | 0.00 | 90.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.33 | 12.70 | 19.97 | 8.00 | 87.9 | 90.0 |
| Bench 4 | Autosub In | Omar Alderete | DEF | 17 | 4.1 | 3.38 | 9.36 | 15.14 | 1.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.39 | 9.33 | 14.29 | 0.00 | 84.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.30 | 24.32 | 39.46 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.54 | 15.04 | 23.64 | 2.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.03 | 12.46 | 19.57 | 2.00 | 76.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.64 | 15.78 | 25.03 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.3 | 5.78 | 15.66 | 25.42 | 3.00 | 85.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.25 | 14.59 | 23.60 | 10.00 | 78.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.01 | 14.53 | 24.02 | 2.00 | 83.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.90 | 13.87 | 22.31 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.70
- Actual score: 44.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 3.44, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 10.84 | 17.63 | 1.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.10 | 0.44 | 0.00 | 6.3 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.83 | 13.22 | 21.51 | 4.00 | 87.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.53 | 13.22 | 19.86 | 1.00 | 77.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.19 | 11.65 | 17.83 | 11.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 2.96 | 8.63 | 14.74 | 1.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.86 | 5.65 | 9.27 | 0.00 | 44.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.29 | 22.87 | 37.65 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.67 | 15.49 | 24.66 | 2.00 | 87.1 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.52 | 10.87 | 17.31 | 2.00 | 70.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.35 | 15.58 | 24.29 | 1.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.18 | 14.84 | 24.40 | 2.00 | 79.3 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.70 | 13.70 | 22.51 | 0.00 | 78.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.69 | 13.48 | 22.06 | 8.00 | 77.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.17 | 11.92 | 19.88 | 10.00 | 73.8 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Morgan Rogers
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 66.57
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.83) beats the best remaining Triple Captain opportunity (7.45).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.77, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.83) beats the best remaining Triple Captain opportunity (7.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.89 | 10.98 | 17.65 | 6.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.18 | 0.36 | 0.49 | 0.00 | 7.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.98 | 14.21 | 22.39 | 8.00 | 87.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.06 | 12.04 | 19.67 | 2.00 | 83.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.82 | 11.27 | 17.85 | 0.00 | 88.4 | 45.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 3.43 | 8.98 | 14.52 | 6.00 | 80.2 | 85.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 0.76 | 2.97 | 6.41 | 0.00 | 21.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.83 | 20.34 | 34.34 | 5.00 | 81.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.45 | 13.67 | 22.03 | 2.00 | 81.3 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.53 | 10.32 | 16.79 | 2.00 | 73.3 | 84.0 |
| XI | XI | Declan Rice | MID | 1 | 7.3 | 5.51 | 16.19 | 25.45 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Morgan Rogers | MID | 2 | 7.7 | 5.53 | 15.46 | 24.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.10 | 14.03 | 22.37 | 8.00 | 81.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.40 | 13.25 | 22.28 | 12.00 | 72.2 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.33 | 12.87 | 20.99 | 2.00 | 86.8 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.60
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Trevoh Chalobah (projected gain 3.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.18 | 11.48 | 18.21 | 7.00 | 86.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.16 | 0.18 | 0.00 | 4.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.53 | 15.18 | 23.91 | 6.00 | 89.4 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.34 | 12.18 | 19.01 | 4.00 | 85.6 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.12 | 11.87 | 19.41 | 2.00 | 83.3 | 90.0 |
| Bench 3 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 2.76 | 8.40 | 13.39 | 1.00 | 79.6 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.21 | 0.86 | 3.35 | 0.00 | 5.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.78 | 20.69 | 34.79 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.99 | 12.79 | 20.97 | 5.00 | 74.7 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.04 | 9.28 | 15.68 | 7.00 | 63.4 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 6.29 | 17.51 | 28.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.04 | 15.25 | 25.23 | 2.00 | 86.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.78 | 13.87 | 22.25 | 10.00 | 82.1 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.63 | 13.85 | 22.09 | 2.00 | 77.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.11 | 11.97 | 19.06 | 2.00 | 80.7 | 90.0 |
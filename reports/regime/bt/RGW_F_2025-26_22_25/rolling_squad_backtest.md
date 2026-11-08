# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 256.89
- Total actual points: 236.00
- Average predicted points: 64.22
- Average actual points: 59.00
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
- Vice captain: Bruno Guimarães Rodriguez Moura
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.50
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Gabriel Gudmundsson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.64 | 10.54 | 16.92 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.39 | 0.56 | 0.83 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.09 | 13.51 | 19.52 | 8.00 | 81.3 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.33 | 12.76 | 20.33 | 8.00 | 87.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.38 | 12.56 | 20.02 | 0.00 | 90.0 | 0.0 |
| Bench 3 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 3.44 | 9.60 | 14.85 | 0.00 | 85.0 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.68 | 7.71 | 12.60 | 6.00 | 77.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.04 | 24.00 | 39.03 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.27 | 13.67 | 21.88 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 4.00 | 12.49 | 19.72 | 2.00 | 78.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.60 | 15.42 | 24.51 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.15 | 14.97 | 23.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.20 | 14.70 | 23.97 | 10.00 | 77.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.90 | 14.12 | 23.48 | 2.00 | 84.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.84 | 13.71 | 22.14 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.51
- Actual score: 51.00
- Transfer: Marc Guéhi -> Cristian Romero (projected gain 4.61, hit 0)
- Autosub: Dominic Calvert-Lewin replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.76 | 10.64 | 17.01 | 1.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.23 | 0.53 | 0.00 | 5.4 | 0.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.92 | 13.35 | 21.71 | 4.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.65 | 13.00 | 19.58 | 1.00 | 82.2 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 4.36 | 12.09 | 18.43 | 11.00 | 88.4 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.71 | 7.83 | 12.77 | 0.00 | 79.0 | 0.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.94 | 5.98 | 9.87 | 0.00 | 44.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.10 | 22.73 | 37.20 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.43 | 14.23 | 22.69 | 2.00 | 88.7 | 90.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.53 | 10.74 | 17.28 | 2.00 | 73.6 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.27 | 15.11 | 24.59 | 2.00 | 80.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.52 | 15.00 | 23.71 | 8.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.65 | 13.34 | 21.83 | 8.00 | 78.7 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.59 | 13.15 | 21.51 | 0.00 | 79.4 | 0.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.16 | 11.60 | 19.35 | 10.00 | 76.1 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 64.98
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.42) beats the best remaining Triple Captain opportunity (7.01).
- Transfer: Bruno Guimarães Rodriguez Moura -> Declan Rice (projected gain 5.57, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.42) beats the best remaining Triple Captain opportunity (7.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 10.67 | 17.09 | 6.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.16 | 0.42 | 0.62 | 0.00 | 3.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 4.94 | 13.78 | 21.88 | 8.00 | 88.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.04 | 11.95 | 19.70 | 2.00 | 82.6 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.0 | 3.86 | 11.24 | 17.90 | 0.00 | 87.8 | 45.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.34 | 4.35 | 7.88 | -1.00 | 40.5 | 90.0 |
| Bench 4 | Bench | Jaka Bijol | DEF | 11 | 3.9 | 1.18 | 4.00 | 7.91 | 0.00 | 28.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.42 | 19.74 | 33.61 | 5.00 | 75.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.13 | 12.79 | 20.63 | 2.00 | 80.4 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 6.0 | 3.40 | 10.01 | 16.51 | 2.00 | 72.0 | 84.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.64 | 15.88 | 25.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 5.30 | 15.42 | 24.42 | 3.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.40 | 15.23 | 24.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.42 | 13.43 | 22.77 | 12.00 | 71.6 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.17 | 12.41 | 20.24 | 2.00 | 86.6 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Declan Rice
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.91
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Nordi Mukiele (projected gain 4.79, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.12 | 11.29 | 17.78 | 7.00 | 85.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.16 | 0.26 | 0.00 | 1.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.44 | 14.94 | 23.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.07 | 11.91 | 19.58 | 2.00 | 82.4 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.6 | 3.63 | 11.14 | 18.44 | 1.00 | 82.1 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.32 | 6.36 | 10.49 | 2.00 | 64.9 | 90.0 |
| Bench 4 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 0.24 | 1.14 | 3.93 | 0.00 | 5.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.46 | 20.09 | 33.62 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.73 | 12.06 | 19.74 | 5.00 | 74.3 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.9 | 3.05 | 9.11 | 15.25 | 7.00 | 65.5 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.4 | 5.66 | 15.69 | 25.04 | 5.00 | 89.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.06 | 15.21 | 25.17 | 2.00 | 85.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.08 | 14.85 | 24.26 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.61 | 13.34 | 21.62 | 10.00 | 79.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 3.98 | 11.38 | 18.08 | 2.00 | 80.3 | 90.0 |
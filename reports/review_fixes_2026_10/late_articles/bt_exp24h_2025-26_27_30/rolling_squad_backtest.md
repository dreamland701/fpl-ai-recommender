# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW27-GW30
- Total predicted points: 263.06
- Total actual points: 237.00
- Average predicted points: 65.76
- Average actual points: 59.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW27

- Train rows: 181084
- Bank: 100.00 -> 1.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 68.13
- Actual score: 45.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Trevoh Chalobah replaced Florian Wirtz.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.74 | 12.69 | 19.15 | 3.00 | 106.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 3.32 | 9.63 | 14.77 | 2.00 | 117.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.37 | 17.33 | 24.72 | 2.00 | 133.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.17 | 13.08 | 20.14 | 11.00 | 96.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.64 | 12.11 | 17.82 | 2.00 | 93.7 | 90.0 |
| Bench 2 | Autosub In | Trevoh Chalobah | DEF | 7 | 5.8 | 4.54 | 11.56 | 18.31 | 2.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 4.27 | 10.72 | 16.87 | 1.00 | 87.8 | 11.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.11 | 15.40 | 24.55 | 7.00 | 87.2 | 79.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 4.60 | 11.96 | 18.03 | 2.00 | 119.4 | 90.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.5 | 4.25 | 11.85 | 18.07 | 2.00 | 130.8 | 62.0 |
| XI | XI | Declan Rice | MID | 1 | 7.6 | 6.25 | 17.45 | 24.33 | 4.00 | 113.7 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.6 | 6.89 | 16.81 | 27.30 | 3.00 | 89.3 | 74.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 6.18 | 16.16 | 23.07 | 4.00 | 100.3 | 86.0 |
| XI | Bench | Florian Wirtz | MID | 12 | 8.4 | 5.03 | 14.19 | 22.45 | 0.00 | 87.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.27 | 13.54 | 20.41 | 2.00 | 87.7 | 90.0 |

## GW28

- Train rows: 181902
- Bank: 1.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Declan Rice
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Declan Rice
- Chip used: none
- Predicted score: 58.95
- Actual score: 52.00
- Transfer: Florian Wirtz -> Bryan Mbeumo (projected gain 4.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.21 | 11.48 | 17.77 | 3.00 | 93.8 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.57 | 7.52 | 11.37 | 8.00 | 94.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.49 | 14.92 | 20.65 | 9.00 | 103.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.35 | 13.50 | 21.31 | 7.00 | 97.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.18 | 11.18 | 17.93 | 6.00 | 87.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.7 | 2.72 | 8.79 | 13.42 | 1.00 | 79.3 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.6 | 1.84 | 6.19 | 9.81 | 0.00 | 34.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.23 | 13.30 | 21.64 | 2.00 | 75.9 | 90.0 |
| XI | XI | Mateus Mané | FWD | 20 | 4.6 | 3.73 | 10.58 | 15.38 | 2.00 | 94.8 | 90.0 |
| Bench 2 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.12 | 8.95 | 13.47 | 4.00 | 87.0 | 90.0 |
| Captain | Captain | Declan Rice | MID | 1 | 7.6 | 5.82 | 16.23 | 24.95 | 5.00 | 98.3 | 75.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.14 | 14.77 | 21.62 | 8.00 | 92.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.53 | 14.01 | 22.88 | 1.00 | 76.0 | 85.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 5.11 | 13.22 | 20.92 | 2.00 | 83.0 | 85.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.33 | 12.97 | 20.71 | 2.00 | 81.9 | 90.0 |

## GW29

- Train rows: 182721
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 65.04
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.64).
- Transfer: Trevoh Chalobah -> James Tarkowski (projected gain 1.02, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.47) beats the best remaining Triple Captain opportunity (7.64).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.83 | 10.02 | 17.26 | 7.00 | 95.5 | 90.0 |
| Bench 1 | Bench | José Malheiro de Sá | GK | 20 | 4.2 | 2.58 | 7.05 | 11.76 | 3.00 | 92.5 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.33 | 15.00 | 21.74 | 11.00 | 106.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.15 | 12.71 | 20.14 | 1.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.57 | 11.22 | 18.34 | 1.00 | 91.4 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.35 | 10.37 | 15.46 | 15.00 | 86.2 | 90.0 |
| Bench 4 | Bench | Nordi Mukiele | DEF | 17 | 4.5 | 1.01 | 3.88 | 7.74 | 0.00 | 24.4 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.71 | 13.27 | 21.62 | 19.00 | 80.3 | 84.0 |
| Bench 2 | Bench | Mateus Mané | FWD | 20 | 4.6 | 3.54 | 9.38 | 14.00 | 2.00 | 91.5 | 69.0 |
| Bench 3 | Bench | Adam Armstrong | FWD | 20 | 5.4 | 3.35 | 9.08 | 14.39 | 1.00 | 90.3 | 59.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.1 | 6.47 | 16.63 | 24.98 | 7.00 | 98.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.76 | 14.54 | 24.56 | 9.00 | 81.5 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.95 | 12.93 | 20.27 | 1.00 | 81.2 | 76.0 |
| XI | XI | Declan Rice | MID | 1 | 7.5 | 4.23 | 12.34 | 19.19 | 3.00 | 89.8 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 3.75 | 10.97 | 17.51 | 1.00 | 75.2 | 90.0 |

## GW30

- Train rows: 183541
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Antoine Semenyo
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: bench_boost
- Predicted score: 70.94
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Nordi Mukiele -> Marcos Senesi Barón (projected gain 1.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.04 | 10.85 | 18.15 | 7.00 | 93.2 | 90.0 |
| Bench 1 | Bench Boost | José Malheiro de Sá | GK | 20 | 4.2 | 2.61 | 7.20 | 11.35 | 0.00 | 87.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.73 | 12.79 | 20.38 | 9.00 | 96.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 5.06 | 12.68 | 19.08 | 2.00 | 85.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.26 | 11.11 | 16.27 | 10.00 | 92.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.05 | 10.41 | 15.89 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench Boost | James Tarkowski | DEF | 9 | 5.7 | 3.16 | 9.28 | 13.93 | 0.00 | 87.1 | 0.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.68 | 17.38 | 25.89 | 2.00 | 101.1 | 90.0 |
| Bench 3 | Bench Boost | Adam Armstrong | FWD | 20 | 5.3 | 2.87 | 8.10 | 12.90 | 5.00 | 79.7 | 86.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.53 | 6.75 | 12.14 | 1.00 | 73.8 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.00 | 16.10 | 24.84 | 2.00 | 95.3 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.54 | 15.39 | 25.09 | 2.00 | 83.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.7 | 4.59 | 12.88 | 20.90 | 2.00 | 77.5 | 74.0 |
| XI | XI | Declan Rice | MID | 1 | 7.4 | 4.80 | 12.20 | 21.65 | 3.00 | 83.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.33 | 10.56 | 17.38 | 2.00 | 79.8 | 90.0 |
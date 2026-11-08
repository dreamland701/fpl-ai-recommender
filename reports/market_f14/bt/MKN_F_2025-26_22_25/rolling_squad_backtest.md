# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 260.71
- Total actual points: 227.00
- Average predicted points: 65.18
- Average actual points: 56.75
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
- Vice captain: Florian Wirtz
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.50
- Actual score: 41.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.18 | 11.43 | 18.33 | 6.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.05 | 0.20 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.11 | 13.78 | 19.84 | 8.00 | 78.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 5.20 | 12.84 | 20.40 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.36 | 12.63 | 20.37 | 0.00 | 90.6 | 0.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.03 | 10.88 | 17.35 | 0.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.4 | 3.95 | 10.27 | 16.74 | 6.00 | 86.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.58 | 23.67 | 38.92 | 2.00 | 110.7 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.39 | 13.91 | 22.84 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.41 | 7.56 | 11.68 | 2.00 | 64.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.29 | 15.76 | 25.52 | 2.00 | 98.6 | 90.0 |
| XI | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.86 | 15.76 | 25.05 | 3.00 | 100.8 | 90.0 |
| Vice Captain | XI | Florian Wirtz | MID | 12 | 8.2 | 5.90 | 14.94 | 23.71 | 10.00 | 83.1 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.45 | 14.89 | 24.40 | 2.00 | 87.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.58 | 13.54 | 22.16 | 2.00 | 89.2 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.78
- Actual score: 49.00
- Transfer: Virgil van Dijk -> James Tarkowski (projected gain 2.10, hit 0)
- Autosub: Nordi Mukiele replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.19 | 11.51 | 18.52 | 1.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.13 | 0.08 | 0.21 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.98 | 13.80 | 20.59 | 1.00 | 84.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.80 | 13.09 | 21.20 | 4.00 | 87.4 | 90.0 |
| Bench 2 | Autosub In | Nordi Mukiele | DEF | 17 | 4.4 | 3.87 | 11.01 | 17.66 | 4.00 | 80.2 | 82.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 3.94 | 10.59 | 17.21 | 7.00 | 83.8 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.31 | 8.36 | 14.17 | 6.00 | 54.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.74 | 23.20 | 37.81 | 1.00 | 115.8 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.53 | 15.30 | 24.47 | 2.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 1.91 | 7.28 | 12.03 | 2.00 | 62.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 6.52 | 16.49 | 25.81 | 8.00 | 102.9 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.90 | 14.59 | 24.17 | 2.00 | 75.8 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.26 | 13.10 | 21.71 | 0.00 | 73.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.18 | 12.97 | 21.53 | 8.00 | 74.4 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.00 | 11.75 | 19.76 | 10.00 | 73.7 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.99
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.32) beats the best remaining Triple Captain opportunity (7.09).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 2.19, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.32) beats the best remaining Triple Captain opportunity (7.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.32 | 11.61 | 18.51 | 6.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.08 | 0.14 | 0.00 | 0.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.37 | 14.68 | 23.04 | 8.00 | 90.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.69 | 11.65 | 19.32 | 2.00 | 77.8 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.57 | 11.59 | 18.25 | 9.00 | 82.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.86 | 11.03 | 18.03 | 3.00 | 75.4 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 2.75 | 9.31 | 15.85 | 0.00 | 80.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.32 | 19.86 | 33.84 | 5.00 | 76.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.82 | 13.23 | 21.89 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.59 | 7.60 | 12.84 | 2.00 | 63.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.93 | 16.82 | 26.97 | 7.00 | 100.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.33 | 15.18 | 24.32 | 2.00 | 91.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.49 | 14.23 | 22.68 | 8.00 | 87.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.65 | 13.45 | 22.45 | 12.00 | 74.9 | 86.0 |
| Bench 2 | Bench | Harry Wilson | MID | 10 | 6.0 | 3.60 | 12.20 | 20.45 | 2.00 | 79.9 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Gabriel dos Santos Magalhães
- Vice captain: Erling Haaland
- Effective captain: Gabriel dos Santos Magalhães
- Chip used: bench_boost
- Predicted score: 64.44
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.67) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Trevoh Chalobah (projected gain 2.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.67) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.92 | 12.40 | 19.41 | 7.00 | 93.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| Captain | Captain | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 6.16 | 15.84 | 24.74 | 6.00 | 95.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.74 | 12.78 | 20.00 | 4.00 | 93.7 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.72 | 11.41 | 18.94 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 2.78 | 10.17 | 17.16 | 1.00 | 69.7 | 90.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.55 | 5.97 | 10.80 | 1.00 | 45.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.9 | 5.76 | 19.72 | 33.87 | 11.00 | 85.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 2.84 | 11.62 | 19.93 | 5.00 | 61.1 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.34 | 7.97 | 13.47 | 2.00 | 64.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 4.70 | 15.23 | 25.30 | 2.00 | 89.2 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.90 | 15.00 | 25.01 | 2.00 | 86.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.24 | 14.30 | 22.59 | 2.00 | 84.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.50 | 13.69 | 22.25 | 10.00 | 78.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.14 | 11.99 | 19.17 | 2.00 | 79.9 | 90.0 |
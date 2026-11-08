# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 263.36
- Total actual points: 231.00
- Average predicted points: 65.84
- Average actual points: 57.75
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
- Predicted score: 65.92
- Actual score: 41.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.14 | 11.43 | 18.32 | 6.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.05 | 0.17 | 0.00 | 3.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.18 | 13.78 | 19.82 | 8.00 | 80.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.64 | 12.84 | 20.44 | 2.00 | 87.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.64 | 12.63 | 20.36 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.05 | 10.88 | 17.36 | 0.00 | 83.3 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.4 | 4.02 | 10.27 | 16.72 | 6.00 | 87.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.01 | 23.66 | 38.91 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.10 | 13.92 | 22.86 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.55 | 7.57 | 11.71 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.50 | 15.76 | 25.08 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.33 | 15.76 | 25.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.26 | 14.95 | 23.74 | 10.00 | 74.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.30 | 14.89 | 24.39 | 2.00 | 84.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.82 | 13.54 | 22.17 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.20
- Actual score: 49.00
- Transfer: Virgil van Dijk -> James Tarkowski (projected gain 2.51, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.06 | 11.51 | 18.52 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.20 | 0.09 | 0.26 | 0.00 | 4.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.74 | 13.80 | 20.58 | 1.00 | 79.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.86 | 13.09 | 21.22 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.12 | 11.01 | 17.65 | 4.00 | 87.0 | 82.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.87 | 10.59 | 17.22 | 7.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 2.90 | 8.37 | 14.21 | 6.00 | 48.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.28 | 23.21 | 37.87 | 1.00 | 90.0 | 17.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.85 | 15.30 | 24.46 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.35 | 7.27 | 12.00 | 2.00 | 71.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.80 | 16.49 | 25.85 | 8.00 | 89.2 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.18 | 14.59 | 24.13 | 2.00 | 81.2 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.44 | 13.10 | 21.72 | 0.00 | 77.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.41 | 12.97 | 21.55 | 8.00 | 80.2 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.17 | 11.75 | 19.76 | 10.00 | 77.9 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.08
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.65) beats the best remaining Triple Captain opportunity (7.25).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.37, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.65) beats the best remaining Triple Captain opportunity (7.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.23 | 11.61 | 18.50 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.01 | 0.08 | 0.12 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.25 | 14.68 | 23.03 | 8.00 | 87.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.03 | 11.64 | 19.30 | 2.00 | 84.1 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.44 | 11.59 | 18.29 | 9.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.95 | 11.03 | 18.02 | 3.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.08 | 9.31 | 15.83 | 0.00 | 86.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.65 | 19.86 | 33.85 | 5.00 | 82.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.37 | 13.23 | 21.86 | 2.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.77 | 7.61 | 12.85 | 2.00 | 68.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.94 | 16.82 | 26.96 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.44 | 15.17 | 24.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.10 | 14.24 | 22.70 | 8.00 | 83.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.32 | 13.45 | 22.45 | 12.00 | 69.0 | 86.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.02 | 12.20 | 20.45 | 2.00 | 89.0 | 90.0 |

## GW25

- Train rows: 179450
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.16
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Trevoh Chalobah (projected gain 2.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.60 | 12.41 | 19.42 | 7.00 | 86.7 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.2 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.84 | 15.84 | 24.75 | 6.00 | 88.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.42 | 12.78 | 20.02 | 4.00 | 86.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.95 | 11.41 | 18.95 | 2.00 | 83.4 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.5 | 3.42 | 10.16 | 17.13 | 1.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.66 | 5.97 | 10.80 | 1.00 | 47.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.38 | 19.72 | 33.87 | 11.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.41 | 11.63 | 19.95 | 5.00 | 72.0 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.57 | 7.98 | 13.50 | 2.00 | 71.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.07 | 15.23 | 25.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.87 | 15.00 | 24.99 | 2.00 | 85.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.72 | 14.30 | 22.61 | 2.00 | 76.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.70 | 13.68 | 22.23 | 10.00 | 81.7 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.18 | 11.99 | 19.16 | 2.00 | 80.4 | 90.0 |
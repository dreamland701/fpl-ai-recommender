# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW21
- Simulated weeks: GW22-GW25
- Total predicted points: 264.02
- Total actual points: 231.00
- Average predicted points: 66.01
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
- Predicted score: 66.05
- Actual score: 41.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Micky van de Ven replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.11 | 11.43 | 18.33 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.05 | 0.20 | 0.00 | 3.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 5.11 | 13.78 | 19.84 | 8.00 | 80.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.76 | 12.84 | 20.40 | 2.00 | 88.1 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 8 | 5.3 | 4.61 | 12.63 | 20.37 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 4.08 | 10.88 | 17.35 | 0.00 | 83.4 | 90.0 |
| Bench 3 | Bench | Nordi Mukiele | DEF | 17 | 4.4 | 3.93 | 10.27 | 16.74 | 6.00 | 87.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 7.99 | 23.67 | 38.92 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.17 | 13.91 | 22.84 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.62 | 7.56 | 11.68 | 2.00 | 69.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.25 | 15.76 | 25.52 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 5.58 | 15.76 | 25.05 | 3.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.38 | 14.94 | 23.71 | 10.00 | 74.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.25 | 14.89 | 24.40 | 2.00 | 84.1 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.86 | 13.54 | 22.16 | 2.00 | 90.0 | 87.0 |

## GW23

- Train rows: 177836
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 64.66
- Actual score: 49.00
- Transfer: Virgil van Dijk -> James Tarkowski (projected gain 2.53, hit 0)
- Autosub: Micky van de Ven replaced Bruno Guimarães Rodriguez Moura.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.06 | 11.51 | 18.52 | 1.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.32 | 0.08 | 0.21 | 0.00 | 4.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.8 | 4.72 | 13.80 | 20.59 | 1.00 | 79.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 4.94 | 13.09 | 21.20 | 4.00 | 90.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.10 | 11.01 | 17.66 | 4.00 | 87.0 | 82.0 |
| Bench 2 | Autosub In | Micky van de Ven | DEF | 18 | 4.6 | 3.91 | 10.59 | 17.21 | 7.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.03 | 8.36 | 14.17 | 6.00 | 48.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.1 | 8.48 | 23.20 | 37.81 | 1.00 | 90.0 | 17.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 5.80 | 15.30 | 24.47 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.26 | 7.28 | 12.03 | 2.00 | 71.7 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.91 | 16.49 | 25.81 | 8.00 | 89.4 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 5.05 | 14.59 | 24.17 | 2.00 | 81.0 | 90.0 |
| XI | Bench | Bruno Guimarães Rodriguez Moura | MID | 15 | 7.2 | 4.45 | 13.10 | 21.71 | 0.00 | 77.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 4.48 | 12.97 | 21.53 | 8.00 | 80.3 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.9 | 4.18 | 11.75 | 19.76 | 10.00 | 78.0 | 90.0 |

## GW24

- Train rows: 178639
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.06
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.27).
- Transfer: Bruno Guimarães Rodriguez Moura -> Enzo Fernández (projected gain 3.36, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.67) beats the best remaining Triple Captain opportunity (7.27).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.20 | 11.61 | 18.51 | 6.00 | 87.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.08 | 0.14 | 0.00 | 2.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.21 | 14.68 | 23.04 | 8.00 | 87.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.96 | 11.65 | 19.32 | 2.00 | 84.0 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.4 | 4.55 | 11.59 | 18.25 | 9.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.2 | 3.90 | 11.03 | 18.03 | 3.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.6 | 3.04 | 9.31 | 15.85 | 0.00 | 86.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 15.0 | 6.67 | 19.86 | 33.84 | 5.00 | 82.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.29 | 13.23 | 21.89 | 2.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.5 | 2.79 | 7.60 | 12.84 | 2.00 | 68.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.90 | 16.82 | 26.97 | 7.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.7 | 5.45 | 15.18 | 24.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 5.14 | 14.23 | 22.68 | 8.00 | 83.0 | 90.0 |
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
- Predicted score: 66.26
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Guéhi -> Trevoh Chalobah (projected gain 2.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.65 | 12.40 | 19.41 | 7.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.9 | 5.88 | 15.84 | 24.74 | 6.00 | 88.2 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.7 | 4.48 | 12.78 | 20.00 | 4.00 | 86.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.8 | 3.97 | 11.41 | 18.94 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Bench Boost | Nordi Mukiele | DEF | 17 | 4.5 | 3.34 | 10.17 | 17.16 | 1.00 | 83.7 | 90.0 |
| Bench 4 | Bench Boost | Micky van de Ven | DEF | 18 | 4.5 | 1.65 | 5.97 | 10.80 | 1.00 | 47.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.9 | 6.39 | 19.72 | 33.87 | 11.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 3.46 | 11.62 | 19.93 | 5.00 | 72.1 | 90.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.5 | 2.66 | 7.97 | 13.47 | 2.00 | 71.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.7 | 5.04 | 15.23 | 25.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.2 | 4.80 | 15.00 | 25.01 | 2.00 | 84.9 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.77 | 14.30 | 22.59 | 2.00 | 76.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.6 | 4.64 | 13.69 | 22.25 | 10.00 | 81.6 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.15 | 11.99 | 19.17 | 2.00 | 80.4 | 90.0 |
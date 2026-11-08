# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 277.21
- Total actual points: 278.00
- Average predicted points: 69.30
- Average actual points: 69.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 69.09
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.80 | 11.42 | 19.40 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.19 | 0.66 | 2.05 | 0.00 | 6.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.22 | 14.53 | 20.29 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.42 | 13.84 | 20.52 | -3.00 | 90.0 | 52.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.94 | 12.34 | 19.38 | 2.00 | 73.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.26 | 11.37 | 18.38 | 2.00 | 78.9 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 4.5 | 2.54 | 10.15 | 15.52 | 4.00 | 87.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.75 | 24.07 | 38.90 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.94 | 16.11 | 26.62 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Viktor Gyökeres | FWD | 1 | 9.0 | 4.44 | 14.18 | 24.36 | 2.00 | 76.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.94 | 18.23 | 28.03 | 7.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.41 | 17.57 | 28.09 | -1.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.22 | 14.56 | 22.89 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.37 | 14.14 | 23.17 | 2.00 | 85.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.48 | 11.56 | 18.21 | 2.00 | 86.2 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.26
- Actual score: 68.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 3.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.93 | 11.28 | 18.23 | 6.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.07 | 0.50 | 1.16 | 0.00 | 6.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.02 | 15.07 | 20.13 | 2.00 | 84.8 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.54 | 14.56 | 21.18 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.06 | 12.44 | 18.42 | 1.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.57 | 10.69 | 16.85 | 2.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.49 | 10.52 | 14.89 | 3.00 | 81.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.63 | 25.04 | 38.62 | 8.00 | 90.0 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 5.21 | 14.77 | 23.87 | 2.00 | 74.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.05 | 12.89 | 21.17 | 2.00 | 71.3 | 73.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.26 | 18.72 | 28.04 | 18.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.05 | 14.16 | 22.21 | 3.00 | 69.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.22 | 12.06 | 18.86 | 12.00 | 73.3 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.65 | 11.10 | 16.53 | 3.00 | 66.1 | 75.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 5.0 | 3.12 | 9.69 | 14.42 | 2.00 | 75.9 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.65
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.03) beats the best remaining Triple Captain opportunity (8.83).
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 6.24, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.03) beats the best remaining Triple Captain opportunity (8.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.84 | 11.15 | 18.18 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Freddie Woodman | GK | 12 | 3.9 | 0.17 | 0.48 | 1.06 | 0.00 | 6.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.34 | 15.84 | 22.62 | 12.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.31 | 14.25 | 20.00 | 2.00 | 77.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.62 | 11.18 | 21.22 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 4.5 | 3.77 | 10.89 | 16.89 | 3.00 | 87.4 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.61 | 9.64 | 16.32 | 0.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.00 | 24.19 | 38.78 | 13.00 | 90.0 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.07 | 12.69 | 20.66 | 2.00 | 63.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.57 | 12.27 | 21.99 | 2.00 | 76.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.8 | 7.18 | 20.28 | 32.78 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.50 | 15.71 | 23.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.29 | 15.14 | 22.30 | 8.00 | 74.6 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 10.30 | 17.91 | 1.00 | 71.2 | 58.0 |
| Bench 4 | Bench | Anton Stach | MID | 11 | 5.0 | 3.53 | 9.59 | 14.82 | 2.00 | 72.8 | 72.0 |

## GW9

- Train rows: 167095
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Antoine Semenyo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 73.21
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.82) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tijjani Reijnders -> Granit Xhaka (projected gain 2.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.82) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.94 | 11.37 | 18.47 | 6.00 | 85.4 | 90.0 |
| Bench 1 | Bench Boost | Freddie Woodman | GK | 12 | 3.9 | 0.09 | 0.38 | 0.93 | 0.00 | 6.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.71 | 16.27 | 24.73 | 9.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.02 | 14.60 | 21.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.15 | 13.16 | 21.29 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 4.5 | 3.09 | 9.97 | 16.83 | 2.00 | 85.5 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.34 | 9.60 | 15.32 | 23.00 | 79.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.5 | 7.82 | 24.41 | 40.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.56 | 12.74 | 21.14 | 2.00 | 77.5 | 84.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.24 | 12.72 | 21.31 | 2.00 | 66.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.9 | 6.83 | 19.29 | 29.98 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.80 | 14.11 | 22.49 | 4.00 | 84.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.43 | 12.92 | 19.79 | 3.00 | 76.0 | 77.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.1 | 4.11 | 11.85 | 19.75 | 2.00 | 88.2 | 90.0 |
| Bench 3 | Bench Boost | Anton Stach | MID | 11 | 5.0 | 3.26 | 8.92 | 13.58 | 0.00 | 63.0 | 0.0 |
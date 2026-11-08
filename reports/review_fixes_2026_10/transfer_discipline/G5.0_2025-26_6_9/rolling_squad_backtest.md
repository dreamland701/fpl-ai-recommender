# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 253.33
- Total actual points: 219.00
- Average predicted points: 63.33
- Average actual points: 54.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 65.79
- Actual score: 28.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.6 | 3.95 | 11.62 | 19.86 | 2.00 | 94.8 | 90.0 |
| XI | XI | Gianluigi Donnarumma | GK | 13 | 5.6 | 4.27 | 11.13 | 18.35 | 2.00 | 94.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.65 | 14.77 | 21.11 | 7.00 | 99.9 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.53 | 13.86 | 21.01 | -3.00 | 100.3 | 52.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.88 | 12.41 | 20.02 | 2.00 | 72.8 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 4.7 | 3.61 | 11.72 | 19.03 | 7.00 | 87.1 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.38 | 11.60 | 19.22 | 2.00 | 80.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.02 | 16.70 | 28.05 | 2.00 | 94.4 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 4.75 | 12.76 | 21.23 | 2.00 | 73.9 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.80 | 8.26 | 14.66 | 2.00 | 77.9 | 79.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.70 | 19.27 | 33.76 | 2.00 | 82.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.7 | 6.33 | 18.33 | 28.73 | 7.00 | 98.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.41 | 17.17 | 28.02 | -1.00 | 90.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.56 | 14.98 | 24.05 | 2.00 | 105.1 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.46 | 14.36 | 24.10 | 2.00 | 86.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 56.33
- Actual score: 72.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.08 | 11.46 | 18.63 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 2.68 | 8.43 | 13.81 | 6.00 | 70.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.24 | 15.21 | 20.45 | 2.00 | 87.7 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.83 | 14.78 | 21.60 | 3.00 | 102.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.93 | 12.45 | 18.53 | 1.00 | 82.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.55 | 10.72 | 16.99 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 2.58 | 9.14 | 13.75 | 0.00 | 51.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.70 | 13.11 | 21.70 | 2.00 | 66.4 | 73.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 2.89 | 9.58 | 15.58 | 1.00 | 51.4 | 16.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.46 | 7.57 | 11.97 | 1.00 | 65.7 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.7 | 6.44 | 18.77 | 28.15 | 18.00 | 98.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.55 | 17.67 | 30.29 | 2.00 | 74.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.81 | 13.50 | 21.21 | 3.00 | 64.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.18 | 12.15 | 19.16 | 12.00 | 72.6 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.57 | 11.07 | 16.62 | 3.00 | 64.5 | 75.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohammed Kudus
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 66.03
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (9.12).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (9.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.86 | 11.23 | 18.42 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.31 | 9.54 | 15.67 | 6.00 | 81.6 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.37 | 14.27 | 20.21 | 2.00 | 78.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.75 | 11.62 | 21.63 | 4.00 | 94.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.56 | 9.76 | 16.58 | 0.00 | 82.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.78 | 9.69 | 17.86 | 3.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 2.12 | 6.35 | 11.39 | 6.00 | 31.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 4.51 | 12.52 | 22.54 | 2.00 | 75.9 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 2.31 | 7.93 | 12.65 | 1.00 | 36.1 | 30.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.51 | 5.95 | 12.04 | 0.00 | 56.9 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.8 | 7.41 | 20.46 | 32.91 | 4.00 | 119.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.48 | 17.13 | 29.34 | 2.00 | 73.2 | 84.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.70 | 15.97 | 23.92 | 2.00 | 101.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.89 | 14.20 | 20.99 | 8.00 | 66.4 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.89 | 10.49 | 18.19 | 1.00 | 71.3 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marcos Senesi Barón
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 65.18
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.02 | 11.49 | 18.74 | 6.00 | 87.0 | 90.0 |
| Bench 1 | Bench Boost | Gianluigi Donnarumma | GK | 13 | 5.6 | 3.04 | 9.44 | 15.67 | 2.00 | 80.9 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.05 | 14.78 | 21.38 | 5.00 | 93.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.8 | 4.27 | 13.51 | 21.88 | 4.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.03 | 11.88 | 18.90 | 3.00 | 88.0 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.25 | 9.69 | 15.50 | 23.00 | 78.6 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.1 | 3.40 | 9.36 | 14.93 | 1.00 | 60.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.45 | 13.06 | 21.76 | 2.00 | 76.7 | 84.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.6 | 2.09 | 7.43 | 12.37 | 4.00 | 35.0 | 28.0 |
| Bench 4 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 1.16 | 3.31 | 7.60 | 7.00 | 25.4 | 13.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 6.83 | 19.28 | 30.00 | 3.00 | 97.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.82 | 15.21 | 27.40 | 6.00 | 62.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.68 | 13.48 | 21.43 | 4.00 | 80.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.32 | 13.03 | 20.04 | 3.00 | 74.1 | 77.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.7 | 2.94 | 9.51 | 15.80 | 1.00 | 53.6 | 75.0 |
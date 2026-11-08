# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 253.62
- Total actual points: 232.00
- Average predicted points: 63.40
- Average actual points: 58.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW13 are included before the first simulated week.
- League-average scores were not available for this run.

## GW14

- Train rows: 170850
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Igor Thiago Nascimento Rodrigues
- Vice captain: Bryan Mbeumo
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 59.12
- Actual score: 32.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Nico O'Reilly, Marc Cucurella Saseta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.85 | 11.28 | 18.65 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.24 | 9.50 | 15.74 | 1.00 | 83.5 | 90.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.38 | 13.16 | 20.98 | 0.00 | 88.1 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.52 | 13.02 | 21.56 | 0.00 | 93.9 | 0.0 |
| Bench 3 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.29 | 12.65 | 20.88 | 1.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.1 | 4.31 | 12.43 | 19.83 | 0.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.36 | 12.31 | 20.40 | 4.00 | 88.4 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 5.62 | 16.77 | 26.17 | 1.00 | 91.8 | 30.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.28 | 13.17 | 22.50 | 2.00 | 64.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.50 | 12.84 | 21.18 | 2.00 | 78.4 | 63.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.51 | 16.01 | 26.70 | 3.00 | 90.1 | 82.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.56 | 15.99 | 26.49 | 2.00 | 86.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.33 | 15.59 | 25.36 | 4.00 | 89.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.26 | 15.22 | 25.29 | 6.00 | 82.4 | 29.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.3 | 4.60 | 12.79 | 21.15 | 2.00 | 88.0 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 56.71
- Actual score: 73.00
- Transfer: Virgil van Dijk -> Daniel Muñoz Mejía (projected gain 2.41, hit 0)
- Autosub outfielders: Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.97 | 11.94 | 19.46 | 2.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 2.99 | 9.39 | 15.53 | 10.00 | 85.3 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.88 | 14.48 | 23.33 | 0.00 | 95.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.15 | 12.81 | 20.91 | 6.00 | 90.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.30 | 12.05 | 19.64 | 6.00 | 79.6 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.80 | 8.60 | 15.21 | 8.00 | 47.2 | 61.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 2.78 | 8.35 | 14.40 | 6.00 | 54.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.53 | 14.70 | 24.18 | 1.00 | 76.5 | 32.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.35 | 13.05 | 21.88 | 2.00 | 68.8 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.16 | 12.42 | 20.31 | 2.00 | 67.9 | 65.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.67 | 16.13 | 26.39 | 8.00 | 88.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.53 | 16.12 | 26.11 | 18.00 | 88.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.75 | 15.02 | 24.60 | 4.00 | 65.8 | 78.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.75 | 14.54 | 24.57 | 6.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.17 | 12.42 | 20.17 | 4.00 | 78.4 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.13
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.09).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 2.72, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.50) beats the best remaining Triple Captain opportunity (7.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.55 | 12.38 | 20.06 | 2.00 | 92.2 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.39 | 10.11 | 16.67 | 6.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 13.69 | 22.11 | 1.00 | 94.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.46 | 13.36 | 21.67 | 6.00 | 92.3 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.05 | 11.77 | 18.65 | 6.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.80 | 11.00 | 18.39 | 1.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.51 | 10.52 | 17.83 | 1.00 | 69.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 4.77 | 14.33 | 23.51 | 2.00 | 76.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.93 | 12.10 | 20.77 | 2.00 | 61.4 | 80.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.90 | 11.93 | 20.01 | 2.00 | 65.8 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.50 | 18.78 | 30.80 | 13.00 | 102.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.90 | 16.78 | 27.00 | 11.00 | 74.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.55 | 15.92 | 26.38 | 2.00 | 88.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.38 | 14.73 | 24.31 | 2.00 | 86.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.40 | 12.84 | 20.69 | 3.00 | 81.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.65
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.00) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Elliot Anderson -> Harry Wilson (projected gain 2.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.00) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.94 | 11.62 | 18.74 | 7.00 | 87.4 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 3.39 | 10.14 | 16.71 | 4.00 | 88.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.58 | 13.36 | 21.44 | 1.00 | 88.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.47 | 13.25 | 21.55 | 1.00 | 92.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.95 | 11.26 | 17.59 | 6.00 | 78.1 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.77 | 10.68 | 17.94 | 0.00 | 79.5 | 90.0 |
| Bench 3 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.75 | 10.31 | 17.34 | 4.00 | 71.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.80 | 14.56 | 22.66 | 2.00 | 67.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.93 | 12.03 | 20.34 | 6.00 | 69.1 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.10 | 7.81 | 14.43 | 2.00 | 35.3 | 76.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.2 | 6.43 | 18.99 | 30.83 | 1.00 | 94.4 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.2 | 5.56 | 16.18 | 26.28 | 3.00 | 74.2 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.76 | 14.21 | 23.17 | 11.00 | 77.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.4 | 4.56 | 13.29 | 20.87 | 2.00 | 82.5 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.23 | 13.12 | 22.73 | 0.00 | 71.2 | 0.0 |
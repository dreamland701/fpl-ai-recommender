# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 253.63
- Total actual points: 232.00
- Average predicted points: 63.41
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
- Vice captain: Declan Rice
- Effective captain: Igor Thiago Nascimento Rodrigues
- Chip used: none
- Predicted score: 59.15
- Actual score: 32.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nico O'Reilly replaced Marcos Senesi Barón.
- Autosub: Marc Cucurella Saseta replaced Micky van de Ven.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.87 | 11.42 | 18.98 | 6.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.23 | 9.53 | 15.96 | 1.00 | 83.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.53 | 13.13 | 21.60 | 0.00 | 93.9 | 0.0 |
| XI | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.37 | 13.08 | 21.04 | 0.00 | 88.1 | 0.0 |
| Bench 3 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.29 | 12.76 | 21.04 | 1.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.1 | 4.31 | 12.61 | 19.99 | 0.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.33 | 12.17 | 20.33 | 4.00 | 88.4 | 90.0 |
| Captain | Captain | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 5.66 | 17.00 | 26.59 | 1.00 | 91.7 | 30.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.28 | 13.24 | 22.77 | 2.00 | 64.0 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.54 | 12.98 | 21.44 | 2.00 | 78.3 | 63.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.53 | 16.07 | 26.59 | 2.00 | 86.3 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 7.0 | 5.53 | 16.03 | 26.58 | 3.00 | 90.1 | 82.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.28 | 15.61 | 25.63 | 6.00 | 82.4 | 29.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.30 | 15.42 | 25.18 | 4.00 | 89.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.3 | 4.57 | 12.88 | 20.98 | 2.00 | 88.0 | 90.0 |

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
- Transfer: Virgil van Dijk -> Daniel Muñoz Mejía (projected gain 2.31, hit 0)
- Autosub: Marcos Senesi Barón replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.00 | 12.00 | 19.61 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.02 | 9.45 | 15.74 | 10.00 | 85.2 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 4.88 | 14.50 | 23.56 | 0.00 | 95.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.18 | 12.84 | 21.18 | 6.00 | 90.1 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 4.27 | 11.99 | 19.47 | 6.00 | 79.6 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.82 | 8.46 | 14.84 | 8.00 | 47.1 | 61.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 2.80 | 8.41 | 14.60 | 6.00 | 54.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.55 | 14.72 | 24.44 | 1.00 | 76.5 | 32.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 4.32 | 13.11 | 22.29 | 2.00 | 68.9 | 90.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.16 | 12.39 | 20.42 | 2.00 | 67.9 | 65.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.49 | 16.15 | 26.50 | 18.00 | 88.6 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 14 | 8.6 | 5.63 | 16.06 | 26.44 | 8.00 | 88.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.78 | 15.02 | 24.64 | 4.00 | 65.8 | 78.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.78 | 14.51 | 24.90 | 6.00 | 83.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.3 | 4.18 | 12.33 | 20.05 | 4.00 | 78.4 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.12
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.12).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Daniel Muñoz Mejía -> Marc Guéhi (projected gain 2.75, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.53) beats the best remaining Triple Captain opportunity (7.12).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.52 | 12.35 | 20.09 | 2.00 | 92.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.40 | 10.08 | 16.74 | 6.00 | 90.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.63 | 13.67 | 22.43 | 1.00 | 94.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.46 | 13.34 | 21.93 | 6.00 | 92.3 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 4.06 | 11.94 | 18.88 | 6.00 | 79.8 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.77 | 10.96 | 18.38 | 1.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.49 | 10.44 | 17.86 | 1.00 | 69.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.77 | 14.29 | 23.79 | 2.00 | 76.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.93 | 11.99 | 20.78 | 2.00 | 61.4 | 80.0 |
| Bench 2 | Bench | Jean-Philippe Mateta | FWD | 8 | 8.1 | 3.89 | 11.96 | 20.19 | 2.00 | 65.8 | 62.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.53 | 18.69 | 31.20 | 13.00 | 102.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.87 | 16.78 | 26.92 | 11.00 | 74.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.57 | 15.96 | 26.57 | 2.00 | 88.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.34 | 14.64 | 24.47 | 2.00 | 86.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.3 | 4.37 | 12.87 | 20.93 | 3.00 | 81.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.65
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.00) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Elliot Anderson -> Harry Wilson (projected gain 2.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.00) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.95 | 11.63 | 18.75 | 7.00 | 87.4 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.8 | 3.37 | 10.11 | 16.68 | 4.00 | 88.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.58 | 13.35 | 21.68 | 1.00 | 88.3 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.46 | 13.29 | 21.67 | 1.00 | 92.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 3.92 | 11.38 | 17.85 | 6.00 | 78.1 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.76 | 10.67 | 17.90 | 0.00 | 79.5 | 90.0 |
| Bench 2 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.78 | 10.43 | 17.71 | 4.00 | 71.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 4.77 | 14.59 | 22.90 | 2.00 | 67.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.91 | 12.01 | 20.36 | 6.00 | 69.2 | 90.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.09 | 7.84 | 14.64 | 2.00 | 35.3 | 76.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.47 | 19.01 | 31.25 | 1.00 | 94.3 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.57 | 16.33 | 26.50 | 3.00 | 74.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.76 | 14.50 | 23.68 | 11.00 | 77.8 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 5.4 | 4.54 | 13.29 | 21.06 | 2.00 | 82.6 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.26 | 13.18 | 22.91 | 0.00 | 71.1 | 0.0 |
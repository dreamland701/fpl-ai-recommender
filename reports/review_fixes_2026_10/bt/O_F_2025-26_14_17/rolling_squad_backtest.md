# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 251.92
- Total actual points: 264.00
- Average predicted points: 62.98
- Average actual points: 66.00
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
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.86
- Actual score: 49.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Marc Cucurella Saseta.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.65 | 10.73 | 17.76 | 6.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.12 | 8.93 | 14.76 | 2.00 | 87.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 4.53 | 12.87 | 20.57 | 14.00 | 83.8 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.39 | 12.55 | 20.81 | 0.00 | 91.5 | 0.0 |
| Bench 2 | Autosub In | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.21 | 12.33 | 20.34 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.03 | 12.26 | 19.54 | 0.00 | 82.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.24 | 12.04 | 19.99 | 4.00 | 86.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 5.06 | 15.79 | 24.77 | 1.00 | 88.0 | 30.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.83 | 13.92 | 22.76 | 2.00 | 81.4 | 63.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.21 | 12.76 | 21.80 | 2.00 | 61.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.65 | 16.44 | 26.67 | 4.00 | 92.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.61 | 16.00 | 26.47 | 2.00 | 85.9 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.36 | 15.74 | 26.32 | 3.00 | 89.2 | 82.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.34 | 15.47 | 25.75 | 6.00 | 85.7 | 29.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.3 | 4.56 | 12.61 | 20.87 | 2.00 | 87.5 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.06
- Actual score: 85.00
- Transfer: Virgil van Dijk -> Marc Guéhi (projected gain 2.13, hit 0)
- Autosub outfielders: Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.77 | 11.40 | 18.59 | 2.00 | 86.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.40 | 15.32 | 3.00 | 88.5 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 5.33 | 15.53 | 24.80 | 0.00 | 95.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.88 | 14.07 | 22.23 | 8.00 | 92.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.98 | 12.28 | 20.05 | 6.00 | 87.4 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.50 | 7.89 | 14.08 | 8.00 | 42.8 | 61.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 2.43 | 7.39 | 12.85 | 6.00 | 48.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.32 | 13.89 | 22.87 | 1.00 | 72.3 | 32.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.42 | 13.61 | 22.06 | 2.00 | 70.8 | 65.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.25 | 13.01 | 21.73 | 2.00 | 66.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.48 | 15.89 | 25.82 | 18.00 | 89.4 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.46 | 15.50 | 25.41 | 8.00 | 84.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.92 | 15.44 | 25.29 | 4.00 | 68.8 | 78.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.73 | 14.50 | 24.52 | 6.00 | 83.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.28 | 12.85 | 20.88 | 4.00 | 80.1 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 1.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.05
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.36) beats the best remaining Triple Captain opportunity (7.13).
- Transfer: Marcos Senesi Barón -> Virgil van Dijk (projected gain 2.29, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.36) beats the best remaining Triple Captain opportunity (7.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.33 | 11.72 | 18.99 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.40 | 9.55 | 15.59 | 1.00 | 89.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.79 | 13.81 | 22.15 | 1.00 | 91.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.27 | 13.00 | 21.08 | 6.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.41 | 12.59 | 20.29 | 6.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.54 | 10.32 | 17.30 | 1.00 | 76.1 | 90.0 |
| Bench 4 | Bench | Daniel Muñoz Mejía | DEF | 8 | 6.1 | 3.28 | 10.01 | 16.84 | 0.00 | 50.6 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 4.90 | 14.30 | 23.34 | 2.00 | 74.5 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.27 | 12.96 | 21.56 | 2.00 | 69.3 | 62.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.70 | 11.65 | 20.04 | 2.00 | 58.1 | 80.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.36 | 18.14 | 29.88 | 13.00 | 102.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.04 | 17.08 | 27.49 | 11.00 | 76.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.33 | 15.15 | 25.20 | 2.00 | 85.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 5.28 | 14.50 | 23.95 | 2.00 | 85.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 4.36 | 12.79 | 20.63 | 3.00 | 81.5 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.10 -> 2.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.94
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jean-Philippe Mateta -> Dominic Calvert-Lewin (projected gain 1.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.80 | 11.23 | 18.12 | 7.00 | 85.2 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.85 | 8.69 | 14.23 | 2.00 | 84.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.55 | 13.21 | 21.15 | 1.00 | 86.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.20 | 12.65 | 20.64 | 1.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.09 | 12.24 | 20.00 | 2.00 | 86.6 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.38 | 9.65 | 16.31 | 0.00 | 73.4 | 90.0 |
| Bench 4 | Bench Boost | Daniel Muñoz Mejía | DEF | 8 | 6.0 | 1.14 | 4.77 | 10.52 | 0.00 | 16.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.1 | 4.62 | 14.17 | 22.09 | 2.00 | 65.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.74 | 12.78 | 19.18 | 13.00 | 71.2 | 86.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.63 | 11.29 | 19.18 | 6.00 | 64.9 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.2 | 6.74 | 20.18 | 32.63 | 1.00 | 97.4 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.2 | 5.70 | 16.53 | 26.89 | 3.00 | 77.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.1 | 4.70 | 14.08 | 23.01 | 11.00 | 77.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.15 | 13.24 | 22.87 | 0.00 | 69.7 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.4 | 3.90 | 11.62 | 18.86 | 4.00 | 77.9 | 90.0 |
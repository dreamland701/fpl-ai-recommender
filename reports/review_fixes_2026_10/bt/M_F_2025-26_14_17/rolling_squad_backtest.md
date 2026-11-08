# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 253.08
- Total actual points: 264.00
- Average predicted points: 63.27
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
- Predicted score: 58.81
- Actual score: 49.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Nico O'Reilly replaced Marcos Senesi Barón.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.67 | 10.82 | 17.90 | 6.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.13 | 8.98 | 14.87 | 2.00 | 87.9 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 4.57 | 13.05 | 20.86 | 14.00 | 83.7 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.39 | 12.63 | 20.76 | 0.00 | 91.5 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.21 | 12.43 | 20.48 | 1.00 | 84.1 | 90.0 |
| Bench 2 | Autosub In | Nico O'Reilly | DEF | 13 | 5.1 | 4.17 | 12.28 | 19.44 | 0.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.02 | 12.16 | 19.55 | 0.00 | 82.5 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 5.09 | 16.05 | 25.21 | 1.00 | 88.0 | 30.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.86 | 14.05 | 23.01 | 2.00 | 81.4 | 63.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.62 | 11.14 | 18.14 | 1.00 | 66.5 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.62 | 16.28 | 26.58 | 4.00 | 92.8 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.57 | 16.09 | 26.60 | 2.00 | 86.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 5.37 | 15.84 | 25.98 | 6.00 | 85.7 | 29.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.38 | 15.77 | 26.21 | 3.00 | 89.2 | 82.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.1 | 4.46 | 13.12 | 21.43 | 6.00 | 78.1 | 45.0 |

## GW15

- Train rows: 171608
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.59
- Actual score: 84.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 2.29, hit 0)
- Autosub: Marcos Senesi Barón replaced Daniel Muñoz Mejía.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 11.43 | 18.59 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.27 | 9.38 | 15.27 | 3.00 | 88.5 | 90.0 |
| XI | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.9 | 5.33 | 15.51 | 25.01 | 0.00 | 95.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.88 | 14.00 | 22.09 | 8.00 | 92.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.00 | 12.31 | 20.34 | 6.00 | 87.4 | 90.0 |
| Bench 3 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 2.51 | 7.74 | 13.64 | 8.00 | 42.8 | 61.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 2.45 | 7.44 | 13.01 | 6.00 | 48.6 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.43 | 13.54 | 22.16 | 2.00 | 70.8 | 65.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.6 | 4.22 | 13.05 | 22.14 | 2.00 | 66.3 | 90.0 |
| Bench 2 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.38 | 10.11 | 17.36 | 2.00 | 52.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.45 | 15.94 | 26.25 | 18.00 | 89.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.43 | 15.44 | 25.46 | 8.00 | 85.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.95 | 15.43 | 25.26 | 4.00 | 68.7 | 78.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.76 | 14.48 | 24.88 | 6.00 | 83.2 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.1 | 3.89 | 11.96 | 20.41 | 2.00 | 66.9 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.05
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.09).
- Transfer: Daniel Muñoz Mejía -> Virgil van Dijk (projected gain 2.40, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.39) beats the best remaining Triple Captain opportunity (7.09).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.29 | 11.66 | 18.90 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.40 | 9.55 | 15.52 | 1.00 | 89.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.78 | 13.80 | 22.44 | 1.00 | 91.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.28 | 12.99 | 21.35 | 6.00 | 89.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.43 | 12.65 | 20.58 | 6.00 | 88.6 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 3.52 | 10.27 | 17.28 | 1.00 | 76.1 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.20 | 9.75 | 16.75 | 1.00 | 65.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.90 | 14.27 | 23.65 | 2.00 | 74.5 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 8.1 | 4.25 | 13.00 | 21.74 | 2.00 | 69.4 | 62.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.37 | 10.33 | 17.23 | 1.00 | 66.0 | 8.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.39 | 18.05 | 30.30 | 13.00 | 102.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 6.01 | 17.08 | 27.40 | 11.00 | 76.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.35 | 15.19 | 25.38 | 2.00 | 85.1 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.25 | 14.41 | 24.12 | 2.00 | 85.1 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.1 | 4.35 | 13.31 | 22.08 | 6.00 | 78.0 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.63
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.23) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Danny Welbeck -> Dominic Calvert-Lewin (projected gain 2.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.23) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.80 | 11.22 | 18.03 | 7.00 | 85.1 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 2.88 | 8.68 | 14.13 | 2.00 | 84.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.55 | 13.21 | 21.40 | 1.00 | 86.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.18 | 12.69 | 20.75 | 1.00 | 88.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 5.9 | 4.06 | 12.27 | 20.34 | 2.00 | 86.7 | 90.0 |
| Bench 2 | Bench Boost | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.73 | 10.02 | 17.02 | 4.00 | 69.6 | 90.0 |
| Bench 3 | Bench Boost | Micky van de Ven | DEF | 18 | 4.7 | 3.37 | 9.64 | 16.23 | 0.00 | 73.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.8 | 4.59 | 14.20 | 22.33 | 2.00 | 65.3 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.75 | 12.90 | 19.37 | 13.00 | 71.1 | 86.0 |
| Bench 4 | Bench Boost | Jean-Philippe Mateta | FWD | 8 | 7.9 | 2.25 | 8.19 | 15.15 | 2.00 | 37.5 | 76.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.77 | 20.26 | 33.11 | 1.00 | 97.4 | 45.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 10.1 | 5.71 | 16.67 | 27.09 | 3.00 | 77.5 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 4.70 | 14.38 | 23.51 | 11.00 | 77.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.3 | 4.18 | 13.31 | 23.04 | 0.00 | 69.6 | 0.0 |
| XI | XI | Pedro Lomba Neto | MID | 7 | 7.2 | 4.31 | 12.90 | 21.19 | 2.00 | 81.1 | 90.0 |
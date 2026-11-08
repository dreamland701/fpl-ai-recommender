# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 264.45
- Total actual points: 264.00
- Average predicted points: 66.11
- Average actual points: 66.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 143668
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 63.71
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.13 | 11.86 | 19.02 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.00 | 0.18 | 0.43 | 0.00 | 2.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.06 | 12.12 | 18.61 | 6.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.16 | 11.37 | 18.81 | 6.00 | 88.5 | 62.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.16 | 8.90 | 14.23 | 2.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 2.11 | 6.06 | 9.89 | 2.00 | 70.2 | 90.0 |
| Bench 4 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 1.83 | 5.99 | 9.95 | 1.00 | 71.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.6 | 6.45 | 17.88 | 28.54 | 11.00 | 90.0 | 72.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 4.46 | 12.36 | 20.23 | 2.00 | 79.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 4.04 | 12.00 | 19.31 | 1.00 | 84.9 | 58.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 8.01 | 23.17 | 37.22 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 7.10 | 21.38 | 36.14 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.06 | 18.39 | 29.21 | 3.00 | 84.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.05 | 12.47 | 19.78 | 5.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Mateus Gonçalo Espanha Fernandes | MID | 17 | 5.0 | 3.08 | 8.69 | 14.27 | 1.00 | 78.1 | 90.0 |

## GW17

- Train rows: 144369
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.75
- Actual score: 69.00
- Transfer: Pedro Porro -> Antonee Robinson (projected gain 3.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.10 | 11.91 | 19.21 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 0.09 | 0.46 | 0.74 | 0.00 | 4.7 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 4.88 | 12.77 | 20.16 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.64 | 11.04 | 17.56 | 2.00 | 78.7 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 2.77 | 8.16 | 13.63 | 6.00 | 75.0 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.93 | 5.81 | 9.75 | 0.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 1.44 | 4.64 | 7.81 | 0.00 | 65.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.7 | 6.15 | 18.69 | 29.40 | 17.00 | 88.6 | 72.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 4.02 | 11.99 | 19.12 | 2.00 | 73.1 | 90.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.79 | 10.50 | 17.39 | 2.00 | 72.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.16 | 22.79 | 36.41 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.4 | 6.81 | 21.95 | 36.54 | 21.00 | 90.0 | 86.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.6 | 6.06 | 18.46 | 30.08 | 1.00 | 83.2 | 23.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.21 | 11.46 | 18.13 | 3.00 | 71.6 | 90.0 |
| Bench 2 | Bench | Mateus Gonçalo Espanha Fernandes | MID | 17 | 5.0 | 2.69 | 7.77 | 13.05 | 3.00 | 77.9 | 90.0 |

## GW18

- Train rows: 145070
- Bank: 0.90 -> 2.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Alexander Isak
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 69.67
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.21) beats the best remaining Bench Boost opportunity (6.08).
- Transfer: Bukayo Saka -> Bruno Borges Fernandes (projected gain 6.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.21) beats the best remaining Bench Boost opportunity (6.08).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.47 | 12.27 | 19.73 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Hákon Valdimarsson | GK | 4 | 3.9 | 0.12 | 0.45 | 0.73 | 1.00 | 4.7 | 54.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.36 | 12.28 | 19.73 | 7.00 | 85.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 2.92 | 9.55 | 15.21 | 1.00 | 77.3 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.17 | 8.93 | 14.46 | 6.00 | 81.3 | 90.0 |
| Bench 3 | Bench Boost | Cameron Burgess | DEF | 10 | 4.0 | 1.64 | 5.68 | 9.45 | 0.00 | 75.4 | 0.0 |
| Bench 4 | Bench Boost | Sepp van den Berg | DEF | 4 | 4.1 | 0.49 | 1.97 | 3.90 | 0.00 | 33.6 | 0.0 |
| Vice Captain | XI | Alexander Isak | FWD | 15 | 8.8 | 7.61 | 22.10 | 34.49 | 8.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 4.15 | 11.67 | 18.95 | 2.00 | 69.8 | 86.0 |
| XI | XI | Jamie Vardy | FWD | 11 | 5.6 | 3.03 | 9.92 | 16.48 | 0.00 | 68.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.4 | 9.36 | 24.82 | 40.93 | 9.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 7.48 | 22.98 | 37.19 | 10.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.07 | 14.16 | 23.87 | -2.00 | 88.0 | 46.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 3.48 | 10.75 | 17.55 | 2.00 | 75.5 | 90.0 |
| Bench 2 | Bench Boost | Mateus Gonçalo Espanha Fernandes | MID | 17 | 5.0 | 2.96 | 8.11 | 13.26 | 2.00 | 75.7 | 72.0 |

## GW19

- Train rows: 145775
- Bank: 2.90 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 71.33
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.36) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Jamie Vardy -> Matheus Santos Carneiro Da Cunha (projected gain 7.12, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.36) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mateus Gonçalo Espanha Fernandes replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 4.27 | 12.25 | 19.83 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Hákon Valdimarsson | GK | 4 | 3.9 | 1.09 | 3.16 | 4.72 | 0.00 | 34.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 4.13 | 12.17 | 20.23 | 2.00 | 86.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.8 | 3.81 | 11.34 | 18.25 | 4.00 | 88.9 | 90.0 |
| XI | XI | Milos Kerkez | DEF | 3 | 4.6 | 3.03 | 9.01 | 14.46 | 1.00 | 82.3 | 90.0 |
| Bench 3 | Bench | Cameron Burgess | DEF | 10 | 4.0 | 1.08 | 3.55 | 6.12 | 0.00 | 44.7 | 0.0 |
| Bench 4 | Bench | Sepp van den Berg | DEF | 4 | 4.1 | 0.25 | 1.48 | 3.12 | 1.00 | 27.4 | 74.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.8 | 7.48 | 21.59 | 33.81 | 7.00 | 81.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 5.39 | 15.34 | 25.35 | 1.00 | 90.0 | 45.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.6 | 3.72 | 11.28 | 18.21 | 12.00 | 73.1 | 75.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.5 | 8.36 | 24.40 | 39.59 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.2 | 7.67 | 22.50 | 37.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Enzo Fernández | MID | 6 | 5.0 | 4.04 | 11.44 | 18.53 | 1.00 | 79.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.4 | 2.71 | 8.78 | 15.67 | 0.00 | 45.8 | 0.0 |
| Bench 2 | Autosub In | Mateus Gonçalo Espanha Fernandes | MID | 17 | 5.0 | 2.71 | 8.40 | 13.64 | 1.00 | 69.8 | 90.0 |
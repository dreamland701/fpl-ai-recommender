# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 252.28
- Total actual points: 197.00
- Average predicted points: 63.07
- Average actual points: 49.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 70.62
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.06 | 10.66 | 17.25 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.35 | 0.97 | 1.65 | 0.00 | 13.5 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.30 | 17.42 | 27.61 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.42 | 12.10 | 19.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.57 | 11.85 | 18.81 | 5.00 | 89.6 | 68.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.14 | 10.60 | 16.89 | 3.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 9.05 | 15.56 | -1.00 | 81.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.54 | 17.83 | 29.35 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.46 | 14.09 | 22.89 | 2.00 | 89.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.27 | 10.61 | 17.28 | 2.00 | 68.7 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.51 | 22.28 | 37.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.81 | 19.83 | 30.98 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.69 | 17.77 | 29.50 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.00 | 16.44 | 25.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.75 | 14.42 | 23.61 | 10.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.55
- Actual score: 36.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.43 | 4.57 | 7.81 | 0.00 | 38.4 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.50 | 1.19 | 1.85 | 0.00 | 10.5 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.30 | 12.96 | 20.24 | 6.00 | 75.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.17 | 10.22 | 16.70 | 2.00 | 74.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.67 | 14.03 | 1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.30 | 6.94 | 11.43 | 9.00 | 67.5 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.91 | 5.78 | 10.20 | 0.00 | 11.6 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.29 | 16.38 | 24.94 | 2.00 | 83.0 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.42 | 15.42 | 25.18 | 2.00 | 73.8 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.52 | 7.80 | 12.92 | 2.00 | 49.0 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 22.15 | 36.88 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.88 | 15.94 | 26.02 | 10.00 | 86.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.61 | 15.76 | 24.37 | 2.00 | 84.5 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.39 | 14.60 | 23.63 | 3.00 | 89.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.71 | 12.21 | 18.80 | 2.00 | 69.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.99
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.56) beats the best remaining Bench Boost opportunity (8.20).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 6.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.56) beats the best remaining Bench Boost opportunity (8.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 2.10 | 6.70 | 10.07 | 0.00 | 66.6 | 0.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 4.0 | 0.25 | 1.41 | 1.49 | 0.00 | 9.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.84 | 13.51 | 20.49 | 5.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.83 | 12.02 | 18.43 | 1.00 | 69.5 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.00 | 11.93 | 18.38 | 9.00 | 84.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.87 | 8.19 | 12.62 | 6.00 | 74.2 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.25 | 7.07 | 10.93 | 0.00 | 59.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.17 | 15.42 | 23.79 | 2.00 | 68.7 | 71.0 |
| Bench 4 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 1.82 | 8.81 | 14.46 | 1.00 | 34.5 | 59.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.20 | 7.69 | 12.18 | 0.00 | 50.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.08 | 23.33 | 37.00 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.58 | 17.21 | 25.25 | 13.00 | 81.0 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 5.16 | 15.42 | 23.41 | 3.00 | 81.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.79 | 24.03 | 2.00 | 76.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.53 | 17.92 | 3.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.40 -> 1.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.12
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.39) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Marc Cucurella Saseta -> Micky van de Ven (projected gain 1.52, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.39) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 0.97 | 3.37 | 5.70 | 0.00 | 32.3 | 0.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.30 | 1.09 | 1.64 | 0.00 | 9.9 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.43 | 12.32 | 18.70 | 2.00 | 75.2 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.09 | 11.99 | 19.03 | 1.00 | 88.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.12 | 11.79 | 18.39 | 2.00 | 81.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.91 | 13.76 | -2.00 | 80.7 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.55 | 6.99 | 11.19 | 4.00 | 66.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.38 | 11.40 | 19.13 | 8.00 | 47.7 | 66.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.71 | 11.24 | 18.80 | 2.00 | 59.4 | 74.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.56 | 5.06 | 8.51 | 1.00 | 28.8 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.36 | 21.91 | 35.72 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.83 | 17.85 | 27.13 | 5.00 | 82.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.25 | 14.83 | 23.62 | 10.00 | 81.1 | 86.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 3.89 | 12.33 | 19.96 | 2.00 | 63.9 | 60.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.29 | 10.47 | 17.35 | 9.00 | 77.1 | 90.0 |
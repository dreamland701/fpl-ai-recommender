# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 256.13
- Total actual points: 210.00
- Average predicted points: 64.03
- Average actual points: 52.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Tijjani Reijnders
- Vice captain: Mohamed Salah
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 73.32
- Actual score: 40.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Rayan Aït-Nouri replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 4.05 | 10.52 | 17.05 | 0.00 | 93.9 | 0.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.16 | 10.50 | 17.12 | 1.00 | 86.4 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.22 | 17.17 | 27.24 | 1.00 | 100.2 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.91 | 12.18 | 19.31 | 5.00 | 97.3 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.72 | 12.16 | 19.51 | 6.00 | 113.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.73 | 12.12 | 19.39 | 6.00 | 115.4 | 90.0 |
| Bench 2 | Autosub In | Rayan Aït-Nouri | DEF | 13 | 6.0 | 4.40 | 11.76 | 19.12 | 1.00 | 103.0 | 22.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.14 | 14.64 | 23.81 | 2.00 | 103.2 | 87.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.32 | 10.60 | 17.22 | 2.00 | 69.0 | 62.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.95 | 7.41 | 12.02 | 2.00 | 71.0 | 85.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 23.06 | 38.62 | 5.00 | 115.4 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.84 | 20.52 | 32.17 | 2.00 | 154.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.44 | 17.60 | 29.05 | 0.00 | 94.7 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.65 | 16.59 | 25.80 | 6.00 | 129.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.97 | 14.87 | 24.47 | 3.00 | 105.7 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Chris Wood
- Vice captain: Mohamed Salah
- Effective captain: Chris Wood
- Chip used: none
- Predicted score: 57.51
- Actual score: 42.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.78 | 7.94 | 13.08 | 8.00 | 78.5 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.32 | 4.09 | 7.13 | 0.00 | 36.6 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.82 | 13.42 | 20.94 | 6.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.65 | 10.24 | 16.72 | 1.00 | 73.9 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.97 | 9.78 | 16.10 | 2.00 | 73.4 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.22 | 6.86 | 11.90 | 0.00 | 17.2 | 0.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 13 | 6.0 | 1.57 | 5.64 | 10.35 | 0.00 | 20.4 | 90.0 |
| Captain | Captain | Chris Wood | FWD | 16 | 7.6 | 6.94 | 16.91 | 25.84 | 2.00 | 92.4 | 72.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.57 | 7.79 | 12.92 | 2.00 | 48.5 | 64.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.35 | 7.27 | 11.86 | 6.00 | 64.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.33 | 20.77 | 35.25 | 3.00 | 111.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.19 | 15.89 | 24.54 | 2.00 | 93.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.00 | 15.86 | 25.79 | 10.00 | 84.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.56 | 15.48 | 24.34 | 2.00 | 94.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 12.19 | 18.88 | 2.00 | 70.6 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.62
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.81) beats the best remaining Bench Boost opportunity (9.28).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.93, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.81) beats the best remaining Bench Boost opportunity (9.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 9.58 | 14.66 | 10.00 | 86.4 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 2.10 | 6.90 | 9.97 | 0.00 | 67.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.91 | 12.56 | 18.82 | 1.00 | 69.6 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.97 | 12.02 | 18.14 | 9.00 | 86.2 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 13 | 6.0 | 2.74 | 8.62 | 13.72 | 0.00 | 51.1 | 0.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.14 | 7.36 | 11.81 | 0.00 | 32.0 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.24 | 4.98 | 7.93 | 0.00 | 16.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.98 | 17.84 | 26.57 | 7.00 | 85.6 | 78.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 2.95 | 9.00 | 13.35 | 2.00 | 72.5 | 85.0 |
| Bench 2 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.30 | 8.02 | 12.24 | 0.00 | 51.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.41 | 22.22 | 35.26 | 9.00 | 109.2 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.16 | 17.78 | 25.63 | 13.00 | 89.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.90 | 14.89 | 23.67 | 2.00 | 69.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.00 | 12.87 | 19.39 | 3.00 | 66.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.61 | 11.77 | 17.96 | 3.00 | 74.3 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.40 -> 1.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.68
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.69) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Rayan Aït-Nouri -> Daniel Muñoz Mejía (projected gain 7.42, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.69) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.09 | 9.63 | 15.46 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.82 | 3.16 | 5.08 | 0.00 | 29.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.36 | 12.33 | 18.64 | 2.00 | 74.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.01 | 11.60 | 18.06 | 2.00 | 82.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.14 | 10.07 | 16.58 | 0.00 | 55.4 | 63.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.0 | 1.62 | 5.62 | 9.63 | 2.00 | 24.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.21 | 4.03 | 6.36 | 1.00 | 13.2 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.59 | 16.53 | 26.28 | 2.00 | 80.8 | 90.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 3.08 | 8.45 | 13.49 | 6.00 | 72.9 | 85.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.50 | 4.93 | 8.05 | 1.00 | 26.3 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.67 | 20.61 | 33.96 | 5.00 | 104.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.29 | 17.99 | 27.40 | 5.00 | 88.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.13 | 14.55 | 23.15 | 10.00 | 74.8 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.85 | 11.84 | 19.43 | 7.00 | 71.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.15 | 10.46 | 17.43 | 9.00 | 75.6 | 90.0 |
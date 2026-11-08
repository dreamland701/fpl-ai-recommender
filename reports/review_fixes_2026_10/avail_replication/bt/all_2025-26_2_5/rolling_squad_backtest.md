# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 217.77
- Total actual points: 212.00
- Average predicted points: 54.44
- Average actual points: 53.00
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Tijjani Reijnders
- Vice captain: Antoine Semenyo
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 59.11
- Actual score: 39.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Robert Lynch Sánchez replaced Marco Bizot.
- Autosub: Virgil van Dijk replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Autosub In | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.89 | 8.20 | 15.39 | 3.00 | 93.4 | 90.0 |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.06 | 7.69 | 15.97 | 0.00 | 92.3 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 5.66 | 13.21 | 21.28 | 1.00 | 99.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.53 | 10.38 | 16.06 | 6.00 | 111.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.58 | 9.93 | 18.26 | 5.00 | 96.3 | 68.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.0 | 3.20 | 9.52 | 17.94 | 3.00 | 101.2 | 90.0 |
| Bench 4 | Bench | Trai Hume | DEF | 17 | 4.5 | 3.02 | 8.09 | 15.11 | 1.00 | 80.2 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.79 | 8.96 | 14.41 | 2.00 | 70.0 | 62.0 |
| Bench 3 | Bench | Jørgen Strand Larsen | FWD | 20 | 6.5 | 3.16 | 8.50 | 14.35 | 2.00 | 76.5 | 77.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.90 | 7.38 | 11.14 | 2.00 | 50.8 | 4.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 6.20 | 18.59 | 31.98 | 5.00 | 115.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 6.72 | 18.57 | 30.82 | 2.00 | 152.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.93 | 15.22 | 24.40 | 0.00 | 94.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.83 | 13.65 | 23.36 | 2.00 | 99.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.20 | 12.65 | 19.84 | 6.00 | 118.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.20 -> 4.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.51
- Actual score: 48.00
- Transfer: Cole Palmer -> Mohammed Kudus (projected gain 6.93, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.36 | 7.99 | 13.54 | 6.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.22 | 3.84 | 6.70 | 0.00 | 53.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.27 | 12.34 | 18.25 | 6.00 | 90.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 2.36 | 8.89 | 14.24 | 2.00 | 75.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.55 | 8.83 | 15.01 | 8.00 | 84.2 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.37 | 6.74 | 10.83 | 2.00 | 78.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.53 | 4.74 | 8.65 | 0.00 | 3.4 | 0.0 |
| Bench 3 | Bench | Jørgen Strand Larsen | FWD | 20 | 6.5 | 2.15 | 7.29 | 11.54 | 0.00 | 60.9 | 0.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.24 | 6.74 | 11.78 | 2.00 | 58.6 | 64.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 2.97 | 6.52 | 10.50 | 2.00 | 48.3 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 5.87 | 20.35 | 35.88 | 3.00 | 106.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.28 | 14.65 | 22.07 | 2.00 | 98.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.29 | 14.12 | 22.79 | 10.00 | 92.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.49 | 13.54 | 23.38 | 2.00 | 98.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 2.81 | 10.27 | 17.36 | 2.00 | 72.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 4.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 58.32
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.62) beats the best remaining Bench Boost opportunity (8.96).
- Transfer: Jørgen Strand Larsen -> Hugo Ekitiké (projected gain 7.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.62) beats the best remaining Bench Boost opportunity (8.96).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.88 | 9.39 | 13.30 | 2.00 | 81.7 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 1.90 | 6.36 | 8.55 | 0.00 | 74.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.65 | 12.38 | 17.89 | 8.00 | 95.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.46 | 11.28 | 16.62 | 1.00 | 73.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.25 | 10.92 | 16.18 | 9.00 | 88.2 | 90.0 |
| Bench 2 | Bench Boost | Trai Hume | DEF | 17 | 4.5 | 2.32 | 7.38 | 11.68 | 6.00 | 79.4 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.85 | 3.97 | 5.89 | 0.00 | 7.2 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 4.44 | 14.91 | 22.00 | 2.00 | 70.7 | 71.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.42 | 8.31 | 11.51 | 0.00 | 54.0 | 0.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.06 | 6.98 | 11.20 | 0.00 | 62.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.24 | 22.29 | 35.34 | 9.00 | 106.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.03 | 14.91 | 21.22 | 13.00 | 97.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 3.97 | 13.33 | 22.32 | 2.00 | 76.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 2.66 | 10.88 | 15.67 | 3.00 | 74.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 2.92 | 10.70 | 17.71 | 3.00 | 70.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 53.83
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Micky van de Ven (projected gain 1.11, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Hugo Ekitiké replaced Junior Kroupi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.28 | 8.32 | 13.71 | -3.00 | 79.5 | 4.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 0.82 | 3.12 | 4.96 | 0.00 | 29.1 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 3.44 | 11.03 | 17.23 | 1.00 | 94.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.78 | 10.97 | 16.36 | 4.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.29 | 10.18 | 15.48 | 2.00 | 84.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 2.49 | 8.40 | 13.80 | 0.00 | 63.6 | 63.0 |
| Bench 3 | Bench | Trai Hume | DEF | 17 | 4.5 | 2.14 | 7.09 | 11.68 | 4.00 | 81.2 | 90.0 |
| Bench 2 | Autosub In | Hugo Ekitiké | FWD | 12 | 8.8 | 2.37 | 10.00 | 16.86 | 8.00 | 32.1 | 66.0 |
| XI | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.65 | 5.41 | 7.69 | 0.00 | 41.6 | 0.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.46 | 4.89 | 8.01 | 1.00 | 26.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.06 | 20.60 | 33.66 | 5.00 | 101.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 4.85 | 15.50 | 22.88 | 5.00 | 93.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 13.28 | 21.72 | 10.00 | 80.7 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 2.87 | 9.36 | 18.04 | 7.00 | 76.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 2.49 | 9.24 | 15.12 | 9.00 | 77.9 | 90.0 |
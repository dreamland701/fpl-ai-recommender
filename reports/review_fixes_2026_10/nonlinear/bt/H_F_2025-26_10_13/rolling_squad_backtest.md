# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW9
- Simulated weeks: GW10-GW13
- Total predicted points: 231.35
- Total actual points: 220.00
- Average predicted points: 57.84
- Average actual points: 55.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW9 are included before the first simulated week.
- League-average scores were not available for this run.

## GW10

- Train rows: 167841
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cody Gakpo
- Vice captain: Mohamed Salah
- Effective captain: Cody Gakpo
- Chip used: none
- Predicted score: 51.58
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.0 | 3.51 | 11.32 | 18.78 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.46 | 10.21 | 19.00 | 2.00 | 86.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.46 | 13.93 | 21.10 | 12.00 | 87.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.09 | 12.66 | 20.07 | 6.00 | 83.7 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.11 | 12.00 | 19.86 | 6.00 | 87.9 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.32 | 11.26 | 19.91 | 7.00 | 84.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.0 | 3.78 | 11.12 | 19.70 | 10.00 | 86.6 | 90.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.58 | 10.40 | 20.92 | 6.00 | 81.2 | 81.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 3.09 | 10.06 | 17.64 | 2.00 | 65.9 | 64.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 1.91 | 8.33 | 13.62 | 2.00 | 65.7 | 61.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 4.83 | 16.74 | 27.83 | 10.00 | 82.6 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.37 | 15.42 | 25.15 | 2.00 | 84.1 | 90.0 |
| Bench 3 | Bench | Antoine Semenyo | MID | 4 | 8.1 | 2.92 | 13.99 | 24.61 | 2.00 | 84.2 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.9 | 3.91 | 13.94 | 24.52 | 2.00 | 83.9 | 90.0 |
| Captain | Captain | Cody Gakpo | MID | 12 | 7.6 | 5.32 | 11.55 | 23.21 | 3.00 | 61.2 | 90.0 |

## GW11

- Train rows: 168588
- Bank: 0.10 -> 0.90
- Free transfers: 2 -> 2
- Captain: Enzo Fernández
- Vice captain: Jack Grealish
- Effective captain: Enzo Fernández
- Chip used: none
- Predicted score: 53.36
- Actual score: 38.00
- Transfer: Cody Gakpo -> Declan Rice (projected gain 4.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.0 | 3.61 | 11.21 | 18.33 | 9.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.45 | 10.01 | 18.72 | 7.00 | 89.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 3.88 | 14.08 | 21.04 | 1.00 | 83.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.27 | 13.97 | 21.55 | 1.00 | 87.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.29 | 13.60 | 18.23 | 6.00 | 83.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.38 | 11.12 | 19.06 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Marc Guéhi | DEF | 8 | 5.0 | 3.69 | 10.29 | 18.33 | 0.00 | 87.8 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.14 | 10.82 | 14.50 | 2.00 | 74.3 | 84.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.23 | 8.41 | 11.25 | 1.00 | 56.6 | 27.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 2.66 | 8.20 | 12.61 | 1.00 | 35.9 | 16.0 |
| Captain | Captain | Enzo Fernández | MID | 7 | 6.7 | 5.61 | 15.60 | 25.27 | 3.00 | 83.1 | 82.0 |
| XI | XI | Declan Rice | MID | 1 | 6.8 | 4.68 | 14.94 | 23.93 | 2.00 | 82.8 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.2 | 4.10 | 14.94 | 25.81 | 2.00 | 82.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 8.1 | 4.11 | 14.35 | 22.20 | 0.00 | 90.2 | 90.0 |
| Vice Captain | XI | Jack Grealish | MID | 9 | 6.8 | 4.69 | 13.09 | 21.72 | 3.00 | 89.5 | 90.0 |

## GW12

- Train rows: 169340
- Bank: 0.90 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Declan Rice
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.96
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.43).
- Transfer: Marc Guéhi -> Maxence Lacroix (projected gain 3.20, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.43).
- Autosub: Junior Kroupi replaced Gabriel dos Santos Magalhães.
- Autosub: Jack Grealish replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.0 | 3.36 | 11.52 | 19.10 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 5.5 | 3.05 | 10.74 | 17.11 | 10.00 | 89.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.1 | 4.17 | 14.29 | 19.84 | 5.00 | 84.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.27 | 13.05 | 20.76 | 6.00 | 82.7 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 4.41 | 12.83 | 19.21 | 11.00 | 85.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.7 | 4.04 | 12.74 | 18.86 | 14.00 | 86.0 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 6.5 | 4.90 | 10.34 | 20.62 | 0.00 | 65.8 | 0.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.4 | 4.06 | 10.83 | 17.28 | 8.00 | 78.1 | 90.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.6 | 3.23 | 9.67 | 13.20 | 2.00 | 60.3 | 85.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 2.14 | 7.61 | 12.67 | 1.00 | 40.0 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.2 | 6.30 | 17.03 | 27.46 | 2.00 | 83.1 | 90.0 |
| Vice Captain | XI | Declan Rice | MID | 1 | 6.8 | 5.76 | 15.46 | 23.58 | 6.00 | 85.6 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 4 | 8.0 | 3.97 | 12.19 | 18.95 | 0.00 | 67.9 | 0.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.13 | 12.13 | 16.94 | 11.00 | 64.1 | 90.0 |
| Bench 3 | Autosub In | Jack Grealish | MID | 9 | 6.7 | 2.92 | 11.05 | 18.07 | 3.00 | 83.7 | 87.0 |

## GW13

- Train rows: 170095
- Bank: 0.90 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Danny Welbeck
- Effective captain: Danny Welbeck
- Chip used: bench_boost
- Predicted score: 64.45
- Actual score: 31.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel dos Santos Magalhães -> Riccardo Calafiori (projected gain 4.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 5.5 | 3.14 | 10.21 | 17.98 | 1.00 | 90.4 | 90.0 |
| XI | XI | Dean Henderson | GK | 8 | 5.0 | 3.33 | 9.53 | 16.85 | 2.00 | 87.0 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.8 | 4.14 | 13.26 | 19.86 | 0.00 | 79.5 | 45.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.2 | 3.60 | 12.83 | 19.92 | 2.00 | 83.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 4.32 | 11.84 | 19.36 | 1.00 | 84.4 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.00 | 11.83 | 21.45 | 1.00 | 87.3 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.0 | 3.73 | 10.28 | 19.67 | 3.00 | 85.8 | 90.0 |
| Vice Captain | Captain | Danny Welbeck | FWD | 6 | 6.5 | 4.78 | 10.32 | 18.99 | 2.00 | 78.8 | 64.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.6 | 3.55 | 9.40 | 15.93 | 1.00 | 68.5 | 10.0 |
| Bench 4 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 1.76 | 6.21 | 9.99 | 7.00 | 33.3 | 45.0 |
| Captain | XI | Mohamed Salah | MID | 12 | 14.2 | 5.88 | 16.39 | 28.50 | 0.00 | 86.4 | 0.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.7 | 4.65 | 14.08 | 25.39 | 2.00 | 83.6 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 6.9 | 3.96 | 13.16 | 20.72 | 4.00 | 85.4 | 90.0 |
| XI | XI | Jack Grealish | MID | 9 | 6.7 | 4.49 | 12.18 | 19.60 | 2.00 | 76.1 | 79.0 |
| Bench 3 | Bench Boost | Antoine Semenyo | MID | 4 | 7.9 | 3.26 | 10.31 | 17.47 | 1.00 | 46.3 | 90.0 |
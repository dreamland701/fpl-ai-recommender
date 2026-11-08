# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 213.36
- Total actual points: 183.00
- Average predicted points: 53.34
- Average actual points: 45.75
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
- Captain: Cole Palmer
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.17
- Actual score: 43.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Mohammed Kudus replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bart Verbruggen | GK | 6 | 4.5 | 3.44 | 10.10 | 16.28 | 1.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.19 | 9.72 | 16.15 | 3.00 | 91.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.46 | 12.43 | 19.26 | 3.00 | 86.6 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 4.64 | 12.00 | 18.50 | 13.00 | 74.1 | 63.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 13 | 6.0 | 3.55 | 11.89 | 19.63 | 1.00 | 86.9 | 22.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.59 | 11.57 | 17.31 | 5.00 | 85.2 | 68.0 |
| Bench 3 | Bench | Rico Lewis | DEF | 13 | 5.0 | 2.90 | 9.85 | 16.65 | 1.00 | 63.5 | 90.0 |
| XI | XI | Niclas Füllkrug | FWD | 19 | 6.0 | 3.54 | 10.65 | 17.63 | 1.00 | 67.2 | 45.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.19 | 10.11 | 17.24 | 2.00 | 65.7 | 62.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.88 | 8.65 | 14.75 | 2.00 | 58.1 | 85.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.14 | 20.90 | 32.82 | 5.00 | 78.2 | 90.0 |
| Captain | Bench | Cole Palmer | MID | 7 | 10.5 | 7.11 | 19.22 | 29.73 | 0.00 | 81.6 | 0.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.5 | 4.74 | 14.21 | 29.16 | 2.00 | 66.3 | 79.0 |
| XI | XI | Matt O'Riley | MID | 6 | 5.5 | 3.65 | 13.06 | 20.44 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Autosub In | Mohammed Kudus | MID | 18 | 6.5 | 3.31 | 12.56 | 24.50 | 3.00 | 84.3 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Mohammed Kudus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 42.63
- Actual score: 44.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Lyle Foster replaced Matt O'Riley.
- Autosub: Niclas Füllkrug replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.35 | 10.52 | 16.84 | 6.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Bart Verbruggen | GK | 6 | 4.5 | 2.14 | 6.98 | 11.34 | 2.00 | 78.6 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 3.30 | 13.25 | 18.17 | 2.00 | 72.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.89 | 11.52 | 20.09 | 6.00 | 75.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.04 | 9.16 | 18.14 | 8.00 | 85.8 | 90.0 |
| XI | XI | Rico Lewis | DEF | 13 | 5.0 | 2.61 | 8.35 | 12.76 | 1.00 | 81.5 | 5.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 13 | 6.0 | 1.34 | 4.59 | 6.94 | 0.00 | 28.0 | 90.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.96 | 7.41 | 11.69 | 2.00 | 52.9 | 64.0 |
| Bench 3 | Autosub In | Niclas Füllkrug | FWD | 19 | 5.9 | 1.91 | 7.35 | 11.72 | 2.00 | 35.1 | 63.0 |
| Bench 2 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 2.06 | 7.14 | 12.36 | 6.00 | 65.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 4.92 | 19.83 | 30.56 | 3.00 | 83.9 | 90.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.27 | 12.70 | 19.56 | 2.00 | 83.1 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.4 | 3.16 | 10.78 | 21.74 | 3.00 | 63.2 | 88.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.4 | 2.73 | 10.65 | 15.04 | 0.00 | 33.1 | 0.0 |
| XI | Bench | Matt O'Riley | MID | 6 | 5.5 | 3.48 | 9.55 | 17.82 | 0.00 | 72.5 | 0.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 3.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 55.46
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.32) beats the best remaining Bench Boost opportunity (8.45).
- Transfer: Cole Palmer -> Antoine Semenyo (projected gain 9.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.32) beats the best remaining Bench Boost opportunity (8.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.45 | 9.69 | 14.28 | 2.00 | 82.8 | 90.0 |
| Bench 1 | Bench Boost | Bart Verbruggen | GK | 6 | 4.5 | 2.36 | 8.23 | 12.21 | 2.00 | 77.4 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 3.84 | 11.02 | 16.31 | 5.00 | 78.8 | 67.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.76 | 10.65 | 16.69 | 8.00 | 85.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.63 | 10.46 | 15.71 | 1.00 | 80.1 | 45.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 13 | 6.0 | 2.43 | 4.96 | 11.64 | 0.00 | 42.1 | 0.0 |
| Bench 3 | Bench Boost | Rico Lewis | DEF | 13 | 5.0 | 1.53 | 4.16 | 6.87 | 0.00 | 33.7 | 0.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 3.19 | 9.03 | 13.59 | 2.00 | 82.0 | 85.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.77 | 7.55 | 12.59 | 0.00 | 46.6 | 0.0 |
| Bench 2 | Bench Boost | Niclas Füllkrug | FWD | 19 | 5.8 | 2.13 | 6.96 | 12.07 | 0.00 | 33.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.19 | 18.27 | 29.29 | 9.00 | 85.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.4 | 4.86 | 15.74 | 26.92 | 13.00 | 89.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.21 | 11.81 | 19.67 | 3.00 | 86.8 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.4 | 3.64 | 10.24 | 20.33 | 3.00 | 68.2 | 86.0 |
| Bench 4 | Bench Boost | Matt O'Riley | MID | 6 | 5.5 | 1.26 | 4.91 | 9.00 | 0.00 | 13.8 | 0.0 |

## GW5

- Train rows: 164124
- Bank: 3.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 59.10
- Actual score: 39.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.15) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Niclas Füllkrug -> Ollie Watkins (projected gain 11.75, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.15) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.08 | 9.73 | 15.65 | -3.00 | 82.8 | 4.0 |
| Bench 1 | Bench | Bart Verbruggen | GK | 6 | 4.5 | 2.89 | 9.27 | 12.62 | 1.00 | 85.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.53 | 12.05 | 15.35 | 4.00 | 85.7 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 3.73 | 10.14 | 16.34 | 2.00 | 69.1 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.02 | 7.11 | 13.83 | 0.00 | 61.1 | 63.0 |
| Bench 2 | Bench | Rico Lewis | DEF | 13 | 5.0 | 1.10 | 4.65 | 7.28 | 0.00 | 25.4 | 0.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 13 | 5.9 | 0.42 | 3.48 | 6.77 | 0.00 | 8.5 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.63 | 15.32 | 22.56 | 2.00 | 78.3 | 90.0 |
| XI | XI | Lyle Foster | FWD | 3 | 5.0 | 3.55 | 9.03 | 13.74 | 6.00 | 79.9 | 85.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.35 | 5.45 | 9.08 | 1.00 | 24.4 | 10.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.62 | 16.67 | 28.52 | 5.00 | 86.1 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.5 | 7.13 | 13.88 | 23.38 | 5.00 | 89.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.02 | 11.84 | 18.84 | 7.00 | 80.0 | 90.0 |
| XI | XI | Florian Wirtz | MID | 12 | 8.3 | 4.19 | 10.50 | 17.56 | 0.00 | 72.8 | 29.0 |
| Bench 3 | Bench | Matt O'Riley | MID | 6 | 5.5 | 0.87 | 3.83 | 8.82 | 0.00 | 18.0 | 0.0 |
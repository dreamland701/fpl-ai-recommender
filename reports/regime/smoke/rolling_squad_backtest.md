# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW6
- Total predicted points: 75.39
- Total actual points: 78.00
- Average predicted points: 75.39
- Average actual points: 78.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 75.39
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.40) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.79 | 11.22 | 18.36 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 3.9 | 0.66 | 1.45 | 2.51 | 0.00 | 5.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.38 | 15.17 | 22.32 | 7.00 | 90.0 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.2 | 3.54 | 14.45 | 22.26 | -3.00 | 90.0 | 52.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 3.63 | 12.33 | 20.03 | 7.00 | 89.1 | 90.0 |
| Bench 2 | Bench | Nordi Mukiele | DEF | 17 | 4.0 | 3.43 | 10.71 | 15.90 | 6.00 | 87.6 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.0 | 2.14 | 10.62 | 16.13 | 17.00 | 89.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.02 | 24.37 | 39.89 | 16.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.49 | 14.58 | 24.26 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 1.26 | 2.94 | 5.73 | 12.00 | 16.3 | 18.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.15 | 19.77 | 34.27 | 2.00 | 88.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.92 | 17.71 | 27.83 | 7.00 | 90.0 | 90.0 |
| XI | XI | Iliman Ndiaye | MID | 9 | 6.5 | 4.22 | 13.80 | 21.71 | 2.00 | 90.0 | 80.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 5.00 | 13.73 | 22.15 | 2.00 | 90.0 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.20 | 13.55 | 22.74 | 2.00 | 86.3 | 90.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 240.70
- Total actual points: 160.00
- Average predicted points: 60.17
- Average actual points: 40.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.84
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 7 | 4.6 | 2.92 | 8.37 | 14.19 | 3.00 | 90.0 | 83.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.02 | 14.80 | 24.34 | -1.00 | 90.0 | 85.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.50 | 10.81 | 17.65 | 5.00 | 74.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.52 | 10.74 | 17.28 | 2.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.23 | 10.46 | 1.00 | 73.4 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.23 | 5.93 | 9.76 | 5.00 | 74.2 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.49 | 24.92 | 40.37 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.44 | 14.19 | 23.73 | 2.00 | 85.7 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.65 | 4.10 | 6.26 | 0.00 | 37.8 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.67 | 20.10 | 33.15 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.77 | 17.58 | 28.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.06 | 12.31 | 19.74 | 2.00 | 78.2 | 73.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.23 | 11.55 | 18.30 | 2.00 | 88.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.74 | 11.36 | 19.12 | 1.00 | 81.6 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.35
- Actual score: 56.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 0.86, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 7 | 4.6 | 2.79 | 8.17 | 13.78 | 0.00 | 75.5 | 0.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.13 | 0.16 | 0.21 | 0.00 | 0.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.84 | 13.60 | 21.62 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.04 | 11.53 | 18.21 | 7.00 | 83.9 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.82 | 11.13 | 19.55 | 0.00 | 72.2 | 0.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.10 | 6.33 | 10.11 | 1.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 5.60 | 9.73 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.62 | 16.78 | 27.39 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.78 | 14.71 | 26.85 | 0.00 | 34.4 | 0.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.34 | 4.13 | 6.31 | 1.00 | 36.4 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.12 | 22.10 | 35.91 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.31 | 18.41 | 29.32 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.89 | 11.06 | 17.75 | 6.00 | 68.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.80 | 10.95 | 18.04 | 14.00 | 68.3 | 90.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.21 | 9.85 | 16.31 | 1.00 | 78.5 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 60.10
- Actual score: 26.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (8.06).
- Transfer: Abdoulaye Doucouré -> John McGinn (projected gain 2.15, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (8.06).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 7 | 4.6 | 1.13 | 3.98 | 7.75 | 0.00 | 42.3 | 0.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.11 | 0.38 | 0.37 | 0.00 | 1.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.43 | 12.83 | 19.81 | 2.00 | 80.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.57 | 11.05 | 17.64 | 2.00 | 87.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.57 | 11.00 | 18.65 | 2.00 | 56.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.00 | 6.48 | 10.48 | 1.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.20 | 3.83 | 6.26 | 5.00 | 42.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.90 | 18.77 | 29.26 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.23 | 26.46 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | William Osula | FWD | 17 | 4.3 | 1.29 | 4.23 | 6.72 | 0.00 | 35.4 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.35 | 20.29 | 33.43 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.90 | 18.26 | 28.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.89 | 13.65 | 21.54 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.06 | 11.77 | 19.10 | 2.00 | 70.4 | 90.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 3.50 | 9.71 | 15.99 | 2.00 | 73.5 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 62.41
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.22) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Robert Sánchez -> André Onana (projected gain 5.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.22) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.17 | 9.51 | 15.73 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.29 | 0.66 | 0.87 | 0.00 | 3.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.94 | 13.59 | 22.34 | 1.00 | 82.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.90 | 11.86 | 18.92 | 5.00 | 80.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.37 | 11.78 | 18.59 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.58 | 7.01 | 11.05 | 1.00 | 78.7 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.21 | 5.96 | 9.49 | 1.00 | 65.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.57 | 14.25 | 22.70 | 2.00 | 74.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.65 | 11.53 | 21.76 | 0.00 | 28.6 | 0.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.13 | 2.91 | 4.83 | 1.00 | 21.5 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.05 | 21.00 | 34.78 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.34 | 17.76 | 28.44 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.79 | 13.05 | 21.25 | 1.00 | 81.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.63 | 11.20 | 18.04 | 0.00 | 66.1 | 0.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 2.73 | 8.94 | 14.57 | 7.00 | 76.1 | 85.0 |
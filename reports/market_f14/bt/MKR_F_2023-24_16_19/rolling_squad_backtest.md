# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 233.80
- Total actual points: 167.00
- Average predicted points: 58.45
- Average actual points: 41.75
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
- Predicted score: 61.03
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.10 | 9.60 | 16.22 | 1.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Robin Olsen | GK | 2 | 3.9 | 0.00 | 0.09 | 0.21 | 0.00 | 0.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.79 | 13.92 | 23.45 | -1.00 | 90.0 | 85.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 3.91 | 11.00 | 16.82 | 2.00 | 73.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.47 | 10.96 | 17.79 | 5.00 | 73.2 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.08 | 5.64 | 9.39 | 5.00 | 74.8 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.70 | 5.58 | 9.63 | 1.00 | 74.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.42 | 24.66 | 39.35 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.50 | 13.73 | 23.34 | 2.00 | 88.5 | 90.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.57 | 4.11 | 6.31 | 0.00 | 38.2 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.55 | 19.93 | 32.74 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.77 | 17.09 | 27.79 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.49 | 11.64 | 18.40 | 2.00 | 89.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.87 | 11.58 | 19.07 | 2.00 | 81.3 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.74 | 11.44 | 19.27 | 1.00 | 82.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.57
- Actual score: 60.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 1.49, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.30 | 8.05 | 13.54 | 10.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Robin Olsen | GK | 2 | 3.9 | 0.02 | 0.21 | 0.36 | 0.00 | 1.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.85 | 13.54 | 21.55 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.87 | 11.48 | 19.95 | 0.00 | 71.9 | 0.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 4.02 | 10.86 | 16.48 | 1.00 | 72.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.75 | 5.53 | 9.16 | 1.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 4.39 | 8.22 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.56 | 16.51 | 27.13 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.81 | 14.59 | 26.20 | 0.00 | 30.9 | 0.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.16 | 3.87 | 6.07 | 1.00 | 37.7 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.94 | 21.94 | 35.37 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.20 | 18.21 | 28.97 | 3.00 | 90.0 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.94 | 11.39 | 18.33 | 14.00 | 64.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.88 | 11.25 | 17.98 | 6.00 | 68.0 | 83.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.26 | 10.22 | 16.78 | 1.00 | 77.9 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 53.80
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (0.10) beats the best remaining Bench Boost opportunity (1.83).
- Transfer: Abdoulaye Doucouré -> John McGinn (projected gain 3.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (0.10) beats the best remaining Bench Boost opportunity (1.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.17 | 9.92 | 16.57 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Robin Olsen | GK | 2 | 3.9 | 0.33 | 0.32 | 0.67 | 0.00 | 4.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.33 | 12.95 | 19.89 | 2.00 | 78.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.56 | 10.84 | 18.45 | 2.00 | 57.0 | 90.0 |
| Bench 3 | Bench Boost | Kyle Walker | DEF | 13 | 5.3 | 0.00 | 6.07 | 11.17 | 0.00 | 0.0 | 0.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.74 | 5.82 | 9.70 | 1.00 | 78.4 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.16 | 3.73 | 6.12 | 5.00 | 42.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.78 | 18.72 | 29.10 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.85 | 26.48 | 0.00 | 0.0 | 0.0 |
| XI | XI | William Osula | FWD | 17 | 4.3 | 1.22 | 4.07 | 6.56 | 0.00 | 35.9 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.33 | 19.69 | 32.72 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.86 | 17.65 | 28.33 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.83 | 13.49 | 21.40 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 11.80 | 19.09 | 2.00 | 70.7 | 90.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 3.62 | 10.63 | 17.02 | 2.00 | 69.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.40
- Actual score: 31.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Kyle Walker -> William Saliba (projected gain 5.28, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Auston Trusty replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.14 | 9.69 | 15.97 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Robin Olsen | GK | 2 | 3.9 | 0.08 | 0.42 | 0.62 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 5.00 | 13.52 | 22.17 | 1.00 | 82.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.48 | 12.37 | 19.32 | 1.00 | 89.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.63 | 11.49 | 18.54 | 5.00 | 81.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.70 | 7.15 | 11.16 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.22 | 5.90 | 9.37 | 1.00 | 65.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.43 | 13.65 | 22.07 | 2.00 | 76.8 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.45 | 11.11 | 21.14 | 0.00 | 29.4 | 0.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.16 | 3.12 | 5.09 | 1.00 | 20.9 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.87 | 20.98 | 34.43 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.35 | 17.83 | 28.24 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.82 | 13.08 | 21.14 | 1.00 | 80.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.78 | 11.47 | 18.34 | 0.00 | 66.3 | 0.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 2.70 | 8.80 | 14.45 | 7.00 | 76.5 | 85.0 |
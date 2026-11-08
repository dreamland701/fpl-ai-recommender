# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 232.15
- Total actual points: 167.00
- Average predicted points: 58.04
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
- Predicted score: 60.79
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.16 | 9.56 | 16.17 | 1.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.07 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.71 | 13.96 | 23.51 | -1.00 | 90.0 | 85.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 3.90 | 11.00 | 16.82 | 2.00 | 73.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.42 | 10.99 | 17.83 | 5.00 | 73.2 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.61 | 5.64 | 9.72 | 1.00 | 74.6 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.14 | 5.61 | 9.33 | 5.00 | 74.9 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.45 | 24.63 | 39.31 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.36 | 13.82 | 23.47 | 2.00 | 88.4 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.64 | 4.07 | 6.25 | 0.00 | 38.2 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.63 | 19.89 | 32.68 | 13.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.67 | 17.14 | 27.88 | 2.00 | 90.0 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.49 | 11.64 | 18.41 | 2.00 | 89.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.76 | 11.63 | 19.15 | 2.00 | 81.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.79 | 11.40 | 19.22 | 1.00 | 82.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.65
- Actual score: 60.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 1.44, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.23 | 8.09 | 13.60 | 10.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.85 | 13.54 | 21.55 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.96 | 11.43 | 19.87 | 0.00 | 71.9 | 0.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 3.99 | 10.87 | 16.50 | 1.00 | 72.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.81 | 5.50 | 9.11 | 1.00 | 76.6 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 4.40 | 8.23 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.60 | 16.48 | 27.08 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.84 | 14.57 | 26.17 | 0.00 | 30.9 | 0.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.23 | 3.84 | 6.02 | 1.00 | 37.8 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.91 | 21.96 | 35.40 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.25 | 18.18 | 28.92 | 3.00 | 90.0 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.86 | 11.43 | 18.38 | 14.00 | 64.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.93 | 11.21 | 17.93 | 6.00 | 68.0 | 83.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.31 | 10.18 | 16.73 | 1.00 | 77.9 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 52.05
- Actual score: 29.00
- Transfer: Abdoulaye Doucouré -> John McGinn (projected gain 3.24, hit 0)
- Autosub: Teden Mengi replaced William Osula.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.18 | 9.92 | 16.56 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.06 | 0.17 | 0.27 | 0.00 | 2.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.37 | 12.91 | 19.85 | 2.00 | 78.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.59 | 10.82 | 18.42 | 2.00 | 57.0 | 90.0 |
| Bench 3 | Bench | Kyle Walker | DEF | 13 | 5.3 | 0.00 | 6.07 | 11.16 | 0.00 | 0.0 | 0.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.73 | 5.84 | 9.71 | 1.00 | 78.4 | 90.0 |
| Bench 2 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.16 | 3.73 | 6.12 | 5.00 | 42.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.74 | 18.73 | 29.12 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.82 | 26.44 | 0.00 | 0.0 | 0.0 |
| XI | Bench | William Osula | FWD | 17 | 4.3 | 1.21 | 4.09 | 6.58 | 0.00 | 35.9 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 6.19 | 19.78 | 32.85 | 7.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.72 | 17.73 | 28.45 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.85 | 13.47 | 21.38 | 1.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 11.79 | 19.08 | 2.00 | 70.7 | 90.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 3.60 | 10.64 | 17.03 | 2.00 | 69.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.66
- Actual score: 31.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Kyle Walker -> William Saliba (projected gain 3.54, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.94) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: John McGinn replaced Cole Palmer.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.12 | 9.71 | 15.99 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.18 | 0.26 | 0.49 | 0.00 | 5.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.98 | 13.53 | 22.18 | 1.00 | 82.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.51 | 12.35 | 19.29 | 1.00 | 89.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.64 | 11.48 | 18.53 | 5.00 | 81.6 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.71 | 7.15 | 11.15 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.23 | 5.88 | 9.34 | 1.00 | 65.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.34 | 13.71 | 22.16 | 2.00 | 76.7 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.56 | 11.04 | 21.06 | 0.00 | 29.5 | 0.0 |
| Bench 4 | Bench | William Osula | FWD | 17 | 4.3 | 1.18 | 3.11 | 5.08 | 1.00 | 20.9 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.94 | 20.94 | 34.38 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.38 | 17.80 | 28.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.80 | 13.09 | 21.16 | 1.00 | 80.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.5 | 3.80 | 11.46 | 18.32 | 0.00 | 66.4 | 0.0 |
| Bench 2 | Autosub In | John McGinn | MID | 2 | 5.5 | 2.60 | 8.86 | 14.54 | 7.00 | 76.5 | 85.0 |
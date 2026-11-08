# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 248.59
- Total actual points: 167.00
- Average predicted points: 62.15
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
- Predicted score: 62.13
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.51 | 9.56 | 16.17 | 1.00 | 96.5 | 90.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.12 | 0.54 | 0.95 | 0.00 | 4.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.08 | 13.96 | 23.51 | -1.00 | 84.4 | 85.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 4.74 | 11.00 | 16.82 | 2.00 | 95.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.91 | 10.99 | 17.83 | 5.00 | 81.9 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.35 | 5.64 | 9.72 | 1.00 | 66.7 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 5.61 | 9.33 | 5.00 | 70.9 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 9.07 | 24.63 | 39.31 | 0.00 | 109.6 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 3.86 | 13.82 | 23.47 | 2.00 | 80.0 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.57 | 4.07 | 6.25 | 0.00 | 37.3 | 52.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.69 | 19.89 | 32.68 | 13.00 | 92.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.44 | 17.14 | 27.88 | 2.00 | 90.7 | 90.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.7 | 4.52 | 11.64 | 18.41 | 2.00 | 89.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.44 | 11.63 | 19.15 | 2.00 | 72.1 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.79 | 11.40 | 19.22 | 1.00 | 81.2 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.12
- Actual score: 60.00
- Transfer: Hwang Hee-chan -> Abdoulaye Doucouré (projected gain 1.44, hit 0)
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: William Osula replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 1.96 | 8.09 | 13.60 | 10.00 | 76.6 | 90.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.03 | 0.14 | 0.35 | 0.00 | 3.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 5.22 | 13.54 | 21.55 | 8.00 | 97.4 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.78 | 11.43 | 19.87 | 0.00 | 71.4 | 0.0 |
| XI | XI | Kyle Walker | DEF | 13 | 5.3 | 4.79 | 10.87 | 16.50 | 1.00 | 93.3 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.38 | 5.50 | 9.11 | 1.00 | 65.2 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.55 | 4.40 | 8.23 | 0.00 | 38.3 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.39 | 16.48 | 27.08 | 9.00 | 96.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.76 | 14.57 | 26.17 | 0.00 | 23.5 | 0.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.01 | 3.84 | 6.02 | 1.00 | 33.4 | 32.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.66 | 21.96 | 35.40 | 3.00 | 114.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.37 | 18.18 | 28.92 | 3.00 | 98.1 | 88.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 4.74 | 11.43 | 18.38 | 14.00 | 77.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.19 | 11.21 | 17.93 | 6.00 | 71.8 | 83.0 |
| XI | XI | Abdoulaye Doucouré | MID | 9 | 5.6 | 3.60 | 10.18 | 16.73 | 1.00 | 84.0 | 45.0 |

## GW18

- Train rows: 116314
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Mohamed Salah
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 63.27
- Actual score: 31.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (8.14).
- Transfer: Abdoulaye Doucouré -> John McGinn (projected gain 3.24, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (8.14).
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.14 | 9.92 | 16.56 | 2.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Thomas Strakosha | GK | 4 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 5.06 | 12.91 | 19.85 | 2.00 | 90.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.68 | 10.82 | 18.42 | 2.00 | 56.4 | 90.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.3 | 0.70 | 6.07 | 11.16 | 0.00 | 36.7 | 0.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.48 | 5.84 | 9.71 | 1.00 | 70.9 | 90.0 |
| Bench 2 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.15 | 3.73 | 6.12 | 5.00 | 41.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 7.47 | 18.73 | 29.12 | 2.00 | 113.4 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 2.67 | 13.82 | 26.44 | 0.00 | 16.3 | 0.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.15 | 4.09 | 6.58 | 0.00 | 34.6 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.1 | 5.77 | 19.78 | 32.85 | 7.00 | 89.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.30 | 17.73 | 28.45 | 1.00 | 89.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.94 | 13.47 | 21.38 | 1.00 | 96.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.20 | 11.79 | 19.08 | 2.00 | 69.2 | 90.0 |
| XI | XI | John McGinn | MID | 2 | 5.5 | 4.63 | 10.64 | 17.03 | 2.00 | 91.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.07
- Actual score: 29.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Kyle Walker -> William Saliba (projected gain 3.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.28 | 9.71 | 15.99 | 1.00 | 95.2 | 90.0 |
| Bench 1 | Bench Boost | Thomas Strakosha | GK | 4 | 3.9 | 0.23 | 0.51 | 0.81 | 0.00 | 6.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 5.00 | 13.53 | 22.18 | 1.00 | 81.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.92 | 12.35 | 19.29 | 1.00 | 101.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.57 | 11.48 | 18.53 | 5.00 | 79.6 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.82 | 7.15 | 11.15 | 1.00 | 81.0 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.20 | 5.88 | 9.34 | 1.00 | 64.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 3.84 | 13.71 | 22.16 | 2.00 | 67.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 2.60 | 11.04 | 21.06 | 0.00 | 12.3 | 0.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.33 | 3.11 | 5.08 | 1.00 | 24.6 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 7.43 | 20.94 | 34.38 | 3.00 | 108.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 6.81 | 17.80 | 28.21 | 2.00 | 99.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 5.15 | 13.09 | 21.16 | 1.00 | 84.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.87 | 11.46 | 18.32 | 0.00 | 68.4 | 0.0 |
| Bench 2 | Bench Boost | John McGinn | MID | 2 | 5.5 | 2.57 | 8.86 | 14.54 | 7.00 | 76.4 | 85.0 |
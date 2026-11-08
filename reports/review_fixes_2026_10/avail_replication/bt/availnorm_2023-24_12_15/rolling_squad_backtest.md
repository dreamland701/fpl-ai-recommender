# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 240.47
- Total actual points: 238.00
- Average predicted points: 60.12
- Average actual points: 59.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.48
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.59 | 9.80 | 15.67 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.52 | 9.63 | 15.64 | 4.00 | 83.0 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.98 | 15.82 | 25.07 | 1.00 | 96.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.28 | 11.84 | 18.79 | 7.00 | 74.7 | 89.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.34 | 11.15 | 17.47 | 9.00 | 92.0 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.2 | 3.89 | 10.76 | 17.15 | 2.00 | 69.8 | 90.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 3.68 | 10.70 | 17.13 | 1.00 | 89.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.62 | 16.46 | 26.15 | 6.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 2.67 | 7.87 | 12.65 | 1.00 | 58.9 | 18.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.77 | 7.78 | 12.98 | 2.00 | 69.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.73 | 20.09 | 32.99 | 16.00 | 104.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.58 | 15.11 | 23.54 | 8.00 | 106.2 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 6.5 | 4.99 | 13.30 | 20.73 | 1.00 | 85.6 | 45.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 7.8 | 4.81 | 12.35 | 19.20 | 2.00 | 73.1 | 88.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.95 | 12.21 | 20.33 | 2.00 | 88.7 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: William Saliba
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.04
- Actual score: 42.00
- Transfer: Kaoru Mitoma -> Cole Palmer (projected gain 4.28, hit 0)
- Autosub: Cameron Archer replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.58 | 9.71 | 15.42 | 3.00 | 91.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 3.06 | 8.98 | 14.99 | 3.00 | 86.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.50 | 13.20 | 21.54 | 1.00 | 88.9 | 90.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.3 | 4.52 | 12.19 | 18.66 | 6.00 | 98.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 3.32 | 10.60 | 17.36 | 8.00 | 71.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.69 | 10.47 | 16.70 | 1.00 | 91.1 | 90.0 |
| Bench 3 | Bench | Matty Cash | DEF | 2 | 5.1 | 2.84 | 9.25 | 14.73 | 0.00 | 65.1 | 45.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.47 | 14.38 | 22.10 | 5.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.81 | 12.80 | 2.00 | 68.6 | 90.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 1.73 | 6.53 | 11.20 | 1.00 | 32.0 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.22 | 20.39 | 33.50 | 5.00 | 106.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.38 | 13.07 | 20.93 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 4.32 | 12.23 | 19.65 | 0.00 | 74.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.07 | 12.02 | 19.12 | 2.00 | 91.7 | 74.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 7.8 | 3.75 | 10.80 | 16.85 | 2.00 | 53.5 | 78.0 |

## GW14

- Train rows: 113281
- Bank: 1.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 62.15
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.73).
- Transfer: Jarrod Bowen -> Bukayo Saka (projected gain 4.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (8.73).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.43 | 9.29 | 14.89 | 2.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | 15 | 5.5 | 2.84 | 8.66 | 14.50 | 6.00 | 85.5 | 85.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.29 | 12.68 | 21.01 | 12.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.15 | 11.70 | 19.23 | 13.00 | 80.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.19 | 11.27 | 17.59 | 1.00 | 85.3 | 90.0 |
| XI | XI | Matty Cash | DEF | 2 | 5.0 | 3.29 | 9.52 | 15.86 | 1.00 | 55.7 | 16.0 |
| Bench 2 | Bench | Joachim Andersen | DEF | 8 | 5.1 | 2.98 | 9.00 | 14.63 | 2.00 | 78.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.09 | 12.56 | 21.14 | 11.00 | 67.0 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.86 | 7.86 | 12.92 | 1.00 | 71.7 | 45.0 |
| Bench 4 | Bench | Neal Maupay | FWD | 4 | 4.9 | 2.55 | 7.32 | 12.47 | 8.00 | 29.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.87 | 20.30 | 33.77 | 5.00 | 106.3 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 6.9 | 6.23 | 16.35 | 25.65 | 5.00 | 100.1 | 77.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.8 | 4.59 | 13.60 | 22.02 | 8.00 | 99.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.49 | 10.50 | 16.78 | 1.00 | 64.2 | 24.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 7.8 | 3.78 | 10.28 | 16.66 | 3.00 | 54.2 | 77.0 |

## GW15

- Train rows: 114034
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.81
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.02) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 1.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.02) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.92 | 8.64 | 14.08 | 0.00 | 87.3 | 0.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | 15 | 5.5 | 2.45 | 7.68 | 13.11 | 0.00 | 74.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.96 | 13.90 | 22.62 | 1.00 | 98.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 7.9 | 4.53 | 12.51 | 21.01 | 12.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.86 | 10.73 | 17.12 | 1.00 | 84.5 | 90.0 |
| XI | XI | Konstantinos Tsimikas | DEF | 11 | 4.8 | 3.58 | 9.63 | 15.44 | 0.00 | 69.5 | 0.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 5.1 | 3.35 | 9.12 | 15.06 | 1.00 | 82.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.05 | 13.05 | 22.19 | 1.00 | 77.8 | 89.0 |
| Bench 2 | Bench Boost | Neal Maupay | FWD | 4 | 4.9 | 2.77 | 8.34 | 13.26 | 2.00 | 44.7 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.6 | 2.30 | 7.05 | 11.48 | 2.00 | 59.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 6.98 | 19.86 | 33.51 | 3.00 | 106.6 | 66.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.8 | 6.05 | 16.64 | 26.78 | 5.00 | 96.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 3.90 | 12.32 | 19.80 | 6.00 | 60.7 | 39.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 7.8 | 3.63 | 10.30 | 16.82 | 7.00 | 53.3 | 63.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.2 | 2.49 | 9.25 | 15.64 | 8.00 | 47.7 | 90.0 |
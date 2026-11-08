# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 243.08
- Total actual points: 196.00
- Average predicted points: 60.77
- Average actual points: 49.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 124319
- Bank: 100.00 -> 2.20
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 82.34
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.60) beats the best remaining Bench Boost opportunity (12.49).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.60) beats the best remaining Bench Boost opportunity (12.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 4.28 | 11.91 | 19.45 | 2.00 | 99.4 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.6 | 4.50 | 10.02 | 15.28 | 4.00 | 113.3 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.80 | 13.40 | 21.32 | 2.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.75 | 12.83 | 20.41 | 1.00 | 82.9 | 90.0 |
| Bench 3 | Bench Boost | Kieran Trippier | DEF | 15 | 6.9 | 3.81 | 11.96 | 20.07 | 0.00 | 76.4 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.93 | 11.39 | 18.45 | 5.00 | 105.5 | 180.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.35 | 10.64 | 18.00 | 2.00 | 87.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 6.95 | 19.93 | 32.59 | 2.00 | 104.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 6.24 | 15.42 | 23.15 | 8.00 | 100.7 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.1 | 4.98 | 11.43 | 18.92 | 4.00 | 103.1 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.93 | 20.18 | 33.33 | 2.00 | 68.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 6.36 | 19.16 | 30.98 | 2.00 | 104.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.71 | 13.62 | 22.27 | 2.00 | 86.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.46 | 12.97 | 21.64 | 13.00 | 76.7 | 85.0 |
| Bench 2 | Bench Boost | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.35 | 12.65 | 21.00 | 11.00 | 85.6 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 2.20 -> 2.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 55.04
- Actual score: 12.00
- Transfer: Norberto Murara Neto -> Thomas Kaminski (projected gain 0.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 10.79 | 18.08 | 3.00 | 91.6 | 90.0 |
| Bench 1 | Bench | Thomas Kaminski | GK | 12 | 4.5 | 3.49 | 9.96 | 16.31 | 2.00 | 112.5 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.82 | 13.92 | 22.19 | 1.00 | 105.4 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.7 | 3.31 | 11.26 | 18.95 | 0.00 | 67.0 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.16 | 10.72 | 17.86 | 0.00 | 62.0 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.35 | 8.85 | 15.49 | 0.00 | 55.5 | 0.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 1.31 | 6.51 | 12.90 | 0.00 | 18.1 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 6.23 | 17.75 | 29.50 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.1 | 4.67 | 15.10 | 24.96 | 0.00 | 76.7 | 0.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.1 | 4.52 | 13.04 | 20.87 | 2.00 | 94.5 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.28 | 17.51 | 29.94 | 0.00 | 57.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.1 | 5.12 | 16.30 | 26.72 | 0.00 | 70.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.45 | 13.71 | 22.49 | 2.00 | 85.6 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.71 | 12.21 | 20.98 | 0.00 | 67.4 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.63 | 11.90 | 20.34 | 0.00 | 60.4 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 2.30 -> 0.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 47.66
- Actual score: 49.00
- Transfer: Bruno Borges Fernandes -> Son Heung-min (projected gain 6.94, hit 0)
- Autosub: William Saliba replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.22 | 10.26 | 17.53 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Thomas Kaminski | GK | 12 | 4.5 | 2.42 | 8.32 | 13.79 | 1.00 | 97.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.22 | 11.40 | 17.98 | 2.00 | 81.4 | 82.0 |
| Bench 3 | Autosub In | William Saliba | DEF | 1 | 5.7 | 2.50 | 8.76 | 15.10 | 7.00 | 53.3 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.8 | 2.71 | 8.17 | 14.12 | 0.00 | 40.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.51 | 7.81 | 13.45 | 1.00 | 50.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.17 | 7.64 | 12.98 | 6.00 | 48.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 5.52 | 17.31 | 29.15 | 1.00 | 85.7 | 45.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.1 | 3.56 | 11.99 | 18.75 | 2.00 | 88.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 3.65 | 11.21 | 19.06 | 7.00 | 51.1 | 84.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.0 | 5.39 | 16.77 | 25.56 | 10.00 | 76.0 | 87.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 4.48 | 14.82 | 24.90 | 3.00 | 50.8 | 77.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.23 | 14.81 | 23.02 | 10.00 | 85.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.65 | 13.12 | 22.24 | 3.00 | 55.4 | 60.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.42 | 9.88 | 16.92 | 15.00 | 53.3 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Son Heung-min
- Effective captain: Son Heung-min
- Chip used: triple_captain
- Predicted score: 58.04
- Actual score: 73.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Thomas Kaminski replaced Alphonse Areola.
- Autosub: Carlton Morris replaced Bukayo Saka.
- Autosub: Alfie Doughty replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.2 | 3.03 | 9.66 | 16.05 | 0.00 | 73.8 | 0.0 |
| Bench 1 | Autosub In | Thomas Kaminski | GK | 12 | 4.5 | 2.25 | 7.08 | 12.26 | 2.00 | 95.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.09 | 11.22 | 18.73 | 7.00 | 77.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.63 | 9.80 | 16.22 | 6.00 | 70.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 3.40 | 9.53 | 15.61 | 2.00 | 71.1 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.79 | 8.36 | 15.64 | 1.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.91 | 5.71 | 10.91 | 0.00 | 23.9 | 0.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.9 | 4.15 | 14.46 | 25.38 | 0.00 | 68.1 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 4.61 | 12.39 | 20.89 | 2.00 | 75.8 | 89.0 |
| Bench 2 | Autosub In | Carlton Morris | FWD | 12 | 5.1 | 2.81 | 8.41 | 15.39 | 2.00 | 81.2 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.1 | 5.45 | 15.01 | 25.20 | 0.00 | 64.5 | 0.0 |
| Vice Captain | Captain | Son Heung-min | MID | 18 | 10.0 | 5.35 | 14.98 | 26.31 | 2.00 | 78.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.92 | 14.10 | 22.82 | 20.00 | 77.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.49 | 12.92 | 23.52 | 5.00 | 83.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.04 | 12.71 | 21.78 | 20.00 | 58.8 | 79.0 |
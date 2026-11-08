# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 241.86
- Total actual points: 200.00
- Average predicted points: 60.46
- Average actual points: 50.00
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
- Bank: 100.00 -> 0.70
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 80.75
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.17) beats the best remaining Bench Boost opportunity (13.76).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.17) beats the best remaining Bench Boost opportunity (13.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 4.26 | 11.80 | 19.13 | 2.00 | 99.5 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.6 | 4.53 | 10.03 | 15.03 | 4.00 | 113.2 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.7 | 4.77 | 13.31 | 21.31 | 2.00 | 86.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.72 | 12.73 | 20.22 | 1.00 | 83.0 | 90.0 |
| Bench 2 | Bench Boost | Kieran Trippier | DEF | 15 | 6.9 | 3.80 | 11.87 | 19.77 | 0.00 | 76.5 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.93 | 11.39 | 18.17 | 5.00 | 105.5 | 180.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.36 | 10.59 | 17.77 | 2.00 | 87.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.9 | 6.98 | 19.80 | 32.08 | 2.00 | 104.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.1 | 6.27 | 15.11 | 22.56 | 8.00 | 100.6 | 180.0 |
| Bench 3 | Bench Boost | Julián Álvarez | FWD | 13 | 6.6 | 3.40 | 11.12 | 18.80 | 2.00 | 60.3 | 68.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.89 | 20.03 | 32.66 | 2.00 | 68.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 6.37 | 19.13 | 30.82 | 2.00 | 104.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.69 | 13.44 | 21.79 | 2.00 | 86.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 4.48 | 12.99 | 21.46 | 13.00 | 76.7 | 85.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.35 | 12.53 | 20.67 | 11.00 | 85.6 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 0.70 -> 2.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 55.07
- Actual score: 12.00
- Transfer: Julián Álvarez -> Carlton Morris (projected gain 1.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.51 | 10.55 | 17.53 | 3.00 | 91.7 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.91 | 9.69 | 15.89 | 0.00 | 99.3 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.84 | 13.90 | 21.79 | 1.00 | 105.4 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.31 | 11.12 | 18.80 | 0.00 | 67.0 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.16 | 10.56 | 17.69 | 0.00 | 62.0 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.35 | 8.73 | 15.26 | 0.00 | 55.5 | 0.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.8 | 1.31 | 6.43 | 12.70 | 0.00 | 18.1 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.26 | 17.61 | 28.99 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.67 | 14.92 | 24.03 | 0.00 | 76.7 | 0.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 4.54 | 12.90 | 20.23 | 2.00 | 94.4 | 90.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.27 | 17.27 | 29.51 | 0.00 | 57.5 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.13 | 16.03 | 26.35 | 0.00 | 70.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.41 | 13.46 | 21.88 | 2.00 | 85.7 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.71 | 12.07 | 20.53 | 0.00 | 67.4 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.63 | 11.79 | 20.12 | 0.00 | 60.4 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 2.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 47.86
- Actual score: 49.00
- Transfer: Bruno Borges Fernandes -> Son Heung-min (projected gain 7.31, hit 0)
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.24 | 10.09 | 17.19 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.01 | 6.06 | 10.50 | 2.00 | 60.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 3.25 | 11.46 | 17.86 | 2.00 | 81.4 | 82.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.51 | 8.67 | 15.04 | 7.00 | 53.3 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.8 | 2.74 | 8.07 | 13.95 | 0.00 | 40.3 | 0.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | 11 | 6.4 | 2.48 | 7.64 | 13.18 | 1.00 | 50.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.18 | 7.56 | 12.91 | 6.00 | 48.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.56 | 17.03 | 28.64 | 1.00 | 85.6 | 45.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 3.60 | 12.04 | 18.54 | 2.00 | 88.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.65 | 10.84 | 18.50 | 7.00 | 51.1 | 84.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.0 | 5.40 | 16.96 | 25.26 | 10.00 | 76.0 | 87.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.25 | 14.88 | 22.83 | 10.00 | 85.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 4.49 | 14.56 | 24.60 | 3.00 | 50.8 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 3.62 | 12.76 | 21.82 | 3.00 | 55.5 | 60.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.40 | 9.70 | 16.71 | 15.00 | 53.3 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Son Heung-min
- Effective captain: Son Heung-min
- Chip used: triple_captain
- Predicted score: 58.18
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Antoine Semenyo (projected gain 0.06, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Norberto Murara Neto replaced Alphonse Areola.
- Autosub outfielders: Antoine Semenyo, Alfie Doughty.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.05 | 9.62 | 15.80 | 0.00 | 73.7 | 0.0 |
| Bench 1 | Autosub In | Norberto Murara Neto | GK | 3 | 4.7 | 2.79 | 8.00 | 13.26 | 7.00 | 81.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.09 | 11.25 | 18.78 | 7.00 | 77.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.63 | 9.83 | 16.27 | 6.00 | 70.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.42 | 9.57 | 15.56 | 2.00 | 71.1 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.75 | 8.37 | 15.75 | 1.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 6.7 | 1.91 | 5.69 | 10.90 | 0.00 | 23.9 | 0.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 9.0 | 4.16 | 14.36 | 24.91 | 0.00 | 68.1 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.60 | 12.51 | 20.90 | 2.00 | 75.9 | 89.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 3.28 | 9.16 | 14.77 | 3.00 | 71.2 | 45.0 |
| Vice Captain | Captain | Son Heung-min | MID | 18 | 10.1 | 5.39 | 15.21 | 26.42 | 2.00 | 78.8 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.1 | 5.45 | 14.92 | 25.32 | 0.00 | 64.5 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.94 | 14.16 | 22.78 | 20.00 | 77.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.53 | 12.96 | 23.50 | 5.00 | 83.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.01 | 12.53 | 21.64 | 20.00 | 58.9 | 79.0 |
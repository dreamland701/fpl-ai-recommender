# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 268.44
- Total actual points: 257.00
- Average predicted points: 67.11
- Average actual points: 64.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 55.95
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.61 | 8.62 | 14.07 | 0.00 | 69.2 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.47 | 14.73 | 1.00 | 83.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.62 | 13.03 | 21.03 | 4.00 | 87.4 | 90.0 |
| Bench 4 | Bench | Kyle Walker | DEF | 13 | 5.5 | 3.01 | 11.12 | 15.83 | 1.00 | 61.7 | 33.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 3.77 | 10.85 | 18.33 | 4.00 | 57.9 | 45.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.6 | 3.49 | 10.45 | 17.18 | 12.00 | 79.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.65 | 9.40 | 18.13 | 1.00 | 71.0 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.92 | 16.65 | 27.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.65 | 11.61 | 18.91 | 1.00 | 85.0 | 19.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 3.93 | 9.84 | 19.44 | 5.00 | 70.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.66 | 20.69 | 29.97 | 3.00 | 89.9 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.94 | 18.50 | 26.34 | 4.00 | 64.3 | 33.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.25 | 16.65 | 27.88 | 15.00 | 75.5 | 66.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.90 | 13.49 | 21.31 | 7.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 5.0 | 3.73 | 9.66 | 18.81 | 2.00 | 73.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 93.92
- Actual score: 66.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.94) beats the best remaining Bench Boost opportunity (11.34).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Kyle Walker -> Gabriel dos Santos Magalhães (projected gain 5.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.94) beats the best remaining Bench Boost opportunity (11.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.27 | 9.24 | 15.04 | 3.00 | 81.1 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 7.93 | 10.88 | 2.00 | 78.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.64 | 12.79 | 16.61 | 1.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 12.10 | 15.52 | 6.00 | 87.6 | 90.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.28 | 11.74 | 14.84 | 6.00 | 84.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.73 | 8.32 | 15.55 | 1.00 | 127.2 | 154.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.6 | 4.27 | 7.24 | 10.69 | 0.00 | 60.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.34 | 13.95 | 23.70 | 13.00 | 74.0 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 5.58 | 8.47 | 16.30 | 0.00 | 128.3 | 0.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.50 | 6.56 | 9.60 | 0.00 | 35.1 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 10.95 | 20.72 | 24.81 | 5.00 | 160.3 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 9.21 | 18.29 | 22.11 | 2.00 | 105.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.17 | 17.40 | 23.15 | 15.00 | 78.6 | 68.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.38 | 14.06 | 16.90 | 4.00 | 150.7 | 43.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.51 | 8.87 | 17.18 | 3.00 | 142.0 | 180.0 |

## GW26

- Train rows: 122659
- Bank: 0.40 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 56.49
- Actual score: 53.00
- Transfer: Diogo Teixeira da Silva -> Pascal Groß (projected gain 6.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.77 | 10.11 | 16.54 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.90 | 6.58 | 8.97 | 0.00 | 77.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.92 | 13.05 | 16.97 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.51 | 12.62 | 15.99 | 2.00 | 87.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.16 | 11.65 | 14.64 | 2.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 11.51 | 18.69 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.6 | 0.00 | 4.94 | 8.50 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.07 | 19.09 | 30.66 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 6.19 | 11.05 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.09 | 5.62 | 8.67 | 0.00 | 26.4 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.55 | 20.68 | 26.13 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.57 | 17.55 | 22.12 | 11.00 | 90.0 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.90 | 14.23 | 18.49 | 0.00 | 64.1 | 6.0 |
| XI | Bench | Ross Barkley | MID | 12 | 5.0 | 0.00 | 13.34 | 21.95 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 4.39 | 13.02 | 16.51 | 7.00 | 85.7 | 90.0 |

## GW27

- Train rows: 123487
- Bank: 2.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 62.08
- Actual score: 89.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.27) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Pascal Groß -> Jarrod Bowen (projected gain 5.67, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.27) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.67 | 10.14 | 16.38 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.30 | 2.64 | 5.72 | 7.00 | 39.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.51 | 8.77 | 17.25 | 1.00 | 88.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.38 | 8.01 | 15.34 | 6.00 | 80.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.02 | 7.59 | 11.60 | 5.00 | 41.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.10 | 7.22 | 13.71 | 6.00 | 74.2 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.5 | 1.60 | 3.85 | 8.33 | 0.00 | 15.1 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.44 | 18.28 | 28.65 | 13.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.56 | 4.37 | 7.64 | 0.00 | 12.3 | 0.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.82 | 2.62 | 6.57 | 0.00 | 14.8 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.27 | 13.09 | 25.93 | 7.00 | 83.5 | 45.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.43 | 12.54 | 20.23 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.55 | 10.85 | 20.94 | 15.00 | 87.3 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 1.79 | 8.48 | 13.61 | 2.00 | 46.5 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 3.36 | 7.39 | 15.17 | 2.00 | 35.0 | 90.0 |
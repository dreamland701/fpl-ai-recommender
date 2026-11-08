# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 234.10
- Total actual points: 243.00
- Average predicted points: 58.53
- Average actual points: 60.75
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
- Captain: Kevin De Bruyne
- Vice captain: Phil Foden
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 53.57
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.53 | 8.66 | 14.09 | 0.00 | 70.5 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.53 | 8.07 | 13.79 | 1.00 | 85.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.32 | 12.04 | 19.38 | 4.00 | 90.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 4.12 | 11.64 | 19.63 | 4.00 | 58.4 | 45.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.9 | 3.50 | 10.25 | 17.13 | 2.00 | 78.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.72 | 9.73 | 15.45 | 1.00 | 72.4 | 86.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.6 | 3.21 | 9.65 | 15.54 | 12.00 | 81.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 4.98 | 13.33 | 21.81 | 6.00 | 57.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.44 | 11.26 | 18.48 | 1.00 | 85.0 | 19.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 3.93 | 10.09 | 16.51 | 5.00 | 70.6 | 90.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 10.8 | 5.37 | 15.07 | 24.30 | 4.00 | 68.3 | 33.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.30 | 14.29 | 23.03 | 3.00 | 93.1 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.25 | 14.11 | 22.41 | 7.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Bukayo Saka | MID | 1 | 9.0 | 3.19 | 12.36 | 20.75 | 15.00 | 75.6 | 66.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.24 | 12.25 | 19.85 | 10.00 | 81.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 3.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 64.90
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.39) beats the best remaining Bench Boost opportunity (8.16).
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Trent Alexander-Arnold -> Nathan Aké (projected gain 6.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.39) beats the best remaining Bench Boost opportunity (8.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.94 | 8.59 | 14.08 | 3.00 | 80.7 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.64 | 7.85 | 13.26 | 2.00 | 79.1 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 5.57 | 12.43 | 18.61 | 2.00 | 110.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.34 | 11.86 | 19.40 | 1.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.08 | 11.04 | 17.59 | 6.00 | 88.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.34 | 6.24 | 9.57 | 1.00 | 93.4 | 154.0 |
| Bench 4 | Bench Boost | Pedro Porro | DEF | 18 | 5.8 | 1.69 | 6.23 | 11.55 | 0.00 | 49.2 | 0.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.18 | 12.68 | 19.30 | 5.00 | 105.6 | 45.0 |
| Bench 3 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.74 | 7.83 | 14.23 | 0.00 | 32.3 | 0.0 |
| Bench 2 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 2.17 | 6.21 | 9.93 | 0.00 | 93.1 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 7.70 | 19.43 | 29.77 | 5.00 | 109.1 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.99 | 16.88 | 27.82 | 15.00 | 78.1 | 68.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.78 | 12.04 | 17.99 | 4.00 | 106.0 | 43.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.86 | 11.19 | 17.83 | 2.00 | 81.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.18 | 9.56 | 16.86 | 2.00 | 59.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 3.50 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 56.38
- Actual score: 50.00
- Transfer: Darwin Núñez Ribeiro -> Ollie Watkins (projected gain 13.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.68 | 10.04 | 16.44 | 2.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.97 | 6.99 | 11.89 | 0.00 | 78.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.97 | 13.18 | 21.33 | 0.00 | 94.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.65 | 12.71 | 19.91 | 2.00 | 89.4 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 2.88 | 8.44 | 13.40 | 6.00 | 63.2 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.35 | 6.65 | 11.48 | 0.00 | 78.6 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.05 | 3.02 | 5.79 | 0.00 | 22.2 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.54 | 19.84 | 31.65 | 9.00 | 118.7 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 3.07 | 9.13 | 16.67 | 0.00 | 25.1 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.51 | 2.39 | 4.72 | 0.00 | 12.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 8.13 | 21.77 | 33.57 | 10.00 | 104.8 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.68 | 18.28 | 28.93 | 11.00 | 110.7 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.20 | 10.45 | 17.95 | 0.00 | 63.3 | 6.0 |
| Bench 2 | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 2.08 | 6.78 | 12.03 | 0.00 | 36.7 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 2.11 | 6.56 | 12.46 | 0.00 | 52.8 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 2.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 59.26
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.07) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Son Heung-min (projected gain 11.09, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.07) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.21 | 9.01 | 14.54 | 13.00 | 92.9 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 0.66 | 1.83 | 3.51 | 7.00 | 40.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.11 | 11.97 | 19.83 | 1.00 | 88.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.07 | 11.04 | 17.35 | 6.00 | 82.7 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 2.70 | 7.92 | 13.11 | 2.00 | 75.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.39 | 7.02 | 12.01 | 5.00 | 41.1 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.7 | 0.82 | 3.85 | 8.17 | 0.00 | 7.2 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.89 | 17.21 | 26.78 | 13.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.38 | 1.85 | 4.43 | 0.00 | 13.6 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | -0.33 | 0.47 | 1.66 | 0.00 | 8.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.07 | 18.85 | 31.06 | 7.00 | 85.1 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.05 | 15.06 | 24.36 | 15.00 | 88.6 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 4.17 | 14.08 | 24.29 | 2.00 | 32.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.92 | 13.19 | 21.55 | 7.00 | 59.7 | 89.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 1.54 | 4.60 | 8.95 | 5.00 | 42.9 | 90.0 |
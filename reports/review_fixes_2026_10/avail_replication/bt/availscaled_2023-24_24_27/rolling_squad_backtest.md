# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 244.11
- Total actual points: 228.00
- Average predicted points: 61.03
- Average actual points: 57.00
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Phil Foden
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 58.76
- Actual score: 50.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.81 | 9.58 | 15.57 | 0.00 | 76.5 | 90.0 |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.81 | 8.89 | 15.13 | 1.00 | 86.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.71 | 13.15 | 21.15 | 4.00 | 91.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 4.55 | 12.82 | 21.63 | 4.00 | 71.4 | 45.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.9 | 3.91 | 11.40 | 19.00 | 2.00 | 79.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.10 | 10.73 | 17.04 | 1.00 | 78.4 | 86.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 3.55 | 10.67 | 17.17 | 12.00 | 83.0 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.53 | 14.72 | 24.11 | 6.00 | 46.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.86 | 12.40 | 20.24 | 1.00 | 85.0 | 19.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.34 | 11.17 | 18.25 | 5.00 | 69.6 | 90.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 10.8 | 5.86 | 16.41 | 26.48 | 4.00 | 51.3 | 33.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.84 | 15.79 | 25.39 | 3.00 | 93.1 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.59 | 15.02 | 23.86 | 7.00 | 72.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.71 | 13.64 | 22.05 | 10.00 | 61.8 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.4 | 4.23 | 13.36 | 21.50 | 10.00 | 73.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.60 -> 4.10
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Nathan Aké
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 68.10
- Actual score: 52.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.41) beats the best remaining Bench Boost opportunity (9.02).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Trent Alexander-Arnold -> Nathan Aké (projected gain 7.94, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.41) beats the best remaining Bench Boost opportunity (9.02).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.23 | 9.40 | 15.36 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.87 | 8.51 | 14.36 | 2.00 | 81.1 | 90.0 |
| Vice Captain | XI | Nathan Aké | DEF | 13 | 5.1 | 6.08 | 13.57 | 20.41 | 2.00 | 95.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.70 | 12.88 | 21.03 | 1.00 | 86.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.42 | 11.97 | 19.07 | 6.00 | 88.8 | 90.0 |
| Bench 3 | Bench Boost | Pedro Porro | DEF | 18 | 5.8 | 1.99 | 7.15 | 13.08 | 0.00 | 51.2 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.61 | 6.49 | 9.87 | 1.00 | 73.4 | 154.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 4.98 | 11.56 | 17.54 | 5.00 | 85.6 | 45.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.94 | 9.22 | 17.01 | 0.00 | 44.3 | 0.0 |
| Bench 2 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 2.46 | 6.26 | 9.76 | 0.00 | 78.1 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 8.38 | 21.12 | 32.38 | 5.00 | 129.1 | 180.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 4.91 | 14.05 | 22.93 | 14.00 | 81.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.71 | 11.14 | 16.66 | 4.00 | 86.0 | 43.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 2.52 | 10.71 | 18.74 | 2.00 | 39.7 | 70.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.93 | 10.18 | 15.97 | 2.00 | 61.9 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 4.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.16
- Actual score: 43.00
- Transfer: Cole Palmer -> Bukayo Saka (projected gain 15.14, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.68 | 10.03 | 16.41 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.97 | 6.98 | 11.89 | 0.00 | 81.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.96 | 13.17 | 21.30 | 0.00 | 74.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.63 | 12.64 | 19.81 | 2.00 | 90.4 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 2.88 | 8.47 | 13.44 | 6.00 | 69.2 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.39 | 7.48 | 12.48 | 0.00 | 58.6 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.08 | 4.87 | 9.71 | 0.00 | 20.2 | 0.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.97 | 8.78 | 16.40 | 0.00 | 16.1 | 0.0 |
| Bench 2 | Bench | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 2.16 | 7.91 | 13.23 | 0.00 | 21.6 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.61 | 3.73 | 7.09 | 0.00 | 10.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.98 | 21.36 | 32.94 | 10.00 | 106.8 | 75.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 6.67 | 18.25 | 28.89 | 11.00 | 98.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 5.54 | 15.57 | 25.11 | 2.00 | 92.4 | 75.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.12 | 9.32 | 15.44 | 0.00 | 43.3 | 6.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 2.36 | 8.40 | 14.05 | 0.00 | 28.7 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 63.09
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Luis Díaz (projected gain 12.42, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.69) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.54 | 9.97 | 16.09 | 13.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 0.80 | 2.30 | 4.20 | 7.00 | 24.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.50 | 13.15 | 21.71 | 1.00 | 89.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.47 | 12.17 | 19.12 | 6.00 | 83.7 | 90.0 |
| XI | XI | Nathan Aké | DEF | 13 | 5.1 | 3.00 | 8.77 | 14.48 | 2.00 | 78.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.67 | 7.91 | 13.60 | 5.00 | 54.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.7 | 0.33 | 2.98 | 7.31 | 0.00 | 0.0 | 0.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 2.15 | 8.46 | 15.85 | 5.00 | 23.8 | 30.0 |
| Bench 2 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.49 | 2.33 | 4.91 | 0.00 | 6.6 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.22 | 1.71 | 3.43 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.69 | 20.63 | 33.87 | 7.00 | 84.1 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.62 | 16.63 | 26.78 | 15.00 | 87.6 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 4.47 | 15.46 | 26.89 | 2.00 | 19.5 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.4 | 4.97 | 13.97 | 23.91 | 10.00 | 74.6 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.5 | 4.63 | 13.66 | 21.64 | 3.00 | 30.2 | 90.0 |
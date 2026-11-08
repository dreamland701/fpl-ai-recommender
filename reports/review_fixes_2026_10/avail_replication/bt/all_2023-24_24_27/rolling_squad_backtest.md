# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 208.81
- Total actual points: 236.00
- Average predicted points: 52.20
- Average actual points: 59.00
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
- Captain: Phil Foden
- Vice captain: Matheus Santos Carneiro Da Cunha
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 47.08
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.48 | 7.80 | 13.37 | 1.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.2 | 2.28 | 7.69 | 12.70 | 0.00 | 76.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.41 | 10.65 | 18.15 | 4.00 | 91.4 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.9 | 3.06 | 9.47 | 15.68 | 2.00 | 79.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 3.35 | 9.45 | 15.70 | 4.00 | 71.4 | 45.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.27 | 8.57 | 13.07 | 1.00 | 78.4 | 86.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 5.6 | 2.94 | 8.43 | 13.71 | 12.00 | 83.0 | 90.0 |
| Vice Captain | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.8 | 4.66 | 12.30 | 19.24 | 1.00 | 85.0 | 19.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 3.93 | 10.55 | 16.74 | 6.00 | 46.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.43 | 8.98 | 14.05 | 5.00 | 69.6 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 3.95 | 14.16 | 23.75 | 15.00 | 55.6 | 66.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 4.84 | 13.09 | 21.19 | 3.00 | 93.1 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.48 | 12.70 | 19.99 | 7.00 | 72.3 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.26 | 12.67 | 19.77 | 4.00 | 51.3 | 33.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 3.61 | 9.64 | 16.05 | 10.00 | 61.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Diogo Teixeira da Silva
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 58.79
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.59) beats the best remaining Bench Boost opportunity (7.00).
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 6.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.59) beats the best remaining Bench Boost opportunity (7.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.56 | 7.29 | 11.93 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.48 | 6.83 | 11.39 | 2.00 | 81.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.62 | 10.87 | 16.67 | 6.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 3.64 | 10.28 | 15.61 | 6.00 | 88.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.35 | 10.14 | 16.81 | 1.00 | 86.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.91 | 6.94 | 10.67 | 1.00 | 73.4 | 154.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.6 | 1.70 | 5.20 | 10.49 | 0.00 | 31.4 | 0.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.48 | 12.68 | 19.30 | 5.00 | 85.6 | 45.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 2.82 | 6.71 | 10.73 | 0.00 | 78.1 | 0.0 |
| Bench 4 | Bench Boost | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 1.12 | 5.07 | 9.38 | 0.00 | 44.3 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.31 | 15.96 | 23.81 | 5.00 | 129.1 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.11 | 15.41 | 25.80 | 15.00 | 58.1 | 68.0 |
| Vice Captain | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.48 | 13.54 | 20.49 | 4.00 | 86.0 | 43.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.76 | 12.69 | 20.53 | 2.00 | 61.9 | 90.0 |
| Bench 3 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 1.15 | 6.39 | 12.19 | 2.00 | 39.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 47.54
- Actual score: 39.00
- Transfer: Darwin Núñez Ribeiro -> Ivan Toney (projected gain 7.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.98 | 8.73 | 13.81 | 2.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.50 | 5.35 | 8.89 | 0.00 | 81.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 3.52 | 10.82 | 16.63 | 2.00 | 82.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.80 | 10.76 | 16.59 | 2.00 | 90.4 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 2.56 | 9.17 | 15.30 | 0.00 | 74.2 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 2.35 | 6.58 | 11.48 | 0.00 | 58.6 | 0.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.6 | 1.29 | 5.02 | 9.77 | 0.00 | 7.8 | 0.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 3.88 | 13.12 | 21.05 | 2.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 2.02 | 5.87 | 10.62 | 0.00 | 16.1 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.51 | 3.25 | 5.66 | 0.00 | 10.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.18 | 18.76 | 29.04 | 10.00 | 106.8 | 75.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.67 | 15.25 | 22.89 | 11.00 | 98.7 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 3.54 | 12.45 | 20.95 | 0.00 | 43.3 | 6.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 2.43 | 9.78 | 16.13 | 0.00 | 28.7 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 2.46 | 8.96 | 15.26 | 0.00 | 39.8 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 55.39
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.25) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 7.40, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.25) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.94 | 8.67 | 13.49 | 13.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 0.73 | 2.14 | 4.60 | 7.00 | 24.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.96 | 11.91 | 18.99 | 1.00 | 89.5 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.23 | 10.84 | 15.91 | 6.00 | 83.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 3.74 | 9.71 | 14.25 | 6.00 | 79.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 1.85 | 4.75 | 7.81 | 5.00 | 54.1 | 90.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.5 | 1.17 | 4.42 | 7.81 | 0.00 | 5.2 | 0.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.2 | 3.07 | 10.39 | 17.01 | 2.00 | 75.8 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.6 | 0.41 | 2.39 | 5.48 | 0.00 | 6.6 | 0.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | -0.23 | 1.15 | 2.82 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 7.25 | 18.00 | 29.53 | 7.00 | 84.1 | 45.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 4.82 | 14.33 | 23.78 | 15.00 | 87.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.23 | 11.29 | 17.68 | 5.00 | 91.9 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 2.69 | 9.74 | 16.21 | 2.00 | 19.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 2.12 | 6.80 | 11.85 | 5.00 | 24.9 | 90.0 |
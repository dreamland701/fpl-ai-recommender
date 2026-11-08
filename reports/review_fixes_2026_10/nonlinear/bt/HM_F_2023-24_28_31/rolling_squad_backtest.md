# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 239.71
- Total actual points: 241.00
- Average predicted points: 59.93
- Average actual points: 60.25
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
- Bank: 100.00 -> 1.30
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Bukayo Saka
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.10
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.20) beats the best remaining Bench Boost opportunity (12.39).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.20) beats the best remaining Bench Boost opportunity (12.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 4.17 | 11.27 | 18.27 | 2.00 | 85.0 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.74 | 10.44 | 15.65 | 4.00 | 172.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.81 | 12.94 | 20.20 | 2.00 | 86.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.71 | 12.55 | 19.28 | 5.00 | 157.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.46 | 11.83 | 18.48 | 1.00 | 85.6 | 90.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.18 | 10.47 | 17.10 | 2.00 | 86.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.66 | 9.84 | 14.49 | 8.00 | 165.9 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.53 | 19.16 | 30.74 | 2.00 | 85.6 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.80 | 17.60 | 26.18 | 8.00 | 155.8 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.63 | 12.35 | 19.68 | 4.00 | 147.7 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.58 | 19.03 | 32.05 | 2.00 | 63.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.68 | 29.50 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 14.63 | 23.50 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench Boost | Kevin De Bruyne | MID | 13 | 10.6 | 3.59 | 12.54 | 21.34 | 6.00 | 70.3 | 68.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.7 | 4.00 | 11.34 | 18.71 | 13.00 | 79.2 | 85.0 |

## GW29

- Train rows: 125157
- Bank: 1.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 60.33
- Actual score: 11.00
- Transfer: Alphonse Areola -> Mark Flekken (projected gain 3.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 4.49 | 11.58 | 17.56 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.76 | 9.60 | 16.16 | 0.00 | 2.8 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.11 | 16.46 | 24.61 | 1.00 | 84.2 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.38 | 11.29 | 18.78 | 0.00 | 1.4 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.04 | 10.19 | 16.83 | 0.00 | 0.7 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.85 | 9.46 | 15.37 | 0.00 | 1.5 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.42 | 8.96 | 15.52 | 0.00 | 1.4 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.43 | 17.81 | 28.91 | 2.00 | 85.3 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.31 | 14.68 | 22.05 | 2.00 | 80.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.06 | 13.80 | 22.84 | 0.00 | 1.2 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.65 | 18.45 | 31.40 | 0.00 | 1.7 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.70 | 18.26 | 27.90 | 2.00 | 87.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.80 | 15.40 | 25.24 | 0.00 | 2.6 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 3.66 | 12.62 | 21.92 | 0.00 | 2.2 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.25 | 10.68 | 18.26 | 0.00 | 1.3 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Cole Palmer
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 35.73
- Actual score: 58.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 4.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.39 | 10.54 | 17.19 | 2.00 | 87.3 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 1.81 | 5.71 | 9.86 | 2.00 | 75.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.83 | 8.36 | 13.83 | 1.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.18 | 7.74 | 13.21 | 7.00 | 81.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.56 | 6.09 | 10.38 | 6.00 | 71.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.01 | 5.84 | 9.70 | 2.00 | 69.2 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.68 | 4.97 | 10.04 | 2.00 | 42.5 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 4.82 | 15.59 | 26.38 | 1.00 | 74.6 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.53 | 8.64 | 15.24 | 7.00 | 55.5 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.11 | 5.94 | 10.99 | 2.00 | 61.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.20 | 12.67 | 21.89 | 3.00 | 56.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.61 | 11.63 | 19.35 | 3.00 | 85.0 | 60.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.7 | 4.35 | 11.12 | 17.95 | 15.00 | 85.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 1.43 | 7.72 | 14.56 | 10.00 | 66.7 | 90.0 |
| Bench 2 | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 1.43 | 7.51 | 14.02 | 3.00 | 66.1 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 1.30 -> 2.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Alexander Isak
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 58.56
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 5.03, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Illia Zabarnyi replaced Bukayo Saka.
- Autosub: Alfie Doughty replaced Kevin De Bruyne.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.71 | 7.84 | 12.84 | 7.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.44 | 7.73 | 13.33 | 0.00 | 50.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.15 | 10.96 | 17.94 | 7.00 | 80.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.62 | 15.58 | 6.00 | 78.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.54 | 9.57 | 15.64 | 2.00 | 78.7 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.40 | 8.42 | 14.32 | 1.00 | 67.4 | 90.0 |
| Bench 2 | Autosub In | Illia Zabarnyi | DEF | 3 | 4.5 | 2.78 | 7.85 | 12.60 | 7.00 | 83.7 | 90.0 |
| Vice Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 4.88 | 12.79 | 19.78 | 8.00 | 80.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.55 | 12.65 | 20.14 | 2.00 | 82.3 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.1 | 2.36 | 7.99 | 13.36 | 2.00 | 72.1 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 16.34 | 26.71 | 0.00 | 71.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.32 | 13.23 | 22.14 | 5.00 | 83.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.59 | 13.08 | 20.51 | 20.00 | 81.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.80 | 11.95 | 20.09 | 20.00 | 64.6 | 79.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 3.69 | 11.29 | 19.40 | 0.00 | 65.1 | 0.0 |
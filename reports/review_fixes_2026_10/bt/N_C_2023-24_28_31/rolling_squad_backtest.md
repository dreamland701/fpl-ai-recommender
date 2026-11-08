# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 242.20
- Total actual points: 217.00
- Average predicted points: 60.55
- Average actual points: 54.25
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Ollie Watkins
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 84.06
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.43) beats the best remaining Bench Boost opportunity (12.07).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.43) beats the best remaining Bench Boost opportunity (12.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 4.03 | 11.02 | 18.07 | 2.00 | 100.1 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.62 | 10.28 | 15.60 | 4.00 | 117.2 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.60 | 12.55 | 19.79 | 2.00 | 84.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.54 | 12.32 | 18.90 | 5.00 | 112.8 | 180.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.51 | 10.93 | 17.95 | 2.00 | 87.7 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.65 | 9.84 | 14.61 | 8.00 | 114.9 | 180.0 |
| Bench 4 | Bench Boost | Fabian Schär | DEF | 15 | 5.4 | 3.11 | 9.12 | 15.11 | 1.00 | 81.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.78 | 19.52 | 31.48 | 2.00 | 100.9 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.58 | 17.58 | 25.79 | 8.00 | 129.5 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.38 | 12.21 | 19.36 | 4.00 | 105.7 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.36 | 19.05 | 30.28 | 2.00 | 99.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 5.94 | 18.19 | 30.68 | 2.00 | 63.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.03 | 14.19 | 22.91 | 2.00 | 96.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.82 | 14.16 | 23.04 | 2.00 | 75.4 | 90.0 |
| Bench 2 | Bench Boost | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.52 | 13.11 | 21.53 | 11.00 | 89.0 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 62.11
- Actual score: 13.00
- Transfer: Fabian Schär -> Pedro Porro (projected gain 3.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.73 | 9.54 | 16.06 | 0.00 | 96.6 | 0.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.90 | 9.26 | 15.68 | 3.00 | 83.3 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.39 | 16.74 | 25.22 | 1.00 | 127.6 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 5.23 | 12.82 | 19.25 | 1.00 | 100.0 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.40 | 11.32 | 18.83 | 0.00 | 70.9 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.82 | 9.38 | 15.24 | 0.00 | 86.8 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.43 | 8.97 | 15.54 | 0.00 | 58.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.39 | 18.34 | 29.88 | 2.00 | 100.6 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.68 | 14.95 | 22.67 | 2.00 | 109.9 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.05 | 13.71 | 22.70 | 0.00 | 66.7 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.70 | 18.54 | 31.55 | 0.00 | 69.3 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.95 | 18.53 | 28.47 | 2.00 | 127.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.75 | 15.37 | 25.17 | 0.00 | 67.1 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 3.72 | 12.72 | 21.38 | 0.00 | 61.5 | 0.0 |
| Bench 2 | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.55 | 11.96 | 20.70 | 0.00 | 65.8 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.40 -> 2.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Cole Palmer
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 40.77
- Actual score: 47.00
- Transfer: Jarrod Bowen -> Cole Palmer (projected gain 6.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.30 | 10.32 | 17.03 | 2.00 | 94.1 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 1.83 | 5.67 | 9.97 | 2.00 | 57.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.95 | 8.49 | 14.15 | 1.00 | 57.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.35 | 7.91 | 13.59 | 7.00 | 50.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.04 | 5.82 | 9.81 | 2.00 | 53.8 | 90.0 |
| Bench 2 | Bench | Pedro Porro | DEF | 18 | 5.8 | 1.40 | 4.83 | 8.91 | 2.00 | 31.4 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.66 | 4.78 | 9.93 | 2.00 | 34.3 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.16 | 15.91 | 27.04 | 1.00 | 80.4 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.65 | 8.76 | 15.53 | 7.00 | 35.5 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.11 | 5.71 | 10.83 | 2.00 | 43.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.78 | 13.02 | 22.64 | 3.00 | 39.1 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.42 | 12.09 | 20.39 | 3.00 | 47.9 | 60.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.8 | 4.24 | 11.13 | 18.07 | 15.00 | 67.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.78 | 9.59 | 16.50 | 3.00 | 44.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 2.94 | 9.17 | 15.86 | 2.00 | 48.6 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 2.50 -> 2.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Dominic Solanke
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 55.26
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Rodrigo Muniz Carvalho (projected gain 2.79, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.67) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Illia Zabarnyi replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.72 | 7.83 | 12.86 | 7.00 | 80.3 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.43 | 7.70 | 13.26 | 0.00 | 63.6 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.97 | 10.77 | 17.64 | 7.00 | 76.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.51 | 9.54 | 15.57 | 2.00 | 70.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 2.98 | 8.55 | 13.69 | 2.00 | 68.0 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 2.44 | 8.27 | 14.10 | 1.00 | 75.1 | 90.0 |
| Bench 2 | Autosub In | Illia Zabarnyi | DEF | 3 | 4.5 | 2.84 | 7.86 | 12.65 | 7.00 | 75.7 | 90.0 |
| Vice Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 4.76 | 12.78 | 20.38 | 2.00 | 78.3 | 89.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.96 | 10.61 | 16.31 | 2.00 | 67.8 | 90.0 |
| Bench 4 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.08 | 9.45 | 18.29 | 0.00 | 36.0 | 0.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 5.67 | 16.04 | 26.22 | 0.00 | 72.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.74 | 13.33 | 20.94 | 20.00 | 74.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.83 | 12.18 | 20.43 | 20.00 | 58.5 | 79.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.81 | 11.60 | 19.38 | 8.00 | 74.2 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 3.96 | 11.43 | 19.02 | 11.00 | 66.6 | 90.0 |
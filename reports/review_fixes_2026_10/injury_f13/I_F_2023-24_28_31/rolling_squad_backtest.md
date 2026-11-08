# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 240.21
- Total actual points: 234.00
- Average predicted points: 60.05
- Average actual points: 58.50
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
- Predicted score: 85.25
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.22) beats the best remaining Bench Boost opportunity (12.40).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.22) beats the best remaining Bench Boost opportunity (12.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 4.16 | 11.34 | 18.41 | 2.00 | 97.6 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.74 | 10.41 | 15.60 | 4.00 | 114.4 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.81 | 12.91 | 20.14 | 2.00 | 84.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.72 | 12.58 | 19.32 | 5.00 | 115.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.46 | 11.79 | 18.41 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.19 | 10.44 | 17.03 | 2.00 | 84.7 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.67 | 9.78 | 14.35 | 8.00 | 112.8 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.55 | 19.17 | 30.74 | 2.00 | 98.8 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.83 | 17.61 | 26.14 | 8.00 | 126.5 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.63 | 12.42 | 19.82 | 4.00 | 108.8 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.60 | 19.06 | 32.08 | 2.00 | 62.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.66 | 29.48 | 2.00 | 99.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.35 | 14.62 | 23.44 | 2.00 | 94.0 | 90.0 |
| Bench 3 | Bench Boost | Kevin De Bruyne | MID | 13 | 10.6 | 3.61 | 12.66 | 21.51 | 6.00 | 51.6 | 68.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.7 | 3.99 | 11.32 | 18.68 | 13.00 | 70.0 | 85.0 |

## GW29

- Train rows: 125157
- Bank: 1.30 -> 1.10
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 60.46
- Actual score: 11.00
- Transfer: Alphonse Areola -> Mark Flekken (projected gain 2.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 4.49 | 11.63 | 17.67 | 2.00 | 110.3 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 2.75 | 9.59 | 16.14 | 0.00 | 97.2 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.12 | 16.49 | 24.66 | 1.00 | 122.8 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.38 | 11.27 | 18.74 | 0.00 | 70.6 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.04 | 10.17 | 16.78 | 0.00 | 62.3 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.86 | 9.42 | 15.27 | 0.00 | 87.5 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 2.43 | 8.94 | 15.48 | 0.00 | 57.8 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.45 | 17.82 | 28.90 | 2.00 | 97.8 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.31 | 14.75 | 22.17 | 2.00 | 105.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.08 | 13.83 | 22.84 | 0.00 | 67.5 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.66 | 18.49 | 31.44 | 0.00 | 68.1 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.72 | 18.26 | 27.84 | 2.00 | 121.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.79 | 15.40 | 25.25 | 0.00 | 67.4 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 3.69 | 12.75 | 22.11 | 0.00 | 44.9 | 0.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.7 | 3.25 | 10.67 | 18.25 | 0.00 | 57.1 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.10 -> 1.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Cole Palmer
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 35.82
- Actual score: 51.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 4.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.39 | 10.60 | 17.32 | 2.00 | 93.3 | 45.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 1.81 | 5.69 | 9.81 | 2.00 | 56.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 2.83 | 8.34 | 13.77 | 1.00 | 56.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.18 | 7.71 | 13.16 | 7.00 | 48.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.56 | 6.06 | 10.31 | 6.00 | 38.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.01 | 5.79 | 9.58 | 2.00 | 52.5 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.69 | 5.00 | 10.09 | 2.00 | 34.5 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 4.84 | 15.60 | 26.36 | 1.00 | 76.0 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.55 | 8.66 | 15.22 | 7.00 | 32.6 | 84.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.11 | 5.99 | 11.10 | 2.00 | 43.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.21 | 12.68 | 21.88 | 3.00 | 33.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.61 | 11.63 | 19.34 | 3.00 | 40.8 | 60.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 5.7 | 4.34 | 11.10 | 17.93 | 15.00 | 67.9 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 1.45 | 7.71 | 14.49 | 10.00 | 34.1 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 1.46 | 7.63 | 14.19 | 3.00 | 15.8 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 1.30 -> 2.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Alexander Isak
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 58.68
- Actual score: 101.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 5.06, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.20) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Illia Zabarnyi replaced Bukayo Saka.
- Autosub: Alfie Doughty replaced Kevin De Bruyne.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.71 | 7.82 | 12.79 | 7.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.43 | 7.79 | 13.45 | 0.00 | 63.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.16 | 10.93 | 17.88 | 7.00 | 77.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.59 | 15.51 | 6.00 | 70.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 3.55 | 9.55 | 15.57 | 2.00 | 71.4 | 90.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.41 | 8.46 | 14.36 | 1.00 | 76.5 | 90.0 |
| Bench 2 | Autosub In | Illia Zabarnyi | DEF | 3 | 4.5 | 2.79 | 7.79 | 12.47 | 7.00 | 75.5 | 90.0 |
| Vice Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 4.87 | 12.77 | 19.76 | 8.00 | 80.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.57 | 12.65 | 20.09 | 2.00 | 76.2 | 89.0 |
| Bench 4 | Bench | Carlton Morris | FWD | 12 | 5.1 | 2.36 | 8.04 | 13.44 | 2.00 | 75.5 | 90.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.20 | 16.33 | 26.68 | 0.00 | 76.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.34 | 13.22 | 22.07 | 5.00 | 84.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.59 | 13.07 | 20.50 | 20.00 | 72.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.81 | 11.93 | 20.05 | 20.00 | 56.5 | 79.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 3.72 | 11.39 | 19.54 | 0.00 | 59.3 | 0.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 249.84
- Total actual points: 213.00
- Average predicted points: 62.46
- Average actual points: 53.25
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
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Bukayo Saka
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.88
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.98) beats the best remaining Bench Boost opportunity (12.39).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.60): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.98) beats the best remaining Bench Boost opportunity (12.39).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 4.17 | 11.27 | 18.27 | 2.00 | 98.0 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.74 | 10.44 | 15.65 | 4.00 | 114.2 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.81 | 12.94 | 20.20 | 2.00 | 83.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.71 | 12.55 | 19.28 | 5.00 | 115.9 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.46 | 11.83 | 18.48 | 1.00 | 75.4 | 90.0 |
| Bench 4 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.18 | 10.47 | 17.10 | 2.00 | 84.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.66 | 9.84 | 14.49 | 8.00 | 112.8 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.53 | 19.16 | 30.74 | 2.00 | 99.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.80 | 17.60 | 26.18 | 8.00 | 126.7 | 180.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.63 | 12.35 | 19.68 | 4.00 | 109.3 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.58 | 19.03 | 32.05 | 2.00 | 63.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.68 | 29.50 | 2.00 | 99.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 14.63 | 23.50 | 2.00 | 94.2 | 90.0 |
| Bench 2 | Bench Boost | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.34 | 12.73 | 20.79 | 11.00 | 84.3 | 90.0 |
| Bench 3 | Bench Boost | Marcus Rashford | MID | 14 | 8.4 | 4.02 | 11.42 | 18.76 | 8.00 | 75.0 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Ivan Toney
- Effective captain: Son Heung-min
- Chip used: wildcard
- Predicted score: 73.05
- Actual score: 18.00
- Transfer: none
- Chip used: Wildcard — full rebuild projects +20.87 squad value (threshold 12).
- Autosub: Mads Roerslev Rasmussen replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 4.49 | 11.58 | 17.56 | 2.00 | 110.8 | 90.0 |
| Bench 1 | Bench | Thomas Kaminski | GK | 12 | 4.5 | 3.62 | 10.14 | 16.16 | 2.00 | 111.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.11 | 16.46 | 24.61 | 1.00 | 123.5 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.86 | 12.06 | 17.96 | 1.00 | 92.4 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.38 | 11.29 | 18.78 | 0.00 | 70.5 | 0.0 |
| Bench 4 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.85 | 9.46 | 15.37 | 0.00 | 87.6 | 0.0 |
| Bench 3 | Autosub In | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 3.34 | 8.78 | 13.89 | 1.00 | 76.3 | 58.0 |
| Vice Captain | XI | Ivan Toney | FWD | 4 | 8.2 | 7.42 | 18.42 | 28.08 | 1.00 | 130.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.43 | 17.81 | 28.91 | 2.00 | 98.0 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 5.31 | 14.68 | 22.05 | 2.00 | 105.7 | 90.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 10.0 | 8.04 | 20.93 | 31.08 | 2.00 | 129.2 | 86.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.65 | 18.45 | 31.40 | 0.00 | 68.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 6.70 | 18.26 | 27.90 | 2.00 | 121.6 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 8.0 | 6.62 | 17.23 | 25.49 | 2.00 | 116.8 | 65.0 |
| Bench 2 | Bench | Phil Foden | MID | 13 | 8.2 | 4.80 | 15.40 | 25.24 | 0.00 | 67.3 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 3.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Rodrigo Muniz Carvalho
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 34.30
- Actual score: 48.00
- Transfer: Ivan Toney -> Rodrigo Muniz Carvalho (projected gain 5.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Thomas Kaminski | GK | 12 | 4.5 | 1.86 | 6.90 | 12.02 | 1.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 0.83 | 4.28 | 8.63 | 3.00 | 56.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.18 | 7.74 | 13.21 | 7.00 | 48.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.01 | 5.84 | 9.70 | 2.00 | 52.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 1.52 | 5.16 | 9.28 | 2.00 | 33.1 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.68 | 4.97 | 10.04 | 2.00 | 35.2 | 82.0 |
| Bench 2 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 1.31 | 4.96 | 8.99 | 6.00 | 49.5 | 86.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 4.82 | 15.59 | 26.38 | 1.00 | 76.1 | 45.0 |
| Vice Captain | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 4.24 | 10.40 | 16.48 | 6.00 | 64.6 | 90.0 |
| Bench 3 | Bench | Carlton Morris | FWD | 12 | 5.1 | 1.11 | 5.94 | 10.99 | 2.00 | 44.4 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.20 | 12.67 | 21.89 | 3.00 | 33.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.61 | 11.63 | 19.35 | 3.00 | 40.7 | 60.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 3.70 | 11.61 | 19.94 | 10.00 | 39.8 | 87.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 1.43 | 7.72 | 14.56 | 10.00 | 34.2 | 90.0 |
| XI | XI | James Maddison | MID | 18 | 8.0 | 1.90 | 6.87 | 13.04 | 2.00 | 24.9 | 67.0 |

## GW31

- Train rows: 126837
- Bank: 3.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Son Heung-min
- Effective captain: Son Heung-min
- Chip used: triple_captain
- Predicted score: 56.62
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlton Morris -> Alexander Isak (projected gain 5.16, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.19) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Roerslev Rasmussen replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 2.84 | 7.83 | 13.08 | 11.00 | 85.0 | 90.0 |
| Bench 1 | Bench | Thomas Kaminski | GK | 12 | 4.5 | 2.17 | 7.04 | 11.94 | 2.00 | 93.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.15 | 10.96 | 17.94 | 7.00 | 77.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.03 | 8.66 | 13.86 | 2.00 | 68.6 | 90.0 |
| Bench 3 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 2.40 | 8.42 | 14.32 | 1.00 | 77.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.78 | 7.85 | 12.60 | 7.00 | 75.5 | 90.0 |
| Bench 2 | Autosub In | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 2.61 | 7.66 | 12.36 | 6.00 | 69.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.7 | 4.88 | 12.79 | 19.78 | 8.00 | 80.0 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 4.00 | 10.53 | 16.10 | 2.00 | 68.8 | 90.0 |
| Bench 4 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 1.58 | 8.95 | 17.52 | 0.00 | 30.1 | 0.0 |
| Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 16.34 | 26.71 | 0.00 | 76.7 | 0.0 |
| Vice Captain | Captain | Son Heung-min | MID | 18 | 10.0 | 5.00 | 15.18 | 24.96 | 2.00 | 75.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.32 | 13.23 | 22.14 | 5.00 | 84.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.80 | 11.95 | 20.09 | 20.00 | 56.4 | 79.0 |
| XI | XI | James Maddison | MID | 18 | 8.0 | 3.24 | 9.83 | 16.57 | 2.00 | 60.5 | 69.0 |
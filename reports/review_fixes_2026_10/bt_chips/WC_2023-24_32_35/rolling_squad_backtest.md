# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 258.20
- Total actual points: 360.00
- Average predicted points: 64.55
- Average actual points: 90.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.77
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Bruno Borges Fernandes replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.06 | 8.76 | 14.28 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.6 | 2.59 | 8.07 | 13.57 | 1.00 | 87.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.96 | 11.38 | 18.63 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.50 | 10.45 | 16.79 | 5.00 | 74.9 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.42 | 9.88 | 16.08 | 6.00 | 76.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.55 | 9.54 | 14.94 | 11.00 | 74.8 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.6 | 3.13 | 9.51 | 15.65 | 1.00 | 72.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.63 | 13.25 | 19.90 | 2.00 | 74.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.41 | 11.79 | 19.75 | 2.00 | 72.3 | 90.0 |
| XI | XI | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.68 | 10.01 | 15.74 | 2.00 | 63.5 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.44 | 17.89 | 27.58 | 5.00 | 96.3 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.67 | 16.23 | 26.69 | 0.00 | 92.3 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.43 | 16.22 | 26.36 | 5.00 | 84.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.99 | 14.28 | 23.54 | 1.00 | 96.1 | 53.0 |
| Bench 2 | Autosub In | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.50 | 11.38 | 19.43 | 9.00 | 74.0 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.80 -> 1.30
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Luis Díaz
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 54.41
- Actual score: 104.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 3.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.8 | 2.85 | 8.50 | 13.80 | 9.00 | 82.9 | 90.0 |
| XI | XI | Mark Flekken | GK | 4 | 4.6 | 2.92 | 8.16 | 13.46 | 7.00 | 81.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.51 | 12.28 | 19.63 | 1.00 | 89.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.28 | 11.30 | 17.60 | 0.00 | 84.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.06 | 11.21 | 17.75 | 5.00 | 79.6 | 66.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.80 | 10.42 | 16.55 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.9 | 2.98 | 9.20 | 14.79 | 0.00 | 72.3 | 48.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.08 | 19.91 | 12.00 | 76.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.84 | 11.30 | 18.58 | 7.00 | 68.9 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 2.78 | 8.34 | 13.66 | 2.00 | 54.5 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.10 | 16.33 | 25.13 | 26.00 | 89.7 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.65 | 14.80 | 24.43 | 1.00 | 76.4 | 57.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 5.37 | 14.34 | 22.46 | 2.00 | 85.4 | 65.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.36 | 12.57 | 20.97 | 15.00 | 86.9 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.48 | 11.11 | 18.74 | 0.00 | 63.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: wildcard
- Predicted score: 71.42
- Actual score: 141.00
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Chip used: Wildcard — full rebuild projects +13.86 squad value (threshold 12).
- Autosub: Joachim Andersen replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 4.21 | 9.97 | 15.26 | 18.00 | 115.3 | 180.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 3.80 | 9.04 | 14.50 | 1.00 | 108.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 5.51 | 13.31 | 20.75 | 14.00 | 117.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 5.30 | 12.48 | 18.95 | 12.00 | 113.9 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.7 | 5.25 | 12.10 | 18.61 | 2.00 | 115.0 | 180.0 |
| Bench 3 | Bench | Fabian Schär | DEF | 15 | 5.6 | 3.82 | 10.33 | 16.71 | 1.00 | 89.9 | 90.0 |
| Bench 2 | Autosub In | Joachim Andersen | DEF | 8 | 4.7 | 4.57 | 10.32 | 15.64 | 11.00 | 115.9 | 180.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 6.05 | 14.79 | 23.27 | 8.00 | 124.0 | 176.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 5.0 | 5.25 | 11.18 | 16.14 | 29.00 | 114.7 | 157.0 |
| Bench 4 | Bench | Julián Álvarez | FWD | 13 | 6.4 | 3.78 | 10.25 | 15.28 | 6.00 | 59.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.5 | 8.01 | 20.30 | 31.76 | 3.00 | 120.3 | 106.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.67 | 18.56 | 28.36 | 9.00 | 122.9 | 171.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.2 | 4.80 | 16.02 | 25.24 | 0.00 | 84.3 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.33 | 14.36 | 23.18 | 18.00 | 97.4 | 90.0 |
| XI | XI | Eberechi Eze | MID | 8 | 6.1 | 6.02 | 13.52 | 20.13 | 14.00 | 118.6 | 162.0 |

## GW35

- Train rows: 130234
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bukayo Saka
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 74.60
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.52) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Eberechi Eze -> Anthony Gordon (projected gain 1.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.52) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.72 | 10.85 | 17.45 | 10.00 | 112.2 | 90.0 |
| Bench 1 | Bench Boost | Norberto Murara Neto | GK | 3 | 4.7 | 2.39 | 6.82 | 11.23 | 0.00 | 71.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.9 | 4.86 | 14.13 | 22.41 | 1.00 | 115.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.4 | 4.67 | 13.35 | 20.83 | 1.00 | 111.5 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.7 | 4.03 | 11.61 | 18.34 | 1.00 | 101.8 | 90.0 |
| Bench 2 | Bench Boost | Joachim Andersen | DEF | 8 | 4.7 | 4.14 | 11.40 | 17.96 | 1.00 | 112.1 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.6 | 4.27 | 11.06 | 17.51 | 1.00 | 87.4 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.69 | 13.64 | 21.45 | 2.00 | 94.9 | 90.0 |
| XI | XI | Jean-Philippe Mateta | FWD | 8 | 5.0 | 4.47 | 11.52 | 17.73 | 2.00 | 92.9 | 68.0 |
| Bench 4 | Bench Boost | Julián Álvarez | FWD | 13 | 6.4 | 3.97 | 10.77 | 16.62 | 2.00 | 61.9 | 88.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.3 | 6.12 | 17.42 | 28.05 | 4.00 | 111.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.96 | 17.22 | 27.48 | 12.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.2 | 5.25 | 14.97 | 24.19 | 8.00 | 79.4 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 4.73 | 14.71 | 24.71 | 1.00 | 52.1 | 11.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.2 | 5.18 | 12.93 | 19.86 | 10.00 | 79.6 | 81.0 |
# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1073.20
- Total actual points: 1056.00
- Average predicted points: 56.48
- Average actual points: 55.58
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.85
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Eddie Nketiah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.86 | 10.51 | 16.43 | 2.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.5 | 3.38 | 9.32 | 14.78 | 4.00 | 83.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.31 | 15.42 | 24.71 | 1.00 | 90.4 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.0 | 3.84 | 10.90 | 17.28 | 1.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.2 | 3.67 | 10.08 | 15.91 | 9.00 | 82.3 | 90.0 |
| XI | XI | Matty Cash | DEF | -1 | 5.2 | 3.78 | 9.91 | 15.14 | 2.00 | 70.0 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 3.24 | 8.82 | 13.95 | 1.00 | 81.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.4 | 5.78 | 16.57 | 25.82 | 6.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Eddie Nketiah | FWD | -1 | 5.6 | 3.34 | 9.34 | 14.58 | 1.00 | 63.2 | 9.0 |
| Bench 4 | Bench | Cameron Archer | FWD | -1 | 4.5 | 3.08 | 8.79 | 13.98 | 2.00 | 74.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.9 | 6.20 | 17.60 | 27.67 | 16.00 | 84.8 | 90.0 |
| XI | XI | Son Heung-min | MID | -1 | 9.6 | 5.33 | 15.20 | 24.68 | 2.00 | 80.0 | 90.0 |
| XI | Bench | James Maddison | MID | -1 | 8.1 | 4.81 | 14.04 | 22.53 | 0.00 | 68.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.7 | 4.29 | 13.71 | 21.80 | 2.00 | 87.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.4 | 4.78 | 13.14 | 20.62 | 8.00 | 84.4 | 90.0 |

## GW13

- Train rows: 112534
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.96
- Actual score: 34.00
- Transfer: James Maddison -> Phil Foden (projected gain 3.15, hit 0)
- Autosub outfielders: Cameron Archer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.78 | 10.52 | 16.44 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.5 | 3.13 | 8.96 | 14.42 | 3.00 | 84.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.00 | 14.73 | 23.55 | 1.00 | 89.8 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 11.60 | 17.94 | 6.00 | 86.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.1 | 3.71 | 10.50 | 16.69 | 1.00 | 85.7 | 90.0 |
| XI | XI | Matty Cash | DEF | -1 | 5.2 | 3.54 | 10.09 | 15.41 | 0.00 | 75.0 | 45.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.6 | 2.80 | 8.36 | 13.55 | 1.00 | 72.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.4 | 5.76 | 16.63 | 25.06 | 5.00 | 89.7 | 90.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | -1 | 5.7 | 2.74 | 8.21 | 12.99 | 1.00 | 46.4 | 24.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | -1 | 4.6 | 2.97 | 8.06 | 12.87 | 2.00 | 72.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 12.9 | 6.01 | 18.76 | 29.81 | 5.00 | 91.2 | 90.0 |
| XI | XI | Son Heung-min | MID | -1 | 9.7 | 4.81 | 14.14 | 22.74 | 2.00 | 80.1 | 90.0 |
| XI | Bench | Jarrod Bowen | MID | -1 | 7.6 | 4.95 | 13.94 | 21.63 | 0.00 | 83.4 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.8 | 4.31 | 12.94 | 20.49 | 2.00 | 81.1 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.5 | 3.89 | 11.15 | 17.18 | 2.00 | 79.4 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.14
- Actual score: 65.00
- Transfer: Jarrod Bowen -> Bruno Borges Fernandes (projected gain 2.04, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.83 | 10.56 | 16.59 | 2.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.5 | 3.06 | 8.92 | 14.38 | 6.00 | 82.6 | 85.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 4.93 | 14.19 | 22.79 | 12.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.4 | 4.38 | 12.05 | 18.82 | 1.00 | 83.6 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.2 | 3.67 | 10.57 | 16.58 | 2.00 | 85.1 | 90.0 |
| Bench 2 | Bench | Matty Cash | DEF | -1 | 5.1 | 2.94 | 8.52 | 13.87 | 1.00 | 56.3 | 16.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.7 | 2.76 | 8.16 | 13.14 | 2.00 | 77.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.85 | 16.23 | 24.92 | 11.00 | 89.0 | 90.0 |
| XI | XI | Cameron Archer | FWD | -1 | 4.6 | 3.00 | 8.33 | 13.27 | 1.00 | 75.0 | 45.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | -1 | 5.7 | 2.46 | 7.19 | 11.90 | 1.00 | 39.3 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.0 | 6.29 | 18.34 | 29.42 | 5.00 | 87.6 | 90.0 |
| XI | XI | Son Heung-min | MID | -1 | 9.7 | 4.41 | 14.06 | 22.84 | 10.00 | 81.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 6.9 | 4.75 | 13.54 | 21.56 | 5.00 | 74.5 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.3 | 3.96 | 12.21 | 19.44 | 2.00 | 83.9 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.5 | 3.78 | 10.90 | 17.57 | 9.00 | 74.5 | 72.0 |

## GW15

- Train rows: 114034
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.25
- Actual score: 22.00
- Transfer: Matty Cash -> Konstantinos Tsimikas (projected gain 1.92, hit 0)
- Autosub outfielders: Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | -1 | 4.3 | 3.35 | 10.04 | 15.86 | 0.00 | 88.8 | 0.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.5 | 3.10 | 8.83 | 14.23 | 0.00 | 80.5 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 7.0 | 5.51 | 15.06 | 23.67 | 1.00 | 95.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 4.21 | 11.64 | 18.27 | 1.00 | 83.9 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.2 | 3.77 | 10.31 | 16.38 | 1.00 | 84.4 | 90.0 |
| XI | Bench | Konstantinos Tsimikas | DEF | -1 | 4.8 | 3.57 | 9.75 | 15.17 | 0.00 | 73.3 | 0.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.7 | 2.92 | 7.91 | 12.68 | 1.00 | 76.8 | 28.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.20 | 15.23 | 24.53 | 1.00 | 87.2 | 89.0 |
| Bench 3 | Bench | Cameron Archer | FWD | -1 | 4.6 | 2.45 | 7.19 | 11.23 | 2.00 | 62.0 | 90.0 |
| Bench 4 | Bench | Eddie Nketiah | FWD | -1 | 5.7 | 2.11 | 6.44 | 10.97 | 0.00 | 32.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 6.39 | 18.33 | 29.21 | 3.00 | 91.3 | 66.0 |
| XI | XI | Son Heung-min | MID | -1 | 9.6 | 5.07 | 14.31 | 23.35 | 2.00 | 82.3 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | -1 | 7.1 | 4.48 | 13.29 | 21.38 | 6.00 | 68.8 | 39.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.3 | 3.93 | 11.25 | 17.83 | 0.00 | 80.8 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.5 | 3.38 | 10.31 | 16.50 | 3.00 | 69.8 | 72.0 |

## GW16

- Train rows: 114791
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 51.17
- Actual score: 60.00
- Transfer: Eddie Nketiah -> Matheus Santos Carneiro Da Cunha (projected gain 1.96, hit 0)
- Autosub outfielders: Cameron Archer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | -1 | 4.3 | 2.33 | 7.29 | 12.16 | 0.00 | 53.8 | 0.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.5 | 1.52 | 5.62 | 9.87 | 0.00 | 41.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 7.0 | 4.83 | 14.31 | 22.57 | -1.00 | 93.4 | 85.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.66 | 11.13 | 17.73 | 2.00 | 84.7 | 90.0 |
| XI | XI | Joachim Andersen | DEF | -1 | 5.2 | 3.13 | 9.27 | 14.73 | 0.00 | 82.0 | 90.0 |
| Bench 3 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.8 | 2.51 | 7.41 | 12.03 | 2.00 | 42.7 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | -1 | 4.7 | 2.11 | 6.65 | 10.80 | 0.00 | 57.7 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.4 | 4.27 | 13.26 | 21.77 | 2.00 | 82.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 5.6 | 3.61 | 9.77 | 15.36 | 9.00 | 79.0 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | -1 | 4.6 | 3.02 | 7.93 | 12.11 | 2.00 | 71.0 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 6.04 | 17.41 | 27.74 | 13.00 | 79.6 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 9.6 | 5.07 | 14.41 | 22.81 | 17.00 | 87.3 | 90.0 |
| XI | Bench | Bryan Mbeumo | MID | -1 | 7.1 | 4.67 | 13.02 | 20.59 | 0.00 | 69.5 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | -1 | 8.3 | 4.06 | 11.50 | 18.26 | 1.00 | 80.3 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.5 | 3.46 | 9.89 | 15.53 | 2.00 | 66.0 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 52.90
- Actual score: 49.00
- Transfer: Joachim Andersen -> Pedro Porro (projected gain 3.12, hit 0)
- Autosub outfielders: Cameron Archer, Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | -1 | 4.3 | 2.27 | 6.76 | 11.56 | 0.00 | 40.3 | 0.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.4 | 1.61 | 5.12 | 9.16 | 0.00 | 31.7 | 0.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 7.0 | 5.03 | 14.26 | 22.79 | 0.00 | 93.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.3 | 4.09 | 11.38 | 18.03 | 8.00 | 84.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.98 | 11.21 | 17.84 | 7.00 | 83.4 | 90.0 |
| XI | XI | Konstantinos Tsimikas | DEF | -1 | 4.9 | 3.25 | 9.10 | 14.44 | 7.00 | 69.8 | 90.0 |
| Bench 4 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.7 | 0.98 | 4.26 | 7.72 | 1.00 | 37.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.4 | 4.50 | 13.35 | 22.06 | 9.00 | 79.0 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 5.6 | 3.68 | 10.70 | 16.77 | 2.00 | 84.2 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | -1 | 4.6 | 3.00 | 8.31 | 12.83 | 2.00 | 72.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.1 | 6.45 | 18.52 | 29.31 | 3.00 | 90.9 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 9.6 | 5.79 | 16.19 | 26.01 | 2.00 | 95.5 | 87.0 |
| XI | Bench | Bruno Borges Fernandes | MID | -1 | 8.3 | 3.68 | 11.48 | 18.47 | 0.00 | 79.5 | 0.0 |
| XI | XI | Phil Foden | MID | -1 | 7.6 | 3.74 | 9.93 | 15.55 | 5.00 | 69.7 | 90.0 |
| Bench 3 | Bench | Bryan Mbeumo | MID | -1 | 7.0 | 2.21 | 8.50 | 16.73 | 0.00 | 24.2 | 0.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 49.97
- Actual score: 48.00
- Transfer: Bryan Mbeumo -> Cole Palmer (projected gain 5.53, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 1.81 | 5.98 | 10.63 | 8.00 | 31.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.4 | 1.15 | 4.03 | 7.65 | 0.00 | 23.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.4 | 4.60 | 12.76 | 20.10 | 2.00 | 84.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.70 | 11.36 | 17.99 | 2.00 | 89.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 3.00 | 10.19 | 18.42 | 2.00 | 47.9 | 90.0 |
| XI | XI | Konstantinos Tsimikas | DEF | -1 | 4.9 | 2.99 | 9.20 | 14.82 | 1.00 | 74.0 | 34.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.7 | 2.41 | 6.76 | 11.05 | 1.00 | 62.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.5 | 5.25 | 15.02 | 23.81 | 2.00 | 82.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 5.7 | 3.62 | 10.29 | 16.17 | 1.00 | 78.8 | 85.0 |
| XI | XI | Cameron Archer | FWD | -1 | 4.6 | 2.77 | 8.31 | 13.08 | 8.00 | 76.6 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.2 | 5.79 | 17.90 | 28.86 | 7.00 | 83.8 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 9.7 | 5.74 | 16.64 | 26.42 | 7.00 | 83.8 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.5 | 4.92 | 13.57 | 21.22 | 1.00 | 93.5 | 90.0 |
| Bench 4 | Bench | Phil Foden | MID | -1 | 7.6 | 2.29 | 8.77 | 15.04 | 0.00 | 42.0 | 0.0 |
| Bench 2 | Bench | Bruno Borges Fernandes | MID | -1 | 8.3 | 2.68 | 8.41 | 14.37 | 1.00 | 42.9 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 1.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.11
- Actual score: 43.00
- Transfer: Phil Foden -> Bukayo Saka (projected gain 6.31, hit 0)
- Autosub outfielders: Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 2.71 | 8.69 | 14.27 | 10.00 | 67.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.4 | 1.34 | 4.12 | 7.58 | 0.00 | 22.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.67 | 13.44 | 21.57 | 1.00 | 81.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.5 | 4.17 | 12.31 | 19.37 | 5.00 | 88.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 4.14 | 11.27 | 17.71 | 1.00 | 89.1 | 90.0 |
| Bench 3 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.9 | 3.00 | 8.68 | 14.05 | 0.00 | 62.1 | 0.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | -1 | 4.7 | 2.22 | 6.82 | 11.11 | 0.00 | 66.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.7 | 4.91 | 15.22 | 24.21 | 2.00 | 81.6 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 5.7 | 3.55 | 10.20 | 16.31 | 5.00 | 74.0 | 90.0 |
| XI | XI | Cameron Archer | FWD | -1 | 4.6 | 3.53 | 9.38 | 14.68 | 5.00 | 81.2 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.2 | 6.50 | 18.83 | 30.30 | 3.00 | 91.2 | 90.0 |
| XI | XI | Son Heung-min | MID | -1 | 9.8 | 5.70 | 16.59 | 26.27 | 5.00 | 95.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 5.89 | 16.17 | 25.01 | 2.00 | 85.4 | 90.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.6 | 4.83 | 13.78 | 21.47 | 0.00 | 85.5 | 0.0 |
| Bench 2 | Autosub In | Bruno Borges Fernandes | MID | -1 | 8.2 | 3.36 | 9.94 | 16.33 | 1.00 | 66.2 | 90.0 |

## GW20

- Train rows: 117854
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.32
- Actual score: 108.00
- Transfer: Bruno Borges Fernandes -> Jarrod Bowen (projected gain 4.54, hit 0)
- Autosub outfielders: Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.78 | 10.32 | 16.51 | 11.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.4 | 0.60 | 3.16 | 6.08 | 0.00 | 19.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.6 | 4.49 | 12.57 | 19.87 | 2.00 | 92.2 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.9 | 3.88 | 11.99 | 19.55 | 0.00 | 82.5 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.5 | 3.75 | 10.90 | 17.35 | 0.00 | 87.3 | 90.0 |
| Bench 3 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.7 | 2.40 | 6.64 | 10.62 | 6.00 | 72.6 | 90.0 |
| Bench 4 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.8 | 1.55 | 5.48 | 10.53 | 0.00 | 30.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.27 | 14.41 | 22.85 | 8.00 | 86.7 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | -1 | 5.8 | 3.73 | 9.89 | 15.75 | 12.00 | 76.0 | 79.0 |
| Bench 2 | Bench | Cameron Archer | FWD | -1 | 4.6 | 2.84 | 8.83 | 13.80 | 1.00 | 77.6 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | -1 | 13.3 | 6.48 | 18.23 | 28.67 | 16.00 | 87.4 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 9.9 | 5.86 | 16.38 | 26.14 | 9.00 | 90.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.0 | 5.73 | 16.08 | 24.80 | 7.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 4.87 | 13.84 | 21.90 | 3.00 | 83.7 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.6 | 3.01 | 9.50 | 15.94 | 18.00 | 47.7 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.70
- Actual score: 38.00
- Transfer: Matheus Santos Carneiro Da Cunha -> João Pedro Junqueira de Jesus (projected gain 1.37, hit 0)
- Autosub outfielders: Cameron Archer, Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.93 | 10.94 | 17.48 | 3.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.4 | 0.54 | 2.52 | 4.82 | 0.00 | 14.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.7 | 3.74 | 11.40 | 18.50 | 6.00 | 88.4 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.79 | 10.32 | 16.36 | 6.00 | 84.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.8 | 2.74 | 8.99 | 15.76 | 1.00 | 50.4 | 90.0 |
| Bench 3 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.7 | 2.06 | 6.42 | 10.35 | 0.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.7 | 0.92 | 3.58 | 6.81 | 0.00 | 20.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.65 | 15.94 | 24.98 | 1.00 | 91.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 4.44 | 11.65 | 17.52 | 2.00 | 82.0 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | -1 | 4.5 | 2.68 | 7.56 | 12.10 | 1.00 | 53.6 | 23.0 |
| Captain | Bench | Mohamed Salah | MID | -1 | 13.3 | 7.50 | 21.11 | 32.49 | 0.00 | 100.7 | 0.0 |
| XI | Bench | Son Heung-min | MID | -1 | 9.9 | 5.71 | 16.95 | 27.29 | 0.00 | 93.4 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | -1 | 9.0 | 6.14 | 16.08 | 24.89 | 3.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.9 | 4.76 | 13.45 | 21.26 | 2.00 | 80.1 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.6 | 4.81 | 12.34 | 19.35 | 10.00 | 79.3 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 0.80 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.57
- Actual score: 52.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 5.43, hit 0)
- Autosub outfielders: Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.64 | 10.38 | 16.81 | 3.00 | 82.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.39 | 2.10 | 4.08 | 0.00 | 10.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.8 | 4.24 | 12.36 | 20.29 | 1.00 | 86.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 3.36 | 11.07 | 18.63 | 7.00 | 72.2 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.92 | 10.96 | 17.43 | 2.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.7 | 2.45 | 6.32 | 9.93 | 1.00 | 73.2 | 90.0 |
| Bench 4 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.6 | 0.64 | 2.62 | 5.18 | 0.00 | 14.5 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.9 | 5.40 | 15.58 | 24.65 | 7.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | -1 | 5.4 | 4.14 | 11.41 | 17.44 | 2.00 | 76.8 | 70.0 |
| Bench 3 | Bench | Cameron Archer | FWD | -1 | 4.5 | 2.21 | 6.39 | 10.60 | 1.00 | 45.6 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 6.08 | 17.03 | 26.66 | 10.00 | 81.1 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 7.9 | 4.80 | 14.47 | 23.61 | 6.00 | 64.2 | 76.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.7 | 4.34 | 14.16 | 23.09 | 2.00 | 69.1 | 84.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 8.1 | 4.25 | 13.09 | 22.48 | 1.00 | 65.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | -1 | 13.2 | 3.32 | 13.05 | 25.23 | 0.00 | 19.6 | 0.0 |

## GW23

- Train rows: 120213
- Bank: 2.70 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.11
- Actual score: 80.00
- Transfer: João Pedro Junqueira de Jesus -> Julián Álvarez (projected gain 4.50, hit 0)
- Autosub outfielders: Tyrick Mitchell.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.27 | 10.04 | 15.86 | 1.00 | 84.0 | 45.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.75 | 2.03 | 3.59 | 0.00 | 7.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.9 | 4.22 | 12.29 | 19.86 | 1.00 | 88.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 3.91 | 11.43 | 18.67 | 9.00 | 74.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.60 | 10.66 | 17.02 | 1.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Tyrick Mitchell | DEF | -1 | 4.6 | 2.15 | 6.36 | 10.13 | 0.00 | 73.7 | 90.0 |
| Bench 4 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.6 | 0.14 | 1.80 | 3.81 | 0.00 | 13.9 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.9 | 5.82 | 16.40 | 26.11 | 18.00 | 91.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 7.0 | 5.24 | 14.43 | 22.47 | 2.00 | 82.6 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | -1 | 4.4 | 1.55 | 5.30 | 9.57 | 1.00 | 32.4 | 25.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 5.83 | 16.61 | 26.20 | 9.00 | 88.1 | 78.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 5.04 | 14.27 | 22.67 | 8.00 | 89.2 | 90.0 |
| XI | XI | Phil Foden | MID | -1 | 8.0 | 4.55 | 13.49 | 22.01 | 20.00 | 73.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 8.1 | 3.94 | 11.99 | 20.10 | 2.00 | 71.9 | 90.0 |
| XI | Bench | Mohamed Salah | MID | -1 | 13.1 | 2.86 | 10.97 | 19.23 | 0.00 | 30.4 | 0.0 |

## GW24

- Train rows: 121022
- Bank: 1.20 -> 7.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 57.56
- Actual score: 56.00
- Transfer: Mohamed Salah -> Richarlison de Andrade (projected gain 5.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 2.90 | 9.33 | 14.72 | 0.00 | 71.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.63 | 1.98 | 3.54 | 0.00 | 6.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.7 | 4.62 | 13.14 | 20.89 | 4.00 | 88.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.9 | 4.31 | 12.16 | 19.51 | 2.00 | 88.7 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 3.53 | 10.45 | 16.73 | 12.00 | 83.6 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | -1 | 4.6 | 2.11 | 6.07 | 9.62 | 1.00 | 73.3 | 90.0 |
| Bench 4 | Bench | Konstantinos Tsimikas | DEF | -1 | 4.5 | 0.78 | 2.47 | 4.81 | 1.00 | 13.6 | 1.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 8.8 | 6.30 | 17.60 | 27.99 | 2.00 | 98.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.9 | 4.74 | 13.50 | 21.57 | 2.00 | 73.3 | 76.0 |
| Bench 3 | Bench | Cameron Archer | FWD | -1 | 4.3 | 1.94 | 6.04 | 10.33 | 7.00 | 37.9 | 80.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.0 | 5.57 | 16.30 | 25.90 | 15.00 | 79.3 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | -1 | 7.9 | 5.75 | 15.99 | 25.14 | 3.00 | 89.9 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 5.06 | 14.85 | 23.47 | 10.00 | 90.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | -1 | 7.1 | 4.85 | 12.74 | 20.08 | 2.00 | 79.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 8.0 | 3.63 | 11.22 | 18.57 | 2.00 | 72.3 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 7.10 -> 3.90
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 70.57
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.59) beats the best remaining Bench Boost opportunity (10.44).
- Transfer: Cameron Archer -> Darwin Núñez Ribeiro (projected gain 3.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.59) beats the best remaining Bench Boost opportunity (10.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.67 | 10.39 | 16.47 | 3.00 | 85.0 | 90.0 |
| Bench 1 | Bench Boost | Nick Pope | GK | -1 | 5.3 | 0.64 | 1.76 | 3.18 | 0.00 | 5.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.8 | 4.68 | 12.96 | 20.70 | 1.00 | 87.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 4.36 | 12.04 | 19.05 | 6.00 | 90.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | -1 | 5.9 | 4.06 | 11.49 | 18.39 | 0.00 | 85.6 | 0.0 |
| Bench 3 | Bench Boost | Tyrick Mitchell | DEF | -1 | 4.6 | 2.22 | 6.29 | 10.14 | 2.00 | 74.0 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Tsimikas | DEF | -1 | 4.5 | 2.20 | 4.00 | 5.74 | 0.00 | 41.3 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.8 | 5.81 | 16.97 | 27.27 | 13.00 | 91.1 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | -1 | 7.5 | 5.93 | 14.62 | 21.83 | 5.00 | 93.1 | 45.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.8 | 5.18 | 13.20 | 20.42 | 7.00 | 91.9 | 151.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 6.05 | 17.26 | 26.96 | 15.00 | 80.8 | 68.0 |
| Captain | Captain | Phil Foden | MID | -1 | 8.0 | 6.47 | 16.51 | 25.11 | 5.00 | 108.1 | 180.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.9 | 4.65 | 14.28 | 23.00 | 2.00 | 85.8 | 70.0 |
| XI | XI | Richarlison de Andrade | MID | -1 | 7.2 | 4.43 | 12.39 | 19.37 | 2.00 | 70.1 | 70.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | -1 | 7.9 | 3.72 | 10.89 | 18.01 | 2.00 | 71.4 | 90.0 |

## GW26

- Train rows: 122659
- Bank: 3.90 -> 2.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 55.84
- Actual score: 66.00
- Transfer: Konstantinos Tsimikas -> Virgil van Dijk (projected gain 6.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.98 | 10.87 | 17.55 | 2.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.00 | 1.27 | 2.60 | 0.00 | 5.8 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.07 | 12.86 | 20.71 | 0.00 | 91.9 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 3.40 | 12.86 | 20.67 | 0.00 | 86.3 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.6 | 4.26 | 12.16 | 19.20 | 2.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 2.40 | 6.59 | 10.48 | 5.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | -1 | 5.8 | 0.31 | 5.85 | 12.24 | 0.00 | 4.6 | 0.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.7 | 6.05 | 17.03 | 27.36 | 9.00 | 91.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.7 | 5.15 | 14.35 | 22.60 | 1.00 | 89.8 | 15.0 |
| XI | Bench | Darwin Núñez Ribeiro | FWD | -1 | 7.6 | 2.58 | 11.56 | 19.16 | 0.00 | 21.9 | 0.0 |
| Captain | Captain | Phil Foden | MID | -1 | 8.0 | 6.88 | 18.96 | 29.21 | 11.00 | 116.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | -1 | 9.0 | 6.34 | 18.09 | 27.59 | 10.00 | 85.0 | 75.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.8 | 2.68 | 11.62 | 20.15 | 0.00 | 38.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 3.57 | 10.01 | 16.56 | 20.00 | 71.3 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | -1 | 7.2 | 2.09 | 9.53 | 16.05 | 0.00 | 26.3 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 2.00 -> 2.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.43
- Actual score: 87.00
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 3.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 3.82 | 10.91 | 17.57 | 13.00 | 95.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.78 | 2.22 | 3.87 | 0.00 | 7.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.9 | 4.43 | 13.24 | 21.16 | 1.00 | 87.3 | 51.0 |
| XI | XI | William Saliba | DEF | -1 | 5.7 | 4.48 | 12.68 | 19.86 | 6.00 | 88.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.41 | 12.29 | 19.06 | 6.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 2.97 | 8.60 | 14.19 | 6.00 | 63.0 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 2.36 | 7.25 | 11.41 | 1.00 | 77.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | -1 | 8.8 | 6.54 | 19.25 | 29.46 | 13.00 | 96.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.7 | 3.76 | 11.15 | 18.08 | 4.00 | 56.4 | 31.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | -1 | 7.6 | 3.52 | 10.11 | 16.13 | 5.00 | 44.6 | 30.0 |
| Captain | Captain | Bukayo Saka | MID | -1 | 9.1 | 6.57 | 19.73 | 30.33 | 7.00 | 83.2 | 45.0 |
| XI | XI | Phil Foden | MID | -1 | 8.1 | 6.40 | 17.86 | 27.61 | 15.00 | 97.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.7 | 4.56 | 12.79 | 20.36 | 5.00 | 88.9 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.8 | 3.37 | 10.10 | 16.81 | 5.00 | 50.7 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | -1 | 7.2 | 2.66 | 7.72 | 12.48 | 0.00 | 33.3 | 0.0 |

## GW28

- Train rows: 124319
- Bank: 2.60 -> 3.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Phil Foden
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 70.45
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.66) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: Darwin Núñez Ribeiro -> Dominic Solanke (projected gain 3.62, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (9.66) beats the best remaining Triple Captain opportunity (9.45).
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.2 | 4.26 | 11.82 | 18.89 | 2.00 | 102.5 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.45 | 1.91 | 3.53 | 0.00 | 7.6 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.7 | 4.70 | 13.11 | 20.64 | 2.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 4.61 | 12.41 | 19.47 | 1.00 | 85.7 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.9 | 3.76 | 11.86 | 19.28 | 0.00 | 75.7 | 0.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | -1 | 6.4 | 3.45 | 10.35 | 16.83 | 2.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 2.67 | 7.17 | 11.38 | 3.00 | 75.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 8.9 | 7.16 | 19.79 | 30.67 | 2.00 | 105.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.1 | 5.83 | 14.00 | 20.72 | 8.00 | 102.3 | 180.0 |
| XI | XI | Julián Álvarez | FWD | -1 | 6.6 | 3.64 | 11.50 | 18.89 | 2.00 | 62.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | -1 | 8.1 | 6.74 | 19.64 | 30.19 | 2.00 | 105.9 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.2 | 6.37 | 18.32 | 29.42 | 2.00 | 71.2 | 90.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.7 | 4.68 | 13.50 | 21.76 | 13.00 | 78.4 | 85.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.8 | 4.40 | 12.58 | 20.37 | 2.00 | 84.7 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | -1 | 7.1 | 1.13 | 4.72 | 9.51 | 0.00 | 14.8 | 0.0 |

## GW29

- Train rows: 125157
- Bank: 3.10 -> 5.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Alfie Doughty
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 49.85
- Actual score: 10.00
- Transfer: Kieran Trippier -> Alfie Doughty (projected gain 6.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.53 | 10.49 | 17.10 | 3.00 | 94.3 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.00 | 0.65 | 2.41 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Alfie Doughty | DEF | -1 | 4.7 | 4.96 | 14.15 | 22.14 | 1.00 | 109.4 | 45.0 |
| XI | Bench | William Saliba | DEF | -1 | 5.8 | 2.95 | 11.31 | 18.97 | 0.00 | 54.2 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 2.80 | 10.74 | 17.90 | 0.00 | 50.3 | 0.0 |
| XI | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 1.79 | 8.48 | 14.90 | 0.00 | 41.5 | 0.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 1.24 | 6.21 | 10.77 | 0.00 | 43.1 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 9.0 | 6.18 | 17.43 | 27.58 | 2.00 | 95.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | -1 | 7.2 | 4.23 | 15.18 | 24.80 | 0.00 | 67.8 | 0.0 |
| Bench 2 | Bench | Julián Álvarez | FWD | -1 | 6.5 | 1.74 | 8.86 | 16.24 | 0.00 | 23.2 | 0.0 |
| XI | Bench | Bukayo Saka | MID | -1 | 9.2 | 4.88 | 16.97 | 28.35 | 0.00 | 45.1 | 0.0 |
| XI | Bench | Phil Foden | MID | -1 | 8.2 | 4.65 | 15.81 | 25.68 | 0.00 | 60.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 7.9 | 4.31 | 12.84 | 20.75 | 2.00 | 84.4 | 90.0 |
| XI | Bench | Cole Palmer | MID | -1 | 5.7 | 3.37 | 12.13 | 20.45 | 0.00 | 49.9 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | MID | -1 | 7.0 | 0.78 | 3.44 | 7.13 | 1.00 | 9.1 | 10.0 |

## GW30

- Train rows: 125995
- Bank: 5.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 49.44
- Actual score: 62.00
- Transfer: Richarlison de Andrade -> Son Heung-min (projected gain 8.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | -1 | 4.3 | 3.38 | 10.29 | 17.03 | 2.00 | 94.1 | 45.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 0.85 | 2.32 | 4.02 | 0.00 | 9.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | -1 | 4.7 | 3.52 | 12.01 | 18.64 | 2.00 | 84.3 | 82.0 |
| XI | XI | William Saliba | DEF | -1 | 5.8 | 2.67 | 8.82 | 14.92 | 7.00 | 56.1 | 90.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | -1 | 5.3 | 2.33 | 7.78 | 13.00 | 6.00 | 52.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 2.51 | 7.55 | 12.80 | 1.00 | 50.6 | 90.0 |
| Bench 4 | Bench | Tyrick Mitchell | DEF | -1 | 4.5 | 1.67 | 5.07 | 8.76 | 2.00 | 43.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | -1 | 9.0 | 5.84 | 16.77 | 27.24 | 1.00 | 88.7 | 45.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 7.2 | 3.82 | 10.83 | 17.94 | 7.00 | 56.2 | 84.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | -1 | 6.5 | 2.12 | 7.48 | 12.96 | 0.00 | 39.6 | 0.0 |
| Vice Captain | XI | Son Heung-min | MID | -1 | 10.0 | 4.98 | 16.21 | 24.74 | 10.00 | 72.0 | 87.0 |
| XI | XI | Jarrod Bowen | MID | -1 | 8.0 | 4.26 | 14.87 | 23.02 | 10.00 | 84.1 | 90.0 |
| XI | XI | Bukayo Saka | MID | -1 | 9.2 | 4.78 | 14.29 | 23.30 | 3.00 | 52.7 | 77.0 |
| XI | XI | Phil Foden | MID | -1 | 8.2 | 4.22 | 13.35 | 21.86 | 3.00 | 60.6 | 60.0 |
| XI | XI | Cole Palmer | MID | -1 | 5.7 | 3.64 | 10.17 | 17.01 | 15.00 | 55.7 | 90.0 |
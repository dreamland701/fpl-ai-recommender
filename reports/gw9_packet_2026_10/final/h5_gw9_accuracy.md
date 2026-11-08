# H5 final read (Sat 2026-10-31 09:15Z snapshot), GW9: shadow accuracy vs settled points (669 players)

| Set | n | RMSE classic | RMSE SFT | MAE classic | MAE SFT | bias classic | bias SFT |
|---|---|---|---|---|---|---|---|
| all | 669 | 1.817 | 1.831 | 1.028 | 1.119 | +0.04 | -0.13 |
| classic >= 4 | 21 | 3.682 | 3.701 | 2.976 | 2.990 | -0.62 | -0.62 |

SFT closer than classic on 43% of the classic >= 4 rows.

| P(appear) | n | Brier classic | Brier SFT | AUC classic | AUC SFT |
|---|---|---|---|---|---|
| all | 669 | 0.1300 | 0.0916 | 0.949 | 0.952 |
| classic P in [0.15, 0.9] | 302 | 0.2155 | 0.1387 | 0.765 | 0.802 |

Forecast starters (classic P >= 0.5) who did not play: 12: White (P 0.85 -> 0.93), Lacroix (P 0.77 -> 0.52), Benitez (P 0.76 -> 0.91), Guéhi (P 0.75 -> 0.93), Henderson (P 0.75 -> 0.95), Tielemans (P 0.68 -> 0.93), Mukiele (P 0.65 -> 0.72), Thomas (P 0.64 -> 0.69), Gravenberch (P 0.63 -> 0.88), Bijol (P 0.63 -> 0.42), Herrington (P 0.61 -> 0.86), Thiaw (P 0.53 -> 0.76)

## Biggest misses (actual - classic)

| Player | Pos | Min | Actual | Classic | SFT |
|---|---|---|---|---|---|
| Fofana | DEF | 90 | 11 | 0.53 | 0.42 |
| Van Hecke | DEF | 90 | 15 | 4.61 | 4.53 |
| McBurnie | FWD | 90 | 12 | 3.18 | 3.09 |
| Verbruggen | GK | 90 | 11 | 2.76 | 2.82 |
| Van den Berg | DEF | 90 | 10 | 2.35 | 2.39 |
| Ayari | MID | 90 | 10 | 2.38 | 2.39 |
| Awoniyi | FWD | 71 | 9 | 1.49 | 1.43 |
| Branthwaite | DEF | 81 | 9 | 1.50 | 1.34 |
| Adli | MID | 2 | 8 | 0.86 | 0.92 |
| Lavia | MID | 90 | 8 | 0.87 | 0.79 |

## Largest SFT-vs-classic disagreements on points

| Player | Pos | Min | Actual | Classic | SFT | SFT closer? |
|---|---|---|---|---|---|---|
| Sessegnon | DEF | 0 | 0 | 0.40 | -0.69 | no |
| Bentancur | MID | 0 | 0 | 0.40 | -0.52 | no |
| J.Rak-Sakyi | MID | 0 | 0 | 0.00 | -0.89 | no |
| Leoni | DEF | 0 | 0 | 0.00 | -0.87 | no |
| Chadi Riad | DEF | 0 | 0 | 0.00 | -0.86 | no |
| Watkins | FWD | 0 | 0 | 1.40 | 0.54 | yes |
| Ruggeri | DEF | 0 | 0 | 0.40 | -0.46 | no |
| Yarmoliuk | MID | 0 | 0 | 0.43 | -0.43 | yes |
| Dowman | MID | 0 | 0 | 0.11 | -0.74 | no |
| Lacroix | DEF | 0 | 0 | 2.93 | 2.09 | yes |

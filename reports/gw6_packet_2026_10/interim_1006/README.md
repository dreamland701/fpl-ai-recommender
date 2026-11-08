# GW6 interim refresh, 2026-10-06 (fixed pipeline)

The scheduled final refresh, after Friday's press conferences, writes `../final/README.md` on 2026-10-09 at 17:00 UTC.

- **Snapshot:** 2026-10-07T05:06:42+00:00 UTC; deadline 2026-10-10T10:00:00Z.
- **Entry 6535607:** bank £0.3m, free transfers 1, chips used: none. Transfers already made for GW6: none.
- **Selling prices vs the 10-04 app values:** all match the app.

## What moved since 2026-10-04

| Player | Status now | News now | GW6 (10-04 → now) | GW6–10 (10-04 → now) |
|---|---|---|---|---|
| Konsa | d | Unspecified injury - 75% chance of playing | 3.30 → 2.85 | 13.6 → 10.2 |

## Options (GW6–10 gain vs holding, net of hits; route scorer from the 10-04 packet)

| Option | Gain now | If rolled to GW7 | Bank after |
|---|---|---|---|
| B.Fernandes + Isak → E.Le Fée + Haaland | +12.1 | +11.9 | 0.0 |
| B.Fernandes + Isak + Bijol → E.Le Fée + Haaland + De Cuyper | +15.7 | +13.5 | 0.0 |
| Bijol → De Cuyper | +7.6 | +5.6 | 0.3 |
| Cunha + Bijol → Rogers + De Cuyper | +8.3 | +9.4 | 0.4 |
| Donnarumma + N.Williams + Bijol → Verbruggen + Calafiori + De Cuyper | +9.0 | +9.0 | 0.4 |
| Wildcard (GW6-10) | +34.9 | — | 0.6 |
| Free Hit (GW6 only) | +9.8 | — | 1.5 |

Hold: XI Donnarumma, N.Williams, Mitchell, Konsa, Groß, B.Fernandes, Saka, Cherki, Cunha, Isak, Evanilson; bench Sels > João Pedro > Justin > Bijol; captain Groß, vice B.Fernandes.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.3): XI Donnarumma, N.Williams, Mitchell, Konsa, Groß, B.Fernandes, Saka, Cherki, Cunha, Isak, Evanilson; bench Sels > João Pedro > Justin > Bijol; C Groß, VC B.Fernandes; GW6 XI forecast 50.9 before hits.
- **Bijol -> De Cuyper (1 FT, no hit)** (bank after 0.3): XI Donnarumma, De Cuyper, N.Williams, Mitchell, Groß, B.Fernandes, Saka, Cherki, Cunha, Isak, Evanilson; bench Sels > João Pedro > Konsa > Justin; C Groß, VC B.Fernandes; GW6 XI forecast 52.8 before hits.
- **Bruno + Isak -> Haaland + Le Fée (-4)** (bank after 0.0): XI Donnarumma, N.Williams, Mitchell, Konsa, Groß, Saka, Cherki, Cunha, E.Le Fée, Haaland, Evanilson; bench Sels > João Pedro > Justin > Bijol; C Haaland, VC Groß; GW6 XI forecast 55.0 before hits.
- **Bruno + Isak -> Haaland + Xhaka (-4)** (bank after 0.2): XI Donnarumma, N.Williams, Mitchell, Konsa, Groß, Saka, Cherki, Cunha, Xhaka, Haaland, Evanilson; bench Sels > João Pedro > Justin > Bijol; C Haaland, VC Groß; GW6 XI forecast 54.8 before hits.
- **Bijol + Bruno + Isak -> De Cuyper + Le Fée + Haaland (-8)** (bank after 0.0): XI Donnarumma, De Cuyper, N.Williams, Mitchell, Groß, Saka, Cherki, Cunha, E.Le Fée, Haaland, Evanilson; bench Sels > João Pedro > Konsa > Justin; C Haaland, VC Groß; GW6 XI forecast 56.9 before hits.

**E20 (clean-data retrain):** its holdout read is done. Forecasts improve (1-week MAE 2.25 → 2.12) but squad points fall to 704 against 753 for classic + F6 over three windows, so it stays in shadow. Its GW6 shadow decode is part of Friday's refresh.

Classic + F6 on the fixed pipeline makes the decision; adapters are logged in shadow. See ../README.md for how to read the route gains and their uncertainty.

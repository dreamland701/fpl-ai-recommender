# GW6 research: Haaland now or next week, and Konsa, Isak, João Pedro

*2026-10-06 evening (PDT). Model numbers come from the fixed classic + F6 pipeline, snapshot 2026-10-07 05:06 UTC (`interim_1006/`).*

## Verdict

- **Haaland: buy him, but in GW7, not this week.**
  - This week: Bijol → De Cuyper with the free transfer.
  - Next week: Bruno + Isak → Haaland + Xhaka (−4).
  - That plan is worth +15.7 over GW6–10, whatever Haaland does at Anfield.
  - Buying him this week only comes out ahead if his GW6 is worth at least 90% of the model's forecast. The model has no idea about the fatigue news, and he'd be captain.
- **Konsa: keep him.** It's a dead leg, not believed serious. Your weak defender is Bijol (0 minutes in two gameweeks), and De Cuyper covers a Konsa absence this week.
- **João Pedro: likely out this week.** Bench him last; don't sell yet.
- **Isak: a 50/50-to-likely starter for Liverpool v City.** Start him this week; he's in next week's sale anyway.

## Haaland

**The news:**

- He played 90 minutes in three Norway games, then started against Portugal and asked off after about 60–67 minutes. He was seen limping, with "suspected muscle fatigue".
- No injury was found. Norway's coach: "He was tired against Wales… he has very bad vibes and feelings about it", and "thoroughly spent". Norway's players had "only six or seven days of holiday" after the summer World Cup.
- City granted him extra time off. He is expected to be available at Anfield (Sunday 11 Oct, 16:30 UK).

**The history** (`post_break_study.py`, regular starters in the first gameweek after each international break, 2019-20 to 2025-26):

| Group | Start rate after the break | Normal start rate | Points after | Points normal |
|---|---|---|---|---|
| All regular starters | 0.830 | 0.847 | 3.07 | 3.11 |
| Premiums (£10m+) | 0.891 | 0.874 | 6.12 | 5.61 |
| Man City regular starters, 2022-26 | **0.750** | 0.803 | 3.40 | 3.81 |

"Weird things after the break" barely shows up league-wide. City are the exception: Guardiola rotates more.

Haaland himself played 90 minutes in 13 of his 15 post-break gameweeks since 2022-23, averaging 6.6 points against 6.1 normally. Both blanks were injuries. One was April 2023, when he returned from Norway hurt and missed the game at Liverpool.

**Two-week plans over GW6–10, versus holding** (`plans.py`). Haaland's GW6 value is scaled by a factor, because he'd be captain and the model can't see the fatigue:

| Plan | Model (×1.0) | ×0.75 | ×0.60 |
|---|---|---|---|
| **GW6 Bijol → De Cuyper; GW7 Bruno + Isak → Haaland + Xhaka (−4)** | **+15.7** | **+15.7** | **+15.7** |
| GW6 Haaland double (−4); GW7 Bijol → De Cuyper | +17.4 | +13.5 | +12.3 |
| GW6 roll; GW7 Haaland double + Bijol → De Cuyper (−4) | +13.5 | +13.5 | +13.5 |
| GW6 roll; GW7 Haaland double (2 FT) | +11.9 | +11.9 | +11.9 |
| GW6 Haaland double only (−4) | +11.8 | +7.9 | +6.7 |
| GW6 Bijol → De Cuyper only | +7.8 | +7.8 | +7.8 |

**Why wait:**

- The break-even factor is about 0.90. Four Norway games, the extra rest, City's post-break rotation and Anfield away (fixture rating 4) all put it below that.
- GW7 is Ipswich at home (rating 2), followed by Villa away, Brighton at home and Forest away.

**Price risk:** the Xhaka version leaves £0.2m. It survives one £0.1m Haaland rise or one Bruno/Isak drop. If two move, Janelt instead of Xhaka leaves £0.7m.

## Konsa (Arsenal)

- **News:** he came into the England camp with discomfort, played against Spain and then 90 minutes against Croatia (7-0), and took another knock on the same quad. Tuchel: "nothing major but not worth the risk". He was released before Czechia, and the problem is not believed serious. He is still uncertain for Leeds.
- **Form:** 0, 11, 90, 90, 90 minutes; 12 points; almost no attacking threat. His starts came while Saliba was out, and Saliba's return is the bigger medium-term risk to his minutes.
- **Model:** GW6 2.85, GW6–10 10.2. That discounts all five weeks for the 75% flag, more than a dead leg deserves.
- **Cheap replacements up to £4.8m:** Thomas (Coventry, £4.0, started every game, GW6–10 15.8) and Davis (Ipswich, £4.0, started every game, 15.1). Taking one as well as Bijol → De Cuyper costs −4 for about +2 if Konsa is fit by GW7. Not worth it now; revisit when Saliba is back.

## Isak (Liverpool)

- **News:** Sweden boss Potter: "a small problem with his thigh… not a big one". He left camp early, and Liverpool are still assessing him. He is "in contention" for City with genuine doubt, and Liverpool are short of forwards (Ekitike is out with his Achilles).
- **Form:** 90, 90, 63, 90, 80 minutes; 33 points (4 goals); about 0.7 expected goals a game. Strong underlying numbers.

## João Pedro (Chelsea)

- **News:** knee injury in the 2-2 with Hull (GW4); he missed GW5 and withdrew from Brazil's squad, and saw a specialist over the break. The Evening Standard (6 Oct) says he is likely to miss Bournemouth, with a return later in October (about four weeks from the injury).
- **Form when fit:** 11, 9, 1, 12 points in GW1–4 (3 goals, 3 assists).

## GW6 lineup if you follow the plan (Bijol → De Cuyper)

- **XI:** Donnarumma; De Cuyper, N.Williams, Mitchell; Groß, Bruno, Saka, Cherki, Cunha; Isak, Evanilson.
- **Bench:** Sels; Justin, Konsa, João Pedro. João Pedro goes last, because the model's order (João Pedro first) predates the news that he's likely out.
- **Captain:** Groß (6.3, at Sunderland) or Bruno (6.2, home to Spurs). It's a coin flip in the model.

## Sources

- [TEAMtalk: Norway boss issues Haaland update (5 Oct)](https://www.teamtalk.com/news/erling-haaland-injury-update-liverpool-v-man-city)
- [Football360: Haaland asks to come off before Liverpool (5 Oct)](https://football360.com.au/erling-haaland-injury-man-city-liverpool-norway-nations-league/)
- [Brit Brief: Haaland granted extra rest (6 Oct)](https://britbrief.co.uk/sports/football/haaland-granted-extra-rest-before-liverpool-clash.html)
- [ArsenalNews: encouraging Konsa update (6 Oct)](https://arsenalnews.co.uk/2026/10/06/arsenal-receive-encouraging-ezri-konsa-injury-update-ahead-of-leeds-clash/)
- [Sports Mole: Tuchel explains Konsa "trauma"](https://www.sportsmole.co.uk/football/arsenal/injury-news/news/tuchel-explains-konsa-trauma-as-arsenal-receive-new-injury-update_606264.html)
- [Arseblog: England release Konsa and Dowman](https://arseblog.news/2026/10/injury-concerns-see-england-release-konsa-and-dowman/)
- [Anfield Index: Liverpool injury latest, Isak (6 Oct)](https://anfieldindex.com/101452/liverpool-injury-latest-alexander-isak-cody-gakpo-and-more-2.html)
- [This Is Anfield: Isak leaves Sweden camp](https://www.thisisanfield.com/2026/09/alexander-isak-leaves-sweden-injury-liverpool/)
- [RotoWire / Evening Standard: João Pedro return date uncertain (6 Oct)](https://www.rotowire.com/soccer/headlines/joao-pedro-injury-return-date-remains-uncertain-537079)
- [chelsea.news: trio await fitness verdicts (2 Oct)](https://chelsea.news/2026/10/chelsea-injuries-bournemouth-returns/)

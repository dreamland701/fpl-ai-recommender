# Classic vs classic + SFT (H1 regression head, final corpus 2026-10-16 10:00 PDT), GW7

Planned moves applied: B.Fernandes:McGinn, Isak:Haaland. The decision still comes from classic; this sheet shows what the adapter would change and why.

This week's generic SFT shrink: delta = +0.064 x classic forecast -0.416. For a 2-point player that is -0.29; for an 8-point player +0.10. That part is the same rule for everyone (the adapter aiming at the typical outcome rather than the average); the player-specific remainder is what reflects the text it read.

## Lineups

| | Classic | Classic + SFT (as written) |
|---|---|---|
| XI | Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson | Donnarumma, De Cuyper, Konsa, Justin, Cherki, Groß, Saka, Cunha, McGinn, Haaland, João Pedro |
| Bench (in order) | Sels, McGinn, N.Williams, Mitchell | Sels, Evanilson, N.Williams, Mitchell |
| Captain / vice | Haaland / Cherki | Haaland / Cherki |
| Expected GW points (incl. captain, own forecasts) | 61.3 | 58.2 |

XI differences: Evanilson (classic only), McGinn (SFT only)

## Every squad player and the main targets

| Player | Status / news | Classic GW | SFT GW | Generic shrink | Player-specific | P(appear) classic → SFT |
|---|---|---|---|---|---|---|
| **Donnarumma** | a | 3.25 | 3.07 | -0.21 | +0.03 | 0.93 → 0.98 |
| **N.Williams** | a | 2.96 | 2.75 | -0.23 | +0.02 | 0.80 → 0.91 |
| **Mitchell** | a | 2.78 | 2.47 | -0.24 | -0.07 | 0.89 → 0.92 |
| **De Cuyper** | a | 4.79 | 4.48 | -0.11 | -0.20 | 0.85 → 0.94 |
| **Groß** | a | 5.26 | 5.19 | -0.08 | +0.01 | 0.86 → 0.97 |
| **Saka** | a | 4.76 | 4.60 | -0.11 | -0.04 | 0.76 → 0.95 |
| **Cherki** | a | 5.98 | 5.55 | -0.03 | -0.39 | 0.95 → 0.97 |
| **Cunha** | a | 4.08 | 3.84 | -0.15 | -0.09 | 0.91 → 0.98 |
| **Evanilson** | a | 3.98 | 3.69 | -0.16 | -0.13 | 0.88 → 0.97 |
| **João Pedro** | a | 5.52 | 5.22 | -0.06 | -0.24 | 0.96 → 0.99 |
| **Sels** | a | 2.41 | 2.37 | -0.26 | +0.23 | 0.87 → 0.95 |
| **Konsa** | a | 3.18 | 2.94 | -0.21 | -0.03 | 0.80 → 0.95 |
| **Justin** | a | 3.13 | 2.79 | -0.22 | -0.12 | 0.84 → 0.88 |
| **McGinn** | a | 3.86 | 3.70 | -0.17 | +0.00 | 0.92 → 0.98 |
| **Haaland** | a | 8.70 | 8.43 | +0.14 | -0.41 | 1.00 → 0.99 |
| E.Le Fée | a | 3.49 | 3.28 | -0.19 | -0.02 | 0.82 → 0.93 |
| Xhaka | a | 3.61 | 3.47 | -0.18 | +0.04 | 0.91 → 0.97 |
| Rogers | a | 5.73 | 5.68 | -0.05 | +0.00 | 1.00 → 0.99 |
| Hall | a | 3.17 | 2.89 | -0.21 | -0.06 | 0.76 → 0.86 |
| Semenyo | a | 4.92 | 4.71 | -0.10 | -0.11 | 0.95 → 0.98 |
| Mbeumo | a | 4.27 | 4.09 | -0.14 | -0.04 | 0.89 → 0.97 |

## What the adapter read for the players it singled out

Listed when the player-specific part is at least 0.3 points or P(appear) moved by 0.1 or more. The text is exactly what was in the prompt; the adapter gives no reasons of its own.

### N.Williams: 2.96 → 2.75 (generic -0.23, specific +0.02); P(appear) 0.80 → 0.91
- Status: a; news: none
- No text evidence in the prompt: the move comes from the numbers and status alone.

### Groß: 5.26 → 5.19 (generic -0.08, specific +0.01); P(appear) 0.86 → 0.97
- Status: a; news: none
- *The Guardian Football | 2026-10-09T14:50:09Z* — The Premier League is back and you absolutely can’t look away: "... for red-hot Brighton. After three weeks on the proverbial deck-chair watching his nation flounder under Jürgen Klopp, will Pascal Groß still resemble Prime Kevin De Bruyne now that 95% of fantasy players have put the wily German into their teams? Arsenal v ..."

### Saka: 4.76 → 4.60 (generic -0.11, specific -0.04); P(appear) 0.76 → 0.95
- Status: a; news: none
- *The Guardian Football | 2026-10-03T18:22:23Z* — Croatia 0-7 England: Nations League football – as it happened: "... d to the week … I’ll be ready to start again on Tuesday.” Bukayo Saka speaks to ITV. “It was an amazing night for us … we came out … show, but then so did Anthony Gordon, Elliot Anderson and Bukayo Saka. A memorable night in Rijeka for so many reasons! Child’s ..."
- *The Guardian Football | 2026-10-10T14:06:47Z* — Arsenal 2-1 Leeds: Premier League – as it happened: "... can go home with their heads held high. 90+5 min: Gyokeres plays Saka in behind the Leeds defence and he’s clear on goal with only … oth been terrific. 75 min: Arsenal surge forward in numbers with Saka on the ball. Despite the support, he goes it alone and ..."

### Cherki: 5.98 → 5.55 (generic -0.03, specific -0.39); P(appear) 0.95 → 0.97
- Status: a; news: none
- *The Guardian Football | 2026-10-11T17:52:02Z* — Liverpool 0-3 Manchester City: Premier League – as it happened: "... d City in front, Jeremy Doku curled a beautiful second and Rayan Cherki scored an even better third. In the grand scheme, nobody h … should. 90+2 min One last chant of “Cheats!” from the home fans. Cherki tries to silence them with a deflected shot that loops ..."
- *The Guardian Football | 2026-10-14T21:30:22Z* — Manchester City 2-4 Paris Saint-Germain: Champions League – as it happened: "... Ndiaye cuts into the box before hoicking harmlessly over. City get the second half started. They’ve made a triple change, hooking Cherki, Doku and Dias for Nunes, Bouaddi and Ndiaye. Half-time postbag. “That 30-odd minutes of football from PSG is some of the ..."

### Konsa: 3.18 → 2.94 (generic -0.21, specific -0.03); P(appear) 0.80 → 0.95
- Status: a; news: none
- *The Guardian Football | 2026-10-10T14:06:47Z* — Arsenal 2-1 Leeds: Premier League – as it happened: "... sends it towards Declan Rice. Leeds win possession back and go Route One, but Dominic Calvert-Lewin is unable to get to it before Konsa despite a well-timed sprint. 12 min: Just the one shot on goal so far, from the boot of Leeds United’s Noah Okafor. 10 min: ..."
- *The Guardian Football | 2026-10-03T18:22:23Z* — Croatia 0-7 England: Nations League football – as it happened: "... from a tight-ish angle. He’s almost certainly going to get the player-of-the-match award nonetheless. 83 min: Matanović goes over Konsa’s leg in the England box, and demands a penalty, but he’s never getting one. The kids boo in the pantomime style … but then ..."

### Haaland: 8.70 → 8.43 (generic +0.14, specific -0.41); P(appear) 1.00 → 0.99
- Status: a; news: none
- *The Guardian Football | 2026-10-14T21:30:22Z* — Manchester City 2-4 Paris Saint-Germain: Champions League – as it happened: "... City will take succour from the performances of two-goal Erling Haaland, plus the second-half subs Iliman Ndiaye and Ayyoub Bouad … y to be nicked by Nunes. The referee points to the spot. 86 min: Haaland rolls a pass into the PSG box from the left. Semenyo ..."
- *The Guardian Football | 2026-10-11T17:52:02Z* — Liverpool 0-3 Manchester City: Premier League – as it happened: "... I thrive in those atmospheres. That’s when I come alive. Erling Haaland This is a lovely moment that will stay with us for a long … en Liverpool’s best player, was controversially sent off. Erling Haaland larruped City in front, Jeremy Doku curled a beautiful ..."

### E.Le Fée: 3.49 → 3.28 (generic -0.19, specific -0.02); P(appear) 0.82 → 0.93
- Status: a; news: none
- *The Guardian Football | 2026-10-15T19:14:50Z* — Noah Sadiki stunner earns Sunderland dramatic late win against Torreense: "... the Congo midfielder capitalised on excellent work from Enzo Le Fée and Granit Xhaka to half-volley an eye-catching first goal fo … trailing at the break. Le Bris had left, among others, Xhaka, Le Fée and Nordi Mukiele on the bench ahead of Sunday’s vital ..."
- *The Guardian Football | 2026-10-15T19:06:59Z* — Lyon 3-2 Crystal Palace, Torreense 1-2 Sunderland, and more: Europa League – as it happened: "... nly improved when Régis Le Bris brought on Reinildo, Mukiele, Le Fée and Xhaka in the second half. Not the best preparation for th … uadruple change. Here come the cavalry, as Reinildo, Mukiele, Le Fée and Xhaka all come off the bench. Not a day to remember for ..."


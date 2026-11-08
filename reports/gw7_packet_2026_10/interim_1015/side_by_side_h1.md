# Classic vs classic + SFT (H1 regression head, interim corpus 2026-10-15), GW7

Planned moves applied: B.Fernandes:McGinn, Isak:Haaland. The decision still comes from classic; this sheet shows what the adapter would change and why.

This week's generic SFT shrink: delta = +0.064 x classic forecast -0.414. For a 2-point player that is -0.29; for an 8-point player +0.10. That part is the same rule for everyone (the adapter aiming at the typical outcome rather than the average); the player-specific remainder is what reflects the text it read.

## Lineups

| | Classic | Classic + SFT (as written) |
|---|---|---|
| XI | Donnarumma, De Cuyper, Konsa, N.Williams, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson | Donnarumma, De Cuyper, Konsa, N.Williams, Cherki, Groß, Saka, Cunha, Haaland, João Pedro, Evanilson |
| Bench (in order) | Sels, McGinn, Justin, Mitchell | Sels, McGinn, Justin, Mitchell |
| Captain / vice | Haaland / Cherki | Haaland / Cherki |
| Expected GW points (incl. captain, own forecasts) | 59.8 | 57.0 |

## Every squad player and the main targets

| Player | Status / news | Classic GW | SFT GW | Generic shrink | Player-specific | P(appear) classic → SFT |
|---|---|---|---|---|---|---|
| **Donnarumma** | a | 3.29 | 3.08 | -0.20 | -0.01 | 0.93 → 0.97 |
| **N.Williams** | a | 3.06 | 2.84 | -0.22 | -0.00 | 0.82 → 0.92 |
| **Mitchell** | a | 2.80 | 2.52 | -0.23 | -0.05 | 0.88 → 0.91 |
| **De Cuyper** | a | 4.56 | 4.31 | -0.12 | -0.13 | 0.81 → 0.94 |
| **Groß** | a | 4.92 | 4.78 | -0.10 | -0.04 | 0.78 → 0.93 |
| **Saka** | a | 4.63 | 4.45 | -0.12 | -0.05 | 0.73 → 0.93 |
| **Cherki** | a | 5.61 | 5.27 | -0.06 | -0.28 | 0.89 → 0.95 |
| **Cunha** | a | 3.96 | 3.70 | -0.16 | -0.10 | 0.88 → 0.97 |
| **Evanilson** | a | 3.84 | 3.57 | -0.17 | -0.10 | 0.85 → 0.95 |
| **João Pedro** | a | 5.41 | 5.13 | -0.07 | -0.21 | 0.96 → 0.99 |
| **Sels** | a | 2.49 | 2.45 | -0.25 | +0.22 | 0.89 → 0.95 |
| **Konsa** | a | 3.22 | 2.98 | -0.21 | -0.03 | 0.80 → 0.95 |
| **Justin** | a | 3.03 | 2.70 | -0.22 | -0.12 | 0.82 → 0.88 |
| **McGinn** | a | 3.66 | 3.54 | -0.18 | +0.06 | 0.87 → 0.97 |
| **Haaland** | a | 8.66 | 8.44 | +0.14 | -0.36 | 1.00 → 0.99 |
| E.Le Fée | a | 3.57 | 3.42 | -0.19 | +0.04 | 0.83 → 0.95 |
| Xhaka | a | 3.54 | 3.35 | -0.19 | +0.00 | 0.90 → 0.96 |
| Rogers | a | 5.62 | 5.53 | -0.05 | -0.04 | 1.00 → 0.99 |
| Hall | a | 3.11 | 2.83 | -0.21 | -0.06 | 0.74 → 0.84 |
| Semenyo | a | 4.82 | 4.61 | -0.11 | -0.10 | 0.92 → 0.98 |
| Mbeumo | a | 4.30 | 4.20 | -0.14 | +0.04 | 0.89 → 0.98 |

## What the adapter read for the players it singled out

Listed when the player-specific part is at least 0.3 points or P(appear) moved by 0.1 or more. The text is exactly what was in the prompt; the adapter gives no reasons of its own.

### De Cuyper: 4.56 → 4.31 (generic -0.12, specific -0.13); P(appear) 0.81 → 0.94
- Status: a; news: none
- *Premier League | 2026-10-08T09:00:00Z* — FPL Challenge: Expert reveals their Gameweek 6 team: "... in four of the five Gameweeks so far this season. Defender Maxim De Cuyper (Brighton) Despite being classified as a defender in Fantasy, De Cuyper has start all five Gameweeks out-of-position on the ..."
- *Premier League | 2026-10-13T01:00:00Z* — FPL player price changes - risers, fallers and top transfers for Gameweek 7: "... t transfers for Gameweek 7* Most transfers in Most transfers out De Cuyper (BHA) 353,874 Isak (LIV) 224,944 Joao Pedro (CHE) 320,5 … *Last updated 09:02 BST, 13 October 12 October Price rises Maxim De Cuyper (Brighton) £5.1m Joao Pedro (Chelsea) £7.8m Morgan ..."

### Groß: 4.92 → 4.78 (generic -0.10, specific -0.04); P(appear) 0.78 → 0.93
- Status: a; news: none
- *The Guardian Football | 2026-10-09T14:50:09Z* — The Premier League is back and you absolutely can’t look away: "... for red-hot Brighton. After three weeks on the proverbial deck-chair watching his nation flounder under Jürgen Klopp, will Pascal Groß still resemble Prime Kevin De Bruyne now that 95% of fantasy players have put the wily German into their teams? Arsenal v ..."

### Saka: 4.63 → 4.45 (generic -0.12, specific -0.05); P(appear) 0.73 → 0.93
- Status: a; news: none
- *The Guardian Football | 2026-10-03T18:22:23Z* — Croatia 0-7 England: Nations League football – as it happened: "... d to the week … I’ll be ready to start again on Tuesday.” Bukayo Saka speaks to ITV. “It was an amazing night for us … we came out … show, but then so did Anthony Gordon, Elliot Anderson and Bukayo Saka. A memorable night in Rijeka for so many reasons! Child’s ..."
- *The Guardian Football | 2026-10-10T14:06:47Z* — Arsenal 2-1 Leeds: Premier League – as it happened: "... can go home with their heads held high. 90+5 min: Gyokeres plays Saka in behind the Leeds defence and he’s clear on goal with only … oth been terrific. 75 min: Arsenal surge forward in numbers with Saka on the ball. Despite the support, he goes it alone and ..."

### Evanilson: 3.84 → 3.57 (generic -0.17, specific -0.10); P(appear) 0.85 → 0.95
- Status: a; news: none
- *The Guardian Football | 2026-10-10T16:22:46Z* — Chelsea 5-1 Bournemouth, Sunderland 0-2 Brighton, and more: football – as it happened: "... OW. Chelsea 5-1 Bournemouth, 81 min: Bournemouth are pushing and Evanilson pops the ball into the area but Martinez plucks it from … Gannon-Doak has been a bright spark and he crosses an effort to Evanilson but he can’t quite get to it. This would be quite the ..."
- *The Guardian Football | 2026-10-10T16:18:07Z* — Henderson and João Pedro lead Chelsea charge against Bournemouth: "... one 22 league games without a clean sheet. They were 3-0 up when Evanilson pulled a goal back for Bournemouth, who are finding the … was RB Leipzig’s manager, was a distinct second-best this time. Evanilson bundled in from a corner, but Chelsea were rampant. ..."

### Konsa: 3.22 → 2.98 (generic -0.21, specific -0.03); P(appear) 0.80 → 0.95
- Status: a; news: none
- *The Guardian Football | 2026-10-10T14:06:47Z* — Arsenal 2-1 Leeds: Premier League – as it happened: "... sends it towards Declan Rice. Leeds win possession back and go Route One, but Dominic Calvert-Lewin is unable to get to it before Konsa despite a well-timed sprint. 12 min: Just the one shot on goal so far, from the boot of Leeds United’s Noah Okafor. 10 min: ..."
- *The Guardian Football | 2026-10-03T18:22:23Z* — Croatia 0-7 England: Nations League football – as it happened: "... from a tight-ish angle. He’s almost certainly going to get the player-of-the-match award nonetheless. 83 min: Matanović goes over Konsa’s leg in the England box, and demands a penalty, but he’s never getting one. The kids boo in the pantomime style … but then ..."

### McGinn: 3.66 → 3.54 (generic -0.18, specific +0.06); P(appear) 0.87 → 0.97
- Status: a; news: none
- *The Guardian Football | 2026-10-03T21:09:33Z* — North Macedonia 0-2 Scotland, Spain 3-1 Czechia and more: Nations League – as it happened: "... Robbie Ure and Aaron Hickey on for Scotland. 73 min: Hats off to McGinn for keeping his cool and tucking that penalty in. After failing to find the net since June (when McGinn’s goal defeated Haiti at the World Cup) Scotland have ..."
- *The Guardian Football | 2026-10-03T21:01:49Z* — Bowie gets Pocognoli off mark with Scotland victory in North Macedonia: "... uld have been worthy of significant Scottish embarrassment. John McGinn’s 22nd goal for his country, coming from the penalty spot, … ive minutes where he forced Stole Dimitrievski into a fine save. McGinn, like Robertson, has been the subject of some scathing ..."

### Haaland: 8.66 → 8.44 (generic +0.14, specific -0.36); P(appear) 1.00 → 0.99
- Status: a; news: none
- *The Guardian Football | 2026-10-11T17:52:02Z* — Liverpool 0-3 Manchester City: Premier League – as it happened: "... I thrive in those atmospheres. That’s when I come alive. Erling Haaland This is a lovely moment that will stay with us for a long … en Liverpool’s best player, was controversially sent off. Erling Haaland larruped City in front, Jeremy Doku curled a beautiful ..."
- *Premier League | 2026-10-09T06:00:00Z* — Who is the best FPL captain for Gameweek 6?: "If you're willing to go against Erling Haaland (£15.6m) with the captaincy in Gameweek 6 of Fantasy Premier League , Bukayo Saka (£9.6m) has the form and fixture to offer the best alternative. Manchester City 's Haaland tops the forward standings on 39 ..."

### E.Le Fée: 3.57 → 3.42 (generic -0.19, specific +0.04); P(appear) 0.83 → 0.95
- Status: a; news: none
- *The Guardian Football | 2026-10-10T16:20:30Z* — Ten-man Brighton continue fine form with battling win at Sunderland: "... y enlivened by some beautiful calibrated deliveries from Enzo Le Fée. Sunderland’s attacking playmaker created decent early openin … ng Brian Brobbey – and Thomas Meunier. Significantly, though, Le Fée faded badly in the second half. In the 53rd minute, a home ..."
- *Premier League | 2026-10-09T06:00:00Z* — Who is the best FPL captain for Gameweek 6?: "If you're willing to go against Erling Haaland (£15.6m) with the captaincy in Gameweek 6 of Fantasy Premier League , Bukayo Saka (£9.6m) has the form and fixture to offer the best alternative. Manchester City 's Haaland tops the forward standings on 39 ..."


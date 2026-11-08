# Extractor pilot: haiku_v2, 31b_v2 on 2291 prose documents + 0 lineups team blocks

## Throughput and form

| arm | docs | parse ok | truncated | facts/doc (prose) | docs with 0 facts (prose) | tokens out p50 | s/doc |
|---|---|---|---|---|---|---|---|
| haiku_v2 | 2291 | 100% | 0 | 2.1 | 776 | - | - |
| 31b_v2 | 2291 | 100% | 1 | 2.0 | 717 | 38 | 46.5 |

## Team blocks against the parser truth (Subs from = bench, Doubtful = doubt, Injured/Suspended = out)

| arm | blocks | precision | recall | name recall | tp | fp | fn | main confusions |
|---|---|---|---|---|---|---|---|---|
| haiku_v2 | 0 | 0.00 | 0.00 | 0.00 | 0 | 0 | 0 |  |
| 31b_v2 | 0 | 0.00 | 0.00 | 0.00 | 0 | 0 | 0 |  |

## Prose documents: agreement between arms (mean Jaccard per document, documents where either arm found facts)

| pair | docs | (name, status) | names only |
|---|---|---|---|
| haiku_v2 vs 31b_v2 | 1653 | 0.58 | 0.67 |

## Outcome validity on prose documents (facts joined to the next gameweek's minutes)

| arm | status | facts | matched to a player | appeared | started |
|---|---|---|---|---|---|
| haiku_v2 | xi | 711 | 575 | 90% | 70% |
| haiku_v2 | bench | 245 | 197 | 62% | 28% |
| haiku_v2 | doubt | 656 | 539 | 53% | 37% |
| haiku_v2 | out | 2082 | 1649 | 19% | 13% |
| haiku_v2 | return | 817 | 658 | 74% | 50% |
| haiku_v2 | role | 375 | 301 | 89% | 75% |
| 31b_v2 | xi | 766 | 635 | 93% | 81% |
| 31b_v2 | bench | 215 | 179 | 61% | 30% |
| 31b_v2 | doubt | 728 | 588 | 48% | 34% |
| 31b_v2 | out | 1988 | 1609 | 17% | 11% |
| 31b_v2 | return | 664 | 531 | 72% | 47% |
| 31b_v2 | role | 273 | 223 | 83% | 58% |

## Disagreement cases for a hand audit (first 6)

**2022-23 GW1 guardian 10.5h** Premier League: 10 things to look out for on the opening weekend  
- haiku_v2: Cheikhou Kouyaté [out] Cheikhou Kouyaté has left; James McArthur [out] the current injury list includes James McArthur; Michael Olise [out] the current injury list includes James McArthur and Michael Olise; Darwin Núñez [xi] does not look as if he needs to be eased in; Richarlison [out] The goalscorer is gone; Dominic Calvert-Lewin [out] the England international is out injured for the next six weeks; Salomón Rondón [out] Rondón is suspended; Nick Pope [xi] Howe will start Pope ahead of Dubravka on Saturday; Martin Dubravka [bench] Howe will start Pope ahead of Dubravka on Saturday; Harry Kane [xi] Harry Kane looks relaxed and ready  
- 31b_v2: James McArthur [out] current injury list includes James McArthur; Michael Olise [out] current injury list includes Michael Olise; Dominic Calvert-Lewin [out] out injured for the next six weeks; Salomón Rondón [out] Rondón is suspended; Nick Pope [xi] consensus is that Howe will start Pope; Martin Dubravka [bench] Howe will start Pope ahead of Dubravka  

**2022-23 GW1 guardian 20.0h** Frank Lampard hopes ‘tough love’ can get Dele Alli back on the goal trail  
- haiku_v2: Dominic Calvert-Lewin [out] ruled out for six weeks with a knee injury; Richarlison [out] Richarlison was sold to Tottenham; Dele Alli [role] could be an option in attack this season  
- 31b_v2: Dele Alli [role] could be an option in attack this season; Dominic Calvert-Lewin [out] ruled out for six weeks with a knee injury  

**2022-23 GW1 guardian 47.8h** Everton’s Dominic Calvert-Lewin faces month out with ‘freak’ knee injury  
- haiku_v2: Dominic Calvert-Lewin [out] ruled out of the club’s opener against Chelsea on Saturday; Salomón Rondón [out] Salomón Rondón suspended for the Chelsea game; Richarlison [out] Everton have sold their leading goalscorer last season, Richarlison  
- 31b_v2: Dominic Calvert-Lewin [out] ruled out of the club’s opener against Chelsea on Saturday; Salomón Rondón [out] suspended for the Chelsea game  

**2022-23 GW1 guardian 53.5h** Fresh faces: six Premier League players to look out for in the 2022-23 season  
- haiku_v2: Flynn Downes [role] will complement and perhaps eventually supplant Declan Rice in midfield; Julián Álvarez [role] His time down the middle might be limited due to Haaland  
- 31b_v2: Brenden Aaronson [role] joining the club; Flynn Downes [role] arrived at West Ham this summer; Moussa Niakhaté [role] ideal man to play on the left side of a back three; Sven Botman [role] signed for £32m from Lille; Julián Álvarez [role] Pep Guardiola wanted him to be part of his squad immediately; Tyrell Malacia [role] a 22-year-old left-back from Rotterdam  

**2022-23 GW1 guardian 54.5h** Premier League 2022-23 preview No 16: Nottingham Forest  
- haiku_v2: Brice Samba [out] Brice Samba, who was allowed to leave; Dean Henderson [role] allowed to leave and replaced by Dean Henderson; Neco Williams [out] certainties to be part of the Wales setup, barring injuries; Brennan Johnson [out] certainties to be part of the Wales setup, barring injuries; Richie Laryea [out] he is earmarked to spend the season out on loan  
- 31b_v2: Richie Laryea [out] earmarked to spend the season out on loan  

**2022-23 GW1 guardian 70.1h** Chelsea agree Carney Chukwuemeka deal and interested in Walker-Peters  
- haiku_v2: (none)  
- 31b_v2: Carney Chukwuemeka [role] agree a deal with Aston Villa; Marc Cucurella [role] close to signing the Brighton defender; Malang Sarr [bench] prepared to loan out; Timo Werner [bench] talks over moving Timo Werner to RB Leipzig  


# ATP Intelligence – új kutatási állapot: 105/150 TDI és a négy hiányzó Top50 eseménykontextusa

**Projekt:** privát férfi ATP/GS mérkőzésintelligencia; 2026. november 22. A forrásadatok **kutatási overlay-k**, nem automatikusan validált prediktív jellemzők, nem kerülnek egyből `main` ágra.

## 1. Új TDI eredmény (94 → 105)

[Egységes, 105 soros mérési tábla](ATP_TDI_TOP150_NORMALIZED_105_2026_11_22.csv) + [11 új teljes TDI-sor, eredeti forrásokkal](ATP_TDI_FULL7_NEW_11_PLAYERS_2026_11_22.csv).

- **105/150** játékos forrásolt TDI-jegyzettel. **65** játékosnál 7/7, további **40** játékosnál 2/7 kiemelt mutató; **535** rögzített mért számérték. **45/150** játékosnál nincs forrásolt TDI rekordsor: [hiánylistájuk](ATP_TDI_REMAINING_45_RESEARCH_QUEUE_2026_11_22.csv).
- A mérési mutatók: In Attack %, Conversion %, Steal %, Serve Quality, Return Quality, Forehand Quality, Backhand Quality. A minőségi mutatók **0–10 skálán** vannak; nem abszolút siker-valószínűségek.
- 2025-ben publikált 52 hetes statisztikai sorból **9** a mérési előző időablak miatt **2024-es eseményt is tartalmazhat**, ezért `temporal_source_scope=EXCLUDE_DIRECT_PREDICTOR_POSSIBLE_2024_MATCHES`. Kifejezett felhasználói 2025/26 közvetlen prediktív időszűrését **nem** sérthetjük. Ezek csak datált történeti kutatási tapasztalatok; akkor válnának közvetlen prediktív adattá, ha egyedi pont/mérkőzés szinten a 2024 előtti részt eltávolítjuk.
- 2025-ös Rio aktuális torna adatában **Jaime Faria** csak a 2025. február 21-ig játszott adott tornapontokat reprezentálja. A másik 2026-os, azonos dokumentum-évű `tournament_to_date` sorok sem egyenlőek a 52 hetes értékekkel.
- A `predictive_validated` minden rekordban `NO`: **forrásolt mérés ≠ validált előrejelző modell**, és nem igazolja belső mentális személyiségállapotot.

### További 11 játékos (minden sornál hét számszerű érték)

| Játékos | A dokumentum kelte | Időablak | In attack | Conversion | Steal | Serve / Return / FH / BH Quality | Forrás |
|---|---|---|---:|---:|---:|---|---|
| Alex Molčan | 2026-04-18 | München, torna addig | 22% | 68% | 40% | 7.8 / 6.4 / 7.1 / 7.3 | [ATP München](https://www.atptour.com/-/media/f41c36bf0a1b4dfdbfab285058ae63f2.pdf) |
| Roman Safiullin | 2025-07-29 | rolling 52 hét | 25% | 69% | 34% | 7.9 / 6.0 / 7.4 / 6.6 | [ATP Toronto](https://www.atptour.com/-/media/02cdd4d88f624b9ba6f07bd1d583644e.pdf) |
| Aleksandar Vukic | 2025-08-08 | rolling 52 hét | 25% | 67% | 30% | 8.2 / 5.9 / 6.9 / 6.1 | [ATP Cincinnati](https://www.atptour.com/-/media/43f77ee9013b4b3ea149656ca4faf5ed.pdf) |
| Nishesh Basavareddy | 2025-08-08 | rolling 52 hét | 25% | 66% | 33% | 7.5 / 5.9 / 6.9 / 6.9 | [ATP Cincinnati](https://www.atptour.com/-/media/43f77ee9013b4b3ea149656ca4faf5ed.pdf) |
| Hugo Gaston | 2025-07-30 | rolling 52 hét | 19% | 66% | 33% | 6.8 / 5.5 / 6.4 / 6.7 | [ATP Toronto](https://www.atptour.com/-/media/551dddb52b5d4316a8891932b4477029.pdf) |
| Jaime Faria | 2025-02-21 | Rio, torna addig | 28% | 69% | 33% | 8.2 / 5.3 / 7.0 / 7.0 | [ATP Rio](https://www.atptour.com/-/media/71cdbb3b57224912924cf23c8c04906d.pdf) |
| Camilo Ugo Carabelli | 2025-10-29 | rolling 52 hét | 19% | 67% | 37% | 7.4 / 6.2 / 7.4 / 6.8 | [ATP Párizs](https://www.atptour.com/-/media/cc0b27e791f24ba790b3282515f7f95f.pdf) |
| James Duckworth | 2025-07-29 | rolling 52 hét | 25% | 67% | 30% | 7.8 / 5.5 / 6.6 / 6.0 | [ATP Toronto](https://www.atptour.com/-/media/02cdd4d88f624b9ba6f07bd1d583644e.pdf) |
| Pedro Martínez | 2025-08-09 | rolling 52 hét | 20% | 66% | 35% | 6.9 / 6.2 / 7.1 / 6.9 | [ATP Cincinnati](https://www.atptour.com/-/media/74fe65f6d9354931a993b68d8e5ce826.pdf) |
| Laslo Djere | 2025-04-25 | rolling 52 hét | 25% | 67% | 33% | 8.1 / 6.3 / 7.8 / 6.7 | [ATP Madrid](https://www.atptour.com/-/media/c6b9a5ec2b964502a17bd1023e298dd3.pdf) |
| Thiago Seyboth Wild | 2025-03-19 | rolling 52 hét | 24% | 69% | 33% | 8.0 / 6.4 / 7.7 / 7.1 | [ATP Miami](https://www.atptour.com/-/media/84c955f7ed904a0481faa2a5caeaae64.pdf) |

A nyilvános ATP PDF-ek egy részénél a szöveges táblából elérhetők a számok, de a PDF-es screenshot-rendszer a képi ellenőrzést 403-mal elutasította. Az új forrásfájl `review_status` mezője ezt külön jelzi; az Alex Molčan müncheni táblája képen is ellenőrzött.

## 2. A Top50-ből TDI nélkül maradt négy játékos – 2026-os bizonyítható megfigyelések

A négy játékosra **nem áll rendelkezésre hivatalosan forrásolt, egyértelműen 2025–26-os hétmutatós TDI sor az eddig azonosított anyagokban**. Viszont 2026-os eredmény-, terhelés- és fordulópont-kontextus **igen**, így az előző kutatási kör óta egyéni helyzetvizsgálat is keletkezett:

[**9 forrásolt, időbélyegzett eseménymegfigyelés**](ATP_TOP150_2026_FOUR_TOP50_CONTEXT_PLUS_DAMM_IDENTITY_2026_11_22.csv)

- **Arthur Fery, ranglista #32:** 2026 Wimbledon 3. kör Bergs ellen két szett/három helyzeti fordulat, **2–6 7–5 2–6 7–6(3) 7–6(10–5)**, 4 óra 39 perc; később 2026 Wimbledon elődöntő Cobolli 6–4 7–6(4) 6–0 legyőzésével. Források: [Bergs elleni fordítás](https://www.atptour.com/en/news/fery-bergs-wimledon-2026-r3); [Cobolli elleni negyeddöntő](https://www.atptour.com/en/news/cobolli-fery-wimbledon-2026-qf).
- **Luca Van Assche, #34:** 2026 Estoril ATP250 salak döntőben a 3. szett 5–3-as vezetésének elvesztése után **6–4 4–6 7–5** győzelem Blockx ellen. Ez konkrét, ellenőrizhető vezetéselvesztési/recovery megfigyelés, **nem** egész személyiségre érvényes mentális címke. [ATP Estoril](https://www.atptour.com/en/news/blockx-van-assche-estoril-2026-final).
- **Daniel Mérida, #42:** 2026 Bucharest ATP250 **3 meccslabda hárítása** a tornán, első döntője és július 18-án 2026 Umag első címe. [Bucharest pénteki beszámoló](https://www.atptour.com/en/news/bucharest-2026-report-friday), [Umag](https://www.atptour.com/en/news/merida-dzumhur-umag-2026-final).
- **Arthur Géa, #48:** 2026 Los Cabos ATP250 Cerúndolo ellen **6–7(11) 6–4 6–0** eredményű fordítás az első elődöntőhöz, majd Shapovalov elleni döntőben első ATP-cím. [Elődöntőbe jutás](https://www.atptour.com/en/news/los-cabos-2026-thursday-report), [döntő](https://www.atptour.com/en/news/gea-shapovalov-los-cabos-2026-final).

A 2026-os H2H-val és torna-/játékoskontextussal később meccsnapon újra kell szűrni az időbeli frissességet; egyetlen comeback, cím vagy szettvesztés **nem** igazol állandó mentális erőt vagy sérülést.

### Kritikus névazonosítás: Martin Damm Jr., #103

Az **ATP 2026. augusztus 3-i** hivatalos tudósítása szerint a 22 éves, balkezes amerikai **Martin Damm Jr** a fiatal játékos, aki Top100 debütált. Édesapja, az idősebb, cseh Martin Damm külön sportoló. A fiatalabb játékos a közlés szerint a megelőző **52 hét 10. legjobb ATP Serve Rating** értékével rendelkezett; **nincs konkrét 0–10-es Serve Quality** az eredményben, így nem helyettesítjük azt a 10. helyezéssel. [ATP hivatalos forrás](https://www.atptour.com/en/news/gea-wong-damm-top-100-august-2026).

Ez fontos, mert egyes korábbi nem hivatalos aggregátor-jelölteknél a `Martin Damm` név az idősebb karrierre mutathat. Minden fonák, tömeg, stat és ATP provider ID lekérésnél egyértelmű személy-ID-re van szükség.

## 3. Adatvalidálási szabályok és lezárási státusz

1. **105/150 TDI evidence**, nem 105 validált coach/mentális profil; azok több mérkőzésen még nincsenek igazolva.
2. **2026-ban a 2025–26 eseményeknek lehet közvetlen prediktív súlya**, de a 2025-ös 52 hetes táblák egy részét **2024-es mintaszennyezés miatt kizártuk**.
3. A játékosok külön mérési napját és az eltérő `rolling_52_weeks` vs `tournament_to_date` időszakot minden matchup-feature előtt össze kell vetni.
4. A hiányzó érték nem nulla, a győzelem nem bizonyít mentális karaktert, az ATP TDI shot quality nem biomechanikai videóértékelés.
5. `main` érintetlen; minden új táblázat és doksi a nyitott PR #13 kutatási ágán van. PR #14 fejlesztési ág nem automatikusan frissül a PR #13 új commitjaival.

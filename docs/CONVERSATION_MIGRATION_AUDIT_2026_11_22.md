# ATP Intelligence – régi beszélgetés → új beszélgetés átadási audit
**2026-11-22. Állapot: RÉSZLEGESEN ELLENŐRZÖTT, 100%-os egyezés NEM BIZONYÍTOTT.**

## A vizsgálat határa
Összevetettük a jelenlegi GitHub PROJECT_MASTER.md-t, a 2026.11.22-i 150 játékosprofil-regiszterét, a Notion négy kutatási aloldalát, a korábbi ATP-beszélgetésből visszakereshető kiválasztott felhasználói döntéseket és a 2025–2026-os relevanciaszabályt. **A teljes eredeti ChatGPT-szál szó szerinti exportja ebben az auditban NEM volt rendelkezésre bocsátva.** Ezért ez *nem* üzenetről üzenetre végzett teljességi audit, és a „minden átkerült” állítást nem támaszthatja alá.

## Ellenőrzött és rögzített követelmények

| Követelmény | Megőrzés | Bizonyíték |
|---|---|---|
| Privát, egy felhasználós férfi ATP app; jelenleg nem SaaS | Igen, döntés megőrzött | PROJECT_MASTER 1, 2; Notion projektközpont |
| Minden ATP Top150 játékos permanens alaprekord | Igen, 150/150 regiszter | PROJECT_MASTER 14–15; research/player_profiles/ATP_COACH_SCOUTING_REGISTER_2026_11_22.csv |
| Eredményrelevancia tárgyév + előző év, 2024 előtti H2H kizárása a közvetlen predikcióból | Igen, szabály és tesztkód | docs/TEMPORAL_RELEVANCE_POLICY.md; atp_intelligence/time_relevance.py; PROJECT_MASTER 16 |
| Coach Intelligence: 0–4 ütés, serve+1, return+1, labdamenet, döntés/kivitelezés, lábmunka, baseline | Igen, modul- és követelmény-szinten | PROJECT_MASTER 1–5; Notion „01 · Coach Intelligence” |
| A és B játékost *külön* vizsgáljuk; momentum lehet pozitív/negatív, favorit/állás nem momentum | Igen, szabály megőrzött | PROJECT_MASTER 1–2; Notion „02 · Momentum” |
| Momentum-/változáspont észlelése lehetőleg **a break előtt** | Igen, célként megőrzött; működés nem bizonyított | PROJECT_MASTER 1, 3–4; Notion főoldal |
| P/T/F réteg (pszichológiai/technikai/taktikai), Player Baseline / Live Coach Observation / Momentum Shift / Prediction | Részben: funkció és F/T/P nomenklatúra megőrzött, a teljes korábbi név- és interfész-séma nem igazolt | PROJECT_MASTER 2, 4–5; eredeti beszélgetés részben visszakereshető |
| **12 edzői tudásterület és 48 megfigyelhető jel** | **Részben: a korábbi beszélgetésből a 12/48 követelmény visszakereshető; teljes tételes 48 jelre nincs ezen auditban lefuttatott elem-szintű egyezés** | Korábbi kontextus; PROJECT_MASTER említi a katalógust; Notion „01” fő kategóriákat sorol |
| Pont/game/set/match előrejelzés, no-lookahead, log-loss/Brier, fals riasztások, éles odds csak külön ellenőrzéssel | Igen, döntésként megőrzött; éles működés nem bizonyított | PROJECT_MASTER 2, 4, 9; Notion „02” és „04” |
| 2025–2026-os H2H, borítás, forma, sérülés-, terhelés-, utazás- és pontvédési kontextus | Igen, célként megőrzött; minden mező élő adatlekérése nem bizonyított | PROJECT_MASTER 2, 4, 16; research/player_profiles/ |
| Tennis API mint kiválasztott külső forrás; meglévő Sportscore RapidAPI kliens | **Tisztázandó provider/kapcsolódás:** a futó prototípusban Sportscore RapidAPI szerepel, nem bizonyított, hogy a külön említett Tennis API már be is van kötve | tennis_api_client.py; Notion „03 · Adatforrások és minőség” |
| Mobilon használható privát app, később opcionális Discord | Igen, termékdöntés megőrzött; mobilélmény nem bizonyított | PROJECT_MASTER 1–3 |
| 150 profil, statisztikák, taktikai/matchup források | Igen, 150 forrással hivatkozott statisztikai scoutingdosszié | ATP_TOP150_SCOUTING_EGYBEN_2026_11_22.md; regiszter |
| 150 teljesen *validált* mentális és ütés/mozgás technikai profil | **Nem kész: 0/150**, nem átadási adatvesztésnek állítjuk, hanem eredetileg sem véglegesített munkának | ATP_TOP150_VALIDATION_STATUS_2026_11_22.csv |
| Élő appba integrált, hiteles korai momentumelőrejelzés | **Nem bizonyítottan kész** | PROJECT_MASTER 3, 6, 9 |

## Ténylegesen ellenőrizhető átadás 3 szinten

**1. Döntésszint.** A régi beszélgetésből visszakeresett minden egyes követelményt soronként a PROJECT_MASTER-hez és Notion-oldalakhoz kötjük; ami nem egyezik, a „hiányos/ütközéses” kategóriába kerül.

**2. Adat- és fájlszint.** A régi kutatási listák és kódmódosítások tételes fájl- és rekord-egyezése (név, dátum, forrás-URL, commit, rekordok darabszáma), 150 játékos jelenlegi dokumentált státuszával.

**3. Funkció- és tesztszint.** A dokumentált funkcióhoz futó kód, működő adatfeed, teszt és az előrejelzés időbélyegzett, visszatesztelt eredménye kell. A specifikáció megléte **nem egyenlő a működő appal**.

## Nyitott auditpontok
1. A **teljes régi ChatGPT-beszélgetés exportjával** üzenetről üzenetre összevetés. Enélkül NEM lehet 100%-os teljességet igazolni.
2. A 12 tudásterület mind a 48 konkrét jelének tételes forrás/változat összevetése; hiányzó jelnevek visszaállítása.
3. A külön említett „Tennis API” pontos szolgáltatói neve, szerződése, lefedettsége és integrációs státusza; Sportscore RapidAPI-szal nem összekeverendő.
4. Régi chatből korábban rögzített, de csak Notionban, fájlban vagy nem exportált beszélgetésszakaszban lévő döntések felkutatása.
5. GitHub issue-k és futó alkalmazás-kód ellenőrzése, mert minden készenléti állítást valós tesztnek kell alátámasztani.

## Referenciák
- [GitHub PROJECT_MASTER](../PROJECT_MASTER.md)
- [2026-11-22 scouting index](../research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md)
- [Top150 validációs hiánylista](../research/player_profiles/ATP_TOP150_VALIDATION_STATUS_2026_11_22.csv)
- [Időablak politika](TEMPORAL_RELEVANCE_POLICY.md)
- [Notion projektközpont](https://app.notion.com/p/41ff603f0d2e8121a7c6c2cc89ff4213)
- [Notion Coach Intelligence](https://app.notion.com/p/41ff603f0d2e8171aa65f6c8099b917f)
- [Notion Momentum](https://app.notion.com/p/41ff603f0d2e81c0bb09dbef3246b1ea)
- [Notion Adatforrások](https://app.notion.com/p/41ff603f0d2e8173af57d727e98be79b)
- [Notion Roadmap](https://app.notion.com/p/41ff603f0d2e8177947fca58ede75300)


## 2026-11-22 – Feltöltött ATP(1).txt alapján felülvizsgálva

A felhasználó feltöltötte az `ATP(1).txt` fájlt (1006 soros szövegkivonat). A részletes elemzés: [ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md](ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md). **Újonnan azonosított hiányok:** három képesség/intuíció, a Blind Prediction minimum 50 javasolt tesztje, 30 napos tanulási program, eredmény előtt lezárt Prediction Sheet, virtuális EV/odds-retegek, kötelező 10 pontos pre-match, 6 lehetséges fordulat-ok, meccs-előszűrés/video nélküli működés, korábban javasolt PWA stack, Tennis API-szolgáltatóval folytatott levelezésre vonatkozó, még nem jogilag igazolt emlékeztető. A 12/48 konkrét jelneve **ebben a fájlban nincs felsorolva**. A teljes, szó szerinti chattranszkript és eredeti csatolmányok továbbra sem ellenőrzöttek.

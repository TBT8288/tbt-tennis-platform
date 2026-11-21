# ATP Intelligence — PROJECT_MASTER

> A projekt központi, verziókezelt állapotdokumentuma. Az új beszélgetések kezdésekor először ezt a fájlt és a GitHub aktuális kódját kell elolvasni.
>
> **Frissítve:** 2026-11-21  
> **Repo:** https://github.com/TBT8288/tbt-tennis-platform  
> **Státusz:** meglévő Streamlit/RapidAPI/Gemini prototípus; coach-intelligence és predikciós rendszer tervezés alatt. A kódból még nem igazolt a valódi, előrejelző momentumfelismerés.

## 1. Vízió és hatókör

Privát, egy felhasználónak készülő, ATP-férfi teniszre koncentráló elemzőrendszer. **Nem tippgenerátor.** A mérkőzést egy tapasztalt edző szemléletével szeretnénk olvasni: korai technikai, taktikai, viselkedési és a pszichológiai állapot esetleges megváltozására utaló jelek azonosítása **még az eredményjelzőn látható break vagy fordulat előtt**.

A favoritstátusz, aktuális állás, előző szett győztese nem határozza meg, melyik játékos változik pozitív vagy negatív irányba. Az A és B játékos változásait **külön-külön** kell modellezni; mindkettő javulhat vagy romolhat. A „pszichológiai momentum” a belső állapotra vonatkozó **hipotézis**, nem közvetlenül mért tény: az adatokból mérhető a teljesítmény- és viselkedésváltozás, a pszichológiai ok bizonyításához további megfigyelés szükséges. Minden jelentés különítse el a tényt, a megfigyelést, a lehetséges magyarázatot és az előrejelzést.

## 2. Tervezett modulok

1. **Player Intelligence:** történeti eredmények, borítás, H2H, szerva/fogadás, játékstílus, személyes baseline.
2. **Pre-Match Context:** utazás, terhelés, regeneráció, selejtező/LL/WC, pontvédelem, időjárás, naptár, nyilvános hírek forrással.
3. **Coach Intelligence:** 0–4 ütés, serve+1/return+1, pályageometria, szervafeldobás és ritmus, lábmunka, fogadópozíció, döntés és kivitelezés, rutin és viselkedés.
4. **Live Shift Intelligence:** játékosonként technikai (F), taktikai (T), megfigyelhető pszichológiai jelek (P); anomália, változáspont, bizonytalanság. Ne csak pontsorozatot figyeljen.
5. **Prediction Engine:** következő pont, következő game, rövid game-horizont, következő szett és mérkőzés **külön célváltozókkal**.
6. **Validation Engine:** előzetesen időbélyegzett becslések, no-lookahead, kalibráció, Brier/log-loss, fals riasztás, jelzés előnye, baseline-összehasonlítás. Piaci odds vizsgálata külön, a ténylegesen elérhető ajánlatok és késések megkülönböztetésével.
7. **Private UI / notifications:** élő felület, későbbi mobilos használhatóság, Discord opcionális.

## 3. Jelenlegi repository — 2026-11-21-i kódáttekintés

- `app.py`: Streamlit UI, élő meccsek kiválasztása, 120 másodperces fragmentfrissítés, Gemini-elemzés, Discord-üzenet.
- `tennis_api_client.py`: Sportscore RapidAPI élő mérkőzéslista, eredményformázás. A pontszintű időtörténet és az időbélyegzett tartós tárolás hiányzik.
- `gemini_client.py`: score/status-alapú AI-kommentár. Ebből nem következik megbízható edzői momentumdiagnózis.
- `openai_client.py`: külön OpenAI-kliens, jelenleg nincs bekötve a fő alkalmazás folyamába.
- `discord_client.py`: webhook értesítési modul.
- `requirements.txt`: jelenleg streamlit, requests, google-genai; a külön OpenAI-klienshez hiányzik az `openai` csomag.

**Még nincs bizonyítva:** valós, pontonkénti korai jelzés, külön F/T/P megfigyelés, adatbázis, játékosbaseline, visszateszt, éles előrejelzési előny. Nem szabad ezeket elkészült funkcióként leírni.

## 4. Kötelező adatminőség és metodika

- Mindig azonosítsuk: player_id, match_id, event_time, ingested_at, source, source_timestamp, completeness, confidence és a rendelkezésre álló mezők.
- Először az eredmény/szerváló szerinti erős B0 alapmodell; utána B1 dinamikus szerva/fogadás; B2 online változáspont; később multimodális edzői jellemzők.
- A mozgás, testbeszéd, labdaelhelyezés és ütésminőség **nem** állapítható meg pusztán az eredményből. Ehhez megfelelő feed, videó, követési adat vagy ellenőrzött kézi megfigyelés kell.
- Tesztelés időrend szerint, a fordulatos és fordulat nélküli helyzeteket is bevonva. A kijelzett esélyek kalibrációját és fals riasztásait mérni kell.
- A hipotézisekhez alternatív magyarázatok és források tartozzanak. Ne diagnosztizáljunk sérülést vagy mentális állapotot bizonyíték nélkül.
- API-kulcsot, jelszót, webhookot, privát adatokat **soha** ne commitoljunk.

## 5. Fejlesztési stratégia

1. Meglévő kód stabilizálása, teljes import/teszt setup, hibakezelés, mock-adat, no-secrets.
2. Egy adatforrás valódi schema-, lefedettség-, kvóta- és latency-auditja.
3. Pontszintű események tartós tárolása; Player/Match/Observation/Prediction/Source metaadat.
4. B0/B1/B2 modellek és egységtesztek, historikus és élő összehasonlítás.
5. Coach-feature katalógus elérhető és hiányzó adatokra bontva; P/T/F modulok.
6. Előrejelzések előzetes rögzítése és hosszú távú validáció.
7. Felület és használhatóság fejlesztése a validált alapra.

## 6. Konkrét nyitott feladatok

- [ ] A repo publikus. Magánhasználatú fejlesztéshez **private** beállítás ajánlott, mielőtt részletes, bizalmas kutatás vagy saját adatok kerülnek bele.
- [ ] API ellenőrzése: RapidAPI/Sportscore aktuális sémák, késés, feed lefedettség és feltételek.
- [ ] A korábbi kutatási fájlok forrásainak és tartalmának összehangolása a repo `research/` mappájában — csak ellenőrzött, elérhető eredetikből.
- [ ] Streamlit és Gemini jelenlegi kódjának tesztelése; függőségek rögzítése.
- [ ] Konkrét B0/B1/B2 modell API és mérőszám-specifikáció.
- [ ] GitHub Issues megnyitása mérföldkövenként.

## 7. Új beszélgetés / átadás menete

Új szálban elegendő ennyit kérni:
> Folytassuk az ATP Intelligence projektet a `TBT8288/tbt-tennis-platform` GitHub repository alapján. Olvasd el a `PROJECT_MASTER.md` fájlt, nézd meg a legutóbbi commitokat és nyitott issue-kat, majd innen folytassuk.

Minden lezárt munkafázis után:
1. kód és tesztek GitHubra;
2. `PROJECT_MASTER.md` frissítése a valós státusszal, döntésekkel, ismert hibákkal;
3. a következő teendők GitHub Issues-ban, amikor kialakult a feladatrendszer.

**A GitHub a projekt tartós igazságforrása, nem a beszélgetés emlékezete.** A csatlakozó adatait minden alkalommal újra be kell olvasni; önmagában egy új chat nem örököl teljes, garantált projektállapotot.

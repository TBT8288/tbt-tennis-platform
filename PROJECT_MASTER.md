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

## 8. Eszköz- és hozzáférési döntések (2026-11-21)

- **Cursor:** csak később mérlegeljük, most nem kötelező vagy megvásárolt fejlesztőeszköz.
- **Claude:** a felhasználó 2026. november végén tervezi előfizetését és külön Claude API-hozzáférés/API-kulcs beállítását. Ez még **nem történt meg**, a Claude-előfizetés nem jelent automatikusan API-kreditet. A titkos kulcsokat soha ne tegyük GitHubba vagy chatbe.
- **Notion és Firecrawl:** a felhasználó szeretné ezeket a ChatGPT-be kapcsolni. 2026-11-21-i ellenőrzés szerint mindkettő **elérhető, de nincs telepítve/csatlakoztatva**. Az első kapcsolódás és a szükséges OAuth-engedély a felhasználó kifejezett UI-jóváhagyását igényli; az asszisztens nem tudja automatikusan megadni helyette.
- **GitHub:** továbbra is az elsődleges forrás kódhoz, feladatokhoz és projektállapothoz. A Notion és Firecrawl csak szükség szerint kiegészítő.

## 9. Megvalósítás és ellenőrzés — 2026-11-21

**Elkészült és GitHubra mentve:**
- `atp_intelligence/probability.py`: standard advantage game/hold/break esélye a feltételezett szervapont-esélyből (B0 matematikai alapeszköz, még nincs játékoserősség vagy borítás becsatolva).
- `atp_intelligence/events.py`: időzónás UTC pontesemények, megfigyelések és predikciók, adatvalidáció, evidence cutoff ellenőrzése.
- `atp_intelligence/storage.py`: SQLite esemény-/előrejelzés-mentés, idempotens event ID.
- `tests/test_core.py`: 11 Python egységteszt.
- `.github/workflows/tests.yml`: GitHub Actions – Python 3.12 CI.
- `.gitignore`, `README.md`: dokumentáció és titkos kulcsok/nyers adatok kizárása.
- **CI ténylegesen sikeres**: [GitHub Actions run #44929140544](https://github.com/TBT8288/tbt-tennis-platform/actions/runs/44929140544) (2026-11-21).

**GitHub feladatok:** [#1 API audit](https://github.com/TBT8288/tbt-tennis-platform/issues/1), [#2 B0](https://github.com/TBT8288/tbt-tennis-platform/issues/2), [#3 B1/B2](https://github.com/TBT8288/tbt-tennis-platform/issues/3), [#4 időbélyegzett validáció](https://github.com/TBT8288/tbt-tennis-platform/issues/4), [#5 Coach Intelligence](https://github.com/TBT8288/tbt-tennis-platform/issues/5).

**Notion projektközpont:** [ATP Intelligence – Kutatási és projektközpont](https://app.notion.com/p/41ff603f0d2e8121a7c6c2cc89ff4213) (négy részletes aloldal: edzői megfigyelés, momentum, adatforrások, roadmap).

**Amit még nem állíthatunk késznek:** a jelenlegi Streamlit app nem használja még a matematikai modult, nincs valós élő pontrögzítés, momentum-/pszichológiai detektor, videóelemzés vagy validált előrejelzési fölény. Az új modul önálló alap, nem kész élő AI-teniszedző.

**Következő prioritás:** #1 adatforrás-audit és a történeti eseményadat sémájának tényleges ellenőrzése; utána a validált B0-becslést bevezetni a meglévő felületbe.

## 10. Korábbi projektek auditja – 2026-11-21

A felhasználó öt korábbi ATP/Challenger PDF-et és a nagy `TBTProjekt.zip` archívumot megosztotta. Két PDF-pár pontos duplikátum; a harmadik 16 oldalas módszertan csak egy modulfolyamat-sorral tér el. A ZIP régi Next.js/FastAPI és Python modulokat, függőségeket és történeti dokumentációt tartalmaz; önmagában nem teljes játékosadatbázis.

- [Kritikus válogatási, migrációs és forráselemzési jelentés](research/legacy_2026_07/ADOPTION_MATRIX.md).
- [Három ellenőrzött, történeti meccs-referencia](research/legacy_2026_07/verified_match_examples.csv) – ezek nem élő ATP-modellek, és nem igazolják a PDF minden további következtetését.
- [Notion – történeti dokumentumok és szakértői források auditja](https://app.notion.com/p/41ff603f0d2e818fae5ac8e2c6b09354).
- [GitHub #6: szakértői és játékosadat átvétel](https://github.com/TBT8288/tbt-tennis-platform/issues/6).
- [GitHub #7: korábbi API-kulcsok biztonsági ellenőrzése](https://github.com/TBT8288/tbt-tennis-platform/issues/7).

Átültethető: eredményminőség, baseline, forrásminősítés, NO SOURCE/NO PREDICTION, egymástól elkülönített prematch/in-play, játékos-idővonal. Nem átültethető változatlanul: állásalapú „momentum”, kézzel választott 0.35/21 nap/LOGIT_SCALE/INPLAY_GAIN paraméterek, fizetős SaaS és széles Challenger-scope.

**Biztonság:** az eredeti ZIP-ben régi, nyílt szövegként tárolt API-kulcsok szerepelnek. A kulcsok nem kerültek bele az új dokumentációba/kódba; a régi aktív hozzáféréseket szükség esetén vissza kell vonni, majd csak secrets tárolón át kezelni. A repository még Public; nem publikáljuk az eredeti ZIP/PDF fájlokat. A régi projektben szereplő, 2026 júliusi játékosmegfigyelés nem tekinthető automatikusan aktuális tényezőnek.

## 11. Damian Kust / Jakub Bobro archívum – első adatgyűjtés (2026-11-21)

A felhasználó kérésére tényleges külső archívumforrásokból összeállt az első **forráshivatkozott történeti játékosdosszié-seed** (nem a teljes podcastarchívum és nem validált élő teniszmodell).

- [5 archív forrás (podcast + cikk)](research/expert_archives/sources.csv): 2022–2024 közötti Kust/Bobro-adások és 2024-es Kust-elemzések.
- [21 játékos dátumozott, státuszforrással igazolt pillanatképe](research/expert_archives/player_mentions_2026_11_21.csv): 16-nál 2026-os versenyeredmény megerősítve, 3 hivatalosan visszavonult (Novak, Berankis, Goffin), 1 ATP-szünet (Cressy), 1 korlátozott/nem eldönthető profi aktivitás (De Loore).
- [11 saját szavas, forráshoz és 2022–2024-es dátumhoz kötött szakmai megfigyelés](research/expert_archives/historical_observations.csv): jelölt ellenőrzési bizonytalansággal. Egy podcastleírásban szereplő vendég nem egyenlő a meghallgatott, átírt szakmai interjúval.
- [Módszertani adatleírás](research/expert_archives/README.md).
- `atp_intelligence/archive.py`: szabványos Python/SQLite import, a forrás és dátum jelölését megőrizve. `tests/test_expert_archive.py`: automatizált teszt.
- [Notion 06 – szakértői archívum](https://app.notion.com/p/41ff603f0d2e81ffb621da1e4ac4675f).

**Reprodukció:** `python -m atp_intelligence.archive --folder research/expert_archives --db data/expert_archive.sqlite3` (helyi SQLite adatbázis, gitignore-on).

**Ne olvadjon be az élő pillanatnyi formába!** A 2024-es játékosmegfigyelés történeti kontextus, nem 2026-os aktív forma, sérülés vagy mentális diagnózis. Az archív források hosszú távú stratégiai előnyhöz vezethetnek, de önmagukban nem bizonyítanak előrejelzési előnyt.

A történeti szakértői archívum véges: Jakub Bobro 2023 augusztusában és Damian Kust 2026 januárjában hunyt el (ezt megbízható publikációk megerősítik). A tudástár csak az eredeti, dátumozott anyagokra támaszkodjon.

**Szerzői jog:** teljes hanganyagokat, cikkeket és transzkriptumokat nem teszünk a nyilvános GitHubba; csak forráslinkeket, metaadatokat és rövid, saját szavú összefoglalókat. A még fel nem dolgozott epizódoknál ne állítsunk semmilyen konkrét játékosról hallott megjegyzést.

**Következő lépések:** további epizódok felkutatása → epizódonkénti vendéglisták → ellenőrizhető egyedi edzői/versenyszempontú megállapítások → rendszeres, külön forrásból mért 2026-os aktív státusz frissítés → a Player Intelligence felé szigorú, időzárt felhasználás.

## 12. Kizárólag ATP Top100 játékosprofilok és jelenlegi szakértők (2026-11-21)

**Új, elsőbbséget élvező termékhatókör:** a férfi ATP-egyes Top 100 2026-11-16-i, dátumozott rangsora, mindegyik játékosnál 2026-os főtáblás mérkőzésadattal ellenőrizve. Célverseny: ATP 250/500/Masters 1000/Finals és Grand Slam; nem elemzünk Challenger/ITF meccseket élő célként. A Challenger-múlt csak **ma is Top100-as** játékos történeti kontextusaként maradhat meg. Kivételes, ranglistán kívüli játékoshoz nincs önálló aktív profil a mostani verzióban.

- [Teljes, 100 soros ATP-ranglistapillanatkép](research/rosters/atp_top100_2026_11_16.csv); [források és korlátok](research/rosters/README.md).
- [Szigorú, validált Top100-szűrő](atp_intelligence/roster.py).
- [Aktuális podcast- és szakértőkatalógus – 7 személy](research/expert_archives/current_analysts_2026_11_21.csv): Gill Gross, Hugh Clarke, Calvin Betton, Craig O’Shannessy, Andy Roddick, Matt Roberts, Alex Gruskin.
- [5 új, dátumozott 2026-os szakértői forrás](research/expert_archives/current_sources.csv) és [8 rövid, saját szavú ATP-megfigyelés](research/expert_archives/current_atp_observations.csv).
- [Szűrt SQLite-import](atp_intelligence/archive.py): 100 roster sor, 10 forrás, a régi 21 jelöltből 7 felvehető játékosemlítés, valamint összesen 13, jogosult játékoshoz kötött történeti megfigyelés. A többi jelölt kizárva a működő aktív játékosadatbázisból. A régi kutatási CSV-k továbbra is bibliográfiai nyomként léteznek; nem kerülnek aktív modellbe.
- [Notion 07 – kutatási eredmények](https://app.notion.com/p/41ff603f0d2e8146a3c6f3bbdfeaf3e4).
- [GitHub #9: heti keretfrissítés](https://github.com/TBT8288/tbt-tennis-platform/issues/9) és [#10: szakértői források bővítése](https://github.com/TBT8288/tbt-tennis-platform/issues/10).

A ranglista és a szakértői megfigyelések **dátumozott pillanatképek**, nem folyamatosan frissülő élő adatok. A szakértői vélemények nem közvetlen pszichológiai mérések és nem bizonyítanak nyerő modellt. A hivatalos ATP webes oldal cache-e régebbi rangsorokat mutatott; a 2026-11-16-i forrás a Tennis.esp.br és a TennisDB egyeztetett ranking/season oldala. A jelenlegi Streamlit alkalmazás éles eseménybeolvasását még nem kötöttük rá a Top100-jogosultságvizsgálatra.

## 13. Pontosítás: Top100 prioritás, nem merev mérkőzéskorlát (2026-11-21)

**Ez pontosítja a 12. fejezet túl merev fogalmazását.** A Top 100 az **állandóan, teljes mélységben követett játékosprofilok** jelenlegi prioritási kerete, de **NEM** a megvizsgálható mérkőzések kizárólagos játékoslistája.

- **Célmeccsek:** ATP 250, 500, Masters 1000, ATP Finals és Grand Slam férfi egyes **főtáblás mérkőzések**, a résztvevők rangsorától függetlenül. Challenger/ITF meccsek nem célmeccsek.
- **Tier A:** aktuális ATP Top100, részletes és folyamatos Player Intelligence / Coach Intelligence profil.
- **Tier B:** Top100-on kívüli, ATP- vagy Grand Slam-főtáblán ténylegesen szereplő játékos, akiről az adott meccshez **minimális, forrásolt ellenfélprofilt és mérkőzéselemzést** készítünk. Nem indul automatikus, teljes életpályás követés.
- **Tier C:** kizárólag Challenger/ITF-ben szereplők, vagy olyan nevek, akiknél nincs aktuális releváns felsőszintű főtáblás mérkőzés: nincs külön aktív profil.
- **Kiemelt kivétel:** ha két Top100-on kívüli játékos játszik egymással egy releváns ATP/Grand Slam-főtáblán, a *mérkőzés* beleesik a célhatókörbe; készülhet ideiglenes meccsprofil mindkét félhez, de tartós teljes profil nem automatikus.
- A 2026-11-16-os Top100 CSV és az `ATPTop100.eligible()` **csak a teljes profilra** vonatkozik. **Nem szabad a meglévő szigorú Top100 profilkaput az élő ATP-meccslista kizárólagos beléptetőjeként alkalmazni.**
- A Tier B játékosok tényleges jogosultságát a **forrásolt torna, forduló, main-draw státusz és mérkőzésazonosító** bizonyítja. A kezdő app még nem valósítja meg ezt az eseményszintű ellenőrzést.

Fejlesztési szabály: `match_is_in_scope(event)` külön döntés az `eligible_for_deep_profile(player)` szabálytól. A részletes profil optimalizálja a költséget; a mérkőzések teljeskörűsége nem függhet mereven a ranglista 100. helyétől.

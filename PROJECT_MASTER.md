# ATP Intelligence — PROJECT_MASTER

> A projekt központi, verziókezelt állapotdokumentuma. Az új beszélgetések kezdésekor először ezt a fájlt és a GitHub aktuális kódját kell elolvasni.
> **ÚJ BESZÉLGETÉS INDÍTÓKÓDJA: `ATP`** – [állandó új-beszélgetés protokoll](docs/ATP_START.md) és [tartós munkanapló](docs/ATP_SESSION_LOG.md). A teljes korábbi ATP(1).txt szöveges beszélgetés a tulajdonos privát **ATP – Privát projektarchívum** ChatGPT Space-ében érhető el. A hívószó az adatok **tényleges beolvasását** jelenti, nem automatikus teljes chatmemóriát.
>
> **Frissítve:** 2026-11-22  
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

## 14. Végleges új játékoskeret: ATP Top 150 (2026-11-21)

**Ez a felhasználó legújabb döntése, és minden korábbi Top100-fókuszú szabályt felülír a tartós profilokra nézve.** Minden olyan férfi egyesjátékos kap állandó Player Intelligence alaprekordot, aki a legutolsó elfogadott ATP-ranglistán **1–150. helyen áll**. A ranglista csak dátumozott snapshot; a frissítés még nem automatikus.

- [**150 játékos ranglista- és rekordállománya**](research/rosters/atp_top150_2026_11_16.csv): pontos 2026-11-16-os helyezés, név, ország, ATP-pontszám, források, adatminőség.
- [**2026-os szezonadatok**](research/rosters/atp_top150_season_stats_2026.csv): 150 sor, **146** egyező név+pontszám alapján ellenőrzött teljesítménystatisztikával (W/L, Elo, Serve+, Return+, Pressure+, stb., amennyiben rendelkezésre állnak). **Négy játékos** nem megerősített a másodlagos statisztikai forrásból: Otto Virtanen (107), Clément Chidekh (116), Max Alcalá Gurri (130), Nikolas Sánchez Izquierdo (132). Ezeknél a nem ellenőrzött statisztikai mezők üresek, NEM nulla értékek.
- Rangsor két oldalon: [1–100](https://www.tennis.esp.br/en/rankings?date=2026-11-16&tour=ATP), [101–200](https://tennis.esp.br/en/rankings?date=2026-11-16&page=2&tour=ATP). Átlagokat külön szolgáltató adja: [TennisDB 2026](https://tennis-db.com/seasons-and-rankings?year=2026). A TennisDB bizonyos ranghelyei eltérnek; statisztikai egyeztetéshez **játékosnév és ranglistapont**, nem csupán ranghely szükséges. A tárolt 146 ellenőrzött statisztikai rekordot név+pont szerint is visszaellenőriztük.
- `atp_intelligence/roster.py`: **ATPTop150** ellenőrző, megengedi a legitim nulla vagy hiányzó 2026-os főtáblás W/L-t.
- `atp_intelligence/archive.py`: 150 játékos és a statisztikák SQLite-importja, dátumozott forrásokkal, szakértői megfigyelések szűrésével.
- [Automatikus Python-tesztek](tests/test_expert_archive.py): Top150 keret, adathiány és DB-migráció ellenőrzése; a tesztbővítés javításra került [GitHub Actions](https://github.com/TBT8288/tbt-tennis-platform/actions/runs/44935243024) futásában.

**Mérkőzés-hatókör:** továbbra is férfi ATP 250/500/Masters 1000/Finals és Grand Slam főtábla. Az esetleg Top150-en kívüli mérkőzésellenfél minimális, ideiglenes mérkőzés-kontextusként szerepelhet, de nem kap állandó teljes játékosprofilt. Challenger/ITF-meccsek nem célmeccsek.

**Ami NINCS kész:** minden játékoshoz személyre szabott, bizonyított ütés-/borítás-/lábmunka-/pszichológiai dosszié; élő adatcsatorna; ténylegesen automatikus ranglistafrissítés; modellek validálása. Ezek a bővítés következő munkafázisai, a statisztikai alapadatoktól elkülönítve. Az üres ismeretlent nem pótoljuk AI-találgatással.

## 15. Játékosdossziék – tényleges adatok és még hiányzó részek (2026-11-21)

A felhasználó kérése: **minden jelenlegi ATP Top150 játékos** kor, súly, magasság, jobb-/balkezesség, szerva/return, taktikai erősségek/gyengeségek, támadó/defenzív stílus, borításonkénti kompetencia, nyomás alatti viselkedés és pszichológiai változáspont-megfigyelések. Csak **forrásolt, ellenőrzött** állítás kerülhet a dossziéba; hiányzó adatot nem szabad kitalálni.

**Készen álló, ellenőrzött adatalapok:**
- [Teljes Top150 egyesített dossziéregister (40+ oszlop)](research/player_profiles/atp_top150_profile_register_2026_11_21.csv) – **150/150 név, rang, pont, születési dátum, kor, kéz**, **134/150 magasság + testsúly**, **150/150 négy borítás Elo-értéke** PythiaTennis 2026-11-20 modelljéből, **146/150 2026-os szezonadat**, összesen **18 régi+új forrásolt szakértői jegyzet 12 játékosról**. Több játékoshoz forrás szerinti edzőnév; nem feltétlen aktuális edzői kapcsolat.
- [Magyar áttekintő lista (18 oszlop, mindenki)](research/player_profiles/ATP_TOP150_ATTEKINTHETO_LISTA_2026_11_21.csv).
- [Életrajzi forrásanyag](research/rosters/atp_top150_biography_2026_11_21.csv), ATP média guide 2024/2025/2026 + friss ATP overview, Australian Open és TennisExplorer profilok.
- [Hard/Clay/Grass/Indoor Elo 150/150](research/rosters/atp_top150_surface_elo_2026_11_20.csv), az Elo nem egyenlő általános játékstílussal vagy mentális erővel.
- [Pontos lefedettség és módszertani korlátok](research/player_profiles/README.md).
- [Notion 08 – teljes 150 játékos, rangsor, kor, súly, kéz, borítás Elo](https://app.notion.com/p/41ff603f0d2e81f08d2bd1d2966d9ed3).
- [Python adatkonzisztencia tesztek](tests/test_player_profile_register.py); [sikeres GitHub Actions](https://github.com/TBT8288/tbt-tennis-platform/actions/runs/44937514653).

**Lényeges adatminőségi tanulság:** az ATP 2026 media guide Flavio Cobolli magasságát **173 cm**-nek közölte, a jelenlegi ATP overview **183 cm**-nek; a regiszter az aktuális ATP adatát használja, és jelzi a konfliktust. A második forrásból fellelt kg és kézadatok forrás szerinti publikus játékosadatok, de súly dinamikusan változhat.

**Nem kész/tilos úgy állítani, hogy kész:** 16 játékos testsúlya nem volt ellenőrizhető; 4 játékos 2026-os szezonstatisztikája forrásütközéses; csak 12 játékoshoz van attribuált szakértői megfigyelés; **0/150 többmeccsesen validált mentális „összeomlik/erős” jellemzés**, **0/150 teljes, ellenőrzött támadó/defenzív és szakértői erősség-gyengeség-profil**. Ezeket a következő építési fázisban, egyéni mérkőzéshistóriával és edzői megfigyelésekkel kell bizonyítani. A TennisDB `Pressure+` stat nem pszichológiai diagnózis, és a hiányzó adat NEM egyenlő nullával.

### Első 7 forrásolt taktikai dosszié-előzetes

[ATP + Hugh Clarke forrásolt megfigyelések](research/player_profiles/atp_top150_tactical_sources_seed_2026_11_21.csv) alapján **7 játékos** (Zverev, Sinner, Alcaraz, Shelton, Medvedev, Fritz, Ruud) kapott *előzetes, dátumozott játékstílus- és matchup-megjegyzést*. Ezek **nem** sok mérkőzésen igazolt állandó gyengeségek vagy pszichológiai diagnózisok. A többi **143** játékos összesített stíluscímkéje továbbra sincs forrásoltan kész. A jelenlegi regiszter forrás-URL-t és bizonyíték-kategóriát is külön tárol.

## 16. Kötelező időablak: mindig a tárgyév és az előző szezon (2026-11-21)

**Felhasználói döntés:** az ATP Top150 játékosok aktuális meccsére vonatkozó **prediktív** formát, borításonkénti eredményeket, serve/return mutatókat, ellenfélhelyzetet és H2H-t az **aktuális és az előző naptári szezonból** állítjuk össze. 2026-ban **2026+2025**; 2027-ben **2027+2026**. A korábbi évekből származó meccseredmény és H2H megőrizhető az archívumban és taktikai történeti előzményként, de **közvetlen aktuális forma/H2H feature-ként nem kaphat súlyt**.

- [Részletes döntés, ellenpéldák és kalibrációs szabályok](docs/TEMPORAL_RELEVANCE_POLICY.md).
- [Kód: időablak, kísérleti recency-decay és kis mintaszámos H2H-simítás](atp_intelligence/time_relevance.py).
- [Anti-leakage, évváltás, H2H-tesztek](tests/test_time_relevance.py).

**A H2H mellékes összehasonlító jel:** ha két játékos 2022–24-ben találkozott, de 2025–26-ban nem, akkor a **jelenlegi prediktív H2H=semleges/hiányzó**, és az archív régi 3–0 nem befolyásolja közvetlenül az esélyt. Ha csak egy friss H2H van, az nem bizonyít tartós mentális fölényt.

**Fontos különbség:** a jelenlegi Pythia Tennis 2026-11-20-i pályaborításos Elo **karrier-/történeti bázisú**, nem kizárólag 2025–2026-ból számolt forma. A meglévő [150-es Elo-tábla](research/rosters/atp_top150_surface_elo_2026_11_20.csv) nem törlendő, de friss formának **nem címkézhető át**. A súlyozott, csak 2025/2026 mérkőzéseiből képzett feature-öket még külön kell előállítani, és backtesttel kalibrálni.

A most alkalmazott 270/180/45 napos teljesítmény/H2H/rövid-forma félidők **kezdő mérnöki hiperparaméterek**, NEM kutatás által validált optimumok. Más ablakokkal, a 24 hónapos rolling időablakkal és idősúly nélkül is össze kell vetni, kizárólag korábbi mérkőzéseket felhasználva, időrendi visszatesztben (log-loss, Brier-score, borítás/főtorna szegmens és kis mintás H2H).

**Még nem kész:** az új kétidényes relevanciakód az élő Streamlit modellezési folyamatba, a nyers meccstörténetbe vagy a valószínűségszámításba **még nincs bekötve**; ezért az adatablak jelenleg dokumentált és tesztelt szabály, nem éles predikciós állítás.


## 2026-11-21: Top150 kutatási adatbázis-bővítés (statisztikai első passz)

- 150/150 kétidényes, **forrásolt számszerű dosszié** a [profilindexben](research/player_profiles/TOP150_EVIDENCE_PROFILES_INDEX_2026_11_21.md).
- TennisDB 2026-11-21 pillanatkép, 2025 mérkőzésarchívum és 2026-11-15-ig frissített 2026 ATP match adat (Min Maxxxer / Tennis Odds Actor).
- A 2025+2026 közötti friss H2H CSV: [2025–2026 H2H, 2026-11-15-ig](research/player_profiles/TOP150_H2H_2025_2026_THROUGH_2026_11_15.csv).
- 2026-os meccsadat-lefedettség 148/150, 2026-os TennisDB rekord 146/150; **a teljes technikai/mentális többmeccses validáció 0/150**, előzetes taktikai jegyzet 13/150.
- Nem tekinthető kész predikciós motornak: a CSV még nincs az alkalmazásba integrálva, a 2026-11-16 és utáni meccsek nem teljesek a friss archívumban, a források W/L definíciói különbözhetnek. Régebbi H2H >2 év 0 közvetlen súly.


## 2026-11-22 – a 150 játékos forráslinkkel ellátott scouting adatbázisa

Elkészült és ellenőrizve: [scouting-index](research/player_profiles/ATP_COACH_SCOUTING_INDEX_2026_11_22.md), [150 kibővített scoutingdosszié egyben](research/player_profiles/ATP_TOP150_SCOUTING_EGYBEN_2026_11_22.md), [150 soros scouting-regiszter](research/player_profiles/ATP_COACH_SCOUTING_REGISTER_2026_11_22.csv). Mind a 150-hez van számszerű alap és egy forráslink; 137 új 2025–2026-os forrásrészlet, 13 eredeti, esetenként régebbi hivatkozás. A kvalitatív megfigyelések többnyire egyszeri mérkőzésre, újságcikkre vagy eredményre korlátozódnak. **Teljes, többmeccses validált technikai és mentális profil: 0/150; az alkalmazásba bekötés nincs kész.** A fejlesztés és további adatvalidáció továbbra is szükséges, különösen 0–4 ütéses rally, szerva+1, fogadás+1, helyezkedés, 2026.11.15 utáni teljes H2H, többmeccses taktikai kutatás. Régi H2H közvetlen súly nulla; Elo történeti baseline. A legfrissebb profiladatok nem jelentik azt, hogy az app ma élő, pontos predikciót végez.


## 2026-11-22 – átadási teljesség auditja

A régi ATP-beszélgetésből a jelenlegi beszélgetésbe történő **100%-os szövegszintű átvitel nincs bizonyítva**. Ellenőrzési bizonyítékok és nyitott kérdések: [CONVERSATION_MIGRATION_AUDIT_2026_11_22.md](docs/CONVERSATION_MIGRATION_AUDIT_2026_11_22.md). Fontos megőrzendő korábbi követelmény: **12 edzői tudásterület, 48 külön megfigyelhető jel**, P/T/F rétegek, személyes játékosbaseline, a két játékos egymástól független teljesítményváltozása, lehetőleg break előtti jelzés; mindezek egyetlen jelenlegi pontfeedből nem tekinthetők megvalósítottnak. A Tennis API felhasználási engedélyének korábban egyeztetett terjedelmét a felhasználó 2026-11-22-én ismételten **ellenőrzött és lezárt döntésként megerősítette**. Ez külön kérdés a prototípus aktuális, Sportscore RapidAPI-ra mutató technikai bekötésétől; az implementáció továbbra is ellenőrizendő. A teljes korábbi ChatGPT-export nélkül nem állíthatunk hiánytalanságot.


## 2026-11-22 – az eredeti ATP(1).txt forrásból visszanyert, korábban hiányos részek

**Részletes, sorhivatkozásos átadási összehasonlítás:** [ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md](docs/ORIGINAL_ATP_THREAD_GAP_AUDIT_2026_11_22.md). Az eredeti feltöltött TXT **nincs közzétéve** a GitHubon; csak az adatvédelmileg csökkentett projektkövetelmények és az audit.

A régi ATP Live Prediction Lab korábbi tervében **három egymástól külön mérendő képesség** szerepelt: (1) intuíció (első, statisztika és oddsok előtti „Blind Prediction”), (2) rejtett, már break előtti változások felismerése, (3) valószínűségi előrejelzés. Az eredeti tanulási **30 napos terv** és **legalább 50 önálló Blind Prediction teszt** egy **megőrzött oktatási/kutatási javaslat**, nem igazolt már elindított automata működés. Az intuíciót önmagában, a statisztikai modellt önmagában és kombinálva **időbélyegzetten** kell mérni; megérzés nem helyettesíti az adatot.

**Prediction Sheet:** mérkőzés ID, A/B játékos, állás, blind intuíció, megfigyelt jelek, saját százalék, konkrét esemény/horizont (következő pont; game; 2–3 game; szett; mérkőzés), opcionális megfigyelt szorzó és timestamp, tényleges eredmény **utólag**, a korábbi predikció módosíthatatlan. A korábbi terv elsőre **virtuális/szimulált odds-összevetés**, nem pénzes fogadásautomatizálás. `EV = p * decimal_odds - 1` csak kalibrált `p` mellett értelmes; árrés, adatfrissesség, odds késés és a becslés bizonytalansága kötelező vizsgálat.

**Pre-Match Intelligence kötelező tíz vizsgálati pontja:** (1) előző/következő naptár; (2) egyedi torna-prioritás; (3) aktuális pontvédelem; (4) előző heti meccsszám/játékidő; (5) regenerációs idő; (6) utazás/időzóna; (7) borítás és átállás; (8) igazolt sérülés/kezelés/visszalépés; (9) aktuális 2 idényben dokumentált nyomáshelyzetek; (10) nyilvános forrásból megerősített motiváció. Az összeomlást **hatféleképpen** magyarázó hipotézisek: fáradás, megfigyelt nyomásreakció, taktikai alkalmazkodás, sérülés, természetes variancia, vagy az ellenfél magasabb szintre kapcsolása. Mindezt eredményből visszamagyarázás és bizonyíték nélküli meccsmanipulációs vád nélkül.

**Felhasználói használhatósági cél:** az alkalmazás gyűjti és előszűri a releváns ATP-meccseket, terhelést és játékos-kontextust, és kevés fontos, kellően megbízható riasztást ad, így nem kell mindet élőben végignézni. A régi javaslatban **70–80% automatizálás** ambíció volt, nem teljesített mérés. Videó csak másodlagos megfigyelési mód, nélküle biomechanikáról/testbeszédről nem állítunk konkrét tényt; elégtelen adat külön érvényes „NO SIGNAL/NO PREDICTION” állapot.

**Korábbi, nem jóváhagyott architektúra-opció:** React/PWA + Python FastAPI + PostgreSQL/Supabase + push, szerveroldali kulcsvédelem; a mai Streamlit-kódot nem helyettesíti automatikusan. A felhasználó mostani végleges hatóköre privát, ATP Top150, célmérkőzés ATP/Grand Slam férfi egyes főtábla; a TXT-ben szereplő Challenger és fizetős SaaS a korábbi opciók közé tartozik.

**Tennis API felhasználási engedély – FELHASZNÁLÓ ÁLTAL KORÁBBAN ELLENŐRZÖTT ÉS ÚJRA MEGERŐSÍTETT, LEZÁRT DÖNTÉS (2026-11-22):** a Tennis API adatai felhasználhatók a saját alkalmazásban, AI-generált saját elemzésekkel kiegészítve; az egyeztetés a fizetős, havi előfizetéses SaaS-eshetőséget is lefedte. A korábban egyeztetett felhasználási terjedelmet **nem kell újra megkérdőjelezni**. A jelenlegi termék továbbra is **privát, nem fizetős app**. Az eredeti levelezés szövege nincs bemásolva a TXT-be, de a felhasználó most kifejezetten megerősítette, hogy a terjedelem már ellenőrzésre került. **KÜLÖN technikai feladat** a megfelelő Tennis API provider/endpoint bekötése: a régi Streamlit prototípusban a `tennis_api_client.py` jelenleg Sportscore RapidAPI-t használ. Az engedély státusza és a tényleges kódintegráció státusza nem ugyanaz.

**Audit továbbra nyitott:** a 12 edzői tudásterület és 48 jel **tételes listája nem szerepel ebben a feltöltött ATP(1).txt fájlban**; ilyen specifikáció nem rekonstruálható automatikusan. A nyers, szövegszerű teljes beszélgetés és az eredeti e-mail/ábrák ellenőrzése továbbra sem 100%-os.


## 2026-11-22 – AZ EREDETI ATP BESZÉLGETÉS 9 HIÁNYZÓ TERÜLETE: GITHUBRA PÓTOLVA

**[A 9 terület teljes, aktuális pótlási jegyzéke](docs/ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md)** – ez a kötelező hivatkozás az új beszélgetések átadási csomagjában. A korábbi `ATP(1).txt` eredeti felhasználói beszélgetés alapján 8 részletes szakmai dokumentum és 3 üres, újrafelhasználható adatgyűjtő CSV jött létre (50 Blind Prediction próba, 50 virtuális odds/EV naplósor, 20 játékosonkénti Pre-Match faktorbejegyzés). A követelmények/sablonok **elmentve, nem egyenlők az éles app-funkciókkal**.

### Visszaállított eredeti elemek
1. [30 napos intuíció, rejtett jelek, predikciós tanulás](docs/ATP_30_NAPOS_TANULASI_PROGRAM.md), napi 30–45 perc egykori javaslat; az első körből induló időtartam nem tudományos garancia.
2. [Blind Prediction protokoll](docs/ATP_BLIND_PREDICTION_50_PROTOCOL.md): első megérzés statisztika és oddsok előtt, időbélyegzetten, **legalább 50 tényleges** próba a korábbi kísérleti terv szerint, külön intuíció / modell / kombináció.
3. [50 üres tesztsor](research/templates/blind_prediction_50_ures_sor.csv); szimulált, tényleges meccs nélküli adatokból nem állítunk valós mérési eredményt.
4. [Virtuális EV/odds és zárolt predikciónapló](docs/ATP_VIRTUAL_PREDICTION_AND_EV.md) és [50 üres virtuális naplósor](research/templates/virtual_ev_naplo_50_ures_sor.csv). A „+EV” csak kalibrált p és valóban elérhető odds mellett jelenthet tesztelhető hipotézist; az aktuális terv nem automata pénzes fogadás.
5. **Tornaprioritás / motiváció / pontvédelem / utazás / regeneráció** bizonyítékalapú vizsgálata: [10 tényezős Pre-Match](docs/ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md), [A/B húsz üres mezős sablon](research/templates/prematch_10_tenyezo_A_B_ures_sor.csv).
6. [Pre-Match A és B tízpontos tényezőlista](docs/ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md) és a hatféle lehetséges meccsfordulat-magyarázat. Egyetlen vereség, megjelenési díj, vagy korai kiesés alapján nem következtetünk motivációra, manipulációra, rejtett sérülésre, pszichológiai alkati címkére.
7. [Automatikus ATP-meccs-előszűrés és korai alert](docs/ATP_AUTO_MATCH_SCREENING_REQUIREMENTS.md). Cél: ne kelljen minden meccset élőben nézni; adat-only üzemmód önállóan, videó opcionális, hiányzó adat = NO SIGNAL. Korábbi **70–80% automatizálás** ambiciózus terv, nem elért KPI.
8. [Mobilos PWA architektúra](docs/ATP_MOBILE_PWA_ARCHITECTURE_OPTIONS.md): React PWA/Python FastAPI/PostgreSQL/Supabase/push egykori **opció**, nem a mostani Streamlit kód lecseréléséről szóló döntés.
9. [Tennis API felhasználási engedély = FELHASZNÁLÓ ÁLTAL KORÁBBAN ELLENŐRZÖTT ÉS ÚJRA MEGERŐSÍTETT, LEZÁRT](docs/ATP_TENNIS_API_ENGEDÉLY_ES_INTEGRACIO.md). A saját alkalmazásban való felhasználás és saját AI-elemzéssel kiegészítés engedélyének terjedelmét **nem kérdőjelezzük meg újra**. Az API provider **tényleges technikai csatlakoztatása** a Sportscore RapidAPI prototípustól független fejlesztési feladat. A saját privát alkalmazás az aktuális végső scope, nem SaaS.

**Régi beszélgetésből tételesen még nem helyreállított elem:** a korábban említett **12 edzői tudásterület 48 konkrét jelének felsorolása**; a feltöltött ATP(1).txt-ben nincs meg. Ne találjunk ki 48 jelet és ne állítsuk, hogy ellenőriztük.


## 2026-11-22 – ATP hívószó és tényleges privát eredeti szövegarchívum

A felhasználó végleges projekt-hívószava **csak `ATP`**. A korábbi `ATP-MASTER-150` felülírt kód és nem használandó. **Kötelező indítási protokoll:** [docs/ATP_START.md](docs/ATP_START.md), [tartós munkanapló](docs/ATP_SESSION_LOG.md), [AGENTS.md](AGENTS.md). Az eredeti felhasználó által feltöltött `ATP(1).txt` **1006 soros szöveges archívuma** most már külön, owner-only hozzáféréssel megőrzött **ChatGPT Space: `ATP – Privát projektarchívum`** / `ATP – Eredeti beszélgetés teljes szövegarchívuma (ATP(1).txt)` oldalon is megtalálható; a jelenleg nyilvános GitHub repo **nem tartalmazza a privát beszélgetés teljes szövegét**. A feltöltött fájl eredeti SHA-256: `ffceb2da5985304084e7d4d26ad9982d260106ae31198eede17d503404d24f01`. A Space szöveges átírásának formázása eltérhet a bájtra azonos nyers TXT-től; hiányzó eredeti képi mellékleteket sem pótol automatikusan.

**Folytonossági elv:** minden jelentős új döntés/implementáció után a releváns GitHub dokumentumokat, a `PROJECT_MASTER.md`-et és a `docs/ATP_SESSION_LOG.md`-et frissítjük; a tényleges GitHub commit és a validáció külön rögzítendő. A privát Space használatához az új beszélgetésben csatlakozó és jogosultság szükséges; a `ATP` szó önmagában nem képes platformszintű teljes, automatikus chatátvitelre. Ez a megoldás a ténylegesen rögzített forrásszövegből és döntésekből teszi lehetővé a folytatást, a hosszú szálak megismétlése nélkül.


**Kiegészítő egyszeri beállítás (2026-11-22):** [ATP – projektutasítás a ChatGPT projekthez](docs/ATP_PROJECT_INSTRUCTIONS.md). Ez biztosítja, hogy a projektben indított következő beszélgetés az `ATP` jelzésre GitHub és privát archívum forrásokból töltse be a korábbi döntéseket. A korábban feltöltött TXT **bájthű másolata már a személyes ChatGPT Library-ben** is elérhető: `/ATP/Conversation_Archive/ATP(1)_eredeti_2026-11-22.txt` (36 620 bájt). A projektutasítást a felhasználónak egyszer kell megadnia a ChatGPT Projekt beállításaiban; a GitHub/Space projektfájlok létrehozása önmagában nem módosítja a ChatGPT belső projektutasításait.

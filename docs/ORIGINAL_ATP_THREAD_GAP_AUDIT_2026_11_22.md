# ATP Intelligence – eredeti ATP(1).txt beszélgetés és tárolt projektállapot: hiányossági audit

**Dátum:** 2026-11-22
**Vizsgált elsődleges forrás:** a felhasználó által feltöltött `ATP(1).txt` (1006 sort tartalmaz a lokális fájl, az indexed forrás 1007 sort jelez a záró sortörés miatt).
**Összevetés:** `PROJECT_MASTER.md`, `docs/TEMPORAL_RELEVANCE_POLICY.md`, `docs/CONVERSATION_MIGRATION_AUDIT_2026_11_22.md`, Notion ATP Intelligence projektközpont és „01–04” aloldalak, 2026. november 22-én megtekintve.

**Alapvető korlát:** a `txt` exportált/felhasználó által bemásolt szöveg több fejezetet, korábbi asszisztensi javaslatokat és összefoglalókat tartalmaz, de az egyes üzenetek eredeti beszélőazonosítói és a korábbi képek/e-mailek eredeti csatolmányai nem mind jelennek meg; a teljes régi szál pontos, szövegszintű rekonstrukciója nem bizonyított. Az eredeti teljes szöveget nem mentjük automatikusan a nyilvános GitHub repositoryba.

## Valóban hiányzott vagy lényegesen aluldokumentált részek

### H01 – A projekt eredeti, három képességre épülő tanulási tengelye [HIÁNYZOTT]
**Forrás:** `ATP(1).txt` 1–9, 56–73. sor.
- Intuíció (előérzet és mintafelismerés), rejtett jelek, előrejelzés **három külön képesség**, amelyek kombináltan is tesztelhetők.
- Az intuíciót nem feltételezzük valódinak: előre rögzítjük, kalibráljuk és tényleges eredménnyel összehasonlítjuk.
- 30 napos első tréning, eredeti javaslat napi 30–45 perccel; a tanulási program külön ág a mobilalkalmazás implementációjától.
**Minősítés:** korábbi működési és tanulási terv; nem jelenik meg a PROJECT_MASTER elsődleges követelményei között. A felhasználó a későbbi appfejlesztésre váltott; ezért az ütemezést **tervként**, nem jóváhagyott határidőként kell megőrizni.

### H02 – Blind Prediction és 50 méréses összehasonlítás [HIÁNYZOTT]
**Forrás:** 130–147, 298–312. sor.
- Első benyomás *még a részletes statisztika és oddsok megtekintése előtt*, időbélyeggel, valószínűséggel.
- Az eredeti terv legalább 50 alkalmat javasolt; külön értékeljük (A) intuíció egyedül, (B) statisztikai modell egyedül, (C) együtt.
- Az eredeti javaslat 50–100% közötti megadott valószínűséget említ; a későbbi modellben a teljes 0–100%-os skála és kalibráció szükséges, az eredeti tréningjavaslatot változtatás nélkül megőrizzük.
**Minősítés:** nem azonos az általános Prediction Engine-nel; önálló tanulási/naplózó követelmény.

### H03 – 30 nap részletes napi lebontás [HIÁNYZOTT]
**Forrás:** 64–73, 238–291. sor.
- 1–5. nap: intuíció; 6–10: rejtett jelek; 11–15: rövid távú; 16–20: hosszú távú előrejelzés; 21–25: piaci összehasonlítás; 26–30: integrált értékelés.
- Az előrejelzést előre kell lezárni, utólag csak az eredmény és értékelés módosulhat.
- Mérőszámok: intuíció pontosság, jelérzékelési előny, predikciós pontosság, Brier, kalibráció, virtuális ROI.
**Minősítés:** külön, korábbi oktatási vázlatként megőrzendő, nem automatikusan aktív napi feladat.

### H04 – Prediction Sheet, H1–H4 és papíralapú/virtuális odds-réteg [RÉSZBEN]
**Forrás:** 148–158, 175–237, 281–291, 844. sor.
- H1 következő pont; H2 következő game; H3 következő 2–3 game; H4 szett/mérkőzés.
- Az eredeti „ATP Prediction Sheet”: mérkőzés, jelenlegi állás, két játékos, első intuíció, megfigyelt jelek, saját százalék, cél-esemény, opcionális élő odds; a predikció esemény előtt véglegesen időbélyegzett.
- Piaci összevetés: `EV = p * decimal_odds - 1` számítás, külön árfolyam- és árromlás, odds-frissesség, árrés és becslési hiba. A 4.00 odds / 32% / +28% példa kizárólag illusztráció, nem mért előny.
- Első lépés a szövegben **virtuális/szimulált teszt**; valódi pénzes automatizálás nem cél.
**Minősítés:** a központi dokumentum tartalmaz predikciót és odds-kockázatot, de a konkrét napló/adatmezők és intuíciós kísérlet hiányosak.

### H05 – Mérkőzés előtti tízpontos prioritási/terhelési vizsgálat [RÉSZBEN]
**Forrás:** 318–439, 486–499, 558–574. sor.
Az eredeti sorrend:
1. előző és következő versenynaptár;
2. konkrét torna egyéni prioritása;
3. előző évi eredmények és ranglistapont-védelem;
4. előző heti mérkőzésszám, játékidő, döntő;
5. regeneráció / mérkőzések közti idő;
6. utazás, időzóna és helyszínváltás;
7. borítás és borításváltás;
8. igazolt sérülés/kezelés/visszalépés;
9. múltbeli dokumentált nyomáshelyzet-minta;
10. forrással alátámasztott motiváció/prioritás.
**Minősítés:** a PROJECT_MASTER Pre-Match Context modulja megőrzi az irányt, de az explicit kötelező **10 pont** és játékosonkénti jelentősége nem volt végleges specifikációban.

### H06 – Miért „esik össze” valaki: magyarázatok különválasztása [RÉSZBEN]
**Forrás:** 440–484, 546–553. sor.
- A régi példában az első szett győztese később visszabréket és harmadik szettet veszít.
- Versengő hipotézisek: fizikai fáradás, megfigyelhető nyomás-reakció, ellenfél taktikai alkalmazkodása, bizonyított sérülés/fájdalom, normál variancia, ellenfél teljesítményének tényleges javulása.
- Nem következtetünk pusztán az eredményből meccsmanipulációra; megjelenési díj nem automatikus bizonyíték a motivációra.
- A mentális profil mérhető break-, tie-break-, hátrányból fordítás- és hosszú meccsek utáni kimenet, nem diagnózis.
**Minősítés:** általános „nem diagnosztizálunk” szabály megvolt, de a hat konkrét alternatíva és a különleges torzítások nem.

### H07 – Az app ne várjon állandó élő videómegtekintést [RÉSZBEN]
**Forrás:** 578–582, 674–749, 846–855. sor.
- Az eredeti célként megnevezett **70–80% automatizálás** aspiráció, nem már elért arány.
- Az app előre gyűjti a naptárt/terhelést/borítást/H2H-t, előszűri a meccseket, és csak értékes vagy szokatlan jelzésnél értesíti a felhasználót.
- **Videó nem kötelező**, hanem a kiválasztott meccsek másodlagos ellenőrző rétege; videó nélkül testbeszéd/biomechanika nem állítható meg.
- A „nincs elég adat” önmagában érvényes és fontos riasztási kimenet.
**Minősítés:** általános alert-cél megvolt, de működési workflow, tervezett automatizálási cél és videó nélküli UX nem elég expliciten.

### H08 – Mobilos PWA és technológiai elképzelés [KORÁBBI JAVASLAT, NEM VÉGLEGES DÖNTÉS]
**Forrás:** 750–789, 834–844, 856–884. sor.
- React PWA / Python + FastAPI / PostgreSQL vagy Supabase / push értesítés; szerveroldali API-kulcs.
- Az eredeti szöveg alternatívákként teljes natív iPhone appot és fokozatos PWA→natív utat is felsorol.
- Az aktuális GitHub **Streamlit prototípus**: az eredeti stack-javaslat nem bizonyít technológiaváltás melletti végleges felhasználói döntést. Nem szabad a működő kódot a javaslat miatt törölni.
**Minősítés:** megőrzendő architektúra-opció és mobilos használhatósági kritérium.

### H09 – Tennis API korábbi felhasználási engedély [FELHASZNÁLÓ ÁLTAL ELLENŐRZÖTT ÉS ÚJRA MEGERŐSÍTETT]
**Forrás:** `ATP(1).txt` 889–935. sora és a felhasználó 2026-11-22-i kifejezett helyesbítése.
- A szolgáltatóval korábban egyeztetett felhasználási terjedelmet a felhasználó **már ellenőrizte**, és ezt a jelen beszélgetésben ismét megerősítette. **Nem nyitjuk újra engedélyezési kérdésként.**
- A korábbi egyeztetés a Tennis API adatainak saját alkalmazásban, saját AI-elemzéssel történő megjelenítésére, és akkoriban akár havi díjas SaaS lehetőségre is kiterjedt. A korábbi „Yes.” válasz az egyeztetés történeti része; a felhasználó jelenleg **privát, nem fizetős** alkalmazást kér.
- A jogi felhasználási terjedelem **projektben elfogadott és lezárt**. A másik, önálló kérdés: a jelenlegi `tennis_api_client.py` Sportscore RapidAPI klienst használ, és még nincs teszttel igazoltan bekötve a kiválasztott Tennis API provider.
- A privát e-mail és API-kulcs tartalmát nem töltjük a nyilvános repóba; erre nincs is szükség a felhasználó által már megerősített engedély elfogadásához.
**Minősítés:** [végleges döntés és integráció külön](ATP_TENNIS_API_ENGEDÉLY_ES_INTEGRACIO.md).

### H10 – Időablak, H2H-súlyozás és történeti Elo [MÁR MEGVAN]
**Forrás:** 938–1004. sor.
- A 2026/2025 relevancia, 2024 és régebbi H2H 0 közvetlen súlya, friss forma előnye, kísérleti idősúlyok és historikus Elo elkülönítése **már** dokumentálva és részben kódolva.
- A felhasználói állítást nem változtatjuk meg; a kétidényes politika 2027-ben 2027/2026-ra vált.
**Minősítés:** átadás ellenőrizve; további adatintegráció és visszateszt szükséges.

### H11 – ATP és Challenger scope eltérése [IDŐBELI DÖNTÉS ÉS OPCIÓK]
**Forrás:** 356–368, 856–884. sor.
- Korai válaszban Challenger elemzés és ATP/Challenger alternatívákat is említettek, de ezek választási javaslatok/opciók voltak.
- A frissebb, a PROJECT_MASTER-ben feljegyzett döntés: ATP 250/500/Masters/Finals és Grand Slam férfi egyes főtábla mint **célmeccs**, és tartósan ATP Top150 profil. Challenger/ITF **nem** célmeccs, de háttérforrásként felhasználható, ha forrás és mintakör világos.
**Minősítés:** nem hiány, hanem felülírt régi lehetőség. Nem állítjuk vissza automatikusan.

### H12 – 12 edzői tudásterület és 48 megfigyelhető jel [EBBŐL AZ ANYAGBÓL NEM REKONSTRUÁLHATÓ]
**Forrás:** a feltöltött `ATP(1).txt` teljes szövegében **nem szerepel a „48” vagy a „12 edzői” kifejezés**; az új beszélgetés korábbi személyes/projektkontextusából merült fel. A feltöltött szövegben vannak edzői mérési témák (87–98, 472–484), de a 48 konkrét elem tételes listája nincs.
**Minősítés:** továbbra is nyitott, nem lehet a dokumentumból rekonstruáltnak jelenteni.

## Kötelező különbségtétel
- **Forrásban szerepelt:** a TXT-ben olvasható korábbi terv, állítás vagy korábbi asszisztensi javaslat.
- **Felhasználó jóváhagyta:** csak akkor állítható, ha erre konkrét, megőrzött felhasználói üzenet vagy végleges későbbi döntés van.
- **Megvalósult:** akkor, ha tényleges GitHub-kód, teszt és ellenőrzött adatfeed igazolja.
- A beszélgetés szövegében szereplő szemléltető UI/odds-számok nem jelentenek valós ATP-mérkőzési eredményt és nem valós előrejelzési előnyt.

## Javasolt integráció
1. A PROJECT_MASTER tartós követelményeihez hozzáadni az intuíciós naplózás, 30 napos tréning-terv, tízpontos Pre-Match, automatizált szűrés, és virtuális piacértékelés visszakereshetőségét.
2. A PWA stack-javaslat továbbra is nem végleges technológiai opció; a Tennis API felhasználási engedélyét viszont a felhasználó **ellenőrzött, lezárt döntésként** megerősítette. Az integráció külön fejlesztési feladat.
3. A 12/48 jel tételes felsorolásához **egy másik korábbi forrás** vagy eredeti export szükséges; jelen fájl önmagában nem elég.
4. A privát szolgáltatói levelezést nem kell újra feltölteni vagy ellenőriztetni az engedély elfogadásához. Az API-ellátottságot és tényleges kódbekötést külön teszteljük; API-kulcsot soha nem osztunk meg.

## Források
- A felhasználó által feltöltött `ATP(1).txt` (2026.11.22-i átadási forrás, nem publikált a GitHubra).
- [GitHub fő dokumentum](../PROJECT_MASTER.md)
- [Előző migrációs audit](CONVERSATION_MIGRATION_AUDIT_2026_11_22.md)
- [Időbeli relevancia](TEMPORAL_RELEVANCE_POLICY.md)
- [Notion projektközpont](https://app.notion.com/p/41ff603f0d2e8121a7c6c2cc89ff4213)


## 2026-11-22 – mind a 9 felhasználó által kiemelt hiány pótolva
Az eredetileg H01–H09 pontokban hiányzó specifikációkat a GitHubba mentettük; részletes átadási és státuszindex: **[9 hiányzó témakör pótlási jegyzéke](ATP_9_HIANYZOTT_TERULET_POTLASA_2026_11_22.md)**. Az engedély terjedelme a felhasználó által újra megerősítetten **ellenőrzött és lezárt**, nem nyitott jogi kérdés. Az app funkcióinak teljes implementációja külön fejlesztés, a jelenlegi dokumentumok újraépített követelmények és üres sablonok. A tételes 48 edzői jel továbbra nem áll rendelkezésre ebből a forrásból.

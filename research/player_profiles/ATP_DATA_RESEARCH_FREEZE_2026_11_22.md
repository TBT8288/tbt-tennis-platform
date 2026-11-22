# ATP Intelligence – DATA RESEARCH FREEZE / KÓDOLÁSI ÁTADÁS (2026-11-22)

**Státusz: PRE-CODING RESEARCH GATE = PASS WITH DECLARED GAPS.** Ez **nem** jelenti a teljes 150 játékos edzői/mentális validálását, és **nem** jelenti az API éles tesztjét. A cél a végtelen előzetes adatgyűjtés leállítása és a kódolás megkezdése.

**Fontos:** ez a dokumentum a PR #13 külön kutatási branchén készült. Nincs automatikus merge, és a `main` ág nem változik. A kutatási döntés csak az ellenőrzött mezőket és forrásokat engedi be, nem minősít bizonytalan adatot validáltnak.

## 1. MIT TÉNYLEGESEN ELLENŐRIZTÜNK A REPOBAN?

Kiinduló alap: `main` = `71de3c61f11a76c71787bd1c316071c4e6e81aef`, ranglista `2026-11-16`.

- `research/player_profiles/atp_top150_profile_register_2026_11_21.csv`: **150 sor**, **51 mező**, nincs duplikált játékosnév. Alapadat: 150/150; kezesség: 150/150 (134 jobb / 16 bal); magasság és súly: 134/150; fonák: 104/150; 2026 szezon W/L: 146/150; `Pressure+`: 122/150; `grass_elo`: 147/150; `indoor_elo`: 148/150. Edző 12/150 forrás-snapshot, nem napi aktuális.
- `research/player_profiles/TOP150_EVIDENCE_PROFILE_REGISTER_2026_11_21.csv`: **150 sor**, **69 mező**; 2025–26 statisztika, borításspecifikus mutatók, forma, tb/döntő szett; a 2026 archív metrikák 148 játékosnál töltöttek; utolsó archív cutoff **2026-11-15**.
- `research/player_profiles/TOP150_H2H_2025_2026_THROUGH_2026_11_15.csv`: **2 809 nem üres megfigyelt játékospár**, összesen **3 855 megfigyelt kétidényes egymás elleni találkozó** a táblában. Nem teljes napi H2H. A `latest_event_date_observed` vegyes: **1 816 ISO-időbélyeg**, **993 YYYYMMDD**, ezért kötelező normalizálás; a hiányzó H2H nem jelent nulla esélyt, vagy gyenge mentalitást.
- `research/player_profiles/ATP_TOP150_VALIDATION_STATUS_2026_11_22.csv`: 150 sorban elkülönített hiányok. A többmeccses igazolt szerva+1, fogadás+1, mozgás, teljes technikai és mentális profil **0/150 validált**. Ez nem akadályozhatja az alapmodell elkészítését.
- PR #13 négy új, **még össze nem vont** forrás-jelölt CSV/MD fájlt kínál: 16 fizikai adat, 46 fonákjelölt és négy statisztikai kivétel. Potenciális kitöltöttség 150/150 a fizikainál és fonáknál; **nem masteradat**, külön QA kell. Ilia Simakin súlya 84/85 kg forráskonfliktus. Martin Damm nevet érdemes ID-vel (fiatal 2003-as USA játékos vs idősebb korábbi cseh játékos) párosítani; egyes aggregátorok név- és karrieradatokat keverhetnek.
- Az anyag nem tartalmaz 150 megalapozott személyiség- vagy sérülésdiagnózist; a pontszám, Pressure+, tie-break, döntőszett önmagában NEM diagnózis.

## 2. NÉGY KIVÉTELES 2026-OS SZEZONREKORD – FORRÁSOLT EREDMÉNY

2026-11-22-i TennisDB egyéni oldal: az alábbi **forrásoldali** ATP-főtábla / selejtező bontás elérhető; **NE automatikusan írjuk felül** a korábbi napi pillanatképet. A TennisDB főtábla-számlálója walkovert is tartalmazhat; modell-specifikus tisztítás szükséges.

| Játékos | ATP főtábla 2026 forrás szerint | 2026 selejtező | Forrás | QA |
|---|---|---|---|---|
| Otto Virtanen | 1–6 | 10–9 | https://tennis-db.com/players/224/otto-virtanen | PR #13 korábbi 1–5 eltérés: forrásidő és meccskör/wo egyeztetendő |
| Clément Chidekh | 2–1 | 4–4 | https://tennis-db.com/players/352/clement-chidekh | forrás dátuma 2026-11-22 |
| Max Alcalá Gurri | nincs főtáblás rekord a forrásban (MISSING, nem automatikus 0) | 0–2 | https://tennis-db.com/players/485/max-alcala-gurri | Challenger nem azonos ATP-főtáblával |
| Nikolas Sánchez Izquierdo | nincs 2026 főtáblás rekord a forrásban (MISSING, nem automatikus 0) | 1–3 | https://tennis-db.com/players/405/nikolas-sanchez-izquierdo | PR #13 korábbi 0–1 Q adata hiányos volt |

Ezen négy különböző versenykörű adat nem egyenértékű a teljes 146 főre érvényes 2026-os szezonstatisztikával; legyen explicit `scope`, `observed_on`, `missing_reason`.

## 3. FONTOS: AZ API SZOLGÁLTATÓ AZONOSSÁGA

A korábban privátként megőrzött, felhasználó által megerősített kapcsolatban a szolgáltató elnevezése `API-Tennis`. A legvalószínűbb megfelelő **https://api-tennis.com/** (nem összekeverendő a hasonló nevű `tennis-api.com`, `tennisapi.dev` vagy `livetennisapi.com` termékekkel). A **jogos felhasználási terjedelmet a felhasználó lezártnak tekinti; nem kell újra rákérdezni**. A fiók pontos hostjának/kulcsjogosultságainak tényleges egyeztetése külön technikai teszt, nem engedély-újratárgyalás.

Hivatalos publikus források, 2026-11-22-i olvasás:
- REST: https://api-tennis.com/documentation (2.9.5)
- WebSocket: https://api-tennis.com/documentation_websocket (1.2.1)
- Példa REST alaphost: `https://api.api-tennis.com/tennis/` ; módszerek query paraméterben.
- `get_events` – csomagban elérhető eseménytípusok, példában ATP Singles `event_type_key=265`; mindig API-ból azonosítsuk, ne univerzális hardcode.
- `get_tournaments` – tournament_key + event_type_key.
- `get_fixtures` – `date_start`, `date_stop`, `event_type_key`, `match_key`, `player_key`; meccsobjektumban `pointbypoint`, `scores`, `statistics` lehet (néha üres tömb).
- `get_livescore` – live board, `event_key`, `first_player_key`, `second_player_key`, `event_serve`, `event_status`, `event_type_type`, `event_qualification`, `pointbypoint[].points[]`, `statistics[]`.
- `get_H2H` – két `player_key` alapján: H2H és külön formák; az évszabályt **mi** szűrjük az eseménydátum alapján.
- `get_players` – szolgáltatói `player_key`, név, születési dátum, szezonrekordok; külső ATP/TennisDB/archív ID-khez explicit mapping kell.
- `get_live_odds` – ha a saját előfizetés/feltételek engedik; az odds-példák önmagukban nem bizonyítanak tényleges piaci likviditást / frissességet.
- Push `wss://wss.api-tennis.com/live` – a dokumentáció szerint élő változáskor üzenet; WebSocket külön tételes meccsadat-ellenőrzéssel, költség/jogosultság szerint. REST polling legyen fallback.
- A publikált mintában `pointbypoint[].points[]` sorszámot, állást, break/set/match-point jelöléseket tartalmaz; **pontonkénti objektív ütésirány, szerva+1, lábmunka, nyers video és hiteles ponttörténeti event_time nem igazolt**. Az `event_date` és `event_time` nem automatikusan az egyes pontok valódi időbélyegei.
- APIkey a dokumentációban query paraméter: **se API-kulcsot, se teljes URL-t soha ne logoljunk**, csak szerveroldali secrets, kiszűrt request log és tesztfixture. Jelenlegi repo `tennis_api_client.py` **másik Sportscore RapidAPI klienst** használ; ezt megőrizzük külön adapterként, az új API-Tennis klienst külön írjuk.

Az API-kliens valódi lefedettsége, kvótája, sebessége **NINCS még hitelesített éles adattal tesztelve**. Ez **első kódolási sprinten belüli integrációs audit**, NEM többhetes kódolás előtti kutatási blokkoló.

## 4. ADATKUTATÁS STOP-SZABÁLY / GATE

**KÓDOLÁS INDÍTHATÓ MOST** a fenti 150 rekorddal, kétidényes mintával, explicit hiányjelöléssel, forrás-/évdátumokkal és külön valószínűségi alapmodullal. Nem várunk:
- 150/150 szerva+1 / return+1 / 0–4 rally / biomechanikai / mentális profilt;
- minden korábbi H2H adatot, új podcastok teljes átírását;
- éles live pontfeed nélkül generált „momentum-előnyt”;
- egyes játékosok hiányzó metaadatai miatt újabb általános kutatási hullámot.

Ami továbbra is kötelező: valós adat azonosító és dátum szerinti validálása, null/missing kezelés, frissességi és forrásjelzés, no-lookahead, tesztadat vs valós adat különválasztása. **2026-ban csak 2025/2026 meccseknek van közvetlen prediktív súlya; 2027-ben 2026/2027.** 2024 előtti H2H közvetlen súlya 0. Historikus Elo külön baseline.

## 5. KÖVETKEZŐ FEJLESZTÉSI SORREND – NE INDÍTSUNK ÚJABB FORRÁSKUTATÁSI KÖRT

1. **QA/ID/CSV normalizáció**: 150 player betöltés, 16+46 overlay jóváhagyott mezők és konfliktusok kezelése; 2025/2026 dátumparse normalizálása, 2025/2026 match source szűrés, H2H deduplikálás, 4 kivétel `MISSING` vagy megjelölt főtábla-scope.
2. **API-Tennis adapter mock-fixture-rel**: `get_events`, `get_livescore`, `get_fixtures`, `get_players`, `get_H2H`, opcionális odds; `event_key`/player_key mapping; mock és contract tesztek, hiányzó/üres mezők, rollback, retry/rate-limit, key-redaction.
3. **Valódi API smoke test** saját biztonságosan beállított szerveroldali hozzáféréssel (nem chatbe küldött kulccsal): 1–2 valós, időbélyegzett ATP meccs; pontfeed megbízhatóság és késés, azonosítók, kvóta és felhasználható mezők.
4. **B0/B1 adat és modell bekötése** a meglévő `atp_intelligence/probability.py`, `events.py`, `storage.py` alapokra, a #12 B0 demo külön PR ellenőrzésével; A/B játékos külön állapota, outputban bizonytalanság; nincs „mentális diagnosis”.
5. **Előzetesen időbélyegzett backtest és live audit**: validált Brier/log-loss, kalibráció, lead time, false alarm, no-lookahead, selection bias; csak innen további coach-feature / mobil-PWA / értesítés.

Első PR-ek még nem merge-elve: #12 B0 UI, #13 adatkutatás; a `main` csak felhasználói jóváhagyásra változhat. Az API bekötésnél a meglévő Sportscore működést ne romboljuk le.

## 6. ÚJ ATP-BESZÉLGETÉSBE VALÓ 2 SOROS ÁTADÁS

`ATP` → olvasd `PROJECT_MASTER.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md`, majd PR #13 ezen dokumentumát. **Kutatási gate PASS WITH DECLARED GAPS**: az új szál ne kérje elölről a játékosadatokat vagy az engedélyt; a következő munkafázis **kódolás / adat- és API-Tennis adapter**.

A forrásolt kutatási hiányok a rendszerben adatminőségi flagként élnek tovább, nem indokolják a projekt újabb „kutatás előbb, kód csak később” újraindítását.

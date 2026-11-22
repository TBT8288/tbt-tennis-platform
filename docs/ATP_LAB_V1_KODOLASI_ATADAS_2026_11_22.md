# ATP Lab – kódolt V1 fejlesztői átadás (2026-11-22)

**Állapot:** működésre előkészített, külön indítható, magyar Streamlit UI + forrás- és dátumérzékeny Top150 adatréteg + mockolható API-Tennis kliens; a GitHub Actions eredménye jelzi az automatizált kódtesztet. **Nem** kész, validált élő momentum/coach algoritmus, és nem tesztelt valódi API-Tennis előfizetéssel.

## 1. Egyetlen indítási parancs Mac / Linux

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run atp_lab.py
```

Az alap játékosprofil-, H2H- és B0-kalkulátor **offline**, API-kulcs nélkül is használható. Az új UI külön `atp_lab.py` fájl: a régi `app.py` / Sportscore RapidAPI / Gemini felület változatlan. A jelenlegi Python 3.12-es GitHub Actions csak forrásfordítás- és unit-teszteket végez, nem UI-kattintásos vizsgálatot.

### Opcionális, tényleges API-Tennis

A felhasználó által **korábban lezártnak megerősített felhasználási engedélyt nem nyitjuk újra**. A jelenlegi teszthez csak technikai API-fiók/aktív kulcs kell. Soha ne másold a kulcsot GitHubra, chatbe, issue-ba vagy kódba.

Szerveroldali lokális környezeti változóban:

```bash
export API_TENNIS_KEY='SAJAT_KULCSOD_HELYBEN'
python3 -m streamlit run atp_lab.py
```

A fenti szövegben szereplő `SAJAT_KULCSOD_HELYBEN` csak helykitöltő. A dokumentáció kézi API-hívásnál POST form adatot használ, hogy a kulcs ne jelenjen meg a request URL-ben. Szolgáltatói szerverlogokat nem tudunk ellenőrizni. A valódi kapcsolatot **nem tudtuk API-kulcs nélkül tesztelni**; lekérés csak gombnyomásra indul, nincs automatikus fizetős háttérhívás.

## 2. Megépített modulok

| Fájl | Tény |
|---|---|
| `atp_intelligence/api_tennis.py` | request validation, kulcs URL-ből kizárva, sanitized hibakezelés, rate limit retry, mockolható transport; events, tournaments, fixtures, livescore, players, H2H, live odds |
| `atp_intelligence/player_data.py` | 150 név, 51 mezős master regiszter, PR #13 16 fizikai és 46 fonák *jelölt* forrás, provenance, 2025/26 H2H dátumparse, no-lookahead gate |
| `atp_lab.py` | offline-first magyar UI két játékossal, 2025/26 H2H, B0 gémkalkulátor, opcionális API élő lekérés |
| `tests/test_api_tennis_and_player_data.py` | offline integrációs/hibakezelési tesztek és valós meglévő CSV lefedettségi tesztek |

A fő korábbi V1 `game_win_probability` csak felvett, állandó szervapont-valószínűségből számol. Az eredmény **nem valós predikció vagy odds-előny**.

## 3. Forrásra és használhatóságra vonatkozó rögzített állítások

- Elsődleges dokumentáció: https://api-tennis.com/documentation ; WebSocket: https://api-tennis.com/documentation_websocket.
- Provider tipikus `event_key`, `first_player_key`, `second_player_key`, `event_serve`, `pointbypoint`, `statistics` mezőket ad. Pontonkénti `event_time` **nem igazolt**; a `received_at` saját rendszerünk adatfogadási ideje, nem a szolgáltatói tényleges pont ideje.
- Az `Atp Singles` címke nem bizonyítja az ATP250/500/M1000/Finals/Grand Slam főtábla-jogosultságot: az `approved_tournament_keys` explicit forrásellenőrzése szükséges, a hiányzó selejtezőflag nem tekinthető biztos `False` értéknek.
- Forrásokat és felhasználási korlátaikat őrizzük; harmadik fél 2025-ös teniszarchívuma CC BY-NC-SA anyagokat is tartalmazhat, ezért külön publikálási/üzleti jogellenőrzés nélkül nem újraosztható.
- A 2026-11-15-i H2H archívum aggregált és eltérő dátumformátumú. A `TwoSeasonH2H` **nem enged** 2026-11-15-én vagy korábban backtestet ebből a teljes archívumból, mert az események történeti cutoff előtti megoszlása nem visszaépíthető a pár-szintű összesítésből. Tényleges backtesthez egyedi, időbélyegzett mérkőzések kellenek.
- Testsúly forrásütközés: Ilia Simakin 84 kg / 85 kg; csak jelölt adat, nem javítjuk át találomra. `Top150Profiles` eredeti 150 soros masterfájlt **nem módosítja**.
- Négy külön kezelendő szezonstatisztikai hiány: Otto Virtanen, Clément Chidekh, Max Alcalá Gurri, Nikolas Sánchez Izquierdo. A forrásban eltérően számolt főtábla / selejtező / Challenger adatok nem keverhetők.

## 4. Mit NEM fogunk készként jelenteni?

- 150/150 többmérkőzéses validált mentális, szerva+1, mozgás és ütésirány megfigyelések: **hiányoznak**; API-score alapján nem gyárthatók.
- Valós Tennis API speed/latency/rate limit / quota/point-event timestamp és valós API teszt: **nincs** az aktuális futtatásban.
- Pályageometria, röpték, testbeszéd, pszichológiai okok: score-only feedből **nem állapítható meg**.
- Korrekt, előzetesen időbélyegzett statisztikai momentumvalidáció, Brier/log-loss, false alert: **külön valódi mérkőzési eseménysor kell**.
- A régi fő appba integrálás, automatikus live poll, mobilos natív PWA és Discord alert: **nincs bevezetve**; a V1 külön indítható UI.

## 5. Következő, már KÓDOLÁSI munkarend

1. PR #13 és e feature PR diff/CI ellenőrzése, a `main` csak a projektgazda jóváhagyásával merge-elhető.
2. A felhasználó által helyben beállított `API_TENNIS_KEY` mellett legalább két valódi, licencelt élő/archív főtáblás meccs mintafeldolgozása: a szolgáltatói schema, server, `pointbypoint`, latency, rate-limit és source event-time tényleges mérése.
3. Stabil ATP/CSV/provider `player_key` crosswalk, versenykategória/szűrés és no-lookahead egyedi eseményrekord alapján.
4. B0 demó PR #12 felhasználói jóváhagyás után fokozatosan kapcsolható; B1 adaptív szervapontbecslés, később ellenőrzött change-point mutatók.
5. Brier/log-loss és téves riasztások mérése; csak ezek után lehet korrekt predikciós előnyről beszélni.

**Új beszélgetésben `ATP`: olvasd `PROJECT_MASTER.md`, `docs/ATP_START.md`, `docs/ATP_SESSION_LOG.md`, PR #13 és a feature PR fenti dokumentumát. Ne térjünk vissza általános 150 fős kutatáshoz; a következő konkrét feladat API contract + valódi source-validáció.**

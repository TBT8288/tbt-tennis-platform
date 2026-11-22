# ATP – régi HWK Claude-modellből átvehető, biztonságos feature-séma

**Forrás:** [Claude/Notion 10 összefoglaló](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5) – a `tbt/` kód 2026.10.01-i történeti leírása, az eredeti kódfájlok nélkül.  
**Minősítés:** **tervezett feature-készlet**, nem működő megvalósítás, nem bizonyított predictive edge. Illeszkedés: [10 pontos Pre-Match](ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md), [Live Shift követelmények](ATP_AUTO_MATCH_SCREENING_REQUIREMENTS.md).

## 1. Hat teniszstílus, mint egységes címkekészlet
Az eredeti angol taxonómia pontosan:
1. `Big Server`
2. `Serve and Volleyer`
3. `All-Court`
4. `Attacking Baseliner`
5. `Solid Baseliner`
6. `Counter Puncher`

**Importálási szabály:** egyéni játékos stílusa **NULL/UNKNOWN**, amíg aktuális (2025/2026) forrás és szakmai ellenőrzés nem igazolja. A „Big Server (hibrid)” nem azonos tiszta 100%-os stílusértékkel: elsődleges és másodlagos címke, módszertan, dátum és megbízhatóság külön mező. A stílus borítástól, időtől és ellenféltől is függhet. A 12 játékos történeti Claude-besorolása **csak** [külön ellenőrzendő CSV-jelöltben](../research/player_profiles/CLAUDE_HWK_2026_10_01_STYLE_CANDIDATES.csv), nem a 150 fős éles master-táblába írva.

## 2. Feature-kandidátusok, elkülönített bizonyítékokkal

| Feature-kulcs | Lehetséges objektív bemenet | Óvintézkedés / státusz |
|---|---|---|
| `tactical_matchup` | A/B játékstílus 6 címkében, handedness, kis/ nagy szerva, forehand/backhand/return, igazolt kontextus | A régi 1,95× nem használható forrás és backtest nélkül |
| `mental_clutch_proxy` | break-point converted/saved meccsekre és borításra bontva, TB és döntő szett, mintaszám | **Nem mér valódi mentális állapotot**; `mental_clutch` eredeti elnevezés megtévesztő lehet |
| `court_weather` | CPR/pályasebesség *hiteles forrásból*, fedett/kültéri, időjárás, szél | CPR határok forrásauditot igényelnek; nincs spekulatív „lassú labda” tény |
| `surface_strength` | ATP Tour 2025/2026 borításon belüli eredmény, ellenfélerő, meccsmennyiség | történeti összesített Elo külön háttéradat |
| `serve_return` | első/második szerva pontnyerés, return points won, return games won, break-point converted | négy mutató NEM ekvivalens; szám és nevező külön mező |
| `load_travel` | előző heti lejátszott játékpercek, game/szettek, utazás, időzóna, pihenőnap | 16 game-es fáradási töréspont **nem** orvosi/validált jel |
| `tournament_priority_index` | igazolt pontvédelem, torna kategória, előző/következő meccsnaptár, nyilatkozat | motiváció **csak hipotézis**, soha nem egyetlen tényből levezetett szám |
| `regime_comeback_dominance` | előre definiált, statisztikailag elég mintás támadó/fogadó teljesítmény-váltás | a `COMEBACK`/`DOMINANCE` címke stratégiai esemény, nem diagnózis |
| `point_to_match` | szervapont-esélyek, aktuális szerváló, állás, szett-formátum, szabályok | 1+ pontbeváltás csak kalibrált inputból; nem elég az aktuális score |

## 3. Bizonyíték-séma – különítsük el a nullát a hiánytól
Ajánlott rekord:
```text
feature_id, match_id, player_id, value, units, source_url,
source_timestamp_utc, observed_at_utc, prediction_cutoff_utc,
coverage, sample_size, status, validity_window, missing_reason,
validation_method, model_version
```
- `value = null`: nem rendelkezésre álló/hiányzó információ; nem egyenlő a `0.0` mért értékkel.
- `evidence_weight = 0.0` (ha a kutatás nem ellenőrizhető): a **megbízhatósági súly** lehet 0, de az eredeti `value` marad hiány vagy forrásolatlan hipotézis. A `value=0` önmagában téves hamis adat volna.
- `source_timestamp_utc <= prediction_cutoff_utc`, no-lookahead. Ha a forrás publikálása későbbi, az adatra nem lehet azt állítani, hogy korábban ismert volt.
- a két játékos adatai külön; hiányzó adatból nem keletkezhet automatikus negatív mentális/kondicionális tényező.
- Forum-gyanú, sérülésre következtetés és meccsmanipulációs spekuláció **nem számszerű modellinput**.

## 4. Stílusok és pályasebesség
Az eredeti összefoglaló Court Pace Rating sávjai: ≤29 lassú, 30–34 közepesen lassú, 35–39 közepes, 40–44 közepesen gyors, ≥45 gyors. **Átvett történeti kutatási megjegyzés**, nem már összekötött API feature; ITF-forrás, adott pálya és esemény időpontja szükséges.
A „de Minaur all-court” módosítás a Claude-oldalon állítólag két forrás alapján történt; a konkrét két forráshivatkozást a Notion oldal **nem tartalmazza**. Ezért még nem lehet a 150 master profil automatikus átminősítésének alapja.

## 5. Régi előrejelzési/technikai megoldás elérhetősége
A Notion történeti kódnevei és 77 tesztje a korábbi Claude projektben szerepeltek. A mostani GitHub main ágon a felsorolt `tbt/` állományok nem lelhetők fel. A meglévő `atp_intelligence/probability.py` külön, átlátható B0 matematika; csak abból szabad azt állítani, hogy implementált.

## 6. Projektbiztonság, hogy ne vesszen el kód
- Minden működő állapot **GitHub commit**. Később ellenőrzött külön (privát) zip/release és titkosított backup, visszaállítási próba.
- Ne készítsünk titokkal/API-kulccsal ZIP-et; a régi ZIP-ekben előforduló nyers kulcsok kockázata miatt külön rotáció szükséges lehet, ha érvényesek.
- Az eredeti 77 tesztet nem tekintjük annak, hogy jelenleg 77 teszt lefut.

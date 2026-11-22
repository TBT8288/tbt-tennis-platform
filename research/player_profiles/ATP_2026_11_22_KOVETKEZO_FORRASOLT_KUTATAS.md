# ATP Intelligence – 2026-11-22 további forrásolt kutatási kör
**Státusz:** új, valóban ellenőrzött kutatási rekordok; a Top150 master és a fő app NEM módosult. A PR #13 kutatási ágát bővíti; a `main` változatlan.

## A kutatás konkrét új hozadéka

1. **26/150 Top150 játékos:** hivatalos, 2026. júniusi ATP/Tennis Data Innovations mérés 52 hetes ablakából **52 kiválasztott, két-két objektív taktikai/ütésminőségi mérőszám**, forrásdátummal. [Kutatási CSV](ATP_TDI_INSIGHTS_VERIFIED_26_2026_11_22.csv).
2. **12 új, teljesült ATP Finals férfi egyes mérkőzés, 2026-11-16–21:** meccsdátum, győztes, vesztes, szetteredmény, RR/SF, hivatalos forrás és független TennisDB-ellenőrzés. Ezek az előző H2H-archívum `2026-11-15` cutoffja utáni bizonyítékok, **nem** módosítottam visszamenőleg az aggregált H2H-t. [12 meccses CSV](ATP_H2H_NEW_COMPLETED_ATP_FINALS_2026_11_16_TO_21.csv).
3. **4 hiányos 2026 ATP-főtábla-szezonrekord forráskör szerinti újraellenőrzése:** megkülönböztetett főtábla/selejtező, hiány/szerepelt 0. [Négy játékos CSV](ATP_2026_SEASON_FOUR_GAPS_RECHECK_2026_11_22.csv).

## ATP TDI 52 hetes mérések – MIT jelentenek?

Az ATP hivatalos leírása szerint:
- `In Attack`: támadó fázisban játszott ütések/állapotok aránya, **nem** egyszerű meccs-győzelmi %.
- `Conversion Score`: támadó helyzetben megnyert pontok / támadó helyzetben játszott pontok.
- `Steal Score`: védekező helyzetből megnyert pontok / védekező helyzetben játszott pontok.
- `Serve/Return/Forehand/Backhand Quality`: AI + labda/játékoskövetés alapján képzett **0–10-es ütésminőségi pontszám**, nem szervapontnyerési arány.

**Források:**
- [ATP – Conversion és Steal fogalmak](https://www.atptour.com/en/news/insights-conversion-steal-score-explained)
- [ATP – TDI Insights: 0–10 shot-quality és mérési architektúra](https://www.atptour.com/en/news/insights-introduction)
- [ATP – június 16. Halle, 52 hetes játékosmutatók](https://www.atptour.com/-/media/2db23f0708d1497eb461bcd4997d6860.pdf)
- [ATP – június 20. Halle](https://www.atptour.com/-/media/a9cea1bc4795485daaf07d052028ab7f.pdf)
- [ATP – június 16. Queen's Club](https://www.atptour.com/-/media/316ad2d4cb684b27bf3d6f3eea7faf2d.pdf)
- [ATP – június 19. Queen's Club](https://www.atptour.com/-/media/95f4effdc9984d658c987a90c7d2c4ad.pdf)

**Kritikus időbeli értelmezés:** az egyes táblák 2026 júniusi **visszatekintő 52 hetes** ablakok. Nem novemberi aktuális forma, és nem tisztán 2026-os szezonadat; a 2025/26-os két év politikájába viszont időben beleillenek. A modellbe csak dátummal, méréshorizonttal, forrással és out-of-sample validáció után kerüljenek. A CSV-ben 26 játékosból kiválasztott két-két számszerű mutató szerepel, nem a teljes ATP TDI-adatbázis másolata.

**Rövid, forráshű technikai következtetések (NEM mentális diagnózis):**
- Giovanni Mpetshi Perricard: június 16-i `Serve Quality=9.3`, `Return Quality=5.3`: jelentős szerva–fogadás minőségbeli aszimmetria, matchup-teszt hipotézise.
- Daniil Medvedev: `Return Quality=7.7`, `Steal Score=37%`: magas fogadásminőség és hatékony védekezésre utaló mért értékek az akkori 52 hetes ablakban.
- Alex de Minaur: `Steal Score=37%` és `Serve Quality=7.5`: védekező helyzetből nyert pontok aránya erősebb jel a júniusi profilban, mint a szervaminőség.
- Alexander Bublik: `In Attack=30%`, `Conversion=72%`: akkori támadófázis-gyakoriság és konverzió az ATP-média 24% / 67%-os referencia mellett.
- Taylor Fritz: `Serve Quality=8.8`, `Steal Score=27%`: szervaerősség és a referencia alatti védekezésből nyert pont-arány.
- Alexander Zverev: `Serve Quality=8.7`, `Backhand Quality=8.1`: kiemelkedő mért szerva/fonák az ATP akkori referenciaértékeihez képest.

Az ATP Insights dokumentációjában szerepel **48 taktikai mintázat** (és 7 taktika) a nyomkövetési rendszerben. Ez **NEM** azonos a felhasználó korábban említett, de szöveges forrásból hiányzó 12 edzői terület/48 jel követelményével; ilyen összemosás tilos.

## 12 friss ATP Finals mérkőzés – miért fontos?

A 2026-11-15-én lezárt `TOP150_H2H_2025_2026_THROUGH_2026_11_15.csv` az ezt követően játszott meccseket **nem** tartalmazhatja. Ezért külön, match-level feljegyeztük az ATP Finals **2026-11-16 és 21 között** befejezett 12 férfi egyes meccsét. Két egymástól függetlenül ellenőrzött eredményforrás:

- [Nitto ATP Finals hivatalos dátumozott eredmények](https://www.nittoatpfinals.com/en/scores-centre/results/)
- [TennisDB ATP Finals 2026 eseménynapló](https://tennis-db.com/tournaments/529/atp-finals?season=2026&view=log)

A 2026-11-22-i döntő **nincs** benne ebben az adatcsomagban; időben a nap végleges eredménye előtt is készülhetett a kutatás. A H2H-aggregált táblát tilos a 12 friss mérkőzéssel idempotens event-ID és eredeti 2025/26 match-szintű alap nélkül egyszerűen hozzáadással felülírni, mert duplikáció és visszateszt-információszivárgás lehet.

Mérkőzésfájl `match_date` mezője a napot jelöli, nem az adott pont vagy meccs vége UTC időbélyegét. **Nincs** tényleges pontonkénti event_time ebben az adatban.

## 4 vitás ATP-főtábla rekord – újranyitás nélkül, bizonyíték szerint

2026-11-22-i TennisDB játékosoldalak alapján:
- **Otto Virtanen:** 2026 ATP főtábla `1–6`; selejtező `10–9`. Korábbi PR #13 `1–5` pillanatképe eltér; helyes `as_of` és meccsszintű reconciliation kell. [Forrás](https://tennis-db.com/players/224/otto-virtanen)
- **Clément Chidekh:** ATP főtábla `2–1` (2026 European Open), selejtező `4–4`. [Forrás](https://tennis-db.com/players/352/clement-chidekh)
- **Max Alcalá Gurri:** 2026-os ATP főtáblás befejezett meccs nincs a szolgáltató rekordjában; két selejtező vereség (`0–2`). A master főtáblás statisztikai rekordot **nem** lehet másodrendű selejtezőeredményre cserélni, sem a hiányt 0%-os teljesítménynek venni. [Forrás](https://tennis-db.com/players/485/max-alcala-gurri)
- **Nikolas Sánchez Izquierdo:** 2026-os ATP főtáblás meccs nincs a szolgáltató rekordjában; `1–3` selejtező (Umag 1–1, Wimbledon 0–1, US Open 0–1). A forrás ranglistapillanatképe eltérhet a projekt `2026-11-16` ranglista-listájától, ezért ID és dátum szerint kell keresztazonosítani. [Forrás](https://tennis-db.com/players/405/nikolas-sanchez-izquierdo)

**Kritikus forrásszabály:** TennisDB maga jelzi, hogy főtáblás eredményszámlálója **walkovereket is beleszámolhat** a W–L-be, míg az Elo/ütésstatisztikák ezeket nem feltétlenül. [TennisDB adatminőség](https://tennis-db.com/data-quality). Az új táblák `research_only` státuszúak; nem azonosak a már korábban a masterbe vett, név+ranglistapont alapján egyeztetett 146 rekorddal.

## Felhasználható az appban?

**Igen, mint dátumozott és külön jelölt kutatási bemenet.** A 26 TDI-játékos nem egyenlő 26 teljesen, saját módszerrel függetlenül validált technikai/mentális profillal; a hiányzó 124 játékosra nincs hamis becslés. Az ATP/GS főtábla profilja és az egyes top150 találkozók automatikus frissítése **külön adatfeldolgozás**, nem végtelen podcast-keresés.

**Változatlan projektirány:** saját privát alkalmazás, ATP+Grand Slam férfi egyes főtábla, aktuális+előző szezon (2026/25), külön A/B játékos, és csak validált/meghatározott bizonytalanságú jelzések.

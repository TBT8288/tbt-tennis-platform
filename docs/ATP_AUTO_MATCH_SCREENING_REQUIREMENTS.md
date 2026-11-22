# ATP Intelligence – automatikus meccs-előszűrés, korai jelzés és felhasználói workflow
**Forrás:** eredeti `ATP(1).txt` 578–582, 614–749, 846–855, 856–885. sor; projekt fő dokumentum 1–5. szakasz.
**Állapot:** követelményspecifikáció / tervezett funkció, **nem kész algoritmus vagy bevált 70–80%-os automatizálás**.

## Cél
A privát, mobilon megnyitható app **az összes releváns férfi ATP Tour/Grand Slam főtáblás meccset** figyeli, és csak azokat emeli ki, ahol adatminőséggel alátámasztott, meccs előtt vagy játék közben kialakult változás/matchup-eltérés látszik. A felhasználónak **nem kell minden meccset élőben néznie**; a videó másodlagos, opcionális validáció.

## Pipeline
1. **Discover:** aktuális naptár, ATP 250/500/Masters 1000/ATP Finals/Grand Slam, férfi egyes főtábla; a két játékos rankjától függetlenül minden releváns meccs az eseményszűrőbe kerül.
2. **Resolve:** `match_id`, `player_id`, `scheduled_start`, `event_time`, `ingested_at`, adatforrás, sportág, borítás, versenyszint. Top150 játékosok tartós profilból, azon kívül ideiglenes kontextusból.
3. **Pre-match enrich:** [10 tényezős vizsgálat](ATP_PREMATCH_INTELLIGENCE_10_TENYEZO.md) mindkét félre; 2025–2026 időablak, ellenfélerő, naptár, borítás, terhelés, adatminőség.
4. **Data quality gate:** `completeness`, `latency`, `missing_fields`, visszamenőleges korrekció és forráseltérés. Ha nincs ponttörténet, csak megfelelően korlátozott game-/set-szintű kijelentés. NINCS kitalált videós vagy mentális adat.
5. **B0 baseline:** meccsállásból és validált szervapont-p-ből számított matematikai alap, külön eredményidőponttal. Ne tekintsük a score-sorozatot automatikusan pszichológiai momentumnak.
6. **B1/B2 dynamism:** a szerva/fogadás trendek mindkét játékosra külön; online változáspont, bizonytalanság, elegendő mintaszám. A és B **egyidejűleg javulhat vagy romolhat**.
7. **Coach evidence:** amennyiben rendelkezésre állnak hiteles pont- és videóadatok, 0–4 ütés, szerva+1, fogadás+1, pályapozíció és mozgás; ha nincs ilyen adat: `UNOBSERVABLE`, nem „megfigyelt hiba”.
8. **Alert gate:** kiváltó jel: időben rögzített, játékos-saját baseline-tól lényeges elmozdulás vagy friss körülményváltozás. Külön címke `WATCH` / `SHIFT_CANDIDATE` / `MODEL_PREDICTION` / `NO_SIGNAL` / `INSUFFICIENT_DATA`. Az első három **nem** jelent bizonyított profitot vagy személyiségdiagnózist.
9. **Notify:** mobil kijelző/push csak küszöb feletti, forrásokkal és időbélyeggel alátámasztott eseménynél, frekvencialimit / ismétlődés-összevonás. Később opcionális Discord.
10. **Validate:** előrejelzés zárolása az esemény előtt; kimenet után Brier/log-loss, jelzés előnye a tényleges break előtt, fals riasztás, adatlatency és kalibráció. A felhasználói kontrollpanelből ellenőrizhető, miért jött a jelzés.

## Két külön használati mód
**Adat-only:** API, állás/pont, meccstörténet, statisztika, naptár. Használható videó nélkül; mozgás/testbeszéd/biomechanika NEM megfigyelhető. **Videóval megerősített:** csak ha jogszerűen elérhető közvetítés vagy rögzített megfigyelés, és külön forrás-időbélyeggel hozzá van rendelve.

## Riasztás minimális formája
`match_id` | `time_utc` | `player_A_shift` | `player_B_shift` | `signal_type` | `estimated_change` | `prediction_horizon` | `source_fields` | `confidence` | `missing_fields` | `false_positive_risk` | `watched_or_alerted`.

## Elfogadási kritériumok
- Nem figyelmen kívül hagyni releváns ATP-főtáblás meccset csak azért, mert az egyik játékos rangja >150.
- Minden megjelenített állításnak van forrása és megelőző időbélyege; utólag nem hazudhatunk korai jelzést.
- Nincs automatikus „mental collapse” címke meccsállásból vagy egy kettőshibából.
- Egy meccset legfeljebb egyszer jelez ugyanarra az eseményre/küszöbre, hacsak tényleges új bizonyíték nem érkezik.
- A 70–80% elemzés-automatizálási arány **régi tervezési cél**, nem mért KPI. Később feladatidő- és felhasználói teszttel ellenőrizendő.
- A meccsnézés és a használhatóság a privát felhasználó számára telefonon legyen kényelmes; nem feltételez 24/7 kézi monitorozást.

# ATP Intelligence – virtuális előrejelzési és oddsérték-elemző protokoll
**Forrás:** `ATP(1).txt` 148–197, 197–237, 267–291, 844. sor.
**Hatókör:** privát, **valódi pénz nélküli kutatási napló**, nem automatikus sportfogadás és nem garantált profit.

## Célhorizontok
- H1: következő pont, egyértelmű szerválóval és event_id-val.
- H2: következő game.
- H3: következő **2–3 game** kimenetele, előre kimondva pontosan, mi számít sikernek (pl. A legalább 2-t nyer a következő háromból).
- H4a: következő szett, H4b: mérkőzés győztese.
- Külön cél: **következő fogadójátékban break** és a break előtti jelzés előnye (nem összevonható pusztán a game-célokkal).

## Előre rögzítendő eseményrekord
`prediction_id`, `match_id`, `event_id`, `target_definition`, `player_a`, `player_b`, `score_at_prediction`, `source_timestamp`, `observed_at`, `prediction_locked_at`, `model_version`, `p`, `confidence`, `data_missingness`, `odds_decimal` (opcionális), `odds_observed_at`, `market_name`, `market_status`, `simulated_stake` (opcionális), `settled_at`, `outcome`, `settlement_status`. **Nem szabad** utólag felülírni az első becslést.

## Számítások
- Tisztán decimális odds `o>1`; nettó break-even `1/o`. A bukmékeri teljes piac marginját csak **valamennyi releváns kimenetel egyidejű, hozzáférhető oddsából** lehet korrigálni.
- `EV = p × o − 1` = egységnyi elméleti, *bruttó* tétre jutó várható eredmény. Ez **nem** valós kereskedhető előny bizonyítéka.
- Példa: `p=0.32`, `o=4.00` ⇒ `EV=0.28` (28% elméleti), **ha** p valóban kalibrált. Ugyanezen odds 25%-os implied valószínűség. Nem állítható, hogy erre biztos nyereség építhető.
- Szimulált tét esetén: nyereség `stake × (o−1)`, veszteség `−stake`, push/cancel = `0` a megfelelő fogadási szabály szerint; csak ténylegesen elérhető, nem késleltetett oddsokkal végzett hipotetikus napló értékelhető.
- Piaci vizsgálat: margin, odds/státusz frissesség, provider delay, felfüggesztés, lehetséges settlement-eltérés, a modell kalibrációja és bizonytalanság. Ezek hiányakor `NO VALUE CLAIM`.

## Tesztprotokoll
1. Minden jelzés időben megelőzi a cél-eseményt és a kiválasztott oddsot hozzáférhetőnek rögzítjük.
2. A megérzésből becsült `p_blind`, a statisztikai `p_model` és a kombinált `p_combined` külön naplózott (hiányzó érték hiányzik, nem 0).
3. Előre definiált, szimulált tétmechanizmus és `NO BET/NO SIGNAL` állapot.
4. Kalibráció, Brier/log-loss, fals riasztás, ROI kizárólag a szimulált sorozaton, időrendben elkülönített adatokon.
5. A modell nem tanulhat a későbbi mérkőzések eredményéből egy korábbi jóslat készítésekor.

## Személyes használat és jogi korlát
A projekt jelenlegi célja privát, nem fizetős alkalmazás; a korábbi SaaS-opció történeti. Fogadóirodai limit kijátszására és automatikus tételhelyezésre nem építünk. **A kockázat és a becslési hiba megmarad**, még akkor is, ha egy adott számítás pozitív EV-t mutat.

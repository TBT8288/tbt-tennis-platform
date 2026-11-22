# ATP Intelligence – Blind Prediction és 50 próbás tesztprotokoll
**Eredeti beszélgetés:** `ATP(1).txt` 130–147, 197–237., 281–291. sor. Állapot: részletesen specifikált, de **nincs 50 valódi elvégzett teszt**.

## Blind = első, nem módosítható becslés
1. Válassz ATP férfi egyes, jövőbeli eseménnyel rendelkező mérkőzést és pontos célváltozót (pl. „A megnyeri a következő game-et”).
2. A **blind** fázis előtt ne nézd meg a mérkőzés részletes statisztikáit, oddsait, korábbi modellkimenetét. Külön jelöld, ha már tudsz róluk valamit: így nem valódi vak teszt.
3. Rövid meccsmegfigyelés után, a cél-esemény előtt rögzítsd az első intuíciót és valószínűséget (0 és 1 között vagy 0–100%), az észlelt jeleket és a döntési időpontot.
4. A rekordot **zárold**. A külön `model_probability` mezőt csak olyan algoritmus töltheti, amelynek bemenetei legkésőbb a predikció időpontjában megvoltak (no-lookahead).
5. A harmadik `combined_probability` értéket előre dokumentált kombinációval számítsd, nem utólag választott optimummal.
6. Esemény végén csak `actual_outcome`, `settled_at`, `notes_after` és mérőszám frissülhet; a blind/model/combined becslés marad eredeti.
7. Mérjük mindhárom módszert **azonos eseményekre**, külön célhorizontokként; ha egy csatorna hiányzik, jelöld hiányként, ne találj ki értéket.

## Kísérlet és kiértékelés
- Előre definiált esemény: `target_event` és `horizon` egyértelmű, ne ugyanazon esemény különböző definícióját keverjük.
- Százalékos becslés 0–100 (az eredeti tréning 50–100%-os nyertesbizalom ötletet adott, de a modellben az A játékos esélye lehet 0–100%).
- Brier: `(p-y)^2`, ahol `p∈[0,1]`, `y∈{0,1}`. Az átlagot **csak értékelhető eseteken** számoljuk.
- Hit rate: 0,5 feletti p a kiválasztott esemény igenje; az 50%-os és elutasított esetekre külön szabály.
- Külön jelentés: `Brier_blind`, `Brier_model`, `Brier_combined`, lefedettség, hiány, kalibráció, szegmensek (borítás, tét, mintaméret). Egyetlen jól sikerült 50-es sorozatból **nem** állítunk stabil sportfogadási előnyt.
- Ellenőrizhető lánc: `observed_at` ≤ `prediction_locked_at` < `event_start` ≤ `settled_at`, továbbá `source_timestamp` ≤ `prediction_locked_at` minden felhasznált adatra.
- Ha valaki nem nézi élőben a játékot, `observation_mode=data_only`; ilyenkor az intuíció nélküli becslést nem nevezzük visszamenőleg blind megfigyelésnek.

## Fájl és használat
- [50 üres, sorszámozott próbafelvétel](../research/templates/blind_prediction_50_ures_sor.csv)
- Üres mező = nincs adat, soha nem 0 és nem bukás.
- **Minden sor csak sablon**. A fájl nem tartalmaz fiktív mérkőzést, oddsot vagy jóslatot.
- A GitHub jelenleg nyilvános; **személyes tétinformációt, kulcsot, jelszót, nem publikus e-mailt nem mentünk**.
- A későbbi appnak ezeket a rekordokat valóban időbélyegzetten, írásvédett előrejelzési naplóban kell tárolnia. A CSV **önmagában nem manipulációbiztos**.

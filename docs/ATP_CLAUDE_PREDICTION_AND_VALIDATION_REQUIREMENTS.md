# ATP – Claude régi kutatásokból átvett kimeneti és validációs követelmények

**Forrás:** [Claude/N​otion 10](https://app.notion.com/p/420f603f0d2e819e90e7d0e988039fe5), 2026-10-01-i eredeti projektösszefoglaló; jelenlegi 2026-11-22-es feladat: privát ATP alkalmazás, nem SaaS.
**Kapcsolódó:** [virtuális EV](ATP_VIRTUAL_PREDICTION_AND_EV.md), [Blind Prediction 50 próba](ATP_BLIND_PREDICTION_50_PROTOCOL.md), [ATP időablak](TEMPORAL_RELEVANCE_POLICY.md).

## 1. Kimenetek, amiket a Claude korábban megkövetelt
- **Match Winner**: A/B nyerési esély (%), kifejezetten `prob_a` és `prob_b = 1 - prob_a` azonos meccs/horizont cutoffnál.
- **Total games**: például `Over/Under 21.5 games` – pontosabb eloszlás kell a teljes meccs játékainak számáról, nem elég `match_win_prob`.
- **Game handicap H1/H2**: kétoldali handicap külön célkimenettel és hendikepvonallal; a sorozat `H1/H2` jelentése forrás szerint handicap oldal (külön az új blind kísérlet `H1` = next point, `H2` = next game!); az elnevezés két jelentését a modellben NEM szabad keverni.
- **Szettállás eloszlás** (best-of-three): A 2:0, A 2:1, B 2:1, B 2:0; összegük 100% a megfelelő mérkőzésformátumnál. Best-of-five (Grand Slam férfi) **nem** fedhető le ezzel a négy végállással.
- **Total sets**: `Over/Under 2.5` csak best-of-three esetén értelmes ugyanígy; best-of-five megfelelő külön határokat igényel.
- **A modell döntő érvei**: konkrét borítás, forma ellenfélerővel korrigálva, stílus-matchelt pár, terhelés, pontvédelem, nyilvános motiváció, H2H csak releváns két szezon, opcionális időbélyeges oddsmozgás.

**Üres/stale input esetén:** `UNAVAILABLE/INSUFFICIENT_DATA`, nem kitalált nyerési százalék. Az odds nem a sporteredményből visszafejtett érték.

## 2. A korábbi Claude-projekt figyelmeztetései
- A válaszok korábban túl gyakran választották a 2:0 kimenetet; ezért a szetteloszlást **külön kalibráljuk**, ne a match winnerből egyszerűsítve következtessük.
- A Gemini riportokból a régi kutatás szerint hiányzott O/U21.5, handicap, O/U2.5 és teljes szettállás eloszlás; **jelentési specifikációt** készítünk, nem állítjuk hogy az aktuális Gemini felület ugyanígy működik.
- Oddsmozgás használata csak teljes forrás/időbélyeg mellett; anélkül nem állítható „smart money”.
- A `tbt/markets.py` régi poll-ciklusokból számolt game→set→match újraárazási logikája **történeti**, a mostani repóban az adott fájl nem található. Az aktuális B0 baseline nem egyenértékű egy teljes eloszlásmotorral.

## 3. Modellvalidáció: mikor mondhatjuk jobbnak?
A Claude régi projektje a Stanfordnak tulajdonított 71,7%-os ranglistafavorit példával hangsúlyozta: **a találati arány önmagában kevés**. Az eredeti 71,7% konkrét forrását még nem ellenőriztük, ezért nem aktuális referencia-küszöb.

**G0 első szimulált backtest – tervezési mérföldkő:**
- 100–300 ATP-meccs **első, exploratív minta** a régi projekttervben; egy ilyen minta nem garantál bizonyított stabil piaci előnyt.
- `Brier` és `log loss`, `calibration`, `coverage`, `sample_size` meccs és horziont szerint; piaci záróoddsból számolt implied probability margin/késés időponttal.
- **Csak a meccs előtt ténylegesen elérhető** statisztika és odds; minősített outcome, no-lookahead.
- Időrendben elválasztott tanító/teszt adatok (2025–2026 szabály megtartása), ellenfélerő, borítás, torna szint és küszöb validálva.
- A piacnál jobb `Brier` a régi projekt **javasolt továbbhaladási feltétele** volt, de még nem elért eredmény.
- G1 személyes tesztüzem régi célja **4 hét dokumentált működés**, „degraded mode”, saját riasztások, adatminőség. Ez külön *későbbi mérföldkő*, nincs most készen.
- Jelenlegi aktuális hatókör: **privát app**; a Claude korábbi G2 nyilvános béta/G3 fizetős/G4 osztrák EPU **nem kerül a jelenlegi ütemtervbe**.

## 4. Ajánlott, tesztelhető predikciós kimeneti séma
```text
match_id; data_timestamp; prediction_locked_at; model_version; player_a; player_b;
best_of; surface; serve_return_sample; opponent_strength_window;
match_win_a; match_win_b;
exact_set_score_distribution; total_games_line; total_games_over; total_games_under;
handicap_line; handicap_a; handicap_b;
total_sets_line; total_sets_over; total_sets_under;
availability_status; missing_fields; calibration_version; evidence_source_ids
```

**Sématesztek**, amelyekre valódi kódot csak ellenőrzött feed esetén írjunk:
1. `0 <= p <= 1` minden valószínűségi mezőn.
2. `p_A + p_B = 1` a kétkimenetelű, settlement-szabályozott piacon; visszalépés/retirement szabály külön.
3. `best_of=3` 4 végkimenetele adjon 1-et; `best_of=5` kimenetszám nem azonos.
4. Kétfél-piac oddsai időbélyegesek, margin és suspended státusz kezelendő.
5. `NO_PREDICTION` hiányos feed esetén, nincsenek hamis fill értékek.
6. Ugyanazon pont/szett/horizont predikció a létrejötte után nem írható felül.

## 5. Végső termékmegkülönböztetés
A korábbi 2026.10-i Claude-teszt szerint minden meccshez részletes chat-válasz kellett. A jelenlegi ATP-termék ettől eltérően **automatikus meccselőszűrést** és csak releváns riasztást akar; amikor részletes riportot nyitunk, a fenti kimenetek csak akkor jelennek meg, ha a szükséges adat és kalibrált modell valóban létezik.

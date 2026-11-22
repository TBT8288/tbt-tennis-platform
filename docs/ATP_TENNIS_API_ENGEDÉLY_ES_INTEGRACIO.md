# ATP Intelligence – Tennis API felhasználási engedély és technikai bekötés két külön státusz
**Felhasználói döntés megerősítve: 2026-11-22.** Ezt a szakaszt nem kezeljük újra megnyitott engedélyezési kérdésként.

## 1. Felhasználási engedély: EGYEZTETETT, LEZÁRT
A felhasználó **korábban ellenőrizte és ismételten megerősítette**, hogy a Tennis API-val megbeszélt felhasználási engedély terjedelme megfelelő. A régi beszélgetés (`ATP(1).txt`, 889–935. sor) szerint:
- a Tennis API adatainak felhasználása saját alkalmazásban,
- azok kiegészítése saját AI-generált elemzéssel,
- és az egykori, akár fizetős havi előfizetéses SaaS-konstrukció
**szerepelt az előzetesen egyeztetett kérdésben**, amelyre a szolgáltatótól „Yes.” válasz érkezett. A felhasználó **2026. november 22-én kifejezetten megerősítette**, hogy az engedély pontos terjedelmét már ellenőrizte és ezt nem kérdőjelezzük meg újra.

**Projektben elfogadott állapot: `USER_CONFIRMED_PERMISSION_SCOPE_VERIFIED`.** Az engedély alapjainak újbóli felkutatása nem a következő fejlesztési fázis előfeltétele. A mostani termék **privát, nem SaaS**; a régi SaaS-lehetőség nem határoz meg jelenlegi monetizációs feladatot.

## 2. Technikai integráció: KÜLÖN, MÉG NEM IGAZOLTAN KÉSZ
A repository meglévő `tennis_api_client.py` fájlja az előző audit szerint Sportscore **RapidAPI** végpontot használ. A fájlnév **nem bizonyítja**, hogy a megállapodás tárgyát képező Tennis API már valóban a backendhez kapcsolódik.

Következő technikai feladatok, amelyek NEM jelentik az engedély újratárgyalását:
1. A már kiválasztott Tennis API fiók/dokumentáció aktuális végpontjainak és hitelesítésének egyeztetése **biztonságosan**, kulcs megosztása nélkül.
2. Live meccs, meccs ID, player ID, szerváló, ponttörténet, mérkőzés-statisztikák, H2H, odds mezők és időbélyegek **tényleges** API-lefedettségi auditja (a csomag elérhetősége elkülönül a licencált használhatóságtól).
3. Mintákból sématábla, adatritmus/késés, limit és fallback.
4. Klienskód megírása és teszt, anélkül hogy a jelenlegi Sportscore-klienst megsemmisítenénk.
5. `source_name`, `source_timestamp`, `data_completeness`, `license_scope_confirmed`, `integration_test_passed` **külön** státuszt kapnak.

## 3. Megőrzött határok
- A felhasználói **engedély-megerősítést elfogadjuk**, nem állítjuk újra, hogy tisztázatlan a korábban egyeztetett engedély terjedelme.
- Az eredeti levelezés teljes privát szövegét nem másoljuk a jelenleg nyilvános GitHub-repóba.
- Külön kezeljük az API-csomag kvótáját, a sémát és a működő adatkapcsolatot: ezek még implementációs feladatok.
- Nem kérünk API-kulcsot a nyilvános beszélgetésben, és nem commitoljuk.
- Az időben régi, esetleg SaaS-ra vonatkozó egyeztetés **nem** jelenti azt, hogy a magánalkalmazásból most fizetős platformot építünk.

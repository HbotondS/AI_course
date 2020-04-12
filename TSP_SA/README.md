# Utazó ügynök problémaja, szimulált hűtéssel
## A feladat
Adva van n város, illetve a város koordinátái, keressük a legolcsóbb utat egy adott városból indulva, amely minden várost pontosan egyszer érint.
## Megoldás
1. Inicializáljuk a szimulált hűtés állandóit: kezdeti és minimum hőmérséklet.
2. Megállási feltétel ellenörzése
3. Aktuális út hossz kiszámolása
4. Kigeneráljuk a következő útat
5. Különbségét számolunk a két táv között
6. Ha az új út rövidebb mint az aktuális elfogadjuk, másképp csak a egy bizonyos valószínűséggel fogadjuk el, aminek az értéke a hőmérséklet csökkenésével egyre kisebb lesz
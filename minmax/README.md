# Gomoku
## Játék lényege
Egy 15x15 vagy 19x19 táblán kell köveket letenni, addig amíg egy sorban, oszlopban vagy átlósan lesz egymás mellett 5 darab.

## Leírás
Ennek a játéknak a konzolos verzióját csináltuk meg. Konzolra írja ki minden egyes lépés után a tábla aktuális állapotát.
A táblán _-2_ jelöli az AI helyzetét és _2_ a játékos helyzetét.

## Futtatás
A progtam futtatásához Python 3.6 szükséges.
Meghívás: `python Gomoku.py [argv]`
A program jelenlegi állapotában egy argumentumot képes fogadni:
    * mélység: minmax rekurzív hívások milyen mélységig menjenek

## Felmerült problémák
A program futási idő jelentett gondot, 15x15-ös tábla eseten nagyon sokáig fut a program.
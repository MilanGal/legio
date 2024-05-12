Ez egy projekt az Eurovíziós dalfesztiválról.

Néhány információ:
Minden évben megrendezik 1956-tól a rendezvényt, ahol minden jogosult ország egy "saját" dallal indul. Az elődöntőket követően a döntőben a legtöbb pontot kapott dal/ország nyer.
A pontozási rendszerben (12, 10, 8, 7, 6, 5, 4, 3, 2, 1) pontot osztanak ki az országok másoknak.
A pontozási rendszer 2016-ban megváltozott, a pontokat az összesített helyett külön jury és public -ra vették szét, így azóta kétszer annyi pontot osztanak ki.

A adatelemzésben az 1956-os és 2020-as pontokat nem vettem bele, mert előbbi esetén nem volt publikus a szavazás, utóbbinál pedig nem rendezték meg.

Követelmények:
Python 3.11.7-ben íródtak a fájlok.
Pandas és Matplotlib könyvtárak szükségesek.

Fájlok:
  main.py
  first_run.py
  data_table.csv
  voting.txt

A voting.txt tartalmazza a pontozást "nyers" formában, ezt a first_run.py alakítja át a data_table-é, amit a main.py használ.
Megj. Így nem kell minden futtatásnál újra rendezni a táblázatot.

Az adatelemzés tartalmaz néhány táblázatot pontozásról, illetve Magyarország 'helyzetét' más országok számára egy plot mutat meg.

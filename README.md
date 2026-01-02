Disaster Recovery & Business Continuity – Demo Project

Ovaj repozitorij sadrži praktičnu implementaciju osnovnih koncepata Disaster Recovery (DR) i Business Continuity (BC) razvijenu u sklopu kolegija Sigurnost informacijskih sustava. Projekt demonstrira kako se uz korištenje virtualne infrastrukture i jednostavne automatizacije mogu osigurati sigurnosno kopiranje podataka, nadzor rada sustava i oporavak nakon incidenta.

Implementacija se temelji na dvije virtualne mašine (produkcijski i backup poslužitelj) te Python skriptama koje automatiziraju ključne procese vezane uz kontinuitet rada sustava.

Struktura repozitorija

Repozitorij sadrži sljedeće datoteke:
- backup.py
- restore.py
- monitoring.py
- index.html

Opis datoteka

backup.py

Python skripta zadužena za automatizirano sigurnosno kopiranje podataka s produkcijskog poslužitelja.
Skripta:
	•	arhivira sadržaj web direktorija
	•	dodjeljuje vremensku oznaku sigurnosnoj kopiji
	•	prenosi arhivu na udaljeni backup poslužitelj putem sigurne SSH komunikacije
	•	uklanja lokalnu kopiju nakon uspješnog prijenosa

Skripta je namijenjena izvođenju u pravilnim vremenskim intervalima (npr. korištenjem cron mehanizma), čime se ostvaruje nizak Recovery Point Objective (RPO).


monitoring.py

Python skripta za nadzor rada web poslužitelja na produkcijskom sustavu.
Skripta periodički provjerava stanje ključnog servisa i:
	•	signalizira normalno stanje rada kada je servis aktivan
	•	generira upozorenje u slučaju prekida rada servisa

Implementirani nadzor omogućuje pravovremeno otkrivanje incidenta i predstavlja temelj za brzo pokretanje postupaka oporavka.


restore.py

Python skripta koja omogućuje oporavak sustava nakon incidenta korištenjem prethodno izrađenih sigurnosnih kopija.
Skripta:
	•	preuzima odabranu sigurnosnu kopiju s backup poslužitelja
	•	uklanja kompromitirane ili oštećene podatke
	•	vraća podatke u stanje koje odgovara trenutku izrade sigurnosne kopije

Postupak oporavka pokreće se ručno, čime se zadržava kontrola nad procesom vraćanja sustava.


index.html

Jednostavna HTML stranica koja se koristi kao demonstracijski sadržaj web poslužitelja.
Stranica služi za:
	•	provjeru dostupnosti web servisa
	•	vizualnu potvrdu prekida rada i uspješnog oporavka sustava tijekom simulacija incidenta


Način korištenja (visoka razina)

Projekt je zamišljen za izvođenje u virtualnom okruženju koje se sastoji od:
	•	produkcijskog poslužitelja (web server + Python skripte)
	•	backup poslužitelja (pohrana sigurnosnih kopija)

Za automatizaciju sigurnosnog kopiranja preporučuje se korištenje Linux mehanizma za zakazivanje zadataka (cron). Komunikacija između poslužitelja ostvaruje se putem SSH protokola s autentifikacijom temeljenom na kriptografskim ključevima.

Detaljniji opis implementacije, konfiguracije virtualnih mašina i testiranja sustava nalazi se u pripadajućoj projektnoj dokumentaciji.


Napomena

Ovaj projekt ima edukativnu i demonstracijsku svrhu. Implementacija prikazuje osnovne principe Disaster Recovery i Business Continuity te služi kao temelj za razumijevanje procesa sigurnosnog kopiranja, nadzora i oporavka sustava u kontroliranom okruženju.

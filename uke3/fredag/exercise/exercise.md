# Oppgave i forelesning fredag 16.01

## Del 1 - klasser, objekter, referanser og main-metode

- Opprett fila main.py  
  Her skal du ha if-name-main-metoden din, så herfra kjører du programmet med å kjøre `python main.py` i terminalen.
- Lag klassene Library, Book, og Author med konstruktører.  
  Et Library skal ha Books  
  En Book skal ha en Author  
  En Book hører til på et Library  
  Sett opp relevante relasjoner, og
  legg til felter og metoder som du trenger i klassene.

- I main.py, opprett instanser av Author, Book og Library  
   med fornuftige relasjoner til hverandre.
  Lag for eksempel 1 library, 2 authors, og 3 books.  
   Bruk print() til å verifisere at programmet fungerer som det skal når det kjører.

## Del 2 - designvalg og arv

- Lag klassen Customer  
   En Customer kan låne Books og returnere Books de har lånt.
  En Book kan bare lånes av én customer av gangen. Prøver noen å låne en bok som allerede er utlånt, skal det skrives ut en fornufutg feilmelding i terminalen med print().

- Lånetiden for Books kan enten være av typen hurtiglån (7 dager lånetid), standardlån (28 dager lånetid), eller ikke til utlån (kan ikke lånes, bare leses på biblioteket).  
   Hvordan vil du implementere dette på en god måte? Implementer denne funksjonaliten på to ulike måter: MED og UTEN å bruke arv.

## Del 3 - Encapsulation, type hints og docstrings

- Gå gjennom all koden du har til nå. Bør du legge på noen ekstra valideringssteg noen steder i metodene som finnes? Hvilke metoder skal være interne, og hvilke skal være eksterne? Hva med tilgang til å hente/skrive verdier til felter? Bør du implementere @property og @property_name.setter for noen av feltene?

- Installer mypy med pip.  
   Kjør mypy --strict på koden din.  
   Se om du klarer å få sjekken til å passere med å legge inn type hints.

  Eksempel:
  Hvis terminalen er navigert til mappa med filer jeg jobber på, feks /fredag, kjører jeg:
  `mypy --strict .` for å sjekke alle filene i mappa, eller `mypy --strict main.py` for å kun sjekke main.py fila.

- Installer black og pylint med pip.

Kjør `black` på koden din for å formattere den, og kjør deretter `pylint`. Se om du klarer å få pylint-sjekken til å passere alle docstrings-sjekker.

## Bonus:

- Implementer følgende funksjonalitet: Et bibliotek har et budsjett (budget) for bokinnkjøp, og ei bok har en pris. En author har en royalties-saldo, og får 50% av bokprisen i royalties hver gang et bibliotek kjøper inn ei bok de har skrevet. Et bibliotek kan ikke bruke mer penger enn de har i budsjettet sitt. Her skal du tenke på encapsulation med alt som kommer til penger. Hvilke felter og metoder bør være interne, og hvilke bør være public? Hvilke sjekker må vi gjøre i metodene våre?

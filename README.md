# Finanz Tracker

## Kurzbeschreibung
In diesem Finanztracker kann man seine Ausgaben eintragen, Ausgabelimits erstellen, Sparziele anlegen und schauen, ob man diese einhält.

## Features
- Eingegebene Ausgaben werden in json-file gespeichert -> Übersicht in Tabelle
- Erstelle Ausgabelimits - Abgleich mit ausgaben.json
- Eingegebene Sparbeträge in json-file gespeichert -> Übersicht in Tabelle
- Sparziele - Abgleich mit gespart.json
- letztes Element aus Tabellen löschbar
- txt dateien dienen als kleiner Speicher - speichern letzte Informationen

## Setup
- Repository klonen
- im Terminal in den Ordner finance_tracker navigieren
- gui.py starten

## Nutzung
- in jedem Tab sind Eingabefelder
- diese füllen und Eingabe nach jedem Feld bestätigen mit jeweiligem Button
- Preise immer ohne Geldeinheit speichern
- Datums in genanntem Format (z.B. YYYYMMDD)
- Um Eintrag zu speichern: start-button

## Struktur (optional)
- gui.py – Quellcode
- json-files – Perma-Speicher von Tabellen-Einträgen
- txt-files - Überschreibare Speicher von jeweils einem Wort

## Status
- PoC

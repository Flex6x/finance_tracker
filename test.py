import json
import os

produkt= str(input("Produkt:    "))
preis= int(input("Preis:    "))
datum= int(input("Datum:    "))

neu = {
    "produkt": produkt,
    "Preis": preis,
    "Datum": datum
}

#with open ("ausgaben.json", "w", encoding="utf-8") as datei:
    #json.dump(daten,datei,indent=4,ensure_ascii=False)

if os.path.exists("ausgaben.json"):
    # Datei lesen
    with open("ausgaben.json", "r", encoding="utf-8") as datei:
        try:
            daten = json.load(datei)  # bestehendes Array laden
        except json.JSONDecodeError:
            daten = []  # falls Datei leer oder ungültig
else:
    daten = []  # neue Datei -> leeres Array

# 2. Neuen Eintrag anhängen
daten.append(neu)

# 3. Alles wieder zurückschreiben
with open("ausgaben.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, indent=4, ensure_ascii=False)
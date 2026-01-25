import json
import os

produkt= str(input("Produkt:    "))
preis= int(input("Preis:    "))
datum= int(input("Datum:    "))

neu = {
    "produkt": produkt,
    "preis": preis,
    "datum": datum
}

# Prüfung, ob .json und array existiert

if os.path.exists("ausgaben.json"):
    with open("ausgaben.json", "r", encoding="utf-8") as datei:
        try:
            daten = json.load(datei)
            # falls ein einzelnes Objekt drinsteht, in Liste umwandeln
            if isinstance(daten, dict):
                daten = [daten]
        except json.JSONDecodeError:
            daten = []
else:
    daten = []

daten.append(neu) # Eintrag wird der zu "daten hinzugefügt"

# Anhang wird ausgeführt
with open("ausgaben.json", "w", encoding="utf-8") as datei:
    json.dump(daten, datei, indent=4, ensure_ascii=False)
import json
import os

produkt= str(input("Produkt:    "))
preis= int(input("Preis:    "))
datum= int(input("Datum:    "))

daten = {
    "produkt": produkt,
    "Preis": preis,
    "Datum": datum
}

with open ("ausgaben.json", "w", encoding="utf-8") as datei:
    json.dump(daten,datei,indent=4,ensure_ascii=False)


import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

print("Daten\n")

for eintrag in ausgaben:
    print(eintrag["produkt"], eintrag["Preis"], eintrag["Datum"])
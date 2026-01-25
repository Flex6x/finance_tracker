import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

print("Daten\n")

for eintrag in ausgaben:
    print("Produkt: ", eintrag["produkt"], "/ Preis: ",eintrag["Preis"], "/ Datum: ",eintrag["Datum"])
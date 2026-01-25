import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

produkte=[]
preis=[]
datum=[]

print("Daten\n")

for eintrag in ausgaben:
    produkte.append(eintrag["produkt"])
    preis.append(eintrag["preis"])
    datum.append(eintrag["datum"])

print(produkte)
print(preis)
print(datum)
import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

preise=[]
datums=[]

for eintrag in ausgaben:
    preise.append(eintrag["preis"])
    datums.append(eintrag["datum"]) 

preis_monat=[] # Liste für alle Preise von Ausgaben in gewähltem Monat
monat_ausgewählt = "01" # Monat auswählen

# Monat wird ausgelesen, falls Monat mit gewähltem M. übereinstimmt wird der jeweilige Preis zur Liste hinzugefügt
for i in range (len(preise)):
    z4 = str(datums[i])[4]
    z5 = str(datums[i])[5]
    z=z4+z5
    if z == monat_ausgewählt:
        preis_monat.append(preise[i])

# Berechnung von gesamtem Preis in Monat
ausgaben_monat = 0

for i in range (len(preis_monat)):
    ausgaben_monat += preis_monat[i]
print(ausgaben_monat)
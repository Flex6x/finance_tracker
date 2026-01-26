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
jahr_ausgewählt = "2026"

# Monat wird ausgelesen, falls Monat mit gewähltem M. übereinstimmt wird der jeweilige Preis zur Liste hinzugefügt
for i in range (len(preise)):
    z0 = str(datums[i])[0]
    z1 = str(datums[i])[1]
    z2 = str(datums[i])[2]
    z3 = str(datums[i])[3]
    zy = z0+z1+z2+z3
    z4 = str(datums[i])[4]
    z5 = str(datums[i])[5]
    zm =z4+z5
    if zm == monat_ausgewählt and zy == jahr_ausgewählt :
        preis_monat.append(preise[i])

# Berechnung von gesamtem Preis in Monat
ausgaben_monat = 0

for i in range (len(preis_monat)):
    ausgaben_monat += preis_monat[i]
print(ausgaben_monat)
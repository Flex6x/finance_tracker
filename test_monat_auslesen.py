import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

produkte=[]
preise=[]
datums=[]

for eintrag in ausgaben:
    preise.append(eintrag["preis"])
    datums.append(eintrag["datum"]) 

monat=[]



for i in range (len(preise)):
    z3 = str(datums[i])[4]
    z4 = str(datums[i])[5]
    z=z3+z4
    monat.append(z)
print(monat)


#for i in range (len(preise)):
    #z3 = (datums[i] // 1000) % 10
    #z4 = (datums[i] // 100) % 10
    #monat.append(z3,z4)
    #print(monat)
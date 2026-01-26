import json

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

produkte=[]
preise=[]
datums=[]

for eintrag in ausgaben:
    preise.append(eintrag["preis"])
    datums.append(eintrag["datum"]) 

print (preise)
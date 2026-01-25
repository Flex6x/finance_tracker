import customtkinter as ctk
from tkinter import ttk
import json
import os

# Auswahl zwischen dark/light und theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# main window
app = ctk.CTk()
app.title("Finanz Tracker")
app.geometry("1040x800")
app.resizable(width=True, height =True) #Fenstereinstellungen skalierbar

# Rows and Columns in app
app.columnconfigure (0,weight=1)
app.columnconfigure (1,weight=1)
app.columnconfigure (2,weight=1)
app.columnconfigure (3,weight=1)
app.columnconfigure (4,weight=1)

app.rowconfigure (0,weight=1)
app.rowconfigure (1,weight=1)
app.rowconfigure (2,weight=5)
app.rowconfigure (3,weight=2)


# Tabview
tabview = ctk.CTkTabview(
        master=app,               
        corner_radius=20,
        #fg_color="#242424",
        segmented_button_selected_color="gray",
        segmented_button_selected_hover_color="black"
        )
tabview.grid(row=1, column=0, rowspan=2,columnspan=5, sticky="nsew")

# Tabs 
tab1=tabview.add("Startseite")
tab2=tabview.add("Ausgaben")
tab3=tabview.add("Ausgabelimit")
tab4=tabview.add("Gespartes Geld")
tab5=tabview.add("Sparziel")

# rows and columns in tab1
tab1.grid_rowconfigure(0, weight=1)
tab1.grid_columnconfigure(0, weight=1)

# rows and columns in tab2
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_rowconfigure(1, weight=3)
tab2.grid_columnconfigure((0,1,2,3), weight=1)

# rows and columns in tab3
tab3.grid_rowconfigure(0, weight=1)
tab3.grid_columnconfigure(0, weight=1)

# rows and columns in tab4
tab4.grid_rowconfigure(0, weight=1)
tab4.grid_columnconfigure(0, weight=1)

# rows and columns in tab5
tab5.grid_rowconfigure(0, weight=1)
tab5.grid_columnconfigure(0, weight=1)

# Überschrift
label = ctk.CTkLabel(app, text="Finanz Tracker", font=("Arial", 35))
label.grid(row=0, column=0, columnspan=5)

# Beschreibung in tab1
label = ctk.CTkLabel(
    master=tab1,
    text="Willkommen zu Deinem persönlichen Finanztracker. Du kannst Ausgabelimits erstellen und deine Ausgaben tracken, Sparziele erstellen und schauen ob du diese einhälst und alles in Diagrammen übersichtlich darstellen.",
    wraplength=500, #mit automatischem Zeilenumbruch
    font=("Arial", 20),
    text_color="white",
    corner_radius=8
)
label.grid(row=0, column=0,sticky ="ew")

# Funktionen für die Entrys
produkt=""
preis=""
datum=""
def answer_produkt():
    global produkt
    produkt = entry_produkt.get()
def answer_preis():
    global preis
    preis = entry_preis.get()
def answer_datum():
    global datum
    datum = entry_datum.get()

def save_ausgabe():
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


# Entry zu Produkt
entry_produkt = ttk.Entry(tab2)
entry_produkt.grid (row =0, column=0,sticky="w")
button_produkt=ttk.Button(tab2,text="<<-- Produkt", command =answer_produkt)
button_produkt.grid(row=0, column=0,sticky="e")

# Entry zu Preis
entry_preis = ttk.Entry(tab2)
entry_preis.grid (row =0, column=1,sticky="w")
button_preis=ttk.Button(tab2,text="<<-- Preis in €", command =answer_preis)
button_preis.grid(row=0, column=1,sticky="e")

# Entry zu Datum
entry_datum = ttk.Entry(tab2)
entry_datum.grid (row =0, column=2,sticky="w")
button_datum=ttk.Button(tab2,text="<<-- Datum in YYYYMMDD", command =answer_datum)
button_datum.grid(row=0, column=2,sticky="e")

button_save_ausgabe=ttk.Button(tab2,text="start",command =save_ausgabe)
button_save_ausgabe.grid(row=0, column=3,sticky="ew")

# Tabelle in Tab 2 anlegen

table = ttk.Treeview(tab2,columns = ("produkt", "preis", "datum"),show="headings")
table.heading("produkt",text="Produkt")
table.heading("preis",text="Preis in €")
table.heading("datum",text="Datum in YYYYMMDD")
table.grid(row=1,column=0,columnspan=4,sticky="nsew")

# Einträge aus ausgaben.json lesen und in listen eintragen 

with open("ausgaben.json", "r") as fh:
    ausgaben = json.load(fh)

produkte=[]
preise=[]
datums=[]

print("Daten\n")

for eintrag in ausgaben:
    produkte.append(eintrag["produkt"])
    preise.append(eintrag["preis"])
    datums.append(eintrag["datum"])

#Einträge eintragen
for i in range (len(produkte)):
    table.insert(parent="", index=i, values =(produkte[i], preise[i], datums[i])) 

# Run the application
app.mainloop()
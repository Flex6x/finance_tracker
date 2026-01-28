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

# Größe von Text in Tabelle - in Zellen
style = ttk.Style()
style.configure(
    "Treeview",
    font=("Arial", 15)   # Schriftart, Schriftgröße
)
# in Übeschriften
style.configure(
    "Treeview.Heading",
    font=("Arial", 15, "bold")
)

# Rows and Columns in app
app.columnconfigure (0,weight=1)
app.columnconfigure (1,weight=1)
app.columnconfigure (2,weight=1)
app.columnconfigure (3,weight=1)
app.columnconfigure (4,weight=1)

app.rowconfigure (0,weight=1)
app.rowconfigure (1,weight=1)
app.rowconfigure (2,weight=5)


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
tab3.grid_rowconfigure(0, weight=7)
tab3.grid_rowconfigure(1, weight=10)
tab3.grid_rowconfigure((2), weight=20)
tab3.grid_columnconfigure((0,1,2,3), weight=1)

# rows and columns in tab4
tab4.grid_rowconfigure(0, weight=7)
tab4.grid_rowconfigure(1, weight=10)
tab4.grid_rowconfigure((2), weight=20)
tab4.grid_columnconfigure((0,1,2), weight=1)

# rows and columns in tab5
tab5.grid_rowconfigure(0, weight=1)
tab5.grid_columnconfigure(0, weight=1)

# Überschrift
label_ueberschrift = ctk.CTkLabel(app, text="Finanz Tracker", font=("Arial", 35))
label_ueberschrift.grid(row=0, column=0, columnspan=5)

# Beschreibung in tab1
label_start = ctk.CTkLabel(
    master=tab1,
    text="Willkommen zu Deinem persönlichen Finanztracker. Du kannst Ausgabelimits erstellen und deine Ausgaben tracken, Sparziele erstellen und schauen ob du diese einhälst.",
    wraplength=500, # mit automatischem Zeilenumbruch
    font=("Arial", 20),
    text_color="white",
    corner_radius=8
)
label_start.grid(row=0, column=0,sticky ="ew")

# Funktionen für die Entrys
produkt=""
preis=""
datum=""
def answer_produkt():
    global produkt
    produkt = entry_produkt.get()
def answer_preis():
    global preis
    preis = float(entry_preis.get())
def answer_datum():
    global datum
    datum = int(entry_datum.get())

def save_ausgabe():
    if produkt == "" or preis == "" or datum == "": # Neuer Eintrag nur wenn alle Felder gefüllt sind
        print("Alle Felder müssen ausgefüllt sein!")
    else:
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
        table.insert(parent="", index=ctk.END, values =(produkt, preis, datum)) # Tabelle bei neuem Eintrag direkt updaten
        update_label_ausgaben_m() # Update der Ausgaben in tab3

def ausgabe_löschen():
    with open("ausgaben.json", "r", encoding="utf-8") as f:
        daten = json.load(f)

    # letzten Datensatz entfernen
    daten.pop()

    with open("ausgaben.json", "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4)
    items = table.get_children()
    table.delete(items[-1])
    update_label_ausgaben_m() # Update der Ausgaben in tab3

# Entry zu Produkt
entry_produkt = ttk.Entry(tab2, font = ("Arial", 13))
entry_produkt.grid (row =0, column=0,sticky="w",)
button_produkt=ttk.Button(tab2,text="<<-- Produkt", command =answer_produkt)
button_produkt.grid(row=0, column=0,sticky="e", padx=(0,10))

# Entry zu Preis
entry_preis = ttk.Entry(tab2, font = ("Arial", 13))
entry_preis.grid (row =0, column=1,sticky="w")
button_preis=ttk.Button(tab2,text="<<-- Preis in €", command =answer_preis)
button_preis.grid(row=0, column=1,sticky="e", padx=(0,10))

# Entry zu Datum
entry_datum = ttk.Entry(tab2, font = ("Arial", 13))
entry_datum.grid (row =0, column=2,sticky="w")
button_datum=ttk.Button(tab2,text="<<-- Datum in YYYYMMDD", command =answer_datum)
button_datum.grid(row=0, column=2,sticky="e", padx=(130,0))

# Save button
button_save_ausgabe=ttk.Button(tab2,text="start",command =save_ausgabe)
button_save_ausgabe.grid(row=0, column=3,sticky="w", padx=(22,0))

# Lösch Button
button_save_ausgabe=ttk.Button(tab2,text="Letzten Eintrag löschen",command =ausgabe_löschen)
button_save_ausgabe.grid(row=0, column=3,sticky="e")

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

for eintrag in ausgaben:
    produkte.append(eintrag["produkt"])
    preise.append(eintrag["preis"])
    datums.append(eintrag["datum"]) 

# Einträge eintragen
for i in range (len(produkte)):
    table.insert(parent="", index=i, values =(produkte[i], preise[i], datums[i]))

# Text für tab3
label_tab3_beschreibung = ctk.CTkLabel(
    master=tab3,
    text="Hier kannst du dein monatliches Ausgabelimit eingeben. Wähle außerdem deinen aktuellen Monat und Jahr aus. Es werden alle Ausgaben aus diesem Monat addiert.",
    wraplength=600, #mit automatischem Zeilenumbruch
    font=("Arial", 20),
    text_color="white",
    corner_radius=8
)
label_tab3_beschreibung.grid(row=0, column=0,columnspan=4,sticky ="ew")

# Funktionen für die Entrys
def answer_ausgabelimit():
    global limit
    global ausgabelimit
    limit = entry_ausgabelimit.get()
    ausgabelimit = int(limit)
    speichere_wert_al ()
def answer_monat():
    global monat_ausgewaehlt
    monat_ausgewaehlt = str(entry_monat.get())
    speichere_wert_monat()
def answer_jahr():
    global jahr_ausgewaehlt
    jahr_ausgewaehlt = entry_jahr.get()
    speichere_wert_jahr()

ausgaben_monat = None
ausgabenbilanz = None
def send_y_m():
    with open("ausgaben.json", "r") as fh:
        ausgaben = json.load(fh)

    preise_tab3=[]
    datums_tab3=[]

    for eintrag in ausgaben:
        preise_tab3.append(eintrag["preis"])
        datums_tab3.append(eintrag["datum"]) 

    preis_monat=[] # Liste für alle Preise von Ausgaben in gewähltem Monat

    # Monat wird ausgelesen, falls Monat mit gewähltem M. übereinstimmt wird der jeweilige Preis zur Liste hinzugefügt
    for i in range (len(preise_tab3)):
        z0 = str(datums_tab3[i])[0]
        z1 = str(datums_tab3[i])[1]
        z2 = str(datums_tab3[i])[2]
        z3 = str(datums_tab3[i])[3]
        zy = z0+z1+z2+z3
        z4 = str(datums_tab3[i])[4]
        z5 = str(datums_tab3[i])[5]
        zm =z4+z5
        if zm == monat_ausgewaehlt and zy == jahr_ausgewaehlt :
            preis_monat.append(preise_tab3[i])

    # Berechnung von gesamtem Preis der Ausgaben in Monat
    global ausgaben_monat
    global ausgabenbilanz
    global ausgabenbilanz_str
    global ausgaben_monat_str
    ausgaben_monat = 0
    for i in range (len(preis_monat)):
        ausgaben_monat += preis_monat[i]
    ausgaben_monat_str = str(ausgaben_monat)
    speichere_wert_ausgaben_monat()
    ausgabenbilanz = ausgabelimit - ausgaben_monat
    ausgabenbilanz_str = str(ausgabenbilanz)
    speichere_wert_bilanz()
    update_label_ausgaben_m()

# Buttons in tab3
entry_ausgabelimit = ttk.Entry(tab3, font = ("Arial", 15))
entry_ausgabelimit.grid (row =1, column=0, sticky="w")
button_ausgabelimit=ttk.Button(tab3,text="<<-- Ausgabelimit in €", command =answer_ausgabelimit)
button_ausgabelimit.grid(row=1, column=0, padx=(200, 0))

entry_monat = ttk.Entry(tab3, font = ("Arial", 15))
entry_monat.grid (row =1, column=1,sticky="w")
button_monat=ttk.Button(tab3,text="<<-- Monat", command =answer_monat)
button_monat.grid(row=1, column=1, padx=(200, 0))

entry_jahr = ttk.Entry(tab3, font = ("Arial", 15))
entry_jahr.grid (row =1, column=2,sticky ="w")
button_jahr=ttk.Button(tab3,text="<<-- Jahr", command =answer_jahr)
button_jahr.grid(row=1, column=2, padx=(200, 0))

button_send_y_m=ttk.Button(tab3,text="Start", command =send_y_m)
button_send_y_m.grid(row=1, column=3)

# Ausgabe von Ausgabelimit im jew. Monat

label_text = ctk.StringVar()

datei_al = "ausgabelimit_datei.txt"
def lade_wert_al():
    if os.path.exists(datei_al):
        with open(datei_al, "r") as f:
            return int(f.read())
    return 0  # Defaultwert (gibt 0 zurück in die Variable falls .txt nicht extistiert)
datei_m_g = "monat_ausg.txt"
def lade_wert_monat():
    if os.path.exists(datei_m_g):
        with open(datei_m_g, "r") as f:
            return int(f.read())
    return 0  # Defaultwert (gibt 0 zurück in die Variable falls .txt nicht extistiert)
datei_j_g = "jahr_ausg.txt"
def lade_wert_jahr():
    if os.path.exists(datei_j_g):
        with open(datei_j_g, "r") as f:
            return int(f.read())
    return 0  # Defaultwert (gibt 0 zurück in die Variable falls .txt nicht extistiert)
datei_ab = "ausgabenbilanz_datei.txt"
def lade_wert_bilanz():
    if os.path.exists(datei_ab):
        with open(datei_ab, "r") as f:
            return int(f.read())
    return 0  # Defaultwert (gibt 0 zurück in die Variable falls .txt nicht extistiert)
datei_am = "ausgaben_monat_datei.txt"
def lade_wert_ausgaben_monat():
    if os.path.exists(datei_am):
        with open(datei_am, "r") as f:
            return int(f.read())
    return 0  # Defaultwert (gibt 0 zurück in die Variable falls .txt nicht extistiert)

def speichere_wert_al():
    with open(datei_al, "w") as f:
        f.write(limit)
def speichere_wert_monat():
    with open(datei_m_g, "w") as f:
        f.write(monat_ausgewaehlt)
def speichere_wert_jahr():
    with open(datei_j_g, "w") as f:
        f.write(jahr_ausgewaehlt)
def speichere_wert_bilanz():
    with open(datei_ab, "w") as f:
        f.write(ausgabenbilanz_str)
def speichere_wert_ausgaben_monat():
    with open(datei_am, "w") as f:
        f.write(ausgaben_monat_str)

def update_label_ausgaben_m():
    bilanzinfo = ""
    ab = ausgabenbilanz
    if ausgabenbilanz is None:
        pass
    else:
        if ab > 0:
            bilanzinfo = f"Sehr gut! Du hast noch {ab}€ übrig."
        elif ab == 0:
            bilanzinfo = f"Achtung! Du hast dein Ausgabenlimit erreicht"
        else:
            bilanzinfo = f"!!Warnung!! Du hast dein Ausgabelimit um {abs(ab)}€ überschritten! \nKeine Ausgaben mehr!"

    if ausgaben_monat is None:
        pass
    else:
        label_text.set(f"Deine Ausgaben im Monat {monat_ausgewaehlt} in {jahr_ausgewaehlt}: {ausgaben_monat}€. \nAusgabelimit im Monat {monat_ausgewaehlt}: {ausgabelimit}€ \nBilanz im Monat {monat_ausgewaehlt}: {ausgabenbilanz}€\n{bilanzinfo}")
if ausgaben_monat is None:
    pass
else:
    ausgaben_monat.trace_add("write", update_label_ausgaben_m)

label_ausgabenbilanz = ttk.Label(tab3, textvariable=label_text, font=("Arial", 30))
label_ausgabenbilanz.grid(row=2, column=0,columnspan=4)

ausgabelimit = int(lade_wert_al())
ausgabenbilanz = int(lade_wert_bilanz())
ausgaben_monat = int(lade_wert_ausgaben_monat())
monat_ausgewaehlt = str(lade_wert_monat())
jahr_ausgewaehlt = str(lade_wert_jahr())
update_label_ausgaben_m()

# Text für tab4
label_tab4_beschreibung = ctk.CTkLabel(
    master=tab4,
    text="Hier kannst du alle deine gesparten Geldbeträge mit jeweiligem Datum eintragen. Dir erhälst auf Basis von deinem Sparziel Vorschläge, wie viel Geld du für dieses jede Woche bei Seite legen muss.",
    wraplength=600, #mit automatischem Zeilenumbruch
    font=("Arial", 20),
    text_color="white",
    corner_radius=8
)
label_tab4_beschreibung.grid(row=0, column=0,columnspan=4,sticky ="ew")


# Run the application
app.mainloop()
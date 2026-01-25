import customtkinter as ctk
from tkinter import ttk

# Auswahl zwischen dark/light und theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# main window
app = ctk.CTk()
app.title("Finanz Tracker")
app.geometry("800x600")
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
tab2.grid_columnconfigure(0, weight=1)

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

# Tabelle in Tab 2

table = ttk.Treeview(tab2,columns = ("produkt", "preis", "datum"),show="headings")
table.grid(row=0,column=0,sticky="nsew")

# Run the application
app.mainloop()
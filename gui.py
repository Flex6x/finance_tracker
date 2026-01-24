import customtkinter as ctk

# Auswahl zwischen dark/light und theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# main window
app = ctk.CTk()
app.title("Finanz Tracker")
app.geometry("800x600")
app.resizable(width=True, height =True) #Fenstereinstellungen skalierbar

# Rows and Columns
app.columnconfigure (0,weight=1)
app.columnconfigure (1,weight=1)
app.columnconfigure (2,weight=1)

app.rowconfigure (0,weight=1)
app.rowconfigure (1,weight=1)
app.rowconfigure (2,weight=1)

# Überschrift
label = ctk.CTkLabel(app, text="Finanz Tracker", font=("Arial", 35))
label.grid(row=0, column=1)

def button_callback():
    print ("Hallo")

# Add a button
button1 = ctk.CTkButton(
    master=app,
    text="Click Me",
    command=button_callback,
    width=200,
    height=50,
    border_width=0,
    corner_radius=8,
    hover=True
)
button1.grid(row=1, column=1, padx=10, pady=10)
#Textfeld 

label = ctk.CTkLabel(
    master=app,
    text="Willkommen zu Deinem persönlichen Finanztracker. Du kannst Ausgabelimits erstellen und deine Ausgaben tracken, Sparziele erstellen und schauen ob du diese einhälst und alles in Diagrammen übersichtlich darstellen.", wraplength=500, #mit automatischem Zeilenumbruch
    font=("Arial", 20),
    text_color="white",
    corner_radius=8
)
label.grid(row=2, column=1)



# Run the application
app.mainloop()
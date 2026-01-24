import customtkinter as ctk

# Auswahl zwischen dark/light und theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# main window
app = ctk.CTk()
app.title("Finanz Tracker")
app.geometry("800x600")
app.resizable(width=True, height =True) #Fenstereinstellungen skalierbar

# Überschrift
label = ctk.CTkLabel(app, text="Finanz Tracker", font=("Arial", 35))
label.pack(pady=20)

# Add a button
button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked!"))
button.pack(pady=10)

# Run the application
app.mainloop()
import tkinter as tk
from tkinter import ttk

# Initialise the main application window
root = tk.Tk()
root.title("TTRPG Campaign Manager")
root.geometry("600x450")

# Setup grid
root.rowconfigure(0, weight=1)

# Frames
frmMenu = ttk.Frame(root)
frmMenu.grid(row=0, column=0, sticky="w", padx=20)

# Labels
lblTitle = ttk.Label(frmMenu, text="TTRPG Campaign Manager", font=("Arial, 24"))
lblTitle.grid(row=0,column=0, sticky="w", pady=(0,20))

# Button Functions



# Buttons
btnCreate = ttk.Button(frmMenu, text="Create World")
btnCreate.grid(row=1, column=0, sticky="w", pady=10)
btnLoad = ttk.Button(frmMenu, text="Load World")
btnLoad.grid(row=2, column=0, sticky="w", pady=10)

# Starts the application
root.mainloop()
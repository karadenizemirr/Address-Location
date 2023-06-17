import tkinter as tk
from tkinter import ttk
from pandastable import Table

def getTableWindow(dataframe):
    root = tk.Tk()
    root.title = "Latitude - Longitude Table"

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    table = Table(frame, dataframe=dataframe, showtoolbar=True,showstatusbar=True)
    table.show()

    root.mainloop()
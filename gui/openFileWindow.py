import tkinter as tk
from tkinter import filedialog

def open_file_windows():
    root = tk.Tk()
    root.withdraw()
    file_types = (("CSV File", "*.csv"),)

    file_path = filedialog.askopenfilename(title="Select a file", filetypes=file_types)

    return file_path
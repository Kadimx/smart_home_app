# utils.py
import tkinter as tk
from tkinter import messagebox

def clear_screen(root):
    """Clears all widgets on the current screen."""
    for widget in root.winfo_children():
        widget.destroy()

def show_message(title, message):
    """Displays a message box with the given title and message."""
    messagebox.showinfo(title, message)

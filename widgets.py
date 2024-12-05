# widgets.py
import tkinter as tk
from tkinter import Button

class CustomButton(Button):
    def __init__(self, master, text, command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(font=("Arial", 14), bg="#4C75D9", fg="white", height=2, width=20)

class CustomLabel(tk.Label):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.config(font=("Arial", 16), bg="#E1E8F0", fg="black")

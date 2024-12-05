# login.py
import tkinter as tk
from tkinter import messagebox
from widgets import CustomButton, CustomLabel
from screens import home_screen
import utils

def login_screen(root):
    utils.clear_screen(root)
    frame = tk.Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Smart Home Login", font=("Arial", 24))
    header.pack(pady=40)

    username_label = CustomLabel(frame, text="Username:")
    username_label.pack(pady=5)
    username_entry = tk.Entry(frame, font=("Arial", 14))
    username_entry.pack(pady=5)

    password_label = CustomLabel(frame, text="Password:")
    password_label.pack(pady=5)
    password_entry = tk.Entry(frame, font=("Arial", 14), show="*")
    password_entry.pack(pady=5)

    def validate_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if username == "admin" and password == "password123":
            utils.show_message("Login", "Login successful!")
            home_screen(root)  # Go to home screen after login
        else:
            utils.show_message("Login", "Invalid username or password")

    CustomButton(frame, text="Login", command=validate_login).pack(pady=10)
    CustomButton(frame, text="Exit", command=root.quit).pack(pady=10)

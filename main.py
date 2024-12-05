# main.py
import tkinter as tk
from login import login_screen

def main():
    # Initialize root window
    root = tk.Tk()
    root.title("Smart Home Control")
    root.geometry("375x667")  # Phone-sized window for the interface
    
    # Show login screen first
    login_screen(root)
    
    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()

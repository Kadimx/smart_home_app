# screens.py
import tkinter as tk
from tkinter import Frame
from widgets import CustomButton, CustomLabel
import utils

def home_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Smart Home Control")
    header.pack(pady=20)

    CustomButton(frame, text="Camera", command=lambda: camera_screen(root)).pack(pady=10)
    CustomButton(frame, text="Control", command=lambda: control_screen(root)).pack(pady=10)
    CustomButton(frame, text="Automation", command=lambda: automation_screen(root)).pack(pady=10)
    CustomButton(frame, text="User Profile", command=lambda: user_profile_screen(root)).pack(pady=10)

def camera_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Camera Feed")
    header.pack(pady=20)
    
    CustomButton(frame, text="Play Camera", command=lambda: camera_play_screen(root)).pack(pady=10)
    CustomButton(frame, text="Back to Home", command=lambda: home_screen(root)).pack(pady=10)

def camera_play_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Camera Playing")
    header.pack(pady=20)
    
    CustomButton(frame, text="Volume Control", command=lambda: camera_volume_screen(root)).pack(pady=10)
    CustomButton(frame, text="Mute", command=lambda: camera_mute_screen(root)).pack(pady=10)
    CustomButton(frame, text="Back to Camera", command=lambda: camera_screen(root)).pack(pady=10)

def camera_volume_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Adjust Volume")
    header.pack(pady=20)
    
    CustomButton(frame, text="Increase Volume", command=lambda: print("Increasing volume")).pack(pady=10)
    CustomButton(frame, text="Decrease Volume", command=lambda: print("Decreasing volume")).pack(pady=10)
    CustomButton(frame, text="Back to Camera", command=lambda: camera_play_screen(root)).pack(pady=10)

def camera_mute_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Mute Camera")
    header.pack(pady=20)
    
    CustomButton(frame, text="Mute", command=lambda: print("Muting camera")).pack(pady=10)
    CustomButton(frame, text="Unmute", command=lambda: print("Unmuting camera")).pack(pady=10)
    CustomButton(frame, text="Back to Camera", command=lambda: camera_play_screen(root)).pack(pady=10)

def control_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Control Devices")
    header.pack(pady=20)

    CustomButton(frame, text="Add Device", command=lambda: add_device_screen(root)).pack(pady=10)
    CustomButton(frame, text="Back to Home", command=lambda: home_screen(root)).pack(pady=10)

def add_device_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Add New Device")
    header.pack(pady=20)

    CustomButton(frame, text="Add Room", command=lambda: add_room_screen(root)).pack(pady=10)
    CustomButton(frame, text="Back to Control", command=lambda: control_screen(root)).pack(pady=10)

def add_room_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Add New Room")
    header.pack(pady=20)

    CustomButton(frame, text="Living Room", command=lambda: print("Living Room added")).pack(pady=10)
    CustomButton(frame, text="Back to Add Device", command=lambda: add_device_screen(root)).pack(pady=10)

def automation_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="Automation Settings")
    header.pack(pady=20)

    CustomButton(frame, text="Add New Automation", command=lambda: print("Adding automation...")).pack(pady=10)
    CustomButton(frame, text="Back to Home", command=lambda: home_screen(root)).pack(pady=10)

def user_profile_screen(root):
    utils.clear_screen(root)
    frame = Frame(root, bg="#E1E8F0")
    frame.pack(fill=tk.BOTH, expand=True)
    
    header = CustomLabel(frame, text="User Profile")
    header.pack(pady=20)

    CustomButton(frame, text="Air Conditioning", command=lambda: print("Air Conditioning settings")).pack(pady=10)
    CustomButton(frame, text="Lights ON", command=lambda: print("Turning on lights")).pack(pady=10)
    CustomButton(frame, text="Lights OFF", command=lambda: print("Turning off lights")).pack(pady=10)
    CustomButton(frame, text="Cleaner Robot", command=lambda: print("Activating cleaner robot")).pack(pady=10)
    CustomButton(frame, text="Back to Home", command=lambda: home_screen(root)).pack(pady=10)

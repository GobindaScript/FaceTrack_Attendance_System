import tkinter as tk
from tkinter import font
import os
import threading

def run_registration():
    # Runs the registration script in a separate thread to prevent freezing the GUI
    threading.Thread(target=lambda: os.system('python Register_Face.py')).start()

def run_attendance():
    # Runs the attendance script in a separate thread
    threading.Thread(target=lambda: os.system('python Attendance.py')).start()

# Initialize the main window
root = tk.Tk()
root.title("FaceTrack Attendance System")
root.geometry("450x350")
root.configure(bg="#1e272e")

# Styling
title_font = font.Font(family="Helvetica", size=18, weight="bold")
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Header
tk.Label(root, text="FaceTrack Control Panel", font=title_font, bg="#1e272e", fg="#d2dae2").pack(pady=30)

# Registration Button
tk.Button(root, text="1. Register New Face", font=button_font, bg="#0fb9b1", fg="white", 
          activebackground="#2bcbba", activeforeground="white", bd=0, padx=20, pady=10, 
          command=run_registration, width=20).pack(pady=10)

# Attendance Button
tk.Button(root, text="2. Start Attendance", font=button_font, bg="#20bf6b", fg="white", 
          activebackground="#26de81", activeforeground="white", bd=0, padx=20, pady=10, 
          command=run_attendance, width=20).pack(pady=10)

# Exit Button
tk.Button(root, text="Exit", font=button_font, bg="#eb3b5a", fg="white", 
          activebackground="#fc5c65", activeforeground="white", bd=0, padx=20, pady=10, 
          command=root.quit, width=20).pack(pady=10)

root.mainloop()
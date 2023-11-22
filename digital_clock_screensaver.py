import tkinter as tk
import time
import ctypes

def display_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, display_time)

root = tk.Tk()
root.title("Digital Clock Screensaver")
root.geometry("250x150")

# Get system color for the window background
color = ctypes.windll.user32.GetSysColor(1)  # 1 for the default color of the window

root.configure(bg='#{:06x}'.format(color))  # Set window background color

clock_label = tk.Label(root, font=('Arial', 60), fg='white', bg='#{:06x}'.format(color))
clock_label.pack(pady=40)

display_time()

root.mainloop()

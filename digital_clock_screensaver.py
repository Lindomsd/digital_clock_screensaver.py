import tkinter as tk
import time
import ctypes

def display_time_and_date():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %B %d, %Y')
    clock_label.config(text=current_time + "\n" + current_date)
    clock_label.after(1000, display_time_and_date)

root = tk.Tk()
root.title("Digital Clock Screensaver")
root.geometry("350x200")

# Get system color for the window background
color = ctypes.windll.user32.GetSysColor(1)  # 1 for the default color of the window

root.configure(bg='#{:06x}'.format(color))  # Set window background color

clock_label = tk.Label(root, font=('Arial', 70), fg='white', bg='#{:06x}'.format(color))
clock_label.pack(pady=60)

display_time_and_date()

root.mainloop()


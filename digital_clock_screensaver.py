import tkinter as tk
import time
import ctypes
import random

def change_colors():
    # Generate random RGB values for the background and text colors
    bg_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    text_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

    # Apply the new colors to the window background and clock label
    root.configure(bg=bg_color)
    clock_label.config(fg=text_color, bg=bg_color)
    root.after(3000, change_colors)  # Change colors every 3 seconds

def display_time_and_date():
    current_time = time.strftime('%H:%M:%S')
    current_date = time.strftime('%A, %B %d, %Y')
    clock_label.config(text=current_time + "\n" + current_date)
    root.after(1000, display_time_and_date)

root = tk.Tk()
root.title("Color-changing Digital Clock Screensaver")
root.geometry("350x200")

# Get system color for the window background
color = ctypes.windll.user32.GetSysColor(1)  # 1 for the default color of the window

root.configure(bg='#{:06x}'.format(color))  # Set initial window background color

clock_label = tk.Label(root, font=('Arial', 100), fg='white', bg='#{:06x}'.format(color))
clock_label.pack(pady=60)

# Start the functions to display time/date and change colors
display_time_and_date()

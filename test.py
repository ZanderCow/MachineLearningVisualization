import tkinter as tk
from tkinter import messagebox

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

def close_window():
    if messagebox.askokcancel("Close", "Do you want to close the window?"):
        root.destroy()

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add an option to open a new window
file_menu.add_command(label="Open New Window", command=open_new_window)

# Add an option to close the main window
file_menu.add_command(label="Exit", command=close_window)

# Start the main loop
root.mainloop()
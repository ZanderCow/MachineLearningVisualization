import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, bg='grey')
frame.pack(fill=tk.BOTH, expand=True)

button = tk.Button(frame, text='Click Me!')
button.pack(padx=10, pady=10)

root.mainloop()

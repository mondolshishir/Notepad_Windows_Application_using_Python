
import tkinter as tk
from tkinter import ttk
from tkinter import  font, colorchooser, filedialog, messagebox

import  os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("MS Notepad")

main_menu = tk.Menu()

new_icon = tk.PhotoImage(file="icons/new_folder.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save_folder.png")
save_as_icon = tk.PhotoImage(file="icons/save_folder.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

file = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="File", menu=file)

file.add_cascade(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+n")
file.add_cascade(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+o")
main_application.config(menu=main_menu)














main_application.mainloop()

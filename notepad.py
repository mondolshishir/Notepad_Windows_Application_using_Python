
import tkinter as tk
from tkinter import ttk
from tkinter import  font, colorchooser, filedialog, messagebox

import  os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("MS Notepad")

main_menu = tk.Menu()

#File Menu Icon
new_icon = tk.PhotoImage(file="icons/new_folder.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save_folder.png")
save_as_icon = tk.PhotoImage(file="icons/save_folder.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

file = tk.Menu(main_menu, tearoff=False)

#Edit Menu Icon
copy_icon = tk.PhotoImage(file="icons/copy.png")
paste_icon = tk.PhotoImage(file="icons/paste.png")
cut_item_icon = tk.PhotoImage(file="icons/cut.png")
find_icon = tk.PhotoImage(file="icons/find.png")

edit=tk.Menu(main_menu,tearoff=False)


#View Menu icon
tool_bar = tk.PhotoImage(file="icons/toolbar.png")
status_bar = tk.PhotoImage(file="icons/statusbar.png")

view = tk.Menu(main_menu, tearoff=False)

# Color image Icons
light_white = tk.PhotoImage(file="icons/light_default.jpg")
white_plus = tk.PhotoImage(file="icons/light_plus.jpg")
dark = tk.PhotoImage(file="icons/dark.jpg")
red = tk.PhotoImage(file="icons/red.jpg")
night_light = tk.PhotoImage(file="icons/night_blue.png")

color_theme = tk.Menu(main_menu, tearoff=False)


main_menu.add_cascade(label="File", menu=file)
main_menu.add_cascade(label="Edit", menu=edit)
main_menu.add_cascade(label="View", menu=view)
main_menu.add_cascade(label="Theme", menu=color_theme)


#Color Theme Menu
color_icons = (light_white, white_plus, dark, red, night_light)

color_dict = {
    'Light_default' : ('#000000', '#ffffff'),
    'White' : ('#474747', "#e0e0e0"),
    'Dark' : ('#c4c4c4','#2d2d2d'),
    'Red' :('#2d2d2d', '#474747'),
    'Blue' :('#ededed', '#6b9dc2')
}
#View Menu
view.add_checkbutton(label="Tool Bar", onvalue=True, offvalue= 0, image=tool_bar, compound=tk.LEFT)
view.add_checkbutton(label="Status Bar", onvalue=True, offvalue= 0, image=status_bar, compound=tk.LEFT)


#Edit Menu
edit.add_command(label="Copy", image=copy_icon, compound=tk.LEFT, accelerator="ctrl+c")
edit.add_command(label="Cut", image=cut_item_icon, compound=tk.LEFT, accelerator="ctrl+x")
edit.add_command(label="Paste", image=paste_icon, compound=tk.LEFT, accelerator="ctrl+v")
edit.add_command(label="Find", image=copy_icon, compound=tk.LEFT, accelerator="ctrl+f")


#File Menu
file.add_cascade(label="New", image=new_icon, compound=tk.LEFT, accelerator="Ctrl+n")
file.add_cascade(label="Open", image=open_icon, compound=tk.LEFT, accelerator="Ctrl+o")
file.add_cascade(label="Save", image=save_icon, compound=tk.LEFT, accelerator="Ctrl+s")
file.add_cascade(label="Save As", image=save_as_icon, compound=tk.LEFT, accelerator="Ctrl+Alt+s")
file.add_cascade(label="Exit", image=exit_icon, compound=tk.LEFT, accelerator="Ctrl+")
main_application.config(menu=main_menu)














main_application.mainloop()

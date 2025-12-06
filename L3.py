from tkinter import *
from tkinter.ttk import *
from time import strftime

recipe = Tk()
recipe.title("Menu")
#recipe.config(background = "red")

# Creating Menu Bar
menubar = Menu(recipe)

# Adding File Menu And Commands
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "file", menu = file_menu)
file_menu.add_command(label = 'new file', command = None)
file_menu.add_command(label = 'Open', command = None)
file_menu.add_command(label = 'Save', command = None)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = recipe.destroy)

recipe.config(menu = menubar)
recipe.mainloop()

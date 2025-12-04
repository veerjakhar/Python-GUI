from tkinter import *

# Create A Tkinter Window
root = Tk()

root.geometry('100x100') 
# Create A Button
btn = Button(root, text = 'Click!', bd = '5', background = "red", command = root.destroy)
btn.pack(side = 'bottom')

btl = Button(root, text = "CLICK", bd = '20', background = "yellow", command = root.destroy)
btl.pack(side = "top")
root.mainloop()
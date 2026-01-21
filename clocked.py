from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

# Display Time on the Label
def time():
    string = strftime('%H: %M: %S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

# Styling the Label Widgit
lbl = Label(root, text = "00:00:00", font = ('calibri', 40, 'bold'), background = 'blue', foreground = 'orange')
lbl.pack()

bts = Button(root, text = "Show Time", command = lambda: time())
bts.pack()

root.mainloop()
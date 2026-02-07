from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("List Rememberer")
root.geometry("500x500")

def savefile():
    fout = asksaveasfile(defaultextention = ".txt")
    if fout is not none:
        for item in listbox.get(0, END):
            print(item.strip(), file = fout)
            listbox.delete(0, END)

def openfile():
    fin = askopenfile(title = 'Open File')
    if fin is not None:
        listbox.delete(0, END)
        items = fin.readlines()
        for item in items:
            listbox.insert(END, item, item.strip())


saveb = Button(root, text = "Save", command = savefile)
saveb.pack(padx = 5, pady = 5)

sentry = Entry(root)
sentry.pack(padx = 5, pady = 5)

addb = Button(root, text = "Add")
addb.pack(padx = 5, pady = 5)

openb = Button(root, text = "Open", command = openfile)
openb.pack(side = LEFT, padx = 5, pady = 5)

deleteb = Button(root, text = "Delete")
deleteb.pack(side = RIGHT, padx = 5, pady = 5)

# Creating a listbox

frame = Frame(root)
scrollbar = Scrollbar(frame, orient = "vertical")
scrollbar.pack(side = RIGHT, fill = Y)
listbox = Listbox(frame, width = 70, yscrollcommand = scrollbar.set, bg = 'orange')
for i in range(1, 101):
    listbox.insert(END, "list" + str(i))
listbox.pack(side = LEFT, padx = 5)
scrollbar.config(command = listbox.yview)
frame.pack(side = RIGHT)


root.mainloop()

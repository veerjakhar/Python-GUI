from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('My Address Book')
root.geometry('700x500')

myaddressbook = {}

def clearall():
    name2.delete(0, END)
    address2.delete(0, END)
    mobile2.delete(0, END)
    email2.delete(0, END)
    birthday2.delete(0, END)

def updatefile():
    key = name2.get()
    if key == "":
        messagebox.showerror('showerror', 'Name Cannot Be Empty')
    else:
        if key not in myaddressbook.keys():
            listbox.insert(END, key)
        myaddressbook[key] = (name2.get(), address2.get(), mobile2.get(), email2.get(), birthday2.get())
        clearall()

def edit():
    clearall()
    index = listbox.curselection()
    if index:
        name2.insert(0, listbox.get(index))
        details = myaddressbook[name2.get()]
        address2.insert(0, details[1])
        mobile2.insert(0, details[2])
        email2.insert(0, details[3])
        birthday2.insert(0, details[4])
    else:
        messagebox.showerror('showerror', 'No Name Selected')

def delete_item():
    index = listbox.curselection()
    if index:
        del myaddressbook[listbox.get(index)]
        listbox.delete(index)
        clearall()
    else:
        messagebox.showerror('showerror', 'No Name Selected')


lbl1 = Label(root, text = "My Address Book")
lbl1.grid(row = 0, column = 1)

openb = Button(root, text = "Open")
openb.grid(row = 0, column = 3)

listbox = Listbox(root, width = 30, height = 15)
listbox.grid(row = 2, column = 0, padx = 5, columnspan = 3, rowspan = 5)

lbl2 = Label(root, text = "Name: ")
lbl2.grid(row = 2, column = 3)

lbl3 = Label(root, text = "Address: ")
lbl3.grid(row = 3, column = 3)

lbl4 = Label(root, text = "Mobile: ")
lbl4.grid(row = 4, column = 3)

lbl5 = Label(root, text = "Email: ")
lbl5.grid(row = 5, column = 3)

lbl6 = Label(root, text = "Birthday: ")
lbl6.grid(row = 6, column = 3)

name2 = Entry(root)
name2.grid(row = 2, column = 4)

address2 = Entry(root)
address2.grid(row = 3, column = 4)

mobile2 = Entry(root)
mobile2.grid(row = 4, column = 4)

email2 = Entry(root)
email2.grid(row = 5, column = 4)

birthday2 = Entry(root)
birthday2.grid(row = 6, column = 4)

editb = Button(root, text = 'Edit', command = edit)
editb.grid(row = 7, column = 1, pady = 5)

deleb = Button(root, text = 'Delete', command = delete_item)
deleb.grid(row = 7, column = 2, pady = 5)

upadb = Button(root, text = 'Update/Add', command = updatefile)
upadb.grid(row = 7, column = 4, pady = 5)

saveb = Button(root, text = 'Save', width = 30)
saveb.grid(row = 8, column = 0, columnspan = 3, pady = 10, padx = 15)


root.mainloop()

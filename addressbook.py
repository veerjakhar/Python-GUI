from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import *
import os

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

def reset():
    clearall()
    listbox.delete(0, 8)
    myaddressbook.clear()
    name2.configure(text = 'My Address Book')

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

def save_file():
    fout =  asksaveasfile(defaultextension = ".txt")
    if fout:
        print(myaddressbook, file = fout)
        reset()
    else:
        messagebox.showinfo('showinfo', "Warning, Addressbook not saved")

def delete_item():
    index = listbox.curselection()
    if index:
        del myaddressbook[listbox.get(index)]
        listbox.delete(index)
        clearall()
    else:
        messagebox.showerror('showerror', 'No Name Selected')

def display(event):
        newwindow = Toplevel(root)
        index = listbox.curselection()
        contact = ""
        if index:
            key = listbox.get(index)
            contact = "NAME: " + key + "\n \n"
            details = myaddressbook[key]
            contact += "ADDRESS: " + details[1] + "\n"
            contact += "MOBILE: " + details[2] + "\n"
            contact += "EMAIL: " + details[3] + "\n"
            contact += "BIRTHDAY: " + deatails[4] + "\n"

        lbl = Label(newwindow)
        lbl.grid(row = 0, column = 0)
        lbl.configure(text = contact)
        reset()

def openfile():
    global myaddressbook
    reset()
    fin = askopenfile(title = 'openfile')
    if fin:
        myaddressbook = eval(fin.read())
        for key in myaddressbook.keys():
            listbox.insert(END, key)
            name2.configure(text = os.path.basename(fin.name))
    else:
        messagebox.showinfo('showinfo', "Warning, No Addressbook Opened")

lbl1 = Label(root, text = "My Address Book")
lbl1.grid(row = 0, column = 1)

openb = Button(root, text = "Open", command = openfile)
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

saveb = Button(root, text = 'Save', width = 30, command = save_file)
saveb.grid(row = 8, column = 0, columnspan = 3, pady = 10, padx = 15)


root.mainloop()

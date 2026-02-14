from tkinter import *

root = Tk()
root.title('My Address Book')
root.geometry('700x500')

lbl1 = Label(root, text = "My Address Book")
lbl1.grid(row = 0, column = 1)

openb = Button(root, text = "Open")
openb.grid(row = 0, column = 3)

#scrollbar = Scrollbar(frame, orient = VERTICAL)
#scrollbar.grid(row = 1, column = 1)
listbox = Listbox(root, width = 30, height = 15)
listbox.grid(row = 2, column = 0, padx = 5, columnspan = 3, rowspan = 5)
#scrollbar.config(command = listbox.yview)

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

root.mainloop()

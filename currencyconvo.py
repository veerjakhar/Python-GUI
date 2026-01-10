from tkinter import *

root = Tk()
root.geometry("500x350")
root.title("Currency Convertion")

def fromus():
    dollars = float(usentry_value.get())
    
    ru = dollars * 90.27
    ro = dollars * 80
    po = dollars * 0.75

    ruptext.delete("1.0", END)
    ruptext.insert(END, ru)

    rblxtext.delete("1.0", END)
    rblxtext.insert(END, ro)

    poundtext.delete("1.0", END)
    poundtext.insert(END, po)

usentry_value = StringVar()

uslabel = Label(root, text = "Enter the currency in US dollar(s)")
uslabel.grid(row = 1, column = 1)

usentry = Entry(root, width = 30, textvariable = usentry_value)
usentry.grid(row = 1, column = 2)

convert = Button(root, text = "Convert", command = fromus)
convert.grid(row = 2, column = 2)

ruplabel = Label(root, text = "Result in Rupees")
ruplabel.grid(row = 3, column = 1)

ruptext =  Text(root, width = 30, height = 1)
ruptext.grid(row = 3, column = 2)

poundlabel = Label(root, text = "Result in Pounds")
poundlabel.grid(row = 4, column = 1)

poundtext = Text(root, width = 30, height = 1)
poundtext.grid(row = 4, column = 2)

rblxlabel = Label(root, text = "Result in Robux")
rblxlabel.grid(row = 5, column = 1)

rblxtext = Text(root, width = 30, height = 1)
rblxtext.grid(row = 5, column = 2)

root.mainloop()
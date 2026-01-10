from tkinter import *

root = Tk()
root.geometry("900x200")
root.title("Weight Distributer")

def frompound():
    pounds = float(lbsentry_value.get())

    g = pounds * 453.592
    kg = pounds * 0.453592
    flz = pounds * 16

    gentery.delete("1.0", END)
    gentery.insert(END, g)

    kgentry.delete("1.0", END)
    kgentry.insert(END, kg)

    flzentry.delete("1.0", END)
    flzentry.insert(END, flz)

lbsentry_value = StringVar()

lbs = Label(root, text = "Enter the weight in pounds")
lbs.grid(row = 1, column = 1)

lbsentry = Entry(root, width = 30, textvariable = lbsentry_value )
lbsentry.grid(row = 1, column = 2)

conv = Button(root, text = "Convert", command = frompound)
conv.grid(row = 1, column = 3)

g = Label(root, text = "Gram(s)")
g.grid(row = 2, column = 1)

kg = Label(root, text = "Kilogram(s)")
kg.grid(row = 2, column = 2)

flz = Label(root, text = "Ounce(s)")
flz.grid(row = 2, column = 3)

gentery = Text(root, width = 30, height = 1)
gentery.grid(row = 3, column = 1)

kgentry = Text(root, width = 30, height = 1)
kgentry.grid(row = 3, column = 2)

flzentry = Text(root, width = 30, height = 1)
flzentry.grid(row = 3, column = 3)




root.mainloop()

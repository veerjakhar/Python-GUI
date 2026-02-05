from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Multiplaction Table Generator")
root.geometry("300x700")

titble = Label(root, text = "Mathematical table")
titble.grid(row = 1, column = 2, pady = 25)

giver = Label(root, text = "Number and Range: ")
giver.grid(row = 3, column = 1)

# Combobox Creation

thenum = IntVar()
numbers = Combobox(root, textvariable = thenum, width = 5)
numbers['values'] = tuple(range(10001))
numbers.grid(row = 3, column = 2)

# Creating Radio Buttons

endVal = IntVar()
r10 = Radiobutton(root, text = "10", variable = endVal, value = 10)
r20 = Radiobutton(root, text = "20", variable = endVal, value = 20)
r30 = Radiobutton(root, text = "30", variable = endVal, value = 300)
endVal.set(10)
r10.grid(row = 3, column = 3)
r20.grid(row = 4, column = 3)
r30.grid(row = 5, column = 3)

def generatemulti():
    tables = ""
    for i in range(endVal.get() + 1):
        # tables += "{:^10d}X{:^10d} = {:^10d}\n".format(thenum.get(), i, thenum.get() * i)
        tables += str(thenum.get()) + "  X  " + str(i) + "  =  " + str(thenum.get() * i) + "\n"
        dismulti.configure(text = tables) 

generate = Button(root, text = "Generate", command = generatemulti)
generate.grid(row = 6, column = 2)

dismulti = Label(root, anchor = "center")
dismulti.grid(row = 7, column = 2, pady = 25)


root.mainloop()
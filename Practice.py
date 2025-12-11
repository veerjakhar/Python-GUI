from tkinter import *

dessert = Tk()
dessert.title("~Shop~")
dessert.config(background = 'red')
dessert.geometry("780x500")

email = Label(dessert, text = "Email").place(x = 80, y = 60)
password = Label(dessert, text = "Password").place(x = 80, y = 100)
emailput = Entry(dessert, width = 30).place(x = 180, y = 60)
passwordput = Entry(dessert, show = "*" ,width = 30).place(x = 180, y = 100)

sandwich = Label(dessert, text = "What food would you like: Chicken Sandwich, B.L.T, Veg sandwich or None?").place(x = 180, y = 170)
sandwichput = Entry(dessert, width = 30).place(x = 180, y = 210)
sand = Spinbox(dessert, from_ = 0, to = 100).place(x = 500, y = 210)

bevarage = Label(dessert, text = "What bevarage would you like: Cola, Fanta, Orange Juice, Water or None?").place(x = 180, y = 260)
bevarageput = Entry(dessert, width = 30).place(x = 180, y = 300)
beva = Spinbox(dessert, from_ = 0, to = 100).place(x = 500, y = 300)

dessert.mainloop()
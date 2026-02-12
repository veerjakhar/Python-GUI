from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("350x400")

turn = 1
result = ""

def bo1click():
    global turn
    texts =bo1.cget("text")
    if texts == '':
        if turn == 1:
            bo1.config(text = 'X')
            turn = 2
        else:
            bo1.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')


bo1 = Button(root, width = 5, height = 5, command = bo1click)
bo1.grid(row = 2, column = 1, padx = 5, pady = 5)

bo2 = Button(root, width = 5, height = 5)
bo2.grid(row = 2, column = 2, padx = 5, pady = 5)

bo3 = Button(root, width = 5, height = 5)
bo3.grid(row = 2, column = 3, padx = 5, pady = 5)

bo4 = Button(root, width = 5, height = 5)
bo4.grid(row = 3, column = 1, padx = 5, pady = 5)

bo5 = Button(root, width = 5, height = 5)
bo5.grid(row = 3, column = 2, padx = 5, pady = 5)

bo6 = Button(root, width = 5, height = 5)
bo6.grid(row = 3, column = 3, padx = 5, pady = 5)

bo7 = Button(root, width = 5, height = 5)
bo7.grid(row = 4, column = 1, padx = 5, pady = 5)

bo8 = Button(root, width = 5, height = 5)
bo8.grid(row = 4, column = 2, padx = 5, pady = 5)

bo9 = Button(root, width = 5, height = 5)
bo9.grid(row = 4, column = 3, padx = 5, pady = 5)

turnl = Label(root, text = 'Player ' + str(turn) + ' turn',font = ("Arial", 20))
turnl.grid(row = 5, column = 2, padx = 10, pady = 10)

root.mainloop()
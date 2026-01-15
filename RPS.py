from tkinter import *

root = Tk()
root.geometry("700x300")
root.title("Rock Paper Scissors")

playerscore = 0
computerscore = 0
options = [('Rock', 0), ('Paper', 1), ('Scissors', 2)]

def compwins():
    global playerscore, computerscore
    computerscore += 1
    wins.config(text = "!Computer Won!")

rpsl = Label(root, text = "Rock Paper Scissors")
rpsl.grid(row = 1, column = 3)

wins = Label(root, text = "Lets Start the Game", fg = "green")
wins.grid(row = 2, column = 3)

optl = Label(root, text = "Your Options:")
optl.grid(row = 3, column = 1)

rockb = Button(root, text = "Rock")
rockb.grid(row = 3, column = 2)

paperb = Button(root, text = "Paper")
paperb.grid(row = 3, column = 3)

scisb = Button(root, text = "Sissors")
scisb.grid(row = 3, column = 4)

scrl = Label(root, text = "Score")
scrl.grid(row = 4, column = 1)

url = Label(root, text = "Your Score:")
url.grid(row = 5, column = 2)

compl = Label(root, text = "Computer Score:")
compl.grid(row = 6, column = 2)



root.mainloop()
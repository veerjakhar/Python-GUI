from tkinter import *
import random

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
    computersc.config(text = "Computer Score: " + str(computerscore))
    playersc.config(text = "Your Score: " + str(playerscore))

def playerwins():
    global playerscore, computerscore
    playerscore += 1
    wins.config(text = "!Player Won!")
    computersc.config(text = "Computer Score: " + str(computerscore))
    playersc.config(text = "Your Score: " + str(playerscore))

def tiechange():
    global playerscore, computerscore
    wins.config(text = "!It's a Tie!")
    computersc.config(text = "Computer Score: " + str(computerscore))
    playersc.config(text = "Your Score: " + str(playerscore))

def playerchoice(player_input):
    global playerscore, computerscore
    print(player_input)
    computer_input = get_computer_choice()
    print(computer_input)
    ursel.config(text = "You Seleceted: " + player_input[0])
    compsl.config(text = "Computer Selected: " + computer_input[0])
    if (player_input == computer_input):
        tiechange()

    # If the Player has Choosen Rock
    if (player_input[1] == 0):
        if (computer_input[1] == 1):
            compwins()
        elif (computer_input[1] == 2):
            playerwins()
    # If the Player has Choosen Paper
    elif (player_input[1] == 1):
        if (computer_input[1] == 0):
            playerwins()
        elif (computer_input[1] == 2):
            compwins()
    # If the Player has Choosen Scissors
    elif (player_input[1] == 2):
        if (computer_input[1] == 0):
            compwins()
        elif (computer_input[1] == 1):
            playerwins()

def get_computer_choice():
    return random.choice(options)

rpsl = Label(root, text = "Rock Paper Scissors")
rpsl.pack()

wins = Label(root, text = "Lets Start the Game", fg = "green")
wins.pack()

inputf = Frame(root)
inputf.pack()

optl = Label(inputf, text = "Your Options:")
optl.grid(row = 0, column = 0, pady = 8)

rockb = Button(inputf, text = "Rock", width = 15, bd = 0, pady = 5, command = lambda: playerchoice(options[0]))
rockb.grid(row = 1, column = 1, padx = 8, pady = 5)

paperb = Button(inputf, text = "Paper", width = 15, bd = 0, pady = 5, command = lambda: playerchoice(options[1]))
paperb.grid(row = 1, column = 2, padx = 8, pady = 5)

scisb = Button(inputf, text = "Scissors", width = 15, bd = 0, pady = 5, command = lambda: playerchoice(options[2]))
scisb.grid(row = 1, column = 3, padx = 8, pady = 5)

scrl = Label(inputf, text = "Score:")
scrl.grid(row = 2, column = 0)

ursel = Label(inputf, text = "You Selected:")
ursel.grid(row = 3, column = 1)

compsl = Label(inputf, text = "Computer Selected:")
compsl.grid(row = 4, column = 1)

playersc = Label(inputf, text = "Player Score:")
playersc.grid(row = 3, column = 2)

computersc = Label(inputf, text = "Computer Score:")
computersc.grid(row = 4, column = 2)

root.mainloop()
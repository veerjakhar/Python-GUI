from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("Heads N' Tails")
root.geometry("500x500")

def whattodo():
    numbered = random.randint(1, 3)
    if numbered == 1:
        messagebox.showinfo('showinfo', "Its Heads!")
    if numbered == 2:
        messagebox.showinfo('showinfo', "Its Tails!")

toss = Label(root, text = "Heads or Tails")
toss.pack()

flippy = Button(root, text = "!Flip the Coin!", command = whattodo)
flippy.pack()

decider = Label(root, text = "FLIP IT UP")
decider.pack()

root.mainloop()
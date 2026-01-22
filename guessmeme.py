from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.title("-Guess the Number-")
root.geometry("500x400")

numbered = random.randint(1, 10)

def buttonkk():
    player_name = name.get()
    messagebox.showinfo('showinfo', "Hello " + player_name + ", I am think of a number between 1 and 20, can you guess what it is?")

def buttongg():
    global numbered
    numberged = numberg.get()
    if numbered > numberged:
        messagebox.showerror('showerror', 'The number choosen is larger')


welec = Label(root, text = "Welcome to our game!")
welec.pack() 

what = Label(root, text = "What is your Name?")
what.place(x = 10, y = 60)

name = Entry(root)
name.place(x = 10, y = 90)

nameb = Button(root, text = "Okay", command = buttonkk)
nameb.place(x = 400, y = 90)

take = Label(root, text = "Take a guess on what the number could be:")
take.place(x = 10, y = 130)

numberg = Entry(root)
numberg.place(x = 10, y = 160)

guessb = Button(root, text = "Guess", command = buttongg)
guessb.place(x = 400, y = 160)

root.mainloop()
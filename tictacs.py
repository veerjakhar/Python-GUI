from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("350x400")

turn = 1
result = ""

def winf():
    global result
    if bo1.cget('text') == bo2.cget('text') == bo3.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo1.cget('text') == bo2.cget('text') == bo3.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo4.cget('text') == bo5.cget('text') == bo6.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo4.cget('text') == bo5.cget('text') == bo6.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo7.cget('text') == bo8.cget('text') == bo9.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo7.cget('text') == bo8.cget('text') == bo9.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo1.cget('text') == bo4.cget('text') == bo7.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo1.cget('text') == bo4.cget('text') == bo7.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo2.cget('text') == bo5.cget('text') == bo8.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo2.cget('text') == bo5.cget('text') == bo8.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo3.cget('text') == bo6.cget('text') == bo9.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo3.cget('text') == bo6.cget('text') == bo9.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo1.cget('text') == bo5.cget('text') == bo9.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo1.cget('text') == bo5.cget('text') == bo9.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo3.cget('text') == bo5.cget('text') == bo7.cget('text') == 'X':
        result = 'Player 1 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()
    elif bo3.cget('text') == bo5.cget('text') == bo7.cget('text') == 'O':
        result = 'Player 2 Wins'
        messagebox.showinfo('Result', str(result))
        wait(3)
        root.destroy()

def bo1click():
    global turn
    texts = bo1.cget("text")
    if texts == '':
        if turn == 1:
            bo1.config(text = 'X')
            turn = 2
        else:
            bo1.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo2click():
    global turn
    texts = bo2.cget("text")
    if texts == '':
        if turn == 1:
            bo2.config(text = 'X')
            turn = 2
        else:
            bo2.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo3click():
    global turn
    texts = bo3.cget("text")
    if texts == '':
        if turn == 1:
            bo3.config(text = 'X')
            turn = 2
        else:
            bo3.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo4click():
    global turn
    texts = bo4.cget("text")
    if texts == '':
        if turn == 1:
            bo4.config(text = 'X')
            turn = 2
        else:
            bo4.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo5click():
    global turn
    texts = bo5.cget("text")
    if texts == '':
        if turn == 1:
            bo5.config(text = 'X')
            turn = 2
        else:
            bo5.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo6click():
    global turn
    texts = bo6.cget("text")
    if texts == '':
        if turn == 1:
            bo6.config(text = 'X')
            turn = 2
        else:
            bo6.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo7click():
    global turn
    texts = bo7.cget("text")
    if texts == '':
        if turn == 1:
            bo7.config(text = 'X')
            turn = 2
        else:
            bo7.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo8click():
    global turn
    texts = bo8.cget("text")
    if texts == '':
        if turn == 1:
            bo8.config(text = 'X')
            turn = 2
        else:
            bo8.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()

def bo9click():
    global turn
    texts = bo9.cget("text")
    if texts == '':
        if turn == 1:
            bo9.config(text = 'X')
            turn = 2
        else:
            bo9.config(text = 'O')
            turn = 1
    turnl.config(text = 'Player ' + str(turn) + ' turn')
    winf()




bo1 = Button(root, width = 5, height = 5, command = bo1click)
bo1.grid(row = 2, column = 1, padx = 5, pady = 5)

bo2 = Button(root, width = 5, height = 5, command = bo2click)
bo2.grid(row = 2, column = 2, padx = 5, pady = 5)

bo3 = Button(root, width = 5, height = 5, command = bo3click)
bo3.grid(row = 2, column = 3, padx = 5, pady = 5)

bo4 = Button(root, width = 5, height = 5, comman = bo4click)
bo4.grid(row = 3, column = 1, padx = 5, pady = 5)

bo5 = Button(root, width = 5, height = 5, command = bo5click)
bo5.grid(row = 3, column = 2, padx = 5, pady = 5)

bo6 = Button(root, width = 5, height = 5, command = bo6click)
bo6.grid(row = 3, column = 3, padx = 5, pady = 5)

bo7 = Button(root, width = 5, height = 5, command = bo7click)
bo7.grid(row = 4, column = 1, padx = 5, pady = 5)

bo8 = Button(root, width = 5, height = 5, command = bo8click)
bo8.grid(row = 4, column = 2, padx = 5, pady = 5)

bo9 = Button(root, width = 5, height = 5, command = bo9click)
bo9.grid(row = 4, column = 3, padx = 5, pady = 5)

turnl = Label(root, text = 'Player ' + str(turn) + ' turn',font = ("Arial", 20))
turnl.grid(row = 5, column = 2, padx = 10, pady = 10)

root.mainloop()
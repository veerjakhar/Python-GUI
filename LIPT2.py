from tkinter import *

top = Tk()
top.title("Login")
top.config(background = "red")
top.geometry("450x300")

# Create A Label
username = Label(top, text = "Username").place(x = 40, y = 60)
password = Label(top, text = "Password").place(x = 40, y = 100)
sub = Button(top, text = "Submit").place(x = 40, y = 140)
usernameput = Entry(top, width = 30).place(x = 140, y = 60)
passwordput = Entry(top, show = '*', width = 30).place(x = 140, y = 100)
top.mainloop()

from tkinter import *

root = Tk()
root.geometry("150x200")
root.title("Frame")

hello = Label(root, text = "HelloHello", font = "50")
hello.pack()

scrolling = Scrollbar(root)
scrolling.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrolling.set)
for line in range (1, 26):
    mylist.insert(END, "Hi " + str(line))
mylist.pack(side = LEFT, fill = BOTH)

scrolling.config(command = mylist.yview)

root.mainloop()

from tkinter import *

root = Tk()
root.geometry("300x150")
root.title("Frame")

choco = Label(root, text = "Chocos and Ice Creams", font = "50")
choco.pack()

frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

listbox = Listbox(root, height = 10, width = 15, bg = "grey", activestyle = "dotbox", font = "helvetica", fg = "orange")

B1_button = Button(root, text = "Choco", fg = "red", bg = "beige")
B1_button.pack(side = LEFT)

B2_button = Button(root, text = "Dark Choco", fg = "brown", bg = "beige")
B2_button.pack(side = LEFT)

B3_button = Button(root, text = "White  Choco", fg = "blue", bg = "beige")
B3_button.pack(side = LEFT)

fooditems = Label(root, text = "FOOD ITEMS")
# Insert Elements By Their Index And Names
listbox.insert(1, "Nachos")
listbox.insert(2, "Pizza")
listbox.insert(3, "Burrito")
listbox.insert(4, "Burger")
listbox.insert(5, "Fire")

fooditems.pack()
listbox.pack()

hello = Label(root, text = "HelloHello", font = "50")
hello.pack()

scrolling = Scrollbar(root)
scrolling.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand = scrolling.set)
for line in range (1, 26):
    mylist.insert(END, "Hi " + str(line))
mylist.pack(side = LEFT, fill = BOTH)

scrolling.config(command = mylist.yview)

B4_button = Button(root, text = "Pastry", fg = "green", bg = "yellow")
B4_button.pack(side = BOTTOM)

B5_button = Button(root, text = "Cake", fg = "green", bg = "pink")
B5_button.pack(side = BOTTOM)

B6_button = Button(root, text = "Tiramisu", fg = "green", bg = "cyan")
B6_button.pack(side = BOTTOM)

root.mainloop()

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Timer")
root.geometry("360x200")

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")

hours = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = hours)
hours.place(x = 100, y = 60)

mins = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = minutes)
mins.place(x = 150, y = 60)

secs = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = seconds)
secs.place(x = 200, y = 60)

timers = Button(root, text = "Start Timer")
timers.place(x = 120, y = 100)

root.mainloop()
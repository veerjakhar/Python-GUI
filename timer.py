from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox

root = Tk()
root.title("Timer")
root.geometry("360x200")

hours = StringVar()
minutes = StringVar()
seconds = StringVar()

hours.set("00")
minutes.set("00")
seconds.set("00")

def submit():
    try:
        temp = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
    except ValueError:
        print("Please input the right value")
        return
    while temp >= 0:
        mins, secs = divmod(temp, 60)
        hurs = 00
        if mins > 59:
            hurs, mins = divmod(mins, 60)
            hours.set("{:02d}".format(hurs))
            minutes.set("{:02d}".format(mins))
            seconds.set("{:02d}".format(secs))
            root.update()
            time.sleep(1)
        if temp == 0:
            messagebox.showinfo('showinfo', "Time Countdown, Times Up")
            break
        temp -= 1


hourse = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = hours)
hourse.place(x = 100, y = 60)

minse = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = minutes)
minse.place(x = 150, y = 60)

secse = Entry(root, width = 3, font = ("Arial", 18, ""), textvariable = seconds)
secse.place(x = 200, y = 60)

timers = Button(root, text = "Start Timer", command = submit)
timers.place(x = 120, y = 100)

root.mainloop()
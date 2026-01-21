from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

running = False
seconds = 0

def start():
    global running
    if not running:
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global running, seconds
    lbl.config(text = "00:00")
    running = False
    seconds = 0

def update_time():
    global seconds
    if running: 
        seconds += 1
        min, sec = divmod(seconds, 60)
        lbl.config(text = f"{min:02d}: {sec:02d}")
        root.after(1000, update_time)

# Styling the Label Widgit
lbl = Label(root, text = "00:00", font = ('calibri', 40, 'bold'), foreground = 'orange')
lbl.pack()

bss = Button(root, text = "Start Stopwatch", command = start)
bss.pack()

bsss = Button(root, text = "Stop Stopwatch", command = stop)
bsss.pack()

bsr = Button(root, text = "Reset Stopwatch", command = reset)
bsr.pack()

root.mainloop()
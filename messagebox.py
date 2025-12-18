from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

# Importing Askopenfile Function From Class Filedialog
from tkinter.filedialog import askopenfile
 
root = Tk()
root.geometry('200x100')

def save():
    files = [('All Files', '*.*'), ('Python files', '*.py'), ('text document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = files)


def open_file():
    file = askopenfile(mode = 'r', filetypes = [('python files', '*.py')])
    if file is not None:
        content = file.read()
        print(content)

btn = Button(root, text = "Open", command = lambda: open_file())
btn.pack(side = TOP, pady = 10)
btn2 = Button(root, text = "Save", command = lambda: save())
btn2.pack(side = TOP, pady = 20)

w = Label(root, text = 'I am a Message box', font = "50")
w.pack()

messagebox.showinfo("showinfo", "the next message is lying")
messagebox.showwarning("showwaring", "the message before is an error")
messagebox.showerror("showerror", "I am an error box and the message after is continued from the message before")
messagebox.askquestion("askquestion", "Is it?")
messagebox.askokcancel("askokcancel", "Do you retake the previous question")
messagebox.askyesno("askyesno", "Are you sure")
messagebox.askretrycancel("askretrycancel", "Please DO IT")

root.mainloop()
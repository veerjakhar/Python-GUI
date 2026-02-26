from tkinter import *
from gtts import gTTS
import os
import speech_recognition as sr
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *
import tkinter as tk

root = Tk()
root.title("Text to Speech Converter")
root.geometry('750x500')

frame1 = Frame(root, height = "150")
frame1.pack(fill = X)

titlelb = Label(frame1, text = "Text to Speech", font = "Arial, 20")
titlelb.place(x = 275, y = 70)

def play():
    language = "en"
    myobj = gTTS(text = tentry.get(), lang = language, slow = False)
    myobj.save("Convert.mp3")
    os.system("afplay convert.mp3")




frame2 = Frame(root, height = "750")
frame2.pack(fill = X)

tentry = Entry(frame2, width = 45, font = 14)
tentry.place(x = 130, y = 52)

subutton = Button(frame2, text = "Submit", width = 20, command = play)
subutton.place(x = 250, y = 100)

sentry = Entry(frame2, width = 45, font = 14)
sentry.place(x = 130, y = 200)

textutton = Button(frame2, text = "Click on me to start recording", width = 20, )
textutton.place(x = 250, y = 152)

textutton = Button(frame2, text = "Save the recording", width = 20, )
textutton.place(x = 250, y = 252)

root.mainloop()



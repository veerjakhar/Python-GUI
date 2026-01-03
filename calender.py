from tkinter import *
import calendar

def show_cal():
    newGUI = Tk()
    newGUI.geometry('400x450')
    newGUI.title('CALENDAR')
    newGUI.config(background = 'white')

    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(newGUI, text = cal_content, font = 'Consolas 10 bold')
    cal_year.grid(row = 5, column = 1)

    newGUI.mainloop()

if __name__ == "__main__":
    GUI = Tk()
    GUI.geometry('250x140')
    GUI.title("CALENDAR")
    GUI.config(background = 'white')
    cal = Label(GUI, text = "CALENDAR", bg = "dark gray", font = ('times', 28, 'bold'))
    year = Label(GUI, text = "Enter Year", bg = 'light green')
    year_field = Entry(GUI)
    show = Button(GUI, text = "Show Calendar", fg = 'black', bg = 'red', command = show_cal)
    Exit = Button(GUI, text = "Exit", fg = 'black', bg = 'red', command = exit)

    cal.grid(row = 1, column = 1)
    year.grid(row = 2, column = 1)
    year_field.grid(row = 3, column = 1)
    show.grid(row = 4, column = 1)
    Exit.grid(row = 6, column = 1)

    GUI.mainloop()




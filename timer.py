import time
from tkinter import *
from tkinter import messagebox

### Create interface object
clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.title("Countdown Timer")
clockWindow.configure(background='dark grey')


### Declare variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()


### Set strings to a default value
hourString.set("00")
minuteString.set("00")
secondString.set("00")


### Get user input
hourTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=hourString)
minuteTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=minuteString)
secondTextbox = Entry(clockWindow, width=3, font=("Calibri", 20, ""), textvariable=secondString)


### Center textboxes
hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)


def runTimer():
    try:
        clockTime = int(hourString.get()*3600) + int(minuteString.get()*60) + int(secondString.get())
        

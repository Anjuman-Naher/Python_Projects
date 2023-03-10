
from tkinter import *
from tkinter.ttk import *
import datetime

root = Tk()
root.title("Clock")

def clock():
    date_time: str = datetime.datetime.now().strftime("%A,%d-%b-%Y")
    date_label.config(text=date_time)
    date_time: str = datetime.datetime.now().strftime("%I:%M:%S %p")
    time_label.config(text=date_time)
    time_label.after(1000, clock)

time_label = Label(root, font=("ds-digital", 60), background="white", foreground="black")
time_label.pack(anchor="center")
date_label = Label(root, font=("Chivo-Mono", 40), background="white", foreground="black")
date_label.pack(anchor="center")



clock()

mainloop()
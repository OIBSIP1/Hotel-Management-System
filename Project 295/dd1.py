from tkinter import *
from tkcalendar import Calendar,DateEntry

root=Tk()
root.geometry('400x500')

def show():
    s=cal.get()
    print(s)
cal=DateEntry(root,width=30,bg='darkblue',fg='white')

cal.grid()
root.mainloop()
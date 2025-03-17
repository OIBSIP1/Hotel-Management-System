import tkinter
from time import strftime
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import LabelFrame
from PIL import Image,ImageTk





top = tk.Tk()
top.geometry('1500x800')

def registration():
    top.destroy()
    import two

def bookings():
    top.destroy()
    import three

def records():
    top.destroy()
    import four

def exit():
    top.destroy()

def time():
    string=strftime('%H:%M:%S %p')
    l77.config(text=string,bg='tan')
    l77.after(1000, time)

path=r"C:\Users\hp\Downloads\resized_hotel_image_1500x1000.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.pack()





l77=Label(top,bg='white',fg='black',font=('Arial 20 bold'))
l77.place(x=1100,y=15)
time()

#f2=Frame(top,height=50,width=2000,bg='tan',highlightbackground='black',highlightthickness=1)
#f2.place(x=0,y=60)

#f3=Frame(top,height=1500,width=2000,bg='white')
#f3.place(x=0,y=150)



l=Label(top,text='HOTEL  MANAGEMENT  SYSTEM',fg='black',bg='tan',font=('Arial 36'))
l.place(x=250,y=7)










b1=Button(top,text='  REGISTRATION  ',bg='tan',font=('Arial 15'),highlightbackground='black',highlightthickness=1
          ,command=registration)
b1.place(x=0,y=70)
b2=Button(top,text='  BOOKINGS  ',bg='tan',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=bookings)
b2.place(x=190,y=70)
b3=Button(top,text='  RECORDS  ',bg='tan',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=records)
b3.place(x=340,y=70)

b5=Button(top,text='   EXIT    ',bg='tan',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=exit)
b5.place(x=482,y=70)


top.mainloop()
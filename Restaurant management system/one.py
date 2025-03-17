from tkinter import *
import  tkinter as tk
from  PIL import Image,ImageTk
from time import strftime

top=tk.Tk()
top.geometry('1500x800')

def DINE_IN():
    top.destroy()
    import extra

def take_away():
    top.destroy()
    import login



path=r"C:\Users\hp\Downloads\resized_restaurant_image_1500x1000.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.pack()

def time():
    string=strftime('%H:%M:%S %p')
    l77.config(text=string,bg='tan')
    l77.after(1000,time)


def date():
    string=strftime("%d/%m/%Y  %A")
    l78.config(text=string, bg='tan')

label =tk.Label(top, text="   Welcome to Our Restaurant   ", font=("Helvetica", 30, "bold"),
                  fg="brown",bg='tan')
label.place(relx=0.5,rely=0.06,anchor='center')

l77=Label(top,fg='black',font=('Arial 20 bold'))
l77.place(x=970,y=95)
time()

l78=Label(top,fg='black',font=('Arial 20 bold'))
l78.place(x=970,y=145)
date()
b1=Button(top,text='  DINE IN  ',fg='black',bg='tan',font=('Arial 20 bold'),command=DINE_IN )
b1.place(x=0,y=150)
b2=Button(top,text='  TAKE AWAY  ',fg='black',bg='tan',font=('Arial 20 bold'),command=take_away)
b2.place(x=0,y=220)

top.mainloop()
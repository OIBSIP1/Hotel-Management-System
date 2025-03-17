from tkinter import *
import tkinter as tk
from PIL import Image , ImageTk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import LabelFrame

top=tk.Tk()
top.geometry('1500x800')

def sign_in():
    username = e1.get()
    password = e2.get()

    if username == "ADMIN" and password == "ADMIN@123":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
        top.destroy()
        import one
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password.")




path=r"C:\Users\hp\Downloads\hotel_login_background_1100x600.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.pack()

f1 =Frame(top, bg='tan', height=430,width=450,bd=2)
f1.place(x=450, y=160)

l2=Label(f1,text='Login',fg='black',bg='tan',font=('Arial 20 bold'),relief='raised',bd=6)
l2.place(x=170,y=0)

l3=Label(f1,text='User Name   :-',fg='black',bg='tan',font=('Arial 15 bold'))
l3.place(x=30,y=110)

e1=Entry(f1,width=15,font=('Arial 15 '))
e1.place(x=200,y=116)

l4=Label(f1,text='Password     :-',fg='black',bg='tan',font=('Arial 15 bold'))
l4.place(x=30,y=180)

e2=Entry(f1,width=15,font=('Arial 15 '))
e2.place(x=200,y=186)

b1=Button(f1,text=' SIGN IN ',fg='black',bg='white',font=('Arial 15 bold'),command=sign_in)
b1.place(x=170,y=250)

top.mainloop()

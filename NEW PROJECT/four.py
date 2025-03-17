from cgitb import reset
from datetime import datetime
from math import floor
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import LabelFrame
from PIL import Image,ImageTk
from time import strftime
from new import update, delete
import tkinter as tk

top = Tk()
top.geometry('1500x800')
canvas = Canvas(top, width=1500, height=650)
canvas.pack()

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

path=r"C:\Users\hp\Downloads\hotel_terrace_resized_1000x600.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

# Add the text on top of the image
canvas.create_text(725, 40, text='HOTEL MANAGEMENT SYSTEM', font=('Arial 30 bold'), fill='gray95')

def time():
    string=strftime('%H:%M:%S %p')
    l77.config(text=string,bg='white')
    l77.after(1000, time)



def insert():
    customer_contact=int(e4.get())
    floor_no=int(e1.get())
    room_no=int(e2.get())
    room_type=cb1.get()


    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s ="""
       INSERT INTO emp2 (customer_contact,floor_no, room_no,room_type)
       VALUES (%s, %s, %s,%s)
       """
    result=cur.execute(s, (customer_contact,floor_no,room_no,room_type))
    db.commit()
    if (result > 0):
        messagebox.showinfo("Result", "Record insert successfully")
    else:
        messagebox.showinfo("Result", "Record not inserted")
    db.commit()
    e4.delete(0,"end")
    e1.delete(0,"end")
    e2.delete(0, "end")
    cb1.set('select')


def reset():
    # Clear all entry fields
    e4.delete(0,"end")
    e1.delete(0, "end")
    e2.delete(0, "end")
    cb1.set('select')

    for item in tv.get_children():
        tv.delete(item)

    messagebox.showinfo("Reset", "All fields have been cleared!")

def delete():
    customer_contact=e4.get()
    import pymysql as sql
    db= sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s="delete from emp2 where customer_contact=%s"
    result = cur.execute(s,(customer_contact,))
    if (result > 0):
        messagebox.showinfo("Result", "Record delete successfully")
    else:
        messagebox.showinfo("Result", "Record not deleted ")
    db.commit()


def update():
    k4=int(e4.get())
    k = int(e1.get())
    k2 = int(e2.get())
    k3 = cb1.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "update emp2 set floor_no=%s,room_no=%s,room_type=%s where customer_contact=%s"
    t=(k,k2,k3,k4)
    result=cur.execute(s,t)
    if (result > 0):
        messagebox.showinfo("Result", "Record update successfully")
    else:
        messagebox.showinfo("Result", "Record not updated")
    db.commit()


def show():
    for i in tv.get_children():
        tv.delete(i )

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "select * from emp2"
    v = cur.execute(s, )
    result = cur.fetchall()
    if (v > 0):
        for col in result:
            customer_contact=col[0]
            Floor_no= col[1]
            Room_No = col[2]
            Room_type = col[3]

            tv.insert("",'end',
            values=(customer_contact,Floor_no,Room_No,Room_type))

    else:
        messagebox.showinfo("result", 'Record not found')

#f1=Frame(top,height=70,width=2000,bg='tan')
#f1.place(x=0,y=0)

#f4=Frame(top,height=80,width=2000,bg='tan')
#f4.place(x=0,y=110)

l77=Label(top,bg='white',fg='black',font=('Arial 20 bold'))
l77.place(x=1100,y=15)
time()



f2=LabelFrame(top,text='New Room Add',height=330,width=450)
f2.place(x=0,y=200)


f3=LabelFrame(top,text='Room Records',height=330,width=802,)
f3.place(x=455,y=200)

tv = ttk.Treeview(top,height=14)
tv['columns']=('Customer Contact','Floor No', 'Room No','Room Type')
tv.column('#0', width=0, stretch=NO)
tv.column('Customer Contact', anchor=CENTER, width=200)
tv.column('Floor No', anchor=CENTER, width=200)
tv.column('Room No', anchor=CENTER, width=200)
tv.column('Room Type', anchor=CENTER, width=200)

tv.heading('Customer Contact', text='Customer Contact', anchor=CENTER)
tv.heading('Floor No', text='Floor No', anchor=CENTER)
tv.heading('Room No', text='Room No', anchor=CENTER)
tv.heading('Room Type', text='Room Type', anchor=CENTER)
tv.place(x=455,y=230)




#l=Label(f1,text='HOTEL  MANAGEMENT  SYSTEM',fg='black',bg='tan',font=('Arial 35'))
#l.place(x=250,y=7)

l4=Label(f2,text='Customer Contact :-',font=('Arial 10 bold'))
l4.place(x=10,y=10)

e4=Entry(top,fg='black',font=('Arial 10 bold'),width=20)
e4.place(x=150,y=227)

l1=Label(f2,text='Floor No :-',font=('Arial 10 bold'))
l1.place(x=10,y=45)

e1=Entry(top,fg='black',font=('Arial 10 bold'),width=20)
e1.place(x=150,y=260)


l2=Label(f2,text='Room No :-',font=('Arial 10 bold'))
l2.place(x=10,y=80)

e2=Entry(top,fg='black',font=('Arial 10 bold'),width=20)
e2.place(x=150,y=300)


l3=Label(f2,text='Room Type  :-',font=('Arial 10 bold'))
l3.place(x=10,y=120)

cb1=ttk.Combobox(top,value=["Select","Single","Double","Family"],font=('arial 10 bold'),width=20)
cb1.set("Select")
cb1.place(x=150,y=340)
cb1.current(0)






l=Label(top,text='ROOM RECORDS DETAILS',fg='black',font=('Arial 25'))
l.place(x=400,y=120)

b8=Button(top,text='Insert',bg='tan',fg='black',font=('Arial 12'),width=10,height=1,command=insert)
b8.place(x=10,y=400)

b9=Button(top,text='Update',bg='tan',fg='black',font=('Arial 12'),width=10,height=1,command=update)
b9.place(x=120,y=400)
b10=Button(top,text='Delete',bg='tan',fg='black',font=('Arial 12'),width=10,height=1,command=delete)
b10.place(x=230,y=400)

b11=Button(top,text='Reset',bg='tan',fg='black',font=('Arial 12'),width=10,height=1,command=reset)
b11.place(x=340,y=400)

b12=Button(top,text="show",bg='tan',fg='black',font=('Arial 12'),width=10,height=1,command=show)
b12.place(x=160,y=450)
b1=Button(top,text='  REGISTRATION  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1
          ,command=registration)
b1.place(x=0,y=70)
b2=Button(top,text='  BOOKINGS  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=bookings)
b2.place(x=180,y=70)
b3=Button(top,text='  RECORDS  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=records)
b3.place(x=320,y=70)

b5=Button(top,text='   EXIT    ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=exit)
b5.place(x=450,y=70)

top.mainloop()

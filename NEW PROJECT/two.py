from cgitb import reset
from datetime import datetime
from tkinter import *
from tkinter import messagebox, Label
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.ttk import LabelFrame
import tkinter as tk
import pymysql
from time import strftime

from PIL import Image,ImageTk

from new import insert, update, delete,show



top = Tk()
top.geometry('1500x800')

canvas = Canvas(top, width=1500, height=650)
canvas.pack()






path=r"C:\Users\hp\Downloads\resized_garden_hotel.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
#l1=tk.Label(top,image=img)
#l1.pack()
canvas.create_image(0, 0, anchor=NW, image=img)

# Add the text on top of the image
canvas.create_text(750, 30, text='HOTEL MANAGEMENT SYSTEM', font=('Arial 38 bold'), fill='gray95')






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







#def time():
    #string=strftime('%H:%M:%S %p')
    #l77.config(text=string,bg='tan')
    #l77.after(1000, time)


def insert():

    ref_no=int(e1.get())
    name=e2.get()
    mother_name=e3.get()
    gender=cb3.get()
    mobile=int(e5.get())
    email=e6.get()
    nationality=cb1.get()
    id_proof=cb2.get()
    id_number=int(e9.get())
    address=e10.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s ="""
       INSERT INTO emp (ref_no, name, mother_name, gender, mobile, email, nationality, id_proof, id_number, address)
       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
       """
    result=cur.execute(s, (ref_no, name, mother_name, gender, mobile, email, nationality, id_proof, id_number, address))
    db.commit()
    if (result > 0):
        messagebox.showinfo("Result", "Record insert successfully")
    else:
        messagebox.showinfo("Result", "Record not inserted")
    db.commit()
    e1.delete(0,"end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    cb3.set('Select')
    e5.delete(0, "end")
    e6.delete(0, "end")
    cb1.set('Select')
    cb2.set('Select')
    e9.delete(0,"end")
    e10.delete(0,"end")

def update():
    k = int(e1.get())
    k1 = e2.get()
    k3 = e3.get()
    k4 = cb3.get()
    k5 = int(e5.get())
    k6 = e6.get()
    k7= cb1.get()
    k8 = cb2.get()
    k9 = int(e9.get())
    k10 = e10.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "update emp set name=%s,mother_name=%s,gender=%s,mobile=%s,email=%s,nationality=%s,id_proof=%s,id_number=%s,address=%s where ref_no=%s"
    t = (k1,k3,k4,k5,k6,k7,k8,k9,k10,k)
    result = cur.execute(s, t)
    if (result > 0):
            messagebox.showinfo("Result", "Record update successfully")
    else:
            messagebox.showinfo("Result", "Record not updated")
    db.commit()







def delete():
    ref_no=e1.get()
    import pymysql as sql
    db= sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s="delete from emp where ref_no=%s"
    result = cur.execute(s,ref_no)
    if (result > 0):
        messagebox.showinfo("Result", "Record delete successfully")
    else:
        messagebox.showinfo("Result", "Record not deleted inserted")
    db.commit()


def search():
    for i in tv.get_children():
        tv.delete(i )
    criteria=cb.get()
    k1=e11.get()


    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    if criteria == 'Ref No':
        s = "SELECT * FROM emp WHERE ref_no=%s"
    elif criteria == 'Name':
        s = "SELECT * FROM emp WHERE name LIKE %s"
        search_value = f"%{k1}%"  # Use LIKE for partial name matches
    elif criteria == 'Mobile No':
        s = "SELECT * FROM emp WHERE mobile=%s"
    elif criteria == 'Email Id':
        s = "SELECT * FROM emp WHERE email LIKE %s"
        search_value = f"%{k1}%"
    else:  # If 'Select by' is chosen
        messagebox.showwarning("Input Error", "Please select a valid search criteria.")
        return

        # Execute the query with the appropriate parameter
    v = cur.execute(s, (k1,))
    result = cur.fetchall()

    # Display search results
    for col in result:
        ref_no = col[0]
        name = col[1]
        mother_name = col[2]
        gender = col[3]
        mobile = col[4]
        email = col[5]
        nationality = col[6]
        id_proof = col[7]
        id_number = col[8]
        address = col[9]
        tv.insert("", 'end',
                  values=(ref_no, name, mother_name, gender, mobile, email, nationality, id_proof, id_number, address))

    # Handle case when no records are found
    if len(result) == 0:
        messagebox.showinfo("Search Results", "No records found for the given search criteria.")


def show():
    for i in tv.get_children():
        tv.delete(i )
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "select * from emp"
    v = cur.execute(s, )
    result = cur.fetchall()
    if (v > 0):
        for col in result:
            ref_no= col[0]
            name = col[1]
            mother_name = col[2]
            gender = col[3]
            mobile = col[4]
            email = col[5]
            nationality= col[6]
            id_proof = col[7]
            id_number = col[8]
            address = col[9]
            tv.insert("",'end',
            values=(ref_no,name,mother_name,gender,mobile,email,nationality,id_proof,id_number,address))
            #print(name, lastname, age, password, contact)
    else:
        messagebox.showinfo("result", 'Record not found')

def reset():
    # Clear all entry fields
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e5.delete(0, "end")
    e6.delete(0, "end")
    e9.delete(0, "end")
    e10.delete(0,"end")  # If included for search functionality


    for item in tv.get_children():
        tv.delete(item)

    
    messagebox.showinfo("Reset", "All fields have been cleared!")
#f1=Frame(top,height=70,width=2000,bg='tan')
#f1.place(x=0,y=0)

#l=Label(f1,text='HOTEL  MANAGEMENT  SYSTEM',fg='black',bg='',font=('Arial 35'))
#l.place(x=250,y=7)







f4=Frame(top,height=45,width=505)
f4.place(x=350,y=120)


#l77=Label(f1,bg='white',fg='black',font=('Arial 20 bold'))
#l77.place(x=1100,y=15)
#time()


f2=LabelFrame(top,text='Customer Details',height=560,width=450)
f2.place(x=0,y=185)
f3=LabelFrame(top,text='Search System',height=100,width=815,)
f3.place(x=455,y=185)

tv = ttk.Treeview(top,height=16)
tv['columns']=('Ref No', 'Name','Mothers Name','Gender','Mobile No','Email Id','Nationality','Id Proof','Id Number','Address')
tv.column('#0', width=0, stretch=NO)
tv.column('Ref No', anchor=CENTER, width=60)
tv.column('Name', anchor=CENTER, width=70)
tv.column('Mothers Name', anchor=CENTER, width=90)
tv.column('Gender', anchor=CENTER, width=75)
tv.column('Mobile No', anchor=CENTER, width=75)
tv.column('Email Id', anchor=CENTER, width=75)
tv.column('Nationality', anchor=CENTER, width=70)
tv.column('Id Proof', anchor=CENTER, width=70)
tv.column('Id Number', anchor=CENTER, width=70)
tv.column('Address', anchor=CENTER, width=160)

tv.heading('Ref No', text='Ref No', anchor=CENTER)
tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Mothers Name', text='Mothers Name', anchor=CENTER)
tv.heading('Gender', text='Gender', anchor=CENTER)
tv.heading('Mobile No', text='Mobile No', anchor=CENTER)
tv.heading('Email Id', text='Email Id', anchor=CENTER)
tv.heading('Nationality', text='Nationality', anchor=CENTER)
tv.heading('Id Proof', text='Id Proof', anchor=CENTER)
tv.heading('Id Number', text='Id Number', anchor=CENTER)
tv.heading('Address', text='Address', anchor=CENTER)
tv.place(x=455,y=290)

l12=Label(f4,text='ADD CUSTOMER DETAILS',fg='black',bg='tan',font=('Arial 30'))
l12.place(x=0,y=0)

l1=Label(f2,text='Customer Ref  :-',font=('Arial 10 bold'))
l1.place(x=10,y=10)

e1=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e1.place(x=150,y=215)


l2=Label(f2,text='Customer Name  :-',font=('Arial 10 bold'))
l2.place(x=10,y=40)

e2=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e2.place(x=150,y=245)


l3=Label(f2,text='Mother Name  :-',font=('Arial 10 bold'))
l3.place(x=10,y=75)

e3=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e3.place(x=150,y=275)


l4=Label(f2,text='Gender :-',font=('Arial 10 bold'))
l4.place(x=10,y=110)
cb3=ttk.Combobox(top,value=["Select","Male","female","others"],font=('arial 10 bold'))
cb3.set("Select")
cb3.place(x=150,y=310)
cb3.current(0)




l5=Label(f2,text='Mobile No :-',font=('Arial 10 bold'))
l5.place(x=10,y=145)

e5=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e5.place(x=150,y=345)


l6=Label(f2,text='Email Id :-',font=('Arial 10 bold'))
l6.place(x=10,y=185)

e6=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e6.place(x=150,y=385)


l7=Label(f2,text='Nationality  :-',font=('Arial 10 bold'))
l7.place(x=10,y=225)


cb1=ttk.Combobox(top,value=['Select','American','Canadian','French','Germany','Iceland','Indian','Swedan','Others'],font=('arial 10 bold'))
cb1.set("Select")
cb1.place(x=150,y=425)
cb1.current(0)



l8=Label(f2,text='Id Proof Type  :-',font=('Arial 10 bold'))
l8.place(x=10,y=270)


cb2=ttk.Combobox(top,value=['Select','Aadhaar Card','Passport','Driving License','Pan Card','Birth Certificate','Others'],font=('arial 10 bold'))
cb2.set("Select")
cb2.place(x=150,y=470)
cb2.current(0)




l9=Label(f2,text='Id Number :-',font=('Arial 10 bold'))
l9.place(x=10,y=315)

e9=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e9.place(x=150,y=515)

l10=Label(f2,text='Address :-',font=('Arial 10 bold'))
l10.place(x=10,y=360)

e10=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e10.place(x=150,y=560)

l11=Label(f3,text='Search By  :-',font=('Arial 10 bold'),)
l11.place(x=10,y=55)

k=['Select by','Ref No','Name','Phone No','Email Id']
cb=ttk.Combobox(top,value=k,font=('arial 10 bold'),width=20)

cb.place(x=570,y=255)
cb.current(0)

e11=Entry(top,fg='black',font=('Arial 10 bold'),width=35)
e11.place(x=750,y=255)

b6=Button(top,text='Search',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=search)
b6.place(x=1015,y=250)

b7=Button(top,text='Show',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=show)
b7.place(x=1130,y=250)

b8=Button(top,text='Insert',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=insert)
b8.place(x=10,y=600)

b9=Button(top,text='Update',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=update)
b9.place(x=120,y=600)
b10=Button(top,text='Delete',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=delete)
b10.place(x=230,y=600)

b11=Button(top,text='Reset',bg='tan',fg='white',font=('Arial 12'),width=10,height=1,command=reset)
b11.place(x=340,y=600)

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
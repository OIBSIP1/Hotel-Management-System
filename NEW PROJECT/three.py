from datetime import datetime
from tkinter import *
import  tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import LabelFrame
from PIL import Image,ImageTk
from tkcalendar import calendar_,DateEntry
from time import strftime

top = Tk()
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
canvas = Canvas(top, width=1500, height=650)
canvas.pack()


path=r"C:\Users\hp\Downloads\hotel_room_1500x800.png"
img = Image.open(path)
img = img.resize((1500, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.pack()

canvas.create_image(0, 0, anchor=NW, image=img)

# Add the text on top of the image
canvas.create_text(725, 40, text='HOTEL MANAGEMENT SYSTEM', font=('Arial 30 bold'), fill='gray95')


#f1=Frame(top,height=70,width=2000,bg='tan')
#f1.place(x=0,y=0)

#l=Label(top,text='HOTEL  MANAGEMENT  SYSTEM',fg='black',bg='tan',font=('Arial 35'))
#l.place(x=250,y=7)


def time():
    string=strftime('%H:%M:%S %p')
    l77.config(text=string)
    l77.after(1000, time)


#f4=Frame(top,height=80,width=2000,bg='tan')
#f4.place(x=0,y=110)

l77=Label(top,bg='white',fg='black',font=('Arial 20 bold'))
l77.place(x=1100,y=15)
time()

def update_room_price(event):
    room_type = cb1.get()  # Get selected room type

    # Define room prices
    room_prices = {
        "Single": "1000 INR",  # Example price for Single room
        "Double": "1500 INR",  # Example price for Double room
        "Family": "2000 INR"   # Example price for Family room
    }

    # Update the label with the corresponding room price
    if room_type in room_prices:
       l6.config(text=room_prices[room_type])
    else:
        l6.config(text="Select Room Type")



def submit_data():
    customer_contact = int(e1.get())
    check_in_date = cal1.get()
    check_out_date = cal2.get()
    room_type=cb1.get()

    room_prices = {
        "Single": 1000,  # Price for Single room
        "Double": 1500,  # Price for Double room
        "Family": 2000  # Price for Family room
    }
    room_price = room_prices.get(room_type, 0)




    import  pymysql as sql

    db =sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    query = """
        INSERT INTO records (customer_contact, check_in_date, check_out_date,room_type,room_price)
        VALUES (%s, %s, %s,%s,%s)
    """
    result=cur.execute(query, (customer_contact, check_in_date, check_out_date,room_type,room_price))
    db.commit()
    if (result > 0):
        messagebox.showinfo("Result", "Record insert successfully")
    else:

        messagebox.showinfo("Success", "Record  not inserted successfully!")
    e1.delete(0, END)




    cb1.set('select')







def fetch_data():
    for i in tv.get_children():
        tv.delete(i)
    customer_contact=e1.get()

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "SELECT customer_contact, check_in_date, check_out_date, room_type , room_price FROM records WHERE customer_contact = %s"
    v = cur.execute(s,customer_contact )
    result = cur.fetchall()
    if (v > 0):
            for col in result:
                Customer_Contact = col[0]
                Check_in_Date = col[1]
                Check_out_date= col[2]
                Room_Type=col[3]
                Room_Price=col[4]


                tv.insert("", 'end',
                          values=(
                          Customer_Contact,Check_in_Date,Check_out_date,Room_Type,Room_Price))
                # print(name, lastname, age, password, contact)
    else:
            messagebox.showinfo("result", 'Record not found')

def show():
    for i in tv.get_children():
        tv.delete(i )

    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project1')
    cur = db.cursor()
    s = "SELECT customer_contact, check_in_date, check_out_date, room_type, room_price FROM records"
    v = cur.execute(s )
    result = cur.fetchall()
    if (v > 0):
        for col in result:
            customer_contact=col[0]
            Check_in_Date= col[1]
            Check_out_date = col[2]
            Room_type = col[3]
            room_price=col[4]

            tv.insert("",'end',
            values=(customer_contact,Check_in_Date,Check_out_date,Room_type,room_price))

    else:
        messagebox.showinfo("result", 'Record not found')



f2=LabelFrame(top,text='Booking Details',height=400,width=450)
f2.place(x=100,y=200)


tv = ttk.Treeview(top,height=18)
tv['columns']=('Customer Contact', 'Check_in Date','Check_out Date','Room Type','Room Price')
tv.column('#0', width=0, stretch=NO)
tv.column('Customer Contact', anchor=CENTER, width=130)
tv.column('Check_in Date', anchor=CENTER, width=130)
tv.column('Check_out Date', anchor=CENTER, width=130)
tv.column('Room Type', anchor=CENTER, width=130)
tv.column('Room Price', anchor=CENTER, width=130)



tv.heading('Customer Contact', text='Customer Contact', anchor=CENTER)
tv.heading('Check_in Date', text='Check_in Date', anchor=CENTER)
tv.heading('Check_out Date', text='Check_out Date', anchor=CENTER)
tv.heading('Room Type', text='Room Type', anchor=CENTER)
tv.heading('Room Price', text='Room Price', anchor=CENTER)


tv.place(x=600,y=210)



l1=Label(f2,text='Customer Contact :-',font=('Arial 10 bold'))
l1.place(x=10,y=10)

e1=Entry(top,fg='black',font=('Arial 10 bold'),width=20)
e1.place(x=250,y=230)


l2=Label(f2,text='Check_in Date  :-',font=('Arial 10 bold'))
l2.place(x=10,y=45)
e2 = Entry(top, fg='black', font=('Arial 10 bold'), width=25)
e2.place(x=250, y=265)

cal1= DateEntry(top,date_pattern='yyyy-mm-dd', width=30, bg='darkblue', fg='white')
cal1.place(x=250, y=265)


l3=Label(f2,text='Check_out Date   :-',font=('Arial 10 bold'))
l3.place(x=10,y=80)
e3 = Entry(top, fg='black', font=('Arial 10 bold'), width=25)
e3.place(x=250, y=297)
cal2= DateEntry(top,date_pattern='yyyy-mm-dd', width=30, bg='darkblue', fg='white')
cal2.place(x=250, y=295)

l4=Label(f2,text='Room Type :-',font=('Arial 10 bold'))
l4.place(x=10,y=115)
cb1=ttk.Combobox(top,value=["Select","Single","Double","Family"],font=('arial 10 bold'))
cb1.set("Select")
cb1.place(x=250,y=330)
cb1.current(0)

l5 = Label(f2, text="Room Price  :- ", font=('Arial 10 bold'))
l5.place(x=10, y=150)
l6= Label(f2, text="      Select Room Type", font=('Arial 10 bold'))
l6.place(x=120, y=150)
cb3=ttk.Combobox(f2,value=["Select","cash","UPI","Credit Card","Others"],font=('arial 10 bold'),width=12)
cb3.set("Select")
cb3.place(x=300,y=150)
cb3.current(0)

cb1.bind("<<ComboboxSelected>>", update_room_price)







l=Label(top,text='ROOM BOOKING DETAILS',fg='black',bg='tan',font=('Arial 30'))
l.place(x=400,y=130)

b1=Button(top,text='Submit',fg='black',bg='tan',font=('Arial 10 bold'),command=submit_data)
b1.place(x=200,y=410)


b=Button(top,text='Fetch Data',bg='tan',fg='black',font=('Arial 10 bold'),width=11,command=fetch_data)
b.place(x= 400, y=226)


b1=Button(top,text='  REGISTRATION  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1
          ,command=registration)
b1.place(x=0,y=70)
b2=Button(top,text='  BOOKINGS  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=bookings)
b2.place(x=180,y=70)
b3=Button(top,text='  RECORDS  ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=records)
b3.place(x=320,y=70)

b5=Button(top,text='   EXIT    ',font=('Arial 15'),highlightbackground='black',highlightthickness=1,command=exit)
b5.place(x=450,y=70)
b12=Button(top,text="  SHOW ",fg='black',bg='tan',font=('Arial 10 bold'),width=10,height=1,command=show )
b12.place(x=280,y=410)

top.mainloop()
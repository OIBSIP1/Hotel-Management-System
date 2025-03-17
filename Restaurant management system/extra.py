from cgitb import reset
from tkinter import *
from tkinter import messagebox,Label
from tkinter import ttk
import tkinter as tk

top=Tk()
top.geometry("1500x800")
top.title("  MENU    ")

prices = [
    50, 80, 120, 90, 100, 60, 150, 150,  # Fast Food
    70, 40, 50, 20, 60,                 # Desserts
    120, 100, 130, 150,                 # Shakes
    20, 30, 50, 70, 20                  # Drinks
]

def exit():
    qexit=messagebox.askyesno('Fast Food','Do You Want To Quit')
    if qexit>0:
     top.destroy()
     return

def reset():

        # Clear all entry fields
        e1.delete(0, "end")
        e2.delete(0, "end")
        e3.delete(0, "end")
        e4.delete(0, "end")
        e5.delete(0, "end")
        e6.delete(0, "end")
        e7.delete(0, "end")
        e8.delete(0, "end")
        e9.delete(0, "end")
        e10.delete(0, "end")
        e11.delete(0, "end")
        e12.delete(0, "end")
        e13.delete(0, "end")
        e14.delete(0, "end")
        e15.delete(0, "end")
        e16.delete(0, "end")
        e17.delete(0, "end")
        e18.delete(0, "end")
        e19.delete(0, "end")
        e20.delete(0, "end")
        e21.delete(0, "end")
        e22.delete(0, "end")
        e23.delete(0, "end")
        e24.delete(0, "end")
        e25.delete(0, "end")




        messagebox.showinfo("Reset", "All fields have been cleared!")
def calculate_total():
    subtotal = 0
    for i, entry in enumerate(entries):
        quantity = entry.get()
        if quantity:  # If entry is not empty
            subtotal = int(quantity) * prices[i]

    tax = round(subtotal*0.02,2 )  # Assuming 10% tax
    total = subtotal + tax

    # Display the results in the respective entry fields
    e23.delete(0, "end")
    e23.insert(0, f"{tax}")
    e24.delete(0, "end")
    e24.insert(0, f"{subtotal}")
    e25.delete(0, "end")
    e25.insert(0, f"{total}")

    messagebox.showinfo("Total", f"Your total payment is = {total}")

f1=Frame(top,bg='beige',bd=10, height=70,width=1500,relief='raised')
f1.place(x=0,y=0)
l1=Label(f1,text='   MENU   ',font=('Arial 20 bold'))
l1.place(x=500,y=5)


mainframe=Frame(top,width=1400,height=580,relief='raised',bg='beige',bd=11)
mainframe.place(x=0,y=72)

f2=Frame(mainframe,width=500,height=560,relief='raised',bd=5)
f2.place(x=0,y=0)

l2=Label(f2,text='Fast Food',font=('Arial 20 bold'),relief='raised',bd=6)
l2.place(x=120,y=0)

entries=[]

fries=Checkbutton(f2,text='Fries  \t\t       Rs.50',font=('Arial 13 bold'))
fries.place(x=0,y=60)
e1=Entry(f2,width=6,)
e1.place(x=270,y=65)
entries.append(e1)

noodles=Checkbutton(f2,text='Noodles \t\t       Rs.80',font=('Arial 13 bold'))
noodles.place(x=0,y=90)
e2=Entry(f2,width=6)
e2.place(x=270,y=95)
entries.append(e2)

burger=Checkbutton(f2,text='Cheese Burger \t       Rs.120',font=('Arial 13 bold'))
burger.place(x=0,y=120)
e3=Entry(f2,width=6)
e3.place(x=270,y=125)
entries.append(e3)
momos=Checkbutton(f2,text='Momos \t\t       Rs.90',font=('Arial 13 bold'))
momos.place(x=0,y=150)
e4=Entry(f2,width=6)
e4.place(x=270,y=155)

chili=Checkbutton(f2,text='Chilli Potato \t       Rs.100',font=('Arial 13 bold'))
chili.place(x=0,y=180)
e5=Entry(f2,width=6)
e5.place(x=270,y=185)
entries.append(e5)

roll=Checkbutton(f2,text='Spring Roll \t       Rs.60',font=('Arial 13 bold'))
roll.place(x=0,y=210)
e6=Entry(f2,width=6)
e6.place(x=270,y=215)
entries.append(e6)

pasta=Checkbutton(f2,text='Red Sauce Pasta \t       Rs.150',font=('Arial 13 bold'))
pasta.place(x=0,y=240)
e7=Entry(f2,width=6)
e7.place(x=270,y=245)
entries.append(e7)

wpasta=Checkbutton(f2,text='White Sauce Potato     Rs.150',font=('Arial 13 bold'))
wpasta.place(x=0,y=270)
e8=Entry(f2,width=6)
e8.place(x=270,y=275)
entries.append(e8)


f3=Frame(mainframe,width=500,height=560,relief='raised',bd=5)
f3.place(x=400,y=0)
l3=Label(f3,text='Desserts',font=('Arial 20 bold'),relief='raised',bd=7)
l3.place(x=140,y=0)

brownie=Checkbutton(f3,text='Chocolate Brownie  \t  Rs.70',font=('Arial 13 bold'))
brownie.place(x=0,y=60)
e9=Entry(f3,width=6)
e9.place(x=350,y=65)
entries.append(e9)

rasgulla=Checkbutton(f3,text='Rasgulla   \t\t  Rs.40',font=('Arial 13 bold'))
rasgulla.place(x=0,y=90)
e10=Entry(f3,width=6)
e10.place(x=350,y=95)
entries.append(e10)

cupcake=Checkbutton(f3,text='CupCake  \t\t  Rs.50',font=('Arial 13 bold'))
cupcake.place(x=0,y=120)
e11=Entry(f3,width=6)
e11.place(x=350,y=125)
entries.append(e11)

Paan=Checkbutton(f3,text='Paan  \t\t\t  Rs.20',font=('Arial 13 bold'))
Paan.place(x=0,y=150)
e12=Entry(f3,width=6)
e12.place(x=350,y=155)
entries.append(e12)
rasmalai=Checkbutton(f3,text='Rasmalai  \t\t  Rs.60',font=('Arial 13 bold'))
rasmalai.place(x=0,y=180)
e13=Entry(f3,width=6)
e13.place(x=350,y=185)
entries.append(e13)

f4=Frame(mainframe,width=450,height=290,relief='raised',bd=7)
f4.place(x=400,y=270)
l5=Label(f4,text='Payment Method',font=('Arial 10 bold'))
l5.place(x=0,y=20)
cb3=ttk.Combobox(f4,value=["Select","cash","UPI","Credit Card","Others"],font=('arial 10 bold'))
cb3.set("Select")
cb3.place(x=50,y=50)
cb3.current(0)



f5=Frame(mainframe,width=500,height=560,relief='raised',bd=5)
f5.place(x=850,y=0)
l5=Label(f5,text='Shakes And Beverages',font=('Arial 20 bold'),relief='raised',bd=7)
l5.place(x=80,y=0)

oreo=Checkbutton(f5,text='Oreo Shake \t \t Rs.120',font=('Arial 13 bold'))
oreo.place(x=0,y=60)
e14=Entry(f5,width=6)
e14.place(x=350,y=65)
entries.append(e14)

vanilla=Checkbutton(f5,text='Vanilla Shake  \t \t Rs.100',font=('Arial 13 bold'))
vanilla.place(x=0,y=90)
e15=Entry(f5,width=6)
e15.place(x=350,y=95)
entries.append(e15)

chocolate=Checkbutton(f5,text='Chocolate Shake  \t\t Rs.130',font=('Arial 13 bold'))
chocolate.place(x=0,y=120)
e16=Entry(f5,width=6)
e16.place(x=350,y=125)
entries.append(e16)

kitkat=Checkbutton(f5,text='KitKat Shake  \t \t Rs.150',font=('Arial 13 bold'))
kitkat.place(x=0,y=150)
e17=Entry(f5,width=6)
e17.place(x=350,y=155)
entries.append(e17)

l5=Label(f5,text='Drinks',font=('Arial 20 bold'),relief='raised',bd=7)
l5.place(x=120,y=230)

tea=Checkbutton(f5,text='Tea  \t\t \t Rs.20',font=('Arial 13 bold'))
tea.place(x=0,y=300)
e18=Entry(f5,width=6)
e18.place(x=350,y=305)
entries.append(e18)

coffee=Checkbutton(f5,text='Coffee  \t\t \t Rs.30',font=('Arial 13 bold'))
coffee.place(x=0,y=330)
e19=Entry(f5,width=6)
e19.place(x=350,y=335)
entries.append(e19)

colddrink=Checkbutton(f5,text='Cold Drink  \t \t Rs.50',font=('Arial 13 bold'))
colddrink.place(x=0,y=360)
e20=Entry(f5,width=6)
e20.place(x=350,y=365)
entries.append(e20)

juice=Checkbutton(f5,text='Orange Shake  \t  \t Rs.70',font=('Arial 13 bold'))
juice.place(x=0,y=390)
e21=Entry(f5,width=6)
e21.place(x=350,y=395)
entries.append(e21)

water=Checkbutton(f5,text='Mineral Water  \t \t Rs.20',font=('Arial 13 bold'))
water.place(x=0,y=420)
e22=Entry(f5,width=6)
e22.place(x=350,y=425)
entries.append(e22)


l6=Label(f4,text='Tax',font=('Arial 13 bold'))
l6.place(x=330,y=50)
e23=Entry(f4,width=8)
e23.place(x=370,y=55)


b2=Button(f4,text='  Reset  ', font=('Arial 13 bold'),bd=10,command=reset)
b2.place(x=190,y=200)
l7=Label(f4,text='SubTotal',font=('Arial 13 bold'))
l7.place(x=289,y=100)
e24=Entry(f4,width=8)
e24.place(x=370,y=105)


b3=Button(f4,text='  Total  ', font=('Arial 13 bold'),bd=10,command=calculate_total)
b3.place(x=60,y=200)
l8=Label(f4,text='Total',font=('Arial 13 bold'))
l8.place(x=320,y=150)
e25=Entry(f4,width=8)
e25.place(x=370,y=155)

b4=Button(f4,text='  Exit  ', font=('Arial 13 bold'),bd=10,command=exit)
b4.place(x=320,y=200)


top.mainloop()
from tkinter import *
import  tkinter as tk
from  PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox,Label



top=tk.Tk()
top.geometry('1500x800')



path=r"C:\Users\hp\Downloads\DALL·E 2025-01-29 00.39.05 - A collage featuring six distinct pictures of fast food items_ 1) A juicy cheeseburger, 2) A bowl of steaming noodles, 3) A tall glass of milkshake wit.webp"
img = Image.open(path)
img = img.resize((1300, 650))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.place(x=0,y=0)



def create_account():
        username = e1.get()
        mobile_no= e2.get()
        otp = e3.get()
        password=e4.get()
        retype_password=e5.get()

        # Check if any field is empty
        if not username or not mobile_no  :
            messagebox.showerror("Error", "All fields are required!")
            return

        # Connect to the database
        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='Saloni@123', db='restro_project')
        cur = db.cursor()

        # Check if the username already exists
        cur.execute("SELECT * FROM emp WHERE username = %s", (username,))
        row = cur.fetchone()

        if row:
            messagebox.showerror("Error", "Username already exists!")
        else:
            # Insert new account into the database
            cur.execute("INSERT INTO emp (username, mobile_no, otp,password,retype_password) VALUES (%s, %s, %s,%s,%s)", (username, mobile_no,otp,password,retype_password))
            db.commit()
            messagebox.showinfo("Success", "Account created successfully!")
            db.close()

            # Close the create account window and go back to the login window
            top.destroy()
            import login







f1 =Frame(top, bg='tan', height=430,width=450,bd=2)
f1.place(x=450, y=130)  # Ensure frame is above the image




l2=Label(f1,text='Create Account',fg='black',bg='tan',font=('Arial 18 bold'))
l2.place(x=150,y=10)

l3=Label(f1,text= ' Name :-',fg='black',bg='tan',font=('Arial 12 bold'))
l3.place(x=20,y=70)
e1=Entry(f1,fg='black',font=('Arial 15 bold'),width=15)
e1.place(x=190,y=70)

l4=Label(f1,text= ' Mobile No :-',fg='black',bg='tan',font=('Arial 12 bold'))
l4.place(x=20,y=120)
e2=Entry(f1,fg='black',font=('Arial 15 bold'),width=15)
e2.place(x=190,y=120)

l5=Label(f1,text= ' Otp :-',fg='black',bg='tan',font=('Arial 12 bold'))
l5.place(x=20,y=170)
e3=Entry(f1,fg='black',font=('Arial 15 bold'),width=15)
e3.place(x=190,y=170)

l6=Label(f1,text= ' Password :-',fg='black',bg='tan',font=('Arial 12 bold'))
l6.place(x=20,y=220)
e4=Entry(f1,fg='black',font=('Arial 15 bold'),width=15)
e4.place(x=190,y=220)

l7=Label(f1,text= ' Retype Password :-',fg='black',bg='tan',font=('Arial 12 bold'))
l7.place(x=20,y=270)
e5=Entry(f1,fg='black',font=('Arial 15 bold'),width=15)
e5.place(x=190,y=270)



b1=Button(f1,text=' Create Account ',fg='black',bg='white',font=('Arial 15 bold'),command=create_account)
b1.place(x=170,y=350)




top.mainloop()
from tkinter import *
import  tkinter as tk
from  PIL import Image,ImageTk
from time import strftime
from tkinter import messagebox,Label
import webbrowser


top=tk.Tk()
top.geometry('1500x800')

def sign_in():
    # Check if any entry is empty
    if not e1.get().strip() or not e2.get().strip():
        messagebox.showerror("Error", "All fields are required!")
        return

    import pymysql as sql
    # Connect to the database
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='restro_project')
    cur = db.cursor()

    # Query the database for the given username and password
    cur.execute("select * from emp where username=%s and password=%s", (e1.get(), e2.get()))
    row = cur.fetchone()
    db.close()  # Close the database connection

    if row is None:  # If no match is found in the database
        messagebox.showerror("Error", "Invalid username or password!")
    else:  # If credentials are correct
        top.destroy()
        import extra

def create_account():
    top.destroy()
    import create_account






def forget_password():
    webbrowser.open("https://www.example.com/forgot-password")


path=r"C:\Users\hp\Downloads\DALL·E 2025-01-25 22.08.22 - A beautiful, vibrant food spread featuring various dishes. The scene includes a variety of dishes like pasta, salad, a bowl of fruit, a slice of cake,.webp"
img = Image.open(path)
img = img.resize((1300, 660))  # Resize image to match the label dimensions
img = ImageTk.PhotoImage(img)
l1=tk.Label(top,image=img)
l1.place(x=0,y=0)



# Create the frame
f1 =Frame(top, bg='tan', height=430,width=450,bd=2)
f1.place(x=450, y=130)  # Ensure frame is above the image




l2=Label(f1,text='Login',fg='black',bg='tan',font=('Arial 18 bold'))
l2.place(x=180,y=10)

l3=Label(f1,text= ' User Name :-',fg='black',bg='tan',font=('Arial 12 bold'))
l3.place(x=20,y=90)

e1=Entry(f1,fg='black',font=('Arial 15 bold'),width=25)
e1.place(x=140,y=90)

l4=Label(f1,text= ' Password :-',fg='black',bg='tan',font=('Arial 12 bold'))
l4.place(x=20,y=160)

e2=Entry(f1,fg='black',font=('Arial 15 bold'),width=25)
e2.place(x=140,y=160)

b1=Button(f1,text=' SIGN IN ',fg='black',bg='white',font=('Arial 15 bold'),command=sign_in)
b1.place(x=170,y=250)


b2 =Button(f1, text="Forget Password?",bg='tan', fg="blue", font=("Arial", 10, "underline"),command=forget_password)
b2.place(x=320,y=350)


b3=Button(f1,text=' Create Account',fg='blue',bg='tan',font=('Arial 10 bold'),command=create_account)
b3.place(x=320,y=320)


top.mainloop()
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

top = Tk()
top.geometry('1500x800')





path=r"C:\Users\hp\Downloads\pexels-lkloeppel-466685.jpg"
img=ImageTk.PhotoImage(Image.open(path))

def login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project')
    cur = db.cursor()
    cur.execute("select * from emp where name=%s and password=%s",(e1.get(),e4.get()))
    row=cur.fetchone()

    if row==None:
        messagebox.showerror("error","Invalid user name and password")
    else:
        top.destroy()
        import project3

l22=Label(top,image=img)
l22.pack()




l = Label(top, text='Login', fg='white', bg='green', font=('Arial 25 bold'))
l.place(x=400, y=50)

l2 = Label(top, text='name', fg='white', bg='green', font=('Arial 25 bold'))
l2.place(x=200, y=150)

e1 = Entry(top, fg='red',font=('Arial 20 bold'))
e1.place(x=400, y=150)



l5 = Label(top, text='password', fg='white', bg='green', font=('Arial 25 bold'))
l5.place(x=200, y=200)

e4 = Entry(top, fg='red',font=('Arial 20 bold'),show="*")
e4.place(x=400, y=200)





b6=Button(top,text='Login',font=('Arial 25 bold'),command=login)
b6.place(x=300,y=300)

top.mainloop()

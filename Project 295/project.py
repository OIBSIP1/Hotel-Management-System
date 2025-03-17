from abc import update_abstractmethods
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

top = Tk()
top.geometry('1000x600')

def insert():
    k=e1.get()
    k2=e2.get()
    k3=int(e3.get())
    k4=e4.get()
    k5=int(e5.get())
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='Saloni@123',db='project')
    cur=db.cursor()
    s="insert into emp values('%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5)
    result=cur.execute(s)
    if(result>0):
        messagebox.showinfo("Result","Record insert successfully")
    else:
        messagebox.showinfo("Result","Record not inserted")
    db.commit()
    e1.delete(0, "end")
    e2.delete(0, "end")
    e3.delete(0, "end")
    e4.delete(0, "end")
    e5.delete(0, "end")

def delete():
    k=e1.get()
    import pymysql as sql
    db= sql.connect(host='localhost', user='root', password='Saloni@123', db='project')
    cur = db.cursor()
    s="delete from emp where name=%s"
    result = cur.execute(s,k)
    if (result > 0):
        messagebox.showinfo("Result", "Record delete successfully")
    else:
        messagebox.showinfo("Result", "Record not deleted inserted")
    db.commit()

def search():
    for i in tv.get_children():
        tv.delete(i )
    k=e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project')
    cur = db.cursor()
    s="select * from emp where name=%s"
    v=cur.execute(s,k)
    result=cur.fetchall()
    if(v>0):
        for col in result:
            name=col[0]
            lastname=col[1]
            age=col[2]
            password=col[3]
            contact=col[4]
            tv.insert("", 'end', values=(name, lastname, age, password, contact))
            #print(name,lastname,age,password,contact)
    else:
        messagebox.showinfo("result",'Record not found')
def show():
    for i in tv.get_children():
        tv.delete(i )
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project')
    cur = db.cursor()
    s = "select * from emp"
    v = cur.execute(s, )
    result = cur.fetchall()
    if (v > 0):
        for col in result:
            name = col[0]
            lastname = col[1]
            age = col[2]
            password = col[3]
            contact = col[4]
            tv.insert("",'end',values=(name,lastname,age,password,contact))
            #print(name, lastname, age, password, contact)
    else:
        messagebox.showinfo("result", 'Record not found')

def update():
    k = e1.get()
    k2 = e2.get()
    k3 = int(e3.get())
    k4 = e4.get()
    k5 = int(e5.get())
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Saloni@123', db='project')
    cur = db.cursor()
    s = "update emp set lastname=%s,age=%s,password=%s,contact=%s where name=%s"
    t=(k2,k3,k4,k5,k)
    result=cur.execute(s,t)
    if (result > 0):
        messagebox.showinfo("Result", "Record update successfully")
    else:
        messagebox.showinfo("Result", "Record not updated")
    db.commit()

def login():
    top.destroy()
    import project2



path=r"C:\Users\hp\Downloads\pexels-lkloeppel-466685.jpg"
img=ImageTk.PhotoImage(Image.open(path))


l22=Label(top,image=img)
l22.pack()

tv = ttk.Treeview(top)
tv['columns']=('Name', 'lastname','age','password','contact')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=70)
tv.column('lastname', anchor=CENTER, width=75)
tv.column('age', anchor=CENTER, width=75)
tv.column('password', anchor=CENTER, width=75)
tv.column('contact', anchor=CENTER, width=75)


tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('lastname', text='Lastname', anchor=CENTER)
tv.heading('age', text='age', anchor=CENTER)
tv.heading('password', text='Password', anchor=CENTER)
tv.heading('contact', text='contact', anchor=CENTER)
tv.place(x=800,y=150)

l = Label(top, text='Registration', fg='white', bg='green', font=('Arial 25 bold'))
l.place(x=400, y=50)

l2 = Label(top, text='name', fg='white', bg='green', font=('Arial 25 bold'))
l2.place(x=200, y=150)

e1 = Entry(top, fg='red',font=('Arial 20 bold'))
e1.place(x=400, y=150)

l3 = Label(top, text='lastName', fg='white', bg='green', font=('Arial 25 bold'))
l3.place(x=200, y=200)

e2 = Entry(top, fg='red',font=('Arial 20 bold'))
e2.place(x=400, y=200)

l4 = Label(top, text='age', fg='white', bg='green', font=('Arial 25 bold'))
l4.place(x=200, y=250)

e3 = Entry(top, fg='red',font=('Arial 20 bold'))
e3.place(x=400, y=250)

l5 = Label(top, text='password', fg='white', bg='green', font=('Arial 25 bold'))
l5.place(x=200, y=300)

e4 = Entry(top, fg='red',font=('Arial 20 bold'),show="*")
e4.place(x=400, y=300)

l6 = Label(top, text='contact', fg='white', bg='green', font=('Arial 25 bold'))
l6.place(x=200, y=350)

e5 = Entry(top, fg='red',font=('Arial 20 bold'))
e5.place(x=400, y=350)

b1=Button(top,text='Submit',font=('Arial 25 bold'),command=insert)
b1.place(x=400,y=400)
b2=Button(top,text='Delete',font=('Arial 25 bold'),command=delete)
b2.place(x=550,y=400)
b3=Button(top,text='Search',font=('Arial 25 bold'),command=search)
b3.place(x=700,y=400)
b4=Button(top,text='Show',font=('Arial 25 bold'),command=show)
b4.place(x=850,y=400)
b5=Button(top,text='Update',font=('Arial 25 bold'),command=update)
b5.place(x=1000,y=400)


b6=Button(top,text='Login',font=('Arial 25 bold'),command=login)
b6.place(x=1150,y=400)

top.mainloop()




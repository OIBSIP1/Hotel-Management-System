from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

top = Tk()
top.geometry('1000x600')
top.title('Welcome')



path=r"C:\Users\hp\Downloads\pexels-lkloeppel-466685.jpg"
img=ImageTk.PhotoImage(Image.open(path))


l22=Label(top,image=img)
l22.pack()
k=['select','java','net','python','html','analysis']
cb=ttk.Combobox(top,value=k,font=('arial 20 bold'))
cb.place(x=200,y=200)
cb.current(0)

c1=Checkbutton(top,text='math')
c1.place(x=300,y=250)

c2=Checkbutton(top,text='english')
c2.place(x=300,y=300)

c3=Checkbutton(top,text='science')
c3.place(x=300,y=350)

r1=Radiobutton(top,text='male',value=1,font=('Arial 15 bold'))
r1.place(x=600,y=100)

r2=Radiobutton(top,text='female',value=2,font=('Arial 15 bold'))
r2.place(x=600,y=150)

r3=Radiobutton(top,text='others',value=3,font=('Arial 15 bold'))
r3.place(x=600,y=200)

r1.select()


l = Label(top, text='Welcome', fg='white', bg='green', font=('Arial 25 bold'))
l.place(x=400, y=50)




top.mainloop()
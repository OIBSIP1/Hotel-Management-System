import tkinter
from tkinter import *
import tkinter as tk


top=tk.Tk()
top.geometry('500x500')


board = { 1:" " , 2:" " , 3:" " ,
          4:" " , 5:" " , 6:" " ,
          7:" " , 8:" " , 9:" " }

turn='X'

def checkforwin(player):
    if board[1]==board[2] and board[2]==board[3] and board[3]==player:
        return True


def play(event):
    global  turn
    button=event.widget
    buttonText=str(button)
    clicked=buttonText[-1]
    print(clicked)
    if clicked=='n':
        clicked =1
    else:
        clicked = int(clicked)



    if button["text"]==" " :


     if turn =='X':
            button["text"]="X"
            board[clicked] = turn
            turn="O"

     else:
            button["text"]="O"
            board[clicked] = turn
            turn="X"

     print(board)
     checkforwin(turn)




f1=Frame(top,height=110,width=1500)
f1.place(x=0,y=0)
l1=Label(f1,text='Tic Tac Toe',bg='tan',fg='black',font='Arial 15 bold')
l1.place(x=200,y=10)

f2=Frame(top,height=300,width=500)
f2.place(x=0,y=100)






b1=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b1.place(x=100,y=0)
b1.bind("<Button-1>",play)
b2=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b2.place(x=191,y=0)
b2.bind("<Button-1>",play)
b3=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b3.place(x=282,y=0)
b3.bind("<Button-1>",play)
b4=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED)
b4.place(x=100,y=93)
b4.bind("<Button-1>",play)
b5=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b5.place(x=191,y=93)
b5.bind("<Button-1>",play)
b6=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b6.place(x=282,y=93)
b6.bind("<Button-1>",play)
b7=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b7.place(x=100,y=186)
b7.bind("<Button-1>",play)
b8=Button(f2,height=1,width=3,text=" ",font=("Arial",35) ,bg='pink',relief=RAISED)
b8.place(x=191,y=186)
b8.bind("<Button-1>",play)
b9=Button(f2,height=1,width=3,text=" ",font=("Arial",35),bg='pink',relief=RAISED )
b9.place(x=282,y=186)
b9.bind("<Button-1>",play)
top.mainloop()



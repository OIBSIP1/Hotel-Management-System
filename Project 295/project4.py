from tkinter import *
from time import strftime

# Create the main window
top = Tk()
top.geometry('1000x600')

# Function to exit the application
def exit():
    top.destroy()

# Function to update the time
def time():
    string = strftime("%H:%M:%S %p")  # Fetch current time
    l77.config(text=string)  # Update the label with current time
    l77.after(1000, time)  # Pass function reference, not call it

# Header frame
f1 = LabelFrame(top, text='Header', height=200, width=1500, bg='orange')
f1.place(x=0, y=0)

# Clock label
l77 = Label(f1, bg='orange', fg='red', font=('Arial', 20, 'bold'))
l77.place(x=1000, y=100)

# Start the clock
time()

# Header text
l1 = Label(f1, text='Registration', fg='white', bg='black', font=('Arial', 30, 'bold'))
l1.place(x=600, y=50)

# Registration form frame
f2 = Frame(top, height=200, width=1500, bg='white')
f2.place(x=0, y=201)

# Name label and entry
l2 = Label(f2, text='Name', fg='white', bg='black', font=('Arial', 20, 'bold'))
l2.place(x=200, y=50)

e1 = Entry(f2, fg='red', font=('Arial', 20, 'bold'))
e1.place(x=350, y=50)

# Last name label and entry
l3 = Label(f2, text='Last Name', fg='white', bg='black', font=('Arial', 20, 'bold'))
l3.place(x=200, y=100)

e2 = Entry(f2, fg='red', font=('Arial', 20, 'bold'))
e2.place(x=350, y=100)

# Footer frame
f3 = Frame(top, height=200, width=1500, bg='green')
f3.place(x=0, y=401)

# Exit button
b1 = Button(f3, text='Exit', font=('Arial', 20, 'bold'), command=exit)
b1.place(x=100, y=100)

# Run the application
top.mainloop()
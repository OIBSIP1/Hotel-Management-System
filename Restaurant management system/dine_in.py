from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("1000x800")
top.title("MENU")


# Function to exit the app
def exit_app():
    qexit = messagebox.askyesno("Fast Food", "Do You Want To Quit?")
    if qexit > 0:
        top.destroy()


# Function to increase quantity
def increase_quantity(label):
    current_quantity = int(label['text'])
    label['text'] = str(current_quantity + 1)


# Function to decrease quantity
def decrease_quantity(label):
    current_quantity = int(label['text'])
    if current_quantity > 0:
        label['text'] = str(current_quantity - 1)
    else:
        messagebox.showwarning("Warning", "Quantity cannot be less than 0!")


# Menu Header
f1 = Frame(top, bg="gray", bd=10, height=70, width=1500, relief="raised")
f1.place(x=0, y=0)
l1 = Label(f1, text="   MENU   ", font=("Arial 20 bold"))
l1.place(x=500, y=5)

# Main Frame
mainframe = Frame(top, width=1400, height=580, relief="raised", bg="beige", bd=11)
mainframe.place(x=0, y=72)

# Fast Food Frame
f2 = Frame(mainframe, width=500, height=560, relief="raised", bd=5)
f2.place(x=0, y=0)

l2 = Label(f2, text="Fast Food", font=("Arial 20 bold"), relief="raised", bd=6)
l2.place(x=120, y=0)

# Fast Food Items with Quantity Management
items_fast_food = [
    "Fries",
    "Noodles",
    "Cheese Burger",
    "Momos",
    "Chilli Potato",
    "Spring Roll",
    "Red Sauce Pasta",
    "White Sauce Pasta",
]

y_position = 60

for item in items_fast_food:
    # Item Name
    item_label = Checkbutton(f2, text=item, font=("Arial 13 bold"))
    item_label.place(x=0, y=y_position)

    # Decrease Button
    quantity_label = Label(f2, text="0", font=("Arial 13 bold"), width=3)
    quantity_label.place(x=220, y=y_position)

    decrease_button = Button(
        f2, text="-", font=("Arial 10 bold"), command=lambda lbl=quantity_label: decrease_quantity(lbl)
    )
    decrease_button.place(x=180, y=y_position)

    # Increase Button
    increase_button = Button(
        f2, text="+", font=("Arial 10 bold"), command=lambda lbl=quantity_label: increase_quantity(lbl)
    )
    increase_button.place(x=260, y=y_position)

    y_position += 40  # Update the y_position for the next item


# Exit Button
exit_button = Button(top, text="Exit", font=("Arial 13 bold"), command=exit_app)
exit_button.place(x=450, y=680)

top.mainloop()
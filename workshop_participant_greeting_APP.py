from tkinter import *
from datetime import date

window = Tk()

window.title("Workshop Welcome Desk")
window.geometry('700x400')

lbl = Label(text="Please enter your name", bg="white", fg="black", width=1, height=300)

name_lbl = Label(text="Participant Name", bg="white")
name_entry = Entry()
text_box = Text(height=3)

def display_welcome():
    name = name_entry.get()
    global greeting
    greeting = f"Welcome, {name}, to the workshop app!"
    welcome = f"\nYou are now signed in. \nToday's date is: "
    text_box.insert(END, greeting)
    text_box.insert(END, welcome)
    text_box.insert(END, date.today())

check_in_btn = Button(text="Check in", command=display_welcome, height=1, bg="#007447", fg="white")

name_lbl.pack()
name_entry.pack()
text_box.pack()
check_in_btn.pack()


window.mainloop()
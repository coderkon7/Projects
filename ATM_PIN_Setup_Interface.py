from tkinter import *

root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry("400x500")

details_frame = Frame(master=root, width=150, height=360, bg="#d0efff") 

account_lbl = Label(master=details_frame, text="Account Name", bg="white", fg="black", width=12)
PIN_lbl = Label(master=details_frame, text="PIN Number", bg="white", fg="black", width=12)

account_entry = Entry(details_frame)
PIN_entry = Entry(details_frame)

keypad_frame = Frame(master=root, bg="grey", relief=SUNKEN, borderwidth=2)

keypad_data = [[7, 8, 9], [4, 5, 6], [1, 2, 3], ["*", 0, "#"]]


def confirm_pin():
    msg = "PIN confirmed!"
    account_name = account_entry.get()
    pin = PIN_entry.get()
    if account_name == "" or pin == "":
        textbox.delete(1.0, END)
        textbox.insert(END, "Please enter your account name and PIN first.")
    else:
        textbox.delete(1.0, END)
        textbox.insert(END, msg)

textbox = Text(bg="grey", fg="white")

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        details_frame.grid(row=i, column=j)
        label = Label(master=details_frame, text=keypad_data[i][j], bg="#6acdff")
        label.pack(padx=3, pady=3)
 
set_ATM_pin_btn = Button(root, text="Set ATM PIN", command=confirm_pin)



details_frame.place(x=100, y=100)
account_lbl.place(x=100, y=100)
account_entry.place(x=110, y=100)
PIN_lbl.place(x=0, y=20)
PIN_entry.place(x=20, y=20)
keypad_frame.place(x=20, y=200)
set_ATM_pin_btn.place(x=100, y=150)
textbox.place(x=100, y=200)

root.mainloop()

from tkinter import *

# Main Window
root = Tk()
root.title("ATM PIN Setup Interface")
root.geometry("400x650")
root.configure(bg="#eaf6ff")

# Heading
heading = Label(root, text="ATM PIN Setup", font=("Arial", 18, "bold"), bg="#eaf6ff")
heading.grid(row=0, column=0, pady=15)

# Account Details Frame
details_frame = Frame(root, bg="#d0efff", padx=15, pady=15)
details_frame.grid(row=1, column=0, padx=20, pady=10)

# Account Name
account_lbl = Label(details_frame, text="Account Name:", bg="#d0efff")
account_lbl.grid(row=0, column=0, padx=5, pady=8)

account_entry = Entry(details_frame, width=20)
account_entry.grid(row=0, column=1, padx=5, pady=8)

# PIN Number
PIN_lbl = Label(details_frame, text="PIN Number:", bg="#d0efff")
PIN_lbl.grid(row=1, column=0, padx=5, pady=8)

PIN_entry = Entry(details_frame, width=20, show="*")
PIN_entry.grid(row=1, column=1, padx=5, pady=8)

# Keypad Frame
keypad_frame = Frame(root, bg="grey", relief=SUNKEN, borderwidth=2, padx=10, pady=10)
keypad_frame.grid(row=2, column=0, pady=10)

# Keypad Data
keypad_data = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    ["*", 0, "#"]
]

# Display message
textbox = Text(root, height=4, width=38, bg="grey", fg="white")
textbox.grid(row=4, column=0, padx=15, pady=10)

def show_message(msg):
    textbox.delete("1.0", END)
    textbox.insert(END, msg)

# Confirm PIN
def confirm_pin():
    account_name = account_entry.get()
    pin = PIN_entry.get()

    if account_name == "" or pin == "":
        show_message("Please enter your account name and PIN first.")
    else:
        show_message("PIN confirmed!\nWelcome, " + account_name)

# Keypad Button Function
def keypad_click(value):

    if value == "*":
        PIN_entry.delete(0, END)

    elif value == "#":
        confirm_pin()

    else:
        PIN_entry.insert(END, str(value))

# Create Keypad Buttons
for i in range(4):
    for j in range(3):

        value = keypad_data[i][j]

        button = Button(keypad_frame, text=value, width=6, height=2, bg="#6acdff", font=("Arial", 12, "bold"), command=lambda v=value: keypad_click(v))

        button.grid(row=i, column=j, padx=5, pady=5)

# Set ATM PIN Button
set_ATM_pin_btn = Button(root, text="Set ATM PIN", bg="#0077b6", fg="white", font=("Arial", 12, "bold"), command=confirm_pin)
set_ATM_pin_btn.grid(row=3, column=0, pady=10)

# Run Application
root.mainloop()
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('After-School Routine Checker')
root.geometry('500x400')

heading = Label(master=root, text='After-School Routine Checker')
instruction = Label(master=root, text='Please enter your next after-school task')
task_entry = Entry(master=root, text='Routine Task')
key_label = Label(master=root, text='')

def handle_keypress(event):
    key_label.config(text=event.char)

task_entry.bind('<Key>', handle_keypress)

def handle_click(event):    
    routine_msg.config(text='Label clicked!')

routine_msg = Label(master=root, text='        ', fg='white', bg='grey')
routine_msg.bind('<Button-1>', handle_click)

def check_routine():
    text = task_entry.get()
    if text != '':
        routine_msg.config(text=text)
    else:
        messagebox.showwarning('Error: No Input Given', 'Please type at least one character for your routine')
    

check_my_routine_btn = Button(master=root, text='Check My Routine', command=check_routine, fg='white', bg='blue')

heading.pack()
instruction.pack()
task_entry.pack()
key_label.pack()
routine_msg.pack()
check_my_routine_btn.pack()

root.mainloop()
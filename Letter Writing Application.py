from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

root = Tk()
root.geometry('600x500')
root.title('Letter Writing Application')
root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

def open_file():
    '''Open a file for editing'''
    filepath = askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return
    txt_edit.delete(1.0, END)

    with open(filepath, 'r') as file:
        text = file.read()
        txt_edit.insert(END, text)
        file.close()
    root.title(f'Letter Writing Application - {filepath}')

def save_file():
    '''Saves the file'''
    filepath = asksaveasfilename(defaultextension='*.txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not filepath:
        return

    with open(filepath, 'w') as file:
        text = txt_edit.get(1.0, END)
        file.write(text)
    root.title(f'Letter Writing Application - {filepath}')

txt_edit = Text(root)
fr_buttons = Frame(root, relief=SUNKEN, bd=2)
open_letter_btn = Button(fr_buttons, text='Open Letter', command=open_file,fg='white', bg='blue')
save_letter_as_btn = Button(fr_buttons, text='Save Letter As...', command=save_file, fg='black', bg='lime')

open_letter_btn.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
save_letter_as_btn.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
fr_buttons.grid(row=0, column=0, padx=5, pady=5, sticky='ns')
txt_edit.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')

root.mainloop()
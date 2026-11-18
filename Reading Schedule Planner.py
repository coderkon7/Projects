import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x400")
root.title("Reading Schedule Planner")
root.configure(bg="light grey")

heading = tk.Label(root, text="Welcome to the Reading Schedule Planner!", font=("Arial", 15, "bold"))
heading.grid(row=0, column=0, padx=3, pady=3)

instruction = tk.Label(root, text="You can use this app to plan your daily reading target. Click the button below to get started ⬇")
instruction.grid(row=1, column=0, padx=1, pady=1)

def launch_planner_toplevel():
    planner_window = tk.Toplevel(root)
    planner_window.geometry("350x250")
    planner_window.title("Planner")
    planner_window.configure(bg="light grey")

    planner_heading = tk.Label(planner_window, text="Plan your Reading Schedule", font=("Arial", 10, "bold"))
    planner_heading.grid(row=0, columnspan=2, padx=0, pady=20)

    total_pages_label = tk.Label(planner_window, text="Total Pages")
    total_pages_label.grid(row=1, column=0)
    total_pages_entry = tk.Entry(planner_window)
    total_pages_entry.grid(row=1, column=1)

    pages_per_day_label = tk.Label(planner_window, text="Pages per Day")
    pages_per_day_label.grid(row=2, column=0)
    pages_per_day_entry = tk.Entry(planner_window)
    pages_per_day_entry.grid(row=2, column=1, pady=20)

    total_days_label = tk.Label(planner_window, text="Total Days: ")
    total_days_label.grid(row=4, column=0)
    #total_days_entry = tk.Entry(planner_window)
    #total_days_entry.grid(row=4, column=1)
    remaining_pages_label = tk.Label(planner_window, text="Remaining Pages: ")
    remaining_pages_label.grid(row=5, column=0)
    #remaining_pages_entry = tk.Entry(planner_window)
    #remaining_pages_entry.grid(row=5, column=1)



    def calculate_plan():
        try:
            total_pages = int(total_pages_entry.get())
            pages_per_day = int(pages_per_day_entry.get())
            if total_pages>0 and pages_per_day>0:
                total_days = total_pages // pages_per_day
                remaining_pages = total_pages % pages_per_day
                #total_days_entry.delete(0, tk.END)
                #remaining_pages_entry.delete(0, tk.END)
                #total_days_entry.insert(tk.END, total_days)
                #remaining_pages_entry.insert(tk.END, remaining_pages)
                total_days_label.configure(text=f"Total Days: {total_days}")
                remaining_pages_label.configure(text=f"Remaining Pages: {remaining_pages}")
            else:
                messagebox.showerror("Error", "Number must be greater than zero")
                
        except ValueError: messagebox.showerror("Error", "Please only type numbers for total pages and pages per day")


    calculate_plan_button = tk.Button(planner_window, text="Calculate Plan", command=calculate_plan, bg="blue", fg="white")
    calculate_plan_button.grid(row=6, column=1, padx=10, pady=10)



open_planner_button = tk.Button(root, text="Open Planner", command=launch_planner_toplevel, bg="green", fg="white")
open_planner_button.grid(row=2, column=0, padx=10, pady=10)

if __name__ == "__main__":
    root.mainloop()
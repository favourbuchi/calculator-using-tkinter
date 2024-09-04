import sys
import datetime
import tkinter as tk

def addTask():
    to_do_dict = {}

    to_do_dict["TASK"]= task_entry.get() 
    to_do_dict["Year"] = year_entry.get()
    to_do_dict["Month"] = month_entry.get()
    to_do_dict["Day"] = day_entry.get()
    to_do_dict["Hour"] = hour_entry.get()


    # date_string = to_do_dict.get("DATE")
    task_date = datetime.datetime(int(to_do_dict.get("Year")), int(to_do_dict.get("Month")), int(to_do_dict.get("Day")), int(to_do_dict.get("Hour")) )
    today_date = datetime.datetime.now()

    if task_date < today_date:
        
        print("INVALID DATE!!!")
    else:
        with open("output.txt", "a") as f:
            sys.stdout = f
            print(f"TASK: {to_do_dict.get("TASK")}\n Year: {task_date.year} \n Month: {task_date.month}\n Day: {task_date.day}\n Hour: {task_date.hour}")


root = tk.Tk()
root.geometry("500x500")

task_label = tk.Label(root, text="Task").place(x=40, y=50)
task_entry = tk.Entry(root)
task_entry.place(x=40, y=70)

year_label = tk.Label(root, text="Year").place(x=40, y=110)
year_entry = tk.Entry(root)
year_entry.place(x=40, y=130)

month_label = tk.Label(root, text="Month").place(x=40, y=170)
month_entry = tk.Entry(root)
month_entry.place(x=40, y=190)

day_label = tk.Label(root, text="Day").place(x=40, y=230)
day_entry = tk.Entry(root)
day_entry.place(x=40, y=250)

hour_label = tk.Label(root, text="Hour").place(x=40, y=290)
hour_entry = tk.Entry(root)
hour_entry.place(x=40, y=310)

add_task_button = tk.Button(root, text="Add Task", command=addTask).place(x=60, y=340)

root.mainloop()

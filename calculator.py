import tkinter as tk

calculation = ""
def button_press(symbol):
    global calculation 
    calculation += str(symbol)
    entry_label.delete(1.0, "end")
    entry_label.insert(1.0, calculation)

def equals():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        entry_label.delete(1.0, "end")
        entry_label.insert(1.0, result)
    except:
        clear()
        entry_label.insert(1.0, "Error")

def clear():
    global calculation
    calculation = ""
    entry_label.delete(1.0, "end")

root = tk.Tk()

root.title("Calculator with Python")
root.geometry("400x350")

entry_label = tk.Text(root,height = 2, width=18, font=('Arial', 24))
entry_label.pack()

button_frame = tk.Frame(root)

button_1 = tk.Button(button_frame, text="1", width=10, height=4, command = lambda: button_press(1))
button_1.grid(row=0, column = 0)

button_2 = tk.Button(button_frame, text="2", width=10, height=4, command = lambda: button_press(2) )
button_2.grid(row=0, column = 1)

button_3 = tk.Button(button_frame, text="3", width=10, height=4, command = lambda: button_press(3) )
button_3.grid(row=0, column = 2)

button_4 = tk.Button(button_frame, text="4", width=10, height=4, command = lambda: button_press(4) )
button_4.grid(row=1, column = 0)

button_5 = tk.Button(button_frame, text="5", width=10, height=4,command = lambda: button_press(5))
button_5.grid(row=1, column = 1)

button_6 = tk.Button(button_frame, text="6", width=10, height=4, command = lambda: button_press(6) )
button_6.grid(row=1, column = 2)

button_7 = tk.Button(button_frame, text="7", width=10, height=4, command = lambda: button_press(7) )
button_7.grid(row=2, column = 0)

button_8 = tk.Button(button_frame, text="8", width=10, height=4, command = lambda: button_press(8) )
button_8.grid(row=2, column = 1)

button_9 = tk.Button(button_frame, text="9", width=10, height=4, command = lambda: button_press(9) )
button_9.grid(row=2, column = 2)

button_0 = tk.Button(button_frame, text="0", width=10, height=4, command = lambda: button_press(0) )
button_0.grid(row=3, column = 1)

plus_button = tk.Button(button_frame, text="+", width=10, height=4, command = lambda: button_press("+"))
plus_button.grid(row=0, column = 3)

minus_button = tk.Button(button_frame, text="-", width=10, height=4, command = lambda: button_press("-"))
minus_button.grid(row=1, column = 3)

mul_button = tk.Button(button_frame, text="*", width=10, height=4, command = lambda: button_press("*"))
mul_button.grid(row=2, column = 3)

div_button = tk.Button(button_frame, text="/", width=10, height=4, command = lambda: button_press("/"))
div_button.grid(row=3, column = 3)

clear_button = tk.Button(button_frame, text="C", width=10, height=4, command = clear)
clear_button.grid(row=3, column = 0)

equals_button = tk.Button(button_frame, text="=", width=10, height=4, command = equals)
equals_button.grid(row=3, column = 2)

button_frame.pack()

root.mainloop()
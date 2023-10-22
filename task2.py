import tkinter as tk

def add_digit(digit):
    current_text = input_variable.get()
    if current_text == "0":
        input_variable.set(digit)
    else:
        input_variable.set(current_text + digit)

def clear_input():
    input_variable.set("0")

def perform_calculation():
    try:
        expression = input_variable.get()
        result = eval(expression)
        input_variable.set(result)
    except Exception as e:
        input_variable.set("Error")

app = tk.Tk()
app.title("Calculator")

input_variable = tk.StringVar()
input_variable.set("0")

start = tk.Entry(app, textvariable=input_variable, font=("Helvetica", 24), justify="right")
start.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0

for button_text in buttons:
    if button_text == '=':
        tk.Button(app, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=perform_calculation).grid(row=row, column=col)
    elif button_text == 'C':
        tk.Button(app, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=clear_input).grid(row=row, column=col)
    else:
        tk.Button(app, text=button_text, padx=20, pady=20, font=("Helvetica", 18), command=lambda text=button_text: add_digit(text)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

app.mainloop()
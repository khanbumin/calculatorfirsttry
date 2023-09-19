import tkinter as tk

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ""
    except Exception as e:
        input_text.set("Error")
        expression = ""

expression = ""

win = tk.Tk()
win.title("Calculator")

input_text = tk.StringVar()

input_field = tk.Entry(win, textvar=input_text, font=("Helvetica", 24), justify="right")
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(win, text=button, padx=20, pady=20, font=("Helvetica", 18), width=2,
              height=1, command=lambda b=button: btn_click(b) if b != "=" else bt_equal()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(win, text="C", padx=20, pady=20, font=("Helvetica", 18), width=2,
          height=1, command=bt_clear).grid(row=row_val, column=col_val)

win.mainloop()

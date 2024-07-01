import math
import tkinter as tk
from tkinter import messagebox


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def square_root(x):
    return math.sqrt(x)


def power(x, y):
    return math.pow(x, y)


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def log(x, base=10):
    return math.log(x, base)


def show_calculator():
    calculator_window = tk.Toplevel()
    calculator_window.title("Calculator")
    calculator_window.geometry("400x300")  # 창 크기 설정

    def calculate():
        try:
            num1 = float(entry1.get())
            if entry2.get():  # Check if entry2 is not empty
                num2 = float(entry2.get())
            else:
                num2 = None
            operation = operation_var.get()

            result = None  # Initialize result variable

            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
            elif operation == "Square Root":
                result = square_root(num1)
            elif operation == "Power":
                result = power(num1, num2)
            elif operation == "Sin":
                result = sin(num1)
            elif operation == "Cos":
                result = cos(num1)
            elif operation == "Log":
                result = log(num1)

            result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_input_fields(*args):
        operation = operation_var.get()
        if operation in ["Square Root", "Sin", "Cos", "Log"]:
            entry2.config(state='disabled')
            entry2_label.config(state='disabled')
        else:
            entry2.config(state='normal')
            entry2_label.config(state='normal')

    frame = tk.Frame(calculator_window)
    frame.grid(row=0, column=0, padx=10, pady=10)

    tk.Label(frame, text="Number 1").grid(row=0, column=0, pady=5)
    entry1 = tk.Entry(frame)
    entry1.grid(row=0, column=1, pady=5)

    entry2_label = tk.Label(frame, text="Number 2")
    entry2_label.grid(row=1, column=0, pady=5)
    entry2 = tk.Entry(frame)
    entry2.grid(row=1, column=1, pady=5)

    # Operation selection
    operation_var = tk.StringVar(value="Add")
    operation_var.trace("w", update_input_fields)
    operations = ["Add", "Subtract", "Multiply", "Divide", "Square Root", "Power", "Sin", "Cos", "Log"]
    tk.OptionMenu(frame, operation_var, *operations).grid(row=2, column=0, columnspan=2, pady=5)

    # Calculate button
    tk.Button(frame, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)

    # Result display
    result_label = tk.Label(frame, text="Result: ")
    result_label.grid(row=4, column=0, columnspan=2)

# For testing the calculator independently
if __name__ == "__main__":
    root = tk.Tk()
    show_calculator()
    root.mainloop()

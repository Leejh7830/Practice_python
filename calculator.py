import math
import tkinter as tk
from tkinter import messagebox


def square_root(x):
    return math.sqrt(x)


def power(x, y):
    return math.pow(x, y)


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


def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            num = float(input("Enter number: "))
            print(f"Square Root of {num} = {square_root(num)}")

        elif choice == '6':
            num1 = float(input("Enter base: "))
            num2 = float(input("Enter exponent: "))
            print(f"{num1} raised to the power of {num2} = {power(num1, num2)}")

        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() not in ['yes', 'y']:
            break


if __name__ == "__main__":
    calculator()

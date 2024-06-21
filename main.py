import tkinter as tk
from tkinter import messagebox
import calculator
import guess_number
import utils

def main():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("300x200")  # Set the size of the window
    root.eval('tk::PlaceWindow . center')  # Center the window on the screen

    def exit_program():
        root.destroy()

    utils.print_welcome_message()

    # Main menu buttons
    tk.Button(root, text="Use Calculator", command=calculator.show_calculator).pack(pady=10)
    tk.Button(root, text="Play Guess the Number", command=guess_number.guess_number).pack(pady=10)
    tk.Button(root, text="Exit", command=exit_program).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

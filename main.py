import tkinter as tk
from tkinter import messagebox
import calculator
import guess_number
import utils


def main():
    root = tk.Tk()
    root.title("Main Menu")

    def show_guess_number():
        guess_number_window = tk.Toplevel(root)
        guess_number_window.title("Guess the Number")
        guess_number.guess_number()  # You may need to adjust guess_number to work with tkinter.

    def exit_program():
        root.destroy()

    utils.print_welcome_message()

    # Main menu buttons
    tk.Button(root, text="Use Calculator", command=calculator.show_calculator).pack(pady=10)
    tk.Button(root, text="Play Guess the Number", command=show_guess_number).pack(pady=10)
    tk.Button(root, text="Exit", command=exit_program).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()

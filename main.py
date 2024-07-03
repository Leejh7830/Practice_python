import tkinter as tk
from tkinter import messagebox
import calculator
import guess_number
import quiz
import utils

def main():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("300x300")  # Set the size of the window
    root.eval('tk::PlaceWindow . center')  # Center the window on the screen

    def exit_program():
        root.destroy()

    def show_error_message(message):
        messagebox.showerror("Error", message)

    # Print welcome message in GUI
    welcome_message = utils.get_welcome_message()  # assuming this function returns a string
    welcome_label = tk.Label(root, text=welcome_message, wraplength=250, justify="center", font=("Helvetica", 12))
    welcome_label.pack(pady=10)

    # Button design settings
    button_config = {
        "font": ("Helvetica", 14),
        "bg": "lightblue",
        "fg": "darkblue",
        "activebackground": "blue",
        "activeforeground": "white",
        "relief": "raised",
        "bd": 3,
        "width": 20,
    }

    # Main menu button
    try:
        tk.Button(root, text="Use Calculator", command=calculator.show_calculator, **button_config).pack(pady=10)
    except Exception as e:
        show_error_message(f"Failed to load Calculator: {e}")

    try:
        tk.Button(root, text="Play Guess the Number", command=guess_number.guess_number, **button_config).pack(pady=10)
    except Exception as e:
        show_error_message(f"Failed to load Guess the Number: {e}")

    try:
        tk.Button(root, text="Play Quiz", command=quiz.show_quiz, **button_config).pack(pady=10)
    except Exception as e:
        show_error_message(f"Failed to load Quiz: {e}")

    tk.Button(root, text="Exit", command=exit_program, **button_config).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
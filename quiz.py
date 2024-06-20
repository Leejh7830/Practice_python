import tkinter as tk
from tkinter import messagebox

questions = [
    ("What is the capital of France?", "Paris"),
    ("What is 2 + 2?", "4"),
    ("What is the capital of South Korea?", "Seoul"),
]

def show_quiz():
    quiz_window = tk.Toplevel()
    quiz_window.title("Quiz Game")

    current_question = tk.StringVar()
    current_answer = tk.StringVar()
    question_index = 0

    def next_question():
        nonlocal question_index
        if question_index < len(questions):
            question, answer = questions[question_index]
            current_question.set(question)
            current_answer.set(answer)
            question_index += 1
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")
            quiz_window.destroy()

    def check_answer():
        if answer_entry.get().lower() == current_answer.get().lower():
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect.")
        next_question()

    tk.Label(quiz_window, textvariable=current_question).pack(pady=10)
    answer_entry = tk.Entry(quiz_window)
    answer_entry.pack(pady=10)
    tk.Button(quiz_window, text="Submit Answer", command=check_answer).pack(pady=10)

    next_question()

# For testing the quiz independently
if __name__ == "__main__":
    root = tk.Tk()
    show_quiz()
    root.mainloop()
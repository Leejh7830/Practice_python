import random
import time
import tkinter as tk
from tkinter import messagebox

# Guess the Number 게임을 시작하는 함수 정의
def guess_number():
    guess_number_window = tk.Toplevel()  # 새로운 창을 생성
    guess_number_window.title("Guess the Number")  # 창 제목 설정

    number_to_guess = random.randint(1, 1000)  # 1부터 1000 사이의 랜덤 숫자 생성
    attempts = 0  # 시도 횟수를 0으로 초기화
    start_time = time.time()  # 게임 시작 시간을 기록

    # 사용자의 추측을 확인하는 함수 정의
    def check_guess():
        nonlocal attempts  # 외부 함수의 attempts 변수 사용
        try:
            guess = int(entry_guess.get())  # 사용자가 입력한 값을 정수로 변환
            attempts += 1  # 시도 횟수 증가

            if guess < number_to_guess:
                messagebox.showinfo("Result", "Too low! Try again.")  # 추측이 너무 낮음
            elif guess > number_to_guess:
                messagebox.showinfo("Result", "Too high! Try again.")  # 추측이 너무 높음
            else:
                end_time = time.time()  # 게임 종료 시간을 기록
                time_taken = end_time - start_time  # 걸린 시간 계산
                # 정답 맞춤
                messagebox.showinfo("Result", f"Congratulations! You guessed the number in {attempts} attempts and {time_taken:.2f} seconds.")
                guess_number_window.destroy()  # 창 닫기
                return # 창이 닫힌 후에는 아래 코드를 실행하지 않도록 함
            entry_guess.delete(0, tk.END)  # 입력 필드 초기화
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")  # 잘못된 입력 알림
            entry_guess.delete(0, tk.END)  # 입력 필드 초기화

    tk.Label(guess_number_window, text="Guess a number between 1 and 1000:").pack(pady=10)  # 안내 레이블 추가
    entry_guess = tk.Entry(guess_number_window)  # 입력 필드 생성
    entry_guess.pack(pady=5)  # 입력 필드 배치
    tk.Button(guess_number_window, text="Submit Guess", command=check_guess).pack(pady=10)  # 버튼 생성 및 배치

# 독립적으로 테스트할 때 사용하는 코드
if __name__ == "__main__":
    root = tk.Tk()  # 메인 루트 윈도우 생성
    guess_number()  # guess_number 함수 호출
    root.mainloop()  # Tk 이벤트 루프 시작

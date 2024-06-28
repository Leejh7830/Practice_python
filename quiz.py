import tkinter as tk
from tkinter import messagebox
import random

# 질문과 정답 리스트
questions = [
    ("프랑스의 수도는?", ["파리"]),
    ("대한민국의 수도는?", ["서울"]),
    ("미국의 수도는?", ["워싱턴 D.C.", "워싱턴D.C", "워싱턴DC", "워싱턴 디씨", "워싱턴", "워싱턴디씨"]),
    ("일본의 수도는?", ["도쿄"]),
    ("중국의 수도는?", ["베이징", "북경"]),
    ("러시아의 수도는?", ["모스크바"]),
    ("독일의 수도는?", ["베를린"]),
    ("영국의 수도는?", ["런던"]),
    ("이탈리아의 수도는?", ["로마"]),
    ("캐나다의 수도는?", ["오타와"]),
    ("호주의 수도는?", ["캔버라", "켄버라"]),
    ("브라질의 수도는?", ["브라질리아"]),
    ("인도의 수도는?", ["뉴델리"]),
    ("스페인의 수도는?", ["마드리드"]),
    ("멕시코의 수도는?", ["멕시코시티", "멕시코 시티"])
]

# 퀴즈 게임 시작
def show_quiz():
    root.withdraw()  # 메인 Tk 윈도우 숨기기
    quiz_window = tk.Toplevel()  # 새로운 창 생성
    quiz_window.title("Quiz Game")  # 창 제목 설정
    quiz_window.geometry("400x200")  # 창 크기 설정

    current_question = tk.StringVar()  # 현재 질문을 저장하는 StringVar 객체
    current_answers = []  # 현재 정답들을 저장하는 리스트
    remaining_questions = questions.copy()  # 남은 질문 리스트를 초기화
    random.shuffle(remaining_questions)  # 질문을 랜덤으로 섞음

    # 다음 질문을 설정하는 함수
    def next_question():
        if remaining_questions:  # 남은 질문이 있는지 확인
            question, answers = remaining_questions.pop()  # 남은 질문에서 하나를 가져옴
            current_question.set(question)  # 현재 질문을 설정
            current_answers.clear()  # 현재 정답 리스트 초기화
            current_answers.extend(answers)  # 현재 정답 리스트 설정
            answer_entry.delete(0, tk.END)  # 입력 필드 초기화
            answer_entry.focus_set()  # 입력 필드에 포커스를 설정하여 활성화
        else:
            messagebox.showinfo("Quiz Completed", "You have completed the quiz!")  # 퀴즈 완료 메시지 표시
            quiz_window.destroy()  # 창 닫기

    def show_hint():
        if current_answers:
            hint = f"The answer has {len(current_answers[0])} letters."
            messagebox.showinfo("Hint", hint)

    # 사용자의 답변을 확인하는 함수
    def check_answer(event=None):  # 이벤트 매개변수를 추가하여 엔터 키 이벤트를 처리
        user_answer = answer_entry.get().lower().strip()
        if user_answer in [ans.lower() for ans in current_answers]:  # 사용자의 답변을 소문자로 변환하여 확인
            messagebox.showinfo("Correct", "Your answer is correct!")  # 정답 메시지 표시
        else:
            messagebox.showerror("Incorrect", f"Your answer is incorrect. Correct answers: {', '.join(current_answers)}")  # 오답 메시지 표시
        quiz_window.after(500, next_question)  # 1초 후에 다음 질문으로 이동

    tk.Label(quiz_window, textvariable=current_question, font=("Helvetica", 14)).pack(pady=10)  # 질문을 표시하는 레이블 생성 및 배치
    answer_entry = tk.Entry(quiz_window, font=("Helvetica", 14))  # 답변을 입력할 수 있는 입력 필드 생성
    answer_entry.pack(pady=10)  # 입력 필드 배치
    answer_entry.bind("<Return>", check_answer)  # 엔터 키 이벤트를 check_answer 함수에 바인딩
    tk.Button(quiz_window, text="Submit Answer", command=check_answer, font=("Helvetica", 14)).pack(pady=10)  # 답변 제출 버튼 생성 및 배치
    tk.Button(quiz_window, text="Show Hint", command=show_hint, font=("Helvetica", 14)).pack(pady=10)

    next_question()  # 첫 질문을 표시

# # For testing the quiz independently
# if __name__ == "__main__":
#     root = tk.Tk()
#     show_quiz()
#     root.mainloop()

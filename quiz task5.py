import tkinter as tk
from tkinter import messagebox
import random

# Quiz questions and answers
quiz_questions = {
    "What is the capital of France?": "Paris",
    "What is the largest planet in our solar system?": "Jupiter",
    "Which programming language is known for its simplicity and readability?": "Python",
    "Fill in the blank: The Earth rotates on its ________ axis.": "axis"
}

class QuizApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz Game")
        self.geometry("500x300")
        self.score = 0
        self.current_question_index = 0

        self.welcome_label = tk.Label(self, text="Welcome to the Quiz Game!", font=("Helvetica", 16))
        self.welcome_label.pack(pady=10)

        self.instruction_label = tk.Label(self, text="You will be presented with multiple-choice and fill-in-the-blank questions.", font=("Helvetica", 12))
        self.instruction_label.pack(pady=10)

        self.start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz, font=("Helvetica", 14))
        self.start_button.pack(pady=20)

        self.result_label = tk.Label(self, text="", font=("Helvetica", 14))

    def start_quiz(self):
        self.start_button.pack_forget()
        self.result_label.pack(pady=10)

        self.current_question_index = 0
        self.score = 0
        self.ask_question()

    def ask_question(self):
        if self.current_question_index < len(quiz_questions):
            question = list(quiz_questions.keys())[self.current_question_index]
            self.display_question(question)
        else:
            self.display_final_results()

    def display_question(self, question):
        self.clear_widgets()

        self.question_label = tk.Label(self, text=question, font=("Helvetica", 14))
        self.question_label.pack(pady=10)

        self.user_answer = tk.StringVar()
        self.user_answer_entry = tk.Entry(self, textvariable=self.user_answer, font=("Helvetica", 12))
        self.user_answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer, font=("Helvetica", 12))
        self.submit_button.pack()

    def check_answer(self):
        question = list(quiz_questions.keys())[self.current_question_index]
        correct_answer = quiz_questions[question].lower()
        user_answer = self.user_answer.get().strip().lower()

        if user_answer == correct_answer:
            self.score += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.result_label.config(text=f"Wrong! The correct answer is: {quiz_questions[question]}", fg="red")

        self.current_question_index += 1
        self.after(1500, self.ask_question)

    def display_final_results(self):
        self.clear_widgets()

        total_questions = len(quiz_questions)
        percentage = (self.score / total_questions) * 100

        self.final_result_label = tk.Label(self, text=f"Quiz Finished!\nYou scored {self.score} out of {total_questions} questions.\nYour performance: {percentage:.2f}%", font=("Helvetica", 14))
        self.final_result_label.pack(pady=20)

        self.play_again_button = tk.Button(self, text="Play Again", command=self.play_again, font=("Helvetica", 12))
        self.play_again_button.pack()

    def play_again(self):
        self.final_result_label.pack_forget()
        self.play_again_button.pack_forget()
        self.result_label.pack_forget()

        self.start_button.pack(pady=20)

    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()

if __name__ == "__main__":
    app = QuizApplication()
    app.mainloop()

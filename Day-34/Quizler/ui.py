from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizlerApp")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_text = Label(text=f"Score: {self.quiz.score}/{self.quiz.question_number}", fg="white", bg=THEME_COLOR)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Questions",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.corr_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")

        self.corr_button = Button(image=self.corr_img, command=self.true_pressed)
        self.corr_button.config(padx=20, pady=20, highlightthickness=0)
        self.corr_button.grid(row=2, column=0)

        self.wrong_button = Button(image=self.wrong_img, command=self.false_pressed)
        self.wrong_button.config(padx=20, pady=20, highlightthickness=0)
        self.wrong_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizz!")
            self.corr_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
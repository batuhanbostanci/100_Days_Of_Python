from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for que in question_data:
    questions = Question(que["question"], que["correct_answer"])
    question_bank.append(questions)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print("\nYou've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
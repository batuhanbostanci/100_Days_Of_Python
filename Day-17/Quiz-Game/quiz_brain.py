class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number}: {current_question.text} (True/False): ")
        correct_answer = current_question.answer
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, useranswer, correct_answer):
        if useranswer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
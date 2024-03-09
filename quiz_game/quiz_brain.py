class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0 #default starting value
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list) #already a bool value

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").title()
        self.check_answer(current_question.answer, user_answer)

    def check_answer(self, correct_a, user_a):
        correct_answer = correct_a
        user_answer = user_a

        if correct_answer == user_answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
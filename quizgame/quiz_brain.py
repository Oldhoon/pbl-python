class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0

    def next_question(self):
        question = self.questions_list[self.question_number]
        text = question.text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {text}. (True/False)?: ")
        self.check_answer(user_answer, question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")

    def still_has_questions(self):
        if len(self.questions_list) > self.question_number:
            return True
        return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")


from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for pair in question_data:
    text = pair["text"]
    answer = pair["answer"]
    question_bank.append(Question(text, answer))


quiz = QuizBrain(question_bank)

score = 0
while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score is {quiz.score}")

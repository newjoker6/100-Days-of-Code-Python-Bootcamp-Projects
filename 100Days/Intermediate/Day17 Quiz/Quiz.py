import data
from QuestionClass import Question
from QuizBrain import QuizBrain


question_bank = []


for q in data.question_data:
    text = q['text']
    answer = q['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Your final score was {quiz.score}/{len(quiz.questions_list)}")


class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0


    def still_has_questions(self):
        if not self.question_number == len(self.questions_list):
            return True


    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.questions_list[self.question_number].text} (True/False)? ").lower().capitalize()
        self.check_answer(user_answer)
        self.question_number += 1


    def check_answer(self, user_answer):
        if user_answer == self.questions_list[self.question_number].answer:
            self.score += 1
            print("You got it right!")
        print(f"The correct answer is {self.questions_list[self.question_number].answer}")
        print("\n")
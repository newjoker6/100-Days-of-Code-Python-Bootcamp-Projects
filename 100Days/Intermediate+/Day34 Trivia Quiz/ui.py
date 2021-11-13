from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz =quiz_brain

        self.root = Tk()
        self.root.title("Quiz Test")
        self.windowWidth = self.root.winfo_reqwidth()
        self.windowHeight = self.root.winfo_reqheight()
        self.positionRight = int(self.root.winfo_screenwidth()/2 - self.windowWidth)
        self.positionDown = int(self.root.winfo_screenheight()/2 - self.windowHeight)
        self.root.geometry(f"+{self.positionRight}+{self.positionDown}")
        self.root.config(padx=20, pady=20, bg= THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.Score_label = Label(bg= THEME_COLOR, fg="white", text="Score: 0", font=("Arial", 12, "normal"))
        self.Score_label.grid(column=1, row=0)

        self.q_text = self.canvas.create_text(150, 125, width = 280, text="", font=("Arial", 20, "italic"))

        self.yes_button_img = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=self.yes_button_img, borderwidth=0, bg=THEME_COLOR, command=self.answer_true)
        self.yes_button.grid(column=0, row=2, pady=40, padx=20)

        self.no_button_img = PhotoImage(file="images/false.png")
        self.no_button = Button(image=self.no_button_img, borderwidth=0, bg=THEME_COLOR, command=self.answer_false)
        self.no_button.grid(column=1, row=2, pady=40, padx=20)

        self.get_next_question()



        self.root.mainloop()

    def get_next_question(self):
        self.change_bg("white")
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text= question_text)
            self.Score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.q_text, text="You've reached the end of the quiz!")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def answer_false(self):
        is_right =  self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right == False:
            self.change_bg("red")
        elif is_right == True:
            self.change_bg("green")

        self.root.after(1000, self.get_next_question)


    def change_bg(self, colour):
        self.canvas.config(bg=f"{colour}")

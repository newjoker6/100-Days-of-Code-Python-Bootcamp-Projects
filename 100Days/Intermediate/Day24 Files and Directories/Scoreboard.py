from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.up()
        self.goto(0, 260)
        self.get_highscore()
        self.update_scoreboard()
        self.hideturtle()


    def get_highscore(self):
        file = open("data.txt", "r")
        self.highscore = int(file.read())
        file.close()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt", "w")
            file.write(str(self.highscore))
            file.close()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align=ALIGNMENT, font=FONT)
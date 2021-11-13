from turtle import Turtle


FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.up()
        self.goto(-250, 280)
        self.show_level()
        self.hideturtle()


    def show_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 24, "bold"))

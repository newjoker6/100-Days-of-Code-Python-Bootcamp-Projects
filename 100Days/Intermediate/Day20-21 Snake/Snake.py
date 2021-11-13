from turtle import Screen
import time
from SnakeClass import Snake
from Food import Food
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

Snake = Snake()
Food = Food()
Scoreboard = Scoreboard()

screen.listen()
screen.onkey(Snake.up, "w")
screen.onkey(Snake.down, "s")
screen.onkey(Snake.left, "a")
screen.onkey(Snake.right, "d")


screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    Snake.move()

    if Snake.head.distance(Food) < 14:
        Food.refresh()
        Scoreboard.increase_score()
        Snake.extend()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -280 or Snake.head.ycor() > 280 or Snake.head.ycor() < -280:
        game_is_on = False

    for segment in Snake.segments[1:]:
        if Snake.head.distance(segment) < 10:
            game_is_on = False

Scoreboard.game_over()

screen.exitonclick()

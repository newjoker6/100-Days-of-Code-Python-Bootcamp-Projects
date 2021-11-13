import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400)
screen.title("Turtle Race")

colours = ["green", "red", "orange", "yellow", "pink", "blue"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.up()
    new_turtle.color(colours[i])
    new_turtle.goto(-230, y_pos[i])
    all_turtles.append(new_turtle)

user_bet = screen.textinput("Place your bet!", "Which colour turtle will win?").lower()


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You win! {winning_colour} won the race!")
            else:
                print(f"Fuckin loser! {winning_colour} won")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
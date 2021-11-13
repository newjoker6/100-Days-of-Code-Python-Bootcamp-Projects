from RGBExtractor import colour_list
from turtle import Turtle, Screen
import random

Sam = Turtle()
screen = Screen()
print(colour_list)


def hirst_painting():
    screen.colormode(255)
    for x in range(10):
        new_colour = random.choice(colour_list)
        Sam.pencolor(new_colour)
        Sam.fillcolor(new_colour)
        Sam.speed(100)
        Sam.begin_fill()
        Sam.circle(20)
        Sam.end_fill()

        Sam.up()
        Sam.forward(100)
        Sam.down()

    Sam.up()
    Sam.setx(-400)
    Sam.sety(Sam.ycor() + 100)
    Sam.down()


Sam.shape('turtle')
screen.bgcolor("darkgrey")
Sam.up()
Sam.setx(-400)
Sam.sety(-500)
Sam.down()
Sam.hideturtle()

for y in range(10):
    hirst_painting()


screen.exitonclick()
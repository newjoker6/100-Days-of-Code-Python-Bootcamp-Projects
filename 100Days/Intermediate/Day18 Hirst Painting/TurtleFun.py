from turtle import Turtle, Screen
import random

Laure = Turtle()
screen = Screen()

Laure.shape("turtle")
Laure.color('blue')


def draw_square(length):
    for i in range(4):
        Laure.forward(length)
        Laure.left(90)


def draw_dash(paces, linecount):
    for i in range(linecount):
        Laure.pendown()
        Laure.forward(paces)
        Laure.penup()
        Laure.forward(paces / 2)


def draw_shape(sides, length):
    for i in range(sides):
        Laure.down()
        Laure.forward(length)
        Laure.right(360 / sides)


def random_pen():
    screen.colormode(255)
    Laure.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))


def set_position(x, y):
    Laure.up()
    Laure.setx(x)
    Laure.sety(y)


def move_direction(length, movements):
    for i in range(movements):
        random_pen()
        turn = random.choice(["Left", "Right", "none"])
        if turn == "Left":
            Laure.left(90)
            direction = random.randint(1, 2)
            if direction == 1:
                Laure.forward(length)
            elif direction == 2:
                Laure.backward(length)
        if turn == "Right":
            Laure.right(90)
            direction = random.randint(1, 2)
            if direction == 1:
                Laure.forward(length)
            elif direction == 2:
                Laure.backward(length)
        else:
            direction = random.randint(1, 2)
            if direction == 1:
                Laure.forward(length)
            elif direction == 2:
                Laure.backward(length)


def spirograph(amount, angle):
    Laure.hideturtle()
    for i in range(amount):
        random_pen()
        Laure.speed(100)
        Laure.circle(100)
        Laure.right(angle)


# Laure.pensize(2)
spirograph(100, 5)


screen.exitonclick()

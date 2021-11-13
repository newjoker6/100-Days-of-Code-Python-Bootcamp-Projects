from turtle import Turtle, Screen

Sam = Turtle()
Sam.pensize(2)
Screen = Screen()

def forward():
    Sam.forward(10)


def backward():
    Sam.backward(10)

def clockwise():
    Sam.right(10)

def counter_clockwise():
    Sam.left(10)

def clear():
    Screen.reset()

Screen.listen()

Screen.onkey(key="w", fun=forward)
Screen.onkey(key="s", fun=backward)
Screen.onkey(key="d", fun=clockwise)
Screen.onkey(key="a", fun=counter_clockwise)
Screen.onkey(key="c", fun=clear)

Screen.exitonclick()
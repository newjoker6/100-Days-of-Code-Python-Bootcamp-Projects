import turtle as t
import pandas

screen = t.Screen()
screen.title("U.S. 50 States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)


data = pandas.read_csv("50_states.csv")
score = 0

scorelabel = t.Turtle()
scorelabel.up()
scorelabel.hideturtle()
scorelabel.goto(100, -200)
scorelabel.write(f"States Right: {score}/50", False, align="center", font=("Courier", 10, "bold"))


def update_score():
    scorelabel.clear()
    scorelabel.write(f"States Right: {score}/50", False, align="center", font=("Courier", 10, "bold"))

def win():
    win = t.Turtle()
    win.up()
    win.hideturtle()
    win.write(f"ALL STATES GUESSED", False, align="center", font=("Courier", 32, "bold"))


game_is_on = True

while game_is_on:
    if score == 50:
        game_is_on = False
        win()

    else:
        answer_state = screen.textinput("Guess a State", "What's another state name?").lower()
        for state in data.state:
            if answer_state == state.lower():
                label = t.Turtle()
                label.up()
                x_cor = int(data[(data.state == state)]["x"])
                y_cor = int(data[(data.state == state)]["y"])
                label.goto(x_cor, y_cor)
                label.hideturtle()
                label.write(str(state), False, align="center", font=("Courier", 8, "bold"))
                score += 1
                update_score()




t.mainloop()

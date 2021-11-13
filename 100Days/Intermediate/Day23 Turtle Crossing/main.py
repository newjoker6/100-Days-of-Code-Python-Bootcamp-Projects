import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False

    if player.ycor() >= 250:
        carmanager.level_up()
        scoreboard.increase_level()
        player.restart()

scoreboard.game_over()

screen.exitonclick()
import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=turtle.move, key="Up")
screen.onkeypress(fun=turtle.move, key="w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    rand = random.randint(1,6)
    if rand == 1:
        cars.create_car()

    cars.move_car()
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            game_is_on = False
            score.game_over()

    if turtle.next_level_check():
        turtle.reset()
        cars.next_level()
        score.level_up()

screen.exitonclick()



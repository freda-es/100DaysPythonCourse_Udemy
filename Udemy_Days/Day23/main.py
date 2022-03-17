import time
from turtle import Screen
from player import Player
from Cars import CarManager
# from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
car.car()
player = Player((0, -280))
screen.listen()
screen.onkey(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
    
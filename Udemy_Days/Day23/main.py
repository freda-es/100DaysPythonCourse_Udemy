import time
from turtle import Screen
from scores import ScoreBoard
from player import Player
from Cars import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
score = ScoreBoard()
player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car()
    car.move_cars()
    for al_cars in car.all_cars:
        if al_cars.distance(player)<=15:
            game_is_on = False
            score.game_over()
    if player.ycor()==290:
        score.calc_points()   
        
        
screen.exitonclick()
    
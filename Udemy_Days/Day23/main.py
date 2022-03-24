import time
from turtle import Screen
from scores import ScoreBoard
from player import Player
from Cars import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#call all the classes
car = CarManager()
score = ScoreBoard()
player = Player()

#give function to the keyboard to move the turtle only up
screen.listen()
screen.onkey(player.move_up, "Up")

#begin the game
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.car()
    car.move_cars()
    
    #control the collapse of the turtle with the cars
    for al_cars in car.all_cars:
        if al_cars.distance(player)<=10:
            game_is_on = False
            score.game_over()
    #if the turtle arrives in front of the other wall it goes to the other level and speed up the speed
    if player.ycor()==290:
        score.calc_points() 
        car.level_up()  
        
        
screen.exitonclick()
    
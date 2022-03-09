from turtle import Turtle, Screen
import time
from snake import Snake

#setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)# the tracer is off, the screen doesn't show anything, blackscreen

#call the Snake class and crate the snake object
snake = Snake()
screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')  
#create a variable to use for the while loop of the snake walk
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.SnakeMove()
       
        








screen.exitonclick()
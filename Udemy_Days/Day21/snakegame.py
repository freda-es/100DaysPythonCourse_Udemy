from turtle import  Screen
import time
from snake import Snake
from food import  Food
from scoreboard import ScoreBoard

#setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)# the tracer is off, the screen doesn't show anything, blackscreen

#call the classes and create the objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

#controll the movement of the snake with the array buttons in the keyboard
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
    #Detect collision with food with the "distance" method, choose the 15 
    # number according to the size shpae of food and the snake and extend after eating food (the snake touches the food)
    if snake.head.distance(food) <15:
        food.refresh()#goes to another position
        snake.extend()#extend +1
        scoreboard.calc_points() #refresh the points adn the message on the screen
        
    #Detect collision with the wall:
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over() # call the method of the text game over
        
        
    #Detect collision with the tail:,if head collides with any segment in the tail: trigger game over
    for segment in snake.the_segments[1:]:
        if snake.head.distance(segment)<10: #if the distance of the head and of any segment in th_segments is less than 10
            game_is_on = False
            scoreboard.game_over()
            
       
        








screen.exitonclick()
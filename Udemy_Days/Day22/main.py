from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from Scores import ScoreBoard
from screen import MyScreen
import time

#setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)# the tracer is off, the screen doesn't show anything, blackscreen

my_screen = MyScreen()
ball = Ball()
r_score = ScoreBoard((50, 230))
l_score = ScoreBoard((-50,230))
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "d")

game_is_on = True
while game_is_on:
    time.sleep(0.022)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320: 
        ball.bounce_x()
        r_score.calc_points() 
    
    #Detect collision with l_paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320: 
        ball.bounce_x()
        l_score.calc_points()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_post()
        l_score.calc_points()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_post()
        r_score.calc_points()

screen.exitonclick()
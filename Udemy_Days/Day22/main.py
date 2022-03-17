from turtle import  Turtle, Screen
import time
from screen import MyScreen

#setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)# the tracer is off, the screen doesn't show anything, blackscreen
my_screen = MyScreen()
tim = Turtle()
tim.pendown()
tim.shape("square")
tim.shapesize(20)
tim.color("red")


screen.exitonclick()
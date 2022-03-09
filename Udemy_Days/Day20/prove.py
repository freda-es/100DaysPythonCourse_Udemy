from turtle import Turtle, Screen

#setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("The Snake Game")

tim = Turtle()

def move_up():
    tim.setheading(90)
    tim.forward(20)
def move_down():
    tim.setheading(270)
    tim.forward(20)
def move_left():
    tim.setheading(180)
    tim.forward(20)
def move_right():
    tim.setheading(0)
    tim.forward(20)
 
screen.listen()
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(move_left, 'Left')
screen.onkey(move_right, 'Right')
screen.exitonclick()
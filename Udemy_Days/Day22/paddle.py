
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup() 
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)
        
    #give function to the buttons of the keyboard to move the paddles up and down     
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

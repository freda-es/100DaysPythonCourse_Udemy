from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup() 
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(position)
            
    def move_up(self):
        if self.ycor() <= FINISH_LINE_Y:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)
        else:
            self.goto(STARTING_POSITION)

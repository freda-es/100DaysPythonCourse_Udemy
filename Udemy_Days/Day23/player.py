from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        #create the turtle 
        super().__init__()
        self.penup() 
        self.shape("turtle")
        self.color("black")
        self.left(90)
        self.goto(STARTING_POSITION)

        
    #function to move the turtle
    def move_up(self):
        if self.ycor() <= FINISH_LINE_Y: #continue the loop until it collapse with the front wall
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(),new_y)
        else: # if collpase with the front wall goes at starting position to continue from the begining again
            self.goto(STARTING_POSITION)
            
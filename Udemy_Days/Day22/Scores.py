from turtle import Turtle, position

from numpy import size

#constants
ALIGNMENT = "center"
FONT = ('Arial', 40, 'bold')

class ScoreBoard(Turtle):
    
    def  __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.point = 0
        self.goto(position)
        self.write(f"{self.point}", align=ALIGNMENT, font=FONT)
        
    #increase the scores     
    def calc_points (self):
        self.clear()
        self.point += 1
        if position == (0,0):
            self.point += 0            
        self.write(f"{self.point}", align=ALIGNMENT, font=FONT)
    
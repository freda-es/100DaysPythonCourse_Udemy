from turtle import Turtle
ALIGNMENT = "Center"
FONT = ('Arial', 7, 'bold')


class State_OnMap(Turtle):
    def __init__(self, position, answer_right):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(position) 
        self.write(f"{answer_right}", align=ALIGNMENT, font=FONT)   
        

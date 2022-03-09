from turtle import Turtle

#constants
ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')

class ScoreBoard(Turtle):
    
    #the text of the "Score 0" is as a turtle with its settings
    #here we declare and tha variable points=0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.point = 0
        self.write(f"Score: {self.point}", align=ALIGNMENT, font=FONT)

    #this calculate the points of eatch time snake its the food (at tha main program) becouse we call this method    
    def calc_points (self):
        self.clear()
        self.point += 1
        self.write(f"Score: {self.point}", align=ALIGNMENT, font=FONT)

    #the text of the game over in the center of the screen
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
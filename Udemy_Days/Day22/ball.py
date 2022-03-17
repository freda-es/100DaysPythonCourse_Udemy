from turtle import Turtle

#Inherit from the Turtle class so the food can be considerd as a turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("white")
        self.goto(0,0)
        self.x_move = 3
        self.y_move = 3
        self.speed_move = 0.1
        self.move()
     
    #determine how the ball will move in the screen   
    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new,y_new)
    
    #bounce when collapse with the walls
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1
        self.speed_move *= 0.9
    def reset_post(self):
        self.goto(0,0)
        self.speed_move *= 0.1
        self.bounce_x()


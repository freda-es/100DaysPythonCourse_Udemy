from turtle import Turtle
class MyScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, -280)
        self.setheading(270)
        for _ in range(29):
            self.pendown()
            self.backward(10)
            self.penup()
            self.backward(10)

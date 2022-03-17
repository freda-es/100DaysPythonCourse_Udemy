COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle, goto
import random

class CarManager:
    
    def __init__(self):
        self.color = random.choice(COLORS)
        self.position = (200,20)
    
    def car(self):
        self.car = Turtle(shape="square")
        self.car.penup()
        self.car.right(90)
    # car.shapesize(stretch_len=0.5, stretch_wid=3)    
        self.car.color(self.color)
        self.car.goto(self.position)

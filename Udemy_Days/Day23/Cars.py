COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle, goto
import random

class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed  = STARTING_MOVE_DISTANCE

    
    def car (self):       
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            #we make this 'if' because it can create one car every time the chance is equal=1 and not every time the screen refreshes
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=0.7)    
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(280,random_y)
            self.all_cars.append(car)

    #every car created can move with the distance=5 for the first level completed
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)
    
    #after eatch level the speed goes +10 to make more difficult      
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

            
            
            
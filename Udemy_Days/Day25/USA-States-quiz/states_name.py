from turtle import Turtle

class State_OnMap(Turtle):
    def __init__(self):
        self.position = (0,0)
    
    def state_name(self,answer_right):
        state_name = Turtle()
        state_name.penup() 
        state_name.write(f"{answer_right}")        
        state_name.goto(self.position) 

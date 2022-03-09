MOVE_DISTANCE = 20 #declare a constant variable
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

from turtle import Turtle, Screen
class Snake:
    def __init__(self):
        self.the_segments = []
        self.SnakeBody()
        self.screen = Screen()
        self.head = self.the_segments[0]
        
    #crate the body of the snake mettod    
    def SnakeBody(self):
        for position in STARTING_POSITION:
            the_squares = Turtle(shape="square")
            the_squares.penup()
            the_squares.color("white")
            the_squares.goto(position)
            self.the_segments.append(the_squares)
           #crate the movement of the snake method
    def SnakeMove(self):
        #move the squares in mode that the last one goes to the previous one
        for seg_num in range(len(self.the_segments) -1, 0, -1):
            new_x= self.the_segments[seg_num-1].xcor()
            new_y= self.the_segments[seg_num-1].ycor()
            self.the_segments[seg_num].goto(new_x,new_y)
        self.the_segments[0].forward(MOVE_DISTANCE)
         
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    

    


#####Turtle Intro######

import random
from ssl import DER_cert_to_PEM_cert
import turtle as t
tim = t.Turtle()
screen = t.Screen
t.colormode(255)


# ######## Challenge 1 - Draw a Square ############
# for _ in range (4):
#     tim.forward(100)
#     tim.left(90)


########### Challenge 2 - Draw a Dashed Line ########
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

########### Challenge 3 - Draw Shapes ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# def draw (side):
#     angle = int(360 /side) 
#     for _ in range(side):
#         tim.forward(50)
#         tim.left(angle)
    

# for side in range(3,11):
#     tim.color(random.choice(colours))
#     draw(side)


########### Challenge 4 - Random Walk ########
# direction = [0, 90, 180, 270]
 
# def random_move(): 
#     tim.color(random_color())   
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     colours = (r,g,b)
#     return colours
    
# tim.pensize(3)
# tim.speed(3)  
# for _ in range (100):
#     random_move()

########### Challenge 5 - Spirograph ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

t.speed("fastest")
t.hideturtle()
t.exitonclick()
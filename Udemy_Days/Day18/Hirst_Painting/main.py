###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##



###----------Import a list of colors from a image----------###
# from typing import Tuple
# import colorgram
# colors = colorgram.extract('C:\\Users\\esoft\\Code\\Udemy\\Day18\\Hirst_Painting\\image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     rgb_colors.append(color)    
# rgb_color= [] 
# rgb_tuple = []
# for i in range(len(rgb_colors)):
#     rgb_color.append(rgb_colors[i].rgb)
#     rgb_tuple.append((rgb_color[i].r,rgb_color[i].g,rgb_color[i].b))
# print(rgb_tuple)
###------We can run the above code everytime we want to generate a new list of colors-----------###

import random
import turtle as t
tim = t.Turtle()
screen = t.Screen
tim.penup()
t.colormode(255)
t.speed("fastest")
tim.hideturtle()

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

def draw_dots():
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)

def draw_hirst():
    i = 50
    for _ in range(10):
        draw_dots()
        tim.goto(0,i)
        i += 50

draw_hirst()
        

t.exitonclick()
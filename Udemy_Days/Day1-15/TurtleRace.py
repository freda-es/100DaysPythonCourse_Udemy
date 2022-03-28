from turtle import Turtle, Screen
import random
import turtle

#screen settings
screen = Screen()
screen.setup(width=500,height=400)

#the variables needed to build the race
is_race_on = False #a variable to loop the walk aof tha turtles
user_bet = screen.textinput(title="Make your bet", prompt = "Whitch turtle will win the race? Enter the colour:")# the user input to bet which color will win
colors = ['red', 'orange', 'yellow', "green", "blue","purple"]# the colors of the turtles
y_posit = [-70, -40, 0, 40, 70, 100] #the position of tha start
all_turtles=[]

#generate 6 turtles in the race
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, y_posit[i])
    all_turtles.append(new_turtle)
    
#if the promt gest a value the race begin so the varibale is_race_on gets true   
if user_bet:
    is_race_on = True
 
#begin the loop of the race   
while is_race_on:
    #loop through the turtles generated above
    for turtle in all_turtles:
        if turtle.xcor() > 230: #if arrives the finish whitch is the coordinate of the x(tha same as the half of parameters of the screen) stops
            is_race_on = False
            wining_color = turtle.pencolor()
            #the if which controlls if the user bet has won or no
            if wining_color == user_bet:
                print(f"You won, The winning color is {wining_color}!")
            else:
                print(f"You lost, The winning color is {wining_color}!")
        #the random walk of the turtles    
        rand_distc = random.randint(0,10)
        turtle.forward(rand_distc)
      
    
screen.exitonclick()

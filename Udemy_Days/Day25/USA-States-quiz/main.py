import turtle
import pandas
from states_name import State_OnMap

# setting up the screen with the map of usa and the littel 
# prompt where the user will enter his guessing state
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\USA-States-quiz\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pandas.read_csv("Udemy_Days\\Day25\\USA-States-quiz\\50_states.csv")
state_n = State_OnMap()
game_is_on = True

# while game_is_on:   
answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?").lower()
the_state = states['state']
for statess in the_state:
    if answer_state == statess.lower():
        state_n(answer_state)
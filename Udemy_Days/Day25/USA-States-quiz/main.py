import turtle
import pandas
from states_name import State_OnMap

# setting up the screen with the map of usa and the little 
# prompt where the user will enter his guessing state
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "C:\\Users\\esoft\\Documents\\GitHub\\100DaysPythonCourse_Udemy\\Udemy_Days\\Day25\\USA-States-quiz\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read the states file from csv
states = pandas.read_csv("Udemy_Days\\Day25\\USA-States-quiz\\50_states.csv")

#declare a liste where to put the correct answers to loop through later on
correct_guess = []

#tha game will continue until the player guesses all the states
while len(correct_guess) <= 50: 
    #the textinput for the player    
    answer_state = turtle.textinput(title=f"{len(correct_guess)}/50 States correct", prompt="What's another state's name?").title()
    
    #from our data frame with the states and coordinates extract only the column state and save it as a list
    the_state = states['state'].to_list()
    
    #if the player wants to quit the game
    if answer_state == "Exit":
        #with the lista comprehension we create the list with the states not guessed when the player finishes the game
        missing_states = [state for state in the_state if state not in correct_guess]
        print(missing_states)
        #create a dataframe with this list and then save it as ea csv file    
        data_states = pandas.DataFrame(missing_states)
        data_states.to_csv("Udemy_Days\\Day25\\USA-States-quiz\\states_to_learn.csv")
        break
    
    #the control if the answer is correct or no (going through the states and control if the answer's there)
    if answer_state in the_state: 
        #the method to extract the value of the two columns x,y fro the state guessed correct            
        x_post = states.loc[states['state'] == answer_state]['x'].values
        y_post = states.loc[states['state'] == answer_state]['y'].values
        #the turtle that makse the procedure of writing the state over the map in its position
        State_OnMap((x_post[0],y_post[0]),answer_state)
        correct_guess.append(answer_state)
    
    
BACKGROUND_COLOR = "#B1DDC6"
from tkinter  import *
import pandas
import random

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

# two global variables for the word that appears in UI and tha dicionary that has the words not appeared
current_word = {}
to_learn = {}

#read the file to_learn, for the first time is the original file french_word (the excpet part)
try:
    data = pandas.read_csv("Day31\\data\\words_to_learn.csv")
except FileNotFoundError:
    data_words = pandas.read_csv("Day31\\data\\french_words.csv")
    to_learn = data_words.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")    
    


#function of french card appear first
def button_press():   
    global current_word, timer
    window.after_cancel(timer)# stops the loop of french card and appears the english card
    current_word = random.choice(to_learn)#choose a word from the dict that we created with the words that remain after the tick button
    #change the canvas
    canvas.itemconfig(title_text, text="French",fill="black")   
    canvas.itemconfig(word_text, text=f'{current_word["French"]}',fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    #the loop that the french card will stay 3sec and the english card will appear
    timer = window.after(3000,func=english_text)


        
#function of english card   
def english_text():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white",)  
    canvas.itemconfig(word_text, text=f'{current_word["English"]}', fill="white",)

#the function that will execute when the tick button is pressed
#it will remove the word that appears in that moment and refresh the file to_learn.csv
#at the end it will call again the button_press function
def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("Day31\\data\\words_to_learn.csv", index=False)
    button_press()


timer = window.after(3000,func=english_text)

#building the UI with canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="Day31\\images\\card_front.png")
card_back_image = PhotoImage(file="Day31\\images\\card_back.png")
canvas_image = canvas.create_image(410,270,image=card_front_img)
title_text = canvas.create_text(400,150, text= "", fill="black", font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263, text="", fill="black", font=("Ariel",60,"bold"))
canvas.grid(row = 0, column=0,columnspan=2)

#two buttons
wrong_image = PhotoImage(file="Day31\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=button_press)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="Day31\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.config(borderwidth=0)
right_button.grid(row=1,column=1)

button_press()

window.mainloop()
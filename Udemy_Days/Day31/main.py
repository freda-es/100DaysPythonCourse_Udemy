BACKGROUND_COLOR = "#B1DDC6"
from tkinter  import *
import pandas
import random

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

data_words = pandas.read_csv("Day31\\data\\french_words.csv")
dict_words = data_words.to_dict()

def button_press():      
    i=random.randint(0,100)
    french_word = dict_words["French"][i]    
    canvas.itemconfig(wordeng_text, text=french_word)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="Day31\\images\\card_front.png")
canvas.create_image(410,270,image=card_front_img)
english_text = canvas.create_text(400,150, text= "French", fill="black", font=("Ariel",40,"italic"))
wordeng_text = canvas.create_text(400,263, text='', fill="black", font=("Ariel",60,"bold"))
canvas.grid(row = 0, column=0,columnspan=2)


wrong_image = PhotoImage(file="Day31\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=button_press)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="Day31\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0,command=button_press)
right_button.config(borderwidth=0)
right_button.grid(row=1,column=1)






window.mainloop()
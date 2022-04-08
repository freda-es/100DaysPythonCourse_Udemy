BACKGROUND_COLOR = "#B1DDC6"
from tkinter  import *
import pandas
import random



def button_press():   
    global current_word
    global timer
    window.after_cancel(timer)
    current_word = random.choice(dict_words)
    canvas.itemconfig(title_text, text="French",fill="black")   
    canvas.itemconfig(word_text, text=f'{current_word["French"]}',fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    timer = window.after(3000,func=english_text)

        
    
def english_text():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(title_text, text="English", fill="white",)  
    canvas.itemconfig(word_text, text=f'{current_word["English"]}', fill="white",)



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
timer = window.after(3000,func=english_text)

data_words = pandas.read_csv("Day31\\data\\french_words.csv")
dict_words = data_words.to_dict(orient = 'records')
current_word = {}


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="Day31\\images\\card_front.png")
card_back_image = PhotoImage(file="Day31\\images\\card_back.png")
canvas_image = canvas.create_image(410,270,image=card_front_img)
title_text = canvas.create_text(400,150, text= "", fill="black", font=("Ariel",40,"italic"))
word_text = canvas.create_text(400,263, text="", fill="black", font=("Ariel",60,"bold"))
canvas.grid(row = 0, column=0,columnspan=2)


wrong_image = PhotoImage(file="Day31\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0,command=button_press)
wrong_button.config(borderwidth=0)
wrong_button.grid(row=1,column=0)

right_image = PhotoImage(file="Day31\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0,command=button_press)
right_button.config(borderwidth=0)
right_button.grid(row=1,column=1)

button_press()

window.mainloop()
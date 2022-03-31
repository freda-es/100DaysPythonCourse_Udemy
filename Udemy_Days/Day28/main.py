# *****The pomodoro project*****

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

# reset all the widgets we created with the gui section
# its important to reset also the global reps to reset also the start timer function
def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_text.config(text="")
    global reps
    reps=0




# ---------------------------- TIMER MECHANISM ------------------------------- # 

#create a global reps that increases every time the start_timer func is called (the button start)
def start_timer():
    global reps    
    reps += 1
    #convert the minutes in sec
    work_sec= WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    
    #determine when to make the long nd short breakes and when to work
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_text.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_text.config(text="Work", fg=GREEN)
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60) # 4,8 = 4 so we find the minutes
    count_sec = count % 60 #we find the seconds
    if count_sec < 10: #this is called dynamic types : we can cahnge the types of variables, this is to look 5:00
        count_sec = f"0{count_sec}"
    
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}") #changes the text of the canvas over the tomato with the count variable
    if count>0:
        global timer #global becouse we'll use it in another func (reset func, how to reset the canvas of the timer 00:00)
        timer = window.after(1000, count_down, count-1) #after 1 second -1 to the counter
    else: #when the counter==0 call the start time over again
        start_timer()
        marks = ""
        session_work = math.floor(reps/2) #after two times (work+break) one check symbol is added
        for _ in range(session_work):
            marks += "✓"
        tick_text.config(text = marks)    



# ---------------------------- GUI SETUP ------------------------------- #

#create the screen
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)


#the title of the screen:Timer
title_text = Label(text="Timer", font=(FONT_NAME, 30,"bold"), fg=GREEN, bg=YELLOW)
title_text.config(padx=20, pady=20)
title_text.grid(column=2, row=1)

#create canvas so we can put images or text over the screen
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#create a variable that reads the image as a file with the Photoimage func
# tomato_img = PhotoImage(file="Udemy_Days\\Day28\\tomato.png")
# #now we can create the canvas with the tomato image where x=103 and y=112 the position of the image
# canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130, text= "00:00", fill="black", font=(FONT_NAME,35,"bold"))
canvas.grid(column=2, row=2)


#the two click button the start and restart
start_button = Button(text="Start",highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

#the tick text 
tick_text = Label(fg=GREEN,font=(FONT_NAME, 25, "bold"), bg=YELLOW)
tick_text.grid(column=2, row=4)






window.mainloop()
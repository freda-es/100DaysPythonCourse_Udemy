# import quizbrain becouse qe need all the methods there
from quiz_brain import QuizBrain
from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain): # determine a variable whitch is type of Quizbrain class
        self.quiz = quiz_brain # this is the variable that takes the values of all the methods of Quizbrain
        
        # ---Build the UI of our quiz
        # main window
        self.window=Tk()
        self.window.title("Quizzler")
        self.the_score = Label(self.window, text="Score: 0", bg="#375362", foreground="white")
        self.the_score.grid(row = 0, column=1)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        # the canvas whitch contains the questions text
        self.canvas = Canvas(width=300, height=250, bg="white",highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,125, 
            text= "Question here", 
            fill="black", 
            font=("Ariel",20,"italic"),
            width=280)
        self.canvas.grid(row = 1, column=0,columnspan=2,padx=20,pady=20)
        
        # two buttons true and false and their command returns True or False when they pressed
        self.false_image = PhotoImage(file="Day34\\images\\false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0,command=self.false_btt)
        self.false_button.config(borderwidth=0)
        self.false_button.grid(row = 2, column=1)
        
        self.true_image = PhotoImage(file="Day34\\images\\true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.tru_btt)
        self.true_button.config(borderwidth=0)
        self.true_button.grid(row = 2, column=0)
        self.next_quest()
        
        # every method above mainloop if we want to be executed
        self.window.mainloop()
        
    # method that determines the canvas of the next question
    def next_quest(self):
        self.canvas.config(background= "white")
        self.the_score.config(text=f"Score: {self.quiz.score}") 
        # at BrainQuiz the still_has_questions return True if are other question in our data and False if there not
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = f"{self.quiz.question_number}: {q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text = f"You've completed the quiz.Your final score was: {self.quiz.score}/{self.quiz.question_number}")   
            self.false_button["state"]= DISABLED
            self.true_button["state"]= DISABLED
            
    # the command of two buttons false_button return false so we pass it to the 
    # check_answer method to control with the answer of the question 
    def false_btt(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def tru_btt(self):
        self.give_feedback(self.quiz.check_answer("True"))
    
    # the screen returns in eatch color depend of button presses and after 1sek she goes to the other questions    
    def give_feedback(self, is_right):
        # is _right takes the value of the funct that the buttons returns when are pressed
        if is_right:
            self.canvas.config(background= "green") 
        else:
            self.canvas.config(background= "red") 
        self.window.after(1000, self.next_quest)
    

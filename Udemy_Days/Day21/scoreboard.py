from turtle import Turtle, update

#constants
ALIGNMENT = "center"
FONT = ('Arial', 10, 'bold')

class ScoreBoard(Turtle):
    
    #the text of the "Score 0" is as a turtle with its settings
    #here we declare and tha variable points=0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.point = 0
        #declare the highscore as varibale that takes the values from a data.x whitch will mantain the high scores if we close the program
        with open ('data.txt') as file:
            self.highscore = int(file.read())
        self.update_points()

      
  
    #funct only for the message on the screen
    def update_points(self):
        self.clear()
        self.write(f"Score: {self.point} High Score {self.highscore}", align=ALIGNMENT, font=FONT)
    
    #we reset the high score message when the snake collapse with the wall (the other level)
    def reset(self):
        if self.point > self.highscore:
            self.highscore = self.point
            #write the new highscore to the file data.txt to read it if we close the program
            with open ('data.txt', mode='w') as file:
                file.write(f'{self.highscore}')
        self.point = 0
        self.update_points()
        
    
    #this calculate the points of eatch time snake its the food (at tha main program) becouse we call this method     
    def calc_points (self):
        self.point += 1
        self.update_points()
    
    
    
      
    #the text of the game over in the center of the screen
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
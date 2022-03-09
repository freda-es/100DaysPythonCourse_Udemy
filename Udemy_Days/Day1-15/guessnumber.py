import random
from art import logo2
#print(logo2)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


the_number = int(random.choice(range(1,101)))
print(f"Pssst, the correct answer is {the_number}")

diff_choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
difficulty = {
    "hard": 5,
    "easy": 10
}

attempt= difficulty[diff_choose]
def gues_nr ():
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess_number = int(input("Make a guess: "))        
    return guess_number


find_guess = False

while not find_guess:
    the_guess = gues_nr()
    if the_guess == the_number:
        print(f"You got it! The answer was {the_guess }.")
        find_guess = True
    else:
        attempt -= 1
        if attempt > 0:
            if the_guess < the_number:
                print("Too low\nGuess again..")
                find_guess = False
            if the_guess > the_number:
                print("Too high\nGuess again..")
                find_guess = False
        if attempt == 0:
            if the_guess < the_number:
                print("Too low\nYou've run out of guesses, you lose.")
            if the_guess > the_number:
                print("Too high\nYou've run out of guesses, you lose.")
            find_guess = True
        if attempt<0:
            find_guess = True
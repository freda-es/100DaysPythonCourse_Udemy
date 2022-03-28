import random
from hangman_art import logo,stages
from hangman_words import word_list 
from replit import clear

#Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
  
  #Use the clear() function imported from replit to clear the output between guesses.
    clear()
    if guess in display:
        print(f"You've already guessed {guess}")
        
    #relace blanks with the letters
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    #print a message if the letter is not the right one, -1 live for eatch error letter
    if guess not in chosen_word:
       print(f"You guessed {guess}, that's not in word. You lose life")
       lives -= 1  
     
    #print the word and the ascii images for eatch -live
    print(f"{' '.join(display)}")
    print(stages[lives]) 
    
    #determine when you lose
    if lives == 0:
        end_of_game = True
        print("You lose.")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

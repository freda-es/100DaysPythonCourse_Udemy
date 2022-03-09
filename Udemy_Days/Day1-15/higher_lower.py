import random
from art import logo3, vs 
from game_data import data
from replit import clear


def names_compared():
    """Returns a random 'dictionary name' from the list data"""
    name_compared = random.choice(data) 
    return name_compared
      
def print_compare(names_compared):
    """Generate the print message with the data generated random from file data"""
    name = names_compared['name']
    description = names_compared['description']
    country = names_compared['country']
    return f"{name}, a {description}, from {country}"
  
def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess and returns True if they got it right. 
       Or False if they got it wrong.""" 
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def play_game():
    print(logo3)
    score = 0
    game_should_continue = True
    account_a = names_compared()
    account_b = names_compared()
    while game_should_continue:
        account_a = account_b
        account_b = names_compared()
        while account_a == account_b:
            account_b = names_compared()
        print(f"Compare A: {print_compare(account_a)}")
        print(vs)
        print(f"Compare B: {print_compare(account_b)}")
        guess = input("Who has more followers? Type 'A' or 'B':").lower()
        a_followers_nr = account_a['follower_count']
        b_followers_nr = account_b['follower_count']
        correct_answer = check_answer(guess, a_followers_nr,b_followers_nr)
        clear()
        print(logo3)
        if correct_answer:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

play_game()    

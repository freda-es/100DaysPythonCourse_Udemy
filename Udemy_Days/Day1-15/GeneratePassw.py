#Password Generator Project
import random

from numpy import outer
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


easy_passw = ''
hard_passw = ''

#generate a list which concatenates the 3 characters randomized with the input length
passw_randlist = random.choices(letters,k = nr_letters) + random.choices(symbols,k = nr_symbols) + random.choices(numbers,k = nr_numbers)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#generate the easy passw which is not randomized
for charct in passw_randlist:
      easy_passw += charct

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#generate the hard passw- shuffle the main list and than join its elements to have one word      
random.shuffle(passw_randlist)
hard_passw = ''.join(passw_randlist)

print(easy_passw)
print(hard_passw)



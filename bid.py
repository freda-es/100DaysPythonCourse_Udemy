from replit import clear
#HINT: You can call clear() to clear the output in the console.
print('Welcome to the secret auction program.')

# create a dictionary to put the name and the bid of eatch name Key=name, value = bid
name_bid={}

def my_dict (the_name, the_bid):
      name_bid[the_name] = the_bid
   
#create a loop to put the name and the bid until there is no other bidder      
other_bid = True
while other_bid:     
  name = input("What is your name: ")
  bid = int(input("What's your bid: $"))
  my_dict(the_name=name, the_bid=bid)
  other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear()
  if other == 'no':
      other_bid = False

# find the max of value= bid to find the hightest bid whitch is the winner
max = 0
for key in name_bid:
    if name_bid[key]>max:
          max = name_bid[key]
          the_winner = key
    else:
          max = max

#print the messagge for the winner
print(f"The winner is {the_winner} with a bid of ${max}")
        

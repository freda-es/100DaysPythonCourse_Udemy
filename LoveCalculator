print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

count_t = name1.count('t') + name2.count('t')
count_r = name1.count('r') + name2.count('r')
count_u = name1.count('u') + name2.count('u')
count_e = name1.count('e') + name2.count('e')
count_true = count_t + count_r + count_u + count_e

count_l = name1.count('l') + name2.count('l')
count_o = name1.count('o') + name2.count('o')
count_v = name1.count('v') + name2.count('v')
count_e = name1.count('e') + name2.count('e')
count_love = count_l + count_o + count_v + count_e

if count_true == 0:
    percentage = int(count_love)
else:
    percentage = int(str(count_true) + str(count_love))

if percentage < 10 or percentage > 90:
    print(f'Your score is {percentage}, you go together like coke and mentos.')
elif percentage >= 40 and percentage <= 50:
    print(f'Your score is {percentage}, you are alright together.')
else:
    print(f'Your score is {percentage}.')



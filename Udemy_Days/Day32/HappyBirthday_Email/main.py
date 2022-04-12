##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import email
import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
today = now.day
names = []
emails=[]

data_files = pandas.read_csv("Day32\\HappyBirthday_Email\\birthdays.csv")
data_birthdays = data_files.iterrows()
name = {name:email for (name, email) in data_birthdays}
for index in range(len(name)):
    if name[index]['day'] == today:
        names.append(name[index]['name'])
        emails.append(name[index]['email'])
        
        
index_letter = random.randint(1,3)

with open(f"Day32\\HappyBirthday_Email\\letter_templates\\letter_{index_letter}.txt") as letter:
    model_letter = letter.read()
    print(model_letter)
    # with open (f"Day32\\HappyBirthday_Email\\letter_templates\\lettertosend_{index_letter}.txt") as my_letters:
    #     my_letter = model_letter.replace("[NAME]", names[0])
    #     my_letters.write(my_letter)




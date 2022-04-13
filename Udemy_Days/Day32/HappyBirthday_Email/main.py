import datetime as dt
import random
import pandas
import smtplib

#determine the current day and month as a control variable
now = dt.datetime.now()
today = now.day
month = now.month
names_emails = {}

#open the file birthday.csv and make it a dict with the name and the info of the name_row
data_files = pandas.read_csv("Day32\\HappyBirthday_Email\\birthdays.csv")
data_dict = {name:data_row for (name, data_row) in data_files.iterrows()}
#create another dict with the names:emails of the list whitch has the birthday today
for index in range(len(data_dict)):
    if data_dict[index]['day'] == today and data_dict[index]['month'] == month:
        names_emails[data_dict[index]['name']] = data_dict[index]['email']

# ----sending the email-----
my_email = "YOUR MAIL"
passw = "YOUR PASSWORD"

with smtplib.SMTP("smtp.gmail.com") as mail_connect:#connect to your email service
    mail_connect.starttls()#secure our connection
    mail_connect.login(user=my_email, password=passw)
    with open(f"Day32\\HappyBirthday_Email\\letter_templates\\letter_{random.randint(1,3)}.txt") as letter:
        model_letter = letter.read()
        #iterate through the dict that we created and put the name in the letter model and then send it
        for key in names_emails:
            my_letter = model_letter.replace("[NAME]", key)  
            mail_connect.sendmail(
                from_addr=my_email, to_addrs=f"{names_emails[key]}", 
                msg=f"Subject:Happy birthday\n\n{my_letter}"
                )






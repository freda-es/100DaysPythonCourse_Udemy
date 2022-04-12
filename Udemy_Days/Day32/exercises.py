# # ----Sending a simple email from python----

# import smtplib

# my_email = "cookingfamily87@gmail.com"
# passw = "Ansi@Vesa2022"

# with smtplib.SMTP("smtp.gmail.com") as connection:#connect to your email service
#     connection.starttls()#secure our connection
#     connection.login(user=my_email, password=passw)
#     connection.sendmail(
#         from_addr=my_email, to_addrs="fredadyrkaj@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email"
#         )


# ----Datetime module----
# import datetime as dt

# now = dt.datetime.now()#gets the current date and time
# year = now.year #gest the current year

# date_birth = dt.datetime(year=1987,month=7,day=1)

# print(date_birth)


# ---sending email in the current day to ourself with a quote from the quote.txt file---

import smtplib
import datetime as dt
import random

my_list_ofquotes = []
with open("Day32\\quotes.txt") as quotes:
    # for quot in quotes:
    #     my_list_ofquotes.append(quot)    
    my_list_ofquotes = quotes.readlines()
    the_quote = random.choice(my_list_ofquotes) 

       
now = dt.datetime.now()
today = now.weekday()

my_email = "cookingfamily87@gmail.com"
passw = "Ansi@Vesa2022"


with smtplib.SMTP("smtp.gmail.com") as mail_connect:#connect to your email service
    mail_connect.starttls()#secure our connection
    mail_connect.login(user=my_email, password=passw)
    if today == 1:
        mail_connect.sendmail(
            from_addr=my_email, to_addrs="cookingfamily87@gmail.com", 
            msg=f"Subject:Today Quote\n\n{the_quote}"
            )







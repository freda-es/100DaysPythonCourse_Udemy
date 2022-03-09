from operator import is_


def is_leap(year):
 if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return False
      else:
        return True
    else:
      return False
 else:
    return True

def days_in_month(year, the_month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) == False:
    return month_days[the_month-1]
  if is_leap(year)  == True:
    month_days[1] = 29
    return month_days[the_month-1]
        
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
is_leap(year=year)
days = days_in_month(year=year, the_month=month)
print(days)













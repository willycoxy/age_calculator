#Age Calculator
import datetime
from datetime import date

# Ask for users birth year, birth month, birthdate 
year = int(input("Please enter birth your year. "))
month = int(input("Please enter birth your month. "))
day = int(input("Please enter the day you were born. "))  

# Coverents inputs into proper format
date1 = datetime.date(year, month, day)

# Get todays date
today = date.today()

# Gets your current age
age = today.year - date1.year

# Checks if birthday has passed this year
if (today.month, today.day) < (date1.month, date1,day):
    age -= 1

print(f"You are {age} years old, ")


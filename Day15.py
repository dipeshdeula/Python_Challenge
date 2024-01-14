#create a simple Clock
#Time module
#There is a built-in module in python named time. it has a lot of time-related functionalities. 
#One function on the time module is called sleep
#The sleep takes a paramter named sec

# import time

# while True:
#     time.sleep(1)
#     print("Tick")

# import time
# print('Simple clock:\n')

# hour = int(input("Type in the current hour:"))
# minute = int(input("Type in the current minute:"))
# second = int(input("Type in the current second:"))

# def display():
#     print(hour,':',minute,':',second)

# def add():
#     global hour
#     global minute
#     global second

#     second=second+1
#     if second == 60:
#         minute = minute +1
#         second = 0
    
#     if minute == 60:
#         hour = hour + 1
#         minute=0
    
#     if hour==24:
#         hour=0

# print('\n')

# while True:
#     time.sleep(1)
#     add()
#     display()

#calculate how many days are remaining for the next birthday

from datetime import datetime

def get_user_birthday():
    date_str = input("Enter your birth date in DD/MM/YYYY:")
    try:
        birthday = datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        # Handle the case where the entered date is not in the correct format
        print("Invalid date format. Please enter the date in DD/MM/YYYY.")
        return get_user_birthday()  # Recursively call the function to get a valid input
    return birthday

def days_remaining(birth_date):
    now = datetime.now()
    current_year_birthday = datetime(now.year, birth_date.month, birth_date.day)

    if current_year_birthday < now:
        # If birthday has already occurred this year, calculate days remaining for next year
        next_year_birthday = datetime(now.year + 1, birth_date.month, birth_date.day)
        days = (next_year_birthday - now).days
    else:
        # If birthday is yet to occur this year, calculate days remaining for the current year
        days = (current_year_birthday - now).days

    return days

birthday = get_user_birthday()
next_birthday = days_remaining(birthday)
print("Your birthday is coming in:", next_birthday, "days")

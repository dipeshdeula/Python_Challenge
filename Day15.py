#create a simple Clock
#Time module
#There is a built-in module in python named time. it has a lot of time-related functionalities. 
#One function on the time module is called sleep
#The sleep takes a paramter named sec

# import time

# while True:
#     time.sleep(1)
#     print("Tick")

import time
print('Simple clock:\n')

hour = int(input("Type in the current hour:"))
minute = int(input("Type in the current minute:"))
second = int(input("Type in the current second:"))

def display():
    print(hour,':',minute,':',second)

def add():
    global hour
    global minute
    global second

    second=second+1
    if second == 60:
        minute = minute +1
        second = 0
    
    if minute == 60:
        hour = hour + 1
        minute=0
    
    if hour==24:
        hour=0

print('\n')

while True:
    time.sleep(1)
    add()
    display()
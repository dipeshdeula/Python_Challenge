# #for loop 
# basket = ['apple','banana','strawberry','grapes','mango']
# fruit=basket.sort()

# for fruit in basket:
#     print(fruit)

# #condition in for loop
# num=[1,2,3,-1,4,5,6,7]

# for nums in num:
#     if(nums>5):
#         print(nums)

# #break in l00p 
# for num1 in num:
#     if(num1<0):
#         break
#     print(num1)

# #continue keyword helps to skip some element from the list
#     num2=[1,2,3,4,5,6,7,8,9,10]
#     for i in num2:
#         if(i==5 or i==7):
#             continue
#         print(i)
# #break will stop immediately . Continue will skip the current iteration
# #continue will skip the rest part of the current iteration

#The range() function can take up to three parameters:range(start,stop,step)
# for n in range(1,5,6):
#     print(n)

#range(stop)
# for n in range(3):
#     print(n)

# This loop iterates on the value of the "n" variable in a range
# of 0 to 10 (the value of the end-of-range index 11 is excluded).
# The incremental value for the loop is 2. The print() function will 
# output the resulting value of "n" as the loop counts from 0 to 10 
# (end-of-range index 11) in incremental steps of 2. This is one 
# method that can be used in Python to print a list of even numbers.


# for n in range(0,11,2):
#     print(n)


# The loop should print 0, 2, 4, 6, 8, 10


# This loop iterates on the value of the "number" variable in a range
# of 2 to 7+1 (the value of the end-of-range index 7 is excluded, so 
# +1 has been added to the parameter to include the numeric value 7 in 
# the range). The incremental value for the loop is the default of +1.
# The print() function will output the resulting value of "number" 
# multiplied by 3.


# for number in range(2,7+1):
#     print(number*3)


# The loop should print 6, 9, 12, 15, 18, 21
    
# This loop iterates on the value of the "x" variable in a range
# of 2 to -1 (the end-of-range index -2 is excluded). The third 
# parameter is also a negative number, making it a decremental value
# of -1. The print() function will output the resulting value of
# "x" as it starts at 2 and counts down to -1 (index -2).


# for x in range(2, -2, -1):
#     print(x)


# The loop should print 2, 1, 0, -1
    
# The roles of the range(start, stop, step) function parameters are:

# Start - Beginning of range

# value included in range

# default = 0

# Stop - End of range

# value excluded from range (to include, use stop+1)

# no default

# must provide the ending index number 

# Step - Incremental value 

# default = 1
    
#nested for loop

# for left in range(7):
#     for right in range(left,7):
#         print("[" + str(left)+ "|"+str(right)+']',end=" ")
#     print()

# teams=['Dragons','Wolves','Pandas','Unicorns']
# for home_team in teams:
#     for away_team in teams:
#         if home_team != away_team:
#             print(home_team + " Vs " + away_team)

# def greet_friends(friends):
#     for friend in friends:
#         print("Hello "+friend)
# greet_friends(["Ram","hari","sita"])

#factorial
# def factorial(n):
#     result=1
#     for x in range(1,n+1):
#         result=result * x
#     return result
# for n in range(1,10):
#     print(n,factorial(n))

#write a script that prints the first 10 cube number(x**3),starting with x=1 and ending with x=10

# for x in range(1,10):
#     print(pow(x,3))

#write a script that prints the multiples of 7 between 0 and 100 . print one multiple per line and avoid
#printing any numbers that aren't multiples of 7. Remember that 0 is also multiple of 7

# for i in range(0,101,7):
#     print(i)

#The retry function tries to execute an operation that might fail,it retries the operation for a number of attempts.
#currently the code will keep executing the function even if it succeeds.

# def retry(operation,attempts):
#     for n in range(attempts):
#         if operation():
#             print("Attempt"+str(n)+"succeeded")
#             break
#         else:
#             print("Attempt"+str(n)+"failed")
# retry(create_user,3)
# retry(stop_service,5)
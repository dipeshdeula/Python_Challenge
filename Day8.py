#practice session

#Take two inputs from the user. one will be an integer. The other will be a float number.Then multiply them to display the output

# num1=float(input("Enter a float number"))
# num2=int(input("Enter the integer num"))

# mul=num1*num2
# print(mul)

#Take two numbers from the users. calculate the result of second number power of the first number
# first_num=3
# second_num=4
# #power=pow(second_num,first_num)
# power=second_num**first_num
# print(power)

# def power():
#     base = int(input('Please enter the base number: '))
#     exponent = int(input('Please enter the exponent: '))
#     result = pow(base,exponent)
#     print(result)
# power()

#create a random number between 0 to 10
# import random
# random_num=random.randint(0,10)
# random_num2=random.randint(5,9)
# print(random_num)
# print(random_num2)

#find the floor division of two number
#floor division means the integer part of a division operation.
#for example, if you divide 17/5 the quotient will be 3.4
#here the integer part is 3
#so you have to find the integer part of the division operation
# // helps to provide floor divison
# num1=17
# num2=5
# division=(num1//num2)
# div_int=int(num1/num2)
# print(division)

#alternative method
#if you pass a number with a fraction to the math.floor function, it will return you the integer part of the number
# import math
# result=math.floor(3.4)
# print(result)

# import math
# num1=int(input("Enter the first Number:"))
# num2=int(input("Enter the second Number:"))
# floor_division=math.floor(num1/num2)
# print(floor_division)


#swap two variables
#To swap two variables: the value of the first variable will become the value of the second variable.
#On the other hand,the value of the second variable will become the value of the first variable
#Here we can use third variable temp to hold the value of the first variable and then assign 

# first_value=int(input("Enter the First Value:"))
# second_value=int(input("Enter the Second value:"))
# temp = first_value
# first_value = second_value
# second_value = temp
# print("The new values are :",first_value,"and",second_value)

#you can use a python shortcut to swap two variable as well

# x=12
# y=13
# print('Before swapping x=',x,'and y=',y)
# #swap this two
# x, y = y, x
# print('After swapping x=',x,'and y=',y)

# #another solution for swapping two values
# a=5
# b=7
# print('Before swapping a=',a,'and b=',b)
# #swap this two without using third variable
# a=a+b
# b=a-b
# a=a-b
# print('After swapping a',a , 'and b=',b)

#find the largest of two numbers

# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number"))
# num3=int(input("Enter the third number:"))
# if(num1>num2):
#     print("This is largest number is :",num1)
# else:
#     print("This is larges number is :",num2)

# #another method
# largest=max(num1,num2)
# print("Largest number is:",largest)

#alernative solution

# if(num1-num2>0):
#     print("The bigger number is:",num1)
# else:
#     print("The bigger number is:",num2)

#find the largest of three number
# if(num1>=num2 and num3):
#     print("The laragest number is :",num1)
# elif(num2>=num3 and num1):
#     print("The largest number is :",num2)
# else:
#     print("The largest number is :",num3)

#another way
#declare first number as the larges

# largest=num1
# if(num2>=num1)and (num2>=num3):
#     largest=num2
# elif(num3>=num1) and (num3>=num2):
#     largest=num3
# else:
#     largest=num1
# print("Largest number you entered is:",largest)

#alernative method using max keyword

# largest=max(num1,num2,num3)
# print("Largest number you have entered is:",largest)

# #Take numbers from a user and show the average of the numbers the user entered
# sum=num1+num2+num3
# avg=sum/3
# print("The average number is :",avg)

#another way
# len=int(input("How many number you want to enter"))
# nums =[]
# for i in range(0,len):
#     element=int(input("Enter element:"))
#     nums.append(element)
# total=sum(nums)
# average=total/len
# print("Average of all elements are ",average)  
    
#another apporach
# len=int(input("How many number you want to enter"))
# total = 0

# for i in range(0,len):
#     element=int(input("Enter the element:"))
#     total+=element
# avg=total/len
# print("The Average value is:",avg)

#The Problem

# For a given number, find all the numbers smaller than the number. Numbers should be divisible by 3 and also by 5

# def divisible_by_3and5(num):
#     result=[]
#     for i in range(0,num):
#         if (i%3==0 and i%5==0):
#             element=int(input("enter the elment"))
#             result.append(element)
            
#         return result
# num=int(input("Enter your number"))
# result=divisible_by_3and5(num)
# print(result)

#another approach
# numbers=[1,5,10,15,12]
# for i in numbers:
#     if i%3==0 and i%5==0:
#         print(i,"is divisible by both 3 and 5")
#         min_num=min(numbers)
# print(min_num)

#another one form dani baba

# num=int(input("Insert the number"))
# result=[]
# i=1

# while i<=num:
#     if i%3==0 and i%5==0:
#         result.append(i)
#     i=i+1
# print(result)

#For a given number, find the sum of every digit
def sum_of_digits(num):
    sum=0
    while(num>0):
        last_digit=num%10
        sum+=last_digit
        num//=10
    return sum
user_num=int(input("Enter a number:"))
total=sum_of_digits(user_num)
print("The total sum of digits is:",total)


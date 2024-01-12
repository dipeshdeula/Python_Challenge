#practice session
#check whether the string is palindrome

# def check_palindrome(string):
   
#     reversed_str = string[::-1]  #reversing

#     if string==reversed_str:
#         print("The given string is a Palindrome.")
#     else:
#         print("The given String is not palindrome")
# usr_str=input("Enter the string")
# check_palindrome(usr_str)

# with a given integral number n , write a program to calculate the sum of cubes

# def calculate_sum_cube(num):
#     sum=0
#     for n in range(num + 1):
#        sum=sum+n**3
#     return sum
# usr_num=int(input("Enter the number:"))
# print("Sum of Cubes from 1 to",usr_num,"is :",calculate_sum_cube(usr_num))

#another solution
# n = int(input("Enter the number:"))
# sum=(n*(n+1)/2)**2
# print("Sum of CUBES from 1 to",n,"is :",sum)

#check whether a number is an amstrong or not
# def check_amstrong(num):
#     num_str=str(num)
#     length=len(num_str)
#     temp=num
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=digit**length
#         temp//=10
#     if num == sum:
#         return True
#     else:
#         return False
    
# usr_num=int(input("Enter the number:"))
# if check_amstrong(usr_num):
#     print("The Given Number Is An Amstrong Number ")
# else:
#     print("The Given Number Is Not An Amstrong Number")

#calculate the greatest common divisor (gcd) of two numbers
#In mathematics, the greatest common divisor (gcd) of two or more integer is the largest positive integer
#that divides each of the integers

#For example, the gcd of 8 and 12 is 4, because 4 is the largest number that divides both 8 and 12 .
#similarly, 15 is the gcd of 15 and 45. Because 15 divides both 15 and 45
# def gcd(a , b):
#     while(b):
#         a, b = b, a % b
#     return a
# x = int(input('Enter first number: '))
# y = int(input('Enter Second number:'))
# print('GCD of', x,'and', y,'is', gcd(x, y))

# #another solution
# def comupte_gcd(x,y):
#     smaller = min(x,y)
#     gcd = 1
#     for i in range(1,smaller + 1):
#         if((x % i==0) and (y % i==0)):
#             gcd = i
#     return gcd

# num1=int(input("Enter First number:"))
# num2=int(input("Enter Second number:"))

# gcd = comupte_gcd(num1,num2)
# print("GCD of",num1,"and",num2,"is:",gcd)

#Recursive method for GCD

# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# GCD=gcd(a,b)
# print("The GCD of",a,"and",b,"is",GCD)

#built-in GCD
#python has a built-in method to calculate gcd

# import math
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))

# gcd=math.gcd(a,b)
# print("The GCD of",a,"and",b,"is",gcd)

#calculate lowest common factor
# import math
# def lcm(x,y):
#     lcm=(x*y)//math.gcd(x,y)
#     return lcm
# A=int(input("Enter the first number:"))
# B=int(input("Enter the second number:"))
# C=lcm(A,B)
# print("The LCM of",A,"and",B,"is",C)

# import math
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# LCM=math.lcm(a,b)
# print("The LCM of",a,"and",b,"is",LCM)

# #calculate highest common factor
# def hcf(x,y):
#     while(y):
#         x, y = y, x % y
#     return x
# HCF=hcf(12, 8)
# print("The HCF of 12 and 8 is ", HCF)


#Guess Game problem
# import random
# print('To stop anytime:q')
# score=0
# while True:
#     num=random.randint(1,10)
#     guess=input("Guess a number between 1-10:")
#     if guess=='q':
#         print('Game over.')
#         break
#     guess_num=int(guess)
#     if guess_num is num:
#         print("CONGRATS, you guessed it correctly..!")
#         score+=10
#         print('Your new score:',score)

#     else:
#         print("your guess did not match:")
#         print('The number was:',num)


#Rock , paper , Scissor game
# def getUserChoice(user1_choice,user2_choice): 
#     if user1_choice == user2_choice :
#         return "Draw"
#     elif user1_choice() == 'p' and user2_choice()== 'r':
#         return "user1_choice win"
#     elif user1_choice() == 's' and user2_choice()=='p':
#         return "user1-choice win"
#     elif user1_choice() == 'r' and user2_choice()=='s':
#         return "user1_choice win"
#     elif user2_choice() == 'p' and user1_choice()=='r':
#         return "user2_choice win"
#     elif user2_choice() == 's' and user1_choice() =='p':
#         return "user2_choice win"
#     elif user2_choice() == 'r' and user2_choice()=='s':
#         return 'user2_choice win'
#     else:
#         return 'Invalid input'
    
# user1_choice=input("\n Enter your choice (r/p/s):").lower
# user2_choice=input("\n Enter your choice(r/p/s):").lower
# choices=getUserChoice(user1_choice,user2_choice)
# print(choices)


#create a bulls and cows game
#The cows and bulls is a number guessing game. In this game, the user guesses a number. Usually,the number will be
# 4 digit number. However,here we will try with 2 digits number first so, if the user guesses the number correctly
#he/she will win. if they didn't guess the exact number,then you will calculate the bulls and cows

import random

secret_number=str(random.randint(10,99))
print("Welcome to Bulls And Cows Game.\n")
print("You have to guess a secret number between 10 and 99.\n")

score=0
remaining_try = 7
while remaining_try>0:
    player_guess = input("Enter your guess:")
    if player_guess == secret_number:
        score=score+10
        print("Yay, you guessed it!")
        print("YOU WIN! and got a ",score,"points!!")
        break
    else:
        bulls=0
        cows=0

        if player_guess[0] == secret_number[0]:
            bulls += 1
        if player_guess[1] == secret_number[1]:
            bulls +=1
        if player_guess[0] == secret_number[1]:
            cows+=1
        if player_guess[1] == secret_number[0]:
            cows+=1
        print("BULLS:",bulls)
        print("COWS:",cows)
        

        remaining_try-=1
       

        if remaining_try<1:
            print("You lost the game.")
            print("The secret number is:",secret_number)
            break




        